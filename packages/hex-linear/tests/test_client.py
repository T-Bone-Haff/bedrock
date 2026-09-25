import asyncio
import json
import traceback

import httpx
import pytest

from hex_linear import LinearClient, LinearError, IssueFilter

TOKEN = "synthetic-token-for-tests"
ISSUE = dict(id="issue-id", identifier="TEST-1", title="Example", description="Before",
             url="https://linear.app/example/issue/TEST-1", updatedAt="2020-01-01T00:00:00Z")
COMMENT = dict(id="comment-id", body="Example", createdAt="2020-01-01T00:00:00Z")
REF = dict(id="ref-id", name="Example")


def page(nodes, *, more=False, cursor=None):
    return dict(nodes=nodes, pageInfo=dict(hasNextPage=more, endCursor=cursor))


def client_with(body, *, status=200, headers=None):
    calls = []
    def respond(request):
        calls.append(request)
        return httpx.Response(status, json=body, headers=headers)
    return LinearClient(TOKEN, transport=httpx.MockTransport(respond)), calls


async def test_issue_result_and_bound_request():
    client, calls = client_with({"data": {"issue": ISSUE}})
    async with client:
        issue = await client.get_issue('TEST-1" malicious text')
    assert issue.identifier == "TEST-1"
    req = calls[0]; body = json.loads(req.content)
    assert str(req.url) == "https://api.linear.app/graphql"
    assert req.headers["authorization"] == "Bearer " + TOKEN
    assert body["variables"] == {"id": 'TEST-1" malicious text'}
    assert "malicious text" not in body["query"]
    assert TOKEN not in repr(client)
    assert client._http.is_closed


async def test_pagination_and_filters_are_explicit():
    calls = []
    def respond(request):
        variables = json.loads(request.content)["variables"]; calls.append(variables)
        return httpx.Response(200, json={"data": {"issues": page(
            [ISSUE] if variables["after"] is None else [], more=variables["after"] is None,
            cursor="cursor-1" if variables["after"] is None else None)}})
    async with LinearClient(TOKEN, transport=httpx.MockTransport(respond)) as client:
        first = await client.list_issues(first=1, filters=IssueFilter(team_id="team", assignee_id="user", state_id="state"))
        assert first.has_next_page and len(calls) == 1
        second = await client.list_issues(first=1, after=first.end_cursor)
        assert not second.has_next_page and not second.items
    assert calls[0]["filter"] == {"team": {"id": {"eq": "team"}}, "assignee": {"id": {"eq": "user"}}, "state": {"id": {"eq": "state"}}}
    assert calls[1]["after"] == "cursor-1"


@pytest.mark.parametrize("method, args, data, expected", [
    ("viewer", (), {"viewer": REF}, "ref-id"),
    ("create_issue", ({"teamId": "team", "title": "Example"},), {"issueCreate": {"success": True, "issue": ISSUE}}, "issue-id"),
    ("create_comment", ("issue-id", "Example"), {"commentCreate": {"success": True, "comment": COMMENT}}, "comment-id"),
])
async def test_single_result_operations(method, args, data, expected):
    client, calls = client_with({"data": data})
    async with client:
        assert (await getattr(client, method)(*args)).id == expected
    assert len(calls) == 1


@pytest.mark.parametrize("method,args,data", [
    ("list_comments", ("TEST-1",), {"issue": {"comments": page([COMMENT])}}),
    ("list_teams", (), {"teams": page([REF])}),
    ("list_states", ("team",), {"team": {"states": page([REF])}}),
    ("list_users", (), {"users": page([REF])}),
])
async def test_page_operations(method, args, data):
    client, calls = client_with({"data": data})
    async with client:
        result = await getattr(client, method)(*args, first=5, after="cursor")
    assert len(result.items) == 1 and not result.has_next_page
    assert json.loads(calls[0].content)["variables"]["after"] == "cursor"


async def test_partial_update_distinguishes_omitted_null_and_empty():
    client, calls = client_with({"data": {"issueUpdate": {"success": True, "issue": ISSUE}}})
    async with client:
        for patch, expected in [
            ({"title": "New"}, {"title": "New"}),
            ({"description": None, "assigneeId": None}, {"description": "", "assigneeId": None}),
            ({"description": ""}, {"description": ""}),
        ]:
            original = dict(patch)
            await client.update_issue("TEST-1", patch)
            assert json.loads(calls[-1].content)["variables"] == {"id": "TEST-1", "input": expected}
            assert patch == original


async def test_clear_description_survives_provider_null_noop():
    # Simulates the observed provider quirk: wire null leaves description alone.
    # Live verification is separate; this double cannot establish server behavior.
    stored = dict(ISSUE)
    writes = []
    def respond(request):
        body = json.loads(request.content)
        if body["operationName"] == "UpdateIssue":
            patch = body["variables"]["input"]
            writes.append(patch)
            stored.update({key: value for key, value in patch.items() if value is not None})
            return httpx.Response(200, json={"data": {"issueUpdate": {"success": True, "issue": stored}}})
        return httpx.Response(200, json={"data": {"issue": stored}})
    async with LinearClient(TOKEN, transport=httpx.MockTransport(respond)) as client:
        assert (await client.get_issue("TEST-1")).description == "Before"
        await client.update_issue("TEST-1", {"title": "New"})
        assert (await client.get_issue("TEST-1")).description == "Before"
        cleared = await client.update_issue("TEST-1", {"description": None})
        fetched = await client.get_issue("TEST-1")
    assert cleared.description == fetched.description == ""
    assert fetched.title == "New"
    assert len(writes) == 2


@pytest.mark.parametrize("patch", [{}, {"unknown": "value"}, {"title": None}, {"priority": True}, {"priority": 5}])
async def test_invalid_inputs_do_not_send(patch):
    client, calls = client_with({})
    async with client:
        with pytest.raises(ValueError): await client.update_issue("TEST-1", patch)
    assert not calls


@pytest.mark.parametrize("status,body,kind", [
    (401, {}, "authentication"), (403, {}, "authentication"),
    (429, {}, "rate_limit"),
    (400, {"errors": [{"extensions": {"code": "RATELIMITED"}}]}, "rate_limit"),
    (200, {"data": {"issue": ISSUE}, "errors": [{"message": TOKEN}]}, "graphql"),
    (200, {"errors": [{"extensions": {"code": "GRAPHQL_VALIDATION_FAILED"}}]}, "validation"),
    (503, {}, "http"),
])
async def test_error_classification_and_redaction(status, body, kind):
    client, calls = client_with(body, status=status, headers={"Retry-After": "3", "X-RateLimit-Requests-Reset": "123456"})
    async with client:
        with pytest.raises(LinearError) as caught: await client.get_issue("TEST-1")
    error = caught.value
    assert error.kind == kind and error.status == status and not error.outcome_unknown
    assert TOKEN not in "".join(traceback.format_exception(error))
    assert len(calls) == 1
    if kind == "rate_limit": assert error.retry_after == 3 and error.rate_limit_reset_ms == 123456


@pytest.mark.parametrize("body", [None, [], {"data": None}, {"data": {"issue": {}}},
    {"data": {"issue": dict(ISSUE, title=7)}},
    {"errors": [{"extensions": {"code": {"unexpected": TOKEN}}}]},
    {"errors": {"unexpected": TOKEN}},
])
async def test_malformed_envelopes_are_safe_errors(body):
    client, _ = client_with(body)
    async with client:
        with pytest.raises(LinearError) as caught: await client.get_issue("TEST-1")
    assert TOKEN not in str(caught.value)


async def test_incomplete_page_refused():
    client, _ = client_with({"data": {"issues": page([ISSUE], more=True)}})
    async with client:
        with pytest.raises(LinearError) as caught: await client.list_issues()
    assert caught.value.kind == "protocol"


@pytest.mark.parametrize("failure", [httpx.ReadTimeout, httpx.ConnectError])
async def test_uncertain_write_never_retries(failure):
    calls = []
    def respond(request): calls.append(request); raise failure(TOKEN, request=request)
    async with LinearClient(TOKEN, transport=httpx.MockTransport(respond)) as client:
        with pytest.raises(LinearError) as caught: await client.update_issue("TEST-1", {"title": "New"})
    assert caught.value.outcome_unknown and len(calls) == 1
    assert TOKEN not in "".join(traceback.format_exception(caught.value))


async def test_deadline_and_cancellation_propagation():
    async def respond(request): await asyncio.sleep(1); return httpx.Response(200, json={})
    async with LinearClient(TOKEN, timeout=.01, transport=httpx.MockTransport(respond)) as client:
        with pytest.raises(LinearError) as caught: await client.get_issue("TEST-1")
        assert caught.value.kind == "timeout"
        task = asyncio.create_task(client.update_issue("TEST-1", {"title": "New"}))
        await asyncio.sleep(0)
        task.cancel()
        with pytest.raises(asyncio.CancelledError): await task


@pytest.mark.parametrize("body,unknown,kind", [
    ({"data": {"issueUpdate": {"success": False}}}, False, "rejected"),
    ({"data": {"issueUpdate": {"success": True, "issue": None}}}, True, "protocol"),
    ({"data": {"issueUpdate": {"success": True, "issue": ISSUE}}, "errors": [{"message": "partial"}]}, True, "graphql"),
])
async def test_mutation_response_must_prove_success(body, unknown, kind):
    client, calls = client_with(body)
    async with client:
        with pytest.raises(LinearError) as caught: await client.update_issue("TEST-1", {"title": "New"})
    assert caught.value.kind == kind and caught.value.outcome_unknown == unknown
    assert len(calls) == 1


async def test_redirect_is_not_followed():
    client, calls = client_with({}, status=302, headers={"Location": "https://example.com/collect"})
    async with client:
        with pytest.raises(LinearError): await client.get_issue("TEST-1")
    assert len(calls) == 1


async def test_api_key_header():
    def respond(request):
        assert request.headers["Authorization"] == TOKEN
        return httpx.Response(200, json={"data": {"viewer": REF}})
    async with LinearClient(TOKEN, auth="api_key", transport=httpx.MockTransport(respond)) as client:
        assert (await client.viewer()).id == "ref-id"


@pytest.mark.parametrize("token", ["", "bad\r\nheader", "bad token"])
def test_invalid_credential(token):
    with pytest.raises(ValueError): LinearClient(token)


async def test_missing_issue_is_clear_not_found_error():
    client, _ = client_with({"data": {"issue": None}})
    async with client:
        with pytest.raises(LinearError) as caught: await client.get_issue("MISSING-1")
    assert caught.value.kind == "not_found" and not caught.value.outcome_unknown


async def test_empty_malformed_errors_object_is_not_success():
    client, _ = client_with({"data": {"issue": ISSUE}, "errors": {}})
    async with client:
        with pytest.raises(LinearError): await client.get_issue("TEST-1")


async def test_corrupt_compressed_write_response_is_uncertain():
    calls = []
    def respond(request):
        calls.append(request)
        return httpx.Response(200, content=b"not-a-gzip-stream", headers={"Content-Encoding": "gzip"})
    async with LinearClient(TOKEN, transport=httpx.MockTransport(respond)) as client:
        with pytest.raises(LinearError) as caught:
            await client.update_issue("TEST-1", {"title": "New"})
    assert caught.value.kind == "protocol" and caught.value.outcome_unknown
    assert len(calls) == 1
