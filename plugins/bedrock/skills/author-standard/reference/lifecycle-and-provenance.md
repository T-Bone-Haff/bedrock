# Standard lifecycle and provenance

## Required lifecycle metadata

Every adopted standard records an owner, status, binding, current revision, compatibility statement, last verification, review trigger, successor, and rollback path. State transitions are explicit:

`proposed → proving → adopted → revised → deprecated → superseded or retired`

Rollback returns consumers to a named compatible revision; it never erases the failed revision or its evidence. Breaking changes identify affected consumers and migration requirements before adoption.

## Evidence grades

| Grade | Meaning |
|---|---|
| A | Normative public specification or reproducible multi-consumer evidence. |
| B | Reproducible evidence from one controlled consumer or multiple independent operational observations. |
| C | Reviewed expert judgment or a single operational observation with stated limits. |
| D | Hypothesis or anecdote; may motivate proving but cannot independently bind. |

Conflicting sources remain visible. The standard states which source controls, why it applies, and what evidence would reopen the judgment.

## Provenance record

For each normative section record: source identifier, version/access date, grade, applicability, conflicts, and author judgment. A reference must remain reachable to the intended consumer; otherwise inline the minimum load-bearing contract with a checked source marker or fail the adoption gate.
