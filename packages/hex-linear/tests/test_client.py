import asyncio
import json
import traceback

import httpx
import pytest

from hex_linear import LinearClient, LinearError, IssueFilter, IssueRelation

TOKEN = "synthetic-token-for-tests"
ISSUE_ID = "00000000-0000-4000-8000-000000000001"
OTHER_ID = "00000000-0000-4000-8000-000000000002"
EDGE_ID = "00000000-0000-4000-8000-000000000003"
EDGE = IssueRelation(EDGE_ID, "blocks", ISSUE_ID, OTHER_ID, None)
ISSUE = dict(id="issue-id", identifier="TEST-1", title="Example", description="Before",
             url="https://linear.app/example/issue/TEST-1", updatedAt="2020-01-01T00:00:00Z")
ISSUE.update(team={"id": "team"}, state={"id": "state", "name": "Done", "type": "completed"},
             priority=3.0, assignee=None, parent=None, dueDate=None, archivedAt=None,
             completedAt="2020-01-01T00:00:00Z", creator={"id": "creator"})
COMMENT = dict(id="comment-id", body="Example", createdAt="2020-01-01T00:00:00Z")
COMMENT.update(user={"id": "author"}, issue={"id": "issue-id"})
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
    client, calls = client_with({"data": {"issue": dict(ISSUE, identifier='TEST-1" malicious text')}})
    async with client:
        issue = await client.get_issue('TEST-1" malicious text')
    assert issue.id == "issue-id"
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
    ("list_comments", ("TEST-1",), {"issue": {"id": "issue-id", "identifier": "TEST-1", "comments": page([COMMENT])}}),
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


async def test_complete_context_and_comment_attribution():
    client, _ = client_with({"data": {"issue": ISSUE}})
    async with client:
        issue = await client.get_issue("TEST-1")
    context = issue.context
    assert context.team_id == "team"
    assert (context.state.id, context.state.name, context.state.type) == ("state", "Done", "completed")
    assert context.priority == 3
    assert context.assignee_id is None and context.parent_id is None
    assert context.due_date is None and context.archived_at is None
    assert context.completed_at == "2020-01-01T00:00:00Z" and context.creator_id == "creator"
    client, _ = client_with({"data": {"commentCreate": {"success": True, "comment": COMMENT}}})
    async with client:
        comment = await client.create_comment("issue-id", "Example")
    assert comment.attribution.issue_id == "issue-id"
    assert comment.attribution.author_id == "author"


@pytest.mark.parametrize("key", ["team", "state", "priority", "assignee", "parent", "dueDate", "archivedAt", "completedAt", "creator"])
async def test_omitted_context_is_not_null_or_success(key):
    incomplete = {k: v for k, v in ISSUE.items() if k != key}
    client, _ = client_with({"data": {"issue": incomplete}})
    async with client:
        with pytest.raises(LinearError, match="protocol"):
            await client.get_issue("TEST-1")


async def test_wrong_issue_read_and_mutation_postimage_are_rejected():
    for operation, data, unknown in [
        ("read", {"issue": dict(ISSUE, id="wrong", identifier="OTHER-1")}, False),
        ("write", {"issueUpdate": {"success": True, "issue": dict(ISSUE, id="wrong", identifier="OTHER-1")}}, True),
    ]:
        client, calls = client_with({"data": data})
        async with client:
            with pytest.raises(LinearError) as caught:
                if operation == "read": await client.get_issue("TEST-1")
                else: await client.update_issue("TEST-1", {"title": "New"})
        assert caught.value.kind == "protocol" and caught.value.outcome_unknown == unknown
        assert len(calls) == 1


async def test_parent_assignment_clear_and_omission():
    client, calls = client_with({"data": {"issueUpdate": {"success": True, "issue": ISSUE}}})
    async with client:
        for patch in [{"parentId": OTHER_ID}, {"parentId": None}, {"title": "New"}]:
            original = dict(patch)
            await client.update_issue("TEST-1", patch)
            assert json.loads(calls[-1].content)["variables"]["input"] == patch == original


async def test_direct_child_pages_preserve_population():
    seen = []
    def respond(request):
        variables = json.loads(request.content)["variables"]; seen.append(variables)
        return httpx.Response(200, json={"data": {"issues": page(
            [dict(ISSUE, parent={"id": OTHER_ID})] if variables["after"] is None else [],
            more=variables["after"] is None, cursor="next" if variables["after"] is None else None)}})
    async with LinearClient(TOKEN, transport=httpx.MockTransport(respond)) as client:
        filters = IssueFilter(parent_id=OTHER_ID)
        first = await client.list_issues(first=1, filters=filters, include_archived=True)
        second = await client.list_issues(first=1, after=first.end_cursor, filters=filters, include_archived=True)
    assert first.items[0].context.parent_id == OTHER_ID and not second.has_next_page
    assert [v["filter"] for v in seen] == [{"parent": {"id": {"eq": OTHER_ID}}}] * 2
    assert all(v["includeArchived"] is True for v in seen)


async def test_wrong_parent_page_refused():
    client, _ = client_with({"data": {"issues": page([ISSUE])}})
    async with client:
        with pytest.raises(LinearError, match="protocol"):
            await client.list_issues(filters=IssueFilter(parent_id=OTHER_ID))


async def test_label_pagination_is_explicit_and_issue_bound():
    for identity in [ISSUE_ID, OTHER_ID]:
        client, calls = client_with({"data": {"issue": {"id": identity, "labels": page([REF], more=True, cursor="next")}}})
        async with client:
            if identity == ISSUE_ID:
                result = await client.list_issue_labels(ISSUE_ID, first=1, after="previous", include_archived=True)
                assert result.has_next_page and result.end_cursor == "next" and result.items[0].id == "ref-id"
                assert json.loads(calls[0].content)["variables"] == dict(id=ISSUE_ID, first=1, after="previous", includeArchived=True)
            else:
                with pytest.raises(LinearError, match="protocol"): await client.list_issue_labels(ISSUE_ID)


def relation(**changes):
    return dict(dict(id=EDGE_ID, type="blocks", issue={"id": ISSUE_ID}, relatedIssue={"id": OTHER_ID}, archivedAt=None), **changes)


@pytest.mark.parametrize("direction,field", [("outgoing", "relations"), ("incoming", "inverseRelations")])
async def test_relation_directions_and_continuation(direction, field):
    edge = relation() if direction == "outgoing" else relation(issue={"id": OTHER_ID}, relatedIssue={"id": ISSUE_ID})
    seen = []
    def respond(request):
        data = json.loads(request.content); seen.append(data)
        more = data["variables"]["after"] is None
        return httpx.Response(200, json={"data": {"issue": {"id": ISSUE_ID, field: page([edge] if more else [], more=more, cursor="next" if more else None)}}})
    async with LinearClient(TOKEN, transport=httpx.MockTransport(respond)) as client:
        first = await client.list_relations(ISSUE_ID, direction=direction, first=1, include_archived=True)
        last = await client.list_relations(ISSUE_ID, direction=direction, first=1, after=first.end_cursor, include_archived=True)
    assert first.items[0].id == EDGE_ID and first.items[0].type == "blocks"
    assert not last.items and not last.has_next_page
    assert all(v["variables"]["includeArchived"] is True for v in seen)
    assert all(field + "(" in v["query"] for v in seen)


@pytest.mark.parametrize("direction,field", [("outgoing", "relations"), ("incoming", "inverseRelations")])
async def test_reversed_relation_does_not_prove_selected_population(direction, field):
    edge = relation() if direction == "incoming" else relation(issue={"id": OTHER_ID}, relatedIssue={"id": ISSUE_ID})
    client, _ = client_with({"data": {"issue": {"id": ISSUE_ID, field: page([edge])}}})
    async with client:
        with pytest.raises(LinearError, match="protocol"):
            await client.list_relations(ISSUE_ID, direction=direction)


@pytest.mark.parametrize("kind", ["blocks", "related"])
async def test_typed_relation_create_and_identity_checked_delete(kind):
    client, calls = client_with({"data": {"issueRelationCreate": {"success": True, "issueRelation": relation(type=kind)}}})
    async with client:
        result = await client.create_relation(ISSUE_ID, OTHER_ID, type=kind)
    assert (result.issue_id, result.related_issue_id, result.type) == (ISSUE_ID, OTHER_ID, kind)
    assert json.loads(calls[0].content)["variables"] == {"input": {"issueId": ISSUE_ID, "relatedIssueId": OTHER_ID, "type": kind}}
    client, _ = client_with({"data": {"issueRelationDelete": {"success": True, "entityId": EDGE_ID}}})
    async with client:
        assert await client.delete_relation(result) == EDGE_ID


@pytest.mark.parametrize("payload", [relation(issue={"id": OTHER_ID}), relation(relatedIssue={"id": ISSUE_ID}), relation(type="related")])
async def test_relation_create_mismatch_is_uncertain(payload):
    client, calls = client_with({"data": {"issueRelationCreate": {"success": True, "issueRelation": payload}}})
    async with client:
        with pytest.raises(LinearError) as caught: await client.create_relation(ISSUE_ID, OTHER_ID, type="blocks")
    assert caught.value.kind == "protocol" and caught.value.outcome_unknown and len(calls) == 1


@pytest.mark.parametrize("payload,unknown,kind", [
    ({"success": True, "entityId": OTHER_ID}, True, "protocol"),
    ({"success": True}, True, "protocol"),
    ({"success": False}, False, "rejected"),
])
async def test_delete_receipt_must_identify_requested_edge(payload, unknown, kind):
    client, calls = client_with({"data": {"issueRelationDelete": payload}})
    async with client:
        with pytest.raises(LinearError) as caught: await client.delete_relation(EDGE)
    assert caught.value.kind == kind and caught.value.outcome_unknown == unknown and len(calls) == 1


@pytest.mark.parametrize("method,args,kwargs", [
    ("create_relation", (ISSUE_ID, OTHER_ID), {"type": "duplicate"}),
    ("create_relation", (ISSUE_ID, ISSUE_ID), {"type": "blocks"}),
    ("create_relation", ("TEST-1", OTHER_ID), {"type": "blocks"}),
    ("list_relations", (ISSUE_ID,), {"direction": "both"}),
    ("delete_relation", ("",), {}),
    ("list_issue_labels", (ISSUE_ID,), {"first": 0}),
    ("list_issues", (), {"include_archived": 1}),
])
async def test_new_operation_invalid_input_never_sends(method, args, kwargs):
    client, calls = client_with({})
    async with client:
        with pytest.raises(ValueError): await getattr(client, method)(*args, **kwargs)
    assert not calls


@pytest.mark.parametrize("method,args,kwargs", [
    ("create_relation", (ISSUE_ID, OTHER_ID), {"type": "blocks"}),
    ("delete_relation", (EDGE,), {}),
])
async def test_relation_unknown_outcome_is_one_attempt(method, args, kwargs):
    calls = []
    def respond(request):
        calls.append(request); raise httpx.ReadTimeout(TOKEN, request=request)
    async with LinearClient(TOKEN, transport=httpx.MockTransport(respond)) as client:
        with pytest.raises(LinearError) as caught: await getattr(client, method)(*args, **kwargs)
    assert caught.value.outcome_unknown and len(calls) == 1
    assert TOKEN not in "".join(traceback.format_exception(caught.value))


@pytest.mark.parametrize("author", [None, {"id": "author"}])
async def test_comment_attribution_nullable_author_and_wrong_issue(author):
    for issue_id in ["issue-id", "wrong"]:
        payload = dict(COMMENT, user=author, issue={"id": issue_id})
        client, _ = client_with({"data": {"issue": {"id": "issue-id", "identifier": "TEST-1", "comments": page([payload])}}})
        async with client:
            if issue_id == "issue-id":
                result = await client.list_comments("TEST-1")
                assert result.items[0].attribution.author_id == (None if author is None else "author")
            else:
                with pytest.raises(LinearError, match="protocol"): await client.list_comments("TEST-1")


def test_original_positional_models_remain_constructible():
    from hex_linear import Issue, Comment, IssueFilter
    assert Issue("id", "T-1", "Title", None, "url", "time").context is None
    assert Comment("id", "Body", "time").attribution is None
    assert IssueFilter("team", "assignee", "state").parent_id is None


@pytest.mark.parametrize("edge", [
    EDGE_ID,
    IssueRelation(EDGE_ID, "duplicate", ISSUE_ID, OTHER_ID, None),
    IssueRelation(EDGE_ID, "blocks", ISSUE_ID, ISSUE_ID, None),
])
async def test_delete_requires_supported_observed_edge(edge):
    client, calls = client_with({})
    async with client:
        with pytest.raises(ValueError): await client.delete_relation(edge)
    assert not calls


async def test_other_relation_types_remain_visible():
    client, _ = client_with({"data": {"issue": {"id": ISSUE_ID, "relations": page([relation(type="duplicate")])}}})
    async with client:
        assert (await client.list_relations(ISSUE_ID, direction="outgoing")).items[0].type == "duplicate"


@pytest.mark.parametrize("change", [{"priority": True}, {"priority": 2.5}, {"state": None}, {"team": []}, {"creator": {}}])
async def test_malformed_context_is_safe_protocol_error(change):
    client, _ = client_with({"data": {"issue": dict(ISSUE, **change)}})
    async with client:
        with pytest.raises(LinearError, match="protocol"): await client.get_issue("TEST-1")


async def test_comment_missing_attribution_is_uncertain():
    for key in ["issue", "user"]:
        comment = {k: v for k, v in COMMENT.items() if k != key}
        client, calls = client_with({"data": {"commentCreate": {"success": True, "comment": comment}}})
        async with client:
            with pytest.raises(LinearError) as caught: await client.create_comment("issue-id", "Example")
        assert caught.value.outcome_unknown and len(calls) == 1


async def test_create_parent_and_populated_context():
    value = dict(ISSUE, parent={"id": OTHER_ID}, assignee={"id": "user"}, creator=None,
                 dueDate="2020-01-02", archivedAt="2020-01-03T00:00:00Z", completedAt=None)
    client, calls = client_with({"data": {"issueCreate": {"success": True, "issue": value}}})
    async with client:
        issue = await client.create_issue({"teamId": "team", "title": "Example", "parentId": OTHER_ID})
    assert issue.context.parent_id == OTHER_ID and issue.context.assignee_id == "user"
    assert issue.context.creator_id is None and issue.context.completed_at is None
    assert issue.context.due_date == "2020-01-02" and issue.context.archived_at == "2020-01-03T00:00:00Z"
    assert json.loads(calls[0].content)["variables"]["input"]["parentId"] == OTHER_ID


def test_typed_input_required_and_optional_metadata():
    from hex_linear import IssueCreate, IssueUpdate
    assert IssueCreate.__required_keys__ == {"teamId", "title"}
    assert IssueCreate.__optional_keys__ == {"description", "stateId", "assigneeId", "priority", "parentId"}
    assert IssueUpdate.__required_keys__ == set()
    assert IssueUpdate.__optional_keys__ == {"title", "description", "stateId", "assigneeId", "priority", "parentId"}
