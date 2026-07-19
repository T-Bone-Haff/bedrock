# HEB-38 Phase-2 — Antagonistic Review Findings (Pass 2) — Handoff to the Authoring Session

> **What this is:** interim antagonistic-review findings on the **converged** Phase-2 enforcement staging file (`heb-38-phase-2-enforcement-edits.md`), for handoff to the authoring session.
> **What this is NOT:** a review-of-record. It is one contributing pass; the durable review-of-record is the separate Pass-1→Pass-N convergence artifact vendored at close-records (`docs/reviews/`). Disposition routing per DIRECTIVE-032 §32.3 — findings return to the authoring session verification-only; the reviewer does not self-fix. All dispositions below are **proposed, pending per-item ratification**.

**Reviewed artifact:** `heb-38-phase-2-enforcement-edits.md` (converged cut, Blocks 1–8).
**Corpus baseline:** HE-Bedrock `main` @ `28a496a` (kit 2.4.0; CSD 3.2.0; DMS 3.2.0) — unchanged; no Phase-2 PR merged.
**Substrate fresh-fetched this session (no recall):** corpus @ `28a496a` (DMS §4.6/§7.x, CSD DIRECTIVE-007 §7.1–§7.5.3 + DIRECTIVE-023 + §24.1, ENG-STD-003 §13.5.x, review-template §2, PROVENANCE, Phase-1 rulings file); live HEB-38 ticket + full comment trail (incl. the 2026-06-26 Roadmap-correction comment); Notion Phase-1 ruling SoR (`38acaeea…`, R040–R042, max R042).

**Outcome:** **PASS WITH FINDINGS.** No BLOCKING findings — both Pass-1 blockers are cleared. 2 MATERIAL (A2-M1 restatement-at-template, A2-M2 routing) for in-scope fix or ratify; 3 COSMETIC. The gate (ready for Phase-2 apply-prompt authoring) is satisfiable without another full review cycle, once A2-M1 and A2-M2 are dispositioned.

---

## 1. Pass-1 findings — disposition check (verified, not taken on the rebuild notes' word)

| ID | Pass-1 finding | Status |
|---|---|---|
| A-B1 | Phase-2 scope drift (#4/#6 dropped; lens relabeled) | **Resolved** at ticket level (Roadmap-correction comment): #4 → HEB-12 + Phase-3 ship event; #6 → Phase-4 (+ §7.9-interim-coverage note); lens = Phase-2 completing AC2 active-read leg. File scope ledger now matches. |
| A-B2 | §7.6 lens restates §7.7 test + §7.2 rationale | **Resolved.** §7.2.1 references the §7.7 test (no stranger-build paraphrase); increment crisply drawn as detection-vs-tagging. "Does not restate" claim now true. |
| A-C1 | §7.6 ↔ DMS §7.6 coordinate collision | **Dissolved** by the §7.2.1 home. |
| A-M1 | §7.2/§7.6/§7.7 surface-identity unpinned | **Pinned:** §7.2 *is* the §7.7 "review findings model" surface; no §7.7 enumeration touch owed; no DMS edit pulled in. |
| A-M2 | check-spec use/mention boundary unspecified | **Resolved:** concrete-ID-anchored (`R\d+`, `{{TRACKER_PREFIX}}-\d+`, `B-\d+`/`M-\d+`), schematic forms excluded, framed as a closed subset of §7.4's open set. New Block 2 text is itself check-conformant. |
| A-M3 | §24.1 ↔ §7.4 collision papered over | **Dispositioned:** instance resolution (descriptive reference) ratified; general seam routed out — *but see A2-M2 on the routing target.* |
| A-M4 | versioning rationale right-answer-wrong-reason | **Resolved:** MINOR now grounded in §7.9 grandfather-until-touched + aspirational status; false claim removed. |
| A-C2 | "re-anchor per §13.5.10" mis-cite | **Resolved:** corrected to §13.5.2 with the precise distinction. |
| A-C3 | R026 cited from recall | **Resolved:** verify-at-apply-prompt caveat added. |

Anchors (Blocks 2–7) re-verified verbatim against `28a496a`. Block 1 insert-after anchor (`This is the audit-trail substrate that prevents future audits from re-doing the work.`) confirmed **unique** (single occurrence) and correctly placed at the §7.2 tail before §7.3 (no `---` between). `##### 7.2.1` at h5 has precedent (§7.5.1–.3).

---

## 2. New findings (Pass 2)

### 2.1 MATERIAL

#### A2-M1 — The review-template §2 gloss (Block 4) leans back into restatement — a softer recurrence of the A-B2 class, at the delivery surface

**Remedy:** remove/relocate (→ trim Block 4 to a barer reference) **OR** ratify the one-line gloss as acceptable framing.

**Location:** staging file Block 4, review-template `§2` intro, NEW second paragraph.

**Description:** The NEW paragraph reads: *"…apply the **contract-purity lens** per DIRECTIVE-007 §7.2.1 and DMS §7.7 — a standing per-pass active read that raises remove/relocate findings for process-narrative / restatement belonging on an audit surface."* The clause after the dash is a compressed gloss of §7.2.1's own core sentence. DMS §7.7/§7.8 are strict — delivery surfaces *reference, never restate* — and the review template is one of the four enumerated §7.7 delivery surfaces. The §7.2.1 lens definition is clean; this is the template re-describing it. Milder than the original A-B2 (one line, leads with the citation, no canonical-test reproduction), and there is a real usability tension: a bare pointer may be too thin for a template reviewers actually read.

**Disposition (proposed):** Pick one and apply it **consistently across all four §7.7 surfaces** (content-contracts, this template, skill-nudge, CI bullet) so reference-vs-gloss does not drift per surface:
- *(a) Trim:* "…additionally apply the contract-purity lens per DIRECTIVE-007 §7.2.1 / DMS §7.7." (barer reference)
- *(b) Ratify the gloss:* accept a one-line orienting gloss as legitimate referential framing for delivery surfaces, and record that as the standing convention.

*Note:* the file's Rebuild notes cover Block 4's cite-retarget and the contract-comment "findings from" fix but are **silent on the gloss** — it is currently unflagged.

#### A2-M2 — The §24.1 ↔ §7.4 seam is routed to HEB-39, which looks like a category mismatch

**Remedy:** add/fix (→ confirm HEB-39's scope is being broadened, or spin the seam its own deliberate-first ticket).

**Location:** staging file Block 2 authoring note + Scope ledger ("§24.1↔§7.4 general seam (routed to HEB-39)").

**Description:** HEB-39 is scoped to the **ENG-STD-002/-003 analogue** — reference-purity for *scripts + apply-prompts*, a different artifact class. The §24.1↔§7.4 seam is a collision *within the existing governance-doc class*: DIRECTIVE-024 §24.1's `tracked at {{backlog item ID}}` template instructs inline ID-naming, which §7.4 prohibits in ADR/DDR/SDD morphing bodies. That is not "extend the doctrine to a new artifact class" (HEB-39's charter) — it is an internal inconsistency in the already-landed doctrine. Routing it to HEB-39 either silently broadens HEB-39 or mis-files the seam.

**Disposition (proposed):** Confirm whether HEB-39 is being deliberately broadened to own CSD-internal reference-purity seams (state it), or give the seam its own deliberate-first ticket (DIRECTIVE-025 dedup first). Low effort; matters because a mis-routed seam is the kind of item that quietly never gets worked.

### 2.2 COSMETIC

- **A2-C1** — Line 13 framing: *"the two ratified DMS §7.7 delivery surfaces — the review findings model (the active-read lens)…"* is lossy. The review-findings-model surface is §7.2 *as a whole*, whose remedy-axis leg landed Phase-1; Phase-2 lands its **active-read leg**, not the whole surface. Line 14's keystone states it correctly. — `[add/fix]`
- **A2-C2** — Lone-numbered-child §7.2.1 (one numbered sub-subsection among §7.2's unnumbered bolded leads). Already flagged in-file as an override candidate; the citeable-anchor rationale is sound, so acceptable as-is. Heavier alternative (number all §7.2 leads) is reference-preserving MINOR but out of Phase-2 scope — deliberate-first carry-forward if the asymmetry grates. — `[none — acknowledged]`
- **A2-C3** — Optional polish in the §7.2.1 NEW text: the closing *"It references the DMS §7.7 test; it does not restate it"* is accurate but is faint meta-narrative about the document's own construction (a small irony given the doctrine); the reference itself already establishes reference-not-restatement. The parenthetical *"(§7.2 — naming its audit-surface home, DMS §7.5)"* reads dense. Both taste, not defects. — `[none]`

### 2.3 No-drift confirmations (positive)

- Keystone executed faithfully — lens folded to §7.2.1; all §7.6 references retargeted (Blocks 2/4/5); no stray §7.6 remains.
- Detection-vs-tagging is a genuine, non-overlapping increment over §7.2 — the conceptual core is sound, not only the wording.
- Block 2 concrete-ID anchoring is self-protecting (the regex literals contain no digits, so the bullet does not self-trip) and correctly scoped; Block 5 contract comment is a clean bare reference, and the "findings *from* the lens" correction is right.
- Reduced-form CSD handling, MINOR versioning (now §7.9-grounded), anchor fidelity, and the carry-forward / queued-capture routing (HEB-36 broaden, HEB-38↔HEB-36 wire, T12 spin) hold and align with the ticket.

---

## 3. Items needing operator ratification (per-item; no bundling)

1. **A2-M1** — trim (a) vs. ratify-the-gloss (b), and the cross-surface consistency rule that follows from it.
2. **A2-M2** — confirm HEB-39 as the §24.1↔§7.4 home, or spin a dedicated ticket.

COSMETIC items (A2-C1/-C2/-C3) need no ratification — take or leave at authoring.

---

## 4. Roll-up note

This pass feeds the HEB-38 Phase-2 review-of-record (the Pass-1→Pass-N convergence artifact), which is authored/vendored separately at close-records. The R043 ruling-rationale entry (the §7.2.1 active-read lens as an extension of R036) and the three-layer HEB-38 Linear capture are downstream close-records actions, each pending its own ratification.

*End of Pass-2 findings handoff.*
