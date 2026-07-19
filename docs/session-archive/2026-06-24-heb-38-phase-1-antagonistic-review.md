# File: docs/reviews/2026-06-24-heb-38-phase-1-antagonistic-review.md
# Author: Tad Haffey — Executive Architect, Haffey Enterprises LLC
# Created: 2026-06-24
# Description: Antagonistic review (DIRECTIVE-032) of the HEB-38 Phase-1 contract-purity doctrine authored text. Gate served: ratification-to-land for the Phase-1 DMS/CSD/template amendments.

# Antagonistic Review — 2026-06-24 (HEB-38 Phase-1 Contract-Purity Doctrine)

| Field | Value |
|---|---|
| **Review Date** | 2026-06-24 |
| **Reviewer** | Claude (claude.ai) — fresh-eyes antagonistic pass under DIRECTIVE-032; three-hat lenses (LAA → SA → EA) folded into one consolidated pass under DIRECTIVE-007; authored for T. Haffey (Executive Architect, Haffey Enterprises LLC) under DIRECTIVE-026 |
| **Scope** | The six authored surfaces in the HEB-38 Phase-1 review-target bundle (DMS §7.4–§7.9; DMS §4.6 retune; CSD DIRECTIVE-007 §7.2 remedy axis; review-template §2 render; ADR/DDR/SDD content-contracts), judged against the frozen Phase-0 rulings R032–R039 and the live corpus. |
| **Authority** | HEB-38 (HE-Bedrock team); DIRECTIVE-032 (antagonistic protocol); DIRECTIVE-007 (multi-role review); the frozen Phase-0 ruling ledger (Notion `389caeea-1325-81f6-bdb5-d30e2a3c4cd0`) as the DIRECTIVE-034 conformance substrate. |
| **Outcome** | **FINDINGS — NOT GATE-CLEAR.** Doctrine is structurally sound and well-anchored; Phase-1 land is held pending resolution of 1 BLOCKING (B-1) + disposition of 4 MATERIAL findings, with a Pass-2 verification to close. |

---

> **Verification posture.** All "existing/verbatim" claims in the review-target bundle were checked against the live corpus rather than the bundle's own reproductions: DMS §7.1–§7.3 / §4.6 / §4.1 / §4.12 / §2.4 / §2.3.1 / §6.2 / §1.2–§1.4; ENG-STD-001 §12.10; CSD DIRECTIVE-007 §7.2 and DIRECTIVE-023 / -029 / -031 / -032 / -034; the live ADR / DDR / SDD / review templates; the live HEB-38 ticket + full comment trail; and the frozen Phase-0 ledger. This is **Pass 1** — zero-findings convergence is **not** asserted (DIRECTIVE-032 §32.4).

> **Remedy-tag note (dogfooding).** Each finding below carries a **Remedy** tag (`add/fix` vs. `remove/relocate`) — the orthogonal axis proposed by the artifact under review (DIRECTIVE-007 §7.2 / review-target §D.2, §E). This is a deliberate **pre-adoption demonstration** of the proposed render, not current canonical template structure. It doubles as a live exercise of the axis (see M-2, which finds where that render is incomplete).

---

## §1 Scope

### 1.1 In-scope per the HEB-38 Phase-1 review-target bundle

The converged authored text for six surfaces, each judged on its own terms against rulings R032–R039:

- **Surface 1 — DMS §7.4–§7.9** (new, additive) — reference-purity rule, two-surface-types, jurisdiction scope, canonical test, content-contracts, consolidation cadence. Implements R032/R033/R034/R035, R037-adjacent, R038.
- **Surface 2 — DMS §4.6** (retune) — content-preserving-consolidation definitions + split-trigger reparameterization + new PATCH example. Implements R037.
- **Surface 3 — CSD DIRECTIVE-007 §7.2** (additive remedy-axis block). Implements the R036 review piece.
- **Surface 4 — review-template §2** (remedy-axis render + §2 content-contract). Implements the R036 review piece.
- **Surface 5 — ADR/DDR/SDD per-section content-contracts** (+ shared authoring-guidance header line). Implements the R033/R036 authoring piece.
- **Version/tier classification** (§H): DMS 3.1.0 → 3.2.0 (MINOR); CSD 3.1.0 → 3.2.0 (MINOR).

### 1.2 Spot-check scope

Not a spot-check review — coverage is exhaustive across the six surfaces. Every cross-reference the authored text asserts (review-target §G map) was integrity-checked against the live target; every "existing verbatim" reproduction was diffed against the live corpus; every ruling-to-text conformance mapping was walked R032 → R039.

### 1.3 Out of scope (deliberately)

- **Phase-2 mechanical enforcement** — the DIRECTIVE-023 CI token-grep gate, the DIRECTIVE-029 skill-refresh trigger, the `author-decision-record` skill nudge, ship-boundary gates. Explicitly deferred by the bundle's phase-boundary note; a Phase-2 forward-pointer is logged at §3.
- **Phase-3 SOFIA-Reboot cascade** and the corpus de-cruft execution (scan → register → cleanup). Downstream of doctrine landing.
- **HEB-39** — the ENG-STD-002/-003 script/apply-prompt analogue. Sibling ticket, deliberate-first, out of this jurisdiction by R034.
- **Apply-prompt / packaging concerns** — kit VERSION bump mechanics and the §4.12 consumer-pin refresh, settled at apply-prompt authoring per §H.

---

## §2 Findings

### 2.1 BLOCKING findings — must resolve before Phase-1 land proceeds

#### Finding B-1: ADR content-contracts route eviction to a `References` surface the ADR template does not have

**Remedy:** `add/fix`

**Location:** Review-target §F.2 (ADR content-contracts §2 and §3); roots in authored §7.4/§7.5. Live target: `docs/templates/adr-template.md` — body §1–§8 and the metadata table.

**Description:** The ADR content-contracts direct operational-substrate eviction and grounding-ledger pointers to a `References` home. F.2 §2: *"any ledger/ticket/finding reference (→ Change Log / References)."* F.2 §3: *"name the grounding ledger once in References."* The live ADR template has **no References or Cross-References body section** — its sections are Context / Decision / Rationale / Alternatives Considered / Consequences / Compliance / Review and Approval / Change Log — and **no References row** in its metadata table (Document ID / Status / Version / Platform Version / Date / Authors / Reviewers / Supersedes / Amendment Process). The DDR has `## Cross-References`; the SDD carries a `References` metadata row and its content-contracts cite inline rather than relocate; the ADR alone has no `References` surface anywhere. The review-target §F-intro exclusion note (*"Cross-References/References are excluded … already governed by §2.3.1 / §7.5"*) silently assumes a surface the ADR lacks.

**Why blocking:** The doctrine's load-bearing claims are *"every fact has exactly one home"* and *"a remove/relocate finding MUST name the destination — never a bare delete."* As authored, the ADR content-contract instructs an impossible relocation: an ADR author with an inline DIRECTIVE-031 ledger pointer to evict has no sanctioned home, so the pointer is either kept inline (violating §7.4) or lost. Landing Phase-1 ships a content-contract pointing at nowhere, in a foundational template, on the exact mechanism the doctrine sells. This is a self-undermining conformance defect, not a deferrable polish item.

**Disposition:** Resolve before land. Two clean paths, author's choice: **(a)** add a `## Cross-References` (or `## References`) surface to the ADR template as part of this Phase-1 change — note this is a template-structure addition that must be explicit in scope and interacts with the tier rationale (see M-1); or **(b)** re-point the ADR content-contracts to surfaces the ADR actually has (Change Log Ticket column for ticket provenance), and answer where an ADR's grounding-ledger pointer lives if not in a References section. Entangled with scope note N-1 (§2.5) — extending content-contracts to the ADR is what surfaced this gap.

---

### 2.2 MATERIAL findings — in-scope-fix or dispositioned

#### Finding M-1: The retuned §4.6 cannot cleanly classify its own landing amendment

**Remedy:** `add/fix`

**Location:** Review-target §C.2 (§4.6 retune) + §H tier rationale. Live target: `DOCUMENT_MANAGEMENT_STRATEGY.md` §4.6.

**Description:** The Phase-1 DMS change bundles additive §7.4–§7.9 (unambiguously MINOR) with a **modification of existing §4.6 normative text** (the MINOR/PATCH definitions are reworded; the split-trigger bullets rewritten). Under the §4.6 rule **in force at PR-create** (the pre-amendment one), "originally-MINOR scope expands to require modifying existing content → split: the modification becomes a separate MAJOR." So the pre-amendment rule classifies this very edit as a MAJOR split — a bootstrap, since the amendment is changing that rule. And under the **new** §4.6 the edit still doesn't qualify cleanly: the retuned MINOR bullet reads *"existing content unmodified except content-preserving consolidation (§7.4),"* but the §4.6 self-edit modifies existing rule text and is **not** content-preserving consolidation (it changes what MINOR permits); the new split-trigger fires only on *reference-breaking or structural* modification, which this is not. The edit falls into a definitional gap the retune introduces — a backward-compatible **semantic** modification of existing rule text that is neither consolidation nor reference-breaking.

**Why material (not blocking):** The MINOR **outcome** is defensible by the SemVer spine the MAJOR bullet already names (this change is backward-compatible — a loosening — breaks no downstream reference, renumbers nothing, makes no prior-conformant artifact non-conformant). So the tier is probably right; what's missing is that the doctrine's own retuned text justifies it. For the one section whose job is classifying amendments — retuned by this amendment — failing to classify this amendment is a dogfooding miss that an EA pass must surface. It does not block land if the classification is sound, but it should be fixed in-scope so the doctrine is self-consistent on its first use. (The Phase-0 handoff pre-flagged exactly this as the open MINOR-vs-MAJOR question.) See the normative-interpretation disposition at §2.5.

**Disposition:** In-scope fix. Broaden the §4.6 MINOR carve-out to admit *backward-compatible semantic modification* (not only content-preserving consolidation), or route classification explicitly through the SemVer-compatibility spine the MAJOR bullet already implies; then sharpen §H to show that the §4.6 self-edit modifies (not merely appends to) existing normative content and lands MINOR for the stated SemVer reason.

#### Finding M-2: The remedy-axis render misses the per-finding surfaces authors actually fill in

**Remedy:** `add/fix`

**Location:** Review-target §E.2. Live target: `docs/templates/review-template.md` §2.1 structured block (the `#### Finding B-1` block) and §2.3 / §2.4 bullet formats.

**Description:** E.2 inserts the remedy tag into the prose enumeration of "each finding gets…". But the live review template carries the per-finding format in three forms, and E.2 touches only the enumeration. The **structured fill-in block** authors actually use — `#### Finding B-1` with **Location / Description / Why blocking / Disposition** fields — gains **no Remedy field**. The COSMETIC (§2.3) and no-drift (§2.4) **bullet** formats (`- {{finding}} — {{location}}`) gain no tag slot either — and the axis explicitly applies to COSMETIC findings (the bundle itself states a remove/relocate finding can be MATERIAL or COSMETIC). So the axis is delivered in the abstract enumeration but has no rendered home in the block an author types into. (This very review demonstrates the gap: rendering the tag here required pre-adopting a `**Remedy:**` line the template does not yet define.)

**Why material:** A lens that has no slot in the authoring surface is a lens that quietly stops firing — the precise failure mode HEB-38 exists to prevent (charter gap #2). Not blocking, because the enumeration carries the rule; material, because the render is incomplete where it counts.

**Disposition:** In-scope fix. Add a `**Remedy:**` field to the structured §2.1 block and a tag convention to the §2.3/§2.4 bullet formats — or explicitly state the enumeration is canonical and have the structured block render it.

#### Finding M-3: R036's "pre-promotion self-check" is not visibly delivered in Phase-1

**Remedy:** `add/fix`

**Location:** R036 (Phase-0 ledger / review-target §A) authoring-delivery triple, vs. authored §7.8 and review-target §F.1.

**Description:** R036 enumerates three authoring-time delivery surfaces: template content-contracts, the `author-decision-record` skill nudge (Phase 2, correctly deferred), and **a pre-promotion self-check**. The bundle delivers the content-contracts and a *per-addition* test (§7.8: "before adding to a section, run the test"; F.1 header: "before adding to any section…"). No distinct **pre-promotion** (whole-document, at the draft → PROPOSED boundary) self-check appears. "Before adding" and "before promotion" are different gates — the first is continuous, the second is a boundary check.

**Why material:** Either the per-addition check is intended to subsume the pre-promotion self-check — in which case the bundle should say so — or a ruled-for delivery surface is missing from Phase-1. Leaving it ambiguous risks a delivery item silently dropping between phases.

**Disposition:** In-scope clarify-or-add. Confirm the per-addition test subsumes the pre-promotion self-check (and state it), or add a whole-document pre-promotion self-check line to the authoring-guidance layer (which already hosts the "DELETE BEFORE PROMOTION TO PROPOSED" and DIRECTIVE-034 blocks).

#### Finding M-4: Two DDR body sections get neither a content-contract nor a stated exclusion

**Remedy:** `add/fix`

**Location:** Review-target §F.3 + §F-intro exclusion note. Live target: `docs/templates/ddr-template.md` — `## Layer-of-abstraction note`, `## Substrate-stability tracking`.

**Description:** The §F-intro scopes content-contracts to "normative body sections only" and excludes metadata / Change Log / Cross-References / the review homes. The live DDR template has two further body sections — `## Layer-of-abstraction note` (asserts which platform layer the DDR governs) and `## Substrate-stability tracking` (declares cross-DDR substrate dependencies and amendment blast radius) — that F.3 omits and the exclusion note does not name. Both are optional but substantive normative body content; by the stated scope they should carry contracts, and by silent omission an author gets no guidance there while a full-coverage conformance check under-covers or false-flags.

**Why material:** A defensible case exists that both are cross-reference-adjacent and belong conceptually with the excluded Cross-References surface — but the bundle does not make that argument; it simply omits them. The doctrine must be explicit about its own coverage boundary on the templates it governs.

**Disposition:** In-scope fix. Either add content-contracts to both sections, or name them in the §F-intro exclusion with rationale (e.g., classified as cross-reference-adjacent navigational/dependency surfaces).

---

### 2.3 COSMETIC findings — noted

- **C-1 — `add/fix` —** Review-target §A claims R032–R039 are *"reproduced verbatim from the Notion Phase-0 ledger,"* but against the live frozen ledger they are systematically abridged: R032 drops its closing Accepted-residual sentence; R033/R034/R035/R036/R038 drop trailing rationale clauses and parentheticals; several Anchors lines lose their parenthetical gloss. The binding **Dispositions** survive intact, so conformance is not corrupted — but §A leans on "verbatim" for its neutrality framing. Relabel as "abridged from the ledger (dispositions verbatim)," or restore the full text.
- **C-2 — `remove/relocate` —** Review-target §G cross-reference map lists `§7.4 → §4.12 [existing] "pins refreshed in place."` Authored §7.4 makes no §4.12 reference — the §4.12 citation lives in §7.5, which §G already maps separately. Delete the spurious §7.4 → §4.12 row. (Destination: removed; the claim is already carried by the existing §7.5 → §4.12 row.) An error in the integrity-checking aid is worth recording precisely because reviewers trust that aid.
- **C-3 — `add/fix` —** The remedy axis obligates each remove/relocate finding to "name the destination," while DIRECTIVE-032 §32.3 confines the antagonistic reviewer to verification, not corrective authoring. Naming a destination is almost certainly finding-metadata (like "why blocking"), not authoring the relocation — but the bundle does not reconcile the two, and a reviewer reading -032 could read the obligation as scope creep. One reconciling clause in the §7.2 block settles it.
- **C-4 — `add/fix` (optional) —** The axis's reach to antagonistic review rests entirely on the one scope sentence in the new §7.2 block (*"applies to … antagonistic …"*), with no back-pointer from DIRECTIVE-032 to §7.2. This is consistent with how the **severity** vocabulary already inherits (also implicit, no back-pointer), so it is not a defect — but a cross-reference from -032 to §7.2 would harden both axes at once.

### 2.4 No-drift confirmations (positive findings)

- **P-1 — `add/fix` n/a —** Authored §7.4 correctly de-binds the ledger's literal `RBT-NN` to the kit-canonical `{{TRACKER_PREFIX}}-NN` placeholder. Proper kit-master hygiene; the SOFIA-Reboot-specific binding did not leak into the upstream corpus.
- **P-2 —** The authored §7.4–§7.9 is **self-compliant**: its inline `R{N}` / `{{TRACKER_PREFIX}}-NN` / `B-N`/`M-N` tokens appear only as teaching examples of the prohibited class, which §7.4 frames as illustrative ("not an exhaustive list"). The doctrine obeys its own one-home rule. *(See the Phase-2 forward-pointer at §3 — the DIRECTIVE-023 token grep must be surface-scoped to exclude these teaching examples or it will false-RED on the doctrine itself.)*
- **P-3 —** Existing §4.6 (review-target §C.1) and DIRECTIVE-007 §7.2 (review-target §D.1) are **byte-accurate** against the live corpus. The remedy-axis block folds in correctly after the "Finding-severity vocabulary lock-in" block and before "Out-of-scope finding routing" — inside what is already the cross-review-type vocabulary home, which is why §7.2 (not DIRECTIVE-032) is the correct single home.
- **P-4 —** R039/R035 single-source homing is faithfully implemented: the contract-purity test is defined **once** in §7.7 and referenced (not restated) by §7.8, §F.1, and §E. No copy-paste-and-drift surface is created across the delivery surfaces.
- **P-5 —** The R034/§7.6 routing of the script/apply-prompt analogue to ENG-STD-002/-003 matches the live HEB-39 ticket scope exactly; the jurisdiction boundary (§2.4 governance-class discriminator; §1.3 generated-artifact exclusion) is clean and anchors entirely on existing corpus.

### 2.5 Normative interpretation

Two interpretation questions surfaced; both are dispositioned here rather than left as drift.

1. **§4.6 self-classification (from M-1).** *Question:* how does the corpus classify a backward-compatible **semantic** modification of existing normative rule text that is neither content-preserving consolidation nor reference-breaking/structural? The retuned §4.6, as written, does not cleanly cover this case. *Disposition:* **fold into the Phase-1 §4.6 amendment** (M-1 fix) — make the MINOR criterion route through SemVer-compatibility (backward-compatible loosening = MINOR), so the section classifies its own kind of edit. This is a governance-doc amendment, not a deferral.

2. **Verification-only scope vs. "name the destination" (from C-3).** *Question:* does the remedy axis's destination-naming obligation push the antagonistic reviewer past DIRECTIVE-032 §32.3's verification-only boundary? *Disposition:* **interpret destination-naming as finding-metadata, not corrective authoring**, and record that interpretation with a one-line clause in the §7.2 remedy block. No separate ledger entry needed; it rides the Phase-1 CSD amendment.

---

## §3 Forward-Pointer Triage

### Candidate (Phase-2, HEB-38) — DIRECTIVE-023 token-grep must be surface-scoped

**Source:** Positive finding P-2.

**Description:** Landing §7.4–§7.9 places literal `R{N}` / `{{TRACKER_PREFIX}}-NN` / `B-N`/`M-N` tokens into the DMS as teaching examples of the prohibited class. The Phase-2 DIRECTIVE-023 reference-check grep — the mechanical seed for the contract-purity rule — will false-RED on the doctrine text itself unless it is surface-scoped (frontmatter / header / fence-stripped body) rather than run as a full-body content grep. This is the known absence-assertion / self-describing-document scoping gotcha; §7.4 is now a live instance of it.

**Proposed disposition:** Fold into the Phase-2 enforcement design (the DIRECTIVE-023 gate work). Not a new ticket — it rides HEB-38 Phase-2. Carry it as an explicit acceptance criterion of the gate: "grep is surface-scoped; verified not to flag §7.4's teaching examples."

### Forward-pointer triage summary

| Proposed ID | Summary | Disposition |
|---|---|---|
| HEB-38 Phase-2 | DIRECTIVE-023 contract-purity grep must be surface-scoped to avoid false-RED on §7.4 teaching examples | Fold into Phase-2 gate design as an acceptance criterion |

---

## §4 Audit Outcome

> **FINDINGS — NOT GATE-CLEAR.** The contract-purity doctrine is structurally sound, faithfully implements R032–R039, is self-compliant, and anchors every disposition on existing corpus mechanics (5 positive confirmations, P-1…P-5). However, the Phase-1 land gate is **not satisfied**: 1 BLOCKING finding (B-1 — the ADR `References` relocation home does not exist) must resolve before land, and 4 MATERIAL findings (M-1 §4.6 self-classification; M-2 incomplete remedy render; M-3 missing pre-promotion self-check; M-4 uncovered DDR sections) should be dispositioned in-scope. 4 COSMETIC findings (C-1…C-4) noted; 2 normative interpretations dispositioned (§2.5); 1 Phase-2 forward-pointer logged (§3).

Per DIRECTIVE-032 §32.3 the antagonistic reviewer does not author the corrective action — findings return to the primary authoring session for disposition. **Gate satisfied when:** B-1 resolved, M-1–M-4 dispositioned, and a Pass-2 antagonistic pass confirms zero new findings and zero unresolved prior-pass findings (DIRECTIVE-032 §32.4 convergence).

**Residual blind spots (DIRECTIVE-032 §32.4.1).** This pass reads each surface largely in isolation; cross-surface propagation drift from the B-1 / M-1 fixes (e.g., adding an ADR References section ripples into §2.3.1 metadata expectations and the §H tier rationale) must be re-checked at Pass 2. Runtime behavior of the Phase-2 grep against the live environment is deferred-to-verification, not certified here.

---

## §5 Cross-References

- **Authority for this review:** HEB-38 (HE-Bedrock); DIRECTIVE-032 (antagonistic protocol); DIRECTIVE-007 (multi-role review); DIRECTIVE-026 (claude.ai authors / Claude Code executes).
- **Conformance substrate:** Notion Phase-0 ruling ledger `389caeea-1325-81f6-bdb5-d30e2a3c4cd0` (R032–R039, frozen per DIRECTIVE-031 §31.7).
- **Documents reviewed (review-target bundle surfaces):** DMS §7.4–§7.9, DMS §4.6; CSD DIRECTIVE-007 §7.2; review-template §2; ADR/DDR/SDD content-contracts; §H tier classification.
- **Live corpus fresh-read:** DMS (§7.1–§7.3, §4.1, §4.6, §4.12, §2.4, §2.3.1, §6.2, §1.2–§1.4); ENG-STD-001 §12.10; CSD (DIRECTIVE-007/-023/-029/-031/-032/-034); ADR/DDR/SDD/review templates; live HEB-38 ticket + comment trail.
- **Findings disposition tracking:** TBD — returns to the Phase-1 authoring session; commit refs / ledger entries to be assigned at disposition time.
- **Next review:** Pass 2 antagonistic verification after B-1 + M-1–M-4 disposition.
- **Related:** HEB-39 (ENG-STD analogue sibling, out of scope); HEB-9 (`author-decision-record` skill, Phase-2 nudge home).
