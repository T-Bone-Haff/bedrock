# HEB-108 Wave 1 validation results

Validated on 2026-08-09 from branch `feature/heb-108-wp1-recovery-restore-plugin-loadability-and-routing-metadata`, based on `aa772938f50cedc498a4917422961162bc09b9b2`.

## Passing local evidence

| Check | Result |
| --- | --- |
| `claude plugin validate --strict plugins/bedrock` through `scripts/validate_plugin.py` | Pass: 13/13 skills |
| Description limit | Pass: all descriptions ≤1,024 characters |
| Positive/negative fixture coverage | Pass: every skill covered |
| Shared routing fixture inventory | Pass: 31 cases, including five overlaps |
| Seeded validator and adapter tests | Pass: 13 tests |
| Seeded invalid frontmatter through the strict host validator | Pass: known defect is rejected |
| Isolated marketplace install and first discovery | Pass: 13 skills discovered |
| Second-process reload discovery | Pass: inventory unchanged, 13 skills discovered |
| Workflow syntax (`actionlint`) | Pass |
| Smoke script lint (`shellcheck`) | Pass |
| Python compilation | Pass |
| Diff whitespace check | Pass |
| Independent description-level forward-routing review | Pass: 31/31 declared routes |
| Targeted authenticated routing remediation | Pass: 18/18 runs |
| Full authenticated routing regression | Pass: 93/93 runs (31 cases × 3) |

Host validation, install evidence, and live routing used Claude Code 2.1.224. Live routing resolved `haiku` to `claude-haiku-4-5-20251001`; the exact-final full run cost $0.805925 and is retained in `routing-results-final.json`. The 18-run remediation proof is retained in `routing-remediation-targeted.json`; the initial 83/93 run is retained in `routing-results.json` as falsification evidence. The metadata inventory is retained in `metadata-inventory.json`; the pre-repair state is retained in `baseline.md`.

## Open acceptance gates

- The pull-request workflow has not run because no commit or push is yet authorized.
- Repository branch protection has not yet been verified to require `Plugin validation / live-routing`.
- The plugin manifest bump was derived from disk and applied under the separately ratified landing transaction.

These open gates prevent claiming HEB-108 complete.
