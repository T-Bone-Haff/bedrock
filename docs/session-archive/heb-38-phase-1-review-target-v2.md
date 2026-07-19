# HEB-38 Phase-1 — Contract-Purity Doctrine — Review-Target Bundle (v2, Pass-2)

## 0. Orientation

This is the **v2 (post-disposition) review target** for the **Pass-2** three-hat and
antagonistic verification round (DIRECTIVE-032 §32.4: verify prior-pass findings are
resolved **and** surface fix-induced drift / new findings).

It differs from v1 in two ways: **§R** below is a disposition-resolution record (the v1
findings + how each was resolved, for verification), and the converged surfaces in §B–§F
carry every ratified fix. The conformance baseline (R032–R039) and bundle conventions are
unchanged from v1; the cross-reference map (§G) and tier table (§H) are updated.

**Baselines.** HE-Bedrock `main @ 49b4c17a`; kit VERSION 2.3.0; corpus tag `v2.3.0`.
Proposed: **DMS 3.1.0 → 3.2.0 (MINOR)**; **CSD 3.1.0 → 3.2.0 (MINOR)**.

**Surfaces under review (v2):** DMS §7.4–§7.9; DMS §4.6 retune; CSD DIRECTIVE-007 §7.2
remedy axis; review-template §2 render; ADR/DDR/SDD content-contracts **+ a new ADR
`## Cross-References` section** (B-1 resolution).

---

## R. Disposition-resolution record (v1 → v2)

*Pass-1 returned 1 BLOCKING + a finding cluster across two independent passes
(three-hat + antagonistic). All were dispositioned and ratified; resolutions below.
Pass-2 verifies each resolution and checks for fix-induced drift.*

| v1 finding (source) | Disposition | Resolved in |
|---|---|---|
| **B-1** BLOCKING — ADR content-contracts route to a `References` surface the ADR lacks *(antag)* | **Path (a):** add `## Cross-References` to ADR template; route contracts there | §F.2 (new ADR §8) + §B.1 note |
| **§4.6 self-classification** *(antag M-1 / three-hat SA-3, EA-2)* | **Clarifying reframe:** MINOR keys on SemVer-compatibility (backward-compatible modification admitted); landing edit = MINOR; bounded self-application precedent → ledger | §C.2 (MINOR bullet) + §H |
| **DIRECTIVE-029 mischaracterized** *(three-hat M-1, EA-4)* | Reword §7.7 close + §7.9 no-sweep to 029's actual audit role; drop "propagates"; skill-refresh stays Phase-2, unnamed in-body | §B (§7.7, §7.9) |
| **Remedy render incomplete** *(antag M-2 / three-hat M-3)* | Add `**Remedy:**` field to structured finding block + tag to §2.3/§2.4 bullets | §E |
| **DDR coverage gap** *(antag M-4 / three-hat M-2, SA-2)* | §7.8 "each section"→"each normative body section" + exclusion clause; §F-intro names the two DDR annotation sections as excluded | §B (§7.8), §F-intro |
| **§4.12 mis-cite** *(three-hat M-4 / antag C-2)* | Drop "refreshed in place per §4.12" from §7.5; remove 2 spurious §G rows | §B (§7.5), §G |
| **Pre-promotion self-check** *(antag M-3)* | Add whole-doc draft→PROPOSED self-check distinct from per-addition test | §B (§7.8), §F.1 |
| **"name the destination" vs -032** *(antag C-3)* | Reconciling clause: destination-naming is finding-metadata, not relocation | §D (§7.2 tail) |
| **§6.2 mislabel** *(three-hat C-1)* | "decision tree" → "edge-case handling" | §B (§7.6) |
| **§A non-verbatim** *(antag C-1 / three-hat EA-1)* | Review-of-record points to the frozen Notion ledger, not a reproduction (doctrine-consistent) | §A note below |
| **M-5** -032 inheritance *(three-hat)* | **Left -032 untouched** — §7.2-canonical inheritance (same mechanism as severity); -032 back-pointer deferred (optional) | no change (ratified) |
| **EA-3** six-class taxonomy *(three-hat)* | Linear-trail disposition ("taxonomy subsumed into §7.7 test"); **pending ratification before posting** | trail action (not text) |
| **SA-1** §4.12 cascade *(three-hat / my own)* | **Preliminary run — see §S.** Cascade empty in-repo; defers to apply-prompt PreFlight | §S |
| **SA-4 / DIR-023 surface-scoping** *(antag §3)* | Phase-2/Phase-3 forward-pointers (heavy-doc baseline set; skill re-vendor; surface-scoped grep) | forward (not text) |

**Cross-pass complementarity (v1):** the antagonistic pass alone caught the BLOCKING
(B-1); the three-hat pass alone caught the 029 mischaracterization; both independently
cross-confirmed §A / DDR-coverage / remedy-render. Spine confirmed sound by both.

---

## A. Conformance baseline — Phase-0 rulings R032–R039

*The frozen Phase-0 ledger (Notion `389caeea-1325-81f6-bdb5-d30e2a3c4cd0`) is the
authoritative conformance baseline. **Per v1 finding C-1/EA-1, this bundle does not
reproduce the ruling text** (the v1 reproduction was abridged while labeled verbatim —
the doctrine's own failure mode). Reviewers read R032–R039 from the frozen ledger
directly; the review-of-record will reference it by pointer, not reproduction.*

Ruling-to-surface map (which surface implements each ruling) is unchanged from v1:
R032/R033 → §7.4/§7.5; R034 → §7.6; R035 → §7.7; R036 (authoring) → §7.8 + §F; R036
(review) → §D + §E; R037 → §C; R038 → §7.9. R039 DMS-homing → §7; R039 CI/refresh →
Phase-2.

---

## B. Surface 1 — DMS §7.4–§7.9 (converged v2)

#### 7.4 Contract-Purity — the one-home rule for normative bodies

§7.2–§7.3 keep *norms* out of operational documents. This subsection is the converse: it keeps *operational substrate* out of normative bodies. A normative body states the contract and its binding boundaries — and nothing else; §7.7 gives the operative test.

**The rule.** Every fact has exactly one home. Within a normative body, an inline reference may point only at **co-traveling normative corpus** — another governance standard or decision record (ADR/DDR/SDD/ENG-STD) or a section cross-reference (`§X.Y`) — or at the document's own audit surfaces as a relocation pointer (`see Cross-References`, `per the Change Log`). Operational substrate itself MUST NOT appear inline in a normative body: ruling-ledger identifiers (`R{N}`), tracker identifiers (`{{TRACKER_PREFIX}}-NN`), review-finding identifiers (`B-N`/`M-N`), and review / session / debate narrative — illustrative of the prohibited class, not an exhaustive list. Its one home is an append-only audit surface (§7.5).

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
- **Baseline (one-time, per document).** A document predating this discipline gets a whole-document de-cruft on its **first substantive touch** — reformed once against §7.4–§7.8. The baseline pass is recorded by the `## Change Log` row that amendment already writes, whose Change text names it as the contract-purity baseline; that row is the durable marker, on the §12.10 grandfather-until-touched model. A document whose Change Log carries the baseline row is past its baseline — subsequent touches owe only touch-time remediation, not re-baselining.
- **No periodic sweep.** There is no calendar-driven corpus sweep — a scheduled obligation is the failure mode that quietly stops firing. Whole-corpus residual is surfaced by the DIRECTIVE-029 governance-maintenance audit at its existing triggers (a governance-document amendment is one), not by a new standing cadence.

---

## C. Surface 2 — DMS §4.6 (converged v2)

*Existing §4.6 verbatim is in v1 §C.1 (unchanged, byte-confirmed by both passes); only
the converged result is reproduced here. v2 change vs v1: the **MINOR** bullet now keys
on SemVer-compatibility (resolves the self-classification gap).*

> - **PATCH** — word-level corrections; version-pin updates; cross-reference fixes; typographical changes; content-preserving consolidation (§7.4: relocating operational references and lineage to their §7.5 audit-surface home, folding redundant restatement) as standalone cleanup; no semantic shift.
> - **MINOR** — new content additions; backward-compatible modification of existing content — content-preserving consolidation (§7.4) riding with an addition, or any other modification that breaks no downstream reference and makes no prior-conformant artifact non-conformant; no structural reorganization.
> - **MAJOR** — structural reorganization; section renumbering; canonical-pattern embedding; SemVer-incompatible changes; existing content modified in ways that break downstream references.
>
> *(Application examples + split-or-relabel trigger list unchanged from v1 §C.2: the new PATCH standalone-consolidation example; the three parallelized triggers with the §7.4 consolidation carve on bullet 1. Heading + lead paragraph untouched.)*

**Self-classification check (resolves antag M-1):** the §4.6 landing edit modifies existing rule text (the MINOR bullet) but is backward-compatible — it loosens classification, breaks no downstream reference, and makes no prior-conformant amendment non-conformant. Under the reframed MINOR criterion it classifies as **MINOR** by §4.6's own text; the bootstrap resolves consistently (loosening MINOR is itself backward-compatible). The bounded self-application precedent is recorded in the ledger (see §H).

---

## D. Surface 3 — CSD DIRECTIVE-007 §7.2 remedy axis (converged v2)

*Folds in after the "Finding-severity vocabulary lock-in" block. v2 change vs v1: the
reconciling tail clause (resolves antag C-3).*

**Remedy axis (orthogonal to severity).** Every finding additionally carries a **remedy tag** naming what the finding asks for:

- **add/fix** — the body is under-specified or wrong; the remedy adds or corrects content.
- **remove/relocate** — the body carries content that does not belong in it (process narrative, restatement, an operational reference per DMS §7.4); the remedy evicts it to its audit-surface home or deletes it. A remove/relocate finding **MUST name the destination** (the §7.5 surface it moves to, or an explicit delete) — never a bare "remove this."

The axis is **orthogonal to severity**: a remove/relocate finding can be MATERIAL or COSMETIC just as an add/fix finding can. The two are independent axes, not a combined scale — which is why remedy is a tag, not a fifth severity tier.

The remedy axis makes the review loop **subtractive as well as additive**: a review pass that only ever adds content to the body accretes cruft by construction (DMS §7.4). Tagging every finding forces the reviewer to ask, per finding, whether the body should *grow* or *shrink* — the standing generalization of a one-off subtraction pass into every review cycle. Applies to every review type that produces findings (three-hat, antagonistic, conformance, pre-BUILD), via whatever surface that review records findings on.

Naming the destination is **finding-metadata** — where the content belongs; it does not perform the relocation, which returns to the work session per the finding-disposition model (and, for antagonistic review, DIRECTIVE-032 §32.3 verification-only).

---

## E. Surface 4 — review-template §2 (converged v2)

*v2 change vs v1: the remedy tag now lands in the structured finding block and the
bullet formats authors actually fill in (resolves antag M-2 / three-hat M-3), not only
the prose enumeration.*

### E.1 §2-head note (new)

> Findings carry two independent axes: **severity** (the §2.1–§2.4 subsection they fall under) and **remedy** (add/fix vs. remove/relocate, per DIRECTIVE-007 §7.2, tagged inline on each finding). Severity sets urgency; remedy sets direction. A remove/relocate finding names where the content goes.

### E.2 Structured finding block (§2.1 / §2.2) — gains a Remedy field as its first line

```
#### Finding B-1: {{summary}}

**Remedy:** {{add/fix | remove/relocate (→ destination surface)}}
**Location:** `{{file:line}}` or `{{file §X.Y}}`
**Description:** {{What the finding is. Specific.}}
**Why blocking:** {{Why this can't be deferred.}}
**Disposition:** {{Fix in this PR / fold into Commit N / ...}}
```

### E.3 Bullet formats (§2.3 COSMETIC / §2.4 positive) — gain a trailing tag

```
- {{finding}} — {{location}} — {{add/fix | remove/relocate (→ destination)}}
```

### E.4 §2 content-contract (new HTML comment under the §2 heading)

```
<!-- Contract — holds: dispositioned findings by severity (§2.1–§2.4), each carrying
its remedy tag (DIRECTIVE-007 §7.2). Not: the corrective content itself (→ the artifact
under review); review-process meta-narrative beyond finding disposition. -->
```

---

## F. Surface 5 — content-contract instances (converged v2)

*v2 changes vs v1: (1) a new ADR `## Cross-References` section (B-1 path a); (2) ADR
content-contract routing → Cross-References; (3) §F-intro exclusion completed to name
the two DDR annotation sections; (4) F.1 header gains the pre-promotion line.*

### F.0 Exclusion scope (completed)

Content-contracts cover **normative body sections only**. Excluded, with reason: the
metadata table, `## Change Log`, and the cross-reference home (`## Cross-References` /
`References` row) — audit/structural surfaces governed at §2.3.1 / §7.5; the
in-document review record (ADR §7 Review and Approval, SDD §9 Architecture Review) —
the sanctioned relocation target for review content, not a body section; and **optional
navigational/dependency annotations** — specifically the DDR's `## Layer-of-abstraction
note` and `## Substrate-stability tracking`, which are cross-reference-adjacent (they
declare layer and cross-DDR dependency, not contract substance) and excluded on the same
basis as the cross-reference home.

### F.1 Shared `AUTHORING GUIDANCE` header addition (v2)

> CONTENT-CONTRACTS (DMS §7.8). Each normative body section carries a one-line content-contract naming what it holds and where out-of-contract content goes. Before adding to any section, run the DMS §7.7 contract-purity test: does this line state contract-or-boundary content a stranger could build from, or audit-surface content (ledger `R{N}` / tracker IDs / review narrative) that belongs in the Change Log, Cross-References, or the ledger? Audit-surface content relocates — it does not live in the body. **At the draft→PROPOSED boundary, run the test once across the whole document as a pre-promotion self-check.**

### F.2 ADR template — NEW `## Cross-References` section (B-1 path a)

Inserted after §7 Review and Approval; **existing §8 Change Log renumbers to §9**:

```
## 8. Cross-References

*The section that makes the ADR navigable and gives relocated provenance a home. Link to:*
- *Downstream DDRs and SDDs that implement this ADR*
- *Sibling or superseded ADRs this one coordinates with or replaces*
- *Engineering standards this ADR depends on, constrains, or amends*
- *The grounding deliberation artifact (ruling-rationale ledger entry / scoping handoff) per DIRECTIVE-034 — the single home for the "why," referenced here rather than replayed in §3*
- *Backlog items tracking §6 compliance conditions*
```

ADR content-contracts (routing updated to the new surface):

```
## 2. Decision
<!-- Contract — holds: the decision + testable sub-decisions. Not: rationale (→ §3); rejected alternatives (→ §4); any ledger/ticket/finding reference (→ Change Log / Cross-References). -->

## 3. Rationale
<!-- Contract — holds: what becomes true after the decision — the affirmative case, in the author's own voice. Not: defense against alternatives (→ §4); inline R{N}/tracker/finding IDs or review narrative (name the grounding ledger once in Cross-References). -->
```
*(§1 Context, §4 Alternatives, §5 Consequences, §6 Compliance contracts unchanged from v1 §F.2.)*

### F.3 DDR template

Contracts unchanged from v1 §F.3 (Decision / Rationale / Substantive Design / Conditions / Migration). The two previously-unaddressed sections are now **named exclusions** in §F.0, not gaps.

### F.4 SDD template

Unchanged from v1 §F.4 (§1–§8, §10, §11 contracts).

---

## G. Cross-reference map (v2 — spurious §4.12 rows removed)

*Changes vs v1: the two `→ §4.12` rows are deleted (the §7.5 §4.12 cite was dropped);
ADR routing now resolves to the new `## Cross-References`.*

| From | → Target | Status | Claim |
|---|---|---|---|
| §7.4 | §7.2–§7.3 | [existing] | the converse rule it builds on |
| §7.4 | §7.7, §7.5 | [new] | the test; the audit-surface home |
| §7.5 | §7.4, §4.6, §4.1 | [new]/[existing] | one rule / two surface-types; fold-in mandate |
| §7.6 | §1.2, §1.3, §6.2, §2.4 | [existing] | jurisdiction; generated-artifact exclusion; edge-case routing; governance-class boundary |
| §7.6 | ENG-STD-001/-002/-003 | [existing] | artifact-class ownership / analogue routing |
| §7.7 | §7.4, §7.5 | [new] | rule operationalized; relocation home |
| §7.7 | DIRECTIVE-029 | [existing] | cross-reference integrity via the maintenance audit |
| §7.8 | §7.7, §7.5, §2.3.1 | [new]/[existing] | the test delivered; relocation home; excluded-surface governance |
| §7.9 | §7.7, §7.8, §4.6, §2.4 | [new]/[existing] | prevention surfaces; semantic-effect classification; trivial-touch carve-out |
| §7.9 | ENG-STD-001 §12.10, DIRECTIVE-029 | [existing] | grandfather model; residual surfaced by the maintenance audit |
| §4.6 (PATCH/MINOR) | §7.4, §7.5 | [new] | content-preserving consolidation + home |
| DIR-007 §7.2 (remedy) | DMS §7.4, §7.5 | [new] | doesn't-belong content; destination surface |
| DIR-007 §7.2 (remedy) | DIR-032 §32.3 | [existing] | verification-only reconciliation |
| Review template §2 | DIR-007 §7.2 | [new in CSD] | the axis it renders |
| Content-contracts | §7.7, §7.8, §2.3.1 | [new]/[existing] | test + rule; excluded-surface governance |
| ADR contracts | ADR §8 Cross-References | [new in ADR template] | relocation home for ticket/ledger provenance |

---

## S. SA-1 — §4.12 consumer-pin cascade sizing (preliminary)

*Run design-side against the attached corpus; definitive enumeration defers to the
apply-prompt §4.12 PreFlight against live repo state.*

- **In-repo cascade: empty.** Every HE-Bedrock corpus document ships in **reduced
  consumed-snapshot frontmatter** (`doctype` + `version`; eng-stds + `document_id`).
  **No document carries a populated `governing_standards:` pin** — all corpus occurrences
  of the token are prose defining/referencing the convention. The DMS and CSD bumps
  trigger **zero in-repo pin refreshes**.
- **DMS↔CSD coupling is body cross-references, not pins.** CSD §7.2 → DMS §7.4 and DMS
  §7.6 → ENG-STDs are prose `§`-references, outside §4.12's YAML-pin scope. They are
  handled by **atomic landing (SA-2)** — both documents land in one PR (or sequenced)
  so neither body cross-reference dangles mid-window — not by pin-refresh.
- **Packaging PreFlight flags (apply-prompt):**
  1. **Confirm live-repo frontmatter form.** Attachments are reduced snapshots; per DMS
     §2.3.4 a doc acquires full frontmatter (`governing_standards`, `last_updated`,
     `## Change Log`) when amended at the governance-owner layer. The apply-prompt
     PreFlight must read the live DMS/CSD working copies and confirm whether this cycle
     bumps `version:` only or also transitions reduced→full (writing a `## Change Log`).
  2. **§7.9 baseline-marker dependency.** §7.9's marker is "the `## Change Log` row the
     amendment writes." This holds for the ADR/DDR/SDD family (templates carry a Change
     Log). For the consumed control-doc/eng-std snapshots, confirm the live form carries
     a Change Log before relying on the marker for those docs.
  3. **§4.10 atomic-refresh pairs** apply only if the live docs are full-form; confirm
     at PreFlight.

---

## H. Version / tier classification (v2)

| Document | Current | Proposed | Tier | Rationale |
|---|---|---|---|---|
| DMS | 3.1.0 | 3.2.0 | MINOR | §7.4–§7.9 additive; §4.6 reframe is a backward-compatible loosening (breaks no downstream reference, makes no prior-conformant artifact non-conformant); ADR-template `## Cross-References` addition + Change-Log renumber is additive/backward-compatible (nothing cites "ADR-template §8"). Classified MINOR by §4.6's own reframed text — the bounded self-application precedent (self-classifying a newly-amended criterion against its own landing amendment, permitted only when three-hat-ratified in-cycle) is recorded as an **R037-refinement ledger note**. |
| CSD | 3.1.0 | 3.2.0 | MINOR | DIRECTIVE-007 §7.2 gains an orthogonal remedy axis + reconciling clause; severity vocabulary untouched; additive, backward-compatible. |

*Templates change as part of the DMS cycle (no independent version). Kit VERSION bump,
the §4.12 PreFlight (§S — empty in-repo), and atomic DMS+CSD landing (SA-2) are
apply-prompt concerns.*

---

*End of v2 Pass-2 review-target bundle.*
