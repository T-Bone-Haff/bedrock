"""Direct asynchronous Linear API access. No persistence or implicit retries."""
from __future__ import annotations

import asyncio
import math
from collections.abc import Callable
from typing import Any, Literal, TypeVar
from uuid import UUID

import httpx

from ._documents import DOCUMENTS
from .models import (Comment, CommentAttribution, Issue, IssueContext, IssueCreate,
                     IssueFilter, IssueRelation, IssueUpdate, Page, Reference, WorkflowState)

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


def _identity(v: dict | None, *, nullable: bool = False) -> str | None:
    if v is None and nullable:
        return None
    return _id(v["id"])


def _bound_node(v: dict, expected: str) -> dict:
    identity = _identity(v)
    if identity.casefold() != expected.casefold():
        identifier = v.get("identifier")
        if not isinstance(identifier, str) or identifier.casefold() != expected.casefold():
            raise ValueError("mismatched issue identity")
    return v


def _issue(v: dict) -> Issue:
    priority = v["priority"]
    if type(priority) not in (int, float) or priority not in range(5):
        raise ValueError("invalid priority")
    state = v["state"]
    context = IssueContext(
        _identity(v["team"]), WorkflowState(_identity(state), _text(state["name"]), _text(state["type"])),
        int(priority), _identity(v["assignee"], nullable=True), _identity(v["parent"], nullable=True),
        _text(v["dueDate"], nullable=True), _text(v["archivedAt"], nullable=True),
        _text(v["completedAt"], nullable=True), _identity(v["creator"], nullable=True),
    )
    return Issue(_identity(v), _text(v["identifier"]), _text(v["title"]),
                 _text(v["description"], nullable=True), _text(v["url"]), _text(v["updatedAt"]), context)


def _comment(v: dict, expected_issue: str) -> Comment:
    issue = _bound_node(v["issue"], expected_issue)
    return Comment(_identity(v), _text(v["body"]), _text(v["createdAt"]),
                   CommentAttribution(_identity(issue), _identity(v["user"], nullable=True)))


def _relation(v: dict) -> IssueRelation:
    return IssueRelation(_uuid(v["id"]), _id(v["type"]), _uuid(_identity(v["issue"])),
                         _uuid(_identity(v["relatedIssue"])), _text(v["archivedAt"], nullable=True))


def _uuid(value: str) -> str:
    value = _id(value)
    try:
        parsed = UUID(value)
    except ValueError:
        raise ValueError("canonical UUID required") from None
    if str(parsed) != value.lower():
        raise ValueError("canonical UUID required")
    return str(parsed)


def _archive(value: bool) -> bool:
    if type(value) is not bool:
        raise ValueError("include_archived must be boolean")
    return value


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
    allowed = {"title", "description", "stateId", "assigneeId", "priority", "parentId"}
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
        elif item is None and not create and key in {"description", "assigneeId", "parentId"}:
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
        return await self._call("GetIssue", {"id": _id(issue_id)}, lambda d: _issue(_bound_node(_node(d, "issue"), issue_id)))

    async def list_issues(self, *, first: int = 50, after: str | None = None,
                          filters: IssueFilter | None = None, include_archived: bool = False) -> Page[Issue]:
        values = _pagination(first, after)
        values["includeArchived"] = _archive(include_archived)
        filters = filters or IssueFilter()
        values["filter"] = {k: {"id": {"eq": _id(v)}} for k, v in (
            ("team", filters.team_id), ("assignee", filters.assignee_id), ("state", filters.state_id)
        ) if v is not None}
        parent_id = _uuid(filters.parent_id) if filters.parent_id is not None else None
        if parent_id is not None:
            values["filter"]["parent"] = {"id": {"eq": parent_id}}
        def parse(v: dict) -> Issue:
            issue = _issue(v)
            if parent_id is not None and issue.context.parent_id != parent_id:
                raise ValueError("mismatched parent")
            return issue
        return await self._call("ListIssues", values, lambda d: _page(d["issues"], parse))

    async def create_issue(self, value: IssueCreate) -> Issue:
        return await self._call("CreateIssue", {"input": _input(value, create=True)},
                                lambda d: self._mutation(d["issueCreate"], "issue", _issue))

    async def update_issue(self, issue_id: str, patch: IssueUpdate) -> Issue:
        return await self._call("UpdateIssue", {"id": _id(issue_id), "input": _input(patch, create=False)},
                                lambda d: self._mutation(d["issueUpdate"], "issue",
                                                         lambda v: _issue(_bound_node(v, issue_id))))

    @staticmethod
    def _mutation(value: dict, field: str, parse: Callable[[Any], T]) -> T:
        if value["success"] is False:
            raise LinearError("rejected")
        if value["success"] is not True:
            raise ValueError("invalid mutation success flag")
        return parse(value[field])

    async def list_comments(self, issue_id: str, *, first: int = 50,
                            after: str | None = None) -> Page[Comment]:
        def parse(d: dict) -> Page[Comment]:
            issue = _bound_node(_node(d, "issue"), issue_id)
            return _page(issue["comments"], lambda v: _comment(v, issue["id"]))
        return await self._call("ListComments", {"id": _id(issue_id), **_pagination(first, after)}, parse)

    async def create_comment(self, issue_id: str, body: str) -> Comment:
        if not isinstance(body, str) or not body.strip():
            raise ValueError("nonempty comment required")
        return await self._call("CreateComment", {"input": {"issueId": _id(issue_id), "body": body}},
                                lambda d: self._mutation(d["commentCreate"], "comment",
                                                         lambda v: _comment(v, issue_id)))

    async def list_teams(self, *, first: int = 50, after: str | None = None) -> Page[Reference]:
        return await self._call("ListTeams", _pagination(first, after), lambda d: _page(d["teams"], _reference))

    async def list_states(self, team_id: str, *, first: int = 50,
                          after: str | None = None) -> Page[Reference]:
        return await self._call("ListStates", {"id": _id(team_id), **_pagination(first, after)},
                                lambda d: _page(_node(d, "team")["states"], _reference))

    async def list_users(self, *, first: int = 50, after: str | None = None) -> Page[Reference]:
        return await self._call("ListUsers", _pagination(first, after), lambda d: _page(d["users"], _reference))


    async def list_issue_labels(self, issue_id: str, *, first: int = 50,
                                after: str | None = None, include_archived: bool = False) -> Page[Reference]:
        issue_id = _uuid(issue_id)
        values = {"id": issue_id, **_pagination(first, after), "includeArchived": _archive(include_archived)}
        return await self._call("ListIssueLabels", values,
                                lambda d: _page(_bound_node(_node(d, "issue"), issue_id)["labels"], _reference))

    async def list_relations(self, issue_id: str, *, direction: Literal["outgoing", "incoming"],
                             first: int = 50, after: str | None = None,
                             include_archived: bool = False) -> Page[IssueRelation]:
        issue_id = _uuid(issue_id)
        if direction not in ("outgoing", "incoming"):
            raise ValueError("unsupported relation direction")
        outgoing = direction == "outgoing"
        operation, field = ("ListOutgoingRelations", "relations") if outgoing else ("ListIncomingRelations", "inverseRelations")
        def parse_relation(v: dict) -> IssueRelation:
            edge = _relation(v)
            if (edge.issue_id if outgoing else edge.related_issue_id) != issue_id:
                raise ValueError("mismatched relation endpoint")
            return edge
        values = {"id": issue_id, **_pagination(first, after), "includeArchived": _archive(include_archived)}
        return await self._call(operation, values,
                                lambda d: _page(_bound_node(_node(d, "issue"), issue_id)[field], parse_relation))

    async def create_relation(self, issue_id: str, related_issue_id: str, *,
                              type: Literal["blocks", "related"]) -> IssueRelation:
        issue_id, related_issue_id = _uuid(issue_id), _uuid(related_issue_id)
        if type not in ("blocks", "related") or issue_id == related_issue_id:
            raise ValueError("unsupported relation type or identical endpoints")
        def parse(v: dict) -> IssueRelation:
            edge = _relation(v)
            if (edge.issue_id, edge.related_issue_id, edge.type) != (issue_id, related_issue_id, type):
                raise ValueError("mismatched relation result")
            return edge
        return await self._call("CreateRelation", {"input": {
            "issueId": issue_id, "relatedIssueId": related_issue_id, "type": type,
        }}, lambda d: self._mutation(d["issueRelationCreate"], "issueRelation", parse))

    async def delete_relation(self, relation: IssueRelation) -> str:
        """Delete a caller-selected observed edge and return its acknowledged UUID.

        The caller binds this record to current authority; this is not an atomic
        precondition. A fresh population read must separately verify absence.
        """
        if not isinstance(relation, IssueRelation) or relation.type not in ("blocks", "related"):
            raise ValueError("supported observed relation required")
        relation_id = _uuid(relation.id)
        if _uuid(relation.issue_id) == _uuid(relation.related_issue_id):
            raise ValueError("identical relation endpoints")
        def parse(identity: str) -> str:
            if _uuid(identity) != relation_id:
                raise ValueError("mismatched deleted identity")
            return relation_id
        return await self._call("DeleteRelation", {"id": relation_id},
                                lambda d: self._mutation(d["issueRelationDelete"], "entityId", parse))
