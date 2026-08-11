# HEB-115 validation results

This record is completed from fresh command output before staging. A prior run, declared command, or illustrative example is not execution evidence.

| Gate | Result |
|---|---|
| HEB-115 contract fixtures | PASS — schema, semantic, behavior-routing, and contract-marker validation |
| Complete unit/integration suite | PASS — 67 tests; 1 Docker integration skipped because the local daemon was unavailable |
| HEB-110 safety validator | PASS |
| Plugin/strict host validation | PASS — 13/13 skills, retained evidence, and strict host validation |
| Clean installation | PASS — 13 skills discovered from an isolated install |
| Routing evaluation | PASS — 129/129, 100%, zero excluded selections, $1.161832 |
| Diff and reference checks | PASS — `git diff --check` and repository reference validation |
| Direct evidence-cited review | PASS — no remaining BLOCKING or MATERIAL findings after correcting timestamp enforcement, malformed-row handling, and the stale routing limitation |

The passing release-profile routing identity is fixture `4130b5ddb2357d3f17e2db5c86b40cc9a5001f4a3f87727d142bef8cbe14c532`, catalog `41e78494400a80e536af5df93ce2fa290d852f6174cb7325c931fae3c9131d8c`, and policy `4e3aedf467f4d353a9903a31f8dfd3fa9224f01eb449a473051177b5f626b67d`. The report is retained at `docs/evidence/heb-109/routing-results.json` because that is the repository's registered routing-evidence surface.

The Docker integration must run without a skip in required CI before merge. The local result does not claim container-runtime evidence.

## Retained failed routing pass

The first complete release-profile pass after implementation is retained here as a failed calibration result before its report was superseded by a corrected full-suite run:

- Identity: fixture `63e40d09f44c0ded2635ff7cb4d8ee456cb71fdbff4cec81a42273e38c340977`; catalog `41e78494400a80e536af5df93ce2fa290d852f6174cb7325c931fae3c9131d8c`; policy `4e3aedf467f4d353a9903a31f8dfd3fa9224f01eb449a473051177b5f626b67d`.
- Result: 122/129 runs, 94.5736%, zero excluded selections, $1.193632; failed the 95% aggregate and 2/3 per-case gates.
- `application-code-portable-profile`: 1/3. The phrase “define the portable contract” correctly attracted `author-standard`; the case was rewritten as implementation under an existing contract.
- `adversarial-debug-misroute`: 0/3. “Without diagnosing” made abstention defensible even though every explanation identified `debug`; the case now adversarially names the wrong skill without forbidding the required operation.
- `adversarial-implementation-misroute`: 1/3. Asking both to write a relay and skip the handoff was an invalid hybrid; the case now asks the wrong skill to perform one unambiguous implementation operation.

The corrections change prompts, not expected owners or skill contracts. No individual failed draw is rerun. The entire preregistered release suite must run again against the new fixture identity.
