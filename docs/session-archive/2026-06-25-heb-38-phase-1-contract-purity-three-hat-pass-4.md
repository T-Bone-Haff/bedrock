# File: docs/reviews/2026-06-25-heb-38-phase-1-contract-purity-three-hat-pass-4.md
# Author: Tad Haffey — Executive Architect, Haffey Enterprises LLC
# Created: 2026-06-25
# Description: Three-hat review (Pass 4 / convergence re-close) of the HEB-38 Phase-1 contract-purity bundle (v3, post-Pass-3-fix), its apply-prompt, AND the staging file (now in scope). Doctrine judged against R032–R040; apply-prompt against ENG-STD-003 v3.0.1; staging against the ratified v3 surfaces. Gate = Phase-1 doctrine ready to land.

# Three-Hat Review (Pass 4 / Convergence Re-Close) — HEB-38 Phase-1 Contract-Purity Doctrine + Apply-Prompt + Staging — 2026-06-25

| Field | Value |
|---|---|
| **Review Date** | 2026-06-25 |
| **Reviewer** | claude.ai — LAA / SA / EA seats (claude.ai-assisted authoring under DIRECTIVE-026) |
| **Scope** | Fresh three-hat review of three artifacts: the v3 doctrine bundle (post-Pass-3 fixes), the apply-prompt, and — newly in scope — the staging file carrying the committed text. Verifies the Pass-3 dispositions and hunts fix-induced drift. |
| **Authority** | DIRECTIVE-007 (Multi-Role Review); DIRECTIVE-032 §32.4; ENG-STD-003 v3.0.1; HEB-38 Phase-0/Pass-2/Pass-3 ratifications. |
| **Outcome** | **PASS WITH FINDINGS — DOES NOT CONVERGE (narrowly).** 1 BLOCKING, 1 MATERIAL; all four Pass-3 findings + three cosmetics verified resolved. Gate not satisfied pending the two findings — both surgical. |

*Finding-axis note: each finding carries the **remedy tag** (add/fix vs remove/relocate) from the §7.2 amendment under review. Artifact tags: **[D]** doctrine, **[AP]** apply-prompt, **[ST]** staging file.*

---

## §1 Scope

### 1.1 In-scope

- **v3 doctrine** (`heb-38-phase-1-review-target-v3.md`, fixed in place): the §C §4.6 rewrite (B-1 fix), the §C self-classification (M-2 fix) — judged against R032–R039 (frozen, by pointer) + R040 (draft).
- **Apply-prompt** (`2026-06-25-…-apply-prompt.md`): the §1.7 sweep (M-1 fix), §0.6/§1.1 bash discipline (M-3 fix), and the cosmetic resolutions — judged against ENG-STD-003 v3.0.1.
- **Staging file** (`heb-38-phase-1-doctrine-edits.md`) — **now in scope** (closing the Pass-3 limitation): all 9 edit-blocks judged for fidelity to the ratified v3 surfaces.

### 1.2 Verification method

All three artifacts fresh-fetched from `~/Downloads` via Filesystem MCP (not reused from prior turns). Live corpus re-fetched: DMS, CSD, ADR/DDR/SDD/review templates, ENG-STD-003 (§5.1/§5.2 phase shape, §6.10 bash-probe). **Every** str_replace anchor — the six named anchors *and* the newly-swept §2.7 content-contract anchors — grep-verified for presence and uniqueness against the live templates. The apply-prompt's `au()` grep call was executed against the live review-template to confirm finding B-1. **Post-review confirmation:** the live HEB-38 Linear ticket (+ all four comments) and the Notion Phase-0 ledger were subsequently pulled and verified unchanged against the review baseline — R032–R039 frozen and intact (ledger snapshot as-of 2026-06-24T16:22), R040 correctly absent from the frozen ledger (forward-trail per §31.7), ticket In Progress with no scope or disposition change.

### 1.3 Out of scope (deliberately)

- **Close-records folding of the taxonomy disposition** — the EA-3 "subsumed into §7.7" disposition is **verified posted** to the HEB-38 trail (comment `364964f2`); what remains is confirming it folds into the close-records review-of-record (the explicit A–F→§7.4/§7.5/§7.7 mapping).
- **Phase-2 enforcement** and the **Phase-3 cascade** (HEB-12).
- **The close-records PR** (R040 ledger + consolidated review-of-record).

---

## §2 Findings

### 2.1 BLOCKING findings — must resolve before the apply-prompt lands

#### Finding B-1 [AP]: the §1.7 sweep's `au()` grep fails on the leading-dash review anchor — PreFlight cannot clear

**Remedy:** add/fix

**Location:** apply-prompt §1.7 — `au()` helper (line ~186) + the call `au "$RVW" "- *{{finding}} — {{location}}*"` (line ~209)

**Description:** The M-1 fix added the §2.7 anchors to the sweep via `au() { command grep -cF "$2" "$1" | grep -qx 1 ...; }`. One swept anchor — the §2.3 cosmetic bullet format `- *{{finding}} — {{location}}*` — begins with `- `. `grep -cF` without `-e`/`--` reads the leading dash as an option flag. **Verified against the live template:** the call exits **2** with `grep: invalid option -- ' '`; under `set -euo pipefail` the pipeline RED-halts the sweep. The anchor itself exists uniquely (confirmed with `grep -F -e`), so the *only* defect is the grep invocation. Fix-induced drift from the M-1 resolution.

**Why blocking:** §1.7 is in Phase 1; the sweep RED-halts every run, so the apply-prompt can never reach Phase 2 to land the doctrine — the gate this review serves is unsatisfiable as written. (It fails **safe** — the halt precedes any mutation — so no corruption risk, but the apply-prompt cannot complete.)

**Disposition:** One-token fix — `au() { command grep -cF -e "$2" "$1" | grep -qx 1 ...; }` (or `-- "$2"`). This also hardens the helper against any future dash-led anchor. Re-run the §1.7 sweep end-to-end after the fix to confirm clean.

### 2.2 MATERIAL findings — in-scope-fix or dispositioned

#### Finding M-1 [D/AP/ST]: §2.4 positive findings — three surfaces disagree on whether they carry a remedy tag

**Remedy:** add/fix

**Location:** CSD-7.2-REMEDY staging block (line 109, "Every finding additionally carries a remedy tag") vs v3 §E (line 111, "trailing tag on §2.3/§2.4 bullets") vs staging REVIEW-2 EDIT C + apply-prompt §2.7 (§2.3 COSMETIC only; "positive §2.4 findings … carry no remedy tag")

**Description:** Reading the staging file (newly in scope) surfaced a three-way inconsistency on whether a §2.4 no-drift/positive finding carries a remedy tag. The CSD remedy block (committed) says *every* finding does; v3 §E (ratified bundle description) says the trailing tag lands on §2.3 **and** §2.4 bullets; but the staging EDIT C and apply-prompt §2.7 (the text that actually lands) apply it to §2.3 COSMETIC **only**, explicitly exempting positives. Two of these surfaces (CSD remedy block, review template) both land in this PR, so the committed corpus would carry the contradiction.

**Why material:** A landed-text contradiction on a normative template surface, in the doctrine that polices exactly this kind of precision. It's an edge (positives only) and the surfaces are each internally sensible, so not blocking — but it should not land unreconciled.

**Disposition:** Reconcile to one position. **Recommended:** positives carry **no** remedy tag (a no-drift confirmation asks for nothing — the CSD block's own qualifier "naming what the finding asks for" already leans this way). That makes the staging EDIT C correct; align v3 §E to "§2.3" and tighten the CSD lead from "Every finding" to "Every actionable finding (BLOCKING / MATERIAL / COSMETIC)." If instead positives *should* be tagged, the staging EDIT C and §2.7 must add the §2.4 edit. Ratify the direction.

### 2.3 COSMETIC findings — noted

None new this pass.

### 2.4 No-drift confirmations (positive findings)

**Pass-3 dispositions — verified resolved:**

- **B-1 (§4.6 PATCH/MINOR contradiction) [D]** — RESOLVED, exactly per the recommended Option A. The split-trigger parenthetical now reads: consolidation "rides with the MINOR work or stands alone as PATCH; reference-preserving structural reorganization or renumbering **is MINOR, whether standalone or riding**." It agrees with the MINOR bullet; the contradiction is gone. **The fix is present in the staging DMS-4.6 block** (committed text), not just the bundle.
- **M-1 (apply-prompt sweep-coverage) [AP]** — RESOLVED: §1.7 now sweeps every §2.7 anchor (template headers, ADR/DDR/SDD headings, review anchors) via the `au()` helper. **All swept anchors verified unique in the live templates this pass.** (Resolution introduced finding B-1 above.)
- **M-2 (§C self-classification residue) [D]** — RESOLVED: the circular "by §4.6's own text" is gone; §C now grounds the renumber's MINOR status "on that same invariant property, **not by applying §4.6's new text to itself**," aligning with §H.
- **M-3 (execution-shell discipline) [AP]** — RESOLVED: §1.1 carries the FP-5 `BASH_VERSION` guard as its first line; §0.6 adds the explicit "write each block to a tempfile, run `bash <tempfile>`, do not paste into zsh" instruction.
- **Cosmetics** — §1.9 heredoc claim corrected (quoted-delimiter ⇒ §6.8 N/A); the §1.7 CSD sweep anchor now matches the actual str_replace-4 old_str; §1.6 pre-vendor header-conformance N/A and the Phase-3 second-commit N/A both stated explicitly. All present.

**Staging-file fidelity (closing the Pass-3 limitation) — verified:**

- **DMS-4.6 block** matches the fixed v3 §C and correctly **excludes** the "Self-classification (Pass-3 check)" commentary — only doctrine text is staged; block span (`### 4.6 …` → "… before merge, not after.") matches the live replacement span.
- **DMS-7.4-7.9 block** carries all six subsections and both §7.4/§7.9 cosmetics (doctype-agnostic relocation pointer; reduced-form baseline note).
- **DDR content-contracts** cover exactly the five normative sections and **exclude** `## Layer-of-abstraction note` / `## Substrate-stability tracking` (the prior coverage-gap fix holds).
- **ADR-8-CROSS-REFERENCES block** is well-formed (ends at `## 9. Change Log` so the existing table re-attaches; the "§6 Compliance backlog items" cosmetic applied); **CSD-7.2-REMEDY** and **TEMPLATE-HEADER-ADDITION** match the ratified surfaces.

**Independent corpus verifications:**

- All six named str_replace anchors (1–6) and all newly-swept §2.7 anchors are **unique** in the live corpus.
- The grep-bug (B-1) fails **safe** — Phase-1 halt, no mutation.
- §2.8 post-edit verification block is well-formed (asserts version bumps, landed doctrine strings, ADR §8/§9, reduced-form preservation).

### 2.5 Normative interpretation — do §2.4 positive findings carry a remedy tag?

The remedy axis (CSD §7.2) says "every finding" carries a remedy tag, but a §2.4 finding is a no-drift confirmation that asks for nothing. The committed review template (staging EDIT C) exempts positives; v3 §E and the CSD lead read as including them. This needs one ratified answer (see M-1). **Recommended:** positives are exempt — they are confirmations, not requests — so the remedy tag is an *actionable-finding* attribute. Records as an R040-adjacent clarification on the forward trail.

---

## §3 Forward-Pointer Triage

| Proposed ID | Summary | Source | Disposition |
|---|---|---|---|
| HEB-NNN | Wire DIRECTIVE-032 → §7.2 findings model | Pass-2 carry | File new, deliberate-first; DIRECTIVE-025 dedup first |
| HEB-NNN | Structural-reorg visibility nudge (R040 residual) | Pass-3 EA | Optional; deliberate-first |
| (trail) | Taxonomy "subsumed into §7.7" comment `364964f2` | Pass-3 EA-3 | **Verified posted** (`364964f2`) — confirm it folds into the close-records review-of-record |

---

## §4 Audit Outcome

> **PASS WITH FINDINGS — DOES NOT CONVERGE (narrowly).** All four Pass-3 findings (B-1 §4.6 contradiction, M-1 sweep-coverage, M-2 self-classification residue, M-3 bash discipline) and all three cosmetics are verified resolved — and the staging file is verified faithful to the ratified v3 surfaces across all nine blocks. **The doctrine has converged: §4.6 is internally consistent and the committed §4.6 text carries the fix.**
>
> Two findings remain, both surgical: **B-1 [AP]** — a one-token grep bug (`au()` needs `-e`) that RED-halts the §1.7 sweep (fail-safe, but the apply-prompt can't execute as written); and **M-1 [D/AP/ST]** — a three-surface inconsistency on whether §2.4 positives carry a remedy tag, which would land as a corpus contradiction.
>
> The gate — **Phase-1 doctrine ready to land — is NOT satisfied**, but the remaining distance is small: fix the grep call, ratify the positive-finding remedy scope and align the three surfaces, then a final confirm-pass on the §1.7 sweep. No doctrine re-authoring is required.

---

## §5 Cross-References

- **Authority:** DIRECTIVE-007; DIRECTIVE-032 §32.4; ENG-STD-003 v3.0.1; HEB-38 Phase-0/Pass-2/Pass-3 ratifications.
- **Conformance baseline:** Notion Phase-0 ledger `389caeea-1325-81f6-bdb5-d30e2a3c4cd0` (R032–R039, frozen, by pointer) + R040 (this cycle, close-records PR).
- **Artifacts reviewed:** `heb-38-phase-1-review-target-v3.md`, `2026-06-25-…-apply-prompt.md`, `heb-38-phase-1-doctrine-edits.md` (staging). Live corpus fresh-fetched: DMS, CSD, ENG-STD-003, ADR/DDR/SDD/review templates.
- **Related reviews:** Pass-1, Pass-2, Pass-3 (three-hat + antagonistic); this Pass-4 convergence re-close.
- **Ticket:** HEB-38 (In Progress).
- **Disposition tracking:** B-1 (grep `-e` fix) + M-1 (positive-finding scope reconcile) → apply-prompt + staging + v3 §E edits; then a §1.7 confirm-pass. Close-records (R040 + consolidated review-of-record) in a separate PR.
- **Next cadence:** confirm-pass on the two fixes before execution.
