"""Direct asynchronous Linear API access. No persistence or implicit retries."""
from __future__ import annotations

import asyncio
import math
from collections.abc import Callable
from typing import Any, Literal, TypeVar

import httpx

from ._documents import DOCUMENTS
from .models import Comment, Issue, IssueCreate, IssueFilter, IssueUpdate, Page, Reference

ENDPOINT = "https://api.linear.app/graphql"
T = TypeVar("T")


class LinearError(Exception):
    """Safe error metadata; provider bodies and credentials are never attached."""

    def __init__(self, kind: str, *, outcome_unknown: bool = False,
                 status: int | None = None, retry_after: float | None = None,
                 rate_limit_reset_ms: int | None = None):
        self.kind = kind
        self.outcome_unknown = outcome_unknown
        self.status = status
        self.retry_after = retry_after
        self.rate_limit_reset_ms = rate_limit_reset_ms
        super().__init__(f"Linear {kind} error" + ("; mutation outcome unknown" if outcome_unknown else ""))


def _text(value: Any, *, nullable: bool = False) -> str | None:
    if nullable and value is None:
        return None
    if not isinstance(value, str):
        raise ValueError("expected string")
    return value


def _node(data: dict, key: str) -> dict:
    value = data[key]
    if value is None:
        raise LinearError("not_found")
    if not isinstance(value, dict):
        raise ValueError("invalid object")
    return value


def _issue(v: dict) -> Issue:
    return Issue(_text(v["id"]), _text(v["identifier"]), _text(v["title"]),
                 _text(v["description"], nullable=True), _text(v["url"]), _text(v["updatedAt"]))


def _comment(v: dict) -> Comment:
    return Comment(_text(v["id"]), _text(v["body"]), _text(v["createdAt"]))


def _reference(v: dict) -> Reference:
    return Reference(_text(v["id"]), _text(v["name"]))


def _page(v: dict, parse: Callable[[dict], T]) -> Page[T]:
    info = v["pageInfo"]
    cursor = _text(info["endCursor"], nullable=True)
    more = info["hasNextPage"]
    if type(more) is not bool or not isinstance(v["nodes"], list) or (more and not cursor):
        raise ValueError("invalid page")
    return Page(tuple(parse(item) for item in v["nodes"]), cursor, more)


def _id(value: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("nonempty identifier required")
    return value


def _pagination(first: int, after: str | None) -> dict:
    if type(first) is not int or not 1 <= first <= 100:
        raise ValueError("page size must be between 1 and 100")
    return {"first": first, "after": _id(after) if after is not None else None}


def _input(value: dict, *, create: bool) -> dict:
    allowed = {"title", "description", "stateId", "assigneeId", "priority"}
    if create:
        allowed.add("teamId")
    if not isinstance(value, dict) or not value or value.keys() - allowed:
        raise ValueError("unsupported or empty issue input")
    if create and not {"teamId", "title"} <= value.keys():
        raise ValueError("teamId and title required")
    for key, item in value.items():
        if key == "priority":
            if type(item) is not int or not 0 <= item <= 4:
                raise ValueError("priority must be an integer between 0 and 4")
        elif item is None and not create and key in {"description", "assigneeId"}:
            continue
        elif not isinstance(item, str) or (key != "description" and not item.strip()):
            raise ValueError("invalid issue field")
    result = dict(value)
    # Linear ignores null for this document field; an empty string clears it.
    if not create and "description" in result and result["description"] is None:
        result["description"] = ""
    return result


def _number(headers: httpx.Headers, name: str, cast: Callable) -> Any:
    try:
        value = cast(headers[name])
        return value if math.isfinite(value) and value >= 0 else None
    except (KeyError, ValueError, OverflowError):
        return None


class LinearClient:
    """One caller-owned credential, fixed HTTPS endpoint, explicit resource lifetime.

    A custom transport is a trusted test/deployment hook. Cancellation of a write
    is uncertain; it propagates to the caller. No operation is automatically retried.
    """

    def __init__(self, token: str, *, auth: Literal["oauth", "api_key"] = "oauth",
                 timeout: float = 30, transport: httpx.AsyncBaseTransport | None = None):
        if auth not in {"oauth", "api_key"}:
            raise ValueError("unsupported authentication type")
        if not isinstance(token, str) or not token or not all(33 <= ord(c) <= 126 for c in token):
            raise ValueError("invalid credential")
        if not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or timeout <= 0:
            raise ValueError("positive finite timeout required")
        self._timeout = timeout
        self._http = httpx.AsyncClient(
            headers={"Authorization": f"Bearer {token}" if auth == "oauth" else token},
            timeout=timeout, transport=transport, follow_redirects=False, trust_env=False,
        )

    async def __aenter__(self) -> LinearClient:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        await self._http.aclose()

    async def _call(self, operation: str, variables: dict, parse: Callable[[dict], T]) -> T:
        document = DOCUMENTS[operation]
        mutation = document.startswith("mutation ")
        try:
            async with asyncio.timeout(self._timeout):
                response = await self._http.post(ENDPOINT, json={
                    "operationName": operation, "query": document, "variables": variables,
                })
        except (TimeoutError, httpx.TimeoutException):
            raise LinearError("timeout", outcome_unknown=mutation) from None
        except httpx.DecodingError:
            raise LinearError("protocol", outcome_unknown=mutation) from None
        except httpx.RequestError:
            raise LinearError("transport", outcome_unknown=mutation) from None
        status = response.status_code
        meta = {"status": status, "outcome_unknown": mutation}
        if status in {401, 403}:
            raise LinearError("authentication", **meta)
        if status == 429:
            raise LinearError("rate_limit", **meta,
                              retry_after=_number(response.headers, "retry-after", float),
                              rate_limit_reset_ms=_number(response.headers, "x-ratelimit-requests-reset", int))
        try:
            root = response.json()
        except ValueError:
            raise LinearError("protocol" if response.is_success else "http", **meta) from None
        if not isinstance(root, dict):
            raise LinearError("protocol", **meta)
        errors = root.get("errors")
        if errors is not None and not isinstance(errors, list):
            raise LinearError("protocol", **meta)
        if errors:
            codes = set()
            for error in errors:
                if isinstance(error, dict) and isinstance(error.get("extensions"), dict):
                    code = error["extensions"].get("code")
                    if isinstance(code, str):
                        codes.add(code)
            kind = "rate_limit" if "RATELIMITED" in codes else "graphql"
            if codes & {"AUTHENTICATION_ERROR", "FORBIDDEN", "UNAUTHENTICATED"}:
                kind = "authentication"
            elif codes & {"GRAPHQL_VALIDATION_FAILED", "BAD_USER_INPUT"}:
                kind = "validation"
            raise LinearError(kind, **meta,
                              retry_after=_number(response.headers, "retry-after", float),
                              rate_limit_reset_ms=_number(response.headers, "x-ratelimit-requests-reset", int))
        if not response.is_success:
            raise LinearError("http", **meta)
        try:
            if not isinstance(root.get("data"), dict):
                raise ValueError("missing data")
            return parse(root["data"])
        except (KeyError, TypeError, ValueError):
            raise LinearError("protocol", **meta) from None

    async def viewer(self) -> Reference:
        return await self._call("Viewer", {}, lambda d: _reference(d["viewer"]))

    async def get_issue(self, issue_id: str) -> Issue:
        return await self._call("GetIssue", {"id": _id(issue_id)}, lambda d: _issue(_node(d, "issue")))

    async def list_issues(self, *, first: int = 50, after: str | None = None,
                          filters: IssueFilter | None = None) -> Page[Issue]:
        values = _pagination(first, after)
        filters = filters or IssueFilter()
        values["filter"] = {k: {"id": {"eq": _id(v)}} for k, v in (
            ("team", filters.team_id), ("assignee", filters.assignee_id), ("state", filters.state_id)
        ) if v is not None}
        return await self._call("ListIssues", values, lambda d: _page(d["issues"], _issue))

    async def create_issue(self, value: IssueCreate) -> Issue:
        return await self._call("CreateIssue", {"input": _input(value, create=True)},
                                lambda d: self._mutation(d["issueCreate"], "issue", _issue))

    async def update_issue(self, issue_id: str, patch: IssueUpdate) -> Issue:
        return await self._call("UpdateIssue", {"id": _id(issue_id), "input": _input(patch, create=False)},
                                lambda d: self._mutation(d["issueUpdate"], "issue", _issue))

    @staticmethod
    def _mutation(value: dict, field: str, parse: Callable[[dict], T]) -> T:
        if value["success"] is False:
            raise LinearError("rejected")
        if value["success"] is not True:
            raise ValueError("invalid mutation success flag")
        return parse(value[field])

    async def list_comments(self, issue_id: str, *, first: int = 50,
                            after: str | None = None) -> Page[Comment]:
        return await self._call("ListComments", {"id": _id(issue_id), **_pagination(first, after)},
                                lambda d: _page(_node(d, "issue")["comments"], _comment))

    async def create_comment(self, issue_id: str, body: str) -> Comment:
        if not isinstance(body, str) or not body.strip():
            raise ValueError("nonempty comment required")
        return await self._call("CreateComment", {"input": {"issueId": _id(issue_id), "body": body}},
                                lambda d: self._mutation(d["commentCreate"], "comment", _comment))

    async def list_teams(self, *, first: int = 50, after: str | None = None) -> Page[Reference]:
        return await self._call("ListTeams", _pagination(first, after), lambda d: _page(d["teams"], _reference))

    async def list_states(self, team_id: str, *, first: int = 50,
                          after: str | None = None) -> Page[Reference]:
        return await self._call("ListStates", {"id": _id(team_id), **_pagination(first, after)},
                                lambda d: _page(_node(d, "team")["states"], _reference))

    async def list_users(self, *, first: int = 50, after: str | None = None) -> Page[Reference]:
        return await self._call("ListUsers", _pagination(first, after), lambda d: _page(d["users"], _reference))
