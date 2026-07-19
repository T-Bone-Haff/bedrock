# File: docs/ruling-rationale/2026-06-28-heb-45-review-record-template-fix-rulings.md
# Author: Claude (claude.ai authoring session 2026-06-28) under DIRECTIVE-026
# Created: 2026-06-28
# Description: Ruling-rationale ledger for the in-document review-history defect fix
#              (HEB-38 Phase-1 content-contract escape) — one ruling, R047, enacted
#              across five carriers: ADR §7 + SDD §9 template sections, DMS §7.8 + §4.4
#              clauses, and CSD DIRECTIVE-007 §7.1. Single-layer per DIRECTIVE-031
#              §31.2.1 (≤3 rulings). Vendored in Commit 2 of the HEB-45 work PR and
#              frozen at that commit per §31.7.

# In-Document Review-History Defect Fix — Ruling-Rationale Ledger (2026-06-28)

**Ticket:** HEB-45 — remove in-document review-history capture across its carriers (ADR §7, SDD §9, DMS §7.8, DMS §4.4, CSD DIRECTIVE-007 §7.1).
**Session:** claude.ai design/authoring 2026-06-28 (DIRECTIVE-026).
**Author:** Claude (claude.ai authoring session).
**Baseline SHA:** HE-Bedrock `main` @ `a3b8a70` — live-verified at session open (local == origin).
**Governance baseline (pre-amend):** CSD 3.3.0 · DMS 3.2.0 · kit VERSION 2.5.0 · corpus tag `v2.5.0`.
**Status:** Doctrine-fix ruling **R047** ratified (claude.ai 2026-06-28). This ledger vendors in **Commit 2 of the HEB-45 work PR** and **freezes at that commit** per §31.7.
**Ruling counter:** **R047** — continues the global sequence (prior global max **R046** [HEB-36], re-verified 2026-06-28 against the repo `docs/ruling-rationale/` set + Notion, per HEB-41 discipline). R048 (Reboot adoption) is the sequential sibling, authored Reboot-side at the HEB-12 re-cascade push.

> **Single-layer ledger (§31.2.1).** One ruling (R047) plus an R048 ID-claim; §1 inventory layer omitted per the ≤3-ruling exception. Detail block only.

---

## R047 — The in-document review record is not a sanctioned audit surface; the defect is corrected across all five carriers

**Ruling.** The in-document review record is **not** a sanctioned audit surface. Review history lives in the external review of record (`docs/reviews/…`), pointed to from a document's Cross-References home; it is never captured in the document body. This single doctrine is enacted across the five carriers that sanctioned the prohibited surface:

1. **DMS §7.8** — strike "the in-document review record" from the no-content-contract enumeration, aligning it to §7.5 (whose in-document audit surfaces are the `## Change Log` and the cross-reference home **only**).
2. **DMS §4.4** (Multi-Version Decision-Record Pattern) — → **RESERVED**; the clause prescribed structuring an in-document `Review and Approval` section, the same prohibited surface. RESERVED per the §4.9 convention; no §4.x tail renumber (deferred to HEB-46).
3. **ADR template `## 7. Review and Approval`** — removed; review-of-record pointer homed in Cross-References; §8→§7 / §9→§8 renumber; metadata `Reviewers` + `Amendment Process` rows struck (reconcile to §2.3.1).
4. **SDD template `## 9. Architecture Review`** — removed; §10→§9 / §11→§10 renumber; new `## Cross-References` seated ahead of `## Change Log`.
5. **CSD DIRECTIVE-007 §7.1 ("No fabricated review entries")** — re-framed: the in-document review-and-approval-table framing dropped, the anti-fabrication rule re-homed on the external review of record. The §7.1 number is preserved; the rule's force is unchanged, its surface corrected.

The DDR template (no review section) was already correct; it takes only a Cross-References parity touch so the review-of-record and grounding-deliberation pointers are byte-parallel across all three templates.

**Disposition.** Doctrine correction — a HEB-38 Phase-1 content-contract escape. Repairs the Phase-1 delivery to conform to the one-home rule (§7.5 / §2.3.1) the corpus already established. One ruling enacted across five carriers; the §4.4 and §7.1 carriers were folded in during execution-deliberation (per-item ratified), as the carrier sweep widened from the template sections to the DMS and CSD clauses that blessed them.

**Rationale.** §7.5, §2.3.1, and the DDR template already encode review-routes-external. The five carriers were the stray sanctions contradicting that intent — and, in the case of CSD §7.1, the **root blessing the templates inherited**. The defect is a **matched set across five carriers** — the ADR and SDD templates (§7, §9), two DMS clauses (§7.8, §4.4), and the CSD directive clause (DIRECTIVE-007 §7.1). It was surfaced by the HEB-38 Phase-3 cascade scan as a **self-violation in the standard's own carriers** — the doctrine shipping the pattern it prohibits (dogfooding catch; same class as Phase-2's standalone-§7.6 self-restatement). The fix (a) restores §7.8 ↔ §7.5 internal consistency; (b) **structurally prevents re-accretion** — every future ADR/SDD authored from the corrected template starts clean, and every author reading the re-framed CSD §7.1 is pointed at the external review of record rather than an in-document table; with the CSD root carrier re-framed, the carrier set is genuinely closed across the HE-Bedrock doctrine carriers (the SOFIA-Reboot instances that still carry the surface are handled by R048 adoption); (c) aligns the templates with the live RBT-47 validator, which flags in-body finding-IDs and is thereby confirmed correct, not over-broad.

**Alternatives rejected.**
- *Fix only the template sections; leave the DMS clauses and CSD §7.1.* Rejected — the DMS §7.8/§4.4 clauses and the CSD §7.1 blessing re-introduce the defect on the next ADR/SDD authored, and a future author reading §7.1 can reasonably re-add the table. Closing the leaf carriers while leaving the root is the precise re-accretion HEB-38 exists to prevent.
- *Extend the validator to strip the in-document review record (Seam-1 option-b).* Rejected — it would keep the in-doc review record a sanctioned surface, contradicting §7.5 / §2.3.1 and perpetuating double-homing. The one-home reading evicts; it does not bless.
- *Collapse §7/§9 to a thin in-doc pointer, keeping the section.* Rejected for delete-and-renumber (pointer homed in Cross-References per §7.5) — a viable mechanical form, but retaining the section retains the surface.
- *Delete CSD §7.1 outright.* Rejected — the anti-fabrication principle is load-bearing and generalizes to the external review of record; re-frame preserves the rule while correcting its surface.

**Primary sources verified.** Live DMS §7.4–§7.9 (esp. §7.5 surface-types, §7.7 test, §7.8 content-contracts) + §2.3.1 + §4.4 + §4.9 (RESERVED convention); CSD DIRECTIVE-007 §7.0–§7.5 (full directive — confirmed zero by-number references to §7.1 corpus-wide; §7.2.1/§7.4/§7.5 already assume the external review-surface model) + DIRECTIVE-031 §31.7 (immutability + freeze) / §31.9 (ledger-in-PR gate); the ADR template (`## 7` + metadata `Reviewers`/`Amendment Process` rows) and SDD template (`## 9`); the DDR template (confirmed clean); the RBT-47 validator strip-set. All @ `a3b8a70`.

**Other.**
- *Empirical floor:* concrete five-carrier defect (two templates, two DMS clauses, one CSD clause), not a single-instance generalization.
- *Version tier (§4.6):* MINOR across all edited docs — every edit reference-preserving (§7.8 strike + §4.4-RESERVED + §7.1 re-frame preserve section numbers; renumbers carry zero by-number cross-ref breaks). kit 2.5.0→2.6.0, DMS 3.2.0→3.3.0, CSD 3.3.0→3.4.0, tag `v2.6.0` post-merge.
- *Forward-pointer:* HEB-46 — deferred DMS §4.x RESERVED-marker collapse + tail renumber (§4.4, §4.9) at next MAJOR DMS touch.
- *Ratification venue:* claude.ai 2026-06-28, HEB-45.

*End of in-document review-history defect-fix ruling-rationale ledger.*

---

## R048 — claimed + disposition set; full ledger authored Reboot-side at the push

**R048 — disposition (ID claimed sequential to R047 per HEB-41; full ledger at the push, substrate-fresh).** SOFIA-Reboot adopts the HE-Bedrock contract-purity / standalone-buildability standard (DMS §7.4–§7.9 + the corrected ADR/DDR/SDD templates + CSD §7.1, post-R047) as the corpus standard for its project-authored ADR/DDR/SDD bodies. The HEB-38 Phase-3 cleanup register is the adoption work-order; the four bodies re-form against the standard; RBT-46 lands on the cleaned DDR-002; DDR-003 / SDD-001 author clean from the start. Reboot ledger. Full ledger authored at the push against the materialized, re-cascaded corrected standard.
