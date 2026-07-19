# File: docs/ruling-rationale/2026-06-26-heb-38-phase-2-enforcement-rulings.md
# Author: Claude (claude.ai authoring session 2026-06-26) under DIRECTIVE-026
# Created: 2026-06-26
# Description: Ruling-rationale ledger for HEB-38 Phase-2 (contract-purity enforcement). One ruling — R043
#              (the §7.2.1 active-read review lens as an extension of R036). Single-layer per DIRECTIVE-031
#              §31.2.1 (≤3 rulings). Frozen at commit per §31.7. This Notion-mirrored copy is the vendored
#              filesystem record; the Notion design-decision page is the product-design system-of-record.

# HEB-38 Phase-2 — Contract-Purity Enforcement Ruling-Rationale Ledger (2026-06-26)

**Anchor work item:** HEB-38 — Artifact contract-purity / standalone-buildability doctrine — Phase-2 (enforcement).
**Session:** claude.ai design/authoring 2026-06-25 → 2026-06-26 (DIRECTIVE-026).
**Author:** Claude (claude.ai authoring session).
**Baseline SHA:** HE-Bedrock `main` @ `28a496a` (main-only, HEB-24) — pre-amend corpus at ruling time.
**Governance baseline:** CSD 3.2.0 · DMS 3.2.0 · kit 2.4.0 (→ post-work-PR: CSD 3.3.0 · kit 2.5.0 · corpus tag v2.5.0).
**Status:** Phase-2 enforcement ruling R043 ratified (claude.ai 2026-06-26). Work PR `{{WORK_PR_NUM}}` → `main` @ `{{WORK_MERGE_SHA}}`; this ledger vendored via the Phase-2 close-records PR. *(SHA fields resolved by the close-records apply-prompt at execution, before this ledger commits — no unfilled placeholder survives to commit, per §31.6.)*
**Ruling counter:** **R043** — continues the global sequence (prior global max **R042** [HEB-38 Phase-1], verified 2026-06-26 against the Notion Phase-1 ruling SoR `38acaeea…`; repo `docs/ruling-rationale/` global-max re-verified at the close-records apply-prompt's Phase-0 gate per HEB-41 discipline).

Per DIRECTIVE-031 §31.7 this ledger is **frozen once committed**; supersessions record on the Linear trail and in a new per-phase ledger, never by amendment here. This vendored file mirrors the Notion product-design decision system-of-record.

> **Single-layer ledger (§31.2.1).** One ruling this phase (R043); the §1 inventory layer is omitted per the ≤3-ruling operator-judgment exception. Detail block only.

---

## R043 — The standing contract-purity review lens lands as DIRECTIVE-007 §7.2.1, extending the R036 remedy axis

**Ruling.** The standing contract-purity review lens is codified as CSD **DIRECTIVE-007 §7.2.1** — a numbered sub-subsection **co-located with the §7.2 remedy axis it extends**, not a standalone §7.6 section. §7.2 (the remedy axis together with the §7.2.1 lens) **is** the DMS §7.7 "review findings model" delivery surface: the remedy axis is its *tagging* facet (the direction tag on a finding already raised), the §7.2.1 lens its *detection* facet (the standing per-section obligation to actively raise contract-purity findings). The lens **references** the DMS §7.7 contract-purity test and §7.2's subtractive loop; it **restates** neither. Because §7.2 already is the review-findings-model surface, no DMS §7.7 delivery-surface enumeration touch is owed and no DMS edit is pulled into Phase-2.

**Disposition.** Review-model doctrine — extends R036 (the remedy axis). Sibling to R041, which also extends R036.

**Rationale.** R036 introduced the orthogonal remedy axis (add/fix vs. remove/relocate) — the *tagging* of a finding already raised — but supplied no *detection* obligation. Phase-2 enforcement needed the active-read lens that actually generates contract-purity findings; DMS §7.7 names "the review findings model" as one of the four delivery surfaces the doctrine binds. The load-bearing question, surfaced independently by both review streams (three-hat P1-M1 form + antagonistic A-B2/A-M1/A-C1) and called the keystone, was **one home** (§7.2 + a §7.2.x lens) vs. **two** (§7.2 + a standalone §7.6). Folding into §7.2.1: (a) honors frozen R036's "a remedy tag + one obligation line, **not** a heavyweight new review section"; (b) dogfoods the one-home contract-purity doctrine the edit enforces — the enforcement surface must not be the first instance of the failure it enforces against; (c) dissolves the §7.6↔DMS §7.6 coordinate collision a standalone §7.6 would introduce; (d) pins the surface-identity (§7.2 *is* the §7.7 review-findings-model surface; the lens is its detection facet, not a fifth surface), so no DMS enumeration touch is owed; (e) inherits §7.2's existing cross-review-type binding rather than re-deriving it. The original standalone §7.6 draft **restated** the §7.7 stranger-build test — a doctrine self-violation shipped into the corpus carrier every consumer copies (antagonistic BLOCKING A-B2; three-hat MATERIAL P1-M2). The §7.2.1 form references-not-restates, and the kept increment is solely the detection obligation (the genuine, non-overlapping add over R036's tagging axis). This single decision cleared six findings across both streams at once (P1-M1/M2/M8 + A-B2/A-M1/A-C1).

**Alternatives rejected.**
- *(a) Standalone DIRECTIVE-007 §7.6 section.* Rejected — it restated the §7.7 test (the doctrine self-violation, rated BLOCKING by the antagonistic stream on the grounds that a self-violation in the carrier is categorically worse than a local conformance miss), introduced a §7.6↔DMS §7.6 coordinate collision, and is exactly the "heavyweight new review section" frozen R036 steered away from.
- *(b) Unnumbered bolded `**Standing contract-purity lens.**` paragraph under §7.2.* Rejected (the closer alternative) — leaner, but it gives the delivery-surface cross-references (review-template §2 integration line + §2 contract comment) no stable citeable anchor. §7.2.1 supplies that anchor — the DMS §7.7 referenceability principle applied to the lens itself. Affirmed across both Pass-2 streams (A2-C2 / P2-2). The heavier counter-alternative (number every §7.2 bolded lead) is a reference-preserving MINOR carry-forward, out of Phase-2 scope.
- *(c) Treat the lens as a fifth §7.7 delivery surface requiring a DMS §7.7 enumeration amendment.* Rejected — §7.2 already is the review-findings-model surface; the lens is its detection facet. Treating it as a new surface would have pulled a DMS edit into Phase-2 unnecessarily.

**Primary sources verified.** Live CSD DIRECTIVE-007 §7.2 + frozen R036 (the remedy axis); DMS §7.4–§7.9 (the §7.7 contract-purity test and its four-surface delivery enumeration; §7.8 content-contracts' "reference — never restate"); the HEB-38 Phase-2 review trail (three-hat Pass-1/2/3 + §11.7.4 sandbox dry-run/Pass-4; antagonistic Pass-1/2) consolidated in the Pass-1→convergence review-of-record. All @ `28a496a`. Global-max ruling ID verified R042 against the Notion Phase-1 ruling SoR (`38acaeea…`, 2026-06-26).

**Other.**
- *Ratification venue:* claude.ai session 2026-06-26 — keystone Option 1 (one-home → §7.2.1), ratified per-item; HEB-38 Roadmap-correction comment (2026-06-26) carries the AC/phase reconciliation.
- *Relationship to R036:* extends, does not amend — R036 frozen (§31.7); R043 adds the detection obligation to R036's tagging axis. Sibling to R041 (remedy-axis totality), also an R036 extension.
- *Empirical floor:* single-cycle (the Phase-2 lens); a closed-form extension of an existing axis, not threshold-gated — no threshold override required.
- *Convergence note:* the one-home decision cleared six findings across the two independent review streams simultaneously (P1-M1/M2/M8 + A-B2/A-M1/A-C1); cross-stream convergence on the keystone is recorded in the review-of-record §5.

---

### Forward pointers (carry-forward — not rulings; queue-piggyback under R043 per §31.2.4)

- **§24.1↔§7.4 doctrine seam** — DIRECTIVE-024 §24.1's `tracked at {{backlog item ID}}` aspirational-compliance template instructs inline ID-naming, which DMS §7.4 prohibits inside a morphing body. The descriptive-reference *instance* (Block 2's "kit-level-validator work item") is ratified; the *general* seam routes to a **new dedicated §7-jurisdiction / DIRECTIVE-024-refinement ticket** — explicitly **not** HEB-39 (whose charter is the ENG-STD-002/-003 scripts/apply-prompts analogue, a different artifact class). Deliberate-first, DIRECTIVE-025 dedup. *(Sources: P1-M6 / A-M3 / P2-1 / A2-M2.)*
- **HEB-36 broaden** — deliberation → execution; add the contract-purity grep-impl deliverable alongside the doc-structure-validator promotion. The running grep mechanization is Phase-2.5. Sequenced into the Phase-2 close so the Block 2 descriptive reference resolves to a real owner. *(Sources: P1-M5 / P2-3.)*
- **DIRECTIVE-032 → §7.2 back-pointer + §7.2.1 antagonistic-review inheritance** — T12 (own ticket). *(Source: P1-M8.)*
- **§13.5.8 surface-type taxonomy gap** — the manifest lacks clean `yaml-version` / `bare-version-file` types (used provisionally this cycle); route to **HEB-25**. *(Source: P3-M2.)*
- **gh-PR-phase worked-example hardening** — capture PR identity from `gh pr create` output, not current-branch `gh pr view`; folded into **HEB-35**. *(Source: P3-M3.)*
- **#4 ship-boundary gates / #6 DIRECTIVE-029 skill-regen wiring** — re-homed per the Roadmap-correction comment: #4 → HEB-12 (render verify-gate) + the Phase-3 cascade ship event; #6 → Phase-4 (skill recompile). *(Source: A-B1.)*

*End of HEB-38 Phase-2 contract-purity enforcement ruling-rationale ledger.*
