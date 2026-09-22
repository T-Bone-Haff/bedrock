# Candidate-5 native actor identity and host readback amendment

| Field | Value |
|---|---|
| Document ID | C5-READBACK-IDENTITY-1 |
| Revision | 1 |
| Status | ACCEPTED-DESIGN; implementation and runtime verification pending |
| Owner | Tad Haffey |
| Decision date | 2026-09-19, America/New_York, native Mac clock |
| Review trigger | identity, host/runtime mapping, affected design clause or contrary observation changes |
| Doctype ruling | scoped amendment to one internal custody construct |
| Supersedes | only the actor numeric identity and output provisioning/finalization clauses identified below |

## Authority, ratification and scope

Tad stated “ratified” in response to the recommendation to bind this native profile's evaluator and comparator to the supervisor's non-root UID/GID 501:20, retain private modes, codify the amendment and prepare a bounded diagnostic. The ratified proposal has raw SHA-256 `69cfa1dfcb5a13b1c0a930ffa744e0936e31444b54de4d10e70150b10eef0609`. Its original PROPOSED wording remains immutable deliberation evidence; this amendment records the subsequent decision.

Read with [accepted construct revision 5](candidate-5-single-run-custody-construct-spec.md), SHA-256 `e4e5a6266c63e0077c19df357fed2ce4d96aa2b008e38c5a618ae610d614d829`, and [payload-boundary amendment revision 2](candidate-5-payload-boundary-amendment.md), SHA-256 `0ea66e4c862d298c700e0bc666b215e537279552ff491d8cffda9753741f0f14`. This amendment takes precedence only for the explicit replacements below. The six C5M demand identities remain; their next test-definition revision and focused review are pending.

The current native profile is macOS 26.6.2/25G83, pinned hdiutil, Docker desktop-linux 29.7.2 Linux/arm64 and non-root host supervisor 501:20. Numeric equality across the Docker Desktop filesystem boundary is a design requirement to test, not a claimed mapping observation. A different identity or platform profile needs a new disposition. No additional runtime execution, helper privilege, commit, review invocation or calibration launch is granted here.

## Decision C5C-readback-identity — One explicit non-root ownership identity

Bind the host supervisor and both container actor roles to UID 501/GID 20 for this profile. Verify supervisor real/effective UID and GID before preparation and before host finalization/readback. Reject root, identity drift or unavailable measurements. Record host supplementary groups for evidence but do not copy them into either actor. The actor's effective primary GID is 20 and its complete group set may contain only 20. Inspect stopped-container configuration and verify actual runtime real/effective UID/GID and group set; configuration text is not the runtime oracle.

The prospective closed run plan binds this exact host/actor identity and group rule along with existing image/command/source identities. Launch and every subsequent role consume that binding. Do not silently derive a new UID from the current login or retain a fallback to 21002. The eventual schema and implementation must carry this meaning without relaxing the existing closed prerequisite snapshot or approval rules.

Create each new writable output's payload directory as 501:20 mode 0755 and payload/tmp as 501:20 mode 0700. Preserve stdout/stderr mode 0600 and the applicable exact output ownership/mode contract. The supervisor already owns newly created paths; no operator sudo/chown step is needed in this profile. Actual native ownership, container-visible ownership and file readability must each be measured. Attachments remain ownership-enabled. A wrong owner or inaccessible member stops; there is no chmod/chown/ACL repair, owners-off inspection or omitted-member fallback.

### Isolation and trade-off

The evaluator and comparator remain container processes with exact phase-specific payload-only binds. Readonly root, dropped capabilities, no-new-privileges, restricted network/IPC, logging none, no devices/mqueue as required by the construct, no host PID namespace or engine control, descriptor binding, complete effective mount inspection and write-denial controls remain mandatory. Native actor execution is not admitted. Extra mounts are rejected regardless of whether a test file happens to be readable. Matching numeric ownership grants no permission to mount home, repository, archive roots or answers early.

The accepted threat model trusts the host supervisor, OS and engine and excludes hostile host administration and container escape. Shared numeric ownership removes a secondary permission barrier if an unintended host path becomes exposed. The design therefore relies on the verified container/path boundary; it makes no separate-UID isolation claim. This trade-off was presented with the ratified recommendation. The governing need is independent exact custody of first results, not protection of those results from their trusted custodian.

## Decision C5C-host-finalization — Independent inventory and create-once manifest

After each actor terminates, inspect and remove its exact container and prove it no longer exists before host finalization. Use no-follow traversal and descriptor identity checks to read all payload members, including dotfiles and tmp. Record paths, types, required ownership/modes and file bytes/size/hash. Reject symlinks, special files, unreadable members and missing/extra/changed members against the applicable contract. An actor-provided inventory is not the supervisor's oracle.

Reserve payload/image-manifest.json for host publication. It must be absent before launch and after actor removal. Any preexisting object, including a dangling symlink, refuses publication and fails the run. The supervisor independently derives the manifest, creates it exclusively without following symlinks, flushes and reads it back, and binds its exact identity externally. Preserve the existing newline-terminated JCS grammar, role/run/source binding and self-hash-free semantics. The complete restoration oracle includes the manifest's externally bound bytes and metadata; the manifest does not include its own hash in its member inventory. Do not rewrite actor results to obtain conformance.

The host finalization stage precedes detach/conversion and copy publication. Evaluator removal, finalization, sealing and both-copy verification precede result-seal receipt and any answer attachment/comparator launch. Apply the analogous host finalization to comparator output. Restore both copies with ownership enabled and verify exact payload bytes, modes and required UID/GID; keep whole ciphertext identity and root-metadata claims separate.

### Evidence and rationale

Attempt `5cdad606-f000-4a1e-a74b-e169e49ee9cb` demonstrated that the prior identity split prevented the required host readback. On the mounted encrypted APFS subject, chown changed both directories to 21002:21002 while preserving device/inode identity and modes. UID 501 could enumerate tmp before chown and its parent afterward; a new no-follow open of tmp then failed with errno 13. The probe stopped before actor execution or sealing and detached successfully. Its archive inventory SHA-256 is `9dabad9d7fbe6b1efb6ad1aba4edabcc17a8664aafe9bc8a20dcea69e4d14e53`.

One controlled directory-access failure is the empirical floor. Private-file failure and host manifest-write denial were not run; the latter is a design implication of the old 0755 directory ownership. The new identity has not been proved through Docker, private-file creation or output sealing. Using it keeps readback and manifest publication in the existing trusted supervisor rather than adding a new privileged helper/collector boundary. A filesystem permission failure still fails the attempt; ownership equality is not evidence that every possible output remains readable.

## Amendment and obligation reconciliation

| Existing locus | Explicit change or preserved rule |
|---|---|
| C5C-isolate and payload amendment's retained UID 21002 | Replace with the exact 501:20 profile and actor group rule above; preserve every other isolation requirement |
| C5C-plan and prospective run-plan schema | Bind host/actor identity and consume it consistently; preserve one supervisor, one secret and separate launch authority |
| C5C-images / C5C-seal-compare | Explicit post-removal host inventory, reserved manifest publication and exact owner/mode restoration |
| Prior probe output provisioning | New profile creates supervisor-owned output; older chown plans and observations remain historical |
| C5M-1 | Projection and answer exclusion unchanged |
| C5M-2 | Verify revised identity, full groups and the complete retained runtime boundary |
| C5M-3 | Bind identity in exact plan; preserve secret/approval/snapshot obligations |
| C5M-4 | Verify removal and host finalization before seal and answer access |
| C5M-5 | Verify 0600 files, nested 0700 directories, manifest publication and exact restored ownership from both copies |
| C5M-6 | Preserve failure evidence and new-ID-only continuation; include unreadability/publication refusal |

Required proof covers actor-created private files, both log streams, a dotfile and nested private directories; known-byte independent host reads; missing/extra/changed member, owner/mode, unreadability, symlink and manifest-collision controls; full mount/configuration refusals; and evaluator-like and comparator-like output lifecycles. Every required falsified or unavailable measurement stops. A passing synthetic file-access test does not prove the native bootstrap's first-action property or the complete Candidate-5 demands.

## Preservation and lifecycle

The accepted construct, payload amendment revision 2, test definition revision 4, original acceptance and all historical attempts remain unchanged. Failed attempt ciphertext and diagnostics remain under Development Archives/HEB-154/output-observations/<attempt-id>/; no image is reopened or secret recovered. This amendment states the operative decision so its meaning does not depend on tracker or conversation access. Evidence identities are provenance, not runtime inputs.

| Transition | State |
|---|---|
| Identity/finalization design direction | ratified by Tad; recorded here |
| Bounded diagnostic plan | prepared separately; execution approval pending |
| Implementation and runtime verification | pending; no success inferred |
| Output metadata policy | pending separate observations and disposition |
| Next test-definition revision and focused review | pending; old reviewed bytes preserved |
| Calibration, release or graduation | not authorized by this amendment |

Revision 1, 2026-09-19: codified the ratified native identity/readback disposition and preserved its empirical and lifecycle limits.
