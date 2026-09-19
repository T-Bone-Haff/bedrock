# DDR-HEB-154-001: Reset the Candidate-5 custody design boundary

| Field | Value |
|---|---|
| Status | ACCEPTED |
| Revision policy | simple |
| Owner | Tad Haffey |
| Verification state | record identity and relation targets verified; SD-1 and SD-2 accepted after the completed supplemental direct check; exact corrected construct pending separately authorized closure verification |
| Review trigger | when closure verification is separately authorized, or when a governing test requirement changes |
| Supersession/retirement | retires revision 5 as an active design path without changing its historical bytes; this record remains current until superseded by an accepted boundary decision |

## Decision and context

Stop the amendment sequence for the Candidate-5 custody construct. Revision 5, exact SHA-256 `3d46c80e2ab7a24e75fcd501e32003115d5c927ec975a23d68cb431ae9592233`, is retained unchanged as historical design-and-review evidence but is no longer an active basis for amendment, ratification or implementation. Its acceptance schema and executable validator are likewise historical and must not be run to propose, complete or validate ratification. No revision 6 may be produced by applying the review-5 fixes to that construct.

Revision 1 recorded Tad Haffey's 2026-09-17 America/New_York statement, `agree to continue with that reset`, following analysis of the five review rounds. It accepted the boundary reset and the method below without accepting a replacement custody design. Revision 2 records the separately presented and accepted minimal replacement boundary. Revision 3 records the separately presented and accepted closure dispositions following the first bounded actor pass and host verification. Revision 4 records the finite corrective packet and two-stance supplemental direct check authorized after the targeted closure review. Revision 5 records the two bounded corrections accepted after that direct check.

The replacement starts from the governing test need and a blank dependency graph. It must keep three concerns separate:

1. stable test-definition evidence invariants;
2. a single-run operator custody procedure; and
3. reusable lifecycle machinery, deferred until repeated use demonstrates a need.

The current phase excludes permanent-finality machinery, real-evidence deletion, retention release, passphrase-compromise migration, generalized same-run recovery and executable validation of review history. Design acceptance is an external, human-readable statement bound to exact artifact hashes and one bounded review against a frozen demand matrix; design-review machinery is not embedded in the custody construct.

## Ratified minimal replacement boundary

Tad Haffey's 2026-09-17 America/New_York statement, `Ratify MB-1 thr MB-5`, accepts:

- **MB-1 — proof objective:** prove only that Candidate-5 calibration can run without the evaluator receiving answer-bearing material before sealed comparison, while retaining enough exact evidence to review the first result.
- **MB-2 — minimum custody invariants:** separate blind inputs from answers; give the evaluator read-only access only to blind material; freeze evaluator outputs before comparison; retain exact inputs, outputs and comparison evidence in encrypted primary and verified replica copies.
- **MB-3 — operator action:** at execution the operator provides one passphrase, verifies the presented package hash and explicitly approves launch; the operator does not track or manage encryption keys separately.
- **MB-4 — failure behavior:** any access violation, identity mismatch, capture failure, encryption/copy failure or pre-seal crash stops the attempt; preserve partial evidence and use a new run identity, with no generalized same-run recovery.
- **MB-5 — artifact and review boundary:** create one stable test-definition artifact and one Candidate-5 single-run procedure; defer reusable lifecycle machinery; freeze a small demand matrix before one bounded review; keep review-history validation external and human-readable.

This ratification authorizes replacement authoring and the bounded review. It is not acceptance of the exact construct text produced by that authoring.

## Ratified closure dispositions

Tad Haffey's 2026-09-17 America/New_York statement, `ratify C5-R0, C5-R1, AC-1 through AC-4, and the targeted closure review`, accepts:

- **C5-R0 — instrument-boundary correction:** revise only the test definition's review-substrate list to include the exact physical-runtime authority already cited by the construct and the exact external schemas required by AC-2. The six demand rows `C5M-1` through `C5M-6` do not change.
- **C5-R1 — passphrase ownership:** one short-lived custody-supervisor process prompts once and retains the passphrase only in process memory for every passphrase-bearing host operation through retained-evidence verification. Evaluator and comparator processes never receive it. The mutating command surface is one `run` command; `inspect` is read-only. Supervisor exit before the retained receipt permanently fails that run identity.
- **AC-1 — prerequisite authority binding:** the closed run plan binds the exact evaluator/provider configuration, provider-relay contract, pricing artifact, spend authorization and calibration-launch authorization. Custody approval grants none of them, and a missing, stale, mismatched or unauthorized prerequisite prevents plan admission and launch.
- **AC-2 — schema and run identity closure:** freeze every external schema required by the evaluator input and result envelope, including wire, verification-contract and run-manifest-identity, and bind both the semantic manifest digest and exact manifest-file SHA-256.
- **AC-3 — atomic run-identity consumption:** create and durably flush a create-once evaluator-start marker before container creation. That marker or any later artifact permanently prevents same-ID re-entry.
- **AC-4 — one writable evaluator surface:** remove the separate writable `/tmp` tmpfs. Temporary evaluator writes live only under `/run/out/tmp` inside the encrypted result volume.
- **Targeted closure review:** after those changes are codified as one construct revision, perform one separately authorized multi-perspective review against the one instrument defect and five canonical design defects identified by the first actor pass. The review keeps the six-row demand matrix unchanged, admits no exploratory expansion and does not authorize another automatic revision or review.

These dispositions accept the design directions and their bounded review, not the exact revised construct bytes, implementation, provider access, spending, calibration execution or launch.

## Ratified corrective closure packet

Tad Haffey's 2026-09-17 America/New_York statement, `ratify RC-0 through RC-4 and authorize the two-stance supplemental direct check`, accepts:

- **RC-0 — authority/instrument separation:** the supplemental review profile lists domain authority separately from review instruments. Both populations are hash-frozen; only domain authority is compared with the test definition's authority boundary.
- **RC-1 — launch-edge freshness:** prerequisite validation remains before plan presentation. After exact operator approval and immediately before durable run consumption, the supervisor re-reads the exact pricing, spend-authorization and calibration-launch-authorization bytes and revalidates their identities, scope and current time. The remaining authorization interval must cover the declared launch-admission window. Drift, mismatch or expiry discards the in-memory passphrase, creates no start marker and refuses launch.
- **RC-2 — dedicated passphrase pipe:** the sole permitted passphrase-bearing child channel is one dedicated standard-input pipe to the exact `/usr/bin/hdiutil` child. The supervisor writes the passphrase and immediately closes the pipe's write end; it retains no reusable descriptor. No other child, inherited descriptor, environment, argument, file, log or model input receives the passphrase.
- **RC-3 — complete writable-surface proof:** `/run/out` is the sole writable regular-file tree. Container IPC is disabled so `/dev/shm` is not mounted; device and mqueue mounts are prohibited; the evaluator runs non-root without capabilities. The preflight wrapper inventories the complete effective mount table and negatively probes every effective regular-filesystem mount and known Docker runtime surface outside `/run/out`. Any writable regular-file result refuses evaluator execution. Device-node semantics are reported separately and never counted as retained file storage.
- **RC-4 — exact phase boundary:** static plan and launch checks precede approval; RC-1 revalidation follows approval; the durable create-once marker then consumes the run identity; the evaluator container is created stopped and host-inspected. On container start, a frozen trusted preflight wrapper—not the evaluator workload—performs the in-container RC-3 inventory and probes before importing, invoking or executing evaluator code. Only a successful proof permits the wrapper to `exec` the evaluator. Any failure after the marker destroys the container when possible, preserves evidence, writes `failed.json` when possible and permanently fails the run identity.
- **Supplemental direct check:** one isolated `SA` invocation checks RC-1 through RC-3 and `C5M-2`/`C5M-3`; one isolated `cross-set` invocation checks RC-0, RC-4 and the AC-1/AC-3/phase-sequence interface. Both receive the same frozen corrected bytes, may not expand scope, and receive no repair or rerun inside the check.

The stopped-container wording in RC-4 is made executable without changing its safety intent: host inspection occurs while stopped; runtime probes require starting only the trusted preflight wrapper; “evaluator launch” means the later wrapper-to-evaluator `exec`. This packet authorizes that codification and the named check only. It does not accept the exact corrected construct bytes or authorize implementation, provider access, spending, calibration execution or launch.

## Ratified supplemental dispositions

Tad Haffey's 2026-09-17 America/New_York statement, `ratify SD-1 and SD-2`, accepts:

- **SD-1 — consume one complete prerequisite snapshot:** after approval and before the create-once marker, the supervisor re-reads and revalidates every AC-1 prerequisite byte, captures those exact verified bytes as the in-memory launch snapshot and derives every launch input only from that snapshot. It never reopens a prerequisite path for launch. Any path re-read, byte drift, identity/scope/time mismatch or inability to bind runtime consumption to those captured bytes refuses before run consumption.
- **SD-2 — close descriptor-backed persistence:** the effective Docker configuration uses and proves logging driver `none`. As the frozen wrapper's first operation, before it emits output or loads evaluator code, it binds standard output and standard error to create-once regular files under `/run/out`, then proves `/proc/self/fd/1` and `/proc/self/fd/2` resolve to those files. Any mismatch refuses evaluator execution. The boundary receipt records the effective log configuration and descriptor targets.

These corrections close only the two blocking omissions reported by the supplemental direct check. They do not alter the six test demands, the one-passphrase/one-approval operator experience or the already-closed RC targets. This ratification authorizes one construct amendment. It does not authorize the recommended host closure audit, another reviewer, exact-byte design acceptance, implementation, provider access, spending, calibration execution or launch.

## Rationale and alternatives

Five reviews reduced the defect count but did not converge. Later defects clustered in mechanisms introduced to repair earlier findings, especially finalization, deletion and executable design-acceptance machinery. The review profile exposed real problems, but it was being used as an iterative design generator despite making no convergence claim. The root cause was amendment-by-accretion at the wrong authority layer, not merely incomplete reviewer feedback.

Continuing to revision 6 was rejected because it would preserve the same dependency graph and add another local repair. Ratifying revision 5 with exceptions was rejected because three blocking design defects remained. Discarding the evidence was rejected because the review lineage is the proof for stopping. The selected reset preserves that evidence while removing its active authority.

## Design contract

- The revision-5 file, its acceptance schema and validator, and all five review sets remain immutable historical evidence.
- A replacement may import a prior requirement only after tracing it to a still-current governing test need; prior mechanism shape is not authority.
- The replacement boundary must be presented for explicit operator ratification before construct authoring.
- The demand matrix must be fixed before the replacement review begins. One bounded review evaluates that fixed population; any later expansion is a new review, not silent continuation.
- If the same semantic defect family recurs after the reset, work stops for another boundary analysis rather than beginning another amendment cycle.

## Conditions and migration

The transition is documentary only: the repository index points to this decision as the current custody-design status, while the retired construct and its review artifacts remain at their existing paths. There is no runtime cutover and no rollback action.

This decision authorizes the SD-1/SD-2 construct amendment. Closure verification remains a separate gate. It does not authorize implementation, provider access, spending, calibration execution, launch, evidence deletion, permanent final freeze, actual passphrase/key handling or a completed custody claim.

## Risk domains and verification

- **Security and privacy:** no runtime access or data movement is authorized. The future replacement must still prove evaluator answer denial and evidence custody for the synthetic test population.
- **Compliance:** no additional compliance claim is made; the evidence remains synthetic and governed by the existing HEB-154 authority set.
- **Cost:** the reset incurs no provider or campaign spend and removes premature lifecycle machinery from the current phase.
- **Operational:** retiring the active path can create stale references. Verification therefore checks the repository index, exact hashes, relation targets and absence of any claim that revision 5 is ratified or implementation-ready.
- **Empirical floor:** the diagnosis rests on one design lineage with five review rounds. That is enough to stop this lineage, but not evidence that the replacement method generalizes to other designs.

## Typed relations

The companion relation document is [`DDR-HEB-154-001-candidate-5-custody-boundary-reset.relations.json`](DDR-HEB-154-001-candidate-5-custody-boundary-reset.relations.json).

## Change log

| Revision | Date | Change |
|---|---|---|
| 1 | 2026-09-17 | Accepted boundary reset; retired revision 5 as an active design path while preserving its bytes and reviews. |
| 2 | 2026-09-17 | Accepted MB-1 through MB-5 and authorized replacement authoring plus one bounded review. |
| 3 | 2026-09-17 | Accepted C5-R0, C5-R1 and AC-1 through AC-4; authorized one targeted closure review under the unchanged six-row demand matrix. |
| 4 | 2026-09-17 | Accepted RC-0 through RC-4 and authorized one SA plus one cross-set supplemental direct check against the unchanged six-row demand matrix. |
| 5 | 2026-09-17 | Accepted SD-1 and SD-2 and authorized their bounded construct amendment; did not authorize closure verification or design acceptance. |

<!-- STANDING: prior published rows are frozen; amend the current unpublished row in place. -->
