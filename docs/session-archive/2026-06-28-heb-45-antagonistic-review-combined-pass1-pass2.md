# File: docs/reviews/2026-06-28-heb-45-antagonistic-review-combined-pass1-pass2.md
# Author: Claude (claude.ai antagonistic-review session 2026-06-28) under DIRECTIVE-026 / DIRECTIVE-032
# Created: 2026-06-28
# Description: Combined two-pass antagonistic review of the HEB-45 in-document review-record
#              defect-fix edit set + apply-prompt + R047 ledger. Input substrate for the
#              review-of-record author. Verification-only per DIRECTIVE-032 §32.3 — names
#              finding destinations; does not enact. NOT the review of record itself.

# HEB-45 — Combined Antagonistic Review (Pass 1 + Pass 2)

| Field | Value |
|---|---|
| **Work item** | HEB-45 — remove in-document review-history capture (HEB-38 Phase-1 content-contract escape) |
| **Ruling** | R047 (one ruling, five carriers) |
| **Baseline** | HE-Bedrock `main` @ `a3b8a70` (live-verified, local == origin) |
| **Stream** | Antagonistic (DIRECTIVE-032) — verification-only; destinations named, enactment returns to the work session (§32.3) |
| **Severity vocabulary** | BLOCKING / MATERIAL / COSMETIC / POSITIVE (DIRECTIVE-007 §7.2 lock-in) |
| **Remedy axis** | add/fix · remove/relocate · none (DIRECTIVE-007 §7.2) |
| **Pass 1 substrate** | 4-carrier edit set (ADR §7, SDD §9, DMS §7.8, DMS §4.4) + apply-prompt + Linear-comment R047 draft |
| **Pass 2 substrate** | 5-carrier edit set (+ CSD DIRECTIVE-007 §7.1) + rebuilt apply-prompt (2-commit, in-PR ledger) + vendored R047 ledger staging file |

> **What this document is.** Input to the review-of-record (RoR) author. It records both antagonistic passes, the Pass-1→Pass-2 disposition of every finding, and the verification basis. It does not enact remedies and is not itself the RoR.

---

## 0. Headline

**No BLOCKING findings in either pass.** The edit set is sound, the carrier sweep is now complete, every change is reference-preserving (verified by live grep, not asserted), and every str_replace/bash anchor matches live bytes and is unique. Pass 2 confirms the author resolved all six Pass-1 findings and correctly added a fifth carrier (CSD §7.1) that Pass 1's phrase-scoped sweep had missed.

The residual exposure is **governance-capture discipline, not edit soundness**: the R047 ledger asserts a §7.1 ratification the Linear trail does not yet substantiate, and the ledger freezes (Commit 2) before the named coherence gate (PAUSE-POINT 2). Both are resolvable before freeze and are the two items the RoR should foreground.

---

## 1. Disposition summary (Pass 1 → Pass 2)

| ID | Pass-1 finding | Severity | Pass-2 disposition |
|---|---|---|---|
| P1-M1 | Defect cardinality inconsistent ("pair"/"triple"/four surfaces) across ledger, apply-prompt, PR body — freezes under §31.7 | MATERIAL | **RESOLVED.** "Five carriers / five surfaces" is now uniform everywhere. Residual roll-up wrinkle → P2-C1. |
| P1-M2 | Phase-5b ledger-correction checklist incomplete; two `§31.6` mis-citations bound to freeze | MATERIAL | **RESOLVED.** Ledger now vendors in-PR (Commit 2, §31.9); both `§31.6` cites removed; verify asserts `§31.6` absent. |
| P1-C1 (m-1) | §1.3 baseline block labeled `AMBER:` but `exit 1` (RED behavior) | COSMETIC | **RESOLVED.** Now `RED:` + `exit 1`. |
| P1-C2 (m-2) | Post-edit verify had no dangling-section-pointer assertion | COSMETIC | **RESOLVED (partial).** Assertion added; catches title-bearing danglers only, not bare `→ §N` → P2-C3. |
| P1-C3 (m-3) | "RBT-47 validator confirmed to pass" framed as if it gated this PR | COSMETIC | **RESOLVED.** Moved to "Forward / cascade"; explicitly "not a Bedrock-side gate on this PR." |
| P1-C4 (m-4) | RESERVED-marker accretion (DMS §4.4 + §4.9) | COSMETIC | **Unchanged / tracked** to HEB-46. §7.1 carrier preserves its number (no new RESERVED marker). |

---

## 2. Pass 1 — findings as raised (4-carrier review)

Recorded for the RoR audit trail. Dispositions above.

**P1-M1 — Cardinality drift in the freeze-bound record.** *(remedy: add/fix → the R047 ledger + PR title/body)* The fix was variously "matched pair" (ledger Rationale — the §31.7-frozen text), "matched triple" (apply-prompt cold-read, PR body, ratification comment), while the prose enumerated four surfaces. Recommended one accurate phrasing applied uniformly before freeze. **Resolved** in Pass 2 (now "five carriers" uniformly).

**P1-M2 — Phase-5b checklist incomplete vs. §31.7 freeze.** *(remedy: add/fix → close-records handoff)* The checklist named two pre-freeze edits but missed the cardinality reword and the fact that the draft carried **two** `§31.6` mis-citations (intro + Status block). §31.6 is RESERVED/empty; §31.7's "Narrow exception" (placeholder backfill) is the correct target. **Resolved** in Pass 2 by relocating the ledger into the work PR (Commit 2) and stripping all `§31.6` cites, with a verify assertion.

**P1-C1 — §1.3 AMBER/RED mislabel.** *(remedy: fix)* Halting block labeled AMBER. **Resolved** (RED).

**P1-C2 — No dangling-pointer verify.** *(remedy: add/fix → apply-prompt §2.2)* **Resolved (partial)** — see P2-C3.

**P1-C3 — RBT-47 framing.** *(remedy: relocate → PR "Forward" section)* **Resolved.**

**P1-C4 — RESERVED-marker accretion.** *(remedy: none — tracked)* HEB-46 owns the eventual §4.x collapse.

---

## 3. Pass 2 — new findings (5-carrier review)

**P2-M1 — The §7.1 fifth carrier (and the in-PR / CSD-bump restructure) is not ratified or captured in the Linear trail, yet the ledger asserts it was.** *(severity: MATERIAL · remedy: add/fix → HEB-45 Linear trail + ticket title/description)*

The vendored R047 ledger states: *"the §4.4 **and §7.1** carriers were folded in during execution-deliberation (per-item ratified)."* The HEB-45 Linear trail is **unchanged since Pass 1** — its execution-ratification comment (2026-06-28 23:53) ratifies §4.4, the ADR metadata strike, delete-and-renumber, the DDR parity touch, and MINOR tier, but says **nothing about CSD §7.1**, the in-PR ledger relocation (§31.9), or the CSD `3.3.0→3.4.0` bump. The pinned ledger draft in Linear is still the four-surface "matched pair" version; the ticket title and description still describe the original three-surface scope.

So a substantive, well-justified decision (the §7.1 fifth carrier — a CSD / `system_locked`-directive edit) is about to be immortalized in a §31.7-frozen ledger that *claims its own ratification*, with no corroborating capture. This is the working model's "no presumed alignment" line: the decision is clearly Tad's intent (the five-carrier files were authored and uploaded), but the **three-layer capture** (comment + description banner + state) for §7.1 has not occurred, and the ledger pre-asserts it.

*Destination / resolution before Commit 2 freeze:* ratify §7.1 (and the §31.9 in-PR restructure + CSD bump) explicitly; capture to the HEB-45 trail (refresh the 23:53 comment or add a new one; update the stale title/description banner per three-layer capture). Then the ledger's "§7.1 per-item ratified" is true at freeze. *This is the single most important item for the RoR to carry.*

**P2-M2 — The ledger freezes (Commit 2) before the named coherence-review gate (PAUSE-POINT 2).** *(severity: MATERIAL · remedy: add/fix → apply-prompt phase sequencing or freeze-semantics note)*

PAUSE-POINT 2 is labeled "the coherence-review gate," and it runs **after** Commit 2 — which freezes the R047 ledger per §31.7. Any ledger-affecting finding surfaced at that gate therefore lands post-freeze, forcing either a §31.7-tension amend or a deferral to the Linear trail. The substantive review (this Pass 1 + Pass 2) is pre-commit, so the practical risk is bounded — but the ordering inverts the safer pattern.

*Destination / resolution (either):* (a) scrutinize the ledger **staging file at PAUSE-POINT 1** (pre-Commit-2) and scope PAUSE-POINT 2 to Commit-1 corpus coherence (templates/DMS/CSD, which §31.7 does not freeze); or (b) the apply-prompt explicitly states the §31.7-compliant pre-push correction path — `git commit --amend` on Commit 2 is clean while nothing is pushed (final history stays one ledger commit; immutability binds the *permanent/pushed* record). Naming this removes the trap.

**P2-C1 — "five carriers in three documents" — the document-count roll-up invites a recount.** *(severity: COSMETIC · remedy: fix → ledger Rationale + apply-prompt cold-read + PR body)* The "five carriers / five surfaces" count is now unambiguous and uniform — P1-M1 is genuinely resolved at that level. But the "**three documents**" roll-up collapses the ADR and SDD templates into one "decision-record template" class; a reader counting files sees four carrier-files (adr-template, sdd-template, DMS, CSD). Consider "across the two templates, the DMS, and the CSD" or dropping the document-count, to avoid a freeze-bound phrase that invites recounting.

**P2-C2 — Re-framed CSD §7.1 asserts the review-is-external surface-model freestanding.** *(severity: COSMETIC · remedy: add/fix → CSD §7.1 new_str)* The new §7.1 opens *"Review history is captured in the external review of record (`docs/reviews/…`), not in the document body…"* — establishing the surface-model in DIRECTIVE-007's voice without citing its authority. The surface-model's home is DMS §7.5; §7.1's own jurisdiction is review-integrity (anti-fabrication). A `(per DMS §7.5)` pointer would cite-not-restate the surface-authority — aligned with the very contract-purity doctrine being enforced (§7.7 keeps load-bearing cross-references; it evicts restatement). Low materiality; the rule's force is intact either way.

**P2-C3 — Dangling-pointer assertion is a partial regression guard.** *(severity: COSMETIC · remedy: add/fix → apply-prompt §2.2)* The added assertion greps for `§N (Review and Approval|Architecture Review)` — it catches *title-bearing* danglers but not a bare `→ §7` that drops its title (which was the actual Pass-1 defect shape in ADR §6 Compliance, since corrected). The current templates are verified clean, so the assertion passes correctly; as a forward regression guard it under-covers. Optional: also assert no template-body `→ §N` resolves into a removed/renumbered section number.

**Note (not a finding) — Linear ticket staleness.** Title/description still read "ADR §7 + SDD §9 + DMS §7.8"; the pinned ledger draft is the superseded four-surface version. Folds into P2-M1's capture remedy.

---

## 4. POSITIVE confirmations (no-drift / verified-sound)

Required per DIRECTIVE-007 §7.2 — the audit substrate so future passes need not re-derive these.

**P-1 — Carrier set is complete (the core mandate).** A broad adjacent-vocabulary re-sweep ("fabricat", "review-and-approval table", "reviewer name", "Date | Outcome | Findings", LAA/SA/EA inline tables, "in-document/interstitial review") surfaces **no sixth carrier**. The five carriers (ADR §7, SDD §9, DMS §7.8, DMS §4.4, CSD §7.1) are the complete set in the HE-Bedrock master. All other review-vocabulary hits are the external review-of-record *home* (`review-template.md` — the correct destination), already-correct allies that route review external (DMS §2.3.4/§2.3.5; §7.5; §2.3.1; DDR template), or unrelated concerns (rationale/alternatives fabrication, compliance-tracking).

**P-2 — §7.1 is a sound, well-grounded fifth carrier.** §7.1 literally frames its rule *around* an in-document review table ("When a document template includes a review-and-approval table…"), presupposing the surface being removed — a genuine residual carrier and the *root* the templates' fabrication-guidance inherited. Honest note: **Pass 1 missed it** (phrase-scoped sweep matched "Review and Approval" but not "review-and-approval table"/"fabricat"); the catch is correct and closes the carrier set.

**P-3 — Reference-preserving, verified by live grep.** Zero by-number citations of ADR §7/§8/§9, SDD §9–§12, DMS §4.4, or CSD DIRECTIVE-007 §7.1 anywhere in the corpus (every `§4.4` hit is ENG-STD-001/002/003's own §4.4; the only `§7.1` hit is the CSD heading itself). The renumbers, the §4.4 RESERVE, and the §7.1 re-frame break nothing. §7.1's number is preserved regardless.

**P-4 — All str_replace / bash anchors present and unique against live bytes @ `a3b8a70`.** DMS §7.8 strike phrase (×1), §4.4 block (×1), `version: 3.2.0` (×1); CSD §7.1 re-frame phrase (×1), `version: 3.3.0` (×1, no stray `3.4.0`); PROVENANCE Kit/DMS/CSD cells + Updated date — all matched and unique. str_replace will not mis-target.

**P-5 — Reduced-form confirmed for both DMS and CSD.** Both carry `doctype: control-document` + `version:` only (no own `## Change Log` / `# Revised:`; the Change-Log/Revised hits are inside embedded *example* templates). The §13.5.8.2 PostVerify version-pair (YAML ↔ Change Log) is correctly N/A and not asserted. Zero `DMS@`/`CSD@` `governing_standards:` pins corpus-wide → both bumps trigger zero §4.12 pin-propagation.

**P-6 — Byte-parallelism of the harmonized Cross-References bullets holds.** The DIRECTIVE-034 grounding bullet and the review-of-record bullet are byte-identical across ADR/SDD/DDR (one distinct variant each); no duplicates. DDR parity touch intact.

**P-7 — Fix-induced-drift trap caught.** The ADR §6 Compliance content-contract's `review sign-off (→ §7)` pointer was rewritten to `→ the external review of record, pointed to from Cross-References` — the renumber introduced no dangling reference.

**P-8 — §31.9 ledger-in-PR + §31.9(d) placeholder-clean.** The R047 ledger and dual-stream review-of-record now vendor in the work PR (Commit 2), satisfying §31.9; the staged ledger carries no unfilled metadata-field placeholders and no `§31.6`.

**P-9 — MINOR tier holds.** Removal+renumber is reference-preserving (no by-number cites) and existing decision records are grandfather-until-touched (§7.9), so no prior-conformant artifact becomes non-conformant in the SemVer sense. kit 2.5.0→2.6.0, DMS 3.2.0→3.3.0, CSD 3.3.0→3.4.0.

**P-10 — §4.4 RESERVE drops no load-bearing function.** Multi-version history is served by the `## Change Log` (§4.1 step 5) + the external review-of-record; §4.4's removed mechanism was the in-document sign-off subsections. RESERVE form matches the §4.9 precedent byte-for-byte; no §4.x tail renumber (would break §4.6/§4.10–§4.12 cites) — deferred to HEB-46.

**P-11 — Loophole closure is structural, not cosmetic.** Post-strike, an in-document review section is no longer a blessed surface — it becomes a body section the §7.7 test actively evicts; §4.4 no longer prescribes it; §7.1 no longer presupposes it. The doctrine now *rejects* the pattern in its own carrier rather than tolerating it.

---

## 5. Open items to settle before the Commit 2 ledger freeze

1. **Ratify + capture the §7.1 fifth carrier** (and the §31.9 in-PR restructure + CSD bump) to the HEB-45 Linear trail; refresh the stale title/description banner. *(P2-M1 — the gating item.)*
2. **Resolve the freeze-before-coherence-gate ordering** — review the ledger staging file at PAUSE-POINT 1, or state the amend-before-push freeze semantics in the apply-prompt. *(P2-M2.)*
3. **Cardinality phrasing** — settle "three documents" vs. an unambiguous alternative for the freeze-bound ledger/PR text. *(P2-C1 — operator's wording call.)*
4. *(Optional)* `(per DMS §7.5)` pointer in re-framed §7.1; broaden the dangling-pointer assertion. *(P2-C2, P2-C3.)*

---

## 6. Verification basis (both passes)

Fresh-fetched at review time (project-knowledge corpus @ `a3b8a70`, full-document reads):

- **DMS** — §2.3.1, §2.3.4/§2.3.5 (reviewer-row strips), §4.1, §4.4, §4.6, §4.9 (RESERVED precedent), §7.1–§7.9 (contract-purity); frontmatter (reduced-form); corpus-wide grep for carriers, by-number §4.4 refs, `DMS@` pins, `3.2.0` uniqueness.
- **CSD** — DIRECTIVE-007 preamble + §7.1 (full text, re-frame anchor), §7.2/§7.2.1 (review vocabulary + remedy axis + contract-purity lens); DIRECTIVE-031 §31.4–§31.9 (§31.6 RESERVED, §31.7 immutability + narrow exception, §31.9 ledger-in-PR gate); frontmatter (reduced-form); `version: 3.3.0` uniqueness; §7.1 by-number ref sweep.
- **Templates** — ADR/SDD/DDR canonical vs. corrected staging diffs; section maps; byte-parallelism; dangling-pointer / carrier-residue checks.
- **ENG-STD-003** — §3.4 (exit-code), §5.9/§6.7 (staging presence), §10.3 (file-based commit), §13.5.8/§13.5.8.2 (surface manifest + version-pair gate), §13.5.9 (schema fetch), §13.5.11 (branch capture).
- **DDR-001** — Render Transform Contract (template render/verify-gate exemption).
- **PROVENANCE / VERSION** — cell anchors + uniqueness.
- **Linear HEB-45** — ticket (description, relations, state) + both pinned comments (scope ratifications; R047 ledger draft) — re-fetched in Pass 2 (unchanged).
- **Notion** — searched; no separate R047 page exists (repo-vendored by design; the staging ledger is authoritative).
- **Broad adjacent-vocabulary re-sweep** (Pass 2) — confirmed no sixth carrier.

*Not independently verifiable from the Bedrock side (out of scope here):* the RBT-47 validator pass (SOFIA-Reboot @ `4afbe38`) — correctly de-scoped to the HEB-12 cascade target, not a gate on this PR.

---

## 7. Recommendation

Land **Commit 1** (the five-carrier kit amendment) as-authored — no edit-soundness reservation. Gate **Commit 2** (the ledger freeze) on resolving **P2-M1** (ratify + capture §7.1) and addressing **P2-M2** (freeze/coherence ordering), so §31.7 does not immortalize an unsubstantiated ratification claim or strand a late ledger finding. The COSMETIC items are wording/robustness polish the RoR can fold in or defer.

The cardinality precision that drove Pass 1 is genuinely resolved at the surface-count level; the remaining material items are governance-capture and freeze-sequencing, not edit defects. The change does what the mandate asked — it closes the in-document-review loophole *structurally*, including the CSD root carrier — provided the §7.1 ratification is made real in the record before it freezes.

*End of combined antagonistic review (Pass 1 + Pass 2).*
