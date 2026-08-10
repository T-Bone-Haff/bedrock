# HEB-116 validation results

This record is completed from fresh command output before staging. A passed direct audit or deterministic validator is not a runner-backed design convergence claim.

| Gate | Command | Result |
|---|---|---|
| Contract fixtures | `python scripts/validate_agent_review_contracts.py` | PASS |
| Unit and integration suite | `python -m unittest discover -s tests -v` | PASS: 59 tests; 1 Docker-dependent test skipped because the daemon was unavailable |
| Safety validator | `python scripts/validate_safety.py` | PASS |
| Plugin validator | `python scripts/validate_plugin.py` | PASS: 13/13 skills passed deterministic and strict host validation |
| Strict host validator | `claude plugin validate --strict plugins/bedrock` | PASS |
| Clean installation | `bash scripts/smoke_clean_install.sh` | PASS: isolated install/reload discovered all 13 skills |
| Routing evaluation | `python scripts/run_routing_evals.py --profile release --runs 3 --output docs/evidence/heb-109/routing-results.json` | PASS under preregistered policy: 113/114 runs (99.12%), every case at or above 2/3, zero excluded selections, full retained-evidence eligibility; $1.051002. One `adversarial-debug-misroute` run returned null while its explanation correctly routed the request to debug; retained as a failed run. |
| Direct review | evidence-cited audit against HEB-111 architecture, HEB-110 safety baseline, and HEB-106 dispositions | PASS with no open BLOCKING or MATERIAL finding; caught and corrected nested-object salvage enumeration and a provider-bound routing fixture during the audit |
