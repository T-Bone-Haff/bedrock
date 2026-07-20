---
name: author-execution-relay
description: Author an execution relay — the handoff prompt that delegates file and git toil to an executor surface (Claude Code) while keeping every judgment with the operator. Carries the four-block spine (fresh-fetch guard → task → stop gate → mutation rider), posture selection (report-and-STOP vs. gated transaction), premise and pin discipline, adjustment licenses, escape-hatch design, and output discipline. Use whenever drafting the Code relay or handoff — "draft the relay," "hand this to Code," "write the handoff prompt," "relay this for execution" — or any time a deliberation surface is about to hand file or git operations to an executor. Authoring-side only: this skill is consumed at relay-drafting time, and the relay artifact it produces is what governs the executor. Assumes the three-actor working model (deliberation surface / executor / ratifying operator); a different working model is a rebind.
---

# Author an Execution Relay

An *execution relay* is a prompt artifact handed from a deliberation surface to an executor surface, carrying an operation the operator has adjudicated but not yet performed. This skill's one job is to make that artifact **safe to obey**: every judgment stays with the operator, every premise is verifiable, and the executor's obedience — or its refusal — is itself evidence.

**Binding:** the three-actor working model — a deliberation surface that proposes and adjudicates, an executor (Claude Code) that performs file and git operations, and a ratifying operator whose per-gate go is the operator act. A materially different working model is a rebind, not a line-edit.

**Scope:** authoring-side only. The skill fires when the relay is *drafted*. Executor behavior — stop semantics, licenses, gates — is governed by the relay artifact this skill produces, not by the executor loading this skill. The standing principles the relay instantiates (fresh-fetch over recall, no presumed alignment, ratification as the operator act) are codified in the operator's always-loaded doctrine; this skill does not re-house them — it converts them into artifact structure at the moment of drafting, the same relationship `author-decision-record` has to "don't fabricate."

**The delegation test, before drafting anything:** does this handoff remove the operator's *decision*, or only the operator's *labor*? Only-labor is safe to delegate; the decision never is. A control is real if it survives the operator losing their keyboard — a gate that requires the operator's typing was delegating judgment and keeping toil, exactly backwards.

## The four-block spine

Every relay carries four blocks, in this order. The order is load-bearing: the guard precedes the task so verification cannot be skipped by momentum; the rider trails the task so mutation constraints arrive with the mutations in view.

1. **Fresh-fetch guard** — the executor re-reads the governing doctrine from disk and never trusts the relay's summary of it or any prior-session memory (prior-art-as-authority is a named failure mode). The guard opens with an **identity gate**: remote, branch, expected files. Mismatch is stop-and-report, never search-and-substitute.
2. **Task** — the operation itself, scoped and numbered, with per-item stop points wherever ratification is per-item, and base hashes for anything the relay replaces.
3. **Stop gate** — what may be touched, what must not be, and the transaction posture (next section). Touch-scope is an allowlist of declared outputs, never a description of intent.
4. **Mutation rider** — per-target verification of the stated FROM, the adjust-and-flag licenses (or their explicit absence), and the blanket STOP default.

A compact skeleton:

```
═══ FRESH-FETCH GUARD ═══
You are <executor> working <repo>. This is an EXECUTION request relayed by the
operator. Re-read the governing doctrine from disk — do NOT trust this prompt's
summary of it, or prior-session memory. Identity gate: verify remote, branch,
and that each named target exists as stated. On ANY mismatch: STOP and report.

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
- **Pre-state assertions are claims the executor verifies, not context it trusts.** "This file currently says X" is a checkable claim; write it as one.
- **Operator assertions are claims too.** An instruction that embeds a factual claim — "note that X happened" — owes that claim a fresh verification before any durable write. Transcribing it because the operator said it is prior-art-as-authority wearing a different hat.
- **Build change-lists from the live tree**, never from a document's description of its own layout — maps drift from the territory they claim.
- **Fresh-read the tool the relay describes.** A relay's premise can be stale against the very artifact it governs; the author may be working from recall of an older tool state.
- **Drafting inherits verify-first.** The relay is itself a write against the target repo's process — verify the target's transaction conventions (git topology, ignore rules, which process owns the commit) *before* drafting, exactly as the executor verifies file state before editing. The executor's halt rule is the second line of defense, not the first.

## Pin discipline

- **Pin content, not history position.** A content hash covers exactly the bytes the ratification covered and is verifiable by any surface holding the file; a commit SHA pins a tree position that moves under rebase and covers bytes nobody adjudicated.
- **A replacement handoff pins both ends:** the base hash (executor STOPs if the target moved since the replacement was authored — drift in the world) and the replacement hash (executor STOPs if its own write doesn't reproduce the ratified bytes — drift in the executor; a transcription defect is not a license to edit).
- **Two transports carry a replacement; the pins are identical either way.** *Executor-writes:* the relay carries the ratified payload; the executor writes it and re-hashes its own write against the replacement pin. *Pre-placed:* the deliberation surface places the ratified bytes in the working tree before the relay fires; the executor **verifies rather than writes** — replacement pin checked against the bytes on disk, base pin checked from `git show HEAD:<path>`, since the tree no longer holds the base. A mismatch on either end is STOP under both transports. Pre-placement moves labor across the seam, never judgment: the ratified bytes are still the operator's, and the executor's verification is what makes them landable.
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
- **Verbatim payloads are wrap-safe or they are not verbatim.** A payload whose bytes are the deliverable — an append fragment, a commit message, a marker block — is never margin-wrapped by an authoring pass: no line break lands mid-token, and whitespace inside the payload is content, not formatting. Carry such payloads fenced, and where the bytes matter enough to pin, validate with a hash or token-integrity check — the executor catching a wrapped token at the gate is the *last* line of defense, not the discipline.
- **Pin the environment of every exact-match assertion.** Any byte-for-byte check over locale- or environment-sensitive tool output (`sort`, `ls`, glob order, date formatting) pins its environment (`LC_ALL=C`) or drops the exact-match — an unpinned assertion is a false-RED landmine on a different machine.

## Drafting posture

- **Phrase constraints as values, not procedures.** "Do not invent what you don't have" transferred cleanly from decision-record rationale to file operations because it names a value; a procedure stops at its enumerated cases. Values generalize to the unscripted condition the relay's author didn't foresee.
- **Constraints ride in the handed artifact, never in accompanying prose or memory.** When an act crosses surfaces, embed the constraint in the artifact itself — a base-pinned URL beats "make sure the base is right"; defaults beat documentation. The correct path should be the lazy path.

## Boundaries with sibling skills

- **Reviewing the landed change** → the `code-review` skill. It also owns narrated-process-is-data and the review-instrument design that enforces it; this skill instantiates that rule on the artifact side, and cites rather than restates it.
- **Authoring this skill, or any reusable standard** → the `author-standard` skill: membership, sourcing, binding, shape, hardening, and proving all live there.
- **Authoring a decision record the relay might land** → the `author-decision-record` skill; the relay carries the record, it doesn't author it.
