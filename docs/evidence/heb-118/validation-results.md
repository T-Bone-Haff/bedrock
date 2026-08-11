# HEB-118 validation results

## Candidate identity

- source baseline: `e3073d11aca23d88b32fcdb7f342cd90bab439e8`
- candidate manifest: `8.1.0`
- migration: compatible additive package-governance surface; no skill identity,
  routing owner, input/output/evidence contract, supported Claude Code host, or
  safety-floor break
- release decision: intentionally unavailable until HEB-119

## Local gates

| Gate | Result | Evidence |
|---|---|---|
| Package governance | PASS | lifecycle, metadata, license, compatibility, policies, authority inventory, vocabulary/schema parity, context budgets, finding reconciliation, and evidence paths |
| Seeded governance defects | PASS | manifest/license/version drift, orphaned/retired lifecycle, consumer enumeration, vocabulary drift, duplicate authority, stale context evidence, missing finding, broken link, and premature release all fail closed |
| Final release simulation | PASS | temporary Git repository with an annotated tag plus external release/rollout exports satisfies `--release`; missing exports fail closed |
| Integrated package validator | PASS | 13/13 deterministic and native strict-host validation |
| Unit and integration suite | PASS | 97 tests; Docker image start/health and Terraform state proofs executed with required-gate flags; no skips |
| Safety | PASS | HEB-110 package safety contract |
| Domain contracts | PASS | authoring, agent/review, application/testing/debug, infrastructure/delivery, and frontend validators |
| Isolated install/reload | PASS | installed `8.1.0` exposes 13 skills and contains manifest, license, changelog, registry, lifecycle, release-evidence, and rollout-ledger contracts after reload |
| Retained routing | PASS, reused | current fixture/catalog/policy identities remain identical to the retained 162/162 population with zero excluded selections; HEB-118 changes no skill description or routing fixture |
| Context budget | PASS | 6,824 catalog description characters; 9,692 progressively disclosed entrypoint words; largest entrypoint 958 words; Claude Code projects about 1,785 always-on tokens |
| Candidate release mode | EXPECTED FAIL | no HEB-119 evidence, immutable `v8.1.0` tag, GitHub release, or completed rollout ledger exists; the final gate refuses closure |

The final pre-staging population passed in full. Pull-request CI remains
mandatory for Linux Docker/Terraform,
Playwright Chromium/Firefox/WebKit, dependency audit, strict host validation,
isolated installation, and authenticated PR routing. Those CI-only results are
linked in the HEB-118 close-out; this file does not predict them.

## Retained evidence and limitations

- `manifest.yaml` reconciles every `PKG-001–039` identity exactly once.
- `context-budget.json` is recomputed by the validator and fails on drift.
- Claude.ai propagation behavior is documented, but the full new-session
  13-skill cold inventory remains an HEB-119 acceptance obligation.
- HEB-118 does not create the tag, GitHub release, or rollout ledger and cannot
  clear the HEB-106 release pause.
