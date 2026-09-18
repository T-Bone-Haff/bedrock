# Candidate-5 minimal custody — supplemental direct-check aggregation

- Date: 2026-09-17 America/New_York
- Profile: one SA plus one cross-set direct check; not runner-backed
- Frozen construct SHA-256: `459c4a93fa3f9048f31478a70ee1889dba475d828cc174c380c7eba8af3ea1fb`
- Actor results: two valid isolated outputs
- Source findings: 2 — 2 BLOCKING
- Canonical defects: 2 — 2 BLOCKING
- Status: two-stance supplemental direct check completed; exact design remains NOT READY
- Claim limit: no convergence, implementation-readiness, launch-readiness or design-acceptance claim

## Complete source accounting

Both source findings are unique and appear exactly once.

| Finding ID | Stance | Targets | Disposition |
|---|---|---|---|
| `ca41c23463c9e226eaa315edc4f970be81c8a898479d99e6e7a55f15f94bb4a1` | SA | `RC-3`, `C5M-2` | open BLOCKING — stdout/stderr and the effective Docker logging driver are outside the specified writable-surface proof |
| `a483dab16a88cee4e058406b9c7dc0f55afc2748bf774bfb68dd241918c981f0` | cross-set | `AC1-AC3-INTERFACE` | open BLOCKING — the launch-edge refresh covers only three members of the complete AC-1 prerequisite population |

## Assigned-target accounting

| Target | Assigned stance | Outcome | Basis |
|---|---|---|---|
| `RC-0` | cross-set | closed | authority and review-instrument populations are separated and independently hash-frozen |
| `RC-1` | SA | closed | pricing, spend and launch bytes are refreshed after approval with scope/time/window checks |
| `RC-2` | SA | closed | each exact `hdiutil` operation receives one fresh, immediately closed stdin pipe and no other passphrase channel |
| `RC-3` | SA | falsified | mount/path probes do not cover descriptor-backed Docker log persistence |
| `RC-4` | cross-set | closed | marker, stopped-container inspection, trusted-wrapper proof and evaluator `exec` form an executable fail-stop sequence |
| `C5M-2` | SA | falsified | evaluator output can persist through Docker stdout/stderr logging outside `/run/out` |
| `C5M-3` | SA | closed | one plan, one passphrase and one approval remain fail-closed under the assigned attacks |
| `AC1-AC3-INTERFACE` | cross-set | falsified | several AC-1 prerequisite bytes can drift before AC-3 consumes the run identity |

## Root cause and boundary

The reviewers completed every assigned target; neither stopped short. The two failures expose different omitted I/O edges in revision 3:

1. **Mutable-input edge:** RC-1 named the three time-sensitive artifacts, but the construct's broader invariant said every prerequisite was launch-edge current. The operative step did not either re-read the remaining AC-1 bytes or require launch to consume the same immutable snapshot that was verified.
2. **Descriptor edge:** RC-3 expanded filesystem mounts but treated writable persistence as path-only. Docker can persist evaluator stdout/stderr through its logging driver even when every in-container mount probe passes.

These are bounded omissions in the consolidated mechanics, not evidence of a new custody lifecycle or a need to reopen the six-row test definition. The empirical floor remains one construct lineage; the result supports correcting these two exact edges, not generalizing a new standard.

## Recommended next disposition — not authorized

- **SD-1 — consume one complete prerequisite snapshot:** after approval and before the create-once marker, re-read and revalidate every AC-1 prerequisite byte—not only the three time-sensitive artifacts—and construct launch inputs only from that captured, hash-verified snapshot. Any path re-read, drift, mismatch or inability to bind runtime consumption to those exact bytes refuses before run consumption.
- **SD-2 — close descriptor-backed persistence:** set and host-verify Docker logging driver `none`; before any evaluator code or output, bind standard output and error to files under `/run/out`, prove `/proc/self/fd/1` and `/proc/self/fd/2` resolve within `/run/out`, and refuse otherwise. The boundary receipt records the effective log configuration and descriptor targets.

My recommendation is to ratify SD-1 and SD-2, amend revision 3 once, and use a host closure audit that checks only the two exact finding claims and their cited loci. Do not commission another open-ended or multi-stance review. If the literal clauses and hash bindings close both findings, present that exact construct hash for design acceptance; if either does not, stop and return the unresolved claim without another automatic amendment.

No amendment, implementation, provider access, spend, passphrase handling, calibration execution, launch or design acceptance is authorized by this aggregation.
