# HEB-133 validation results

## Deterministic contract proof

| Gate | Result | Evidence |
|---|---|---|
| Focused authoring contracts | PASS | 10/10 tests; reconstructed Gate I reject/accept boundary, full instrument demand, taxonomy mismatch, touch-set omission, custody/reachability, premise controls, and success-as-absence counterfactuals behave as declared. |
| Authoring-contract validator | PASS | 5/5 interaction contracts plus required relay, template, reviewer-charge, and counterfactual carriers. |
| Rule-trigger audit | PASS | 55 Markdown carriers, 17 structured carriers, and 1,018 semantic units; six changed Markdown carriers re-read whole; zero internal-state findings and zero unresolved dispositions. |
| Package governance | PASS | Lifecycle, metadata, compatibility, policy, registry, context-budget, and evidence contracts. |
| Deterministic plugin validation | PASS | 13/13 skills. |
| Full repository suite | PASS | 120 tests under Claude Code 2.1.226; 119 passed and the locally unavailable Docker-daemon integration was skipped. Both Terraform integrations passed. |
| Strict host validation | PASS | Repository-pinned Claude Code 2.1.226, including the seeded malformed-frontmatter refusal. |
| Isolated install/reload | PASS | Candidate installed from an isolated marketplace and exposed 13 skills plus packaged governance. |
| PR-profile live routing | PASS | 54/54, every case 1.0, zero excluded selections, all policy gates true; pinned Claude Code 2.1.226 resolved `claude-haiku-4-5-20251001`; $0.496101. |
| Diff hygiene | PASS | `git diff --check` produced no findings. |

## Host-version diagnosis

The first full run used the locally installed Claude Code 2.1.233. Its strict plugin validator accepted the seeded malformed-frontmatter fixture, reproducing the host drift already retained under HEB-136. An isolated temporary 2.1.226 host passed the exact failing test and the complete suite. No repository repair is warranted for that external version difference, and the user's global Claude installation was not changed.

## Live routing

The first sandboxed PR-profile attempt failed in preflight on `agent-code-positive` with `transport_failure`, zero completed draws, zero cost, and no model response. Because it consumed no draw, it did not alter the preregistered population.

After explicit operator approval for Anthropic API egress, the complete PR profile ran once outside the restricted network sandbox. It passed 54/54 with overall and per-case rates of 1.0, zero excluded selections, all aggregate/case/exclusion/budget gates true, and no failed rows. The report identities are fixture `d776ecc3b69207d18b3ceafdefba3e57cb670eed3ce7e409347f75fb8db35eb1`, catalog `fb8111abc3095efb4baf3c9ee6a93e1dad94455ceda54cb0f5a3f065f7fce06e`, and policy `4e3aedf467f4d353a9903a31f8dfd3fa9224f01eb449a473051177b5f626b67d`. The exact report is retained at `docs/evidence/heb-133/routing-results.json` with SHA-256 `33e00d13d4ea7cd68eebec6bc351cf9b41db27350a871a9c27923299a441822d`.

## Current gate

The implemented amendment, deterministic gates, pinned-host checks, live routing, and direct review are green. The operator ratified the implementation findings and dispositions on 2026-08-26 ET, advancing the standard amendment from proving to adopted. Docker is unavailable locally but is not a changed boundary; repository CI remains the required pre-merge confirmation. The next gate is the exact allowlisted stage set and one-commit transaction.
