# Candidate-5 payload and volume-metadata boundary amendment

| Field | Value |
|---|---|
| Document ID | `C5-PAYLOAD-BOUNDARY-1` |
| Status | ACCEPTED-DESIGN for the payload boundary, tested native input sealing procedure and narrow input metadata rule; output policy and implementation admission remain pending |
| Revision | 2 |
| Owner | Tad Haffey |
| Decision recorded | 2026-09-19 America/New_York, native Mac clock |
| Review trigger | output-policy completion, host/tool/profile change, any affected clause change, or contradictory platform observation |
| Doctype ruling | scoped amendment to one internal custody construct |
| Deliberation substrate | localized APFS failure, source-unlock diagnosis, verified synthetic correction, and Tad's explicit approval of the boundary and input dispositions |
| Supersedes | inventory-domain, mount-source and native input-sealing clauses identified below; no historical artifact is overwritten |

## Purpose, authority and lifecycle limit

Read this amendment together with [`candidate-5-single-run-custody-construct-spec.md`](candidate-5-single-run-custody-construct-spec.md), revision 5, SHA-256 `e4e5a6266c63e0077c19df357fed2ce4d96aa2b008e38c5a618ae610d614d829`. The original acceptance record, reviewed sources, audit evidence and prerequisite files remain unchanged. This amendment governs only the explicit replacements below; all other requirements remain in force.

Tad ratified the proposed boundary after a disposable probe could write synthetic payload but could not enumerate `.fseventsd` at the mounted volume root. The accepted direction is: exact application-payload inventory; separately classified OS volume metadata; whole-image ciphertext identity; and payload-only container binds.

Revision 2 additionally records Tad's instruction, “Go for retro. Then proceed with test sealing procedure and input-metadata rule.” This adopts the two concrete dispositions in the retained successful-correction report: the tested source-unlock/output-encryption sequence and the narrow native input root policy. It supersedes revision 1's pending status for those input decisions only. Historical reports retain their original proposed status as records of what was known and authorized then.

**The writable evaluator/comparison-output metadata policy remains incomplete.** This amendment grants no additional privilege and makes no cross-host or output-image compatibility claim. No previous design-review or runtime verdict is extended to these changes. The existing separate implementation, proving and release gates remain in force.

## Original boundary observation and read limits

The localized attempt `7bf58b27-f527-47fe-9422-5d4887450710` used macOS 26.6.2 build 25G83 and native `hdiutil`. It created a 256 MiB image, independently observed encrypted/AES-256 UDRW metadata, attached case-sensitive APFS, and wrote two differently cased files with distinct inodes and expected bytes. The image root was UID 501/GID 20, mode 0755. Inventory then raised `PermissionError`, errno 13, from `os.scandir` on the root's `.fseventsd` directory. The attempt stopped and detached; its before/after attached-image/device populations matched. Docker, ownership changes, conversion and restoration were not reached.

The root population was not retained completely. `.fseventsd` is a positively observed entry, not a complete metadata allowlist. Its content, ownership and permission bits were not established by this record. The empirical floor is one localized attempt. A preceding PermissionError lacked a retained failing path and does not establish a second localized case.

Retained evidence identities:

| Artifact from the localized attempt | Raw SHA-256 |
|---|---|
| `exception.json` | `e7c1a206e34eac13ac6469830e05f6898b0120df443f497d8d9bc8a5aafbb29f` |
| `input-root-stat.json` | `6b76a2a2cab28b66ec70e441c10ef3165fde2aa6c7978f9abe8814579a778c69` |
| `input-payload-created.json` | `91d31af5b2ec0fba0b7f8d59db2834b911dd52fe80dd19a5d61c66b2201fe8c9` |
| `result.json` | `7e84aca80148ff8b1af3291df8866ef4481d1dc282cfdb2b3fd4f32577d47c06` |
| `finding-and-proposed-disposition.md` | `a5f7574770f3771551789796e3df20e264f1fe1bf9af7ffce4ec115f2218d2f8` |
| Failed ciphertext | `beff8153ad19b1ed3baa027270c472acf228b97ffeecc3da750f74dd492da91e` |

These are archival evidence references, not runtime inputs. The observed failure and operative rules are stated here so a cold reader does not need the original conversation or private tracker. The [Apple filesystem-event security reference](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/FSEvents_ProgGuide/FileSystemEventSecurity/FileSystemEventSecurity.html) explains the system directory's restricted nature; it does not define this construct's allowlist. No metadata suppression mechanism was exercised or accepted.

## Decision C5C-images — Separate payload fidelity from whole-image identity

Each of the four evidence images contains one explicitly named `/payload` directory. All application payload, derived artifacts, output logs and `image-manifest.json` live under that directory. Exact member-path, type, mode, size and raw-byte identity checks cover the entire payload subtree, including dotfiles. Payload members are relative to `/payload`; traversal, symlinks, unreadable members, and missing, extra or changed members fail closed.

The manifest remains self-hash-free as in revision 5. Its identity is bound externally by the existing custody receipts; this amendment introduces no recursive self-hash requirement. The final manifest/schema expression of the payload inventory must preserve that distinction.

Whole-image encryption checks, final ciphertext hashing, primary/replica byte equality and copy readback continue to cover the entire image, including OS metadata. A ciphertext digest does not prove payload semantics. A payload inventory does not claim to enumerate unread OS metadata contents. Both claims must be reported separately.

**C5C-restore-equivalence** now compares the complete declared payload inventory on each restored copy. The root metadata policy below is an additional required check on each attachment and restore. No successful restore may be declared while either required check is unavailable.

## Decision C5C-volume-metadata — Classify every volume-root entry

Enumerate every immediate root entry with no-follow inspection. The root may contain `/payload` and only individually named, justified OS metadata entries from an explicitly ratified policy. Reject unknown names, unsupported types, symlinks and policy mismatches. Never use a blanket dotfile, unreadable-directory or OS-generated-content exclusion.

Record each metadata entry's accessible attributes and the exact read depth. Where the ratified policy permits opaque OS metadata, explicitly report its contents as not read; do not present it as a complete content inventory or a clean-content finding. An inaccessible attribute needed by policy yields `unavailable` and stops admission.

For the native input profile, apply the exact policy below. Writable evaluator/comparison outputs still require complete scoped lifecycle observations and an explicitly ratified policy for names and attributes. Their observations must not silently widen the accepted input set.

No metadata chmod/chown, root-wide scanner, privileged traversal, logging suppression, deletion or OS configuration change is granted by this amendment.

## Decision C5C-input-seal — Tested native input-image procedure

This scoped procedure replaces direct encrypted source-path conversion for input images in this native proving profile. It does not yet establish the same procedure for writable output images or complete all four evidence-image classes.

The measured profile is macOS 26.6.2 build 25G83, arm64e `hdiutil` 683.160.3, executable SHA-256 `7b73b38f363c3fa1a338fb876d7bb7c9a6a8a9e5c1ba82fd74d8453a74c6795a`. The successful test used a 256 MiB UDIF image created with `-fs 'Case-sensitive APFS' -nospotlight -encryption AES-256 -stdinpass`; writable format was UDRW. Record this creation context when applying the input metadata rule. The observed set is not a promise for a different creation context or tool build. `-nospotlight` is part of the tested command, not evidence of filesystem-event suppression; no `.fseventsd` suppression or traversal is admitted.

The following are command shapes and acceptance requirements, not a runnable relay. `INPUT`, `VERIFIED_DEVICE` and `SEALED` must resolve to the exact attempt's admitted subjects. Every command must finish successfully within the existing bounds; missing or ambiguous evidence stops the attempt.

1. Create and independently validate the AES-256 UDRW input. Attach with ownership enabled; establish the exact case-sensitive APFS mount and writable access. Check the fresh root policy. Populate `/payload`, retain the complete payload inventory required by its contract, and check the populated root policy. Detach the writable image by exact identity and hash the entire source ciphertext.
2. Unlock that source using `hdiutil attach -readonly -nomount -stdinpass -nobrowse -noautoopen -plist INPUT`. The one supervisor supplies the same source secret through a fresh one-use NUL-terminated pipe. This operation exposes a transient decrypted block-device mapping; both persisted images must remain encrypted and no plaintext intermediate image file is allowed.
3. Correlate the attach result, complete `hdiutil info -plist` image identity and `diskutil info -plist` for every returned device. Require one unambiguous whole GUID-partitioned virtual disk backed by this exact image, readonly media throughout its returned device population, and no mounted source entity. Check the complete native mount population with a known mounted-filesystem positive control. Never select a fixed disk number, physical disk or unrelated device. Require the selected `/dev/diskN` to be a nonsymlink block-special device. Open it with `O_RDONLY|O_NOFOLLOW`, compare descriptor device/inode identity, close it, and immediately repeat image/device/no-mount checks. Permission denial or identity disagreement stops; do not use `authopen`, sudo or a permission change.
4. Perform exactly one `hdiutil convert VERIFIED_DEVICE -format UDRO -encryption AES-256 -stdinpass -o SEALED`, with the output secret supplied in another one-use pipe. Source unlock and output encryption are distinct operations. Detach the source by its verified identity and require its ciphertext SHA-256 to equal the preconversion digest.
5. Independently require `hdiutil isencrypted -plist SEALED` and `hdiutil imageinfo -plist -stdinpass SEALED` to pass the structural verifier below. Require `hdiutil verify -stdinpass SEALED` to report successful checksum verification. Hash the complete sealed ciphertext.
6. Attach `SEALED` readonly with `-owners on -nobrowse -noautoopen -stdinpass`, binding the exact mount through returned/native identities. Require case-sensitive APFS, ownership enabled and native readonly access. Apply the sealed root policy and compare complete payload membership, types, bytes, sizes and modes, plus UID/GID where required by the payload contract. Detach; require unchanged sealed ciphertext. Carry forward the existing primary/replica copying, both-copy restore, wrong-passphrase and write-denial obligations; the successful correction did not perform those controls.
7. On every exit, clean up only this attempt's verified attachment/process identities and retain results and any failure evidence. Compare attached-image identities against prestate. Unavailable cleanup proof is reported as such; no force detach, unrelated termination or same-identity restart is authorized. Dispose of the secret at supervisor exit as already required.

The single-supervisor secret boundary applies to create, attach, imageinfo, verify and convert. Each secret-bearing invocation receives a separate one-use pipe; the secret never enters argv, environment, retained files or logs and is not inherited by unrelated children. Synthetic tests retain their generated-memory-only secret policy; actual custody retains revision 5's user-passphrase admission policy. This amendment changes credential routing, not credential ownership or retention.

The completed correction was bounded to one conversion, 120-second command limits, a 20-minute total budget and 4 GiB free-space admission. These limits remain part of that correction profile. The broader probe retains its own approved image/conversion population and storage/container bounds; the single-image correction does not reduce or complete that population. A timeout is a failed attempt, not a reason to increase the limit or retry. Diagnostic identity-checked observations, if needed, must fit its separately bound instrument; no new live run is authorized by this document.

### Structural encryption verifier

Parse the complete native plists for the exact image. Require `isencrypted.encrypted == true`, `imageinfo.Properties.Encrypted == true`, the expected `Format`, and `Segments == [exact image path]`. Starting only at `Backing Store Information`, require exactly these class chains:

| Expected format | Exact outer-to-inner chain |
|---|---|
| UDRW source | `CEncryptedEncoding` → `CBSDBackingStore` |
| UDRO sealed input | `CUDIFEncoding` → `CEncryptedEncoding` → `CBSDBackingStore` |

Every layer's `URL` must be a local `file` URL with empty authority and decoded path equal to the exact image path. The one `CEncryptedEncoding` layer must declare `Encryption == AES-256`; no extra backing-store tail, absent field or unknown wrapper is accepted. An unrelated nested AES-256 value is not evidence. Failure to parse or bind the subject yields `unavailable` or `falsified` as appropriate, never acceptance. Filesystem `diskutil` encryption flags describe another layer and do not replace these container checks.

Retained controls include both observed formats and rejection of AES-128, missing algorithm, unrelated AES-256 decoy, unknown wrapper, wrong subject, wrong format, unencrypted flag and unexpected tail. Validate the next instrument against these complete retained shapes before its live admission. They establish coverage of these cases, not every possible native representation.

## Decision C5C-input-metadata — Exact native input root policy

For the scoped input profile above, enumerate **all immediate root entries** without following symlinks. Require this exact phase population:

| Phase | Exact root names | Required `.fseventsd` attributes |
|---|---|---|
| Fresh writable, before payload creation | `.fseventsd` | nonsymlink directory, UID 0, GID 20, mode 0700, flags 0 |
| Populated writable | `.fseventsd`, `payload` | same required attributes |
| Sealed readonly attachment and each restore | `.fseventsd`, `payload` | same required attributes |

`payload` must be a real directory whose attributes and complete recursive contents satisfy the applicable payload contract; UID 501 from the synthetic sample is not a universal owner requirement. Repeat the appropriate root check on every filesystem attachment and restore, including both retained copies. The unmounted source-device phase has no volume-root walk; it is governed by the no-mounted-entity checks above.

Record metadata size, inode, device and timestamps as observations, not cross-phase equality requirements. The successful run observed size 96 before sealing and 160 after sealing; this interval includes writable teardown and conversion and does not identify the changing operation. The sealed ciphertext did not change during readonly inspection. The retained snapshots did **not** collect timestamps; timestamp reporting is a forward requirement, not retrospective proof. Explicitly report an unavailable observational field. Any extra/missing name, symlink, changed required attribute, unreadable payload member or unavailable required policy measurement stops admission. Do not auto-expand the set or change an expected attribute to obtain a pass.

Metadata contents remain opaque and are not recursively read. A matched root policy is not a clean-content claim for `.fseventsd`. Exact recursive payload proof, including dotfiles, and complete ciphertext identity remain separate mandatory claims. No blanket dotfile exclusion, metadata chmod/chown, privileged traversal, deletion or filesystem-event suppression follows from this rule.

### Evidence basis and empirical floor

The completed correction `ec5873b7-191b-4253-95eb-f351fb799b34` performed one conversion in 1.508 seconds, followed by the encryption, checksum, readonly mount, payload and ciphertext checks above. The complete observed payload was one directory and two case-distinct files. It did not exercise the full Candidate-5 payload, primary/replica restoration, wrong-secret rejection, writable output ownership or Docker/native-bootstrap boundaries.

Evidence is archived under `HEB-154/conversion-correction/<attempt-id>/` in Development Archives. The original inventory binds 62 members (including 49 native command records); it excludes itself. A supplemental success inventory binds the later report, postcheck and structured diagnosis. These local archival references establish provenance; the operative rules are fully stated here for a cold reader.

| Retained artifact | Raw SHA-256 |
|---|---|
| Successful `conversion-correction-v2.py` | `4296f7a709861b32689085126a85f9642dcaf0b86c6cb63b474a3c030b83acbb` |
| Successful `inventory.json` | `96669b9c480000d8cb4a85ea04b955628c22ff88408ae4af04d14dfb5087ee0e` |
| Successful `success-inventory.json` | `58b5495bd2b3e4d8c191269c1c244a423e0ce4117a16492f263045c2269844f4` |
| Successful source ciphertext | `84c6a9b807d228eb50e52c33f7ddc8cb6cfcabdabf892c55393863f2339f1773` |
| Successful sealed ciphertext | `c3f85cb9df00cd6142fe69d5cc9e159aee3ea365ca927d357220a50e91b4b341` |

The empirical floor is **one fully verified synthetic sealing instance on this host**. Adopting this narrow profile is justified as the next bounded, fail-closed proving step: all names/required attributes must be reobserved, unknowns stop, and neither output-image behavior nor cross-host behavior is inferred. The secret was discarded; retained ciphertext does not promise future decryption. Original failed/corrected reports and their then-current disposition language remain immutable.

## Decision C5C-isolate — Expose only the payload subtree

The evaluator's two bind sources become the attached judge image's `/payload` subtree at `/run/in:ro` and the attached results image's `/payload` subtree at `/run/out:rw`. `/run/out/tmp`, stdout/stderr, preflight receipts and result files remain inside that payload. Apply the same source-subtree rule to each comparator input and its writable output.

The host verifies the exact no-follow bind-source identity; the effective Docker configuration and in-container mount evidence must agree with it. A whole-volume root bound at the expected target is a failed boundary even if the read/write flag is correct. Do not infer inaccessibility merely from directory permissions: the actor must have no exposed mount/path to the parent volume root or its metadata through the declared binds.

UID 21002, readonly root, dropped capabilities, no-new-privileges, IPC/network/logging restrictions, descriptor binding, complete effective-mount classification and write-denial controls remain unchanged. This amendment does not establish Docker Desktop compatibility or the native bootstrap's first-action guarantee.

## Amendment and obligation reconciliation

| Existing clause or artifact | Effect |
|---|---|
| Revision-5 `C5C-images`, `image-manifest.json`, `C5C-restore-equivalence` | Payload-domain inventory plus separate whole-ciphertext and root-metadata claims as above |
| Revision-5 `C5C-isolate` and comparator mounts in `C5C-seal-compare` | Bind each image's `/payload`, preserving all phase/access rules |
| `C5M-2` | Extend the boundary instrument to refuse a whole-volume bind and prove payload-only source identity |
| `C5M-5` | Distinguish payload restoration, whole-ciphertext identity and root-policy outcomes; add the tested native input sealing sequence and structural verifier |
| Revision-5 `C5C-images` input conversion and secret-bearing image operations | Explicit readonly/unmounted source unlock, verified-device conversion, and per-invocation one-use secret delivery as above |
| `C5M-1`, `C5M-3`, `C5M-4`, `C5M-6` | No relaxation of projection, authority, ordering or fail-stop demands |
| Frozen test definition revision 4 and historical reviews | Preserve bytes and historical meaning; do not claim they reviewed the new interpretation |

The affected `C5M-2`/`C5M-5` interpretation must enter the next test-definition revision and a separately authorized focused review after the remaining output metadata policy is complete. `C5M-3` admission must bind the amended input procedure and exact source/instrument identity; its existing authority requirement is not waived. Retain the six stable IDs; do not manufacture review closure from this ratification.

Verification must include exact payload restore from both copies and refusals for an extra payload member, missing/changed member, unexpected root entry, unreadable required attribute, and a whole-volume bind substituted for `/payload`. Controls operate on their named populations; they may not silently alter the expected policy to pass.

## Risks, evidence handling and lifecycle gates

Opaque system metadata limits the claim that can be made about its contents. Exact ciphertext identity preserves those bytes without claiming to understand them. A later requirement to inspect, suppress or exclude particular metadata content reopens that decision explicitly.

Failed probe artifacts remain preserved in the local Development Archives under `HEB-154/platform-probes/<attempt-id>/`, with source attempts retained in Working. Generated test secrets were discarded; future decryption is not promised. No evidence relocation, deletion or retrospective alteration is part of this amendment.

| Transition | Required evidence | State |
|---|---|---|
| Boundary acceptance | Tad's ratification of the three proposed boundary decisions | passed |
| Native input procedure and root policy | complete scoped observations and Tad's adoption of both concrete dispositions | accepted for this input profile; empirical limits above |
| Writable evaluator/comparison-output metadata policy | complete scoped observations and per-item operator disposition | pending |
| Focused design/test-definition reconciliation | exact changed bytes and separately authorized review | pending |
| Conformance probe | complete policy and aligned instrument; fresh bounded attempt | not admitted by this document alone |
| Implementation, runtime verification and calibration | existing separate gates and required evidence | pending |

## Change log

| Revision | Date | Change |
|---|---|---|
| 1 | 2026-09-19 | Recorded the ratified payload/metadata boundary, its clause replacements and the unresolved metadata-policy gate; preserved historical authorities and evidence. |
| 2 | 2026-09-19 | Adopted the tested native input sealing sequence, exact structural encryption verifier and narrow input root policy; retained output-policy, focused-review and broader-proving gates. |
