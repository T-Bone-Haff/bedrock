---
name: author-execution-relay
description: "Executor prompts and handoffs only; every gated instruction sent to Code or another executor routes here, never to app-delivery-pipeline, even when it mentions delivery gates or starts from a construct spec. Use this skill to author an execution relay, implementation handoff, or session kickoff that delegates bounded file and git toil while reserving judgment and per-gate ratification for the operator. Here Code means the executor, not application source code. Do not use this to perform implementation, write a general design record or reusable standard, or review a finished diff."
---

# Author an Execution Relay

An *execution relay* is a prompt artifact handed from a deliberation surface to an executor surface, carrying an operation the operator has adjudicated but not yet performed. This skill's one job is to make that artifact **safe to obey**: every judgment stays with the operator, every premise is verifiable, and the executor's obedience — or its refusal — is itself evidence.

**Binding:** the three-actor working model — a deliberation surface that proposes and adjudicates, an executor (Claude Code) that performs file and git operations, and a ratifying operator whose per-gate go is the operator act. A materially different working model is a rebind, not a line-edit.

**Scope:** authoring-side only. The skill fires when the relay is *drafted* — and equally when a session kickoff or session handoff is drafted, the artifact classes § Claim discipline binds. Executor behavior — stop semantics, licenses, gates — is governed by the relay artifact this skill produces, not by the executor loading this skill. The standing principles the relay instantiates (fresh-fetch over recall, no presumed alignment, ratification as the operator act) are codified in the operator's always-loaded doctrine; this skill does not re-house them — it converts them into artifact structure at the moment of drafting, the same relationship `author-decision-record` has to "don't fabricate."

**The delegation test, before drafting anything:** does this handoff remove the operator's *decision*, or only the operator's *labor*? Only-labor is safe to delegate; the decision never is. A control is real if it survives the operator losing their keyboard — a gate that requires the operator's typing was delegating judgment and keeping toil, exactly backwards.

## The relay spine

Every relay opens with Block 0 and carries four blocks after it, in this order. The order is load-bearing: the assertions table precedes the guard because the guard and the executor's checks are what discharge it; the guard precedes the task so verification cannot be skipped by momentum; the rider trails the task so mutation constraints arrive with the mutations in view.

0. **Block 0 — external assertions** — the `EXTERNAL ASSERTIONS` table (§ Claim discipline): every claim the relay makes about state outside itself, its provenance, and where it is checked. An assertion in the body absent from the table is a defect the executor reports.
1. **Fresh-fetch guard** — the executor re-reads the governing doctrine from disk and never trusts the relay's summary of it or any prior-session memory (prior-art-as-authority is a named failure mode). The guard opens with an **identity gate**: remote, branch, expected files. Mismatch is stop-and-report, never search-and-substitute. The identity gate extends to every authority the guard cites: each doctrine the executor is instructed to re-read is named by explicit path, resolved and existence-verified at drafting time — an alias is an unverified premise. Where the executor's operations run through a tool that takes exclusive locks, the identity gate checks for stale ones and treats any as **STOP-and-report, never delete** — the executor cannot distinguish a stale lock from a live concurrent operation, and that judgment is the operator's.
2. **Task** — the operation itself, scoped and numbered, with per-item stop points wherever ratification is per-item, and base hashes for anything the relay replaces.
3. **Stop gate** — what may be touched, what must not be, and the transaction posture (next section). Touch-scope is an allowlist of declared outputs, never a description of intent.
4. **Mutation rider** — per-target verification of the stated FROM, the adjust-and-flag licenses (or their explicit absence), and the blanket STOP default.

A compact skeleton:

```
═══ BLOCK 0 — EXTERNAL ASSERTIONS ═══
| # | Assertion | How known | Checked at |
<one row per claim about state outside this relay; an assertion in the body
absent from this table is a defect: report it and STOP>

═══ FRESH-FETCH GUARD ═══
You are <executor> working <repo>. This is an EXECUTION request relayed by the
operator. Re-read the governing doctrine from disk at <named path(s)> — do NOT
trust this prompt's summary of it, or prior-session memory. Identity gate:
verify remote, branch, and that each named target exists as
stated; check for stale tool locks and report any without deleting. On ANY
mismatch: STOP and report.

═══ TASK ═══
<The operation, scoped and numbered. Per-item stop points where ratification is
per-item. Base hash pins for every file this relay replaces.>

═══ STOP GATE ═══
Touch only: <the declared outputs>. Stage only those paths — never a broad add.
<Posture: report and STOP — the commit is the operator's | gated transaction:
execute commit → push → PR → merge → cleanup, STOPPING at each named gate for
the operator's go. Running past a gate is never licensed.>

═══ MUTATION RIDER ═══
Verify each target's stated FROM on disk before editing. On ANY mismatch: STOP
and report — do not reconcile by guess. Adjust-and-flag license: <one named,
narrow class — or "none">. Everything else: STOP on discrepancy.
```

## Posture selection

Two transaction postures, chosen at drafting time — the relay states which one it carries:

- **Report-and-STOP (the default).** The executor changes files, reports what it changed, and stops; nothing enters history without the operator's own commit. A relay without an explicit authorization block *is* this posture. Choose it when the operator needs the working tree inspectable before anything is committed, or when the transaction shape isn't fully known at drafting.
- **Gated transaction (explicit authorization).** The relay carries an authorization block naming the full transaction — commit → push → PR → merge → cleanup — and the executor STOPs at each named gate for the operator's go. The per-gate ratification IS the operator performing that step; the executor's hands are clerical. Running past a gate is never licensed. Choose it when the transaction shape is settled and the operator's control is judgment at the gates rather than possession of the keystrokes. The operator may, live at a gate, elect to batch-authorize a named span of the remaining gates in one explicit go — ratification at coarser grain, not a license to run past anything: the batch names its gates, halt-on-anomaly is retained in full, and any anomaly voids the remainder of the batch, re-atomizing the gates. The election is always the operator's at transaction time; a relay never pre-authorizes a batch.

## Premise discipline

Every relay carries silent premises — which repo, which branch, which version, which file state — and the author didn't notice they were premises. The discipline is structural, not vigilance:

- **The identity gate makes repo-identity premises explicit.** Name the remote, the branch, the expected targets; instruct mismatch = stop-and-report. An unstated identity premise meets a frozen archive or the wrong clone silently.
- **Name every artifact by explicit path, never by alias.** Any reference the executor must resolve — governing doctrine, a skill, a charter, a target file — resolves to an explicit path (or pinned URL) at drafting time, existence-verified by a safe read before the relay fires. An alias ("the vault doctrine," "your CLAUDE.md chain") delegates premise-resolution to executor guesswork, and resolution against the wrong artifact is silent until it isn't.
- **Pre-state assertions are claims the executor verifies, not context it trusts.** "This file currently says X" is a checkable claim; write it as one. Block 0 (§ Claim discipline) is the table these claims land in.
- **Operator assertions are claims too.** An instruction that embeds a factual claim — "note that X happened" — owes that claim a fresh verification before any durable write. Transcribing it because the operator said it is prior-art-as-authority wearing a different hat.
- **Build change-lists from the live tree**, never from a document's description of its own layout — maps drift from the territory they claim.
- **Fresh-read the tool the relay describes.** A relay's premise can be stale against the very artifact it governs; the author may be working from recall of an older tool state.
- **A tool operation does more than it says.** Every command a relay's author or executor issues runs through a toolchain with its own mutation paths — hooks, templates, filters, locks, caches, format-on-save. The relay never assumes the operation was only what it named. On the **write** path, verify the artifact the tool stored rather than the input you handed it (§ Pin discipline). On the **read** path, use the form that observes without mutating (below).
- **Drafting inherits verify-first.** The relay is itself a write against the target repo's process — verify the target's transaction conventions (git topology, ignore rules, which process owns the commit) *before* drafting, exactly as the executor verifies file state before editing. The executor's halt rule is the second line of defense, not the first.
- **Drafting-time inspection is read-only or it is a mutation.** The verification a relay's author performs against the target is itself a touch. Use the read-only form of every inspection command (`git --no-optional-locks status`, `git log`, `git show`, `git cat-file`) and never a form that takes a lock, refreshes an index, or writes a cache. A drafting surface that cannot release what it acquires leaves the executor a failure the relay never mentions — and the author is the one party guaranteed not to see it.

## Claim discipline (no naked claims)

Every claim an artifact makes about state outside itself carries its provenance: **measured** (the command, where it ran, when), **assumed** (declared, with why the assumption is survivable), **an act with a named owner**, an explicit **UNVERIFIED** flag — or **UNSTATEABLE**, for a claim that cannot state itself in principle (a file's own hash; a value that exists only after the artifact is sealed). UNSTATEABLE is a legal value precisely because a row that wants filling invites a fabricated one; the true value travels beside the artifact, never inside it.

Three rules are this discipline applied to its recurring cases, not additions to it:

- **Platform:** every command the artifact carries states `run on <platform>` or `never run`. Runnability is a property of text paired with a platform, and the pairing is what artifacts silently omit.
- **Corpus:** every quantified claim ships with the command that recomputes it.
- **Payload:** every pinned payload is extracted back out of the finished artifact and re-hashed (§ Pin discipline owns the transport forms).

**Block 0 is the table rendering of this discipline:** the relay opens with an `EXTERNAL ASSERTIONS` table — each row a claim, how it is known, and where it is checked — under two closure rules: every act named as done has a named owner, and every claim is checked-or-accepted-with-reason. An assertion in the body absent from the table is a defect the executor reports. This subsumes Premise discipline's claim bullets: a pre-state assertion or an embedded operator claim is a Block 0 row, not a second mechanism. The table's candidate-generation mechanics and stopping rule are the Block 0 spec's concern, not this skill's — the spec's home is HEB-85, its codification pending; the deferral names a home, not a landed artifact.

**Scope:** this discipline binds not only relays but session kickoffs and session handoffs — any artifact handing an executor or successor surface a claim-bearing brief (HEB-85 scope ruling, 2026-08-06).

## Instrument discipline

An instrument is anything whose output is offered as evidence — a check authored into the relay, or one the executor invents mid-transaction. The relay carries this discipline as executor-facing text (the drafter's obligation is to include it), so it binds the inventor of every check, whichever surface invents it. An instrument's output does not count as evidence until three things are stated:

- **Its claim, including what it actually reads.** What a pass asserts, and the input it asserts it from — a check that reads a local tracking ref cannot claim remote identity, and the vacuousness is visible the moment the input is named.
- **Its population.** What both arms of any comparison range over, asserted by count *before* comparing.
- **Its third outcome.** What it reports when it could not measure: empty input, unreachable subject, wrong environment.

Two hard rules: **a digest of unverified-nonempty input is a failure, not a value**, and **a suspiciously clean report is a failure signal, not a pass** — a first reading that would indict a durable artifact is re-run before it is reported, and both readings are reported, never only the corrected one.

## Pin discipline

- **Pin content, not history position.** A content hash covers exactly the bytes the ratification covered and is verifiable by any surface holding the file; a commit SHA pins a tree position that moves under rebase and covers bytes nobody adjudicated.
- **A replacement handoff pins both ends:** the base hash (executor STOPs if the target moved since the replacement was authored — drift in the world) and the replacement hash (executor STOPs if its own write doesn't reproduce the ratified bytes — drift in the executor; a transcription defect is not a license to edit).
- **A third drift class: the tool interposes.** Base drift and executor drift both assume the only mutation paths are the world's and the executor's. Toolchains carry their own. Where a relay pins a payload a toolchain could rewrite, the guard checks that the tool's mutation surfaces are inert before the operation — in git, hooks, a configured `commit.template`, line-ending and filter config; in another toolchain, its equivalents. The check is cheap and fails early. **It is not what makes the pin sound** — verification after the operation does not depend on having enumerated them correctly.
- **Three transports carry a change; every transport pins both ends.** *Executor-writes:* the relay carries the ratified payload; the executor writes it and re-hashes its own write against the replacement pin. *Pre-placed:* the deliberation surface places the ratified bytes in the working tree before the relay fires; the executor **verifies rather than writes** — replacement pin checked against the bytes on disk, base pin checked from `git show HEAD:<path>`, since the tree no longer holds the base. *Derived-edit:* the relay carries no payload but a deterministic edit rule plus the base pin; the deliberation surface independently derives the **expected post-edit bytes** from the rule against the pinned base and pins them; the executor performs the edit and re-hashes its result against that pin. The post-edit pin is conditional on the base pin — a moved base fails first, so derivation at drafting time is safe. A mismatch on either end is STOP under all three transports. A relay MAY mix transports across targets; each target names its transport explicitly and carries that transport's pins — a target's transport is never left to inference. Pre-placement and derivation move labor across the seam, never judgment: the ratified bytes (or the rule that determines them) are still the operator's, and the executor's verification is what makes them landable.
- **Verify the durable form, not the input to the tool.** A pin over a payload handed to a tool is discharged against the artifact the tool stored, read in its rawest available form — the commit object, not `git log --format=%B`; the file on disk, not the string the executor believed it wrote. Convenience readers interpose their own formatting: trailing newlines, wrapping, escape handling. **A hash over a convenience read is a hash over the reader.**
- **A hash proves fidelity, not sanity.** Pins verify that the landed bytes are the ratified bytes; they say nothing about whether those bytes are sane to land. An executor reading the full content or diff before landing is sanctioned conduct, not instruction-creep — author the relay expecting the read, and anything it surfaces arrives as gate input, never as a license to edit.
- **A gated transaction closes with third-surface verification:** an independent surface re-hashes the landed artifacts against the ratified pins. Authored = ratified = landed becomes provable without trusting any single reporter — the executor's account of having verified is itself just a claim.

## License discipline

Separate, explicitly, what the executor may **adjust-and-flag** from what must **STOP on discrepancy** — and make STOP the blanket default. Default-adjust is how executors improvise past load-bearing pins; default-STOP-on-everything is brittle, halting real work on a stale process reference. The shape that works: STOP as the stated default, plus a narrow, named, operator-granted license for one class of discrepancy (e.g., a SHA-at-HEAD reference that has legitimately moved). Adjusted items are flagged, never silently substituted, and the license is declared spent at completion — it does not survive into the next relay.

## Escape hatches

- **Encode constraints as tripwires, not absolutes.** "Implement with zero prompt-byte changes; if the target requires byte changes, stop and surface the exact contradiction" converts pressure into a scoped escalation. An absolute invites creative reinterpretation under pressure; a tripwire routes the judgment back to the operator. The fence works *because* it names its own escape hatch.
- **"Stop and flag rather than guess" is what converts the executor into an auditor.** Faithful execution forces every premise in the relay to touch reality; without the clause, the executor silently absorbs the correction — the artifact comes out right while the record stays wrong, and the divergence goes invisible.
- **Read refusals as diagnostics.** A precise refusal — "this isn't one scoped edit; it needs wording choices the rule doesn't determine" — is not non-compliance; it is the executor classifying the directive as mis-scoped. Design the relay so refusal-with-reasons is a sanctioned output, and read the reasons as feedback on the relay's own scoping.

## Output discipline

- **Scope the stage to the operation's declared outputs** — named paths, never `-A` / `-a` / `.`. A broad stage sweeps unexamined working-tree dirt into the operation's commit; unrelated dirt gets its own commit.
- **Demand a proposed-commit artifact, not a done-story.** Completion is granted at a gate, never narrated past one — a done-story reads as a fact to ratify rather than a request to gate, and the gate never visibly fires. The executor's completion report is data to verify, not a verdict that discharges verification; `code-review` owns that rule (narrated process is data) — this discipline instantiates it in the relay artifact.
- **Verbatim payloads are wrap-safe or they are not verbatim.** A payload whose bytes are the deliverable — an append fragment, a commit message, a marker block — is never margin-wrapped by an authoring pass: no line break lands mid-token, and whitespace inside the payload is content, not formatting. Carry such payloads fenced, and where the bytes matter enough to pin, validate with a hash or token-integrity check **over the durable artifact (§ Pin discipline), never over the payload as handed in** — the executor catching a wrapped token at the gate is the *last* line of defense, not the discipline.
- **An otherwise-verbatim payload MAY carry named fill-slots.** Each slot is explicitly marked (a `<VERSION>`-style token), its fill rule is deterministic and stated in the relay — any surface applying the rule to the pinned base derives the same bytes — and everything outside the slots stays wrap-safe verbatim. An unnamed slot, or one whose fill requires judgment, voids the payload's verbatim status. Verification takes the derived-edit form: the deliberation surface derives the expected post-fill bytes and pins them.
- **Pin the environment of every exact-match assertion.** Any byte-for-byte check over locale- or environment-sensitive tool output (`sort`, `ls`, glob order, date formatting) pins its environment (`LC_ALL=C`) or drops the exact-match — an unpinned assertion is a false-RED landmine on a different machine.
- **No transaction closes with a specified use pass unrun.** Where the relay names a use pass — render it, read it, operate it — the executor runs it before close or reports `could not run: <reason>`; silence is neither.

## Calibration

Periodically point a cold, context-free reader at artifacts that already passed this skill's authoring-side checks — and **record every second catch of an already-known defect as data, never dropped as noise**. Deliberate overlap between independent catchers is the only measurement of what the whole system misses; without the recording rule, zero recorded overlap is uninterpretable. Seam: this practice samples relay-class artifacts for authoring-check misses; review-instrument empiricism stays at its home in `design-review-loop`.

## Drafting posture

- **Phrase constraints as values, not procedures.** "Do not invent what you don't have" transferred cleanly from decision-record rationale to file operations because it names a value; a procedure stops at its enumerated cases. Values generalize to the unscripted condition the relay's author didn't foresee.
- **Constraints ride in the handed artifact, never in accompanying prose or memory.** When an act crosses surfaces, embed the constraint in the artifact itself — a base-pinned URL beats "make sure the base is right"; defaults beat documentation. The correct path should be the lazy path.

## Boundaries with sibling skills

- **Reviewing the landed change** → the `code-review` skill. It also owns narrated-process-is-data and the review-instrument design that enforces it; this skill instantiates that rule on the artifact side, and cites rather than restates it. Review instruments are its territory; this skill's instrument discipline governs the checks a relay carries or an executor invents mid-transaction.
- **A prompt the code ships** — a charter, a shipped prompt artifact — → the `agent-code` skill; a prompt the operator hands to an executor is this skill's relay. The two partition the prompt-artifact class, and `agent-code` declares the same seam from its side.
- **Authoring this skill, or any reusable standard** → the `author-standard` skill: membership, sourcing, binding, shape, hardening, and proving all live there.
- **Authoring a decision record the relay might land** → the `author-decision-record` skill; the relay carries the record, it doesn't author it.
