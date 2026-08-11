# HEB-114 direct review

Status: **finished-diff standard review complete; implementation and required
local evidence are acceptable for the authorized remediation commit and push.
The repaired pushed-CI population remains a required merge gate.**

Review input was the full 58-file candidate against
`origin/main@6e57f2b3df7aa5c28eb26dec339a00c91b2e5288`, including every untracked
exclusive file, all modified shared files, the unchanged shared boundaries,
and final local gate evidence. The workflow was reviewed with both
`frontend-code` gate-semantics and `app-delivery-pipeline` placement,
permissions, evidence-retention, failure-isolation, and topology overlays.

## Direct findings

| ID | Stance | Class | Finding | Disposition |
|---|---|---|---|---|
| HEB114-DR-001 | LAA | Positive architecture | The portable core, Haffey profile, task-shaped references, component/state/data boundaries, capability semantics, prototype outcomes, and sibling handoffs implement the ratified architecture without retaining stack choices in the portable core. | No implementation finding. |
| HEB114-DR-002 | SA | Resolved security | The initial Vite 8.0.0 lock selected a release with a high-severity development-server advisory. | Re-pinned to Vite 8.2.1; full and runtime-only audits now report zero known vulnerabilities. |
| HEB114-DR-003 | LAA/SA | Resolved correctness | The executable disposable registry stopped after the first throwing disposer, contradicting deterministic cleanup on failure and leaking later resources. | A meaningful-red regression reproduced the defect. The registry now clears ownership, attempts every disposer, aggregates errors, and passes 5/5 component tests with 100% statement/line/function and 97.05% branch coverage. |
| HEB114-DR-004 | SA/EA | Resolved evidence | The initial workflow disabled npm's implicit audit without adding an explicit advisory gate and discarded coverage/Playwright JSON. | Added an explicit high-severity audit and pinned upload-artifact retention inside the existing deterministic job. Topology remains `deterministic → live-routing`; no deployment, hosting, or artifact-promotion machinery was added. |
| HEB114-DR-005 | EA | Resolved evaluation | The first new backend-enforcement prompt demanded impossible server enforcement inside a React client, producing two correct `null` selections and a 160/162 failed observation. | Debugging isolated a fixture-specification defect. The repaired adversarial prompt asks for implementation in the owning application layer; a non-retained targeted probe passed 3/3 and a fresh full identified suite passed 162/162 with zero excluded selections. Failed/targeted observations were not pooled. |
| HEB114-DR-006 | SA | Resolved evidence | The required representative Safari + VoiceOver flow was initially unavailable because macOS Computer Use permission was absent. | After permission was granted, the named Safari/VoiceOver population passed: keyboard focus visibly reached `Open details`, activation changed the view, and accessibility focus moved to `Details ready`. Exact audible wording and broader manual populations remain explicitly unclaimed. VoiceOver was restored to off. |
| HEB114-DR-007 | EA | Required downstream gate | The workflow preserves HEB-113's topology and ownership. Its configured Ubuntu/Node 22.12.0 browser population and retained artifact upload have not run because push/PR is outside the current authorization. | Expected pre-push unavailable gate; require green CI without browser skips before merge. |
| HEB114-DR-008 | EA | Environmental | The 82-test suite passes locally with one Docker integration skipped. Requiring Docker produces exactly one unavailable-daemon failure; Terraform-required integration passes. | Require the existing Docker integration unskipped in CI; no frontend code or workflow-topology defect is inferred. |
| HEB114-DR-009 | EA | Resolved evaluation | The first pushed candidate's review-shaped prototype-promotion prompt selected `code-review` in one PR draw. A later full release observation also showed that a conflicting named-skill preference could yield `null` even when another catalog entry authorized the underlying operation. | Rephrased prototype promotion as an operation-first frontend request. Kept the pre-existing adversarial fixture unchanged and repaired the adapter contract so user skill preferences cannot override catalog ownership or erase an otherwise authorized operation. Targeted probes passed 3/3; a fresh full population passed 162/162 with zero excluded selections. Added `$0.06` per-call and `$3.00` aggregate budget enforcement without changing workflow topology. |

## Gate dispositions

| Gate | Disposition |
|---|---|
| Frontend schemas, semantic negatives, behavior ownership, and browser fixture contract | Passed |
| Full Python suite | Passed locally: 82 tests, one Docker-only skip |
| Docker-required integration | Unavailable locally; required in CI |
| Terraform-required integration | Passed |
| HEB-110 and HEB-113 validators | Passed |
| Strict package/host validation and isolated install | Passed: 13/13 skills |
| Dependency install and full/runtime advisory audits | Passed: exact lockfile, zero known vulnerabilities |
| Type, lint, component, coverage, build, and bundle budget | Passed |
| Chromium, Firefox, and WebKit browser/security/accessibility/performance population | Passed: 21/21, zero skips |
| Release routing evaluation | Passed: 162/162, zero excluded, candidate identities match; `$1.438027` under enforced `$3.00` aggregate ceiling |
| Manual Safari + VoiceOver representative flow | Passed with exact identity and limitations retained |
| Pushed GitHub Actions population | Prior candidate deterministic job passed and live routing failed; repaired candidate must rerun both jobs after the authorized push |

## Verdicts

- **LAA:** implementation architecture and finding coverage are acceptable;
  no open correctness or architecture defect remains. Verdict `approve` for
  the authorized remediation commit and push.
- **SA:** application-side security, dependency posture, and the bounded manual
  accessibility evidence are acceptable; no open code-security or required
  local evidence defect remains. Verdict `approve` for the authorized
  remediation commit and push.
- **EA:** ownership, workflow topology, routing identity, and retained package
  evidence conform. The actual delta changes portable authority, binding,
  failure/evidence behavior, schemas, and routing incompatibly, so
  `7.0.0 → 8.0.0` remains package-major. Verdict `approve` for the authorized
  remediation commit and push; repaired-candidate CI remains a mandatory merge
  gate.

Overall review verdict: **APPROVE the authorized remediation commit and push**.
Local Docker remains an environmental unavailable check and repaired-candidate
CI remains a mandatory merge gate; neither is silently treated as passed.
