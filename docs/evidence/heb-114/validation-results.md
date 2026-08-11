# HEB-114 validation results

Status: **required local and configured CI populations pass.** Docker remained
unavailable locally, and the required CI population closed that environmental
gap without the local skip. Source `ed5b8338214b834bc78c203a8ccdae6e7e54923c`
landed through PR [#30](https://github.com/T-Bone-Haff/bedrock/pull/30) as merge
`14ec001b5ca4e9dcf45d1d96a97a696a3027427e`.

| Population / command | Input population | Result |
|---|---|---|
| `python scripts/validate_frontend_contracts.py` | Schemas, 2 valid fixtures, 6 seeded-invalid fixtures, 7 ownership cases, required/forbidden corpus markers, browser fixture file/gate/lock contract | PASS |
| `python -m unittest discover -s tests -v` | 82 repository unit/integration tests | PASS: 82 run, 1 Docker integration skipped because daemon unavailable |
| Same suite with `HEB110_REQUIRE_DOCKER=1 HEB110_REQUIRE_TERRAFORM=1` | Same 82, with integrations required | FAIL: Docker runtime image check unable to run; Terraform state integrations passed |
| `claude plugin validate --strict plugins/bedrock` | Candidate plugin manifest and package | PASS |
| `validate_safety.py` | Accepted HEB-110 deterministic contracts | PASS |
| `validate_infrastructure_delivery_contracts.py` | HEB-113 infrastructure/delivery registry and fixtures | PASS |
| Package validator with retained-routing validation disabled | All 13 skills, manifests, package links/paths, samples, schemas and domain contract registries | PASS: 13/13 |
| Full `validate_plugin.py` | Same population plus retained routing evidence | PASS: 13/13 skills; retained candidate identities match |
| `smoke_clean_install.sh` | Isolated marketplace install/reload | PASS: 13 skills discovered |
| `npm ci --ignore-scripts` + `npm audit --audit-level=high` | Exact lockfile, runtime and development populations | PASS: clean install; 0 known vulnerabilities after Vite 8.2.1 security update |
| `typecheck`, `lint`, `unit`, `coverage`, `build`, `budget` | Exact browser fixture | PASS; 5/5 component tests; 100% statements/lines/functions and 97.05% branches for declared source population; 60,556 compressed JS+CSS bytes ≤ 120,000 |
| `playwright test` | 7 scenarios × Chromium, Firefox, WebKit | PASS: 21/21, zero skips |
| Release routing adapter | 54 cases × 3 repetitions under `claude-haiku-4-5-20251001`; `$0.06` per-call and `$3.00` aggregate ceilings | PASS: 162/162, zero excluded selections, retained-evidence eligible; cost `$1.438027`; aggregate budget not exhausted |
| Manual Safari + VoiceOver | One representative flow on macOS 26.5.2 (25F84), Safari 26.5.2 (21624.2.5.11.8), VoiceOver 10 (993) | PASS: Option-Tab focused `Open details` with a visible VoiceOver ring; Return activated it; accessibility focus moved to the `Details ready` heading. Exact audible wording was not captured. VoiceOver was restored to off. |
| Configured GitHub Actions population | Existing deterministic job on Ubuntu/Node 22.12.0 followed by live routing | PASS: run [`31518930280`](https://github.com/T-Bone-Haff/bedrock/actions/runs/31518930280); deterministic job `93870904783` and live-routing job `93871781057` both succeeded on the landed source |

The first full routing observation under fixture digest
`040186db609cbb15e86fd2ac09683dc5695a34fc6a2256b2cfd0c1901b94c6ef`
was 160/162: two draws selected `null` for
`overlap-frontend-backend-enforcement` because the prompt demanded that
server-only controls be placed inside a React client. Debugging identified a
fixture-specification defect. The prompt was narrowed to request enforcement in
the owning application layer; a targeted non-retained 3/3 falsification passed,
then the complete release population was rerun from scratch. The retained
report uses fixture digest
`13b8435390b10a1b8d4be4e2a2d152a01f85f8e21f0c895e1030634a03b98c30`,
catalog digest
`fb8111abc3095efb4baf3c9ee6a93e1dad94455ceda54cb0f5a3f065f7fce06e`,
and policy digest
`4e3aedf467f4d353a9903a31f8dfd3fa9224f01eb449a473051177b5f626b67d`.
The failed and targeted observations were not pooled into retained evidence.

The first pushed HEB-114 candidate then exposed an independent ambiguity in
`frontend-code-prototype-promotion`: its leading review verb routed one PR draw
to `code-review`. The operation-first repair passed a targeted 3/3 probe. During
the fresh release rerun, `adversarial-implementation-misroute` exposed that the
adapter sometimes treated a user's conflicting skill preference as binding,
returning `null` or the excluded skill despite an authorized underlying
operation. Three fixture-only rewrites failed to stabilize that boundary and
were discarded. The authorized adapter repair now treats named-skill
preferences as untrusted routing input, while preserving `null` for operations
that no catalog description authorizes. The unchanged adversarial case passed
3/3 targeted and again 3/3 in the fresh complete population. The retained
report uses fixture digest
`c7a2b41693a553ceabfc9355b36d4d3123bcee4b83c310ecbf49e4004577a311`,
the same catalog and policy digests cited above, and records the enforced
per-call and aggregate budget ceilings. Diagnostic and targeted observations
remain outside retained evidence.

`git diff --check` and workflow YAML parsing pass. A changed-surface secret scan
found no embedded credential; the workflow's secret expression is an expected
reference, not a value. Generated `node_modules`, coverage, build, and browser
result directories are fixture-local ignored outputs.
