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
are title, description, stateId, assigneeId and priority; creation also needs
teamId. Unsupported fields fail before a request. This is deliberately a subset.

Available methods: `viewer`, `get_issue`, `list_issues`, `create_issue`,
`update_issue`, `list_comments`, `create_comment`, `list_teams`, `list_states`,
`list_users`. Listing returns a typed `Page`: inspect `has_next_page`, then pass
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
