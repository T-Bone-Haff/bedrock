# Review — <change>

| Field | Value |
|---|---|
| Date | YYYY-MM-DD |
| Reviewer | <name or surface> |
| Scope | <diff and claimed outcome> |
| Profile | lightweight / standard / high-risk |
| Outcome | approve / approve-with-advisory / pause |

## Checked surfaces

- <surface and evidence inspected>

## Gate dispositions

| Gate | Disposition | Evidence or reason |
|---|---|---|
| <name> | passed / failed / not-relevant / unavailable | <pointer> |

## Findings

| ID | Class | Impact | Likelihood | Confidence | Exploitability | Blocking | Locus | Evidence |
|---|---|---|---|---|---|---|---|---|
| F-1 | correctness | high | medium | high | not-applicable | yes | `file:line` | <proof> |

If there are no findings, state: **No findings after checking <named surfaces>.** Do not add filler positives.

## Out-of-scope debt

| Item | Owner | Deadline or trigger | Why it does not block this change |
|---|---|---|---|

## Verdict basis

State the terminal predicate: unresolved blockers and failed required gates pause; advisory debt does not block unless it carries an unresolved decision.
