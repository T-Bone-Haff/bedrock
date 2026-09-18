# Candidate-5 minimal custody — host closure-audit profile

- Date: 2026-09-17 America/New_York
- Authorization: Tad Haffey's statement `proceed with the audit`
- Profile: one literal host closure audit; direct review; not runner-backed
- Actor: current host only; no reviewer agents or independent stance calls
- Permitted completion claim: `host closure audit completed`
- Prohibited claims: convergence, whole-design review, implementation readiness, runtime proof, launch readiness or design acceptance
- Data classification: synthetic HEB-154 design and review metadata; no credentials, passphrase or provider content
- Tools: read-only local inspection, deterministic hashing/parsing and repository-local audit evidence writes
- Network/provider/spend/runtime budget: none
- Repair/retry: no design repair, reviewer retry or additional audit target inside this audit
- Evidence location: this directory

## Frozen authority substrate

| Artifact | SHA-256 |
|---|---|
| `DDR-HEB-154-001-candidate-5-custody-boundary-reset.md` | `4d5b9557b43ec6433e477d50dd89ff357deb201cea196746a6f2251f7ffd16d1` |
| `candidate-5-minimal-custody-test-definition.md` | `7f850b4c26e034a2472c19a9109e18df73b11398e09c99ec08d42fbcab266b02` |
| `candidate-5-minimal-custody-construct-spec.md` | `464b52c4f05959796b2e2819430f88c52dbd9055d3210f167f8693ccf24efeca` |
| `physical-runtime-binding.md` | `41b640517da9fd6879e610e72f7e270460152c424c5fb84df811260b6b266a06` |

All authority paths are relative to `docs/evidence/heb-154/agent-code-v2/`.

## Frozen target evidence

These are prior review evidence, not design authority:

| Artifact | SHA-256 |
|---|---|
| `reviews/candidate-5-minimal-custody-supplemental-direct-check-1/sa-result.json` | `09eb9ef8575cfd98d3d7e53f6f47444bc456f0ed81a7fa874267fbb74a70a2fb` |
| `reviews/candidate-5-minimal-custody-supplemental-direct-check-1/cross-set-result.json` | `9e625f3467f4bd2a50b2e873a2d1eec58fc97259fdc1e90225e429025c0ab285` |
| `reviews/candidate-5-minimal-custody-supplemental-direct-check-1/aggregation.md` | `bb22e3b523ee925f9a04aa13e897ce77a3375939395e1c48a7ec82641fdfbfd3` |

## Exact audit population

The audit decides only whether revision 4's literal design clauses close these two retained findings:

1. `a483dab16a88cee4e058406b9c7dc0f55afc2748bf774bfb68dd241918c981f0` — incomplete launch-edge coverage of the AC-1 prerequisite population before AC-3 consumption.
2. `ca41c23463c9e226eaa315edc4f970be81c8a898479d99e6e7a55f15f94bb4a1` — evaluator stdout/stderr and Docker logging can persist bytes outside `/run/out` while mount probes pass.

No other demand, defect or design surface may be opened. Absence of a new finding is not a whole-design assurance.

## Required closure checks

### HCA-1 — complete launch-consumed prerequisite snapshot

- `HCA1-POPULATION`: the post-approval population enumerates every AC-1 prerequisite and every owning schema/contract.
- `HCA1-CAPTURE`: after approval and before the marker, every named regular file is no-follow re-read, captured, hashed, parsed and revalidated for identity, scope and time.
- `HCA1-CONSUME`: command, configuration, relay and every launch input are derived only from the captured bytes; no prerequisite path is reopened or separately parsed for launch.
- `HCA1-FAIL`: drift, re-read, missing/non-regular input, mismatch, expiry, inadequate interval or snapshot-to-launch failure refuses before marker/container creation.
- `HCA1-MARKER`: the exact phase order puts snapshot verification before AC-3 consumption and the marker binds the complete snapshot digest.

### HCA-2 — descriptor-backed persistence closure

- `HCA2-LOGGING`: the stopped-container effective configuration requires Docker logging driver exactly `none`, no options, and host verification.
- `HCA2-SILENCE`: the trusted wrapper emits no byte to inherited standard output/error before rebinding them.
- `HCA2-REBIND`: file descriptors 1 and 2 are create-once/no-follow bound to regular files on `/run/out`, originals closed, and evaluator `exec` preserves them.
- `HCA2-PROVE`: `/proc/self/fd/1` and `/proc/self/fd/2` must resolve within `/run/out`; the boundary receipt records canonical targets and effective logging configuration.
- `HCA2-FAIL`: any logging, open, type, mount, replacement, resolution or receipt failure prevents evaluator execution and follows permanent post-marker failure behavior.

Each requirement receives `satisfied`, `not_satisfied` or `unavailable`. A finding closes at the design-text layer only if all five requirements are satisfied from the frozen authority. Otherwise it remains open. Runtime feasibility and enforcement remain future implementation/verification obligations.

## Evidence and completion

`audit-input-manifest.sha256` freezes authority, target evidence and audit instruments; `audit-input-manifest.digest` freezes that manifest. `audit-result.json` must validate with `validate_host_audit.py`. The report preserves both finding outcomes and the claim boundary. The audit may state only that the host closure audit completed and whether each exact finding is closed in the frozen design text.
