# HEX Linear client

A small asynchronous Python library for agents that call Linear directly.
Requires Python 3.11+; HTTPX is its only direct runtime dependency.

```sh
python -m pip install ./packages/hex-linear
```

```python
from hex_linear import LinearClient, IssueFilter

async def inspect_work(access_token: str, issue_id: str, team_id: str):
    # Your trusted runtime supplies the token; never put it in model prompts.
    async with LinearClient(access_token) as linear:
        issue = await linear.get_issue(issue_id)
        page = await linear.list_issues(filters=IssueFilter(team_id=team_id))
        return issue, page
```

After the caller has authorized a write:

```python
updated = await linear.update_issue(issue_id, {"description": "New description"})
created = await linear.create_issue({"teamId": team_id, "title": "New issue"})
comment = await linear.create_comment(issue_id, "Comment text")
```

Run these calls inside the open client context. Omitted update fields are left
untouched. `{"description": None}` requests clearing and is sent as an empty
string because Linear ignores null for this field. `{"assigneeId": None}` is
sent as null; `{"description": ""}` also sends an empty string. The caller's
patch is not modified. The supported issue fields
are title, description, stateId, assigneeId, priority and parentId; creation also needs
teamId. Unsupported fields fail before a request. This is deliberately a subset.

Available methods: `viewer`, `get_issue`, `list_issues`, `create_issue`,
`update_issue`, `list_comments`, `create_comment`, `list_teams`, `list_states`,
`list_users`, `list_issue_labels`, `list_relations`, `create_relation`,
`delete_relation`. Listing returns a typed `Page`: inspect `has_next_page`, then pass
`end_cursor` as `after` while retaining the same filters. One page is not an
entire collection. The library makes no snapshot-consistency promise while
provider data is changing. Page size is explicitly limited to 1–100 items.

OAuth is the default. For an explicitly supplied API key, set `auth="api_key"`.
The library does not discover credentials, change Keychain settings, refresh
OAuth tokens, persist state or approve actions. Credentials belong to the
trusted calling process. It uses Linear's fixed HTTPS endpoint with certificate
verification, no redirects and no ambient proxy configuration. A custom HTTPX
transport is a trusted hook for tests, not an untrusted caller option. Close
with `async with` or `await client.aclose()`.

`LinearError` exposes `kind`, HTTP `status`, `outcome_unknown`, numeric
`retry_after` seconds and `rate_limit_reset_ms` when available. It does not expose
tokens or raw provider error messages/bodies. GraphQL errors are checked even
with HTTP 200. Partial data with errors is not returned as a successful result.
Missing/inaccessible objects may appear as `not_found` or a provider error.

There are **no automatic retries**, including rate-limited calls. Callers can
schedule a later read using rate-limit metadata. After a write timeout, malformed
reply or other uncertain result, inspect `outcome_unknown` and resolve what
happened before deciding on another write. Cancellation propagates normally;
a cancelled write must also be treated as potentially applied. The configured
request timeout is not an exactly-once or durable-recovery mechanism.

## Work-record extension (0.2.0)

This bounded extension implements the ratified P2 direction of
[HEB-177](https://linear.app/t-bone-haff-sofia/issue/HEB-177).
It leaves [DDR-002's accepted original scope](https://github.com/Haffey-Enterprises/HEX/blob/0b82e1ebd4d7edb64b5a3096aafb555818566266/docs/ddr/DDR-002-shared-linear-client.md)
and HEB-170's completed acceptance intact. This section records the added provider
operations and their review-trigger disposition; it does not activate the deferred
administrative runtime or assert new live acceptance.

Every API-produced `Issue` includes an `IssueContext`: team ID; workflow state
ID/name/type; priority (integer 0–4); nullable assignee and parent IDs, due date,
archive/completion timestamps, and creator ID. Read **all pages** of
`list_issue_labels(issue.id)` for the separate label IDs/names. No implicit
label collection is embedded in the scalar context. A context read does not
establish authority, a completed work disposition, or preservation of fields
outside this declared subset.

API-produced comments include `CommentAttribution(issue_id, author_id)`.
A null author means the provider supplies no user attribution (for example an
integration); it does not identify the caller. Missing requested context or
attribution is a protocol error, distinct from an explicitly null field.
Existing positional constructors for `Issue`, `Comment` and `IssueFilter` still
work: manually constructed legacy objects have `context=None` or
`attribution=None`, meaning **not observed**, never an empty observed context.
Existing method signatures remain valid. Results for `get_issue`, `update_issue`
and issue-bound comment reads/writes now reject a mismatched issue ID/identifier;
a mismatched mutation response is an unknown outcome, never a retry invitation.
Bind stable UUIDs before mutation; a moved or renamed identifier can cease to match.

Set `parentId` on issue creation or update; on update, omission preserves it and
explicit `None` sends null to request clearing. Readback determines the actual
result; schema-valid null alone does not prove a live clear. Direct children use
`IssueFilter(parent_id=parent_uuid)`. Retain the same filter and
`include_archived` selection across pages. This is one level, not a recursive
descendant inventory. The new parent filter, label/relation reads and relation
writes require canonical UUIDs, obtained from issue reads; existing issue and
comment methods retain ID/identifier input support.

```python
children = await linear.list_issues(
    filters=IssueFilter(parent_id=parent.id), include_archived=True)
labels = await linear.list_issue_labels(issue.id, include_archived=True)
outgoing = await linear.list_relations(issue.id, direction="outgoing", include_archived=True)
incoming = await linear.list_relations(issue.id, direction="incoming", include_archived=True)
```

These calls each return **one page**. `include_archived` defaults to false for
issues, labels and relations; select true when the protected population includes
archived records. Visibility is still limited to the caller's provider permissions.
Separate pages and fields do not form an atomic snapshot.

An `IssueRelation` preserves edge ID, raw provider type, source `issue_id`, target
`related_issue_id`, and nullable archive timestamp. For `blocks`, the source
blocks the target. `related` expresses related work, but still retains the
provider's stored orientation. Inspect both directions and deduplicate by edge ID
when assessing a complete incident-edge population. Reads retain other provider
types (including duplicate/similar) so they are not silently hidden; writes support
only `blocks` and `related` and refuse self-edges.

```python
# Only after the caller binds authorization, endpoints and current state:
edge = await linear.create_relation(source.id, target.id, type="blocks")
# Later, with specific deletion authority for this freshly observed edge:
deleted_id = await linear.delete_relation(edge)
```

Deletion requires an `IssueRelation` selected from an authorized read or creation
result; a bare edge ID or unsupported relation type is refused before sending.
The provider deletion receipt must identify that exact edge. Its API deletes by
ID, so the supplied type/endpoints are caller-owned context, **not an atomic
provider precondition**. The adapter does not authenticate an in-memory record's
provenance. Reconcile current context before sending and read the complete selected
edge populations afterward to establish absence. The acknowledgment itself is not
that readback. Parent changes, relation creation and deletion retain the existing
one-attempt/unknown-outcome contract.

No labels, dates, archive, project or duplicate-disposition writes are added.
The caller still owns actor/team binding, authorization, stale-edit detection,
closure evidence, duplicate reconciliation, and preservation of human material.
Offline tests and schema validation establish mechanics only; live parent clearing,
relation effects, permissions and withheld-ack behavior remain separate proof gates.

## Verification

```sh
python -m pip install -e './packages/hex-linear[test]'
python -m pytest packages/hex-linear/tests
python packages/hex-linear/scripts/check_schema.py /path/to/linear-schema.graphql
```

Tests use HTTPX MockTransport: they prove request construction and response/error
handling, not actual provider writes. The schema checker validates every shipped
document against a separately supplied official Linear schema and includes an
invalid-query control. Schema validity does not establish permissions or live
write behavior. The build's evidence records distinguish these checks from real
API observations. No database, desktop approval app or assistant plugin is needed.

[Linear API](https://linear.app/developers/graphql) ·
[Pagination](https://linear.app/developers/pagination) ·
[Rate limits](https://linear.app/developers/rate-limiting) ·
[Design and origin](https://github.com/Haffey-Enterprises/HEX/blob/0b82e1ebd4d7edb64b5a3096aafb555818566266/docs/ddr/DDR-002-shared-linear-client.md)
