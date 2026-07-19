# File: docs/reviews/2026-06-24-heb-38-phase-1-contract-purity-three-hat.md (interim — first sweep, pre-disposition)
# Author: Tad Haffey — Executive Architect, Haffey Enterprises LLC
# Created: 2026-06-24
# Description: HEB-38 Phase-1 (Contract-Purity Doctrine) three-hat review — complete first sweep (LAA + SA + EA). Interim deliberation artifact (DIRECTIVE-026 Tier-1, pre-commit). Findings pending per-item disposition; re-review round follows under the review-until-zero-findings cadence. Folds into the consolidated review-of-record at convergence.

# HEB-38 Phase-1 — Contract-Purity Doctrine — Three-Hat Review (First Sweep)

| Field | Value |
|---|---|
| **Review Date** | 2026-06-24 |
| **Reviewer** | claude.ai (LAA / SA / EA seats) — claude.ai-assisted authoring under DIRECTIVE-007 / DIRECTIVE-026 |
| **Scope** | The six amended surfaces in the HEB-38 Phase-1 review-target bundle, judged against the Notion Phase-0 ruling set R032–R039. |
| **Authority** | DIRECTIVE-007 (Multi-Role Review); three-hat cadence LAA → SA → EA, review-until-zero-findings. |
| **Status** | **Complete first sweep — all three hats.** Findings pending per-item disposition before the re-review round. |
| **Outcome** | **PASS WITH FINDINGS** — 0 BLOCKING, 12 MATERIAL (3 cross-pass elevations of 2 underlying issues), 2 COSMETIC, 1 process; 4 POSITIVE. Net distinct issues ≈ 11. |

---

## Lens definitions and baseline

- **LAA — Lead Application Architect (daily-driver):** will a practitioner authoring/reviewing/maintaining these documents get correct, unambiguous, navigable guidance?
- **SA — Solution Architect (migration cost / risk):** what does it cost to land and cascade this, and what's the blast radius?
- **EA — Enterprise Architect (governance / pattern enforcement):** does this conform to and reinforce the corpus's own governance patterns?

Fresh-fetched before forming any view: CSD (DIRECTIVE-007 incl. live §7.2, plus -023/-024/-026/-029/-031 §31.7/-032/-034); DMS (§7.1–7.3 and §4.6 verbatim anchors + every [existing] cross-reference target — §1.2–1.4, §2.3.1, §2.4, §4.1, §4.12, §6.1/§6.2); review/ADR/DDR/SDD templates; ENG-STD-001 §12.10; the live HEB-38 ticket + all three comments; the Notion Phase-0 ledger (page `389caeea…4cd0`).

Framing facts from the live trail: **(1)** Phase-1 scope is targets #1/#2/#7 — doctrine + content-contracts; mechanical enforcement is **Phase 2**, so findings are held to Phase-1 deliverables. **(2)** The §4.6 MINOR-vs-MAJOR tier is an explicitly-open authoring decision routed to SA/EA.

Findings carry the **remedy axis** the bundle proposes (add/fix vs remove/relocate) — dogfooding Surface 3.

---

## §2 Findings

### 2.1 BLOCKING
None.

### 2.2 Pass 1 — LAA (daily-driver)

#### M-1 · DIRECTIVE-029 mischaracterized in the canonical test subsection · *add/fix*
**Location:** §7.7 ("DIRECTIVE-029 propagates it to every citing surface"); echoed §7.9.
**Description:** Live DIRECTIVE-029 is **Governance Maintenance Cadence** — a periodic + triggered *audit*, not a propagation engine. The propagation/skill-refresh capability is the Phase-2 extension, not yet wired.
**Why (LAA):** A reader who opens 029 for the propagation mechanism finds an audit cadence; and the doctrine polices reference accuracy, so this is the worst place for an inaccurate directive reference.
**Disposition:** Reword to 029's actual role (its cross-reference-integrity audit keeps citing references valid as the test amends); scope skill-refresh as forward-looking (Phase-2).

#### M-2 · DDR content-contract coverage gap · *add/fix*
**Location:** §F.3 vs live DDR template; §7.8.
**Description:** §7.8 says "each section" carries a content-contract. F.3 contracts five DDR sections; §F excludes three more by name. But `## Layer-of-abstraction note` and `## Substrate-stability tracking` are neither contracted nor named as exclusions. ADR/SDD are clean because their only un-contracted body sections (Review, Change Log) *are* named exclusions.
**Why (LAA):** A DDR author populating those sections finds no contract and no exemption — doctrine (§7.8) vs instance (F.3) inconsistency.
**Disposition:** Add the two contracts, or extend the §F exclusion rationale to name optional author-annotation sections as exempt with the reason.

#### M-3 · Remedy tag not wired into the structured finding block · *add/fix*
**Location:** §E.2 vs live review template (`#### Finding B-1` block).
**Description:** E.2 amends the descriptive bullet line but not the structured fill-in block authors actually populate — which gets no Remedy field.
**Why (LAA):** The review template is *the* delivery surface for the remedy axis (R036); if the populated slot has no remedy field, the tag is captured inconsistently or skipped.
**Disposition:** Add `**Remedy:** add/fix | remove/relocate (→ destination)` to the structured finding block; show that edit in E.2.

#### M-4 · §4.12 cite conflates the ADR/DDR/SDD References surface with the YAML pin surface · *add/fix* · *(borderline → COSMETIC defensible)*
**Location:** §7.5; §G rows for §7.4/§7.5.
**Description:** §4.12 governs YAML `governing_standards:` pins on control-docs/eng-stds. ADR/DDR/SDD references live in the metadata `References` row + `## Cross-References` and refresh via §4.1 fold-in / §4.6 PATCH cross-ref fix — not the §4.12 cascade. The compound phrase implies §4.12 governs both.
**Why (LAA):** An ADR maintainer following "refreshed per §4.12" lands on a pin cascade that doesn't apply. The core claim (these are append-only audit surfaces) is correct; only the refresh-mechanism cite is loose.
**Disposition:** Split the mechanism — pins per §4.12; ADR/DDR/SDD reference surfaces per §4.1/§4.6.

#### M-5 · DIRECTIVE-032 inheritance asserted but not wired · *add/fix*
**Location:** Surface 3 (D.2); target #2's home was "DIRECTIVE-007/-032."
**Description:** The remedy axis lands in DIRECTIVE-007 §7.2 and asserts antagonistic-review coverage, but DIRECTIVE-032 isn't touched and has no cross-ref to the §7.2 findings model. Inheritance works only via the review template (Surface 4).
**Why (LAA):** An antagonistic reviewer working from -032's text wouldn't discover the remedy obligation.
**Disposition:** State the review template is the delivery surface every review type inherits through, or add a -032 cross-ref to the §7.2 findings model. Surface which, since target #2 named -032.

#### C-1 · "§6.2 decision tree" misnames the section · *add/fix*
**Location:** §7.6.
**Description:** §6.2 is "Edge Cases"; the decision tree is §6.1. The routing content is correctly at §6.2, so the target resolves — only the descriptor is wrong.
**Disposition:** Drop "decision tree" (keep §6.2) or reword to "the §6.2 edge-case routing."

### 2.3 Pass 2 — SA (migration cost / risk)

#### SA-1 · §4.12 consumer-pin cascade is unsized before commit · *add/fix*
The MINOR tier is defensible (a loosening is backward-compatible), but §H defers the §4.12 cascade to apply-prompt authoring without sizing it. Two-document bump (DMS + CSD → 3.2.0) → every consumer pinning `DMS@3.1.0` / `CSD@3.1.0` needs a pin refresh. **Disposition:** run the §4.12 PreFlight enumeration now; confirm the cascade is bounded.

#### SA-2 · DDR content-contract gap is on the Phase-3 critical path · *add/fix* · elevates M-2
DDR-002 is the worked de-cruft exemplar for the SOFIA-Reboot cascade; its un-contracted sections would have nothing to cut against. An incomplete contract set risks a doctrine re-amendment mid-cascade, re-blocking the held RBT-46 / RBT-45. **Disposition:** close M-2 in Phase 1.

#### SA-3 · MINOR tier needs explicit ratification · *process*
§4.6 makes three-hat scope-tier agreement a gate ("disagreement … is the trigger to split or re-label"). MINOR can't pass silently. **Disposition:** ratify (or contest) MINOR as a named decision this cycle; record it for apply-prompt citation.

#### SA-4 · Touch-time baseline cost + Phase-2 skill re-vendoring · *cosmetic / forward-pointer*
§7.9's whole-doc baseline on first substantive touch is a real cost on heavy crufted docs (DDR-002 = 98 `R{N}` + 110 `RBT-NN`). Confirm the Phase-3 bulk set covers the heavy docs so the baseline doesn't ambush routine amendments. Forward: the Phase-2 skill-refresh must re-vendor to every consumer that vendored the HEB-9 skill.

#### SA-POSITIVE
Adoption blast radius is low by construction — R038/R039 anchor every piece on an existing corpus mechanic; no new directive, cadence, or Phase-1 artifact.

### 2.4 Pass 3 — EA (governance / pattern enforcement)

#### EA-1 · §A "verbatim" claim is false — the doctrine's own failure mode · *add/fix* · gates the review-of-record
A contract-purity doctrine must model source fidelity; §A paraphrases while claiming verbatim — the exact distortion DIRECTIVE-007 §7.4 + §26.5 police. (Dispositions intact; trailing rationale/parentheticals dropped — e.g., R032 loses "Knowing a change was decision-driven beats polluting the body…"; R034/R036/R037 compressed.) **Disposition:** correct §A before the review-of-record cites it as the conformance baseline.

#### EA-2 · §4.6 self-referential tier-bootstrapping — record as a bounded precedent · *add/fix*
The amendment classifies itself under the criterion it introduces. Acceptable because the criterion is three-hat-ratified in-cycle and §H discloses it — but record it as bounded ("self-application permitted only when the criterion is itself three-hat-ratified in-cycle"), not a blanket license.

#### EA-3 · Six-class taxonomy acceptance-criterion gap · *add/fix*
The HEB-38 charter lists "standard + six-class taxonomy" as an acceptance criterion; Phase-0 distilled A–F into the §7.7 test + §7.4's illustrative list rather than codifying named classes. Defensible (codifying six brittle classes = the over-specification the doctrine prevents, R034), but the gap must be dispositioned explicitly. **Disposition:** annotate the HEB-38 acceptance checklist ("taxonomy subsumed into the §7.7 test"); record on the Linear trail (Phase-0 ledger frozen per §31.7).

#### EA-4 · 029 mischaracterization = single-source-of-truth drift · elevates M-1
§7.7 asserts a 029 capability that doesn't exist — precisely the drift DIRECTIVE-029 §29.4's own single-source check would flag. Same fix as M-1, EA-priority.

#### EA-POSITIVE (two)
(a) Directive-reuse is exemplary — doctrine → DMS §7, CI → -023, refresh → -029, no new directive, single citable identity = the R035 test (R039). (b) The doctrine extends the existing §7.1–7.3 normative/operational line as its converse rather than a parallel taxonomy — correct home, anchored on §2.4 + §1.2.

### 2.5 No-drift confirmations (POSITIVE, cross-pass)

- **P-1** — Existing-text reproductions are genuinely verbatim: DMS §7.1–7.3, DMS §4.6, DIRECTIVE-007 §7.2 match the live corpus; the §4.6 converged delta matches its own changelog note.
- **P-2** — §7.7's contract-purity test faithfully implements R035 and the ticket's "could a stranger build from this?" cut-line.
- **P-3** — §7.9's grandfather-until-touched baseline is an accurate analogue of ENG-STD-001 §12.10.
- **P-4** — ADR and SDD content-contract coverage is complete.
- **P-5** — §7.4 correctly genericizes the ledger's `RBT-NN` to `{{TRACKER_PREFIX}}-NN` for the kit-level DMS.
- **Checked-clean** — The DMS's own whole-doc baseline rides the Phase-3 cascade (kit as source-of-truth), not this additive amendment; the discipline doesn't retroactively bind its own enacting PR.

---

## §3 Consolidated roll-up

| ID | Pass | Severity | Theme | Cross-ref |
|---|---|---|---|---|
| M-1 | LAA | MATERIAL | DIRECTIVE-029 mischaracterized | ↔ EA-4 |
| M-2 | LAA | MATERIAL | DDR content-contract coverage gap | ↔ SA-2 |
| M-3 | LAA | MATERIAL | Remedy tag not in structured finding block | — |
| M-4 | LAA | MATERIAL | §4.12 References/pins conflation *(borderline)* | — |
| M-5 | LAA | MATERIAL | DIRECTIVE-032 inheritance not wired | — |
| C-1 | LAA | COSMETIC | "§6.2 decision tree" mislabel | — |
| SA-1 | SA | MATERIAL | §4.12 cascade unsized before commit | — |
| SA-2 | SA | MATERIAL | DDR gap on Phase-3 critical path | ↔ M-2 |
| SA-3 | SA | process | MINOR tier needs explicit ratification | — |
| SA-4 | SA | COSMETIC | Touch-time baseline cost / Phase-2 skill re-vendor | — |
| EA-1 | EA | MATERIAL | §A non-verbatim — gates review-of-record | (LAA §2.5) |
| EA-2 | EA | MATERIAL | §4.6 self-bootstrapping — bounded precedent | — |
| EA-3 | EA | MATERIAL | Six-class taxonomy acceptance-criterion gap | — |
| EA-4 | EA | MATERIAL | 029 drift = single-source violation | ↔ M-1 |

**Tally:** 0 BLOCKING · 12 MATERIAL (3 are cross-pass elevations of 2 underlying issues) · 2 COSMETIC · 1 process · 4 POSITIVE. Net distinct issues ≈ 11.

---

## §4 Status and cadence

- **First sweep (LAA + SA + EA):** complete — findings above, pending **per-item disposition**.
- **Open decision carried into disposition:** the §4.6 MINOR tier (SA-3) — ratify or split per §4.6's own three-hat trigger.
- **Cadence:** review-until-zero-findings. After disposition, a re-review round verifies fixes and catches fix-induced drift (DIRECTIVE-032 §32.4 known blind spots: cross-block consistency; downstream platform behavior). The consolidated review-of-record folds all passes and is the citable artifact — authored design-side, committed via Claude Code per DIRECTIVE-026. Nothing posts to Linear/Notion without explicit ratification.

*End of first sweep.*
