# HEB-109 validation results

This record is populated from fresh commands on the completed branch. It does not pre-claim live model evidence.

## Deterministic contract

- Seeded package defects: pass; all isolated negative cases produced their expected diagnostics.
- Test suite: 46 passed, one local Docker-daemon skip.
- Package and strict host validation: pass, 13/13 skills.
- HEB-110 safety regression: pass; Terraform runtime-state fixtures executed locally, while Docker remains a required CI check.
- Clean install/reload: pass, 13 skills discovered from an isolated marketplace and plugin directory.

## Nondeterministic routing contract

The preregistered policy is `validation/eval-policy.yaml`. The full `release` profile ran on 2026-08-10 through Claude Code 2.1.226 using `claude-haiku-4-5-20251001`:

- 37 cases × 3 independent draws = 111/111 passed;
- direct, implicit, adversarial, positive, negative, and overlap strata each passed at 100%;
- zero excluded-route selections;
- full-suite completion and retained-evidence eligibility both true;
- total model cost: $0.976117.

The retained report is `routing-results.json`. Its fixture SHA-256 is `846bca124ebd643750db5c8f5bb6514c05bfe8bb14c664bb36e0f55b7346f541`, catalog SHA-256 is `c853d3119f299504534849a9dcb12c5505b8153abb3fbd83fb8da5ae63d47bb1`, and policy SHA-256 is `4e3aedf467f4d353a9903a31f8dfd3fa9224f01eb449a473051177b5f626b67d`.
