---
name: author-construct-spec
description: "Internal engineering machinery only; product or feature requirements documents (PRDs) are explicitly outside this skill and have no Bedrock route. Use this skill to author or amend an implementation-complete construct spec for one runner, harness, instrument, pipeline, or other internal mechanism when an implementer must build it from the document alone. Never infer construct-spec ownership merely because a request says specification or requirements. Do not use for reusable standards (author-standard), finished-code review, or general architecture documentation; author-decision-record owns engineering doctype selection and integrity."
---

# Author a Construct Spec

A **construct spec** is a design document for a change to one construct — a runner, a harness, an instrument, a service's internal machinery — whose consumer is an implementer who must build that change from the document alone. Its success condition is exactly that: someone builds it cold and gets the right thing.

**Binding:** the three-actor working model — a deliberation surface that designs and authors, an executor that builds, and an operator whose per-item ratification settles each disposition — over a construct whose changes are built from documents rather than from conversation. **Not stack-bound:** these disciplines govern a spec whose target is Python, a prompt artifact, a shell script, or infrastructure alike. A materially different working model is a rebind, not a line-edit.

**The template is a carrier, not an authority.** `templates/construct-spec-template.md` restates parts of this skill so the discipline is present at the author's cursor rather than only in a document they must choose to fetch. **Where the two diverge, this skill governs** — and the divergence is a defect in the template to be fixed, not a variance to be reasoned around. Every amendment here owes the template a check in the same act; its standing comments are the copy an author is actually reading.

**The falsifier:** a construct spec that follows everything here and still cannot be built from. If that happens this skill is wrong — report it rather than working around it.

## Before authoring: read `author-decision-record`

Read its **deliberation gate**, **Body integrity**, **Amendment lifecycle**, **status lifecycle**, and **cold read** sections before drafting anything. The deliberation gate is the first of these and the one that stops a fabricated Rationale; this skill's substrate requirement lives in that skill's routing entry for the construct spec. They are doctype-independent — they govern any durable design record, **including the ones that skill routes away**, and a construct spec is one of the things it routes away. This is a read, not a citation.

**Three of its disciplines are instantiated here, in construct-spec form.** *Pointer-not-mirror* becomes the operative rule below; *provenance decays in body text* becomes step 3's routing; *citations are fetch-verified facts* becomes the artifact check. Instantiation is not replacement: **where an instantiation here and `author-decision-record` diverge, that skill governs — except where this skill declares a licensed variance, below.**

**Licensed variances**, declared rather than silent. (1) *The floor outranks the provenance rule.* A version, date or identifier that a cold implementer needs is held here even though it reads as provenance — the floor decides, not the appearance. (2) *A Change Log is optional*; a construct spec that never versions before acceptance carries none. (3) *The frame carries a Ticket row* — a fourth sanctioned home for a ticket identifier, and the parent's homes list admits it.

**The reason to read it anyway is what is not instantiated here** — tense earned by enforcement, status claims earned by the trail, the amendment lifecycle, the status lifecycle that defines what acceptance is, and the cold read. A spec authored without those fails in ways nothing in this skill catches.

## Is this a construct spec?

`author-decision-record` owns the routing gate, carries this doctype's routing entry, and states the deliberation substrate it requires. Two tests decide whether you are in the right place:

- **Altitude.** If the decision constrains the architecture across services, or the platform data model, stop — that is an ADR or a DDR.
- **Delta, or standing thing.** An SDD describes **what a service is**; a construct spec describes **what changes** in a construct. If you are documenting a thing's current shape rather than a change to it, you want an SDD. This is also why a construct spec disperses part of its content at acceptance while an SDD does not — a delta's durable residue is *what the thing now is*, which is the standing doctype's territory. See **Graduation**, below.

**When the call is not clean — the artifact plausibly fits two homes, or none — surface it to the operator with the discriminating test and the answer it gave, and stop.** Do not route by default. A routing answer nobody examined is how a document ends up governed by nothing.

## The two jobs

A construct spec does two jobs at once. It is a **programming spec** — the document an implementer builds from — and it is a **ratification record**, the trail of what was deliberated, corrected, and agreed on the way to the design. Both jobs are legitimate, but only one is housed here: the spec carries the contract, and a standing pointer to where the record lives. That record lives in **the ticket** — the tracker item governing this spec's work, referred to that way throughout this section. The failure this skill exists to prevent is the record migrating into the spec until the spec is unusable. Call that migration **the bleed**.

The bleed is survivable in a short document, but it becomes the dominant cost once someone starts implementing against the spec — everything the build teaches wants to be written down, and the record of how each thing was agreed arrives at the same rate as the constraint itself.

**Reorganisation is not the fix.** The instinct is to say contract and argument are tangled and must be pulled apart. At document scale they usually are not tangled: the bleed sits beside the contract, paragraph after paragraph, and rearranging what sits beside the contract does not reduce how much of it there is. Where bleed *is* embedded — a clause inside a contract sentence — it is excised, which is still relocation. **The fix is relocation, not rearrangement.** That is a claim about the document, not a prohibition on editing a sentence: where history is fused into a contract sentence's grammar, rewriting that sentence to state the constraint without the history is exactly the right move.

### The floor — the rebuild test

One test governs everything below:

> **Would a cold implementer build something different — or later change something they should not — if this passage were deleted?**

If yes, the floor **holds** it: it stays, whatever else this section says. If no, the floor **releases** it, and the rules below decide where it goes. *Held* and *released* are the only two words used for this; nothing here passes, fails, or survives.

**The cold implementer** is competent in the stack and has no access to the tracker, the chat history, or you. That reader is the spec's whole reason for existing, and every judgment here is made on their behalf.

**The second clause is not decoration.** Rationale that forecloses a change — *"the sync client, because the async one deadlocks against our connection pool"* — changes the build the first time someone tries to improve it.

**The floor holds, at minimum:** every constraint, threshold and required value; rationale that forecloses a change; term definitions; worked examples; caveats naming a likely misreading; and the orienting material a cold reader needs to place the construct among its neighbours. An ambiguity resolved wrongly is a different build, and so is a correct build someone breaks next quarter.

**Durability test for foreclosing rationale.** Foreclosing rationale is held only while its reason is a property of the system that remains true. *"The async client deadlocks against our connection pool"* is such a property. *"We rejected Kafka because the team had no ops capacity in Q3"* is a circumstance, not a property — it is released, and goes to the ticket carrying the trigger that would reopen it. Without this test the floor's second clause holds every rejection ever made, permanently.

**The floor does not hold** the record of *who agreed to what, when, and after considering what*. That is the ratification record, and it changes nothing an implementer does now or later.

### The operative rule — state the conclusion, relocate the evidence

**Where the spec carries evidence for a claim, and that evidence is re-derivable from a durable artifact, the spec keeps the claim and removes the evidence, citing the artifact.** Hashes live in manifests. Prior rulings live in prior records. Observed figures live in the logs they were computed from.

**"Re-derivable" means the artifact permits recomputation — it need not store the value.** A statistic computed over a corpus — *"87 of 179 classifications differ"* — is re-derivable from that corpus even though nothing in it holds the number. The test is *could someone recompute this from the cited artifact*, not *does the artifact contain this string*. Read the other way, every derived figure in a spec becomes unsourced, which is the wrong answer in the direction that hurts most.

**What stays is the predicate.** A figure is only re-derivable if the method that produced it is recoverable. Where the method lives in the artifact, the figure goes clean. **Where it does not, the predicate stays in the spec even though the figure leaves** — what was counted, over what population, under what definition. A statistic without its predicate is not re-derivable at all; it is a number the next surface will recompute differently and then argue about.

**Scope, and it is narrow.** This rule reaches *evidence supporting a claim* — the derivation, the table of raw values, the quoted source passage. It never reaches the claim, the constraint, the threshold or the required value: a schema field is re-derivable from the schema file and a timeout from the config, and neither moves, because the floor **holds** both. **Projected figures — cost, budget, duration, capacity — are neither.** Nothing must cost the projected amount and nothing was measured at it; they are plan figures, and two rules govern them. **The floor decides, and it decides on comparison**: a projection stays where it forecloses a choice — where deleting it lets someone pick the more expensive arm, the slower path, the larger fixture — while the intermediate arithmetic that only supports the comparison is released. Where that arithmetic has a durable artifact behind it — a pricing record, a committed cost model — step 2 takes it. **Where it has none, it is part of the argument and goes to the ticket at step 3**, not into the flagged-evidence class; a projection is not an observation of the world and does not become one for want of a source. And **a projected figure is never evidence for anything else**: it measures a plan, not the world, and a later claim leaning on it is leaning on an estimate that moves when the plan is re-run.

**A value a labelled obligation cites is held, whatever the prose around it looks like.** A hash written as an observation — *"hashes to X on every call"* — is a required constant the moment a test asserts against it. The obligation set is the check: if an obligation names the value, the floor holds it and step 2 never reaches it.

Where a figure could be either, the discriminator is **requirement or observation**: *"throughput must sustain 4,200 rec/s"* is a constraint and stays; *"throughput was measured at 4,200 rec/s"* is evidence and goes, with the conclusion it supports kept.

**The artifact must be durable and must pre-exist the relocation** — a manifest, a captured corpus, a log with retention longer than the spec's life, a prior record, a source file, a merged change at a fixed revision.

**The artifact must not be created by the act of relocating to it.** Copying the evidence into a document and then citing that document satisfies the letter of the check and none of its purpose. This is a rule about the *act*, not about the *kind*: a tracker item is not disqualified for being a tracker item, and a merged change with its diff and its checks is a perfectly good artifact — but the thing you are about to write the evidence into never qualifies.

**The citation form.** A relocated fact leaves behind a citation carrying two things: **a resolvable identifier for the artifact** — a path, a run id, a revision, a document id — never a description like *"the logs"*; and, **where the artifact does not itself record the method, the predicate**. The syntax is the document's own and should be consistent within it; absent a reason to differ, use a trailing italic parenthetical on the sentence that keeps the claim — *(source. Predicate: what was counted, over what population, under what definition.)* What matters is that a reader can reach the artifact and reproduce the number. **A citation nobody can follow relocated nothing; it deleted something.**

The rule is **checkable** — name the artifact, and verify it actually permits the derivation — which is why it is stated ahead of the tiebreaker. **It never runs ahead of the floor.** If the spec does not yet cite the artifact, **adding the citation is part of the removal** — an uncited fact is a lost fact.

A spec that reproduces its own evidence grows without bound, because a conclusion is bounded — one sentence, one row — and the evidence that produced it is not.

### Applying them, in order

**0. Split, then deduplicate.** Break the passage into the smallest spans that can be removed without breaking the sentence around them.

Then, **before the floor runs**, reduce every fact to one span. Where the same fact appears in more than one place, keep the statement best placed for a cold implementer and delete the others as redundant. **Deleting a redundant copy is not relocation** — it needs no destination and no citation, because the fact has not moved. This is an editing act, not a disposition, which is why it happens here rather than competing with the routing below. **Delete a copy only against one you can see**, never against one you remember: under the continuous cadence you do not hold the whole document, and a copy deleted against a remembered original is a fact deleted. **In a table, the cell is the atom and the row plays the part the sentence plays in prose**; a column may be removed only by rewriting the table, which is the same licence this step gives for a fused sentence. **A cell that fuses a constraint with an observation is rewritten**, exactly as a fused sentence is — otherwise putting a statistic beside a required value in one cell makes it permanently unroutable. **Section headings and structural whitespace are orienting material: the floor holds them and the procedure never routes them.** Scaffolding *inside* a routed structure — a table's header row and separator — inherits the disposition of the content it frames: if the rows go the header goes with them, and a table whose rows split between dispositions is two tables. Where history is fused into a contract sentence's grammar — *"Priya's 12 March review established that the timeout is 30s"* — **rewrite the sentence first** (*"The timeout is 30s."*) so the history becomes a removable span. Do not evaluate a paragraph whole when one clause is doing the work.

**1. The floor.** Held → it stays. Stop.

**2. The operative rule.** Is this evidence for a claim?

- **With a durable pre-existing artifact that produces it** → keep the claim, remove the evidence, cite the artifact. Before deleting, **lift out any discriminating value the conclusion depends on** — if the conclusion is "dataset B may not be pooled," the identity of B is a required value and must survive the table's deletion.
- **Without one** → the evidence **stays in the spec, marked `[unsourced]`**, and is named as a candidate for a durable artifact. It never goes to the ticket; the ticket is not an artifact.

**3. What is left** — everything the floor released that is not evidence — **is the ratification record. Route it to the ticket.** Four species land here: agreement history; correction history; commentary on the document's own status or governance; and **the argument that produced the design** — the persuasion rather than the constraint (*"100% coverage here is the cheapest insurance in the programme"*, *"stated as a declared bet"*).

**Evidence embedded in a released passage travels with the passage.** Where the claim itself is going to the ticket, there is no claim left to keep, and splitting the quotation out to its artifact leaves a citation attached to nothing. Step 2 reaches evidence supporting a claim the spec *retains*; where the claim goes, its support goes with it.

**This step is terminal — nothing follows it.** If routing something feels wrong, the floor was answered too narrowly — go back and answer it again. But that is a diagnostic, not an exit: nothing sits undisposed while you decide.

**One rule governs the procedure as a whole: never route a span on the grounds that its content survives elsewhere.** Each span faces the floor and the artifact test on its own. A span released because another span carries the same fact has created a dependency on that span, and releasing that one later takes the fact with it and nobody notices. **After step 0 this is never a live temptation**, because step 0 has already reduced every fact to one span — which is precisely why deduplication runs before the floor and not beside it.

**Fast signal for step 3:** a passage naming *people, sessions, or acts of agreement* is ratification record. **Versions, dates and identifiers are deliberately not on that list** — they are frequently build constraints, and the floor decides them, never the signal.

### The cadence — route continuously, not at the end

**Routing runs at every amendment the build provokes, in the same act as the amendment** — the constraint the build taught goes into the spec, the reasoning that produced it goes to the ticket, together. A spec routed once at the end has spent the whole build accumulating, and by then the material has grown roots: it is cited, it is quoted, and removing it looks like losing something.

The difference from a decision record is frequency, not stringency. A decision record is amended occasionally; a construct spec under build is amended continuously, so its routing runs continuously too.

**A spec that has already accumulated** runs the steps once over the whole document, then adopts the cadence. Do not defer the cadence until the backlog is cleared.

### Where things go

Two destinations, and they are not interchangeable.

- **Released evidence goes to its source artifact** — which already holds it. The spec deletes its copy and cites. No ticket is involved, and none is needed.
- **Released agreement history goes to the ticket** — the tracker item governing this spec's work — because in the working model this skill binds to, nothing else holds it. Where the construct's deliberation is *already* durably recorded elsewhere — review threads, commit trailers, a decision log — that record is the destination and the ticket carries the pointer. If neither exists, open the ticket: **relocation with nowhere to go is deletion, and this section never licenses deleting the ratification record.** Where no tracker is reachable at all, the history stays in the spec **marked `[unrouted]`**, not dropped. This fallback covers history only; released evidence never needs it.

**The spec carries a standing pointer to the ticket**, so the record is reachable from the only document anyone reads. Beyond that, the spec adds a pointer *into a prior document* only where the relocation would otherwise leave a **live contradiction** — a prior document still asserting a position this spec reverses. That pointer states the current position in one sentence and cites the prior document; it does not narrate the reversal.

### Worked calls

Each verdict derives from the steps, so you can check it rather than accept it.

- **A paragraph explaining why this document may be marked complete under a weaker standard than a sibling document used.** Floor: released — the cold implementer builds identically and is foreclosed from nothing; it describes the document's status, not the thing being built. Not evidence. → **the ticket, entirely.**
- **A table of sixteen hashes showing that one of three recorded datasets came from a different instrument version.** Floor: the *conclusion* — these three datasets may not be pooled — is **held**; without it the implementer builds a pooling step that is wrong. The hashes are evidence, and the per-dataset manifests already produce them. → **conclusion stays, with the identity of the odd dataset lifted out; hashes deleted, manifests cited.** No ticket.
- **Three block quotations from three prior documents, establishing that an earlier deferral was reversed on a changed criterion.** Floor: released. Operative rule: evidence, and the three documents pre-exist and produce it. The prior deferral is still live elsewhere, so one sentence stating the current position and citing the three documents is **written** in their place. → **quotations deleted, three citations added, one sentence written.**
- **"Datasets recorded before the v3 encoding change use the old field order."** Names a version and reads like history. Floor: **held** — remove it and the implementer builds a reader that fails on half the corpus. → **stays.** The floor outranks the fast signal.
- **"We use the sync client; the async client deadlocks against our connection pool."** Reads like a rejected alternative. Floor: **held** — remove it and the next person "fixes" it to async and reintroduces the deadlock. Durability: the deadlock is a property of the system. → **stays.**
- **"We rejected the queue-based design because we had no ops capacity that quarter."** Also reads foreclosing. Durability: capacity is a circumstance, not a property. → **released; to the ticket, carrying the trigger that would reopen it.**
- **A parenthetical of the form "(Corrected at v0.8.0: v0.7.0 said X)" inside a contract sentence.** Floor: released — identical build, nothing foreclosed. Granularity: the unit is the parenthetical. → **excised; the sentence keeps only its current statement, and the correction history goes to the ticket.** This shape is also `author-decision-record`'s; the disposition is the same.

## Shape

This section says what a construct spec is made of. It does not decide what belongs in it — the two jobs does that, and the two are independent: a well-shaped document can be full of bleed, and a document with no bleed can still be unbuildable because its obligations are unfindable.

### The document frame

A construct spec opens with a file header and a metadata table, then states its scope, then its pieces, then closes with what it does not cover.

**The frame is not subject to the routing.** The metadata table and the Change Log are the licensed home for the document's own provenance — status, ratification, authorship, doctype, correction history live *there* precisely so they do not live in the body. The two jobs governs the **body**; when it releases something as commentary on the document's own status, the frame is where it lands if it stays in the document at all. Without this exemption the routing would evict the frame it depends on.

**And the frame is a pointer, not a log.** The Ratification row records *what* was ratified and *when*, by reference; the per-item record lives in the ticket. Because the frame is the one zone routing cannot reach, accumulation there is never evicted — keep it bounded by hand.

The metadata table carries: **Document · Doctype · Status · Date · Ticket · Author · Ratification · Empirical driver · Body integrity.**

Three of those rows do real work and are easy to leave out:

- **Doctype carries its ruling, not just its name.** State why this is a construct spec and not an ADR, DDR, or SDD — the discriminating test and the answer it gave. A reader who disagrees with the routing can then argue with the reasoning instead of guessing at it, and the next author has a worked precedent.
- **Empirical driver** names what the spec answers — a run, an incident, a measurement. Where the construct is being built for the first time and no such evidence exists, the row names the **forcing function** instead: what makes this needed now. A row that can be filled with neither is a spec nobody needed yet. Do not invent a driver to fill it.
- **Body integrity** declares, where Doctype and Status are, that the body states the contract as it currently stands and that correction history lives elsewhere. Putting it in the metadata makes the discipline visible at the top of every read, which is where a discipline has to be to survive an amendment.

**Scope** carries three things:

- **The problem**, and what closes it.
- **Orientation** — where this construct sits among its neighbours, and the terms a cold reader needs defined. The floor holds both, and they are the most commonly under-supplied material in a spec, because the author already knows the system and cannot see the gap.
- **The invariants the spec does not reopen.** A construct under active development accumulates settled commitments; a spec that does not name them invites an implementer to re-litigate one by accident.
- **The empirical basis** — where a claim rests on thin evidence, say how thin, and mark what is fixed by design from what is a held constant awaiting data. *(Called basis, not floor: **the floor** in this skill means the rebuild test and nothing else.)*

**A Change Log is optional.** Where one exists, rows are a single line of at most 200 characters carrying version, date, ticket, and what changed. The deliberation that produced the change goes to the ticket. A record that never versions before acceptance needs no Change Log at all.

### The piece

A construct spec is composed of **pieces**. Each piece carries, in order:

- **Decision** — what is being built or changed, stated so that conformance has a yes-or-no answer.
- **Rationale** — why this shape and not the obvious alternative. Subject to the floor and the durability test.
- **Amendments** — every file this piece touches and how.
- **Correctness invariant** — the property that must hold, stated as a property rather than as a procedure.
- **Required tests** — the obligations that satisfy the invariant, each labelled. The field holds **obligations, not necessarily tests**: the instrument that answers each one varies by target, and the target section below says how to declare it.

**The amendment set names deliberate non-changes.** Where a reader would reasonably expect a file to move and it does not, say so and say why. An unlisted file is ambiguous between *considered and excluded* and *forgotten*, and an implementer resolves that ambiguity by guessing.

**Where a change opens a specific risk, the piece names the risk and the gate that closes it.** A performance change that reorders inputs, a scheduling change that alters what a component sees — these have failure modes an implementer will not infer from the Decision. Name the failure mode concretely and name the check that would catch it. This block is not always needed; where it is needed, its absence is the defect that ships.

### One piece, one invariant

**A piece carries exactly one correctness invariant.** If you find yourself writing a second, you have two pieces — split them.

This is the only piece-boundary rule, and it is deliberately not a size rule. A piece is as long as its invariant needs. Size caps invite the two failures they are meant to prevent: material gets compressed past legibility to fit, or gets relocated somewhere it does not belong. The invariant test asks the question that actually matters — *is this one thing?* — and a piece that has grown large while still answering to one invariant has grown legitimately.

### When a piece splits

The invariant test will sometimes fire on a piece already written. Three rules govern the split, and none is discretionary:

- **Obligations follow their invariant.** Each labelled obligation moves to the piece whose invariant it satisfies. **Labels do not change** — the suffix rule applies to pieces as it does to obligations, so a split Piece 2 becomes 2a / 2b / 2c and `H4` stays `H4` wherever it lands. Renumbering on a split invalidates every citation for no gain.
- **Material shared by more than one resulting piece moves up, never sideways.** A convention, a constraint, or an orienting fact that all the new pieces need belongs in the document's scope — not repeated in each. Repeating it is the mirror the operative rule prohibits, and the copies will diverge at the first amendment.
- **The split is stated once, where the pieces begin.** A reader arriving at 2b needs to know 2a exists and what it holds. One line does it.

### The piece and its document

Some things belong to the document rather than to any piece: **the frame, the scope, the obligation namespace, and the empirical basis.** A piece never restates them.

**Authoring or amending one piece of an existing document** is the common case once a build is under way, and it is not the same act as writing the document. Read the frame and the scope first — the namespace especially, because a new obligation must be dense and ordered within it and a piece cannot see that from inside itself. Where the piece needs something the frame does not yet carry, amend the frame in the same act rather than inventing a local convention.

**A piece may carry its own floors.** Where an honest floor is specific to one piece's evidence it belongs with that piece; the document's empirical basis states what the spec as a whole rests on, a piece's floor states what its own claims rest on. Both are legitimate and they are not the same statement.

### Obligation sets

Labelled obligations are **contract, not annotation.** An implementer builds against them, checks them off, and cites them in the commit.

**Labels are a prefix plus an ordinal, and the prefix is yours to choose** — a letter for the family and, where a spec has several pieces whose obligations must not collide, the piece as a qualifier: `H1…Hn` for one family, `L1-T1…L1-T5` where the piece is `L1`. Declare the namespace once. Whether it is per-piece or per-document determines what "dense" means, and a reader cannot infer it.

Three rules follow:

- **State them as a dense, ordered sequence.** A gap reads as a dropped obligation and costs a reader time proving it was not.
- **Insert with a suffix; never renumber.** A new obligation between `H3` and `H4` is `H3a`, because renumbering silently invalidates every citation in the tests, the commits, and the review record. The suffix is mildly ugly and the alternative is a broken reference nobody notices.
- **Verify elementwise, never by count.** The check compares two sequences: **the obligation list as declared**, against **the places that answer it** — the piece text that raised each one, or, where a spec carries a consolidated obligation section, that section's rows. Compare position by position. Thirteen bullets against thirteen rows tells you nothing about whether they are the *same* thirteen or in the same order — **a count cannot see order**, and a set that has drifted out of sequence passes every count-based check ever run against it.

*Three relations share the word* discharge *and are kept apart here:* an obligation **satisfies** an invariant; an instrument **answers** an obligation; a verification pass **reconciles** the obligation list against the places that answer it.

### Sections beyond the spine

The spine is required. Sections beyond it are permitted and often necessary — a piece that builds an instrument may need to specify its fixture, its calibration, its self-test; a piece that changes a protocol may need none of that. **Do not treat a proliferation of sections as a defect.** Whether a section belongs is the floor, applied to its contents; the number of sections is not evidence of anything.

### Graduation — what happens to the shape at acceptance

A construct spec is not a permanent home for everything in it.

**Acceptance** is the status transition in `author-decision-record`'s status lifecycle — PROPOSED to ACCEPTED — declared by the operator's ratification and recorded in the Status row. It is not "the build finished." A spec can be built from and still be PROPOSED, and graduation does not fire until the status moves.

**How this reconciles with the floor.** The floor governs the spec **while it is the document being built from**. Graduation fires at acceptance, when it stops being that. And graduation does not lose a constraint — it relocates *authority* and leaves a pointer, so a cold implementer arriving afterward builds from the construct's document set rather than from the spec alone. The floor is never violated; its subject changes.

**A standing contract document** is where graduated rules land: the durable statement of one facet of a construct's behaviour — its data shape, its state transitions, its preparation or invocation contract — living beside the construct's code and cited by specs rather than superseded by them. It sits below the doctypes above: an SDD describes a whole service, a standing contract document describes one facet of one construct. It is a destination, not a doctype this skill authors; its shape follows the facet it carries, and it is created the first time a rule has nowhere else to go.

At acceptance, three things happen:

- **Operative rules graduate. A design decision graduates when something other than this implementation must conform to it** — a serialisation constraint a second component must obey, a state-handling contract any future field addition must satisfy, a reader rule every future reader of the same data inherits. It moves into the construct's standing contract documents, which become its authority; the spec keeps a pointer and the reasoning, never a second copy of the rule. Where the construct has no standing contract document yet, graduating the first rule is what creates one. **The test is checkable: name the second thing that must conform, or it does not graduate.**
- **Change-local material stays and is spent.** The fixture this campaign used, the file-change list, the build's test obligations — these remain in the spec as the record of what was built. They are no longer instructions, and nothing graduates.
- **The decision and its rationale stay. That is what the accepted spec is.** A construct spec that has been built from and accepted reads as a decision record for its construct: what was decided, why, what invariant holds, and where the operative rules now live.

**The graduation judgment is made at acceptance, not while authoring — with one exception that is not optional.**

Mid-build, most rules are genuinely ambiguous: a rule that will bind future code and one that merely describes this build look alike until the build is done. At acceptance they separate — what got built is known, what the standing documents needed is known, and what was scaffolding is obvious in hindsight. Do not force that call early; you will get it wrong in both directions and then defend it.

**The exception: a contract between two components of the same construct is knowable the moment there is a second component.** Where two build targets must agree on a shape — a serialisation format, a field set, an anchor — fix and publish it *then*, not at acceptance. Deferring it means two implementers build against a contract nobody has promoted, and the divergence surfaces as a defect rather than as a review finding.

## The target

What the implementer builds — a Python module, a prompt artifact, a shell script, infrastructure — does not change the shape. It changes what two parts of the shape must **declare**: the obligations, and the amendment set.

- **Every obligation names the instrument that discharges it.** A unit test is the right default for code and the wrong default for everything else. A prompt amendment may admit no mechanical check at all; say so, and name what does check it — a proving run, a cold audit, a replay against captured output. An obligation whose instrument is unstated gets a fabricated unit test or gets quietly dropped.
- **And every obligation states whether it gates the landing.** Not every instrument can gate: a pre-push test can block a merge, a cold audit or a proving run cannot. An obligation whose gating status is unstated is either read as blocking — and holds the landing hostage to an instrument that cannot fire before it — or read as advisory and quietly skipped.
- **Where the target carries its own version identity, the amendment states the stamp movement.** Prompt generations, model maps, calibration counters, schema versions — these have an identity axis source files do not. State whether the change moves it, and where it does not, why not. A stamp that should have moved and didn't stays invisible until something downstream cites the wrong generation.
- **The amendment set names the target's authoring authority and never restates it.** Service code, agent and LLM-call code, frontend code, infrastructure — each has its conventions in its own skill. The spec says what the construct must do; that skill says how artifacts of its kind are shaped.

## Boundaries with sibling skills

- **Which doctype this is, plus the body-integrity and amendment-lifecycle disciplines** → `author-decision-record`. It owns the routing gate and the record-honesty rules; this skill is one of its routes and defers to it on both.
- **Authoring this skill, or any reusable standard** → `author-standard`: membership, sourcing, binding, shape, and proving.
- **The handoff that gets the spec built** → `author-execution-relay`. The relay points at the spec; it never contains it.
- **Reviewing the finished change** → `code-review`. This skill governs the document the change was built from.
- **How artifacts of the target's kind are shaped** → the target's own authoring skill, named in the amendment set.
