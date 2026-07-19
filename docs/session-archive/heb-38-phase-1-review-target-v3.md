# HEB-38 Phase-1 — Contract-Purity Doctrine — Review-Target Bundle (v3, Pass-3 convergence close)

## 0. Orientation

This is the **v3 (post-Pass-2-disposition) review target** for the **Pass-3 convergence close** (DIRECTIVE-032 §32.4: verify the Pass-2 BLOCKING + MATERIALs are resolved and the §4.6 change classifies cleanly with zero new findings).

Pass-3 is **narrowly scoped by both Pass-2 passes** to the §4.6 unification (P2-B1/B-1) and its dependent resolutions (M-1/P2-M1, M-2) plus the cosmetics — judged against the already-verified spine (Pass-2 confirmed 11/13 prior dispositions closed, no spine drift). §R2 is the Pass-2→v3 disposition record; the changed surfaces are §C (§4.6, fully rewritten), §H (tier rationale), the new R040 ruling, and five cosmetics. The spine (§7.4–§7.9 less the two cosmetic touches, CSD §7.2, review §2, DDR/SDD contracts) is unchanged from v2 and reproduced for self-containment.

**Baselines.** HE-Bedrock `main @ 49b4c17a`; kit 2.3.0; corpus tag `v2.3.0`. **DMS 3.1.0 → 3.2.0 (MINOR)**; **CSD 3.1.0 → 3.2.0 (MINOR)** — tier now grounded directly in the unified §4.6 (§H).

---

## R2. Pass-2 → v3 disposition record

*Pass-2 (three-hat + antagonistic, both independent) returned 1 BLOCKING + 2 MATERIAL + cosmetics, non-converging. Operator-ratified dispositions below.*

| Pass-2 finding (source) | Disposition | Resolved in |
|---|---|---|
| **B-1 / P2-B1** BLOCKING — §4.6 reframe re-keyed modification on compatibility but left structural/renumber triggers categorical; the ADR §8→§9 renumber reads MINOR by §H, MAJOR by §4.6 | **Option (a), ratified:** unify all of §4.6 on the SemVer-compatibility principle — reference-preserving structural reorganization/renumbering is MINOR; MAJOR is reserved for reference-breaking / conformance-breaking change. | §C (rewritten) + **R040** |
| **M-1** (three-hat) — §4.6 MINOR justified circularly (by its own reframed text) | Ground the MINOR call in the **invariant compatibility property** (a reference-preserving renumber is backward-compatible regardless of criteria-version); the old categorical trigger was a miscalibrated proxy, now corrected. No bootstrap. | §H (rewritten) |
| **P2-M1** (antag) — the "self-application permitted when…" precedent is a forward-norm parked in an operational ledger note (violates §7.2) | Option (a) removes the need for any self-application permission — there is no self-reference to grant once the proxy is corrected. The framing is **dropped entirely**; no meta-rule codified, no ledger-note norm. | §H (framing removed) |
| **M-2** (three-hat) — the precedent note must not amend frozen R037 (§31.7) | The decision is recorded as a **new Phase-1 ruling R040**, cross-referencing R037 — not an edit to it. | **R040** |
| **P2-M2 / EA-3** — six-class taxonomy subsumption "pending ratification" | **Resolved:** ratified and posted to the HEB-38 trail this session (comment `364964f2`). The explicit A–F→§7.4/§7.5/§7.7 mapping folds into the close-records review-of-record. | trail (posted) |
| **Cosmetic** — §7.4 relocation-pointer example ADR/DDR-shaped (SDD has no Cross-References) | Made doctype-agnostic. | §B §7.4 |
| **Cosmetic (antag SA-4)** — §7.9 baseline marker presumes full-form frontmatter | One-line note: the Change-Log-row marker first applies at the reduced→full transition (DMS §2.3.4). | §B §7.9 |
| **Cosmetic (antag LAA-4)** — ADR §8 "Backlog items tracking §6 compliance conditions" | → "§6 Compliance backlog items." | §F.2 |
| **Cosmetic (three-hat)** — §S/§H mis-cite "SA-2" for atomic-landing | → "SA-1" (the cascade finding). | §S, §H |
| **Cosmetic (antag §G)** — §G missing the CSD→DMS forward-ref row | Row added. | §G |
| **DIRECTIVE-032 → §7.2 wiring** (both) | Pre-existing latent gap, out of scope; filed as deliberate-first backlog candidate post-HEB-38 (DIRECTIVE-025 dedup first). | forward (not text) |

**Reduced-form finding (live-verified this session):** both DMS and CSD working copies are reduced-snapshot form (no `## Change Log`, no `last_updated`/`# Revised:`, reduced frontmatter). Consequences fold into §S; the apply-prompt manifest and the reduced-vs-full transition are apply-prompt-authoring concerns (operator fork pending), not doctrine-text changes.

---

## A. Conformance baseline — R032–R039 (frozen) + R040 (this cycle)

Read R032–R039 from the frozen Notion Phase-0 ledger (`389caeea-1325-81f6-bdb5-d30e2a3c4cd0`; not reproduced — §A is a pointer, per the doctrine's one-home principle). **R040** (new this cycle, draft below) refines R037 on the forward trail.

### R040 — §4.6 structural-trigger compatibility unification (draft)

> **Disposition.** §4.6's MAJOR / MINOR / split-trigger criteria are unified on a single SemVer-compatibility test: a change is MAJOR iff it breaks a downstream reference or makes a prior-conformant artifact non-conformant; reference-preserving structural reorganization and section renumbering ride at MINOR. The categorical "structural reorganization / section renumbering → MAJOR" proxy is removed.
> **Rationale.** The categorical structural triggers were a surface-proxy for "breaks citations." In a by-name-reference corpus the proxy is miscalibrated — a reference-preserving renumber breaks nothing — so it contradicted the SemVer-compatibility basis the modify-criterion already used, producing the v2 half-application defect (the B-1 ADR §8→§9 renumber read MINOR by §H and MAJOR by the unchanged structural trigger). Correcting the proxy to its actual intent resolves the contradiction and unifies the section.
> **Relation to R037.** Refines R037's "semantic-effect-not-bytes" principle from the consolidation sub-case to all of §4.6. Does **not** amend R037 (frozen, DIRECTIVE-031 §31.7); a new forward-trail ruling cross-referencing it.
> **Anchors.** DMS §4.6; HEB-38 Phase-1 Pass-2 (B-1 / P2-B1); refines R037.

*(Ledger schema fresh-fetched from DIRECTIVE-031 §31.2 at ledger-authoring per §0.5; provisional ID R040, sequenced against the authoring rulings when the full Phase-1 ledger is written.)*

---

## B. Surface 1 — DMS §7.4–§7.9

*Spine §7.5/§7.6/§7.7/§7.8 unchanged from v2 (Pass-2-verified). §7.4 and §7.9 carry one cosmetic each (marked).*

#### 7.4 Contract-Purity — the one-home rule for normative bodies

§7.2–§7.3 keep *norms* out of operational documents. This subsection is the converse: it keeps *operational substrate* out of normative bodies. A normative body states the contract and its binding boundaries — and nothing else; §7.7 gives the operative test.

**The rule.** Every fact has exactly one home. Within a normative body, an inline reference may point only at **co-traveling normative corpus** — another governance standard or decision record (ADR/DDR/SDD/ENG-STD) or a section cross-reference (`§X.Y`) — or at the document's own audit surfaces as a relocation pointer (to its §7.5 cross-reference home or its Change Log). Operational substrate itself MUST NOT appear inline in a normative body: ruling-ledger identifiers (`R{N}`), tracker identifiers (`{{TRACKER_PREFIX}}-NN`), review-finding identifiers (`B-N`/`M-N`), and review / session / debate narrative — illustrative of the prohibited class, not an exhaustive list. Its one home is an append-only audit surface (§7.5).

**Accepted residual.** Version→decision traceability is retained — the Change Log names the ticket that drove each version. Clause→decision traceability is let go: the body does not preserve which ruling drove which clause.

*(§7.5, §7.6, §7.7, §7.8 — unchanged from v2; reproduced in the v2 bundle §B. §7.6 "edge-case handling"; §7.7 close grounds cross-ref integrity in the DIRECTIVE-029 audit; §7.8 two-gate model on "each normative body section".)*

#### 7.9 Consolidation cadence

*(Prevention / Remediation / Baseline / No-sweep legs unchanged from v2, plus the SA-4 cosmetic note on the Baseline leg:)*

- **Baseline (one-time, per document).** …recorded by the `## Change Log` row that amendment writes, whose Change text names it as the contract-purity baseline… **A document in reduced-snapshot form (DMS §2.3.4) carries no Change Log; its baseline marker is first written when it transitions to full form at its governance-owner amendment.** A document whose Change Log carries the baseline row is past its baseline.

---

## C. Surface 2 — DMS §4.6 (v3 — unified on SemVer-compatibility; FULLY REWRITTEN, primary Pass-3 target)

> ### 4.6 Scope Discipline at Document Amendment Authoring
>
> Document amendments scoped as MAJOR / MINOR / PATCH MUST be evaluated against SemVer criteria at PR-create time. The tiers key on **SemVer-compatibility** — whether the change breaks a downstream reference or makes a prior-conformant artifact non-conformant — not on whether existing bytes or structure changed:
>
> - **PATCH** — word-level corrections; version-pin updates; cross-reference fixes; typographical changes; content-preserving consolidation (§7.4: relocating operational references and lineage to their §7.5 audit-surface home, folding redundant restatement) as standalone cleanup; no semantic shift.
> - **MINOR** — new content additions; backward-compatible modification of existing content, **including reference-preserving structural reorganization or section renumbering**: any change that breaks no downstream reference and makes no prior-conformant artifact non-conformant.
> - **MAJOR** — any SemVer-incompatible change: a modification, structural reorganization, section renumbering, or canonical-pattern change **that breaks a downstream reference or makes a prior-conformant artifact non-conformant**.
>
> If during authoring the scope expands beyond the labeled tier, the PR MUST be split or re-labeled before merge. Retrospective reclassification ("this should have been MAJOR after the fact") is a known anti-pattern.
>
> The author at PR-create time evaluates the scope against the criteria above. Three-hat review verifies the evaluation. **Disagreement during three-hat review on scope tier is itself the trigger to split or re-label.**
>
> **Application examples:**
> - *PATCH:* Refresh a stale cross-reference (e.g., "SDD-NNN v1.0.0 §6" → "v1.1.0 §6"); fix a typo; update a service hostname.
> - *PATCH (standalone consolidation):* evict process-narrative and relocate ledger/ticket identifiers from a decision-record body to its Change Log and References, preserving every normative claim — content-preserving, reference-neutral.
> - *MINOR:* Append a new section subsection; codify a new directive without modifying existing directive text; add a section and renumber a reference-preserving tail section (e.g., seating a Cross-References section ahead of a Change Log that nothing cites by number).
> - *MAJOR:* Embed a new canonical pattern that supersedes existing patterns (prior-conformant docs become non-conformant); restructure a layout tree that breaks existing import paths; renumber sections that are cited by number elsewhere.
>
> **Split-or-relabel triggers during authoring:**
> - A MINOR amendment **requiring** modification that breaks downstream references or makes a prior-conformant artifact non-conformant → split: the breaking modification lands as a separate MAJOR amendment; the additive content lands as MINOR. *(Reference-preserving change is not such a modification. Content-preserving consolidation per §7.4 rides with the MINOR work or stands alone as PATCH; reference-preserving structural reorganization or renumbering is MINOR, whether standalone or riding.)*
> - A PATCH amendment **carrying** a substantive (semantic) content change → relabel to MINOR — or to MAJOR if the change also breaks references or makes a prior-conformant artifact non-conformant.
> - A MAJOR amendment **narrowing** to reference-preserving content → relabel down to MINOR.
>
> The split-or-relabel decision happens **before merge**, not after.

**Self-classification (Pass-3 check):** the §4.6 rewrite is itself an existing-content modification. It loosens classification (reference-preserving structural change becomes MINOR-eligible), breaks no downstream reference, and makes no prior-conformant artifact non-conformant → it classifies **MINOR** on the invariant compatibility property. The ADR §8→§9 renumber is reference-preserving (grep-confirmed nothing cites ADR §8) ⇒ backward-compatible ⇒ **MINOR** — grounded on that same invariant property, not by applying §4.6's new text to itself.

---

## D. Surface 3 — CSD DIRECTIVE-007 §7.2 remedy axis

*Unchanged from v2 (Pass-2-verified). Remedy axis (add/fix vs remove/relocate, orthogonal to severity, names destination) + reconciling clause (destination-naming is finding-metadata, not relocation, per -032 §32.3). Reproduced in v2 bundle §D.*

---

## E. Surface 4 — review-template §2

*Unchanged from v2 (Pass-2-verified), with the Pass-4 positive-finding reconcile. `**Remedy:**` field first-line in the structured finding block; trailing tag on §2.3 cosmetic bullets; §2.4 positives default to remedy `none` (CSD §7.2) and carry no explicit tag; §2 content-contract. Reproduced in v2 bundle §E.*

---

## F. Surface 5 — content-contract instances

*ADR `## Cross-References` (§8, renumber §8→§9 Change Log) + ADR/DDR/SDD contracts + §F.0 exclusions + F.1 pre-promotion line — all unchanged from v2 (Pass-2-verified), except the one cosmetic:*

### F.2 ADR `## 8. Cross-References` — cosmetic applied

> - *Engineering standards this ADR depends on, constrains, or amends*
> - *The grounding deliberation artifact (ruling-rationale ledger entry / scoping handoff) per DIRECTIVE-034 — the single home for the "why," referenced here rather than replayed in §3*
> - ***§6 Compliance backlog items*** *(was: "Backlog items tracking §6 compliance conditions")*

---

## G. Cross-reference map — CSD→DMS row added (cosmetic)

*v2 §G unchanged except the added row:*

| From | → Target | Status | Claim |
|---|---|---|---|
| **CSD DIRECTIVE-007 §7.2 (remedy block)** | **DMS §7.4 / §7.5** | **[new, forward-ref]** | **the doesn't-belong-content definition + destination surface; the dependency SA-1 atomic-landing protects (land DMS+CSD together)** |
| *(all v2 §G rows unchanged)* | | | |

---

## S. §4.12 cascade + frontmatter form (CONFIRMED this session)

- **In-repo cascade: empty (confirmed).** No corpus document carries a populated `governing_standards:` pin; the DMS/CSD bumps trigger zero in-repo pin refreshes. Both Pass-2 passes grep-confirmed.
- **Both DMS and CSD are reduced-snapshot form (live-verified).** Headers carry `# File:`/`# Author:`/`# Description:` only; frontmatter `doctype` + `version` only; no `## Change Log`, no `last_updated`/`# Revised:`. The DMS ends at §9 + terminator (its 32 `## Change Log` grep hits are all convention-defining prose); the CSD has zero.
- **Consequences for the apply-prompt manifest:** the version-bearing surface set for each doc is **the YAML `version:` field** (plus any Document-Metadata version *pointer* cell, prose-only per §2.2 rule 6). **No atomic-refresh pairs apply** (no Change Log / `last_updated` / `# Revised:` to pair) unless this cycle transitions the docs reduced→full — an **operator fork** (DMS §2.3.4 "amended at governance-owner layer acquires full form" vs. the docs' established reduced state at 3.1.0). Resolved at apply-prompt authoring; does not affect the doctrine text.
- **DMS↔CSD coupling is body cross-references** (the §G CSD→DMS row), handled by **atomic landing (SA-1)**, not pins.

---

## H. Version / tier classification (v3 — grounded in unified §4.6)

| Document | Current | Proposed | Tier | Rationale |
|---|---|---|---|---|
| DMS | 3.1.0 | 3.2.0 | MINOR | §7.4–§7.9 additive. The §4.6 rewrite unifies the tiers on SemVer-compatibility — a backward-compatible loosening (reference-preserving structural change becomes MINOR-eligible; nothing previously MINOR becomes MAJOR; no prior-conformant artifact becomes non-conformant) — so it classifies MINOR on the compatibility principle itself, not by applying its own new text to itself. The ADR `## Cross-References` + §8→§9 renumber is reference-preserving (grep-confirmed: nothing cites ADR §8 numerically) → MINOR under the unified §4.6. |
| CSD | 3.1.0 | 3.2.0 | MINOR | DIRECTIVE-007 §7.2 gains the orthogonal remedy axis + reconciling clause; severity vocabulary untouched; additive, backward-compatible. |

*Templates change as part of the DMS cycle (no independent version). Kit VERSION bump, the §4.12 PreFlight (§S — empty), atomic DMS+CSD landing (SA-1), and the reduced-vs-full fork are apply-prompt concerns.*

---

*End of v3 Pass-3 convergence-close review-target bundle.*
