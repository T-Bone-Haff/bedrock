# Candidate-5 minimal custody — test definition

| Field | Value |
|---|---|
| Test ID | `C5-MIN-CUSTODY-1` |
| Status | FROZEN-PENDING-CLOSURE-VERIFICATION-AUTHORIZATION |
| Revision | 4 |
| Owner | Tad Haffey |
| Date | 2026-09-17 America/New_York |
| Population | exactly six demand rows, `C5M-1` through `C5M-6` |
| Review profile | none currently authorized; the completed supplemental direct check remains historical evidence |
| Reopening rule | any row addition, removal or semantic change creates revision 5 and a separately authorized review |

## Purpose and authority

This artifact freezes the complete review population for the Candidate-5 single-run custody design. It tests only HEB-154 evaluation of the `agent-code` skill. It makes no Agents of HEX overall-design decision and supplies no implementation, provider access, spend, calibration execution or launch authority.

The governing boundary is [`DDR-HEB-154-001`](DDR-HEB-154-001-candidate-5-custody-boundary-reset.md), SHA-256 `4d5b9557b43ec6433e477d50dd89ff357deb201cea196746a6f2251f7ffd16d1`, revision 5. The selected Candidate-5 population is bound by `evaluation/calibration/candidate-5/selection-disposition-1.json`, SHA-256 `f05e802a1d0411af9984e73381ec946b720d92bc42c9abcc0585e3041cdd02e2`; its blind manifest is SHA-256 `1a9a7ff9a2ffb2913970d0d883b9e1799979e1b778b8af6583f1328e04ec6cad` and its custodian-answer manifest is SHA-256 `6404e38b1260d070ae67b7c8b93a08e3dccf69cf032fd7b2e17a78c7841a0993`.

## Fixed demand matrix

Every row receives exactly one `confirmed`, `falsified` or `unavailable` outcome from each applicable stance. A falsified or unavailable row blocks a recommendation to accept the exact construct. Findings may cite more than one row, but no row may be inferred from finding silence.

| ID | Demanded property | Verdict-bearing inputs | Structural measurement | Falsification control | Required review evidence |
|---|---|---|---|---|---|
| `C5M-1` | The judge-visible package is a deterministic projection of all 50 selected Candidate-5 tasks and contains no answer-bearing member or resolvable answer reference. | exact Candidate-5 manifests, evaluator-input schema and proposed construct | recompute source and projected inventories, task order, member hashes, projection diff and forbidden-member/key scan | inject one custodian answer member and one `hidden_ground_truth_artifact` field; preparation must refuse both | complete population count, projection rule, source/projected roots and both refusal results |
| `C5M-2` | The evaluator can read only the judge-visible package, can write only its result volume and cannot reach answers, the repository, custody copies, host home or Docker control. | evaluator image/configuration, launch command and effective mounts | inspect image digest, UID, capabilities, network and complete mount set; execute allowed reads/writes and every denial probe | add one forbidden answer-canary mount and one writable blind mount; preflight must refuse launch | exact effective configuration plus positive and negative probe results |
| `C5M-3` | One exact run plan binds inputs, implementation, evaluator configuration, storage roots and exclusions; launch requires the operator to verify its hash, supply one passphrase and type the exact approval statement without managing a separate key. | run-plan schema/bytes, TTY transcript policy and launch wrapper | recompute plan hash; inspect passphrase channel and persisted artifacts; test exact approval grammar | wrong hash, denial, EOF, non-TTY input, passphrase in argv/environment/file/log or any persisted key must refuse launch | plan bytes/hash, structural transcript, refusal outcomes and a zero-secret scan |
| `C5M-4` | Evaluator outputs are complete, detached, verified, hashed and copied before answer material becomes available to comparison. | phase receipts, result image, comparison launch preconditions and process/mount evidence | verify exactly 50 terminal result envelopes, result-image integrity, primary/replica byte identity and event order | request comparison before result sealing and while evaluator access remains live; both must refuse | sealed-result receipt, ordered phase evidence and both refusal results |
| `C5M-5` | Exact judge-visible inputs, custodian answers, evaluator outputs and comparison results are retained as encrypted primary and verified replica images; restoring either copy reproduces the same complete inventory. | four encrypted image classes, copy receipts and inventory manifests | verify encryption flag, image integrity, ciphertext hashes, copy equality and full restore inventories from primary and replica | wrong passphrase, one-byte replica drift and missing-member image must each fail closed | identities for all images/copies, two restore inventories per class and three refusal results |
| `C5M-6` | Any access, identity, capture, image, copy or pre-seal failure stops the attempt, preserves available partial evidence and requires a new run ID; no same-run recovery path exists. | command surface, phase receipts, failure record and re-entry guards | enumerate commands/transitions; inject one failure in each named family and attempt same-ID re-entry | same-ID resume or comparison after any injected failure must refuse | complete injected-failure population, retained partial identities and new-ID requirement |

## Review boundary

The authority substrate is exactly this test definition; the proposed replacement construct; `DDR-HEB-154-001` revision 5; the Candidate-5 selection disposition; the blind and custodian-answer manifests; the evaluator-input, evaluator-result-envelope, evaluator-configuration, wire, verification-contract and run-manifest-identity schemas; and `physical-runtime-binding.md`. Any future verification freezes each artifact by exact SHA-256. Historical custody revisions and reviews may explain why the reset occurred but are not authority for importing a mechanism. Review charges, result schemas, validators and review input manifests are review instruments, not authority substrate; they are hash-frozen separately and are never compared with this authority list.

The completed supplemental direct check remains frozen at `reviews/candidate-5-minimal-custody-supplemental-direct-check-1/`. It falsified RC-3/C5M-2 and the AC-1/AC-3 interface; SD-1 and SD-2 are the ratified corrections. The six demand rows remain byte-for-byte unchanged. No closure audit, reviewer invocation or automatic next cycle is authorized by this revision. Any future verification must be separately authorized, freeze the then-current exact bytes and claim no more than its declared profile permits.

## Change log

| Revision | Date | Change |
|---|---|---|
| 1 | 2026-09-17 | Froze MB-1 through MB-5 as six reviewable custody demands for one bounded review. |
| 2 | 2026-09-17 | Added the exact physical-runtime and transitive schema authorities under C5-R0/AC-2; left `C5M-1` through `C5M-6` unchanged and bound one targeted closure review. |
| 3 | 2026-09-17 | Preserved all six demand rows byte-for-byte; separated review instruments from authority and bound the authorized two-stance supplemental direct check. |
| 4 | 2026-09-17 | Preserved all six demand rows byte-for-byte; recorded the completed failed direct check and SD-1/SD-2 ratification while leaving closure verification unauthorized. |
