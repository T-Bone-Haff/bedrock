# File: (staging — downloaded to ~/Downloads/, not committed)
# Author: Claude (claude.ai authoring session 2026-06-25)
# Created: 2026-06-25
# Description: HEB-38 Phase-1 contract-purity doctrine — literal edit-blocks (the new_str / insert-payload sources) referenced by the apply-prompt §2. Each block is the exact final ratified text (v3, all cosmetics folded). Apply per the apply-prompt's str_replace instructions. This file is staging substrate — it is NOT committed to the repo.

# ============================================================================
# STAGING — HEB-38 Phase-1 doctrine edit-blocks
# Pairs with: 2026-06-25-heb-38-phase-1-contract-purity-apply-prompt.md
# ============================================================================

Each block below is delimited by `>>> BLOCK: <LABEL>` / `<<< END BLOCK`. The
apply-prompt names the str_replace anchor (old_str) and the block label whose
content is the new content. Insert-payload blocks are inserted after the named
anchor; replacement blocks replace the named anchor span in full.

---

>>> BLOCK: DMS-7.4-7.9 (insert-payload — inserted after the §7.3 closing paragraph, before `## 8.`)

#### 7.4 Contract-Purity — the one-home rule for normative bodies

§7.2–§7.3 keep *norms* out of operational documents. This subsection is the converse: it keeps *operational substrate* out of normative bodies. A normative body states the contract and its binding boundaries — and nothing else; §7.7 gives the operative test.

**The rule.** Every fact has exactly one home. Within a normative body, an inline reference may point only at **co-traveling normative corpus** — another governance standard or decision record (ADR/DDR/SDD/ENG-STD) or a section cross-reference (`§X.Y`) — or at the document's own audit surfaces as a relocation pointer (to its §7.5 cross-reference home or its Change Log). Operational substrate itself MUST NOT appear inline in a normative body: ruling-ledger identifiers (`R{N}`), tracker identifiers (`{{TRACKER_PREFIX}}-NN`), review-finding identifiers (`B-N`/`M-N`), and review / session / debate narrative — illustrative of the prohibited class, not an exhaustive list. Its one home is an append-only audit surface (§7.5).

**Accepted residual.** Version→decision traceability is retained — the Change Log names the ticket that drove each version. Clause→decision traceability is let go: the body does not preserve which ruling drove which clause.

#### 7.5 Two surface-types — morphing body vs. append-only audit surface

Reference-purity (§7.4) and consolidation (§4.6) are one rule seen from two surface-types. An operational reference is *prohibited* in a morphing body and *expected* in an audit surface — the operational reference's one home is the audit surface.

- **Audit surfaces (the operational substrate's home).** Whole operational documents — ruling-rationale ledgers, reviews-of-record, session-handoffs — plus, *within* a normative document, the `## Change Log` (append-only by rule) and the document's designated cross-reference home (`References` row / `## Cross-References` section).
- **Morphing bodies.** The normative body of an ADR/DDR/SDD, the governance corpus (the engineering standards, this strategy, the session directives) on amendment, and the canonical templates. These fold in (§4.1) and consolidate (§4.6); strict-additive does NOT apply to a morphing body.

Separating the surface-types resolves the standing tension between the §4.1 fold-in mandate and additive-only review accretion: the audit surfaces carry the append-only history; the contract bodies stay consolidated.

#### 7.6 Scope — the jurisdiction discriminator

This discipline governs the **project-authored governance and design documents under this strategy's jurisdiction** (§1.2), classified by the *what-it-is* discriminator, not by a closed list. A new doctype routes through the §6.2 edge-case handling rather than deadlocking the rule.

Out of scope: runtime and system-generated outputs (a file an application emits is a §1.3 *Generated artifact*, governed as application behavior by ENG-STD-001), and artifacts whose authoring is governed by ENG-STD-001/-002/-003. The reference-purity and consolidation analogue for shell scripts and apply-prompts falls to ENG-STD-002 and ENG-STD-003 — the standards owning those artifact classes — for separate assessment, not to this section. The boundary is the governance-class discriminator the corpus already uses (§2.4: governance-class, not file-extension, is the boundary).

#### 7.7 The contract-purity test — single canonical source

The rule of §7.4 is operationalized by one test, defined **here once** and **referenced — never restated — by every delivery surface** (the template section content-contracts, the review findings model, the authoring-skill nudge, the CI reference check):

> **Contract-purity test.** *Does this line state contract-or-boundary content — what to build and the limits to build within — or audit-surface content (what happened in a decision, a ticket, or a review)? Could a competent stranger, with no access to the tracker, the ledger, or the review history, build correctly from it?* Contract-or-boundary content stays in the body; audit-surface content relocates to its append-only home (§7.5).

Load-bearing references that *are* contract-or-boundary — upstream-authority pins, scope-routing cross-references, conformance pointers, named-gap markers — pass the test and stay.

The canonical definition lives here; every other surface cites it rather than copying it. Cross-reference integrity between those citing surfaces and this definition is maintained under the DIRECTIVE-029 governance-maintenance audit.

#### 7.8 Section content-contracts

Each canonical decision-record template (ADR/DDR/SDD) carries a **per-section content-contract** on each **normative body section** — a one-line statement of what the section holds. An authored body conforms to its template's content-contracts: content that falls outside a section's contract moves to the section that owns it, or — when it is audit-surface content — to its §7.5 home. Audit and structural surfaces (the metadata table, `## Change Log`, the cross-reference home, the in-document review record) and optional navigational/dependency annotations are not body sections in this sense and carry no content-contract (governed at §2.3.1 / §7.5).

The §7.7 test runs at two gates: **continuously**, before adding any line to a section (the content-contract names the section's scope; the test decides whether the candidate belongs in the body at all); and **once at the draft→PROPOSED boundary**, as a whole-document pre-promotion self-check across every section.

The content-contracts are the authoring-time delivery surface for the §7.7 test. They reference it; they do not restate it.

#### 7.9 Consolidation cadence

Contract-purity is maintained continuously and remediated at touch-time; it is not swept periodically.

- **Prevention (continuous).** The §7.7 test fires at every authoring, review, and CI touch of a morphing body, via its delivery surfaces (§7.8 content-contracts; the review findings model; the CI reference check).
- **Remediation (touch-time).** A substantive amendment to a morphing body consolidates what it touches in the same amendment — now classified by semantic effect per §4.6, so consolidation no longer forces a MAJOR split. Trivial touches (typo, pin-bump, formatting) carry the §2.4 / ENG-STD-001 §12.10 carve-out and trigger no consolidation.
- **Baseline (one-time, per document).** A document predating this discipline gets a whole-document de-cruft on its **first substantive touch** — reformed once against §7.4–§7.8. The baseline pass is recorded by the `## Change Log` row that amendment writes, whose Change text names it as the contract-purity baseline; that row is the durable marker, on the §12.10 grandfather-until-touched model. A document in reduced-snapshot form (§2.3.4) carries no Change Log; its baseline marker is first written when it transitions to full form at its governance-owner amendment. A document whose Change Log carries the baseline row is past its baseline — subsequent touches owe only touch-time remediation, not re-baselining.
- **No periodic sweep.** There is no calendar-driven corpus sweep — a scheduled obligation is the failure mode that quietly stops firing. Whole-corpus residual is surfaced by the DIRECTIVE-029 governance-maintenance audit at its existing triggers (a governance-document amendment is one), not by a new standing cadence.

<<< END BLOCK

---

>>> BLOCK: DMS-4.6 (replacement — replaces the full current §4.6 span)

### 4.6 Scope Discipline at Document Amendment Authoring

Document amendments scoped as MAJOR / MINOR / PATCH MUST be evaluated against SemVer criteria at PR-create time. The tiers key on **SemVer-compatibility** — whether the change breaks a downstream reference or makes a prior-conformant artifact non-conformant — not on whether existing bytes or structure changed:

- **PATCH** — word-level corrections; version-pin updates; cross-reference fixes; typographical changes; content-preserving consolidation (§7.4: relocating operational references and lineage to their §7.5 audit-surface home, folding redundant restatement) as standalone cleanup; no semantic shift.
- **MINOR** — new content additions; backward-compatible modification of existing content, including reference-preserving structural reorganization or section renumbering: any change that breaks no downstream reference and makes no prior-conformant artifact non-conformant.
- **MAJOR** — any SemVer-incompatible change: a modification, structural reorganization, section renumbering, or canonical-pattern change that breaks a downstream reference or makes a prior-conformant artifact non-conformant.

If during authoring the scope expands beyond the labeled tier, the PR MUST be split or re-labeled before merge. Retrospective reclassification ("this should have been MAJOR after the fact") is a known anti-pattern.

The author at PR-create time evaluates the scope against the criteria above. Three-hat review verifies the evaluation. **Disagreement during three-hat review on scope tier is itself the trigger to split or re-label.**

**Application examples:**

- *PATCH:* Refresh a stale cross-reference (e.g., "SDD-NNN v1.0.0 §6" → "v1.1.0 §6"); fix a typo; update a service hostname.
- *PATCH (standalone consolidation):* evict process-narrative and relocate ledger/ticket identifiers from a decision-record body to its Change Log and References, preserving every normative claim — content-preserving, reference-neutral.
- *MINOR:* Append a new section subsection; codify a new directive without modifying existing directive text; add a section and renumber a reference-preserving tail section (e.g., seating a Cross-References section ahead of a Change Log that nothing cites by number).
- *MAJOR:* Embed a new canonical pattern that supersedes existing patterns (prior-conformant docs become non-conformant); restructure a layout tree that breaks existing import paths; renumber sections that are cited by number elsewhere.

**Split-or-relabel triggers during authoring:**

- A MINOR amendment **requiring** modification that breaks downstream references or makes a prior-conformant artifact non-conformant → split: the breaking modification lands as a separate MAJOR amendment; the additive content lands as MINOR. *(Reference-preserving change is not such a modification. Content-preserving consolidation per §7.4 rides with the MINOR work or stands alone as PATCH; reference-preserving structural reorganization or renumbering is MINOR, whether standalone or riding.)*
- A PATCH amendment **carrying** a substantive (semantic) content change → relabel to MINOR — or to MAJOR if the change also breaks references or makes a prior-conformant artifact non-conformant.
- A MAJOR amendment **narrowing** to reference-preserving content → relabel down to MINOR.

The split-or-relabel decision happens **before merge**, not after.

<<< END BLOCK

---

>>> BLOCK: CSD-7.2-REMEDY (insert-payload — inserted after the §7.2 "Finding-severity vocabulary lock-in" paragraph, before "Out-of-scope finding routing")

**Remedy axis (orthogonal to severity).** Every finding additionally carries a **remedy tag** naming what the finding asks for:

- **add/fix** — the body is under-specified or wrong; the remedy adds or corrects content.
- **remove/relocate** — the body carries content that does not belong in it (process narrative, restatement, an operational reference per DMS §7.4); the remedy evicts it to its audit-surface home or deletes it. A remove/relocate finding **MUST name the destination** (the §7.5 surface it moves to, or an explicit delete) — never a bare "remove this."
- **none** — a no-drift confirmation (positive finding) asks for no change; there is nothing to enact. `none` is the **default**: a finding carries `none` unless it asks for an add/fix or a remove/relocate, so a positive finding need not be tagged explicitly.

The axis is **orthogonal to severity**: a remove/relocate finding can be MATERIAL or COSMETIC just as an add/fix finding can. The two are independent axes, not a combined scale — which is why remedy is a tag, not a fifth severity tier.

The remedy axis makes the review loop **subtractive as well as additive**: a review pass that only ever adds content to the body accretes cruft by construction (DMS §7.4). Tagging every finding forces the reviewer to ask, per finding, whether the body should *grow* or *shrink* — the standing generalization of a one-off subtraction pass into every review cycle. Applies to every review type that produces findings (three-hat, antagonistic, conformance, pre-BUILD), via whatever surface that review records findings on.

Naming the destination is **finding-metadata** — where the content belongs; it does not perform the relocation, which returns to the work session per the finding-disposition model (and, for antagonistic review, DIRECTIVE-032 §32.3 verification-only).

<<< END BLOCK

---

>>> BLOCK: ADR-8-CROSS-REFERENCES (replacement — replaces the anchor `## 8. Change Log` with this block followed by a renumbered `## 9. Change Log`)

## 8. Cross-References

*The section that makes the ADR navigable and gives relocated provenance a home. Link to:*
- *Downstream DDRs and SDDs that implement this ADR*
- *Sibling or superseded ADRs this one coordinates with or replaces*
- *Engineering standards this ADR depends on, constrains, or amends*
- *The grounding deliberation artifact (ruling-rationale ledger entry / scoping handoff) per DIRECTIVE-034 — the single home for the "why," referenced here rather than replayed in §3*
- *§6 Compliance backlog items*

## 9. Change Log

<<< END BLOCK

---

>>> BLOCK: TEMPLATE-HEADER-ADDITION (insert-payload — inserted into the AUTHORING GUIDANCE block of the ADR/DDR/SDD templates, immediately before the "WHAT AN ADR IS" / "WHAT A DDR IS" / "WHAT AN SDD IS" line; str_replace old_str = that line, new_str = this note + blank line + that line)

CONTENT-CONTRACTS (DMS §7.8). Each normative body section carries a one-line content-contract naming what it holds and where out-of-contract content goes. Before adding to any section, run the DMS §7.7 contract-purity test: does this line state contract-or-boundary content a stranger could build from, or audit-surface content (ledger `R{N}` / tracker IDs / review narrative) that belongs in the Change Log, Cross-References, or the ledger? Audit-surface content relocates — it does not live in the body. At the draft→PROPOSED boundary, run the test once across the whole document as a pre-promotion self-check.

<<< END BLOCK

---

>>> BLOCK: ADR-CONTENT-CONTRACTS (insert-payload — one HTML comment inserted under each named ADR heading)

## 1. Context
<!-- Contract — holds: current platform state + the forcing function (why decide now). Not: rationale (→ §3); prior-version narrative beyond what grounds the decision. -->

## 2. Decision
<!-- Contract — holds: the decision + testable sub-decisions. Not: rationale (→ §3); rejected alternatives (→ §4); any ledger/ticket/finding reference (→ Change Log / Cross-References). -->

## 3. Rationale
<!-- Contract — holds: what becomes true after the decision — the affirmative case, in the author's own voice. Not: defense against alternatives (→ §4); inline R{N}/tracker/finding IDs or review narrative (name the grounding ledger once in Cross-References). -->

## 4. Alternatives Considered
<!-- Contract — holds: each alternative described as its proponents would, + its rejection rationale. Not: the affirmative case (→ §3); review-process narrative. -->

## 5. Consequences
<!-- Contract — holds: positive consequences (§5.1), constraints imposed (§5.2), risks + mitigation/monitoring (§5.3). Not: restatement of the decision (→ §2) or rationale (→ §3). -->

## 6. Compliance
<!-- Contract — holds: how conformance is verified (mechanism, or aspirational-with-tracking pointer). Not: the decision itself (→ §2); review sign-off (→ §7). -->

<<< END BLOCK

---

>>> BLOCK: DDR-CONTENT-CONTRACTS (insert-payload — one HTML comment inserted under each named DDR heading)

## Decision
<!-- Contract — holds: the ruling + its components, stated testably. Not: rationale (→ Rationale); rejected alternatives (→ Rationale); any ledger/ticket/finding reference (→ Change Log / References). -->

## Rationale
<!-- Contract — holds: why this design and not another, in the author's own voice, including rejected alternatives. Not: inline R{N}/tracker/finding IDs or review narrative — name the grounding ledger once in References, don't replay it. -->

## {{Substantive Design Sections — variable count and shape}}
<!-- Contract — holds: the design substance — schema, boundary/gateway patterns, multi-store contracts, operational mechanics. Not: rationale (→ Rationale); process/debate narrative. -->

## Pre-Acceptance / Pre-Migration Conditions
<!-- Contract — holds: the discrete prerequisites + their tracking pointer, each stated as a buildable condition. Not: rationale for the conditions (→ Rationale). -->

## Migration Path
<!-- Contract — holds: phasing, cutover, data mechanics, rollback, decommissioning timeline. Not: rationale; status narrative. -->

<<< END BLOCK

---

>>> BLOCK: SDD-CONTENT-CONTRACTS (insert-payload — one HTML comment inserted under each named SDD heading)

## 1. Purpose
<!-- Contract — holds: what the service does + its sole-authority responsibilities + what it explicitly does NOT do. Not: how it's built (→ §5); rationale narrative. -->

## 2. What Changes from {{prior-service-name}}
<!-- Contract — holds: the prior→new comparison, one factual statement per row. Not: "same" rows (noise); migration mechanics (→ §7). -->

## 3. Responsibilities
<!-- Contract — holds: owned (§3.1) and not-owned (§3.2) responsibilities, concrete enough for a reviewer to place code. Not: API detail (→ §4); rationale. -->

## 4. API Contract
<!-- Contract — holds: endpoint shapes, request/response, auth, error + idempotency semantics. Not: internal architecture (→ §5). -->

## 5. Internal Architecture
<!-- Contract — holds: module structure, adapter pattern, pipeline/state-machine, secrets, config, readiness logic. Not: external API contract (→ §4). -->

## 6. Data Flows
<!-- Contract — holds: principal inbound/outbound flows traced entry→persistence, with side effects. Not: endpoint-contract restatement (→ §4). -->

## 7. Migration from {{prior-service-name}}
<!-- Contract — holds: phasing, data migration, rollback, verification gates, decommissioning timeline. Not: rationale. -->

## 8. Testing Requirements
<!-- Contract — holds: service-specific test discipline beyond platform defaults + coverage threshold. Not: restatement of platform testing standards — reference them. -->

## 10. ADR / DDR Compliance Checklist
<!-- Contract — holds: per-upstream-doc conformance statement (or honest non-conformance + tracking pointer). Not: the upstream requirement's full text — cite it. -->

## 11. Observability Contract
<!-- Contract — holds: structured log events, metrics, traces, retention. Not: restatement of platform logging/observability standards — reference them. -->

<<< END BLOCK

---

>>> BLOCK: REVIEW-2 (apply the review-template §2 edits below; anchors verified against the live review-template)

### EDIT A+D — under the §2 heading (one str_replace)
- `old_str`: `## §2 {{Findings}}`
- `new_str`:
```
## §2 {{Findings}}

<!-- Contract — holds: dispositioned findings by severity (§2.1–§2.4), each carrying its remedy tag (DIRECTIVE-007 §7.2). Not: the corrective content itself (→ the artifact under review); review-process meta-narrative beyond finding disposition. -->

Findings carry two independent axes: **severity** (the §2.1–§2.4 subsection they fall under) and **remedy** (add/fix vs. remove/relocate, per DIRECTIVE-007 §7.2, tagged inline on each finding). Severity sets urgency; remedy sets direction. A remove/relocate finding names where the content goes.
```

### EDIT B — `**Remedy:**` as the first field of the structured finding block
- `old_str`: ``**Location:** `{{file:line}}` or `{{file §X.Y}}` ``
- `new_str`:
```
**Remedy:** {{add/fix | remove/relocate (→ destination surface)}}

**Location:** `{{file:line}}` or `{{file §X.Y}}`
```

### EDIT C — trailing remedy tag on the §2.3 COSMETIC bullet format (positive §2.4 findings are no-drift confirmations and carry no remedy tag)
- `old_str`: `- *{{finding}} — {{location}}*`
- `new_str`: `- *{{finding}} — {{location}} — {{add/fix | remove/relocate (→ destination)}}*`

<<< END BLOCK

---

*End of staging edit-blocks.*
