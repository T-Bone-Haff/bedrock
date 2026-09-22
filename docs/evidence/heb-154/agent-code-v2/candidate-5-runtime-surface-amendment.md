# Candidate-5 runtime surface boundary amendment

| Field | Value |
|---|---|
| Document ID | C5-RUNTIME-SURFACE-1 |
| Revision | 1 |
| Status | ACCEPTED-DESIGN directions; exact runtime profile, enforcement and verification incomplete |
| Owner | Tad Haffey |
| Decision recorded | 2026-09-21, America/New_York, native Mac clock |
| Review trigger | exact profile proposal, runtime/tool/image change, affected clause change or contrary observation |
| Doctype ruling | scoped amendment to one internal Candidate-5 custody construct |
| Supersedes | only the read/write scope and blanket device/mqueue-mount prohibitions identified below |

## Ratification, authority and limits

Following an explicit distinction between design approval and information gathering, Tad stated: “ratify those 3 (now that I am back to the Agent Code skill mindset...)”. This accepts the three directions below. It does not select an exact device inventory, queue-denial mechanism or executable diagnostic. It creates no implementation, live-run, provider, calibration, commit, review-invocation or release authorization.

Read with [accepted construct revision 5](candidate-5-single-run-custody-construct-spec.md), [payload amendment revision 2](candidate-5-payload-boundary-amendment.md), [identity amendment revision 1](candidate-5-readback-identity-amendment.md), the [boundary-reset decision](DDR-HEB-154-001-candidate-5-custody-boundary-reset.md) and the [frozen test definition revision 4](candidate-5-minimal-custody-test-definition.md). Exact source identities are listed below. This amendment takes precedence only for its explicit replacements. All other obligations remain operative.

This is a semantic change to the literal C5M-2 demand, not a claim that the previous design or failed diagnostic already satisfied the revised meaning. Preserve the frozen test and review bytes. The next test-definition revision must express the accepted scope and its exact proof requirements before claiming conformance under it.

## Decision C5R-protected-boundary — Application data and runtime facilities

Permit reads of the frozen runtime's executable/dependency files and individually specified operating-system interfaces, in addition to the judge-visible payload. Bind those runtime resources to the exact image and reviewed runtime profile; this is not permission for arbitrary additional host or data mounts.

Keep judge input read-only. Every writable regular-file tree, including temporary-file storage and memory-backed file trees, must remain inside the encrypted result payload mounted at /run/out. Temporary files remain under /run/out/tmp. Keep stdout/stderr binding, logging none, host finalization, sealing before answer access and complete result retention. No answer material, repository, host home, archive roots or Docker control becomes accessible through this change.

Kernel interfaces require their own classified rules; neither a filesystem's name nor a mount's presence proves harmlessness. Permitting a declared virtual interface is not a claim that every kernel operation is a regular-file write or that every process-memory change is retained evidence. Unknown interfaces, alternate storage paths and missing required measurements remain blockers.

### Proof requirements

The final profile must define the permitted image/runtime reads, phase-specific payload binds and prohibited reachability. Reconcile host configuration with complete in-container mount, descriptor and interface observations. Retain the positive input-read/output-write controls and negative forbidden-answer, extra-mount, writable-input and outside-output storage controls. Apply the corresponding rules to the comparator's three read-only inputs and sole writable output.

## Decision C5R-virtual-devices — Exact restricted virtual-device profile

Replace the absolute /dev and /dev/pts mount prohibition with conditional permission for an exact, specified virtual-device profile. Before admission, freeze the permitted device identities and types, permissions/ownership, symlink targets, mount properties and terminal configuration. Verify actual identities rather than accepting names alone. Extra devices, host-device access and writable regular-file storage outside /run/out remain prohibited.

The current evidence does not establish a complete device-node inventory or prove the final access policy. No default device list is adopted merely because Docker or OCI commonly supplies it. Runtime-image, namespace, capability, UID/GID/group, no-new-privileges, network, logging, descriptor and payload-only bind restrictions continue to apply. No privilege, remount helper or host-device pass-through is granted here.

### Proof requirements

Measure the complete relevant node/link population and its effective mount context against the independently specified profile. Use controls that detect an extra device, wrong type/identity, changed link, changed permissions and unintended writable storage. An inaccessible required attribute or unclassified surface fails admission. Device and pseudo-terminal behavior must be assessed by the interface's semantics, not by an ordinary directory-create probe alone.

## Decision C5R-message-queues — Deny queue creation and use

POSIX message-queue creation and use remain prohibited. The /dev/mqueue mount may exist only if that functional prohibition is explicitly enforced and verified for the actual actor identity. The retained ordinary-file EINVAL result is not a queue-denial measurement. A declared IPC flag is also not a substitute for effective proof.

The exact enforcement mechanism, architecture-specific API/system-call coverage, descriptor handling and discrimination controls remain unresolved. Do not select a custom security profile, silently inherit a default, or weaken the denial to obtain a pass. The later proposal must state how actor queue creation/use is prevented, how inherited access is excluded and how actual denial is distinguished from an unsupported or malformed probe. If this cannot be established under the permitted runtime, return for a runtime/boundary decision instead of continuing.

### Proof requirements

Use valid queue-interface operations with an independent positive control demonstrating that the instrument can exercise the intended operation. Bind both the enforcement configuration and its observed effect to the actor/profile identity. A positive-control setup, native helper or new container requires inclusion in the separately approved diagnostic scope. Unknown coverage or unavailable control blocks admission; this amendment authorizes no such experiment by itself.

## Measurement corrections and required bindings

The prior /proc observations include ENOENT and deliberately unperformed kernel-control writes. They do not establish complete denial. Do not relabel them as successes. Specify a safe, interface-appropriate oracle for each required property; do not write kernel controls merely to imitate a regular-file test.

A probe at a mount root does not prove all descendants nonwritable. The profile and instrument must account for nested writable directories, existing writable regular files, nested mounts, links and descriptor-mediated access. Combine effective enforcement with probes and contrary controls; a handful of failed creates is not complete confinement proof. Do not recursively traverse dynamic kernel interfaces without a bounded, meaningful measurement contract.

Before a live diagnostic, the proposal must close: exact virtual-node/mount/terminal profile; complete surface classification and scoped /proc or masked-node oracles; queue-denial mechanism and coverage; frozen instrument/fixture identities and controls; exact mutation/resource/cleanup bounds. The existing native first-action descriptor guarantee remains a separate requirement and cannot be established by a Python bootstrap test alone.

## Evidence and empirical floor

Consumed synthetic attempt 9f542893-1de4-449d-8587-81ce9ea74a69 observed actor UID/GID 501:20, group set [20], output-bound descriptors and a successful /run/out/tmp write control. It observed /dev as tmpfs, /dev/pts as devpts and /dev/mqueue as mqueue; the accepted prohibition correctly yielded falsified. Several /proc and queue measurements remained unavailable. Its complete diagnostic SHA-256 is 4e725aa6f389ca4694e1259444aae6b25c5ecf33c89364e55d8ffec8caae2706, verified against its original archive inventory.

The diagnostic remains failed. Later host reads of its existing private files and eventual ordinary image detachment do not complete nested-file, output-sealing, comparator or acceptance proof. Original evidence remains under Development Archives/HEB-154/private-readback/ followed by the attempt ID; cleanup and final detached copies are separately retained under the corresponding closeout, docker-restart-cleanup and final-detach archives. No secret recovery, same-ID continuation, evidence deletion or retrospective verdict change is permitted.

The empirical floor is one runtime attempt for this surface mismatch. External references explain interface distinctions; they are not proof of the installed runtime: [OCI Linux defaults and devices](https://github.com/opencontainers/runtime-spec/blob/main/config-linux.md), [Linux POSIX message queues](https://man7.org/linux/man-pages/man7/mq_overview.7.html). Queue-interface and persistence passages and OCI default-filesystem/device passages were read as scoped references; moving upstream documents are not frozen runtime dependencies.

## Reconciliation and lifecycle

| Existing locus | Effect |
|---|---|
| C5M-2 and C5C-effective-denial | Explicit runtime reads/interfaces plus the preserved data-access boundary; semantic reconciliation required in the next test revision |
| C5C-one-write-surface and DDR RC-3 | Writable regular-file trees remain confined to /run/out; replace blanket virtual-device/mqueue mount bans only under the conditional rules above |
| C5C-isolate and both prior amendments' retained mount bans | C5R-virtual-devices and C5R-message-queues govern their explicit replacements; no other isolation relaxation |
| C5M-3 | Bind final profile, enforcement and instrument identities to the exact plan; preserve prerequisite snapshot and separate authority |
| C5M-1, C5M-4, C5M-5, C5M-6 | Preserve projection, sealing/order, encrypted copies/restoration and fail-stop/new-ID behavior |
| Frozen test, historical decisions/reviews and failed attempts | Preserve original bytes and historical verdicts; do not claim prior review covers this change |

The three design directions are ratified. Exact profile/mechanism design, instrument preparation, separately authorized diagnostic, output-metadata completion, revised test definition and focused review remain pending. No conformance or implementation-readiness claim follows from this document. Next proceed with read-only evidence/documentation analysis to produce the missing concrete bindings, then present substantive choices and the bounded diagnostic before execution.

### Source identities

- `candidate-5-single-run-custody-construct-spec.md`: `e4e5a6266c63e0077c19df357fed2ce4d96aa2b008e38c5a618ae610d614d829`
- `candidate-5-payload-boundary-amendment.md`: `0ea66e4c862d298c700e0bc666b215e537279552ff491d8cffda9753741f0f14`
- `candidate-5-readback-identity-amendment.md`: `97ec88cf7b38a82a79a00f4ff6a5cba53b3dcd1021643248936ea95773f12104`
- `candidate-5-minimal-custody-test-definition.md`: `7f850b4c26e034a2472c19a9109e18df73b11398e09c99ec08d42fbcab266b02`
- `DDR-HEB-154-001-candidate-5-custody-boundary-reset.md`: `4d5b9557b43ec6433e477d50dd89ff357deb201cea196746a6f2251f7ffd16d1`
- `physical-runtime-binding.md`: `41b640517da9fd6879e610e72f7e270460152c424c5fb84df811260b6b266a06`

Revision 1, 2026-09-21: recorded the three ratified runtime-boundary directions and their unresolved proof bindings; preserved historical bytes and separate execution gates.
