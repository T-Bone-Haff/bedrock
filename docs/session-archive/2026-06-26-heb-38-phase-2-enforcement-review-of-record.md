# File: docs/reviews/2026-06-26-heb-38-phase-2-enforcement-review-of-record.md
# Author: Claude (claude.ai review session under DIRECTIVE-026) — consolidating the three-hat stream (DIRECTIVE-007 §12.6) and the antagonistic stream (DIRECTIVE-032)
# Created: 2026-06-26
# Description: Durable review-of-record for HEB-38 Phase-2 enforcement (the contract-purity delivery surfaces). Consolidates the full Pass-1→convergence trail across two review streams plus the §11.7.4 sandbox runtime dry-run, over both work artifacts (the converged staging edits + the Phase-2 apply-prompt). Vendored at close-records per the close-records pattern.

# HEB-38 Phase-2 Enforcement — Review-of-Record (Pass-1 → Convergence)

| Field | Value |
|---|---|
| **Review window** | 2026-06-25 → 2026-06-26 |
| **Author of record** | Claude — claude.ai review session under DIRECTIVE-026 |
| **Streams consolidated** | (1) **Three-hat** (DIRECTIVE-007 §12.6 / ENG-STD-001 §12.6) — Pass-1, Pass-2, Pass-3 + sandbox dry-run, Pass-4. (2) **Antagonistic** (DIRECTIVE-032) — Pass-1 (pre-apply-prompt gate) + Pass-2 (converged-cut handoff). |
| **Artifacts reviewed** | `heb-38-phase-2-enforcement-edits.md` (the converged staging cut, Blocks 1–8); `2026-06-25-heb-38-phase-2-enforcement-apply-prompt.md` (the Phase-2 work apply-prompt). |
| **Corpus baseline** | HE-Bedrock `main` @ `28a496a` (kit 2.4.0 · CSD 3.2.0 · DMS 3.2.0) — unchanged across the window; no Phase-2 PR merged. |
| **Authority** | ENG-STD-001 §12.6 (three-hat); DIRECTIVE-032 (antagonistic); ENG-STD-003 (apply-prompt authoring; §6.x guards, §11.7.4 runtime pass, §13.5.2/§13.5.8); DMS §7.4–§7.9 (the doctrine enforced); HEB-38 Roadmap-correction comment (2026-06-26, authoritative phase decomposition). |
| **Outcome** | **CONVERGED — 0 BLOCKING / 0 MATERIAL on both the static and runtime axes.** Both antagonistic blockers (A-B1, A-B2) and the dry-run blocker (P3-B1) are cleared; all MATERIAL findings across both streams are resolved or routed; residual is one COSMETIC documentation-currency note. The work artifacts are clear to execute. |

---

## §0 Purpose & method

This is the durable Pass-1→Pass-N convergence record for HEB-38 Phase-2's **work artifacts**, vendored at close-records per the close-records pattern (distinct from the work PR). It consolidates two independent review streams that ran in parallel against the same artifacts and fed the same converged cuts:

- the **three-hat** stream (LAA "what is this change" / SA "how does it conform" / EA "should it land in this shape now"), and
- the **antagonistic** stream (DIRECTIVE-032 adversarial read).

It also incorporates an executed **§11.7.4 sandbox runtime dry-run** of the apply-prompt's bash blocks (§4), which surfaced a blocker that neither stream's static read caught.

**Finding-ID namespacing (HEB-41 discipline).** The antagonistic Pass-1 and the three-hat Pass-3 dry-run both independently minted a finding numbered "B-1." To avoid a cross-venue ID collision — the exact failure mode HEB-41's single-registry fix targets — every finding here is namespaced by its originating stream/pass: `P{n}-…` for three-hat passes, `A`/`A2-…` for the antagonistic passes. The two blockers are therefore **A-B1** (antagonistic scope-drift) and **P3-B1** (dry-run leading-dash), held distinct throughout.

---

## §1 Scope

**In-scope:** correctness, contract-purity, versioning, citation accuracy, and scope-fidelity of the converged staging edits (Blocks 1–8); structural + ENG-STD-003 conformance and **runtime behavior** of the apply-prompt; completeness against the ratified Phase-2 plan and the Roadmap-correction decomposition.

**Out of scope (by phase boundary):** the running grep mechanization (Phase-2.5 / HEB-36); the SOFIA-Reboot cascade (Phase-3); the skill-nudge surface (Phase-4); the Phase-1 landed doctrine itself (reviewed only where Phase-2 interacts with it).

**Substrate fresh-fetched (no recall):** corpus @ `28a496a` (DMS §4.6/§7.x; CSD DIRECTIVE-007 §7.1–§7.5.3, DIRECTIVE-023, DIRECTIVE-024 §24.1, frontmatter; ENG-STD-003 §13.5.x; review-template §2; PROVENANCE; Phase-1 R040–R042 rulings); live HEB-38 ticket + full comment trail (incl. the 2026-06-26 Roadmap-correction); Notion Phase-0 (R032–R039, `389caeea…`) and Phase-1 (R040–R042, `38acaeea…`, max R042) ruling SoRs.

---

## §2 Convergence trail

Phase-2's work artifacts converged across three cuts and a runtime pass:

1. **Pre-converged staging.** The first staging file homed the review lens at a standalone `#### 7.6`. Reviewed by **three-hat Pass-1** (8 MATERIAL P1-M1…M8 + P1-C1) and **antagonistic Pass-1** (FAIL — 2 BLOCKING A-B1/A-B2, 4 MATERIAL A-M1…M4, 3 COSMETIC). The streams overlapped on the restatement defect (P1-M2 ≈ A-B2) and the §24.1 seam (P1-M6 ≈ A-M3), and were complementary elsewhere (A-B1 scope-drift, A-M4 versioning — see §5).

2. **Converged cut #1 (keystone).** The lens folded from standalone `#### 7.6` to `##### 7.2.1` under §7.2, co-located with the remedy axis it extends. This single move cleared P1-M1/M2/M8 + A-B2/A-M1/A-C1 at once. Block 2 gained concrete-ID-anchoring (P1-M3/A-M2); the versioning rationale was re-grounded on DMS §7.9 grandfather-until-touched (A-M4); the §24.1 seam and phase decomposition were dispositioned. Reviewed by **three-hat Pass-2** (P2-1/2/3) and **antagonistic Pass-2** (PASS WITH FINDINGS — A2-M1 Block 4 gloss, A2-M2 §24.1 routing).

3. **Converged cut #2.** Folded Pass-2 + antagonistic-Pass-2: Block 4 trimmed to a bare reference (A2-M1, trim-(a)); the §24.1 seam re-routed from HEB-39 to a **dedicated §7-jurisdiction / DIRECTIVE-024-refinement ticket** (P2-1 / A2-M2); the §7.2.1 self-claim stripped (A2-C3); line-13 framing tightened to the "active-read leg" (A2-C1); HEB-36 broaden sequenced into close (P2-3). Plus the Phase-2 **apply-prompt** authored against this cut.

4. **Three-hat Pass-3 + sandbox dry-run.** Static read of the apply-prompt (P3-M1/M2/M3 + cosmetics) plus an executed §11.7.4 runtime pass that surfaced **P3-B1** (a leading-dash false-RED hard-stop) — a blocker no static read caught. Verdict: PAUSE.

5. **Fix + three-hat Pass-4 (convergence).** P3-B1 fixed (`grep -qF --`) and the fix runtime-verified; P3-M1/M2/M3 + C-1/C-3 resolved. Re-run sandbox: §1.7 sweep clean, all 8 edits apply, §2.2 verify passes, idempotency guard fires, 13/13 blocks `bash -n` clean, 0 unprotected leading-dash patterns. **CONVERGED.**

---

## §3 Consolidated findings ledger

Severity × remedy per DIRECTIVE-007 §7.2. **Final status** is the state in the converged artifacts after the full trail.

### 3.1 Three-hat stream

| ID | Sev | Finding | Final status |
|---|---|---|---|
| **P3-B1** | BLOCKING | Apply-prompt §1.7 Block 2 anchor `'- Frontmatter…'` begins with `-` → `grep: invalid option` → false "anchor absent" RED, halting Phase 1.7 on every run (dry-run). | **RESOLVED** — `grep -qF --` at §1.7:202; runtime-verified clean (§4). |
| P1-M1 | MATERIAL | §7.6 lens is a codification-breadth decision beyond frozen R036; standalone-vs-fold form unresolved. | **RESOLVED** — folded to §7.2.1 (R036-extension; R043 reserved). |
| P1-M2 | MATERIAL | §7.6 restates the §7.7 stranger-build test (R035 "reference, never restate"). | **RESOLVED** — §7.2.1 references, does not restate (≡ A-B2). |
| P1-M3 | MATERIAL | DIRECTIVE-023 reproduces §7.4's open identifier list. | **RESOLVED** — closed-subset note + concrete-ID-anchoring (≡ A-M2). |
| P1-M4 | MATERIAL | Phase-attribution seam — lens was Phase-1 target #2, landing in Phase-2, undeclared. | **RESOLVED** — Roadmap-correction; AC2 "partially landed." |
| P1-M5 | MATERIAL | HEB-36 dependency misattribution (doc-structure validator ≠ contract-purity grep). | **RESOLVED** — HEB-36 broaden owned + sequenced into close; relation wired. |
| P1-M6 | MATERIAL | §24.1↔§7.4 doctrine seam. | **ROUTED** — dedicated ticket (≡ A-M3 / A2-M2). |
| P1-M7 | MATERIAL | Phase-2 rulings not enumerated. | **RESOLVED** — R043 (lens) sole Phase-2 ruling, attributed. |
| P1-M8 | MATERIAL | §7.6 cross-review-type binding. | **RESOLVED** — §7.2.1 inherits §7.2 binding; DIRECTIVE-032 inheritance → T12. |
| P1-C1 | COSMETIC | §2 contract comment "holds the lens" imprecise. | **RESOLVED** — "findings *from* the lens." |
| P2-1 | MATERIAL | §24.1 seam routed to HEB-39 — venue mismatch. | **RESOLVED** — re-routed to dedicated §7-jurisdiction ticket (≡ A2-M2). |
| P2-2 | COSMETIC | Lone-numbered-child §7.2.1 form. | **AFFIRMED** as-is (citeability rationale; ≡ A2-C2). |
| P2-3 | COSMETIC | HEB-36 broaden sequencing. | **RESOLVED** — sequenced into Phase-2 close. |
| P3-M1 | MATERIAL | §11.7.4 runtime-pass scope — PR-body "no runtime pass needed" under-scoped. | **RESOLVED** — claim re-scoped; §11.7.4 pass cited (post-fix). |
| P3-M2 | MATERIAL | §13.5.8 surface-type mislabels (CSD `version:`; VERSION `terminator`) — HEB-25 drift. | **RESOLVED** — `yaml-version` / `bare-version-file` (provisional), HEB-25 routed. |
| P3-M3 | MATERIAL | gh-PR-phase fragility (bare `gh pr view --json number`) — HEB-35. | **RESOLVED** — create-output capture; base-verify folded same-block (FP-5). |
| P3-C1 | COSMETIC | Edit 3 bare `version:` anchor vs staging 2-line anchor. | **RESOLVED** — 2-line anchor parity. |
| P3-C2 | COSMETIC | §1.6 repurposed (header-conformance → LABEL-EXISTENCE). | Benign — noted, unchanged. |
| P3-C3 | COSMETIC | BASH-INTERPRETER-PROBE not cited to §6.10. | **RESOLVED** — §6.10 cite added. |
| P4-C1 | COSMETIC | PR-body / §6 pass-count references (~1–2 passes stale). | Open — fix at vendor (use "Pass-1→Pass-N"). |

*Reviewer self-correction (recorded on the trail):* three-hat Pass-1 rated the versioning **POSITIVE** on the staging file's "no prior-conformant artifact becomes non-conformant" basis. That basis was false; the antagonistic stream caught it (A-M4). The conclusion (MINOR) held; the basis did not. The §7.9 grounding now in the artifact is correct.

### 3.2 Antagonistic stream

| ID | Sev | Finding | Final status |
|---|---|---|---|
| **A-B1** | BLOCKING | Phase-2 scope drift — targets #4 (ship-boundary gates) + #6 (DIRECTIVE-029 skill-regen wiring) dropped without disposition; lens relabeled Phase-1→Phase-2. | **RESOLVED** at ticket level — Roadmap-correction: #4 → HEB-12 + Phase-3 ship event; #6 → Phase-4 (+ §7.9-interim coverage); lens completes AC2 active-read leg. File scope ledger matches. |
| **A-B2** | BLOCKING | §7.6 lens restates §7.7 test + §7.2 rationale while claiming it does not — doctrine self-violation in the corpus carrier. | **RESOLVED** — §7.2.1 references, does not restate; self-claim stripped (≡ P1-M2). |
| A-M1 | MATERIAL | §7.2/§7.6/§7.7 surface-identity unpinned. | **RESOLVED** — §7.2 *is* the §7.7 review-findings-model surface; no DMS enumeration touch owed. |
| A-M2 | MATERIAL | Check-spec use/mention boundary unspecified. | **RESOLVED** — concrete-ID-anchored, schematic forms excluded (≡ P1-M3). |
| A-M3 | MATERIAL | §24.1↔§7.4 collision papered over locally. | **RESOLVED** — instance (descriptive ref) ratified; general seam routed (≡ P1-M6 / P2-1 / A2-M2). |
| A-M4 | MATERIAL | Versioning rationale right-answer-wrong-reason. | **RESOLVED** — §7.9 grandfather-until-touched basis; false claim removed (caught the three-hat P-1 miss). |
| A-C1 | COSMETIC | §7.6 ↔ DMS §7.6 coordinate collision. | **DISSOLVED** — §7.2.1 home; no §7.6 in CSD. |
| A-C2 | COSMETIC | "re-anchor per §13.5.10" mis-cite. | **RESOLVED** — corrected to §13.5.2 with the precise distinction. |
| A-C3 | COSMETIC | R026 cited from recall. | **RESOLVED** — verify-at-apply-prompt caveat added (≡ three-hat C-3). |
| A2-M1 | MATERIAL | Block 4 review-template gloss leans back into restatement (softer A-B2 recurrence). | **RESOLVED** — trimmed to a bare reference (trim-(a)). |
| A2-M2 | MATERIAL | §24.1 seam routed to HEB-39 — category mismatch. | **RESOLVED** — re-routed to a dedicated §7-jurisdiction / DIRECTIVE-024-refinement ticket, explicitly not HEB-39 (≡ P2-1). |
| A2-C1 | COSMETIC | Line-13 "surfaces landed" framing lossy. | **RESOLVED** — tightened to "active-read leg." |
| A2-C2 | COSMETIC | Lone-numbered-child §7.2.1. | **AFFIRMED** as-is (≡ P2-2). |
| A2-C3 | COSMETIC | §7.2.1 closing self-claim + dense parenthetical. | **RESOLVED** (self-claim) — trimmed; parenthetical kept (taste). |

**Normative-interpretation questions (antagonistic Pass-1 §2.5):** NI-1 (which surface *is* the §7.7 "review findings model") — resolved by A-M1's pinning (§7.2 is the surface; lens is its active-read facet). NI-2 (does §24.1's template violate §7.4) — routed to the dedicated DIRECTIVE-024-refinement ticket (the general seam), with the descriptive-reference instance ratified.

---

## §4 The runtime dry-run (§11.7.4) — the decisive pass

Three-hat Pass-3's static read rated the apply-prompt proceed-with-changes; the runtime pass moved it to PAUSE. Method: a mock HE-Bedrock built from the live corpus at the `28a496a` pre-amend state, every block run the operator's way (write-to-tempfile + `bash <file>`, per the FP-5 executor-shell discipline), the FP-5 probe additionally exercised under `dash` as a zsh proxy.

**P3-B1 (blocking), found and fixed.** The §1.7 Block 2 anchor check `command grep -qF '- Frontmatter schema conformance…'` — pattern begins with `-`, so grep parses it as an option (`grep: invalid option -- ' '`), takes its `||` branch, and emits a **false** "OLD anchor absent" RED that halts the sweep with `exit 1` on every run. The misleading message would be read as "`main` moved." Fix verified: `grep -qF -- '…'` (end-of-options marker) → exit 0; the full sweep then passes all 10 checks. It is the only leading-dash pattern in the file.

**What the dry-run cleared (and re-confirmed at Pass-4, post-fix):**
- FP-5 probe passes under bash; correctly REDs under a non-bash shell (the tripwire works).
- `set -euo pipefail` interactions are sound — the `grep -c` uniqueness check and the `! command grep … || {…}` absence check do not spuriously abort.
- All 8 edits apply with **unique** anchors; the §2.2 post-edit gate passes; the §7.2.1 idempotency guard correctly REDs on re-run (no double-insert).
- The §7.2.1 NEW text is **byte-identical** between the staging file and the apply-prompt's Edit 1 (vendoring fidelity).
- All bash blocks pass `bash -n`; the M-1 fix (create-output PR capture) is `bash -n`-clean and carries no bare `gh pr view --json number`.

**Lesson recorded.** Static convergence (0B/0M) is necessary but not sufficient; the §11.7.4 runtime pass caught a hard blocker both static streams missed. This is the FP-5 / leading-dash class (`grep -e` / `au`) made concrete on a live artifact.

---

## §5 Cross-stream observations

The two streams were genuinely complementary, not redundant:

- **The antagonistic stream caught what the three-hat stream rubber-stamped.** A-M4 (versioning right-answer-wrong-reason) corrected a three-hat **positive** (P-1) that had accepted a false basis. Recorded honestly: the three-hat pass under-verified; the adversarial read did its job.
- **The antagonistic stream rated shared findings more severely — correctly.** The restatement defect was three-hat **MATERIAL** (P1-M2) but antagonistic **BLOCKING** (A-B2), on the grounds that a doctrine self-violation shipped into the corpus *carrier* every consumer copies is categorically worse than a local conformance miss. The BLOCKING framing is the right one; it is preserved in this record.
- **The antagonistic stream caught a scope-integrity blocker the three-hat stream under-weighted.** A-B1 (#4/#6 dropped) was sharper than the three-hat P1-M4 (phase seam); the Roadmap-correction comment resolved both.
- **Independent convergence cross-validated the §24.1 routing.** Three-hat P2-1 and antagonistic A2-M2 independently flagged the HEB-39 venue mismatch — convergent evidence that strengthened the re-route decision.
- **One decision eased many findings.** The antagonistic Pass-1 §4 convergence note was correct: B-2, C-1, and M-1 all pointed at one question — one home (§7.2 + §7.2.x) vs. two (§7.2 + §7.6). The §7.2.1 keystone resolved that single decision and, with it, six findings across both streams at once.

---

## §6 Final audit outcome

> **CONVERGED.** Three-hat verdict (ENG-STD-001 §12.6): **LAA → proceed · SA → proceed · EA → proceed**. Antagonistic gate (DIRECTIVE-032): **satisfied** — both A-B1 and A-B2 cleared; A2-M1/A2-M2 resolved. Runtime gate (§11.7.4): **satisfied** — P3-B1 fixed and verified; the apply-prompt's blocks pass clean.
>
> **0 BLOCKING / 0 MATERIAL on both the static and runtime axes.** Residual is one COSMETIC documentation-currency note (P4-C1), addressable at vendor. The converged staging edits are contract-pure, correctly versioned MINOR (R040 / §7.9-grounded), and anchor-faithful; the apply-prompt is template-conformant, runtime-clean, and runnable (the Phase 1.7 hard stop is gone; pause-points + operator confirmation intact). This is the review-until-zero-findings terminus for Phase-2's work artifacts.

---

## §7 Forward-pointers & close-records actions

**Forward-pointers (each deliberate-first, DIRECTIVE-025 dedup):**

| Item | Source | Home |
|---|---|---|
| §24.1↔§7.4 seam (template ID-naming vs §7.4 prohibition) | A-M3 / P1-M6 / P2-1 / A2-M2 | New dedicated §7-jurisdiction / DIRECTIVE-024-refinement ticket — **not** HEB-39 |
| HEB-36 broaden (deliberation→execution; add contract-purity grep-impl) | P1-M5 / P2-3 | HEB-36 (sequenced into Phase-2 close) |
| DIRECTIVE-032 → §7.2 back-pointer + §7.2.1 antagonistic-review inheritance | P1-M8 | T12 (own ticket) |
| §13.5.8 taxonomy gap (`yaml-version` / `bare-version-file`) | P3-M2 | HEB-25 |
| gh-PR-phase worked-example hardening | P3-M3 | HEB-35 |
| #4 ship-boundary gates / #6 DIRECTIVE-029 skill-regen wiring | A-B1 | HEB-12 + Phase-3 / Phase-4 (per Roadmap-correction) |

**Close-records actions (Phase-5b; each pending its own ratification):**
- Cut the annotated corpus tag `v2.5.0` on the merge commit (DIRECTIVE-018).
- Vendor the Phase-2 ruling-rationale ledger — **R043** (the §7.2.1 active-read lens as an extension of R036) — re-verifying global-max across repo `docs/ruling-rationale/` + Notion per HEB-41 discipline; mirror R043 to the Notion design-decision SoR.
- Vendor this review-of-record to `docs/reviews/`.
- Three-layer HEB-38 Linear capture (comment + state + description banner via in-editor paste, DIRECTIVE-026).
- Queued captures: broaden+restate HEB-36; spin T12; create the §24.1↔§7.4 ticket. *(HEB-38↔HEB-36 relation already wired.)*
- **P4-C1:** update the apply-prompt's PR-body / §6 pass-count references to the full "Pass-1→Pass-N" set (incl. Pass-3 dry-run + Pass-4) at vendor.

---

## §8 Cross-references

- **Authority:** ENG-STD-001 §12.6 (three-hat); DIRECTIVE-032 (antagonistic); ENG-STD-003 (§6.x, §11.7.4, §13.5.2, §13.5.8); DMS §7.4–§7.9; HEB-38 Roadmap-correction comment (2026-06-26).
- **Constituent reviews consolidated here:** three-hat Pass-1, Pass-2, Pass-3 (+ sandbox dry-run), Pass-4; antagonistic Pass-1 (`2026-06-25-…-antagonistic-review.md`) and antagonistic Pass-2 (`heb-38-phase-2-antagonistic-findings-pass-2.md`).
- **Artifacts:** the converged staging edits (Blocks 1–8); the Phase-2 apply-prompt.
- **Corpus baseline:** `28a496a` (kit 2.4.0 · CSD 3.2.0 · DMS 3.2.0).
- **Rulings:** Phase-0 R032–R039 (Notion `389caeea`); Phase-1 R040–R042 (Notion `38acaeea` + repo mirror; max R042). Phase-2 mints **R043** (captured at close-records).
- **Tracker:** HEB-38 (Phase-2). Related: HEB-36, HEB-35, HEB-25, HEB-40, HEB-41, HEB-24, HEB-12, HEB-39, T12.
- **Disposition routing:** all findings returned to the authoring session verification-only (DIRECTIVE-032 §32.3); the reviewer did not self-fix. Dispositions are ratified as reflected in the converged artifacts.

*End of HEB-38 Phase-2 enforcement review-of-record (Pass-1 → convergence).*
