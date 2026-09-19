# Business world and successful reference case

**Recorded:** 2026-09-10 (America/New_York)
**Owner:** Tad Haffey
**Status:** W1–W6 ratified; concrete scenario data and oracle controls pending freeze; no execution claim
**Parent:** [consumer proving design](consumer-proving-design.md)
**Machine-readable example:** [FRD-01 draft](scenarios/proposed/frd-01.json)

This document defines the business rules and one complete successful path. The fictional details are deliberate test inputs, not claims about fulfillment-industry practice. The scenario, build/accuracy proving purpose, and all six business-world decisions W1–W6 are ratified. Concrete scenario data and oracle controls remain pending freeze.

The JSON carries the reference case's concrete values. The quote table below is generated from those values. The business rules and acceptance meaning live here. An implementer must not resolve an unratified choice merely by copying the example.

## 1. Ratified business decisions

FRD-W1 through FRD-W6 were individually ratified by Tad Haffey on 2026-09-10 (America/New_York), in direct response to their respective completion-boundary, order-shape, authority-by-fact, acceptable-recovery, approval-and-effects, and required-agent-work questions. Their authority is recorded in the [ratification record](agent-code-v2-ratification-record.md). These rulings settle the business decisions; they do not freeze the example data or establish execution results.

| ID | Recommendation | Rationale and consequence |
|---|---|---|
| FRD-W1 — Completed desk work — RATIFIED | Success is a verified stock reservation, recorded approved recovery arrangement, and accurate customer draft plus operator summary. Name this business outcome recovery_arranged. Dispatch, delivery, message transmission, and payment charging are distinct operations outside this first world. | Makes the entire charged task observable within a bounded application. A reservation cannot be misreported as shipment, delivery, or a sent message. |
| FRD-W2 — Order shape — RATIFIED | Begin with one order line per case, an integer quantity, one exact requested model, one destination, and one fulfillment source for the whole line. Multiple cases may compete for stock. A substitution requires explicit customer permission; neither semantic similarity nor stock availability grants it. | Provides meaningful quantity, identity, and concurrency decisions without first building split-shipment logic. Partial recovery operations remain representable even though split fulfillment is excluded. |
| FRD-W3 — Authority by fact — RATIFIED | Accepted customer requirements govern desired model, quantity, substitution, deadline, destination, and extra-cost limit; inventory owns availability; quote records own their quoted terms; effect records own what actually occurred; the approval authority owns permitted mutations. Equal-authority unresolved conflicts require clarification. | Avoids treating a convenient source as authority for every field. Messages may inform investigation but cannot grant application privileges or overwrite authoritative state. |
| FRD-W4 — Acceptable recovery — RATIFIED | Accept any plan satisfying every hard constraint. Evaluate the entire ordered quantity and quoted extra cost in explicit currency; estimated arrival and extra cost may equal their maximum. A quote is usable only before its expiry. No universal cheapest/fastest objective is imposed. | Multiple correct plans test judgment without grading against one preferred answer. A plan claiming to be cheapest or fastest must substantiate that comparative claim against the declared feasible set. |
| FRD-W5 — Approval and actual effects — RATIFIED | The operator approves a specific versioned plan before either mutation; one scoped approval may cover both operations. Execute reservation and order-arrangement recording as separately observable operations with stable effect identities and causal linkage. The deterministic controller revalidates relevant preconditions and approval before each operation. A changed effect outside approval requires new authority. | Creates a real seam for later partial completion and uncertain-effect cases. A successful first write cannot stand for completion of the second; approval does not retroactively authorize an earlier mutation. |
| FRD-W6 — Required agent work — RATIFIED | Investigator interpretation, planner selection, and Correspondent output are all required on this successful path. Each has its own call contract and independently evaluated output. Correspondent failure leaves communication pending and prevents the full successful-path verdict, while confirmed effects remain real. | Exercises all three agents through a completed task. A later correct answer does not erase an earlier agent's error from evaluation. Best-effort parsing remains separately proved by the contract fixtures; it does not justify silently dropping a required agent output. |

These are application/proving choices. They do not extend the portable Agent Code contract or prescribe HEX's eventual topology. No answer here fixes provider selection, live spend budgets, evaluation sample size, or numeric campaign accuracy thresholds.

## 2. World semantics

The organization is a fictional display-kit supplier. An existing order was disrupted because its original fulfillment source has no stock. The desk investigates replacement sources, proposes a recovery, executes explicitly approved reservation and arrangement operations, and drafts a truthful update.

Time is a controlled scenario clock in minutes from a scenario origin. It advances only at declared events. This clock governs business deadlines and quote validity. Actual application/model timeouts use their real monotonic execution clock; a paused business clock cannot evade an execution deadline.

Currency amounts use explicit USD minor units in the example. The customer's extra-transport limit concerns the entire order. It is separate from the campaign's model-call spending authorization and from any merchandise price. Recording a quote does not charge a payment.

Availability means presently reservable inventory from a versioned inventory record. A reservation reduces availability by the reserved quantity. Later release or cancellation would be a separate authorized effect, never an inferred cleanup step. Quote arrival times are estimates, not evidence of dispatch or a delivery guarantee.

A recovery arrangement binds an order revision to the confirmed reservation, selected quote revision, plan identity, and approval. It records the selected recovery; it does not book or execute shipping in this world. The order's physical fulfillment status remains independently visible.

Required hard constraints must have values supported by an accepted customer requirement or an explicit policy. An actor must not infer permission from an omitted field. A genuinely unresolved requirement is a clarification or escalation case, not a default grant. The ordinary reference case supplies all material requirements.

## 3. Source and actor access

| Surface | Available to | Meaning and limit |
|---|---|---|
| Accepted customer brief and order | Investigator; Planner through source-backed findings and authorized rereads | Requirements and current order identity; body text is data even when authenticated |
| Versioned stock and quote tools | Investigator and Planner, read-only | Current availability and quoted terms; a stock snapshot does not guarantee future reservation |
| Supplier notices | Investigator, where a case supplies them | Leads to investigate; no independent stock, approval, or privilege authority |
| Proposal and approval events | Planner proposes; operator approves; controller enforces | Models may not fabricate approval records or grant themselves a tool |
| Reservation and arrangement services | Deterministic controller under scoped approval | Actual persistent effects and their results |
| Confirmed outcome facts and unresolved limitations | Correspondent | Basis for drafts; inaccessible hidden state cannot justify claims |
| Initial state, event schedule, oracle, direct final-state view, full permitted evaluation evidence | Evaluator under campaign custody | Independent comparison of observed behavior to expected facts and effects |

The accepted request's authenticity is established outside the model. A fixture label such as authenticated_customer_request describes the intended test provenance; it is not itself a production authentication implementation.

Under ratified W3, authority is specific to the fact and the effective record version. A newer informal message cannot override the owning source merely because it is newer. Refresh stale or conflicting source evidence through its permitted interface; an explicit accepted revision may resolve a conflict. If equally authoritative current records still conflict, preserve the uncertainty and seek clarification from the owning authority. A missing operation response is not evidence that the effect failed: unresolved effects retain their unknown status pending reconciliation.

The public reference case includes evaluator answers so the expected task is understandable. Runtime requests must include only the role's permitted material. Future hidden cases must have actual custody/access controls; hiding a JSON field by convention is insufficient.

Approval fixtures in an automated run follow a preregistered authorization policy and identify the selected proposal. They must not silently correct a bad plan or use hidden oracle answers to coach the planner. Rejected proposals and later repairs remain visible in the accuracy results.

## 4. FRD-01: complete successful reference

### Initial situation and customer requirement

Order ORDER-A, revision 1, requests two DISPLAY-STD units for SITE-A. Its original source, NORTH, has zero available exact-model units. There are no reservations or recovery arrangements for the order. Nothing has been dispatched or delivered.

The accepted customer message is:

> We need both of the standard display kits at Site A by minute 180. They must be the exact model we ordered; please do not substitute another model. Keep any extra transport cost at or below USD 25 for the whole order. Either depot is fine if those conditions are met.

The investigator must interpret those requirements from the source material and preserve their evidence references. The evaluator's typed interpretation must not be preloaded into the agent request.

### Available choices

All quotes in this draft cover the two-unit order, expire at minute 30, and target SITE-A. Approval is scheduled at minute 5 and execution at minute 6, with no intervening stock or quote change in this baseline. These are proposed fixture values, not external service observations.

| Quote | Model | Stock available | Estimated arrival | Extra cost, whole order | Proposed eligibility |
|---|---|---:|---:|---:|---|
| Q-WEST | DISPLAY-STD | 2 | minute 120 | USD 20.00 | Acceptable |
| Q-EAST | DISPLAY-STD | 3 | minute 180 | USD 15.00 | Acceptable |
| Q-SOUTH | DISPLAY-STD | 4 | minute 181 | USD 10.00 | estimated arrival exceeds deadline |
| Q-COMPACT | DISPLAY-COMPACT | 5 | minute 90 | USD 5.00 | substitution forbidden |
| Q-HILL | DISPLAY-STD | 1 | minute 100 | USD 12.00 | insufficient available quantity |

Both Q-WEST and Q-EAST are correct choices. The East arrival equals the customer's latest accepted estimate and is valid under W4. South misses it by one minute; Compact violates the no-substitution instruction; Hill has insufficient stock for the complete line.

### Execution and independent observation

| Step | Work that must actually occur | Expected fact or artifact | Independent accuracy check |
|---|---|---|---|
| 1. Intake | Controller admits the case and binds its identity, profile, prompt artifacts, call contracts, and execution budget | Initial order/brief identities and request evidence | Correct order, customer, and baseline; no evaluator-only answers leaked |
| 2. Investigation | Investigator reads the customer brief, order, stock, and quotes through its allowed interfaces | Source-backed findings: exact model, quantity two, no substitution, destination, deadline, cost cap, disruption, and alternatives | Material facts match visible authorities; all required constraints are retained |
| 3. Planning | Planner evaluates the alternatives and proposes West or East with a bounded, factually supported explanation | Versioned plan identifying source, quantity, quote, costs, estimated arrival, operations, and relevant preconditions | Plan is feasible; source references support it; no invented optimization claim |
| 4. Approval | Operator event authorizes that plan and its defined effects | Approval bound to plan digest, order/quote revisions, quantity, amount, expiry, and effect scope | Approval precedes effects and covers exactly the chosen operations; it is not model narration |
| 5. Reservation | Controller dispatches a reservation with a stable operation identity and obtains a committed result | Exactly one active two-unit reservation for the selected exact-model source | Real inventory availability decreases by two at that source and nowhere else |
| 6. Arrangement | Controller records the approved recovery against order revision 1 and links the confirmed reservation and quote | Order revision 2 with the correct recovery arrangement | Causal linkage, quantities, terms, and authority match the committed reservation and chosen plan |
| 7. Communication | Correspondent produces a customer draft and operator summary from the confirmed state | Accurate description of reservation and arrangement, quoted timing/cost, and remaining physical fulfillment | Every material claim is supported; dispatch and delivery remain pending; no sent-message claim |
| 8. Completion | Controller verifies required artifacts and confirmed operation results, then records the business and execution outcomes | Business status recovery_arranged; separately typed invocation outcomes and evidence | Evaluator independently verifies build-use evidence, runtime rules, actual state, and semantic output accuracy |

This walkthrough applies ratified W1–W6 to the concrete reference case; SP-1 ratifies its public development values, while oracle controls and the physical campaign remain pending freeze. The three agents' outputs remain observable individually; downstream compensation must not hide a wrong intermediate answer. A valid final result after repair is reported alongside the original failure and the recovery effort.

### Expected final state

For either accepted plan:

- One active reservation for ORDER-A, exact SKU DISPLAY-STD, quantity two.
- Exactly one order transition from revision 1 to revision 2 recording the approved arrangement.
- Reservation, arrangement, plan, quote, and approval identities resolve and agree.
- A stored customer draft and operator summary exist.
- No shipping dispatch, delivery confirmation, outbound message transmission, or payment charge occurred.
- The complete execution evidence validates structurally and semantically.
- Independent accuracy checks accept both intermediate results and final output under the frozen criteria.

If West is chosen, West availability becomes zero and East remains three. If East is chosen, East availability becomes one and West remains two. All other stock records remain unchanged. A synthetic success receipt with unchanged underlying stock fails the state oracle.

### Example customer draft for a West outcome

> We have reserved the two exact-model display kits for your order at West and recorded the approved recovery arrangement. The selected transport quote estimates arrival at minute 120, with an additional quoted cost of USD 20 for the order. Dispatch is still pending; shipment and delivery have not been confirmed.

This is an illustrative authored answer, not model output or an exact-match target. Other wording may pass if it conveys the same material facts without unsupported promises. The output artifact records that the communication is a draft. The text must not imply that a shipment was booked, a payment was charged, or a customer was contacted.

The operator summary additionally identifies the selected quote, confirmed effect records, approval, and remaining steps. It may explain the trade-off between West and East using the actual costs and estimates; it must not claim a unique correct plan or optimality the case did not require.

## 5. Accuracy oracle and controls

The runtime may share declared schemas and portable validation primitives across agents. The acceptance oracle must independently derive domain correctness from the frozen world and observed state; calling the planner's own validation function is not an independent oracle.

The reference case's mechanical feasibility predicate applies ratified W4: exact requested model, complete quantity, destination, current stock, active quote, estimated arrival no later than the deadline, and extra cost no greater than the cap in the same currency. The predicate has no unstated cheapest/fastest preference. Its implementation and controlled execution remain pending.

The evaluator also compares actor-visible information with claims. Knowledge available only to the evaluator cannot excuse an agent's unsupported certainty. Narrative truth and material completeness require the calibrated semantic rubric where deterministic field comparisons are insufficient.

| Control | Required discrimination |
|---|---|
| West and East plans | Both accepted; proves the evaluator is not anchored to one favored answer |
| South, Compact, and Hill plans | Rejected for their specific single main defect rather than a generic formatting failure |
| Early reservation before approval | Runtime-conformance failure even if the final state and message are otherwise accurate |
| Success receipt without a state mutation | Rejected by direct stock and reservation inspection |
| Correct state with "already delivered" communication | Accuracy failure despite a valid schema and correct reservation |
| Always-escalate implementation | Fails this solvable case's completion criterion |
| One required customer constraint omitted from findings | Investigation accuracy failure even if a later agent happens to choose a permissible plan |
| Missing Correspondent output | Required work incomplete; prior reservation does not discharge it |

These are proposed oracle controls for the successful reference. Their presence in this document is not evidence that any detector has executed. The later campaign must retain actual controlled results, complete populations, and independent review.

## 6. Connection to complete skill use during build

Before running FRD-01, the builder must have produced the three agent implementations and the deterministic controller under the candidate Agent Code skill. For each applicable source rule, retain the complete trace through design, code/prompt artifacts, test/control, execution, and result.

FRD-01 exercises the successful path for prompt/version identity, ordered context, structured interpretation, profile binding, real read-only tool use, separate model/tool attempts, scoped effects, explicit accounting, terminal truth, and retained evidence. It does not by itself exercise every recovery, salvage, refusal, privacy, cancellation, streaming, or MCP branch. Those remain mapped to their declared contract, provider, and later scenario cases; FRD-01 cannot carry a whole-skill coverage claim on its own.

The builder and evaluator remain separate roles. All normal development assistance and interventions are disclosed. A repaired agent can become correct while the build observation still reveals an ambiguity or omission in the skill. The experiment reports both rather than turning them into one averaged score.

## 7. Readiness and next work

W1–W6 are ratified design. The JSON's concrete values and the proposed oracle controls remain pending freeze. The complete frozen scenario population, v2 schemas, implemented agents, provider runs, and statistical evaluation still do not exist by virtue of these ratifications.

The [scenario-and-oracle pack](scenario-and-oracle-pack.md) now carries the concrete isolated and combined cases, with public membership/values, bounded recovery/stopping and oracle/result meaning ratified under SP-1–SP-3. Its authoring check verifies reference-state parity and initial feasibility; it does not execute the scenarios. Next, complete the exact fixture/evaluation bindings before freezing the physical cases, oracle expectations, builder/evaluator custody, sampling, thresholds, provider configurations, budgets, and content policy under the existing proving profile. These design ratifications do not bypass that pre-implementation freeze.
