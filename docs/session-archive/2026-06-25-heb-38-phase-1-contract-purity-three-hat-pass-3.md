# File: docs/reviews/2026-06-25-heb-38-phase-1-contract-purity-three-hat-pass-3.md
# Author: Tad Haffey — Executive Architect, Haffey Enterprises LLC
# Created: 2026-06-25
# Description: Three-hat review (Pass 3 / convergence close) of the HEB-38 Phase-1 contract-purity bundle (v3) AND its apply-prompt. Cross-corpus: doctrine judged against R032–R040; apply-prompt judged against ENG-STD-003 v3.0.1. Gate served = Phase-1 doctrine ready to land via the apply-prompt.

# Three-Hat Review (Pass 3 / Convergence Close) — HEB-38 Phase-1 Contract-Purity Doctrine + Apply-Prompt — 2026-06-25

| Field | Value |
|---|---|
| **Review Date** | 2026-06-25 |
| **Reviewer** | claude.ai — LAA / SA / EA seats (claude.ai-assisted authoring under DIRECTIVE-026) |
| **Scope** | Fresh three-hat review of two artifacts: the v3 doctrine bundle (DMS §7.4–§7.9 + §4.6 unification; CSD §7.2; ADR/DDR/SDD/review content-contracts) and the apply-prompt that lands it. Doctrine judged against R032–R039 (frozen) + R040 (this cycle); apply-prompt judged against ENG-STD-003 v3.0.1. |
| **Authority** | DIRECTIVE-007 (Multi-Role Review); DIRECTIVE-032 §32.4 (convergence close); ENG-STD-003 (apply-prompt authoring); HEB-38 Phase-0/Pass-2 ratifications. |
| **Outcome** | **PASS WITH FINDINGS — DOES NOT CONVERGE.** 1 BLOCKING, 3 MATERIAL, 3 COSMETIC; all Pass-2 dispositions verified resolved. Gate not satisfied pending B-1. |

*Finding-axis note: each finding carries the **remedy tag** (add/fix vs remove/relocate) from the DIRECTIVE-007 §7.2 amendment under review — applied here as dogfooding, additive to the canonical finding format. Artifact tags: **[D]** doctrine, **[AP]** apply-prompt.*

---

## §1 Scope

### 1.1 In-scope

- **v3 doctrine bundle** (`heb-38-phase-1-review-target-v3.md`): the §4.6 rewrite (primary Pass-3 target), the §7.4/§7.9 cosmetic touches, R040 draft, the §H tier rationale, and the five cosmetic resolutions — against R032–R039 (read by pointer from the frozen ledger) + R040.
- **Apply-prompt** (`2026-06-25-…-apply-prompt.md`): all phases, str_replace anchors, PreFlight/dry-execute/PostVerify gates, and the commit/PR apparatus — against ENG-STD-003 v3.0.1.

### 1.2 Verification method

Live corpus fresh-fetched: DMS (§4.6, §7.x anchors), CSD (DIRECTIVE-007 §7.2), the four templates, ENG-STD-003 (§5.1 phase shape, §5.2 pre-flight mandate, §6.7–§6.16 dry-execute catalog, §6.10 bash-probe). Every apply-prompt str_replace anchor was grep-verified for presence and uniqueness against the live files. Reference-neutrality of the ADR renumber re-confirmed by grep.

### 1.3 Out of scope (deliberately)

- The **staging file** (`heb-38-phase-1-doctrine-edits.md`) block bodies — not provided this pass; verified by reference (anchors, block labels), not by content. Flagged where this limits a finding's closure.
- **Phase-2 enforcement** (CI gate, skill nudge) and the **Phase-3 cascade** (HEB-12).
- The **close-records PR** (R040 ledger + consolidated review-of-record) — a separate artifact; the apply-prompt correctly defers it.

---

## §2 Findings

### 2.1 BLOCKING findings — must resolve before the apply-prompt lands

#### Finding B-1 [D]: §4.6 contradicts itself on standalone reference-preserving structural change

**Remedy:** add/fix

**Location:** v3 §C — MINOR bullet (line 79) vs the split-trigger parenthetical (line 93); committed by apply-prompt §2.2 (str_replace 2)

**Description:** The unified §4.6 classifies a standalone reference-preserving renumber two ways. The **MINOR bullet** lists *"backward-compatible modification of existing content, including reference-preserving structural reorganization or section renumbering"* → MINOR. The **split-trigger parenthetical** says reference-preserving change — explicitly including *"reference-preserving structural reorganization or renumbering"* — *"rides with the MINOR work or stands alone as PATCH."* So a **standalone** reference-preserving renumber is MINOR by the bullet and PATCH by the parenthetical. (The consolidation case is unambiguous — PATCH-when-standalone, per the PATCH bullet; the contradiction is specific to structural-reorg / renumber.) This is fresh fix-induced drift: the v2→v3 unification corrected the MAJOR-side half-application (B-1/P2-B1) but introduced a PATCH/MINOR-side inconsistency.

**Why blocking:** §4.6 is the primary rewritten surface and a *tier-classification* rule; an internal contradiction about which tier a change-class receives will produce exactly the scope-tier disputes §4.6 exists to adjudicate. The apply-prompt (§2.2) commits this text verbatim, so it cannot land cleanly until reconciled.

**Disposition:** Pick one reading (see §2.5). Recommended: standalone reference-preserving structural change = **MINOR** (drop "or stands alone as PATCH" as it applies to structural-reorg/renumber; keep it for consolidation), so the parenthetical matches the MINOR bullet. Re-verify the staging block after the fix.

### 2.2 MATERIAL findings — in-scope-fix or dispositioned

#### Finding M-1 [AP]: sweep-then-edit does not cover the §2.7 content-contract anchors

**Remedy:** add/fix

**Location:** apply-prompt §1.7 (sweep) vs §2.7 (str_replaces 7…N)

**Description:** §1.7's header mandates sweeping *"every str_replace anchor BEFORE authoring edits"* (per ENG-STD-003 §13.5.8). The sweep covers str_replaces 1–6 (DMS doctrine insert, §4.6 rewrite, DMS version, CSD remedy, CSD version, ADR renumber) but **not** the §2.7 content-contract insertions — the ADR §1–6 / DDR / SDD heading anchors, the three template-header additions, and the four REVIEW-2 edits — which live in the staging file and are never pre-swept. A reworded heading since baseline would surface as a mid-§2.7 str_replace failure after edits 1–6 already mutated three files. (Recoverable — the executor STOPs pre-commit — so not blocking, but it defeats the upfront-catch purpose of sweep-then-edit.) ADR §1–6 anchors were verified unique this pass; DDR/SDD/review/header anchors were not (staging file out of scope).

**Why material:** §13.5.8 conformance gap and a partial-application risk on the largest cluster of edits; the apply-prompt's own §1.7 statement is not met.

**Disposition:** Extend §1.7 to sweep every §2.7 anchor (presence + uniqueness), enumerated from the staging block anchor lists.

#### Finding M-2 [D]: the §C self-classification still grounds in "§4.6's own text," undercutting the ratified M-1/P2-M1 resolution

**Remedy:** add/fix

**Location:** v3 §C self-classification check (line 99) vs §H (line 151) + R2 (lines 20–21)

**Description:** Pass-2's M-1/P2-M1 were resolved by grounding the MINOR call in the **invariant compatibility property** — §H states it classifies MINOR *"on the compatibility principle itself, not by applying its own new text to itself,"* and the bootstrap framing was *"dropped entirely."* But the §C self-classification check still closes with the renumber being *"the MINOR example above, **by §4.6's own text**"* — the exact circular framing the resolution removed. §H is clean; §C carries the residue, so the two read inconsistently.

**Why material:** This is the precision the doctrine itself polices, in the section that sets the (now-eliminated) self-classification precedent; leaving the circular phrasing in §C re-opens what R040 closed.

**Disposition:** Align §C with §H — ground the renumber's MINOR status in the invariant compatibility property (reference-preserving ⇒ backward-compatible ⇒ MINOR), and drop "by §4.6's own text."

#### Finding M-3 [AP]: execution-shell discipline is prose-only; no self-enforcing guard

**Remedy:** add/fix

**Location:** apply-prompt §0.6 (prose) + §1.9 §6.10 probe

**Description:** §0.6 states blocks "are written to be run as `bash <file>` (not zsh)," and §1.9 runs the §6.10 BASH-INTERPRETER-PROBE — but §6.10 is a `bash -n` *parse* check; it does not guarantee blocks are *executed* under bash. The known recurring failure (Claude Code's Bash tool runs under zsh; zsh's 1-indexed arrays break bash idioms under `set -u`) is not self-enforced. The blocks here scan as zsh-safe (no 0-indexed array idioms), so live risk is low — but the discipline rests on the executor honoring §0.6 prose.

**Why material:** A known, repeatedly-hit failure class left to prose rather than a guard; cheap to harden.

**Disposition:** Add the FP-5 guard (`[ -n "${BASH_VERSION:-}" ] || { echo "RED: not bash"; exit 1; }`) at the first block, and/or make the kickoff explicitly instruct per-block `bash <tempfile>` execution.

### 2.3 COSMETIC findings — noted

- **[AP]** §1.9 asserts *"No heredoc payloads,"* but §2.9 and §4.4 use quoted-delimiter heredocs (`<<'COMMIT_EOF'`, `<<'PR_EOF'`). They are literal (quoted), so §6.8 HEREDOC-ESCAPE-GREP is genuinely N/A — but restate the justification as "heredocs are quoted-delimiter ⇒ §6.8 N/A," not "none present." — *remedy: add/fix.*
- **[AP]** The §1.7 CSD sweep anchor (`"Other vocabularies (RED/YELLOW, MUST/SHOULD/MAY) are NOT used"`) differs from str_replace 4's actual `old_str` (the lock-in paragraph ending `"…Mid-project vocabulary drift is a real failure mode prevented by lock-in."`). Both are unique in the live CSD, but the sweep should verify the *actual* edit anchor. — *remedy: add/fix.*
- **[AP]** Per the corpus's explicit-N/A / stable-numbering convention, state N/A explicitly for §5.2 step 6 (pre-vendor header-conformance — N/A, in-place str_replace, no vendoring) and the Phase-3 second-commit role (N/A, single-commit PR). — *remedy: add/fix.*

### 2.4 No-drift confirmations (positive findings)

**Pass-2 dispositions — verified resolved in v3:**

- **B-1/P2-B1 renumber/tier** — §4.6 rewritten to unify on SemVer-compatibility (R040); categorical "renumbering → MAJOR" removed; the ADR renumber is the MINOR example. The v2 half-application is gone. (Resolved — but see B-1 for the *new* PATCH/MINOR inconsistency the rewrite introduced.)
- **M-1 circular framing** — §H now grounds in the invariant compatibility property (clean). (See M-2 for the §C residue.)
- **P2-M1 bootstrap precedent** — framing dropped entirely; no meta-rule codified. Conformant.
- **M-2 frozen-ledger** — recorded as new ruling **R040** cross-referencing R037, explicitly not amending it (§31.7-safe). Conformant.
- **Five cosmetics** — §7.4 doctype-agnostic; §7.9 reduced-form baseline note; ADR "§6 Compliance backlog items"; §S/§H "SA-2"→"SA-1"; §G CSD→DMS row added. All present. Conformant.

**Apply-prompt — independent corpus verifications:**

- **All six named str_replace anchors (1–6) verified unique in the live corpus** — DMS §7.3 close, §4.6 heading (`### 4.6`, line 592) + closing line + `version: 3.1.0`; CSD §7.2 remedy anchor + lock-in close + `version: 3.1.0`; ADR `## 8. Change Log`. Conformant.
- **ADR content-contract anchors (§1–6) verified unique** — no collision with the authoring-guidance comment.
- **ADR renumber str_replace (6) is correctly constructed** — `old_str` = the heading line; `new_str` ends at `## 9. Change Log`, so the existing table re-attaches under the new heading. Reference-neutrality grep-confirmed (nothing cites ADR §8 numerically).
- **§4.6 post-edit verification greps are well-formed** — they assert the exact landed strings (`key on **SemVer-compatibility**`, the §7.4 heading, the remedy axis, ADR §8/§9), and re-assert reduced form (no Change Log gained).
- **Reduced-snapshot handling is correct and live-verified** — both control docs carry only YAML `version:`; no Change Log / `last_updated` / `# Revised:`; the §13.5.8.2 atomic-refresh pairs are documented N/A (not silently skipped); the §4.12 cascade is empty.
- **Explicit-N/A discipline applied well** — §6.8 HEREDOC-ESCAPE and §6.12 SED-DELIMITER correctly N/A'd; §0.5 Canonical-Authority-Fetch N/A'd with reason.
- **Phase structure conforms to §5.1** — single-commit PR, so no Phase 3; §2 (commit) → §4 (push/PR) is the canonical positional shape.
- **Close-records correctly deferred** — R040 ledger + consolidated review-of-record routed to a separate PR (§0.5, §5), per the work-PR ≠ close-PR pattern.

### 2.5 Normative interpretation — standalone reference-preserving structural change: MINOR or PATCH?

The unified §4.6 must answer once whether a *standalone* reference-preserving structural reorganization / renumber (no accompanying addition, no consolidation) is MINOR or PATCH. The MINOR bullet says MINOR; the split-trigger parenthetical says PATCH (§B-1).

- **Option A — MINOR.** Structural reorganization is more than pure cleanup; treat it as a backward-compatible modification. Fix: scope the parenthetical's "stands alone as PATCH" to *consolidation only*.
- **Option B — PATCH.** A structure-only, reference-preserving, semantics-preserving change is a no-op to consumers, like consolidation. Fix: scope the MINOR bullet's structural-reorg/renumber clause to "*riding with an addition*," routing the standalone case to PATCH.

**Recommendation: Option A** — it preserves the v3 intent (the ADR renumber rode with the Cross-References *addition* → MINOR, and the MINOR example already reads that way), and keeps a bright line: consolidation = PATCH; structural reorganization = MINOR. Either way, record the resolution as a refinement under R040 (forward trail), not an R037 edit.

---

## §3 Forward-Pointer Triage

### Candidate HEB-NNN — structural-stability visibility (ratified-residual safeguard)

**Source:** EA lens on the R040 unification

**Description:** R040 (ratified) re-keys structural reorganization/renumbering on reference-breakage. In a by-name-reference corpus this means nearly all reorganization now rides MINOR — the categorical "renumbering is visible/expensive" deterrent is intentionally retired. Not a finding (ratified). Candidate future safeguard: a lint/review-nudge that flags structural reorganization in MINOR PRs for reviewer attention, restoring visibility without forcing MAJOR.

**Proposed disposition:** Optional; file deliberate-first if desired, post-HEB-38.

### Candidate HEB-NNN — wire DIRECTIVE-032 to the §7.2 findings model

**Source:** carried from Pass-2

**Description:** DIRECTIVE-032 inherits the §7.2 severity/remedy vocabulary implicitly (no explicit cross-ref). Pre-existing, out of scope.

**Proposed disposition:** File new, deliberate-first; DIRECTIVE-025 dedup first.

### Forward-pointer triage summary

| Proposed ID | Summary | Disposition |
|---|---|---|
| HEB-NNN | Structural-reorg visibility nudge (R040 residual) | Optional; deliberate-first |
| HEB-NNN | Wire DIRECTIVE-032 → §7.2 findings model | File new, deliberate-first |
| (trail) | Six-class taxonomy "subsumed into §7.7" note (comment `364964f2`) | **Operator-asserted posted; not independently re-verified this pass** — confirm in close-records |

---

## §4 Audit Outcome

> **PASS WITH FINDINGS — DOES NOT CONVERGE.** 1 BLOCKING (B-1: the unified §4.6 contradicts itself on standalone reference-preserving structural change — MINOR by the bullet, PATCH by the split-trigger parenthetical — fresh fix-induced drift from the v2→v3 unification, committed verbatim by apply-prompt §2.2), 3 MATERIAL (M-1 apply-prompt sweep-coverage gap on the §2.7 anchors; M-2 the §C self-classification residue undercutting the ratified bootstrap-elimination; M-3 prose-only execution-shell discipline), 3 COSMETIC. All Pass-2 dispositions are verified resolved; every named apply-prompt anchor is grep-verified unique; reduced-form / empty-cascade handling is correct.
>
> The gate this review serves — **Phase-1 doctrine ready to land via the apply-prompt — is NOT satisfied.** B-1 must be reconciled in the §4.6 text (and re-flowed into the staging block) before the apply-prompt executes; M-1–M-3 fold in alongside. One further disposition + re-review turn is required, narrowly scoped to B-1's §2.5 resolution and the apply-prompt MATERIALs.

*Note on closure limits: the staging-file block bodies were not in scope this pass; B-1 and the anchor confirmations are verified against the v3 bundle text and the live corpus, but final closure depends on the staging blocks matching the ratified v3 surfaces.*

---

## §5 Cross-References

- **Authority:** DIRECTIVE-007 (Multi-Role Review); DIRECTIVE-032 §32.4; ENG-STD-003 v3.0.1 (apply-prompt authoring); HEB-38 Phase-0/Pass-2 ratifications.
- **Conformance baseline:** Notion Phase-0 ledger `389caeea-1325-81f6-bdb5-d30e2a3c4cd0` (R032–R039, frozen, by pointer) + R040 (this cycle, close-records PR).
- **Artifacts reviewed:** `heb-38-phase-1-review-target-v3.md`; `2026-06-25-heb-38-phase-1-contract-purity-apply-prompt.md`. Live corpus fresh-fetched: DMS, CSD, ENG-STD-003, ADR/DDR/SDD/review templates.
- **Related reviews:** Pass-1 (three-hat + antagonistic); Pass-2 (three-hat + antagonistic, non-converging); this Pass-3 convergence close.
- **Ticket:** HEB-38 (In Progress).
- **Disposition tracking:** B-1 + §2.5 resolution → §4.6 text fix + staging re-flow; then re-review. Close-records (R040 + consolidated review-of-record) in a separate PR.
- **Next cadence:** re-review of the B-1 fix + apply-prompt MATERIALs before execution.
