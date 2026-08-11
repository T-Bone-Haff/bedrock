# HEB-113 validation results

This record is completed from fresh command output before staging. It makes no claim for an unavailable integration or future CI run.

| Gate | Result |
|---|---|
| HEB-113 schema/semantic/behavior fixtures | PASS — valid and invalid infrastructure profile, apply binding, delivery profile, release, workload, and routing-boundary cases |
| Complete local unit/integration suite | PASS — 78 tests; 1 Docker integration skipped because the local daemon was unavailable; both Terraform state-safety integrations passed |
| HEB-110 safety validator | PASS |
| Strict package/host validation | PASS — 13/13 skills with current retained routing identity and strict host validation |
| Clean installation | PASS — isolated install and reload discovered 13 skills |
| Release-profile routing | PASS — corrected full suite 141/141, 100%, zero excluded selections, $1.341287 |
| Diff/reference checks | PASS — compilation, JSON Schema validation, YAML loading through validators, reference/sample inventory, and `git diff --check` |
| Direct evidence-cited review | PASS — routing exposed and resolved one MATERIAL catalog-description ambiguity; no BLOCKING or MATERIAL findings remain |

## Integration limits

Terraform state-safety integration is available locally and must pass in the final suite. The local Docker daemon is unavailable; the container runtime integration must run unskipped in required CI. Protected GitHub Environment approval, WIF claim conditions, cloud plan/apply, registry attestation verification, application deployment, migration, hosted static headers, browser/synthetic checks, and rollback are consumer integration gates; repository fixtures and schemas validate their identities and fail-closed contracts without claiming that those external systems ran.

The completed failed calibration report identifies fixture `a1aa15bf77e35969e0d05e96bf6d29d3c15ce6ed8cbd8019e69375e9def9b6b0`, pre-correction catalog `586ef0ce45b7d4164038c9e3c0d0aa627a92184d25d888678f32fc6c88fd2eb7`, and policy `4e3aedf467f4d353a9903a31f8dfd3fa9224f01eb449a473051177b5f626b67d`. Its 137/141 result clears the aggregate threshold but fails the every-case and excluded-selection gates, so it is not eligible retained release evidence.

The description correction makes a non-Haffey IaC/cloud profile an explicit infrastructure-code rebind. The corrected complete replay passed 141/141 against fixture `a1aa15bf77e35969e0d05e96bf6d29d3c15ce6ed8cbd8019e69375e9def9b6b0`, catalog `36364fcd53f919edee9e4f44e90e33d0b79a9e6620b618e0e2941c24de4df19c`, and policy `4e3aedf467f4d353a9903a31f8dfd3fa9224f01eb449a473051177b5f626b67d`. The report is complete and eligible retained evidence.
