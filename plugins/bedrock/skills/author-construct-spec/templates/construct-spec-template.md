<!--
  CONSTRUCT SPEC TEMPLATE

  Read `author-decision-record`'s Body integrity, Amendment lifecycle, status
  lifecycle, and cold read sections BEFORE filling this in. This template gives
  shape; it cannot give substance, and a blank frame is easy to fill with
  plausible-looking nothing.

  TWO COMMENT CLASSES. The distinction is load-bearing:

    FILL:     guidance for writing this section. DELETE it once the section
              is written.
    STANDING: the discipline that governs this section at every later
              amendment. DO NOT DELETE — ever. These fire long after the
              first draft. Deleting them puts you back on a pointer someone
              has to remember to follow.

  ONE PIECE, ONE INVARIANT. Writing a second invariant in one piece means you
  have two pieces.
-->

# File: <path/to/this-file.spec.md>
# Author: <name and role>, authored on <surface>
# Created: <YYYY-MM-DD>
# Description: <two or three lines: what this spec changes, in which construct,
#   and the obligation that closes it.>

<!--
  STANDING — THE FRAME. The metadata table and the Change Log are the licensed
  home for this document's own provenance and are NOT subject to the routing
  below. They are also the one zone routing cannot reach, so nothing evicts
  accumulation here: the frame is a POINTER, NOT A LOG. Ratification records
  what was ratified and when, by reference; the per-item record lives in the
  ticket. Keep it bounded by hand.
-->

| Field | Value |
|---|---|
| **Document** | `<filename>` |
| **Doctype** | Construct spec. <!-- FILL: state the RULING, not the name — which discriminating test you ran and the answer it gave. Altitude: does this constrain the architecture across services, or the platform data model? If yes it is an ADR or DDR, not this. Delta or standing thing: an SDD says what a service IS; this says what CHANGES in a construct. If the call was not clean, you should have surfaced it to the operator rather than filling this row. --> |
| **Status** | PROPOSED v0.1.0 <!-- FILL: status lifecycle is author-decision-record's. ACCEPTED is declared by the OPERATOR'S RATIFICATION and recorded here — it is not "review came back clean" and not "the build finished." Moving this row to ACCEPTED is what fires graduation. --> |
| **Date** | <YYYY-MM-DD> |
| **Ticket** | <ID> <!-- FILL: the standing pointer to the ratification record. Everything routed out of the body lands here. --> |
| **Author** | <name> |
| **Ratification** | <what was ratified, when — by reference> |
| **Empirical driver** | <the run / incident / measurement this answers — or, for a first build with no such evidence, the forcing function: what makes this needed now. Do not invent one.> |
| **Obligation namespace** | <e.g. `H1…Hn`, document-wide — or `P1-T1…`, per piece> <!-- FILL: declare it ONCE, here. Whether labels are per-piece or per-document determines what "dense" means, and a reader cannot infer it. --> |
| **Body integrity** | The body states the contract as it stands. Version provenance and correction history live in the frame and the ticket. |

---

## Purpose and scope

<!-- FILL: the problem, in which construct, and what closes it. -->

**Orientation.**

<!--
  FILL: where this construct sits among its neighbours, and the terms a cold
  reader needs defined. The floor HOLDS both. This is the most commonly
  under-supplied material in a spec, because you already know the system and
  cannot see the gap. Define the terms whose meaning shifts by context.
-->

**Hard invariants preserved (not reopened here).**

<!--
  FILL: the settled commitments this spec does NOT reopen. A construct under
  active development accumulates these; a spec that does not name them invites
  an implementer to re-litigate one by accident.
-->

**Empirical basis.**

<!--
  FILL: where a claim rests on thin evidence, say how thin. Mark what is fixed
  by design (defensible from first principles) from what is a held constant
  awaiting data. Not called "floor" — THE FLOOR in this discipline means the
  rebuild test and nothing else.
-->

---

<!--
  STANDING — THE ROUTING. This governs the WHOLE BODY, every section below,
  at every amendment the build provokes — not once at the end, and not only
  in Rationale. Bleed sits beside the contract paragraph by paragraph, and it
  arrives fastest while you are building.

   0. SPLIT, THEN DEDUPLICATE. Smallest span removable without breaking the
      sentence around it. Then, BEFORE the floor runs, reduce every fact to
      one span: keep the best-placed statement, delete the rest as redundant.
      That is an editing act, not a disposition — no destination, no citation.
      DELETE ONLY AGAINST A COPY YOU CAN SEE, never one you remember.
      If history is fused into the grammar ("Priya's 12 March review
      established that the timeout is 30s"), rewrite the sentence first.
      IN A TABLE: the cell is the atom, the row plays the sentence's part; a
      column moves only by rewriting the table. A CELL FUSING A CONSTRAINT
      WITH AN OBSERVATION IS REWRITTEN, like a fused sentence. Header rows
      and separators inherit the disposition of what they frame.
      HEADINGS and structural whitespace are orienting material: HELD, never
      routed.

   1. FLOOR. Would a COLD IMPLEMENTER — competent in the stack, no access to
      the tracker, the chat, or you — build something different, or later
      change something they should not, if this span were deleted?
      YES -> it STAYS. Stop.
      The floor holds, at minimum: every constraint, threshold and required
      value; rationale that forecloses a change; term definitions; worked
      examples; caveats naming a likely misreading; and orienting material.
      DURABILITY: foreclosing rationale is held only while its reason is a
      durable property of the system. "The async client deadlocks against our
      pool" stays. "We had no ops capacity that quarter" is a circumstance ->
      released, to the ticket, carrying the trigger that would reopen it.

   2. EVIDENCE. Is this evidence for a claim?
      Durable pre-existing artifact that PERMITS RECOMPUTATION -> keep the
        claim, DELETE the evidence, CITE the artifact. The artifact need not
        store the value: a statistic over a corpus is re-derivable from the
        corpus. Before deleting, LIFT OUT any discriminating value the
        conclusion depends on, and KEEP THE PREDICATE — what was counted,
        over what population, under what definition. A figure without its
        predicate is not re-derivable, it is just a number.
      No such artifact -> it STAYS IN THE SPEC, marked `[unsourced]`, and
        NAMED AS A CANDIDATE for a durable artifact.
      A value a LABELLED OBLIGATION cites is held by the floor whatever the
        prose looks like; step 2 never reaches it.
      The artifact must not be CREATED by the act of relocating to it: never
        copy evidence into a document and then cite that document.
      CITATION FORM: a resolvable identifier — path, run id, revision, doc id
        — never "the logs"; plus the predicate where the artifact does not
        record the method. A citation nobody can follow deleted something.
      PROJECTED FIGURES (cost, budget, duration, capacity) are neither
        requirement nor observation. The floor decides, on comparison: a
        projection stays where it forecloses a choice; the arithmetic behind
        it is released. A projection is never evidence for anything else.

   3. WHAT IS LEFT is the ratification record -> THE TICKET. Four species:
      agreement history; correction history; commentary on this document's
      own status; and THE ARGUMENT THAT PRODUCED THE DESIGN — the persuasion
      rather than the constraint ("the cheapest insurance in the programme").
      EVIDENCE INSIDE A RELEASED PASSAGE TRAVELS WITH IT — where the claim
        goes to the ticket, its support goes too; step 2 reaches only support
        for a claim the spec RETAINS.
      TERMINAL — nothing follows it. If routing it feels wrong, the floor was
      answered too narrowly; re-answer it. A diagnostic, not an exit.

   WHOLE-PROCEDURE RULE.
      NEVER ROUTE A SPAN BECAUSE ITS CONTENT SURVIVES ELSEWHERE. Each span
        faces the floor and the artifact test alone. After step 0 this is
        never a live temptation — dedup has already reduced every fact to
        one span, which is why it runs before the floor, not beside it.
      NO TRACKER REACHABLE? The history STAYS IN THE SPEC and is marked
      `[unrouted]`. Relocation with nowhere to go is deletion, and deleting
      the ratification record is never licensed.

   FAST SIGNAL for step 3: a passage naming people, sessions, or acts of
   agreement is ratification record. Versions, dates and identifiers are
   deliberately NOT on that list — the floor decides them, never the signal.
-->

## Piece <N> — <name>

<!-- FILL: repeat this whole block per piece. Sections beyond the spine are
     permitted and often necessary, including a floor specific to this piece's
     own evidence. Section count is not evidence of anything. -->

<!-- STANDING — IF THIS PIECE SPLITS (a second invariant means a second piece):
     obligations follow their invariant and KEEP THEIR LABELS; the piece takes
     a suffix (2 -> 2a / 2b / 2c), never a renumber. Material shared by more
     than one resulting piece moves UP into Purpose and scope, never sideways
     into each copy. State the split once, where the pieces begin. -->

### Decision

<!-- FILL: what is built or changed, stated so that "did this conform?" has a
     yes-or-no answer. Definitive voice, not aspirational. -->

### Rationale

<!--
  FILL: why this shape and not the obvious alternative.

  GATE — if you would be INVENTING this, stop. The substrate that grounds it is
  named in `author-decision-record`'s routing entry for this doctype: either the
  construct's observed behaviour, or the decision records plus a deliberation
  artifact that fixed the shape. Produce it first, or mark this section an
  explicit TODO with a tracking pointer and leave the spec in PROPOSED. A
  fabricated rationale ages worse than a missing one.
-->

### Risk this change opens, and the gate that closes it

<!--
  FILL — OPTIONAL. Include where the change opens a failure mode an implementer
  would not infer from the Decision: a reorder that changes what a component
  sees, a schedule change that alters ordering. Name the failure mode
  concretely and name the check that catches it. Where it is needed, its
  absence is the defect that ships.
-->

### Amendments

| File | Change |
|---|---|
| `<path>` | <what changes> |
| `<path>` | **No change** (stated explicitly) |

<!-- STANDING — THE AMENDMENT SET names deliberate NON-changes wherever a
     reader would expect movement. An unlisted file is ambiguous between
     "considered and excluded" and "forgotten," and an implementer resolves
     that ambiguity by guessing. -->

**Stamp movement:** <does this move the target's own version identity — a prompt generation, a model map, a calibration counter, a schema version? If it does not, why not.>

**Authoring authority:** <the skill governing artifacts of this target's kind.>

<!-- STANDING — both lines above are REQUIRED where the target has them. A
     stamp that should have moved and didn't stays invisible until something
     downstream cites the wrong generation. Name the authoring authority;
     never restate its conventions here. -->

### Correctness invariant

<!-- FILL: ONE per piece, stated as a property that must hold — not as a
     procedure. Writing a second means you have two pieces. -->

### Required tests

<!--
  FILL: obligations, not necessarily tests. EACH ONE NAMES THE INSTRUMENT THAT
  ANSWERS IT — a unit test is the right default for code and the wrong default
  for everything else. A prompt amendment may admit no mechanical check; say so
  and name what does check it. State separately which obligations gate the
  landing; not every instrument can (a cold audit cannot block a push).
-->

<!-- STANDING — OBLIGATION LABELS. Dense and ordered, in the namespace declared
     in the frame. INSERT WITH A SUFFIX (H3a); NEVER RENUMBER — renumbering
     silently invalidates every citation in the tests, the commits, and the
     review record. -->

- **<H1> — <name>.** <obligation> *(instrument: <unit test | replay | proving run | cold audit>; gates landing: yes/no)*
- **<H2> — <name>.** <obligation> *(instrument: …; gates landing: …)*

---

## Consolidated obligations

<!-- FILL — OPTIONAL, where obligations span several pieces. -->

<!--
  STANDING — RECONCILE ELEMENTWISE, NEVER BY COUNT. The check compares two
  sequences: the obligation list AS DECLARED, against the places that ANSWER
  it — the piece text that raised each one, or this section's rows where it
  exists. Compare position by position. Thirteen bullets against thirteen rows
  tells you nothing about whether they are the same thirteen or in the same
  order. A COUNT CANNOT SEE ORDER. This check applies whether or not this
  section exists.
-->

## Out of scope and deferred

<!-- FILL: every deferral names the event that re-surfaces it. "Noted for the
     next touch" is where obligations go to die. -->

## Cross-references

<!-- FILL: the construct's standing contract documents, sibling specs, the
     empirical driver, and — after acceptance — where each graduated rule now
     lives. Point; do not mirror. -->

## Change Log

<!--
  FILL — OPTIONAL. Delete this whole heading if the record will not version
  before acceptance; some accepted specs carry none. If kept: ONE LINE per row,
  at most 200 characters, carrying version, date, ticket, and what changed. The
  deliberation that produced the change goes to the ticket. Do not pre-place
  rows.
-->

---

<!--
  STANDING — AT ACCEPTANCE (PROPOSED -> ACCEPTED, on the operator's
  ratification, recorded in the Status row):

   - OPERATIVE RULES GRADUATE. A design decision graduates when something
     OTHER THAN THIS IMPLEMENTATION must conform to it. Name that second
     thing, or it does not graduate. It moves to the construct's standing
     contract document — the durable statement of one facet of the construct's
     behaviour, living beside its code — which becomes its authority. This
     spec keeps a POINTER (in Cross-references) and the reasoning, never a
     second copy of the rule. If no such document exists, graduating the first
     rule is what creates one.

   - CHANGE-LOCAL MATERIAL STAYS AND IS SPENT — the fixture, the file-change
     list, the build's obligations. Record of what was built; no longer
     instructions.

   - THE DECISION AND ITS RATIONALE STAY. That is what the accepted spec is.

  Do not attempt this classification while the build is in flight: mid-build
  MOST rules that will bind future code and ones that merely describe this
  build look identical, and you will get it wrong in both directions and then
  defend it.

  THE ONE EXCEPTION, and it is not optional: a contract between two components
  of the same construct is knowable the moment there is a second component.
  Where two build targets must agree on a shape — a serialisation format, a
  field set, an anchor — FIX AND PUBLISH IT THEN, not at acceptance. Deferring
  it means two implementers build against a contract nobody has promoted.
-->
