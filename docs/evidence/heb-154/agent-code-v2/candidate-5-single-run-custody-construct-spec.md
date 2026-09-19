# Candidate-5 single-run custody construct specification

| Field | Value |
|---|---|
| Document ID | `C5-MIN-CUSTODY-CONSTRUCT-1` |
| Status | ACCEPTED-DESIGN |
| Revision | 5 |
| Owner | Tad Haffey |
| Review trigger | before implementation, or upon any change to a design clause, obligation or cited authority |
| Doctype ruling | construct spec: one internal single-run custody mechanism that a cold implementer must build without conversation |
| Deliberation substrate | `DDR-HEB-154-001` revision 5, `C5-MIN-CUSTODY-1` revision 4, C5-R0/C5-R1/AC-1 through AC-4, RC-0 through RC-4, SD-1/SD-2 and `C5-HOST-CLOSURE-AUDIT-1` |
| Accepted design source | `candidate-5-minimal-custody-construct-spec.md` revision 4, SHA-256 `464b52c4f05959796b2e2819430f88c52dbd9055d3210f167f8693ccf24efeca`, frozen at Git commit `d94641b5186359560715955a978046cf0bce18fd` |
| Acceptance evidence | `reviews/candidate-5-minimal-custody-host-closure-audit-1/audit-result.json` plus `candidate-5-single-run-custody-design-acceptance.md` |
| Supersedes | `C5-MIN-CUSTODY-CONSTRUCT-1` revision 4 as active design; the exact reviewed source remains immutable evidence |

## Purpose and scope

Build one narrow procedure that can execute a Candidate-5 evaluator calibration without giving the evaluator answer-bearing material before sealed comparison and can retain exact first-result evidence for review. One short-lived custody-supervisor process prepares and executes the entire attempt, obtains one explicit operator approval, executes one evaluator identity, seals its first results, performs one offline comparison and retains encrypted copies. A failed attempt is never resumed under the same run identity.

The later implementation lives at `evaluation/calibration/candidate-5/custody-single-run/` and exposes one entry point, `candidate_5_custody_run.py`, with one mutating `run` command and one read-only `inspect` command. Each `run` invocation owns one run identity from preparation through retained-evidence verification. It is not a general custody service, retention system, workflow engine or reusable review-history validator.

### Authorities and preserved invariants

- [`DDR-HEB-154-001`](DDR-HEB-154-001-candidate-5-custody-boundary-reset.md), SHA-256 `4d5b9557b43ec6433e477d50dd89ff357deb201cea196746a6f2251f7ffd16d1`, revision 5 accepts MB-1 through MB-5, C5-R0, C5-R1, AC-1 through AC-4, RC-0 through RC-4 and SD-1/SD-2 and authorizes this bounded amendment only.
- [`C5-MIN-CUSTODY-1`](candidate-5-minimal-custody-test-definition.md), SHA-256 `7f850b4c26e034a2472c19a9109e18df73b11398e09c99ec08d42fbcab266b02`, revision 4 preserves the same six-row review population. The operator's later audit authorization and acceptance decision are captured separately rather than retroactively changing those frozen bytes.
- Candidate-5 selection disposition SHA-256 `f05e802a1d0411af9984e73381ec946b720d92bc42c9abcc0585e3041cdd02e2` binds exactly 50 selected controls, blind-manifest SHA-256 `1a9a7ff9a2ffb2913970d0d883b9e1799979e1b778b8af6583f1328e04ec6cad` and custodian-answer-manifest SHA-256 `6404e38b1260d070ae67b7c8b93a08e3dccf69cf032fd7b2e17a78c7841a0993`.
- Evaluator-input schema SHA-256 `0e8f46d1cab95015241ef11d8ebcfa204d30ba5ca7cde833389ce3bba7140ece` defines the complete harness input. Evaluator-result-envelope schema SHA-256 `b5744b094b365d57189468a4c3890f9974b4fd96c2eee013647a168ac02eb31c` defines retained attempt results. Evaluator-configuration schema SHA-256 `bbdfb017f06116bc72c08ca49723bba4ca362bf2090ec432fc9833af1fe3d34a` defines the separately frozen judge configuration.
- Wire schema SHA-256 `a8ef80f63554827f80e2b602c7e2b6445af3405e6c28b900881fa2dbc4412371` and verification-contract schema SHA-256 `38229987ed55c98f2f7765d43b7b08f012bb313863d0b08740e9234afa521b97` close every external `Id`, `Digest`, `Artifact` and `VersionedArtifact` reference used by the evaluator schemas. Run-manifest-identity schema SHA-256 `161068b50a8093f53604204fbcdf3e1fcdc6f7e6bb06075a2d414c28231b4550` requires `{run_id, manifest_digest, manifest_artifact_sha256}`.
- The accepted local Docker trust-boundary direction is in `physical-runtime-binding.md`, SHA-256 `41b640517da9fd6879e610e72f7e270460152c424c5fb84df811260b6b266a06`. This construct uses only its non-root, least-mount evaluator boundary; it does not import the broader runtime design.
- [`C5-HOST-CLOSURE-AUDIT-1`](reviews/candidate-5-minimal-custody-host-closure-audit-1/audit-report.md) completed against the exact revision-4 source hash above. Its validated result closes the two retained supplemental findings at the design-text layer and explicitly makes no runtime, convergence, whole-design or acceptance claim.
- Historical Candidate-5 bytes remain unchanged. Derived request projections receive new identities and never overwrite source inputs.

### Out of scope

- Selecting or granting provider configuration, credentials, relay access, pricing, spend or calibration launch. Those remain separately owned gates; this construct only requires and verifies their exact identities before admission.
- Permanent final freeze, deletion, retention release, passphrase migration, claim retirement and generalized recovery. Reopen only under a separately accepted lifecycle design.
- Protection from a hostile host administrator, Docker/container escape, physical seizure of an unlocked host or operator disclosure of the passphrase.
- Media-failure independence. Primary and replica are verified encrypted copies at distinct paths on the current host; this design makes no separate-device or disaster-recovery claim. Reopen if loss of the host must be tolerated.
- Calibration semantics, rubric correctness, candidate selection or adoption. This mechanism preserves observations; it does not decide their meaning beyond the already-defined comparison.

## Decision C5C-project — Derive a judge-visible request pack

### Decision and rationale

Never mount the repository or the existing `candidate-5/blind/` tree into the evaluator. Each of the 50 current `frd/evaluator-input/v1` source files contains `hidden_ground_truth_artifact`; the harness needs that binding, but the judge does not. Preparation therefore creates a separate exact projection for each task and an allowlisted package containing only the projected requests and their transitively referenced judge-visible artifacts.

For each control in the exact manifest order, the implementation:

1. verifies both source manifests and every referenced source byte against its declared SHA-256;
2. loads the source evaluator input and removes exactly `hidden_ground_truth_artifact`;
3. changes only `schema_revision` to `frd/evaluator-request/v1` and validates the result against a new closed schema equal to evaluator-input v1 minus the hidden-ground-truth member;
4. copies only the candidate-output artifact, eligible rubric artifacts, output schema and allowed-evidence artifacts referenced by that projection;
5. records the source-input hash, projection hash and complete referenced-member inventory in `judge-request-manifest.json`; and
6. refuses any missing, extra, duplicate, traversing, symlinked, hash-mismatched or answer-namespace member.

The custodian package retains the exact source manifests, exact source evaluator inputs, all ground-truth/expected/truth-contract material and the selection disposition. The projected judge package contains exactly 50 projected request files and their allowlisted transitive members. The preparation gate scans every projected JSON key and every member path; `hidden_ground_truth_artifact`, expected classifications/payloads, custodian manifests, truth contracts and `judge-ground-truth/` members are forbidden.

### Amendments

| Path or artifact | Operation | Required result |
|---|---|---|
| `evaluation/calibration/candidate-5/custody-single-run/schemas/evaluator-request-v1.schema.json` | add | closed judge-visible projection schema |
| `evaluation/calibration/candidate-5/custody-single-run/schemas/judge-request-manifest-v1.schema.json` | add | closed 50-task source/projection/member inventory |
| `evaluation/calibration/candidate-5/custody-single-run/candidate_5_custody_run.py` | add | deterministic projection and all later single-run phases |
| existing Candidate-5 files | no-change | remain byte-identical historical and selected-population evidence |

### Correctness invariants

- **C5C-projection-complete:** all and only the 50 manifest-ordered tasks receive one projection.
- **C5C-no-answer-surface:** no answer-bearing member, answer namespace or hidden-ground-truth field exists in the judge image.
- **C5C-source-trace:** every projection and copied member resolves to one verified source identity.

### Risks and failure behavior

- A path reference may escape the intended source root → reject absolute paths, `..`, symlinks and non-regular files before reading.
- A harmless string may resemble a forbidden answer term → key and member-path checks are structural, not unrestricted text matching.
- Projection may accidentally remove more than the one harness-only field → byte-compare all remaining ordered fields and values to the source object.

## Decision C5C-plan — One plan, one passphrase, one approval

### Decision and rationale

The one mutating `run` command creates a single custody-supervisor process that remains alive from preparation through `50-retained.json`. It emits newline-terminated JCS `run-plan.json`. Its root is closed and contains: schema revision; UUIDv4 run ID `c5cal-<lowercase-uuid>`; the implementation-file SHA-256; all authority/source/schema hashes above; judge-request-manifest hash; evaluator image digest and exact command; working, primary and replica roots; four image names; exclusions exactly `provider authority is external`, `spend authority is external`, `calibration launch authority is external`, `permanent final freeze is excluded` and `evidence deletion is excluded`; and the complete prerequisite bindings below.

The prerequisite block is required, not optional. It binds:

1. the external HEB-154 run manifest by exact artifact path/SHA-256 plus the schema-required `{run_id, manifest_digest, manifest_artifact_sha256}` triple;
2. the evaluator configuration artifact path/SHA-256, configuration ID/revision, and its exact evaluator-configuration schema hash;
3. the provider profile and settings artifact identities plus the provider-relay contract artifact and the relay's owning schema/contract identity;
4. the immutable pricing artifact and owning schema/contract identity;
5. a separately issued spend-authorization artifact; and
6. a separately issued calibration-launch-authorization artifact.

The spend and launch authorizations must name this run ID, evaluator configuration, provider/profile, relay contract, pricing artifact, permitted cost ceiling, approving principal and unexpired authorization interval. The supervisor verifies every referenced byte, schema/contract identity, cross-field equality, authorization scope and current validity before it presents the plan. If an owning schema/contract is not frozen, or any prerequisite is missing, unknown, stale, mismatched or unapproved, `run-plan.json` is not admitted and no passphrase or custody approval is requested. The custody approval below confirms only the displayed custody plan; it neither creates nor substitutes for provider, pricing, spend or launch authority.

The primary root is `/Users/thaffey/Documents/Haffey Enterprises/Development Archives/HEB-154/candidate-5-calibration/<run-id>/primary/`. The replica root is the sibling `replica/`. The working root is `/Users/thaffey/Documents/Haffey Enterprises/Working/HEB-154-<Eastern-date>/candidate-5-custody/<run-id>/`; the date is derived at invocation with `TZ=America/New_York date +%Y-%m-%d`. Every run directory must be absent before preparation and is create-once.

The supervisor prints the complete human-readable plan plus its exact-file SHA-256, then requires an interactive TTY passphrase and exact input `APPROVE C5 CUSTODY <run-plan-file-sha256>`. Denial, EOF, non-TTY input or mismatch records no approval, discards the in-memory passphrase and performs no evaluator launch. The approval interaction has a declared maximum duration, and the plan is admissible only if the remaining spend- and launch-authorization interval covers that duration plus the declared launch-admission window.

After exact approval and immediately before durable run consumption, the supervisor opens with no-follow semantics, re-reads once and captures in memory every prerequisite artifact named by the closed block: the external run manifest, evaluator configuration, provider profile, provider settings, provider-relay contract, immutable pricing, spend authorization, calibration-launch authorization and every owning schema or contract. Every path must still resolve to the expected regular file. From those captured bytes—not from a later path read—the supervisor recomputes every file SHA-256; parses and validates every owning schema/contract; revalidates the run/configuration/provider/relay/pricing identities, cross-field equality, approving principal, cost ceiling and scope; and validates current time. The remaining spend- and launch-authorization interval must cover the complete declared launch-admission window.

The captured byte population is the complete launch-consumed prerequisite snapshot. The supervisor derives the effective evaluator command, configuration, relay binding and every other launch input exclusively from the parsed captured bytes and holds them in the same process through container creation. It never reopens a prerequisite path or substitutes a separately parsed object for launch. A domain-separated JCS inventory of ordered `{role, artifact_sha256}` tuples gives the snapshot digest recorded in the start marker; prerequisite content is not persisted into structural receipts. Any path re-read, missing or non-regular file, byte drift, identity/scope/time mismatch, expiry, insufficient remaining interval or inability to construct launch solely from the snapshot discards the in-memory passphrase, creates no `20-evaluator-started.json` marker or container and terminates nonzero. Mutation of a source path after capture cannot affect launch because launch consumes only the captured snapshot.

The passphrase is read once with a no-echo TTY prompt and held only in the supervisor's process memory. For each image create or attach, the supervisor invokes the exact `/usr/bin/hdiutil` binary with `-stdinpass`, opens one new dedicated standard-input pipe to that child, writes the passphrase and immediately closes the pipe's write end. It retains no reusable passphrase-bearing descriptor. The passphrase never appears in arguments, environment, files, receipts, logs or model input, and reaches no other child or inherited descriptor. No key file, broker or recovery key exists for the operator to manage.

After approval, the same supervisor creates and attaches encrypted images, launches and waits for the isolated evaluator, seals its result image, attaches the three read-only comparator inputs and writable comparison image, launches and waits for the isolated comparator, verifies both copies of all four image classes and emits `50-retained.json`. Evaluator and comparator receive mounted filesystems only; neither process receives the passphrase or an open passphrase-bearing pipe. The read-only `inspect` command reports structural receipt and ciphertext identities without attaching an image or requesting the passphrase. Any supervisor exit before a valid `50-retained.json` permanently fails the run identity.

### Amendments

| Path or artifact | Operation | Required result |
|---|---|---|
| `evaluation/calibration/candidate-5/custody-single-run/schemas/run-plan-v1.schema.json` | add | closed plan grammar, exact exclusions, closed prerequisite block and dual run-manifest identity |
| `evaluation/calibration/candidate-5/custody-single-run/schemas/phase-receipt-v1.schema.json` | add | create-once structural phase and failure receipts without secrets/content |

### Correctness invariants

- **C5C-plan-bound:** no launch input exists outside the exact plan.
- **C5C-prerequisite-authority:** custody approval grants no provider, pricing, spend or launch authority; every separately owned prerequisite is exact, valid and plan-bound before approval, recaptured and revalidated at the launch edge, and consumed for launch only from that one verified snapshot.
- **C5C-manifest-identity:** the plan binds both the external run manifest's semantic digest and its exact-file SHA-256 under the frozen run-manifest-identity schema.
- **C5C-one-secret:** the operator supplies only the passphrase; derived encryption material is never persisted.
- **C5C-one-supervisor:** one process owns every passphrase-bearing host operation; evaluator and comparator remain passphrase-free.
- **C5C-explicit-launch:** only the exact approval statement for the displayed plan hash crosses the launch gate.

### Risks and failure behavior

- Python cannot guarantee erasure of every in-memory passphrase copy → keep one process short-lived, prohibit persistence and child inheritance, and state the hostile-host exclusion honestly.
- The supervisor may fail after the operator's single prompt → fail the run permanently and require a new run ID and new prompt; never introduce a secret handoff or same-ID continuation path.
- Two archive directories on one device may be mistaken for disaster recovery → receipts state `same-host verified replica; no media independence claim`.

## Decision C5C-images — Four encrypted evidence images, two exact copies

### Decision and rationale

Use the native `/usr/bin/hdiutil` encrypted-image capability observed on the target Mac. Each class—`judge-inputs.dmg`, `custodian-answers.dmg`, `evaluator-results.dmg` and `comparison-results.dmg`—is an AES-256 encrypted, case-sensitive APFS disk image. The custody supervisor creates each encrypted writable image, attaches it only for its owning phase, writes the complete inventory plus `image-manifest.json`, detaches it, converts it to read-only UDRO, runs `hdiutil isencrypted` and `hdiutil verify`, and hashes the final bytes. A final image is copied byte-for-byte to primary and replica; both copies are read back and must match the same digest before the phase receipt exists.

`image-manifest.json` is newline-terminated JCS and binds image role, run ID, source identities, ordered member path/size/SHA-256 tuples and the manifest schema revision. It does not self-hash. No plaintext staging tree is created: source bytes are copied directly into an attached encrypted image, evaluator results are written directly into an attached encrypted result image, and comparison output is written directly into an attached encrypted comparison image.

Structural `run-plan.json`, approval and phase/failure receipts contain hashes, paths, tool identities and outcomes only. They are copied to both roots but need not be encrypted because they contain no payload, passphrase, provider credential, answer, evaluator result or comparison content.

### Amendments

| Path or artifact | Operation | Required result |
|---|---|---|
| `evaluation/calibration/candidate-5/custody-single-run/schemas/image-manifest-v1.schema.json` | add | closed role and complete ordered member inventory |
| primary/replica run roots | add at execution only | identical encrypted images and structural receipts; no pre-authored outcomes |

### Correctness invariants

- **C5C-encrypted-at-rest:** payload evidence exists durably only inside AES-256 encrypted images.
- **C5C-copy-identity:** primary and replica bytes match the same recorded SHA-256.
- **C5C-restore-equivalence:** either copy restores the complete manifest inventory with no missing, extra or changed member.

### Risks and failure behavior

- Interrupted conversion or copy may leave a partial image → publish through a new staging name and create the receipt only after readback; partial bytes remain identified as failed evidence.
- Encryption status may be assumed from a filename → require both `hdiutil isencrypted` and wrong-passphrase refusal.

## Decision C5C-isolate — Mount only the current phase

### Decision and rationale

The evaluator runs as non-root UID `21002` in the exact image digest bound by the run plan. Its root filesystem is read-only; all Linux capabilities are dropped; `no-new-privileges` is set; container IPC is disabled so `/dev/shm` is not mounted; and device and mqueue mounts are prohibited. No separate writable `/tmp` filesystem exists. It receives exactly two declared mounts: the attached judge-input image at `/run/in:ro` and the attached encrypted result image at `/run/out:rw`. Before launch, the supervisor creates `/run/out/tmp` with ownership restricted to UID `21002`; the evaluator environment sets `TMPDIR=/run/out/tmp`, and `/tmp` remains nonwritable in the read-only root. The evaluator receives no repository, custodian-answer image, primary/replica root, host home, Docker socket or host PID/IPC/device mount.

The container entrypoint is a frozen trusted preflight wrapper from the same image digest, not evaluator code. The container is created with Docker logging driver exactly `none` and no logging options. The supervisor creates it stopped, obtains the host-visible effective container configuration, and refuses unless `HostConfig.LogConfig.Type` is exactly `none` and its option map is empty. It also refuses any undeclared mount or tmpfs, writable `/run/in`, `TMPDIR` other than `/run/out/tmp`, UID other than `21002`, privileged mode, retained capability, Docker socket, host PID/IPC namespace, device or mqueue mount. It records the complete effective mount, descriptor/logging and security configuration rather than treating declared launch text as the effective boundary.

The supervisor then starts the container at the preflight wrapper. The wrapper must emit no byte to its inherited standard output or standard error. Its first operation opens `/run/out/evaluator.stdout` and `/run/out/evaluator.stderr` with no-follow, write-only, create-once semantics and mode `0600`, verifies both descriptors name regular files on the `/run/out` mount, atomically replaces file descriptors 1 and 2 with them and closes the original descriptors. It then resolves `/proc/self/fd/1` and `/proc/self/fd/2`, requires both canonical targets to remain inside `/run/out` and refuses silently with a nonzero exit if any open, type, mount, replacement or resolution check fails. The supervisor treats that exit as a post-marker failure. No wrapper or evaluator output can reach Docker's inherited logging descriptors, and any later standard output or error becomes encrypted result-volume content.

Only after descriptor binding succeeds, and still before the wrapper imports, invokes or executes any evaluator module or makes any provider request, it parses `/proc/self/mountinfo`, inventories every effective mount, classifies each regular-filesystem and Docker runtime surface, and attempts a reversible create/write/remove probe at every candidate surface outside `/run/out`. `/run/in` must prove readable and nonwritable; `/run/out` must prove readable and writable; every other regular-file surface must refuse a regular-file create/write. The wrapper separately reports device-node semantics without treating them as retained file storage. Any unclassified surface, writable regular-file result outside `/run/out`, missing denial or receipt-write failure terminates the wrapper without evaluator execution. A successful wrapper writes `21-evaluator-boundary-proved.json` directly under `/run/out`, including the host-verified logging configuration and canonical file-descriptor targets, flushes it, and only then `exec`s the evaluator without changing descriptors 1 or 2. Thus container start is not evaluator launch; evaluator launch is the wrapper-to-evaluator `exec` after the proof succeeds.

Network is `none` unless the separately authorized provider-relay identity and launch authorization are both valid in the run plan; in that case the only network attachment and destination is that relay. The preflight wrapper performs no provider call. Provider authorization remains outside this construct.

The evaluator processes all 50 request-manifest entries in order and writes exactly one terminal `frd/evaluator-result-envelope/v1` record per entry. Missing, duplicate, malformed or nonterminal results fail the run; they are not filled, retried or repaired.

### Correctness invariants

- **C5C-effective-denial:** host inspection and in-container proof cover the complete effective runtime surface, Docker logging and output descriptors before evaluator code executes; evaluator reachability is the exact two-mount allowlist plus, only when separately authorized, the one bound relay.
- **C5C-one-write-surface:** every evaluator write, including temporary output, is under `/run/out` inside the encrypted result image.
- **C5C-first-result:** each task has exactly one retained terminal envelope from the first attempt.

### Risks and failure behavior

- Declared launch text may differ from effective runtime → inspect the stopped container, require effective logging driver `none`, then make the frozen preflight wrapper prove its output descriptors and every effective runtime surface before it executes evaluator code.
- A provider transport failure may tempt a retry → retain the unavailable envelope and stop; retry policy is outside this construct.

## Decision C5C-seal-compare — Seal results before answer access

### Decision and rationale

After evaluator termination, the custody process prevents restart, detaches the result image, converts/verifies/hashes it, publishes and readback-verifies both copies, then creates `30-results-sealed.json`. Comparison refuses unless that receipt, both exact result copies and proof that the evaluator container no longer exists all pass.

Only then does the custody supervisor attach the primary judge, custodian and result images read-only and a new encrypted comparison image read-write, then launch the offline non-root comparator against those mounts. The comparator has no network, Docker socket, host home, archive-root or passphrase access. It requires exactly 50 source tasks and exactly 50 terminal result envelopes in manifest order, compares observed classifications/reasons to custodian expectations under the ratified v2 contract, and writes the existing comparison result plus a complete comparison inventory. It makes no provider, adoption or graduation recommendation.

The comparison image is then detached, verified, hashed and copied/readback-verified to both roots. `50-retained.json` exists only after all four image classes have two verified copies and both copies of each can be attached read-only and reproduce the same complete inventory.

### Correctness invariants

- **C5C-seal-before-answer:** no comparison process or answer-image attachment occurs before `30-results-sealed.json` is valid.
- **C5C-complete-result:** all 50 first-result envelopes and the complete comparison are retained; absence is evidence, never an inferred failure record.

### Risks and failure behavior

- A result seal might be asserted from a hash alone → require evaluator absence, image detach, image verification, dual-copy readback and manifest restore before the receipt.
- Comparator access may leak answers back into evaluator state → evaluator container destruction precedes answer attachment and no shared writable mount exists.

## Decision C5C-stop — Abort once; restart only with a new identity

### Decision and rationale

The command surface is exactly one mutating `run` command plus one read-only `inspect` command. `run` refuses if the working, primary or replica run root already exists or if any marker, receipt, image, temporary publication name or other artifact already names the requested run ID. `inspect` may read structural receipts and ciphertext identities but cannot create a directory, attach an image, launch a process or mutate evidence. There is no `prepare`, phase-resume, `compare`, `verify-retention`, `recover`, `repair`, `overwrite`, `delete`, `unseal`, `migrate` or same-ID retry operation exposed separately.

The evaluator phase order is exact:

1. validate the run plan, all initial prerequisite authority and the static launch configuration;
2. obtain the one passphrase and exact approval;
3. capture, revalidate and bind the complete launch-consumed prerequisite snapshot defined by SD-1;
4. atomically create `20-evaluator-started.json` in the working run root with exclusive create semantics;
5. create the evaluator container in a stopped state and inspect its host-visible effective configuration;
6. start only the frozen trusted preflight wrapper, which proves the in-container effective runtime boundary and writes `21-evaluator-boundary-proved.json`; and
7. permit the wrapper to `exec` the evaluator only after that receipt is durable in `/run/out`.

The start marker binds the run-plan file SHA-256, run-manifest identity triple, complete prerequisite-snapshot digest, evaluator image digest, static launch-configuration hash, effective logging requirement and intended container identity. It writes newline-terminated JCS, flushes the file, atomically publishes it, flushes the parent directory and verifies the bytes. Container creation is forbidden unless that durability sequence succeeds. The marker is later copied as structural evidence to primary and replica, but its create-once working-root identity is the run-consumption boundary. Any failure after marker creation destroys the container when possible, preserves all available evidence, writes `failed.json` when possible and permanently fails the run identity; evaluator code is not run after a descriptor or preflight failure.

Any access violation, prerequisite-authority or identity mismatch, projection/capture failure, image/encryption failure, copy/readback mismatch, pre-seal crash, invalid result, premature comparison or supervisor exit before `50-retained.json` writes `failed.json` when possible, leaves all available images and receipts in place and terminates nonzero. If a process crash prevents the receipt, the create-once marker, absent next receipt or any existing partial artifact is itself an incomplete failed attempt. Any existing marker, terminal receipt, failure receipt or unexplained artifact permanently blocks same-ID `run` entry. Any further attempt requires a fresh UUID, fresh prerequisite bindings, fresh passphrase prompt and fresh operator approval.

### Correctness invariants

- **C5C-no-reentry:** a failed or structurally incomplete run ID can only be inspected read-only.
- **C5C-consumed-before-container:** the durable create-once evaluator-start marker consumes the run identity before container creation.
- **C5C-partial-truth:** available partial bytes and their uncertainty remain; the mechanism never manufactures a complete result.

### Risks and failure behavior

- Failure receipt creation can itself fail → receipts are not used to erase or reinterpret already-present partial bytes.
- Lost or exposed passphrase can make retained images unavailable or suspect → preserve ciphertext, stop, and return for a future separately accepted disposition; no migration exists here.

## Obligations

| ID | Obligation | Instrument | Gates landing | Evidence |
|---|---|---|---|---|
| `C5M-1` | complete answer-free 50-task projection | clean projection test plus answer-member and hidden-field dirty tests | yes | retained test output and projected-root digest |
| `C5M-2` | effective evaluator allowlist and denials | stopped-container inspection of logging `none`; create-once `/run/out` stdout/stderr binding; descriptor resolution; complete mount inventory, regular-filesystem/Docker-surface probes and evaluator-before-proof refusal | yes | effective config, descriptor targets, `21-evaluator-boundary-proved.json` and complete probe receipts |
| `C5M-3` | exact prerequisite-bound plan, launch-consumed snapshot, one supervisor/passphrase channel and explicit approval | complete post-approval byte recapture/hash/schema/identity/time tests, source-path drift and reopen controls, snapshot-to-launch binding, dedicated-pipe inspection, process-boundary secret scan and wrong-input/non-TTY tests | yes | plan, snapshot digest and identities, structural transcript, descriptor evidence and refusal receipts |
| `C5M-4` | complete result seal precedes answer access | 50-envelope check, ordered receipts and premature-comparison probes | yes | result-image identity and seal receipt |
| `C5M-5` | encrypted primary/replica and restore equivalence | encryption/verify/copy/restore tests plus wrong-passphrase/drift/missing-member controls | yes | eight copy identities and restore inventories |
| `C5M-6` | fail-stop with durable pre-container identity consumption and new-ID-only continuation | marker durability/crash tests, descriptor-binding and post-marker preflight failures, one injected failure per named family and same-ID re-entry tests | yes | start marker, boundary-proof or failure receipts, retained partial identities and refusal results |

## Evidence handling

The current Candidate-5 repository bytes remain the source evidence and are neither moved nor deleted. The later implementation creates derived judge projections with explicit source hashes. Runtime encrypted images and structural receipts are new evidence under the exact run roots; copying to the replica is non-destructive and verified before either copy is relied upon. No duplicate-retirement step exists in this phase.

Design-review artifacts remain repository-local under `reviews/candidate-5-minimal-custody-review-1/`, the targeted closure-review directory, the separately authorized supplemental direct-check directory and `reviews/candidate-5-minimal-custody-host-closure-audit-1/`. They bind exact design bytes but never enter a runtime image or become a launch precondition. The revision-4 reviewed source remains at its original path and in Git commit `d94641b5186359560715955a978046cf0bce18fd`; this accepted revision is a non-destructive lifecycle promotion with unchanged operative design clauses.

## Lifecycle gate

| Transition | Required evidence | Result |
|---|---|---|
| design acceptance | separately authorized closure verification of both supplemental findings plus explicit operator decision on exact revision-4 construct hash | passed 2026-09-17 America/New_York; closure audit passed and Tad Haffey ratified the design |
| implementation | exact implementation, schema, image and dependency identities | pending |
| verification | all six obligations pass against that implementation, including dirty controls | pending |
| calibration launch | separately frozen provider/configuration, pricing, spend and launch authorization | outside this design; pending elsewhere |
| graduation | post-run review and operator decision | not-applicable to this single-run mechanism |

## Change log

| Revision | Date | Change |
|---|---|---|
| 1 | 2026-09-17 | Proposed blank-graph replacement implementing ratified MB-1 through MB-5 and only the six frozen demands. |
| 2 | 2026-09-17 | Applied ratified C5-R1 and AC-1 through AC-4: one custody supervisor, exact prerequisite/schema bindings, dual run-manifest identity, durable pre-container run consumption and one encrypted writable evaluator surface. |
| 3 | 2026-09-17 | Applied RC-1 through RC-4: launch-edge authority revalidation, one-use passphrase pipes, complete effective writable-surface proof and executable marker/container/preflight/evaluator ordering. |
| 4 | 2026-09-17 | Applied SD-1 and SD-2: one complete launch-consumed prerequisite snapshot plus logging-disabled, result-volume-bound stdout/stderr proof before evaluator execution. |
| 5 | 2026-09-17 | Promoted the exact audited revision-4 design to `ACCEPTED-DESIGN` after explicit operator ratification; changed lifecycle, provenance and acceptance metadata only, with no operative design-clause or obligation change. |

<!-- STANDING: prior published rows remain frozen; amend the unpublished current row in place. -->
