# File: docs/reviews/2026-06-26-heb-38-phase-2-enforcement-pass-3.md
# Author: Claude (architecture-team three-hat simulation — LAA/SA/EA) — claude.ai review session under DIRECTIVE-026
# Created: 2026-06-26
# Description: Three-hat review (Pass-3) of the HEB-38 Phase-2 converged edits + the Phase-2 apply-prompt, including an executed §11.7.4 sandbox runtime dry-run of the apply-prompt's bash blocks. Consolidates all Pass-3 findings (static + dry-run). Findings hand-off to the authoring session per DIRECTIVE-032 §32.3.

# Three-Hat Review — HEB-38 Phase-2 (edits + apply-prompt), Pass-3 + sandbox dry-run

| Field | Value |
|---|---|
| **Review Date** | 2026-06-26 |
| **Reviewer** | Claude — architecture-team three-hat simulation (LAA / SA / EA), claude.ai review session under DIRECTIVE-026 |
| **Artifacts under review** | (1) `heb-38-phase-2-enforcement-edits.md` (CONVERGED cut); (2) `2026-06-25-heb-38-phase-2-enforcement-apply-prompt.md` (new this pass) |
| **Baseline** | HE-Bedrock `main` @ `28a496a` (CSD 3.2.0 · DMS 3.2.0 · kit 2.4.0) |
| **Scope** | Pass-3: confirm the edits file folds the Pass-2 findings (brief); review the apply-prompt against ENG-STD-003 + the apply-prompt template; **execute a §11.7.4 sandbox runtime dry-run** of the apply-prompt's bash blocks (P3-M1 from the Pass-3 static read). |
| **Authority** | ENG-STD-001 §12.6 (three-hat); ENG-STD-003 (apply-prompt authoring; §6.x guards, §11.7.4 runtime pass, §13.5.2/§13.5.8); the apply-prompt template; HEB-38 Roadmap-correction comment (2026-06-26). |
| **Ticket confirmation** | HEB-38 description + 6-comment trail unchanged since Pass-2 (`hasNextPage:false`); Roadmap-correction remains authoritative. P2-1/P2-2/P2-3 dispositions are reflected in the edits file, queued for Phase-5b ticket capture (not yet on the trail). |
| **Outcome** | **PAUSE — one BLOCKING finding (B-1, dry-run).** The apply-prompt as written fails at Phase 1.7 on every run (false-RED). One-line fix clears it. Plus 3 MATERIAL, 3 COSMETIC. The edits file is clean. |

---

## §0 Method note — the runtime dry-run

Pass-3's static read (proceed-with-changes on all hats) flagged that the apply-prompt's own bash blocks are a distinct runtime surface (P3-M1). This pass **executed** the §11.7.4 sandbox runtime pass to settle that: a mock HE-Bedrock was built from the live corpus (CSD / PROVENANCE / review-template at the `28a496a` pre-amend state; a `VERSION` file seeded at `2.4.0`), and each apply-prompt block was run the operator's way — written to a tempfile and invoked via `bash <file>`, per the FP-5 executor-shell discipline. The FP-5 probe was additionally exercised under a non-bash shell (`dash`) as a zsh proxy (zsh is not installed in the sandbox). The 8 edits were applied with per-anchor uniqueness asserts, then the post-edit gate (§2.2) and the idempotency guard were run against the mutated mock. Every `bash` block was `bash -n` syntax-checked. This is the empirical basis for §2.1–§2.4 below; the static read alone did **not** surface B-1.

---

## §1 Scope

### 1.1 In-scope
- The converged edits file (Pass-2 fold-confirm).
- The apply-prompt: structure vs. template; §6.x guard attributions; §13.5.2 step-5 tactical fetch; §13.5.8 surface manifest + PostVerify disposition; release/commit/PR/post-merge phases; **runtime behavior of all bash blocks**.

### 1.2 Out of scope
- `gh`-dependent blocks (§1.6 label, §4.4 PR-create, §4.5 base-verify) — not executable in-sandbox (no `gh`/network); `bash -n` syntax-checked instead.
- The running grep mechanization (Phase-2.5 / HEB-36); cascade (Phase-3); skill nudge (Phase-4).

---

## §2 Findings

Axes per DIRECTIVE-007 §7.2: **severity** (§2.1–§2.4) × **remedy** (add/fix · remove/relocate · none-default). Each finding tags the **hat** and whether it is **[dry-run]** or **[static]**.

### 2.1 BLOCKING findings

#### Finding B-1: leading-dash anchor halts the Phase 1.7 sweep with a false-RED  ·  [dry-run]
**Hat:** SA · **Remedy:** add/fix · **Location:** apply-prompt §1.7, line 202 (the Block 2 DIRECTIVE-023 OLD-anchor check)

**Description.** The check is:
```
command grep -qF '- Frontmatter schema conformance for typed documents (ADR, DDR, SDD, session-handoffs)' "$FILE" \
    || { echo "RED: ${FILE} — Block 2 DIRECTIVE-023 OLD anchor absent" >&2; exit 1; }
```
The pattern begins with `- ` (a markdown bullet), so `grep` parses the leading `-` as an option and errors: `grep: invalid option -- ' '`. The check therefore takes its `||` branch and emits **`RED: … Block 2 DIRECTIVE-023 OLD anchor absent`** even though the anchor **is present**, and `exit 1` halts the sweep. Because the anchor invariantly starts with `-`, this fires on **every** run — the apply-prompt cannot proceed past Phase 1.7. Worse, the message misdirects: an operator reads "anchor absent" as "`main` moved," when nothing moved.

**Reproduced & fixed in-sandbox.** Unfixed: `grep` exits 2 (option error) → false-RED → sweep `exit 1`. Fix: insert the end-of-options marker —
```
command grep -qF -- '- Frontmatter schema conformance for typed documents (ADR, DDR, SDD, session-handoffs)' "$FILE" \
```
— exits 0 (found); with the fix the full §1.7 sweep passes all 10 checks clean. (`-e` also works; `--` is preferred per the leading-dash-anchor lesson.) This is the only leading-dash pattern in the file — a whole-file scan confirms no others.

**Why blocking.** The apply-prompt is non-functional as written: it stops at the pre-flight sweep on first execution, before any mutation. Trivial to fix, but it must be fixed before the apply-prompt runs, and a Pass-4 confirm should re-run the §1.7 sweep post-fix.

**Disposition.** Apply the `--` fix at line 202. (Audit the §1.7/§2.2 grep set generally for any future bullet-anchored patterns; this is the recurring `grep -e`/`au` leading-dash class.)

### 2.2 MATERIAL findings

#### Finding M-1: §4.5 re-instances the gh-PR-phase fragility HEB-35 hardens  ·  [static]
**Hat:** SA · **Remedy:** add/fix · **Location:** apply-prompt §4.5, line 427

**Description.** The PR number is captured via a bare `PR_NUM="$(gh pr view --json number -q .number)"` (current-branch resolution) immediately after `gh pr create`. That is precisely the fragility the HEB-35 "gh PR-phase fix" exists to close. Capture from `gh pr create`'s own output instead — `PR_URL="$(gh pr create …)"; PR_NUM="${PR_URL##*/}"` — then use `$PR_NUM` throughout (§4.5 already does so for the subsequent `baseRefName` calls). Not runtime-testable in-sandbox (no `gh`); the block is `bash -n`-clean.

**Disposition.** Adopt the create-output capture per HEB-35.

#### Finding M-2: §13.5.8 surface-type mislabels — an HEB-25 taxonomy-drift re-instance  ·  [static]
**Hat:** SA · **Remedy:** add/fix (or route) · **Location:** apply-prompt §0.4.2 (File 1 row; File 3 row)

**Description.** Two manifest rows don't map to the §13.5.8 taxonomy: the CSD YAML `version:` is tagged `body-bold-version (YAML scalar)` (neither body-bold nor a clean taxonomy type), and the `VERSION` scalar is tagged `terminator` (which denotes the end-of-doc footer marker — a distinct, never-mutated surface). The taxonomy lacks clean `yaml-version` / `bare-version-file` types — this is the known **HEB-25** drift. The Phase 1.7 sweep and pre/post values are correct, so there is **no functional consequence this cycle**; the weight is conformance + the HEB-25 re-instance.

**Disposition.** Correct the two labels to the nearest defensible type with a note, or route the taxonomy gap to HEB-25 (and label these rows provisionally).

#### Finding M-3: §11.7.4 runtime-pass scope — the PR-body claim under-scopes  ·  [static; substantiated by the dry-run]
**Hat:** EA · **Remedy:** add/fix · **Location:** apply-prompt §4.4 PR body ("Verification" paragraph)

**Description.** The PR body asserts "Static-axis convergence; no runtime pass needed (no executable content — grep impl rides HEB-36)." That holds for the **shipped deliverable** (doc text), but conflates it with the apply-prompt's **own bash blocks**, which are executable machinery the operator runs — exactly the §11.7.4 / FP-5 surface. This pass's dry-run proves the point: the blocks **did** need a runtime pass (it caught B-1). The "do the dry-run" half of this finding is now **satisfied** (performed here); the residual is to **re-scope the claim** to "no runtime pass for the committed content," and to record that the apply-prompt blocks passed the §11.7.4 sandbox pass **after the B-1 fix**.

**Disposition.** Re-word the PR-body verification line; cite the completed §11.7.4 sandbox pass (post-B-1-fix) as the runtime evidence.

### 2.3 COSMETIC findings

- **C-1 (SA, static)** — apply-prompt §2.1 Edit 3 uses `old_str` `version: 3.2.0` (doctype noted parenthetically) rather than the staging file's 2-line `doctype:`+`version:` anchor. Safe (str_replace fails loudly on non-unique; the dry-run confirmed the 2-line form is unique), but less specific than the staging anchor. Prefer parity with staging. · add/fix.
- **C-2 (SA, static)** — §1.6 is repurposed from the template's "header conformance" slot to LABEL-EXISTENCE; the staging-header conformance check is folded into §1.5. Benign adaptation; note for traceability. · none.
- **C-3 (SA, static)** — the BASH-INTERPRETER-PROBE is referenced only by its §1.1 location; cite its §6.10 catalog number for guard traceability. · add/fix.

### 2.4 No-drift confirmations (positive findings)

- **P-1 (edits file, static)** — Converged: all Pass-2 findings folded — **P2-1** §24.1 seam re-routed to a dedicated §7-jurisdiction / DIRECTIVE-024-refinement ticket (explicitly not HEB-39, correctly reasoned); **P2-2** lone-child §7.2.1 affirmed; **P2-3** HEB-36 broaden sequenced into close. The 2nd antagonistic round trimmed the Block 4 gloss to a bare reference and stripped the §7.2.1 self-claim. The §7.2.1 NEW text is byte-identical between the staging file and the apply-prompt's Edit 1 (self-claim-strip included).
- **P-2 (dry-run)** — FP-5 probe verified: passes under `bash` (`✓ bash interpreter confirmed`); correctly REDs under a non-bash shell (`dash`, zsh-proxy: `RED … probe correctly fired`, exit 1). The tripwire works.
- **P-3 (dry-run)** — §1.7 `set -euo pipefail` interactions are clean: the `grep -c` uniqueness check and the `! command grep -qE … || {…}` absence check both behaved correctly (no spurious `set -e` abort). These were the subtle runtime risks; they're sound.
- **P-4 (dry-run)** — All 8 edits apply with **unique** anchors (every simulated str_replace matched exactly once); the §2.2 post-edit gate passes clean against the mutated mock; the §7.2.1 idempotency/absence guard correctly REDs on a re-run (no double-insert).
- **P-5 (dry-run)** — All **14** bash blocks pass `bash -n`; a whole-file scan finds **only one** leading-dash grep pattern (B-1) — no others hiding in the gates.
- **P-6 (apply-prompt, static)** — Template-conformant structure (cold-read → carry-forward → surface manifest → invocation → pre-flight → single commit → push/PR → Phase-5b → cross-refs); Phase 1.7 correctly serves as the §13.5.2 step-5 tactical fetch (all OLD anchors swept, Block 1 uniqueness + §7.2.1 absence checked); §13.5.8 PostVerify **N/A** soundly reasoned (reduced-form CSD + flat PROVENANCE + bare VERSION + content-only template carry no atomic-refresh pairs), with cross-surface consistency (kit / CSD-pin / date) still enforced by the §2.2 gate; HEB-40 release-step ride in Commit 1; close-records (R043 + review-of-record + Notion mirror + three-layer Linear capture) correctly deferred to Phase-5b / the separate close PR; quoted-heredoc + `-F`/`--body-file` message patterns correct.
- **P-7 (apply-prompt, static)** — Correctly **not** held to DMS §7 contract-purity: apply-prompts are §7-out per R032 scope (→ HEB-39 jurisdiction), so the apply-prompt's free use of R-IDs / tracker-IDs is conformant, not a dogfooding violation.

---

## §3 Forward-Pointer Triage

| ID | Summary | Source | Proposed disposition |
|---|---|---|---|
| FP-1 | §24.1↔§7.4 seam | edits scope ledger | New dedicated §7-jurisdiction / DIRECTIVE-024-refinement ticket (DIRECTIVE-025 dedup); **not** HEB-39 |
| FP-2 | HEB-36 broaden (deliberation→execution; add grep-impl) | edits scope ledger / P2-3 | Land at Phase-2 close so the descriptive reference resolves |
| FP-3 | T12 — DIRECTIVE-032 → §7.2 back-pointer + §7.2.1 antagonistic-review inheritance | edits scope ledger | Own ticket |
| (M-1) | gh-PR-phase capture fragility | M-1 | Fix in-place; the worked-example hardening tracks at HEB-35 |
| (M-2) | §13.5.8 surface-type taxonomy gap (`yaml-version` / `bare-version-file`) | M-2 | Route to HEB-25 |

---

## §4 Audit Outcome

> **PAUSE.** One BLOCKING finding (**B-1**, dry-run-proven): the apply-prompt halts at Phase 1.7 on every run via a leading-dash false-RED. Three-hat verdict aggregation per ENG-STD-001 §12.6:
> - **LAA → proceed** (scope clean; single commit; phase decomposition matches the Roadmap-correction comment)
> - **SA → pause** (B-1 blocking; M-1 + M-2 + C-1/C-2/C-3 are proceed-with-changes once B-1 clears)
> - **EA → proceed-with-changes** (M-3 claim-scoping)
>
> The edits file is converged and clean. The apply-prompt is otherwise well-built and template-conformant — the dry-run cleared the FP-5 probe, the `set -e`/grep interactions, anchor uniqueness, the post-edit gate, and the idempotency guard. **B-1 is a one-line fix (`grep -qF --`)**; once applied, a Pass-4 confirm re-runs the §1.7 sweep (expected clean — already verified in-sandbox post-fix), after which all hats reach proceed / proceed-with-changes. This is the §11.7.4 lesson in the concrete: static convergence (Pass-3) rated everything proceed-with-changes; the runtime pass found the blocker.

---

## §5 Cross-References

- **Authority:** ENG-STD-001 §12.6 (three-hat); ENG-STD-003 (§6.x guards, §11.7.4 runtime pass, §13.5.2 tactical fetch, §13.5.8 surface manifest); the apply-prompt template; HEB-38 Roadmap-correction comment (2026-06-26).
- **Artifacts reviewed:** the converged edits file; the Phase-2 apply-prompt.
- **Prior passes:** `2026-06-25-heb-38-phase-2-enforcement-pass-1.md`; `…-pass-2.md` (this Pass-3 re-anchored against current content per §11.7.7 and adds the executed §11.7.4 runtime pass).
- **Corpus re-verified (@ `28a496a`):** CSD DIRECTIVE-007 §7.2 / -023 / -024 §24.1 + frontmatter; DMS §7.4–§7.9; `review-template.md` §2; `PROVENANCE.md`. `VERSION` (`2.4.0`) seeded in-sandbox (not in project knowledge; owed to the apply-prompt's §13.5.2 live fetch).
- **Rulings:** Phase-0 R032–R039 (Notion `389caeea`); Phase-1 R040–R042 (Notion `38acaeea` + repo mirror). Phase-2 mints **R043** (the §7.2.1 lens as an R036 extension; captured at close-records).
- **Tracker:** HEB-38 (Phase-2; Roadmap-correction 2026-06-26). Related: HEB-36 (grep-impl owner; broaden queued), HEB-35 (gh-PR-phase + guard hardening — M-1), HEB-25 (surface-type taxonomy drift — M-2), HEB-40 (release-step), HEB-41 (ruling-ID), HEB-24 (main-only rebind), HEB-39 (ENG-STD analogue — explicitly *not* the §24.1-seam home).
- **Findings disposition:** returns to the authoring session per DIRECTIVE-032 §32.3; ratification items per §6.
- **Next pass:** Pass-4 confirm after the B-1 fix — re-run the §1.7 sweep (verified clean in-sandbox post-fix); then the package + review-of-record vendor.

---

## §6 Open ratifications (per-item — nothing locked)

1. **B-1** — Apply the `grep -qF --` fix at §1.7 line 202 (and confirm the audit found no sibling leading-dash anchors — it didn't).
2. **M-1** — Adopt the `gh pr create`-output PR-number capture per HEB-35.
3. **M-2** — Correct the two §13.5.8 surface-type labels, or route the taxonomy gap to HEB-25.
4. **M-3** — Re-scope the PR-body "no runtime pass needed" claim; cite the completed (post-fix) §11.7.4 sandbox pass.
5. **C-1 / C-3** — Edit 3 two-line anchor parity; §6.10 catalog cite for the probe (both optional).

*End of Pass-3 three-hat review (+ sandbox dry-run) — HEB-38 Phase-2 enforcement edits + apply-prompt.*
