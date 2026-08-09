---
name: author-decision-record
description: "Select the correct engineering decision-record type, then author, amend, or de-drift an ADR, DDR, or SDD while preserving deliberation, provenance, lifecycle metadata, and body integrity. Use when recording why an architecture or design choice was made, documenting a service design, choosing among the house doctypes, or repairing an existing ADR, DDR, or SDD. If selection identifies an implementation-complete construct spec, route its authorship or amendment to author-construct-spec. Do not use for direct construct-spec authorship, reusable standards (author-standard), implementation handoffs (author-execution-relay), product PRDs, finished-code review, or convergence review of a record set (design-review-loop)."
---

# Author a Decision Record

Four doctypes capture decisions at four altitudes. This skill routes to the right one, supplies its template, and enforces the one discipline that determines whether the record is worth anything: real deliberation behind it.

**Binding:** the house doctype family (ADR / DDR / SDD / construct spec), the `docs/adr|ddr|sdd/` homes of the first three, and the naming, status-lifecycle, and versioning conventions declared here. A different doctype family or record system is a rebind, not a line-edit; the pre-authoring deliberation gate and the body-integrity discipline are doctype-agnostic and travel with any rebind.

## The deliberation gate (read before authoring anything)

A decision record's authority comes from the thinking behind it, not the template around it. **The template gives shape; it does not give substance.** Before authoring, you need deliberation substrate to draw on — a real comparison of options, an investigation, a spike, a scoping discussion, an operator conversation that weighed the trade-offs.

If you reach the section where the *why* goes — an ADR's Rationale and Alternatives, a DDR's Rationale, an SDD's Responsibilities — and find you'd be **inventing** it from a thin prompt, **stop.** Produce the deliberation first, or mark the section as an explicit TODO with a tracking pointer and leave the record in draft. Do not fabricate.

Fabricated rationale and strawman alternatives age worse than missing ones: a future reader who discovers them stops trusting the whole document, and if a later decision reverses the call, the strawman becomes the new decision and the rejection reads as foolish. Honest "TODO — alternatives pending, tracked at X" beats a confident invention every time.

Each doctype names the specific substrate it needs in its routing entry below. That substrate requirement is the gate.

## Which doctype

Three of the four sort by altitude; the fourth sorts by consumer and is reached below. The discriminating tests:

- **ADR — a platform principle.** A commitment that constrains the architecture across services. *Test: if you deleted every service tomorrow and started over, would this still apply?* Yes → ADR. (e.g., "the graph is the system of record for all architecture state.")
- **DDR — a design ruling.** A specific data-shape, system-shape, or coordination decision, usually technology-specific. *Test: is this a technology-independent pattern (→ lean ADR) or a design specific to a chosen technology (→ DDR)? Does it constrain multiple services or the platform data model (→ DDR) or just one service's internals (→ SDD)?* (e.g., "the knowledge graph and reasoning graph share one database instance behind a gateway.")
- **SDD — a service design.** The concrete design of one service. *Test: would this design exist if you deleted this service? No → SDD.* (e.g., "knowledge-service module structure, API contract, data flows, migration path.")

**None of these?** Ask one more question before concluding the decision is too small: **is the consumer an implementer who must build this from the document alone?** If yes — a change to one construct, specified so someone can build it cold — that is a *construct spec*, and it routes to `author-construct-spec`. It is a real doctype, not a leftover.

If the answer is still no, then some decisions genuinely are too small for a record — a library choice inside one service, a config default, a retry-logic trade-off. Capture those in a code comment or the commit narrative. Don't reach for the nearest doctype just because this skill is open — over-documenting a small decision is its own failure mode.

When more than one *does* fit, author at the highest altitude the decision actually reaches, and let the lower-altitude records reference it.

**When the call is not clean, it is the operator's.** If the artifact plausibly fits two homes, or none, surface the call — with the discriminating test and the answer it gave — and stop. Do not route by default. A routing answer nobody examined is how a document ends up governed by nothing, and the failure is silent: the document looks filed.

## Routing

### ADR — `templates/adr-template.md`
- **Deliberation substrate required:** a real evaluation of alternatives — a scoping discussion with documented options, an investigation note with at least one rejected alternative and why, or a captured operator deliberation. An ADR with one alternative wasn't a real choice; go think harder.
- **Shape:** Context (current state + forcing function) → Decision (testable sub-decisions) → Rationale (the affirmative case) → Alternatives Considered → Consequences (gains / constraints / risks) → Compliance → Cross-References → Change Log.

### DDR — `templates/ddr-template.md`
- **Deliberation substrate required:** *either* a spike with empirical findings that motivate the ruling, *or* a scoping output documenting the design space and the chosen path. A DDR without empirical or deliberative grounding produces a ruling that gets amended every time reality intrudes.
- **Shape:** Decision → Rationale (empirical- or deliberation-grounded) → the substantive design sections the ruling needs (multi-store contract, spike findings, gateway/boundary pattern, schema, operational mechanics — variable) → Pre-Acceptance/Migration Conditions → Migration Path → Cross-References → Change Log.

### SDD — `templates/sdd-template.md`
- **Deliberation substrate required:** *all of* — (1) the upstream ADRs/DDRs this service implements, identified; (2) confirmation those are ACCEPTED, not still PROPOSED (designing against a moving principle produces rework); (3) either a working prior service to compare against, or a deliberation artifact establishing why this service exists as a separate concern.
- **Shape:** Purpose (sole-authority responsibilities) → What Changes from prior (if a migration) → Responsibilities (owned / not-owned) → API Contract → Internal Architecture → Data Flows → Migration (if any) → Testing Requirements → Upstream Compliance Checklist → Observability Contract → Cross-References → Change Log.

### Construct spec — `author-construct-spec` (its own `templates/construct-spec-template.md`)
- **Deliberation substrate required:** *both of* — (1) **evidence that the design was determined somewhere other than in the spec.** Two admissible forms, and which applies is a fact about the construct, not a preference: where the construct **already runs**, its *observed* behaviour — a run, a tape, a log, a reproduction, a failing test; authored from what the construct is supposed to do rather than what it does, the spec fabricates its own premise and every invariant downstream inherits it. Where the construct **does not exist yet**, the decision records that govern it plus a deliberation artifact that fixed its shape — a design session outcome, a scoping output, a spike; without the second, the Rationale is written from the prompt. (2) **the authorities it is already bound by** — upstream ADRs/DDRs/SDDs, the construct's own standing contract documents, and invariants ratified in prior specs for the same construct — identified and confirmed current, not recalled.
- **Shape:** metadata frame → Purpose and scope (problem, orientation, invariants not reopened, empirical basis) → pieces (Decision → Rationale → Amendments → Correctness invariant → Required tests) → consolidated obligations → out of scope and deferred → cross-references → Change Log (optional). Governed in full by `author-construct-spec`; this entry states the gate and the placement, not the discipline.

## Placement, naming, metadata

- **Location:** `docs/adr/`, `docs/ddr/`, `docs/sdd/` respectively.
- **Filename:** `ADR-NNN-kebab-slug.md` (prefix uppercase, number zero-padded to 3 digits, slug lowercase-kebab). Same form for `DDR-` and `SDD-`.
- **Number allocation:** next unused number in the target directory; verify uniqueness first. Numbers are never reused — a superseded record keeps its number, and the supersession is recorded in the superseding record's metadata.
- **File header + metadata table + Change Log** come pre-shaped in each template. Fill the header (`# File:` / `# Author:` / `# Created:` / `# Description:`) and the metadata table; append Change Log rows most-recent-first.
- **A Change Log row before first acceptance is one line.** Version, date, ticket, and a summary of at most 200 characters. The deliberation that produced the change — what was argued, what was refuted, who agreed — goes to the ticket. A pre-1.0 Change Log growing faster than the body is telling you the deliberation is being written into the wrong artifact. Post-acceptance rows are not retroactively bound by the cap; apply it going forward.

## Status and version

- **Status lifecycle:** `PROPOSED → ACCEPTED → SUPERSEDED`, with `REJECTED` and `DEFERRED` as terminal branches from PROPOSED. DDRs and SDDs also use `ACCEPTED-WITH-CONDITIONS` when the design is sound but blocked on prerequisites (the conditions are enumerated and tracked). Stay in PROPOSED until review clears blocking findings — don't promote to make a document "feel done."
- **Version:** `0.1.0` initial draft; `0.X.0` substantive revisions while PROPOSED; `1.0.0` first ACCEPTED; `1.X.0` material post-acceptance amendments; `2.0.0` breaking changes. Typo/format fixes within a drafting session don't bump.

## Authoring discipline (applies to all four)

- **Only include sections and sub-decisions the record actually constrains.** The template categories are illustrative, not a checklist. Omit what doesn't apply — don't write "N/A" filler. A focused 3-section record beats a padded 8-section one.
- **Be specific.** "Doesn't scale" is not a rejection rationale; "the per-record audit query exceeds 100ms p95 above 10M rows for lack of a secondary index" is. If a rejection is on preference grounds, say so honestly.
- **State decisions testably.** "Did this conform or not?" should have an answer. Definitive voice ("the platform uses X for Y"), not aspirational ("we recommend considering X").
- **Template comments come in two classes, and the difference is load-bearing.** A `FILL:` comment guides writing that section and is deleted once the section is written. A `STANDING:` comment carries a discipline that governs the record at every later amendment — Change Log ordering, version increments, the current-row rule — and is **never deleted**. Standing comments fire long after the first draft, which is exactly when a record starts drifting; a template whose guidance is deleted on first fill leaves every subsequent amendment unguided.
- **Under an empirical floor, fix the form and hold the constants.** A record written before real data exists can still fix a design's *form* — defensible from first principles, testable without data — while explicitly holding its *constants* as contested and unvalidated. Say in the document which is which. Pretending to calibrate at n=0 is the failure mode; separating what design authority settles now from what only traffic settles later is the fix.

## Body integrity (what keeps the record honest)

**Jurisdiction: doctype-independent.** This section, the amendment lifecycle below, and the cold read govern *any* durable design record — **including artifacts this skill routes away.** A routing answer is not a jurisdiction answer: ruling a document out of ADR/DDR/SDD does not rule it out of these disciplines. `author-construct-spec` instantiates three of them in construct-spec form and defers here where they diverge.

The body carries the contract and only the contract. Everything else has a dated container built for it.

- **No storytelling in the body.** Process narrative, review history, deliberation prose, and forward-speculation live in the Change Log, Cross-References, the conditions apparatus, or your tracker — never threaded through contract sections. Provenance language decays in body text: a lineage sentence that's load-bearing today is noise in three months. The test for any body sentence: *would a stranger reading this in a year need it — or just need to not be confused by it?* And know your tooling's limit: contract-purity is a **semantic** property, and any validator enforces a **syntactic** proxy — a green check clears the regex, never the convention. The gap between them is owned by review. Empirical-floor statements are the same species: honest and load-bearing at ratification time, decaying provenance in a normative body — they live in the administrative layer (the PR description, the ticket, the readiness record), never the body.
- **Point, don't mirror.** When the record needs an authority's enumerated content — a vocabulary, a taxonomy, a mapping owned elsewhere — point to the authority; don't restate it inline. An inline restatement is a standing drift surface: it goes stale the next time the authority moves, and "fixing" it by re-copying just re-plants it. (The class-level rule for any reusable artifact lives in `author-standard`; this is its decision-record-body form.)
- **Ticket identifiers have exactly four sanctioned homes:** the metadata frame, the Change Log, the conditions apparatus (pre-acceptance / migration conditions), and explicit TODO gap-markers. Contract prose never carries them. A forward reference in the body is subject-named only — genus plus what's unsettled — and the navigability lives in the opposite direction: the ticket's definition-of-done carries the obligation to come back and resolve the document's pointer. The record stays standalone-buildable; the administrative layer references the canonical layer, never the reverse.
- **Tense is earned by enforcement.** A property whose enforcing mechanism is forthcoming is stated in the conditional — "holds once Condition N lands" — with the conditions apparatus carrying the present truth. Present-voice claims about future enforcement read as false statements to every reviewer, and they cost whole finding families; nothing needs to be hidden, only phrased in the tense the facts support.
- **Status claims are earned by the trail.** "Reviewed," "ratified," "enforced," "built" — assert these only when the trail substantiates them. A posture claim the repo has overtaken (or hasn't caught up to) makes every reader and reviewer faithfully report a world that doesn't exist. Review-proposed-and-folded is not operator-ratified; keep the provenance distinct.
- **An amendment that adds a ruling updates the Decision enumeration.** Rulings enter through amendments anywhere in the record — a new clause, a widened basis, a scoping qualifier — but the Decision block is the contract's index, and a ruling it doesn't enumerate is invisible to every reader who correctly treats the enumeration as complete. The obligation attaches where a ruling *enters* the corpus: an amendment that aligns this record to a ruling adjudicated elsewhere rides that ruling's existing enumeration and owes no new line — over-enumerating an alignment as if it were an adjudication is the inverse defect.
- **Section citations are facts — fetch-verify them.** A "§2.3" typed from memory is a distinct error class: the substance right, the pointer off — and it survives review because reviewers verify the claim, not the address. Treat every §-cite as a fetch-verified fact at write time.
- **Remove, don't annotate, zero-load claims.** Annotation is the second-best tool, reserved for unreliable claims that must remain because something rests on them. Once a commitment is re-grounded on a verifiable present dependency, the historical justification is deletable, not flag-able.
- **A correction amends the clause; it never appends after it.** When a statement is wrong, rewrite the statement. Writing the correction *after* the sentence it corrects leaves the record asserting X and not-X in one contiguous passage, and every reader must work out which is live. The audit trail belongs in the version note, not in the body beside the thing it contradicts.

## The amendment lifecycle (what keeps the record honest through change)

*Doctype-independent, per the jurisdiction note above.* A record's honesty is re-earned at every amendment. These disciplines govern the change, the deferral, and the withdrawal — the moments where a well-authored record quietly goes wrong.

- **The row for the version you are authoring is not history.** Prior Change Log rows are frozen — they describe published states and are never renumbered or rewritten. The current, unpublished version's row is different: it describes a body that is still moving, and it is amended in place until that version commits. A ruling that historical rows are immutable, applied to the row you are still writing, produces a row describing a document that no longer exists.

- **A decision isn't clean until it's swept.** A conditional or environment-differentiated ruling plants "in X do A; in Y, deferred" — and every downstream document still asserting the old unconditional form is now drift; the amended record is only the head. Run the lightest coherence sweep that re-points the references before calling the decision captured.
- **Route the pin cascade; don't inline it.** When an amendment bumps this record's version, dependent records pinning the old version go stale — but re-pinning them inline contaminates the amendment's "no decision change" claim with a sprawling change-set. Leave the stale pins, drop a change-log breadcrumb ("pin cascade routed to a follow-up"), and batch the re-pins into a bounded follow-up that is explicitly pure pin-currency: MINOR bump plus change-log row, no decision, schema, or contract change.
- **Rescan your own additions against any principle the same change widens.** When you widen a disclosure by stating its membership principle, the element you're adding may itself be an instance the widened disclosure now admits — only the rescan catches it. And restate a disclosure grown by ad-hoc appends by its membership principle: that completes the current set and makes future members self-covering.
- **Every deferred obligation gets a home with a firing trigger.** "Noted for that record's next touch" is where obligations go to die. Route each deferral to a backlog item whose body names the event that re-surfaces it. At any close-out, sweep the artifacts for "next touch" / "future ruling" phrases and ask each one: what event re-surfaces you? No answer means orphan, means ticket.
- **Lock tests defend deferred rulings.** A deliberate under-enforcement whose resolution belongs elsewhere is one well-meaning refactor away from silent local resolution. Encode the deliberately-permitted shape as a conformant fixture that fails the moment someone tightens past the ratified scope — comments describe intent; lock tests defend it.
- **Document deliberate gaps as deliberate.** An intentional gap carries its reason and a revisit trigger ("Held by design"), or it is indistinguishable from an oversight — and a future maintainer will faithfully "fix" a decision that was made on purpose.
- **Durable records cite durable authorities only.** A ledger entry, a session ruling, a chat disposition may inform the amendment — that's substrate — but it cannot load-bear in the record, which outlives it. Where ephemeral reasoning is genuinely load-bearing, promote it into a durable record or restate it self-containedly; never leave the standing artifact pointing at something that dissolves.
- **Withdrawal is not erasure.** A withdrawn or superseded fact is excluded from *use* and demoted, never hard-deleted — the answer to "why is this built this way" lives in the fact as it stood at decision time. The decision→fact link must survive too: provenance that exists but can't be traversed is provenance lost.
- **Premise-changed is not decision-wrong.** A stale premise discovered mid-build routes a re-evaluation ticket; overturning canon is its own deliberation, never a side-effect of build-prep. Keep the two verdicts separate in the record — the premise's change is a fact, the decision's fate is a ruling.
- **Ratification is data, not discharge.** The record carries the *reasoning* that discharges a challenge, not the assertion that ratification happened — "it was approved" is a claim to a cold reader, not an argument.
- **Prose is the contract; illustrations are lossy.** When a simplified illustration and the mechanization that enforces the design disagree, the design's prose resolves both — verify illustrations against the prose before copying them forward.
- **Record elective ordering as elective.** Sequencing chosen by preference is written as operator-elected, with the real gate named; elective ordering written as a prerequisite manufactures a dependency that calcifies at real cost.

## The cold read (before a record is promoted)

Before promoting past PROPOSED, run the stranger test as an actual pass/fail gate, not a sentiment: *a reader with no access to your tracker, your chat history, or your memory of intent can build from this record.* Read the record cold — fresh eyes, the artifact set as the only authority. The two failure signatures to hunt: a **dangling hinge** (a cross-reference that resolves to nothing in the artifact set) and an **unsupported normative claim** (a rule stated without the reasoning that justifies it). Expand every acronym at first use — an unexpanded acronym is an open invitation for any future consumer, human or model, to invent its meaning. A sentence that reads as diary in one document may be the load-bearing hinge another leans on; only the cold, cross-document read surfaces that.
