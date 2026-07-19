# File: docs/reviews/2026-06-25-heb-38-phase-2-enforcement-antagonistic-review.md
# Author: Tad Haffey — Executive Architect, Haffey Enterprises
# Created: 2026-06-25
# Description: Antagonistic review (DIRECTIVE-032) of the HEB-38 Phase-2 enforcement staging edits (heb-38-phase-2-enforcement-edits.md), prior to Phase-2 apply-prompt authoring. Gate: "Phase-2 enforcement edits are correct, complete against the ratified plan, and contract-pure before apply-prompt authoring."

# Antagonistic Review — HEB-38 Phase-2 Enforcement Staging Edits — 2026-06-25 (Pre-Apply-Prompt Gate)

| Field | Value |
|---|---|
| **Review Date** | 2026-06-25 |
| **Reviewer** | claude.ai antagonistic-review session (DIRECTIVE-032), this session |
| **Scope** | The HEB-38 Phase-2 enforcement staging file (`heb-38-phase-2-enforcement-edits.md`, Blocks 1–8) against the live HE-Bedrock corpus @ `28a496a`, the live HEB-38 Linear trail, and the Notion HEB-38 Phase-1 ruling SoR. |
| **Authority** | DIRECTIVE-032 antagonistic review; HEB-38 charter + ratified Planning deliberation (2026-06-24). |
| **Outcome** | **FAIL — gate not satisfied.** 2 BLOCKING (B-1 scope-drift, B-2 contract-purity self-violation) must resolve before apply-prompt authoring; 4 MATERIAL in-scope; 3 COSMETIC; 7 POSITIVE. All dispositions below are **proposed, pending per-item operator ratification** (no presumed alignment). |

---

**Substrate fresh-fetched this session (no recall):**
- Corpus @ `28a496a`: DMS 3.2.0 (§4.6, §7.1–§7.9), CSD 3.2.0 (DIRECTIVE-007 §7.1–§7.5.3, DIRECTIVE-023, DIRECTIVE-024 §24.1, frontmatter), ENG-STD-003 (§13.5.2, §13.5.8, §13.5.10), `review-template.md` §2, `PROVENANCE.md`, the Phase-1 R040–R042 rulings file.
- Linear HEB-38: full description + all 5 comments (trail exhausted, `hasNextPage: false`).
- Notion: HEB-38 Phase-1 ruling SoR `38acaeea-1325-815c-93ce-cc4cd3822f95` (R040–R042; max = R042).

**Disposition routing:** per DIRECTIVE-032 §32.3 these findings return to the authoring session verification-only; the reviewer does not self-fix.

---

## §1 Scope

### 1.1 In-scope

- `heb-38-phase-2-enforcement-edits.md` Blocks 1–8 — correctness of each str_replace/insert (anchor fidelity, edit-type, target), contract-purity of the committed text, versioning classification, and citation accuracy.
- Completeness of Phase-2 against the **ratified Phase-2 scope** (Planning deliberation 2026-06-24: enforcement targets #3/#4/#5/#6).
- Coherence of the new citing surfaces against DMS §7.4–§7.9 and DIRECTIVE-007 §7.2.

### 1.2 Out of scope (deliberately)

- The running grep **mechanization** (HEB-36 / Phase-2.5) — only the check-*spec* is in scope here.
- The SOFIA-Reboot cascade (Phase-3) and the skill-nudge surface (Phase-4).
- The Phase-1 landed doctrine itself (DMS §7.4–§7.9, the §7.2 remedy axis) — reviewed only where Phase-2 interacts with it.

---

## §2 Findings

<!-- Contract — holds: dispositioned findings by severity (§2.1–§2.4), each carrying its remedy tag (DIRECTIVE-007 §7.2: add/fix / remove/relocate / none-default). Not: the corrective content itself (→ the staging file under review); review-process meta-narrative beyond finding disposition. -->

Findings carry two axes: **severity** (§2.1–§2.4) and **remedy** (DIRECTIVE-007 §7.2: add/fix, remove/relocate, none). A remove/relocate finding names its destination.

### 2.1 BLOCKING findings — must resolve before Phase-2 apply-prompt authoring proceeds

#### Finding B-1: Phase-2 scope has silently drifted from the ratified plan — two enforcement targets dropped with no disposition, one Phase-1 target relabeled Phase-2

**Remedy:** remove/relocate (→ explicit disposition of #4 and #6 in the staging file scope ledger + an HEB-38 Linear trail note)

**Location:** staging file "Surfaces landed" + "Scope ledger"; vs. Linear HEB-38 Planning deliberation (2026-06-24) targets #2/#3/#4/#5/#6.

**Description:** The ratified plan assigns **Phase-2 = enforcement targets #3/#4/#5/#6**, and puts the standing review lens at **target #2 — a Phase-_1_ doctrine target** (charter gap #3 / acceptance criterion AC2). Mapping the staging file against that:

- **#3** DIRECTIVE-023 CI check → Block 2 ✓
- **#4 ship-boundary gates** (extend the DDR-001 kit-render verify-gate + author the project→product gate, a new artifact) → **absent; not in "Does NOT do"; no re-home.**
- **#5** skill-nudge → deferred to Phase-4 ✓ (stated).
- **#6 DIRECTIVE-029 skill-regen wiring** into the version-bump trigger → **absent; no re-home.**
- **#2 review lens** → lands as Block 1, but **silently relabeled from Phase-1 to Phase-2.**

#4 and #6 have fallen out of tracking across all three surfaces — the staging file's "Does NOT do" list, the Phase-1 milestone comment's "Remaining," and the Notion Phase-1 forward-pointers — none disposition them.

**Why blocking:** Phase-2 cannot be declared complete (or its apply-prompt authored as "the Phase-2 enforcement set") against the ratified plan while 50% of the ratified mechanical defense-in-depth is dropped without ratification. This is a no-presumed-alignment violation. It is sharpened by **#6 specifically**: DMS §7.7 (line 824) and §7.9 assign cross-reference integrity between citing surfaces and the canonical test to **the DIRECTIVE-029 governance-maintenance audit**. Phase-2 *adds three new citing surfaces* (§7.6→§7.7; DIRECTIVE-023→§7.4–§7.7; review-template→§7.6/§7.7) — enlarging exactly the citation web §7.9 hands to DIRECTIVE-029 — while omitting the ratified DIRECTIVE-029 wiring that keeps it coherent.

**Disposition (proposed):** Explicitly disposition #4 and #6 per-item — re-home with reason (candidate: #4 → HEB-12 render / a new ship-gate ticket; #6 → Phase-4 with the skill work) or pull into Phase-2. State in the staging file that **Block 1 completes the Phase-1 target #2 / AC2**, landed late. Ratify each disposition individually.

#### Finding B-2: The §7.6 review lens (Block 1) violates the contract-purity doctrine it enforces — it restates what it must only reference, and denies doing so in the same sentence

**Remedy:** remove/relocate (→ rewrite Block 1: strip restatement; replace with bare references to DMS §7.7 and DIRECTIVE-007 §7.2)

**Location:** staging file Block 1 (CSD DIRECTIVE-007 §7.6 NEW text) vs. DMS §7.7 (line 818 "referenced — never restated — by every delivery surface"), §7.8 (line 832), and DIRECTIVE-007 §7.2 (line 184).

**Description:** Block 1's NEW text commits two restatements into a morphing body (CSD), which is precisely the E/F-class cruft the doctrine exists to evict:

1. It paraphrases the canonical stranger-build test — *"could a competent stranger — with no tracker, ledger, or review history — build correctly from this"* — a near-verbatim restatement of DMS §7.7's *"Could a competent stranger, with no access to the tracker, the ledger, or the review history, build correctly from it?"* — **while the same sentence asserts "it does not restate the test."** Self-contradictory on its face.
2. It restates §7.2's rationale — *"the standing generalization of one-off subtraction passes… subtractive… by construction"* — which is already in DIRECTIVE-007 §7.2 (line 184: *"the standing generalization of a one-off subtraction pass into every review cycle"*).

The genuine increment §7.6 should carry is narrow and real: §7.2 governs how you *tag* a finding you already have; §7.6 makes *actively generating* per-section stranger-build findings a *standing obligation* ("by construction, not only when a reviewer happens to look"). That increment is sound and is wanted (it completes AC2). The defect is that it is buried under ~60% restatement.

**Why blocking:** This ships a doctrine self-violation into the corpus *carrier* that every consumer project will copy, and it is the canonical example future surfaces cite. The enforcement mechanism must not be the first instance of the failure it enforces against. (Note: the violation is on the *restatement / one-home* axis of §7.4, **not** the operational-substrate axis — §7.6's cross-refs are all co-traveling normative corpus and are clean.)

**Disposition (proposed):** Rewrite Block 1 to state ONLY the increment — the active, per-section, standing read obligation + destination-naming for narrative-class findings — and reference DMS §7.7 (the test) and DIRECTIVE-007 §7.2 (the subtractive-loop rationale) rather than re-explaining either. See C-1 for a numbering move (§7.2.x) that structurally reinforces this fix.

### 2.2 MATERIAL findings — in-scope fix or dispositioned

#### Finding M-1: The §7.2 / §7.6 / §7.7 surface-identity is unpinned

**Remedy:** add/fix (→ pin the relationship in Block 1; decide whether a DMS §7.7 enumeration touch is owed) — surfaces a normative-interpretation question, see §2.5.

**Location:** staging file "Surfaces landed" ("the review findings model (review lens)") vs. Phase-0 ratified design (Linear comment "(a) The lens") vs. DMS §7.7 enumeration (line 818).

**Description:** Phase-0's ratified design assigned the §7.7 *"review findings model"* delivery surface to **the §7.2 remedy axis** (landed Phase-1). The staging file re-assigns that surface to the **new §7.6 lens** without flagging the re-identification. DMS §7.7's enumeration (untouched in Phase-2) names four surfaces: content-contracts, the review findings model, the skill nudge, the CI check. So either (a) the §7.6 lens *is* "the review findings model" — then it must be reconciled with §7.2, which currently also holds that role; or (b) it is a **fifth, unenumerated surface** — then §7.7's enumeration is now incomplete and owes a one-line DMS touch that Phase-2 does not include (Phase-2 touches no DMS surface).

**Disposition (proposed):** Pin it explicitly. Recommended reading: §7.2 remedy axis = the finding-*tagging* facet; §7.6 lens = the active-*read* facet; both are facets of the single §7.7 "review findings model" surface. Whichever way ratified, decide if DMS §7.7 needs the enumeration touch (and whether that pulls a DMS edit back into Phase-2).

#### Finding M-2: The DIRECTIVE-023 check-spec (Block 2) names the prohibited identifier classes but not the use/mention boundary that keeps the spec — and DMS §7.4 — conformant

**Remedy:** add/fix (→ Block 2 surface-scoping paragraph)

**Location:** staging file Block 2 NEW bullet + surface-scoping paragraph; vs. DMS §7.4 (line 797, which inlines the same teaching tokens) and the R027 / reduced-form-absence-grep false-RED history.

**Description:** The new bullet inlines `R{N}`, `{{TRACKER_PREFIX}}-NN`, `B-N`/`M-N` as teaching tokens. The surface-scoping paragraph correctly handles *document-level* exclusions (Change Log, audit doctypes) but not *token-level* use-vs-mention. A naive grep false-REDs on §7.4's own teaching tokens **and** on this very bullet. The latent saving grace: the schematic forms (`R{N}`, `B-N`) don't match a digit-anchored matcher (`R\d+`, `B-\d+`), so a concrete-ID matcher is self-protecting — but the spec never states the matcher is concrete-ID-anchored. Given the project's documented R027 history, the implementer will hit this.

**Disposition (proposed):** State in the spec that the check matches *instantiated* identifiers (`R\d+`, `{{TRACKER_PREFIX}}-\d+`, `B-\d+`/`M-\d+`) and excludes schematic/metalinguistic mentions and the doctrine's own teaching tokens. Mechanization is HEB-36's, but the boundary belongs in the spec so it is not rediscovered as a defect.

#### Finding M-3: DIRECTIVE-024 §24.1 ↔ DMS §7.4 collision, papered over locally

**Remedy:** add/fix (→ carry-forward ruling/ticket + ratify the descriptive-reference convention as the general resolution) — surfaces a normative-interpretation question, see §2.5.

**Location:** staging file Block 2 authoring note vs. DIRECTIVE-024 §24.1 (line 488–494) and DMS §7.4 (line 797).

**Description:** §24.1's aspirational-compliance template instructs naming the backlog item ID inline (*"tracked at {{backlog item ID}}"*). The new DIRECTIVE-023 bullet + §7.4 prohibit bare tracker IDs in a normative body, and ADR/DDR/SDD bodies are morphing bodies — so §24.1's literal template now conflicts with §7.4 wherever it is applied in a morphing body. The Block 2 authoring note *correctly flags this for ratification* and dodges it via descriptive reference ("the kit-level-validator work item") — good instinct, but it resolves a doctrine-level collision locally and one-off.

**Disposition (proposed):** Surface the §24.1↔§7.4 collision as its own carry-forward (candidate ruling, or HEB-39-adjacent), and ratify the descriptive-reference convention as the *general* resolution rather than a per-edit dodge. The descriptive-reference choice itself is a clean dogfood of the doctrine and should be kept — but explicitly, not implicitly.

#### Finding M-4: The versioning rationale is the right answer for the wrong reason

**Remedy:** add/fix (→ staging file "Versioning rationale" block)

**Location:** staging file "Versioning rationale (MINOR, R040)" vs. DMS §4.6 (line 613) + §7.9 (line 840 grandfather-until-touched).

**Description:** "No prior-conformant artifact becomes non-conformant" is **false on its face** for the new DIRECTIVE-023 check — a pre-existing ADR carrying inline `R040` in its body becomes non-conformant the moment the check exists. MINOR is the correct classification, but only because (a) the check is aspirational / not-yet-enforced and (b) DMS §7.9 grandfathers pre-existing documents until first substantive touch. The rationale asserts a falsehood instead of citing the §7.9 baseline model that actually rescues the MINOR call.

**Disposition (proposed):** Replace the "no prior-conformant artifact becomes non-conformant" claim with the §7.9 grandfather-until-touched basis (+ aspirational-status note). The doctrine being landed is what justifies the version — cite it.

### 2.3 COSMETIC findings — noted

- **C-1 — §7.6 coordinate collision.** CSD DIRECTIVE-007 §7.6 now collides in topic-space with **DMS §7.6** ("Scope — the jurisdiction discriminator"), which sits *inside* the §7.4–§7.9 contract-purity block — both contract-purity-topical. No bare cross-doc `§7.6` cite exists today (verified corpus-wide), so the prefix convention holds and this is navigable. *Consider* numbering the lens as a sub-section of §7.2 (e.g., §7.2.x) — co-locates it with the remedy axis it extends, dodges the collision, **and** structurally reinforces the B-2 one-home fix. — staging file Block 1 — remedy: none required (flag for consideration).
- **C-2 — "re-anchor per §13.5.10" is a mis-cite.** Authoring-time re-anchoring (main moved since this staging capture) is **§13.5.2**'s job; §13.5.10 is the *execution-time* temporal-coordinate gate (a Phase-0 Claude-Code beat). Scaffolding-only (anchor-fidelity note, not committed text). — staging file "Anchor-fidelity note" — remedy: add/fix the cite to §13.5.2 (or the §13.5 family). The companion "§13.5.2 step 5" cite is correct.
- **C-3 — R026 cited from recall.** "PostVerify pairs N/A per R026" — R026 is not in attached project knowledge. The underlying logic (reduced-form has no `last_updated`/Change-Log surface to pair-refresh) is self-evidently sound regardless. — staging file "Reduced-form note" / Block 3 — remedy: none (verify the R026 attribution at apply-prompt time per fresh-fetch discipline).

### 2.4 No-drift confirmations (positive findings)

- **P-1** — All str_replace OLD anchors (Blocks 2, 3, 4, 5, 6) — checked verbatim against live `28a496a`; **byte-faithful**. Anchor fidelity clean.
- **P-2** — Reduced-form CSD handling (Block 3) — checked; version-only bump correct, PostVerify atomic-refresh pairs genuinely N/A (no `last_updated` / `## Change Log` surface exists). Conformant.
- **P-3** — Block 4 (review-template §2) — checked; folding the R041 none-default correction + the lens integration into one paragraph touch correctly applies DMS §7.9 touch-time remediation. Dogfoods the doctrine; conformant. Also closes a Phase-1 §7.5.3-class multi-surface staleness (R041 landed in §7.2 but the review-template intro stayed two-way).
- **P-4** — Deferred-items list — checked against the Notion Phase-1 forward-pointers; aligns (DIRECTIVE-032→§7.2 wiring, R042 §7.8 one-liner, R040 structural-reorg lint, HEB-40, HEB-41). Conformant.
- **P-5** — Ruling-ID posture (R043-next, re-verify-at-close across repo + Notion under HEB-41 discipline) — checked; correctly provisional given the known R032–R034 cross-venue collision. R042 confirmed current Notion max. Conformant.
- **P-6** — Block 2 CI-check home (DIRECTIVE-023) and **token-only** scope — checked against the Phase-0 ratified design ("DIRECTIVE-023 token grep as CI seed; gate closes token form, review owns semantic, human owns novel"). On-plan; conformant.
- **P-7** — Block 4/5 edits to the review template — checked; introduce only co-traveling normative cross-refs (§X.Y, directive/standard refs), no operational substrate. The template touches are themselves contract-pure. §13.5.2-step-5 cite correct; all six edit-type classifications (insert / str_replace) appropriate.

### 2.5 Normative-interpretation questions (un-dispositioned → route)

- **NI-1 (from M-1):** Is the §7.7 "review findings model" delivery surface the §7.2 remedy axis, the §7.6 lens, or both as facets of one surface? Resolution may amend DMS §7.7's enumeration. → ratify in Phase-2 deliberation; if it amends §7.7, that is a DMS edit currently absent from Phase-2.
- **NI-2 (from M-3):** Does DIRECTIVE-024 §24.1's `tracked at {{backlog item ID}}` template violate DMS §7.4 when applied in a morphing body, and is descriptive reference the standing resolution? → candidate ruling; route per §3.

---

## §3 Forward-Pointer Triage

### Candidate — Phase-2 target #4 (ship-boundary gates) disposition
**Source:** Finding B-1
**Description:** Ratified Phase-2 target #4 (extend DDR-001 kit-render verify-gate + author the project→product gate) is undelivered and unhomed.
**Proposed disposition:** Re-home with ratification — candidate HEB-12 (render) or a new ship-gate ticket; or pull into Phase-2. Operator's call.

### Candidate — Phase-2 target #6 (DIRECTIVE-029 skill-regen wiring) disposition
**Source:** Finding B-1
**Description:** Ratified Phase-2 target #6 (wire skill-regen into the DMS/ENG-STD version-bump trigger) is undelivered and unhomed; load-bearing for the §7.7/§7.9 cross-reference-integrity audit that Phase-2's new citing surfaces enlarge.
**Proposed disposition:** Re-home with ratification — candidate Phase-4 (with the skill work) or a dedicated ticket. Operator's call.

### Candidate — §24.1 ↔ §7.4 collision ruling
**Source:** Finding M-3 / NI-2
**Description:** Doctrine-level collision between §24.1's ID-naming template and §7.4's bare-tracker-ID prohibition in morphing bodies.
**Proposed disposition:** Candidate ruling (R043+) and/or fold into HEB-39 (ENG-STD analogue) deliberate-first. Dedup-check first per DIRECTIVE-025.

### Candidate — contract-purity check use/mention boundary
**Source:** Finding M-2
**Description:** The check matcher must be concrete-ID-anchored and exclude teaching-token mentions.
**Proposed disposition:** Fold into HEB-36 (kit-level-validator mechanization) as a spec constraint; the boundary statement lands in DIRECTIVE-023 (Block 2) now.

### Forward-pointer triage summary

| Proposed home | Summary | Disposition |
|---|---|---|
| HEB-12 / new ship-gate ticket | Phase-2 #4 ship-boundary gates | Re-home, ratify |
| Phase-4 / new ticket | Phase-2 #6 DIRECTIVE-029 skill-regen wiring | Re-home, ratify |
| R043+ ruling / HEB-39 | §24.1 ↔ §7.4 collision | Candidate ruling, dedup-first |
| HEB-36 | Check use/mention boundary | Fold; spec note in Block 2 now |

---

## §4 Audit Outcome

> **FAIL — gate not satisfied.** 2 BLOCKING findings unresolved: **B-1** (Phase-2 scope drifted from the ratified #3/#4/#5/#6 — #4 and #6 dropped without disposition, the lens relabeled Phase-1→Phase-2) and **B-2** (the §7.6 lens restates DMS §7.7 and DIRECTIVE-007 §7.2 while claiming it does not — the enforcement edit violating its own doctrine). 4 MATERIAL findings for in-scope fix (M-1 surface-identity, M-2 use/mention boundary, M-3 §24.1↔§7.4 collision, M-4 versioning rationale); 3 COSMETIC; 7 POSITIVE no-drift confirmations. The text itself (anchors, reduced-form, carry-forwards) is clean — the blockers are scope-integrity and doctrine-coherence, both resolvable pre-apply-prompt. Convergence note: B-2, C-1, and M-1 all point at one underlying decision — whether the subtractive-review discipline lives in one home (§7.2 + a §7.2.x lens) or two (§7.2 + a new §7.6). Resolving that one item eases all three.
>
> **Gate is not satisfied for Phase-2 apply-prompt authoring** until B-1 and B-2 are dispositioned and ratified.

---

## §5 Cross-References

- **Authority:** DIRECTIVE-032 (antagonistic review); HEB-38 charter + Planning deliberation (2026-06-24).
- **Artifact reviewed:** `heb-38-phase-2-enforcement-edits.md` (Blocks 1–8).
- **Corpus baseline:** HE-Bedrock `main` @ `28a496a` (kit 2.4.0; CSD 3.2.0; DMS 3.2.0).
- **Linear:** HEB-38 (description + 5 comments, trail exhausted).
- **Notion:** HEB-38 Phase-1 ruling SoR `38acaeea-1325-815c-93ce-cc4cd3822f95` (R040–R042; max R042).
- **Disposition routing:** findings return to the authoring session verification-only (DIRECTIVE-032 §32.3); dispositions above are proposed, pending per-item operator ratification.
- **Related:** HEB-36 (validator mechanization), HEB-39 (ENG-STD analogue), HEB-40 (release-step), HEB-41 (ruling-ID registry), HEB-12 (Phase-2 render).

*End of review.*
