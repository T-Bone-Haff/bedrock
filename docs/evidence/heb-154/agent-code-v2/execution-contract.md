# Fulfillment-recovery execution contract

| Field | Value |
|---|---|
| Document ID | FRD-EXECUTION-CONTRACT |
| Status | All four EC boundary decisions accepted; physical contract still PROPOSED/incomplete; not a cold-build handoff or campaign freeze |
| Revision | draft-1 |
| Owner | Tad Haffey |
| Recorded | 2026-09-11 (America/New_York) |
| Review trigger | Before fixture implementation, schema freeze, or a change to a boundary below |
| Doctype ruling | Construct-spec draft: one internal proving fixture and its application-facing protocol; not a HEX product design or portable standard |
| Deliberation substrate | Ratified W1–W6, SP-1–SP-3 and EXEC-SEQUENCE in the [ratification record](agent-code-v2-ratification-record.md) |
| Supersedes | None |

## 1. Purpose, authority and non-goals

Turn the agreed business scenarios into observable tool, state, recovery and evaluation boundaries. The [concrete pack](scenarios/proposed/scenario-pack.json) owns world values, public membership, event schedules and oracle meanings. Its current byte identity is `46cd351ab957e974829695c0562093ab664e1fb81249b9124a3a58a144fdf0b0`; this draft does not change those bytes. The [proving profile §7](agent-code-v2-proving-profile.md#7-consumer-build-execution-and-accuracy-proof) owns complete build use, runtime conformance and independent outcome accuracy. The [standard §§5–9](agent-code-v2-standard-amendment.md) owns portable attempts, parsing, budgets, uncertainty and request integrity.

The operator ratified the sequence, drafting step, EC-boundary division of work/access, EC-operation-journal identity/finality/replay design, EC-state-commit behavior and EC-event-evidence injection/evidence design. Unbound protocol/mechanism details remain proposed or pending. “Require” in a proposed section describes the proposed contract, not an adopted rule. Missing physical schemas, transport/persistence bindings, campaign settings and access enforcement prevent an implementer-complete or execution-ready claim.

The [physical runtime-binding companion](physical-runtime-binding.md) develops the next foundation: PB-runtime's local Compose model, PB-transport's local HTTP/JSON with separate private administration and PB-persistence's PostgreSQL engine are accepted. Enrollment of the existing PostgreSQL instance remains conditional on exact access/custody/lifecycle bindings and verification. The operator removed fixture HTTPS/certificate overhead and separately accepted the existing database's certificate/credential condition; provider TLS remains unchanged. Host/database observations and authoring checks do not establish a functioning or isolated fixture or replace the remaining wire/schema, builder-custody or campaign gates.

Do not supply product-agent prompts, internal generation schemas, completed tool loops, controller code or a reference agent implementation here. The cold builder must author those using the candidate skill. Do not choose the HEX architecture, a web framework, a cloud deployment, actual models, live budgets or evaluator thresholds through this draft. It supplies no hidden evaluation instances and authorizes no raw model-content capture.

Read depth for drafting: complete reference JSON; complete initial states and evaluator requirements for every public world; complete event schedules and expected-result blocks for every public case; complete common contract, oracle and control specifications. Other case metadata was mechanically inventoried, not re-reviewed field by field. Governing reads were complete standard §§5.1–8, proving §7 and consumer-design §§1–3, not a fresh full-bundle review.

## 2. Decision status and remaining bindings

| Decision | Recommendation | Alternative and reason for this choice |
|---|---|---|
| EC-boundary — ratified division of work/access | Supply an independently implemented, stateful business-service fixture; the cold builder authors the product agents and deterministic controller. Keep fixture administration/evaluation inaccessible to the product. | Having the same builder also supply the business-world machinery broadens the build and makes failures harder to attribute. A service fixture supplies the environment, not the solution. |
| EC-operation-journal — ratified design | Distinguish one logical effect from each physical attempt; require authoritative finality and a single-use replay permit after a no-effect closure. | A state lookup alone cannot fence a delayed original request. A permanently closed logical key would make FRD-08A/14B's required same-key replay impossible. |
| EC-state-commit — ratified behavior | Use separate atomic reservation and arrangement transactions, each atomic with its journal result; retain a uniqueness guard across logical keys for each order's active allocation. | One transaction for the entire recovery would erase the deliberately tested partial-completion boundary; a receipt-only fake would not prove actual effects. |
| EC-event-evidence — ratified design | Bind hidden schedules to observable boundary hooks and retain independent service, application-observation and evaluator records. | Sleeps are not reliable injection points; a single application log cannot independently prove either actual effects or what was visible to an agent. |

EC-boundary's division of work/access, EC-operation-journal's identity/finality/replay design, EC-state-commit's transaction/partial-completion/restart behavior and service-status distinction, and EC-event-evidence's injection/evidence design were individually ratified by Tad Haffey on 2026-09-11 (America/New_York); see the [ratification record](agent-code-v2-ratification-record.md). All four boundary decisions are accepted within their recorded scope; exact physical bindings remain proposed or pending. The coupled obligations below operationalize these decisions without reopening the public population or its acceptance meaning.

## 3. EC-boundary — ownership and application-facing protocol

### Separation and supplied material

The ownership/access division is accepted design. The companion also records accepted runtime, amended transport and PostgreSQL engine choices. Their exact process/transport/storage details, instance enrollment, wire fields and enforcement bindings remain proposed or pending; acceptance of the boundary is not approval of every implementation detail below.

| Actor/surface | Owns | Must not supply or access |
|---|---|---|
| Cold builder | Agent designs, immutable prompts, generation contracts, provider adapters/bindings, controller, local evidence/checkpointing, tests and handoff | Authoring conversation, hidden instances/labels, supplied completed agent/controller implementation |
| Built application | Interpretation, proposals, authorization checks, budget admission, tool dispatch, reconciliation decisions, communication and terminal decisions | Fixture admin credentials, direct service-store access, event schedules, evaluator verdicts/labels |
| Business-service fixture | Authoritative source reads, scoped grant verification, conditional state mutations, durable operation journal | Plan generation/ranking, agent correction, automatic recovery orchestration, desk completion verdict |
| Operator/requirement-owner fixture | Responses to actual clarification/approval requests under a preregistered visible-fact policy | Evaluator answer labels, an unsolicited correct plan, rewritten agent output |
| Harness/evaluator | Scenario initialization, environmental events, fault timing, isolated snapshots, independent predicates and retained evaluation | Secret assistance to the product or rewriting first results |

Use the accepted separate application/fixture model so an actual application termination cannot erase service effects. The companion selects local HTTP and PostgreSQL; their exact deployment, connection and instance-enrollment bindings remain open. Process separation alone does not prove access isolation: before hidden evaluation, enforce and test filesystem, credential, admin-endpoint and request-material boundaries. Until then, hidden-custody evidence is unavailable. Fixture implementation and its contract-test results must be independently identified before cold construction. Supplying it does not discharge the builder's own controller obligations.

### Wire conventions (design accepted in the companion; physical JSON Schemas pending)

Use provider-neutral JSON messages. Reject duplicate keys and unknown fields once closed physical schemas are bound; no implicit scalar coercion. IDs are nonempty opaque strings, revisions/quantities positive integers, stock and money amounts nonnegative integers. Business minutes are nonnegative integers. Preserve the pack's currency strings and quoted absolute arrival/expiry minutes; do not reinterpret them as durations or convert currencies.

- Request envelope: `protocol_revision`, `run_id`, `request_id`, `order_id`, `action`, `payload`. The authenticated caller/principal comes from the transport binding, not a model-supplied role field. Bind principal to permitted run/order/actions. No cross-order customer-data read; shared inventory is scoped to the run.
- Response envelope: `protocol_revision`, `request_id`, `observation_id`, `observed_at_minute`, and exactly one typed `result` or `error`. Observation IDs are opaque, not private journal positions. Transport timeout/disconnect is an application observation, not a fabricated service response.
- `SourceRef`: source kind, record ID, revision and content digest. Wrap existing source records without rewriting their body or losing original bytes. An accepted-source catalog identifies current records and explicit supersession; a larger revision of another record does not silently supersede it.
- All reads return their complete declared scope with source identities. If a later implementation paginates, continuation and complete-population evidence become binding additions before freeze. No silent truncation or hidden feasibility filtering.

### Service interface

These are logical action names, not a selection of HTTP, MCP or an SDK. All calls and rejected dispatches retain correlation and budget evidence. Read-only refers to business effects; audit recording is permitted.

| Action | Permitted caller | Request payload | Result contract |
|---|---|---|---|
| `order_context.read` | Investigator; controller-mediated permitted Planner reread | Empty object; order is envelope-scoped | Exact order revision, all current accepted brief references/bodies and supplier notices available now. No parsed oracle requirements. Equally current conflicting briefs both appear. |
| `source.read` | Investigator/Planner through controller | `source_ref` | Exact immutable referenced body, or typed unavailable/denied. Restores the complete source in FRD-13B; never returns an evaluator summary. |
| `availability.read` | Investigator/Planner through controller; controller revalidation | Explicit `skus` and `sites` sets within the run's published catalog | Inventory and quotes for that scope, including unavailable, late, expired and forbidden-substitution options. Quote presence is not permission. New quotes appear only after publication. |
| `requirements.clarify` | Investigator through controller | `request_id` correlation plus `field` (`deadline` or `destination`), question and conflicting/missing `source_refs` | `accepted_revision` with actual replacement source and superseded refs; `unresolved`; or `unavailable`. Consume the case allowance; never infer a value on no reply. |
| `approval.request` | Controller after an actual Planner proposal | Immutable proposal identity, proposed plan terms and source refs | `granted` with scoped grant; `denied` with authority reason; or `unavailable`. No replacement/ranked plan. Approval is not the outcome-accuracy verdict. |
| `inventory.reserve` | Authorized controller only | Mutation identity and approved plan terms, as below | `committed` with Reservation; definitive `rejected` with reason and no-effect closure; or pending `unresolved` under the accepted WIRE-outcomes refinement. A dropped response supplies neither commitment nor no-effect conclusion. |
| `arrangement.record` | Authorized controller only | Mutation identity, same approved plan terms, confirmed `reservation_id` | `committed` with Arrangement and resulting order revision; definitive `rejected` with no-effect closure; or pending `unresolved` under the accepted WIRE-outcomes refinement. |
| `operation.reconcile` | Controller within declared allowance | `operation_key`, uncertain `attempt_id`, original request digest, operation kind and semantic effect digest; identity additions accepted by PG-finality, exact wire schema/encoding pending | `committed` with original effect; `closed_not_applied` with finality proof; or `unresolved`. Not-found is unresolved unless the service has fenced the identified request. |
| `operation.cancel` | Controller cancellation propagation | `operation_key`, in-flight `attempt_id` | Cancellation accepted or unsupported; this alone is not proof of no effect. FRD-10D returns unsupported without revealing commitment. No post-cancel reconciliation in that case. |

Local draft/summary persistence is application-owned, not a customer-message service. The Correspondent's original output, accepted artifacts and any deterministic fallback status remain distinguishable. There is no product API for shipping, delivery, payment, message sending or stock release in this first world. Attempts to request those effects must be visible as denied attempts, and the evaluator also inspects their stores.

### Plan and grant boundary

The wire plan projection contains: order ID/revision; plan ID/revision; accepted-requirement source refs; selected quote ref; site, SKU, whole quantity, destination, quoted arrival, whole-order extra cost/currency and quote expiry. Retain the original Planner output and explanation separately; this projection is not a supplied agent generation schema. Derive its digest from frozen canonical bytes, excluding transport request/attempt IDs. The precise encoding belongs in the physical-schema freeze.

The [wire companion's WIRE-identity](wire-and-identity-contract.md) now accepts the raw/semantic encoding design and `grant_digest` refinement: exact physical-body hashes remain separate from domain-separated JCS plan/grant/effect hashes. The immutable grant's ID and content digest both bind the effect. The companion separately accepts source and action-specific outcome designs, including pending-mutation unresolved and original committed-result bytes on reconciliation. Machine-schema expansion, full physical bindings and runtime verification remain pending; this is not a supplied agent generation schema or additional replay authority.

A grant contains approval ID, issuer/policy identity, plan digest, full approved terms, issue time, expiry and the operations `inventory.reserve` then `arrangement.record`. Its arrangement authority is conditional on a reservation matching that plan. The trusted approval channel installs the grant; an ID invented in model text cannot create it. Do not grant unresolved requirements, invalid proposals or unrequested replacements. The operator policy must be implemented from the same actor-visible sources, not `evaluator_requirements` or expected outcome labels. Its exact rule binding and denial behavior are still required before freeze; no placeholder policy may coach a valid answer into existence.

The controller revalidates applicable authority, requirements, order and quote before each mutation. The service independently checks the scoped grant and current atomic preconditions. Service rejection does not erase an erroneous controller dispatch. Stock is an availability condition, not an inventory hold created by approval. Two approvals may compete for one unit. After reservation, its confirmed allocation replaces the pre-reservation stock check; it does not require the units to remain unreserved.

## 4. EC-operation-journal — effect identity, finality and replay

The operation/attempt distinction, authoritative finality and single-use replay-permit design are accepted. The [PostgreSQL companion's PG-finality](postgresql-persistence-contract.md) now accepts the generation-bound state machine, pre-admission fencing and reconciliation operation-kind/semantic-digest additions. These identify and fence a never-admitted original without inventing execution; current identity, authority and case allowances still govern. Exact physical schemas/encodings, DDL/grants and enforcement implementation are not frozen or verified by acceptance.

Each mutation supplies `operation_key`, `attempt_id`, `plan_digest`, `approval_id`, expected order revision and exact approved effect terms. Arrangement also supplies the reservation ID. A replay additionally supplies its finality/replay permit. The semantic effect digest excludes attempt ID and permit but includes operation kind and all effect parameters. Changing that digest under an existing operation key is rejected without a new business effect.

- Logical operation key: scoped to run, order, approved plan and operation kind; immutable across a transport retry/restart.
- Physical attempt ID: newly allocated and durably recorded before every physical dispatch, including replay. Bind it to the portable tool-attempt evidence. Re-delivery of the same attempt bytes never creates another execution opportunity; preserve evidence of every physical transmission.
- Journal: one logical record plus append-only attempt records and at most one committed effect. A durable fence governs whether a particular attempt can still commit. The service must serialize permit consumption with mutation admission.

| Actor-visible reconciliation result | Authoritative service condition | Permitted continuation |
|---|---|---|
| `committed` | Matching operation already has a durable effect and original result | Use that result; no new business mutation/replay in the committed cases. An unauthorized duplicate request may be deduplicated by the service but still fails controller conformance. |
| `closed_not_applied` | All admitted prior attempts for the logical operation are terminal without effect; the named original attempt is fenced against delayed commit; no effect exists | Service returns a single-use permit bound to operation key, semantic digest and journal generation. Controller may start a new physical attempt only if the case, current grant, quote and aggregate budget still allow it. |
| `unresolved` | Pending work, unavailable journal, ordinary empty lookup, conflicting identity, or inability to prove finality | Preserve uncertainty; no automatic replay. Continue only as the case explicitly permits. |

`closed_not_applied` is an authoritative snapshot about the original logical operation's attempts to that point, not permanent retirement of its logical key. A permitted replay opens a new attempt, not the old one. Atomically consume the permit; a concurrent second consumer, stale permit or delayed original attempt cannot mutate. The old attempt's closure remains immutable. A permit establishes service replay safety, not business approval or additional budget.

Reconciliation reports historical truth even if the original quote or grant has since expired. Expiry may prohibit another mutation; it cannot turn an actual committed effect into a failure or erase it. Reconciliation still requires current read authority and budget.

This gives FRD-14A/C one committed reservation attempt followed by reconciliation, and FRD-14B a definitively closed first attempt, reconciliation, then one new attempt under the same logical key. The identical A end state cannot make their traces interchangeable. Plain stock/order reads do not prove whether the named uncertain operation committed; resolution must provide matching effect identity or the declared finality authority.

## 5. EC-state-commit — actual transactions and restart

The separate atomic business operations, active-allocation uniqueness, partial-completion and uncertainty handling, durable restart/cancellation behavior and service-status distinction are accepted. Exact record fields, PostgreSQL isolation/locking and enrollment, details of the companion's accepted HTTP transport and physical enforcement bindings remain proposed or pending; no implementation or transaction/restart proof follows from acceptance.

| Boundary | Atomic service changes | Explicit non-changes |
|---|---|---|
| Reservation commit | Verify trusted grant, exact current order/quote/requirements refs and available stock; decrement one stock balance by whole quantity and advance its revision; insert Reservation; commit effect/journal result together | No order revision advance, arrangement, shipping or communication. A uniqueness guard prevents a second active allocation for the same run/order even under another key. |
| Arrangement commit | Verify grant and matching confirmed Reservation; compare-and-set the expected order revision; insert Arrangement; attach reservation and approved recovery-plan terms to that order; advance order revision once; commit journal result together | No further stock decrement. Preserve requested model, customer and original disruption facts; an allowed substitute lives in the recovery plan, not a rewritten customer request. |
| Definite rejection | Persist typed failure and fenced no-effect attempt result | No partial stock/order write. Reasons distinguish invalid authority, stale order/source/quote, insufficient stock, conflicting effect/key and the named injected order-write failure. |
| Environmental stock event | Apply the declared deltas and record both affected revisions in a separate environmental event transaction | Not a reservation by either test order. It must remain independently attributable in stock reconstruction. |

Proposed Reservation record: effect ID, operation key, committed attempt ID, run/order, plan digest, approval ID, quote ref, SKU/site/quantity/destination, committed business time and resulting stock revision. Proposed Arrangement record: effect ID, operation key, committed attempt ID, run/order, plan digest, approval ID, reservation ID, exact quoted terms and before/after order revisions. Both are immutable; transport acknowledgement is separate from commitment.

Use `arrangement_recorded` for the order's service status after this mutation, distinct from the desk outcome `recovery_arranged`. This status distinction is accepted: the former describes recorded effects; the latter also requires accurate communication. The wire schema must keep these separate before freeze.

No transaction spans both business mutations. Failure between them must leave the reservation held and the order unamended. A lost arrangement response may leave an amended order unknown to the application until reconciliation; a service snapshot seen only by the evaluator cannot repair that knowledge gap.

Before mutation dispatch, the application durably records plan/grant refs, logical key, new physical attempt, budget admission/consumption and dispatch intent. After response, it records the observation and knowledge checkpoint. A crash between these writes is conservative uncertainty, not failure/no-effect. Restart uses the same durable run/accounting identity; reconciles uncertain dispatched work when allowed; resumes confirmed work without repeating it. FRD-10A actually terminates the application after its acknowledgement checkpoint; FRD-14 crashes before confirmation is checkpointed. Fixture persistence and event-consumption state survive both. Never restore the initial world to simulate restart.

Cancellation is durable and stops new work under SP-2. Propagate cancellation to supported children, preserve unsupported results and in-flight uncertainty. It neither rolls back a committed effect nor permits late output to turn cancellation into success. A later external effect observation may be retained without silently resuming the task.

## 6. EC-event-evidence — deterministic seams without scripted agents

Execution-boundary injection, prerequisites/causal order/one-shot exposure, separate business and execution clocks, the three correlated evidence views and preservation of first results are accepted design. Physical hook/schema/collector bindings, access enforcement, custody/content permission and evaluator calibration remain open; acceptance is not evidence that any injection or evaluation has executed successfully.

The harness uses trusted boundary hooks, not elapsed sleeps: intake gate; source/clarification read; emitted proposal; approval response; before mutation dispatch; service admission; before/after commit; before reply delivery; before/after application checkpoint; model response/parse seam; manifest assembly/integrity gate; final artifact boundary. Hooks acknowledge reachability but do not hand the application a hidden scenario label or future schedule. Business time advances only under the fixture clock. Real model/tool deadlines and harness waits remain governed by the separately frozen monotonic-time budget.

Each physical binding names case/variant, event ordinal, hook, order, role/operation, occurrence, required predecessors, exact payload or transformation identity, visibility projection and one-shot consumption state. Preserve the pack's same-minute causal order. A failed prerequisite cannot be skipped or synthesized: mark the event unexposed and retain its cause. A `finish` instruction releases the remaining work and states expected obligations; the harness never writes the agent's arrangement or communication on its behalf.

### Complete event-kind binding inventory

This maps every event kind in the public pack, not every future native fixture or hidden case. Rows with several families share a seam, not an inferred permission to add attempts.

| Public families | Event kinds | Required boundary binding |
|---|---|---|
| FRD-01 | `advance_clock` | After approval, before reserve: expire unchanged quotes. Ordinary paths also use the common baseline schedule. |
| FRD-02 | `supplier_notice`, `conflicting_records` | Source reads; unresolved clarification after both accepted destination records are exposed. |
| FRD-03 | `accepted_revision`, `clarification_unavailable` | Actual permitted clarification; replace only the declared source or report unavailable. |
| FRD-04 | `supplier_notice` | Preserve untrusted source body/trust labels through the actual request manifest. |
| FRD-05 | `barrier`, `reservation_order` | Both plans/approvals precede controlled service admission; mirrored winner, with valid preflight prevention also accepted. |
| FRD-06 | `environmental_stock_change`, `approval_response` | Stock changes before dispatch; actual replacement proposal precedes the grant/denial. |
| FRD-07 | `commit_then_drop_reply`, `journal_result` | Real commit before lost response; reconciliation returns committed or unresolved exactly as scheduled. |
| FRD-08 | `drop_before_commit`, `journal_result` | Journal admission then fenced no-effect closure; finality precedes the single same-key replay. |
| FRD-09 | `definitive_rejection`, `commit_then_drop_reply`, `journal_result` | Arrangement boundary only; reservation remains real in both paths. |
| FRD-10 | `process_restart`, `cancel`, `cancel_in_flight` | Named process/checkpoint and cancellation boundaries; preserve service state and application knowledge separately. |
| FRD-11 | `profile_refusal`, `profile_output_limit`, `raw_response`, `response_transform`, `stream_interrupt` | Exact profile/adapter/parser seam; retain original and delivered identities separately under approved capture. Transformation precondition failure is not a handled injected fault. |
| FRD-12 | `budget_exhausted`, `usage_unavailable`, `unsupported_capability` | Actual admission/capability checks before governed transport; preserve unknown usage, never replace with zero. |
| FRD-13 | `reorder_data`, `declared_compaction`, `undeclared_context_loss` | Bind the named ordering/compaction phase and actual serialized outbound material; context-loss control must precede transport. |
| FRD-14 | `supplier_notice`, `barrier`, `timeout_then_restart`, `journal_result`, `reservation_conflict`, `new_quote`, `branch_on_permission`, `finish` | A uncertainty/restart first; B current-stock conflict next; quote notification before B replanning. Permission is already in B's accepted brief, not supplied by the branch event. |

For FRD-11E, absence of a schema-valid original response means its transformation condition was not reached. Preserve the actual model failure; do not manufacture valid JSON to inject the intended fault. Native refusal/output-limit/capability bytes and all physical hooks remain pending bindings. Injected failures are handling evidence, never estimates of natural provider failure rates.

### Evidence and evaluator interface

Retain three correlated views: service truth (transactions, journals, environmental events); application observations (delivered results, actual outbound requests, knowledge checkpoints and claims); evaluator expectations/results. Use a trusted collector's causal event order plus explicit predecessor IDs for cross-process ordering; public actors receive only their authorized projections. Do not send private causal positions, case labels, expected outcomes or fixture recipes into model requests.

The evaluator receives an immutable run manifest, initial/final service snapshots, full service transaction history, grants, all delivered observations, original/transformed response identities, application checkpoint/attempt/budget evidence, role artifacts including missing records, and exposure records. Bind run to case/world/configuration/candidate/implementation identities out of band. O-FACT/O-OUTPUT compare claims with what was delivered before them; O-PLAN independently checks feasibility and accepts every permitted choice, not a fixture-selected favorite; O-STATE reconstructs from direct persistent state and external events rather than trusting receipts. O-AUTH/O-UNKNOWN assess ordering and scope even if a defensive service avoided harm. O-TERMINAL checks effects and required output together. O-EXECUTION, O-ACCESS, O-EXPOSURE and O-BUILD retain their separate obligations.

The [PostgreSQL companion's PG-export](postgresql-persistence-contract.md) supplies the accepted service-state export design: final seal at the declared terminal/abort boundary, inspection and dump from one shared snapshot, then isolated restore with complete relation comparison. It does not manufacture finality for pending work, substitute database truth for delivered application knowledge, prove source grants through a data restore, or authorize content capture. Exact export commands/versions, deadlines, row encoding, restore configuration and content/retention permissions remain pending; no export/restore has been executed by this design record.

Evaluator APIs are read-only against immutable run evidence and have no correction channel to the first run. Calibrated judgment and operator adjudication follow SP-3. A complete first-result population must be retained before remediation evidence is added. Access to hidden labels and raw content requires the separately approved custody/content policy; this draft grants neither. The builder may use public examples, but runtime product agents still receive only permitted source material.

## 7. Correctness obligations and planned verification

The selected planned test realization remains the Haffey pytest profile; no FastAPI/database choice follows. Below are proposed mechanism tests, not executed tests or a schema-valid final campaign strategy. Every row gates fixture acceptance and thus eventual HEB-154 landing/adoption; none alone passes agent accuracy. Numeric coverage/quality thresholds remain an explicit freeze item.

| Stable obligation | Contract/instrument and clean specimen | Known-dirty counterpart and required detection | Existing acceptance link |
|---|---|---|---|
| FRDX-access | Integration/access test: own-order reads and shared scoped inventory; independent admin can inspect | Product principal reads other customer, journal store, admin schedule or oracle labels; deny access and detect deliberate label leak | O-ACCESS, CTRL-ACCESS |
| FRDX-sources | Contract test: complete versioned source scope; both current conflicting briefs visible | Drop a restriction/record or treat supplier text as approval; identity/completeness or authority detector fires | O-FACT, CTRL-FACT |
| FRDX-approval | Contract/order test: exact grant and current preconditions before each mutation | Early dispatch or changed plan using old grant; reject and retain invalid attempt even if no effect | O-AUTH, CTRL-AUTH, CTRL-EARLY |
| FRDX-reservation | Transaction/concurrency test: one actual allocation; both mirrored schedules | Fabricated receipt, over-allocation or new-key duplicate for same order; direct-state detector fires | O-STATE, CTRL-STATE, CTRL-DOUBLE |
| FRDX-arrangement | Transaction test: matching reservation, order CAS and effect journal commit together | Wrong reservation/order, repeated revision advance or partial order/journal commit; consistency detector fires | O-STATE, O-TERMINAL |
| FRDX-finality | Journal contract test: committed recovery versus fenced non-commit and permitted replay | Release a delayed original after closure, consume permit twice, use empty lookup as finality, or replay before reconciliation; fence/causal detector fires | O-UNKNOWN, CTRL-UNKNOWN, CTRL-REPLAY |
| FRDX-restart | Process integration: actual termination at each declared checkpoint seam; durable effects/attempts/accounting retained | Reset initial world/budget, lose dispatch intent or re-reserve confirmed stock; state/attempt detector fires | O-EXECUTION, O-STATE |
| FRDX-cancel | Boundary tests: no new dispatch and correct held/unknown/no-effect status | Silent release, post-cancel work or unsupported cancellation treated as no-effect; state/claim detector fires | O-STATE, O-UNKNOWN, O-TERMINAL |
| FRDX-exposure | Harness test: each one-shot event binds to its actual prerequisite | Agent fails before seam yet harness marks handling pass, fires twice or supplies replacement answer; exposure/assistance detector fires | O-EXPOSURE, CTRL-EXPOSURE, CTRL-POPULATION |
| FRDX-evidence | Snapshot/trace test: first output, all later attempts and original/transformed emissions distinguishable | Erase first failure, count injected output as natural, or grade only application self-report; provenance/population detector fires | O-BUILD, CTRL-FIRST-FAILURE, CTRL-BUILD-TRACE |

Reconciliation controls must include both actual service fencing and controller behavior; testing only a mock response cannot prove finality. Property/fuzz expansion may follow accepted schemas; controlled concurrency, crash injection and access-boundary tests are required by these risks. Production vendor chaos, load, deployment and migration claims remain outside this fabricated local fixture. These controls do not replace the original AC2 contract fixtures or three live provider-profile gates.

## 8. Amendments, risks and evidence handling

| Artifact | Operation | Result |
|---|---|---|
| This document | Record accepted boundary design and retain proposed physical contract | Cold-reader-visible decisions and explicit unresolved bindings |
| Ratification record | Retain sequence authorization and individual EC ratifications | All four EC boundary decisions accepted within their recorded scope; physical bindings remain open |
| Scenario guide and README | Link this draft | One discoverable execution-binding work surface |
| Concrete pack, baseline, installed skill and package | No change | Preserve ratified case semantics and pre-implementation state |

Main risks: a fixture that solves the task instead of providing services; counterfeit independence from mere folder/process names; no-effect claims without fencing; over-prescribed product internals; a perfect service concealing controller defects; and validation of fixtures mistaken for validation of agents. The ownership split, independent direct-state evidence and paired controls address these risks but are not yet implemented proof.

All inputs remain in place; this leg relocates no evidence. Earlier authoring reports retain their original input hashes and are not refreshed into fictional current proof. Keep new authoring checks separately with actual commands/stdout and exact input identities. A superseding design revision must identify affected decisions/fixtures/tests; no result is silently reused after a material binding changes. No deletion or rollback is needed for this additive draft; rejected proposals can remain historical or be explicitly superseded.

The [boundary-ratification authoring output](scenarios/proposed/execution-boundary-authoring-checks.json) retains the subsequent documentation-integrity and static event-inventory checks. It does not implement or exercise the accepted access boundary.

The [journal-ratification authoring output](scenarios/proposed/execution-journal-authoring-checks.json) retains the next integrity and static inventory rerun against its own input identities. It does not execute the accepted journal, fences or replay permits.

The [state-commit-ratification authoring output](scenarios/proposed/execution-state-commit-authoring-checks.json) retains the subsequent integrity and static inventory rerun against its own input identities. It does not execute transactions, crashes, cancellation or agent behavior.

The [event-evidence-ratification authoring output](scenarios/proposed/execution-event-evidence-authoring-checks.json) retains the subsequent integrity and static inventory rerun against its own input identities. It does not execute event hooks, prove isolation or evaluate agents.

## 9. Lifecycle and next gate

| Transition | Required evidence | Current result |
|---|---|---|
| Sequence and drafting authorization | Explicit operator ratification | Ratified; see EXEC-SEQUENCE |
| Boundary design acceptance | Individual EC decisions and disposition of substantive amendments | All four EC boundary decisions accepted within their recorded scope; physical bindings pending |
| Implementer-complete fixture contract | Closed schemas/bytes, exact error unions, transport/auth/storage, operator policy, hooks and schema-valid test strategy | Pending; this draft is not sufficient alone |
| Campaign freeze | Provider/settings, budgets, physical AC2/FRD fixtures, hidden custody, calibration plan, numeric thresholds, content policy and candidate build-input inventory | Pending |
| Implementation and verification | Identified fixture/candidate code plus positive/dirty controls, cold construction and all independent verdicts | Not performed |
| Graduation | Post-build review, governed destination and operator approval | Not requested; do not promote this consumer protocol into the portable skill by default |

Recommendation: develop exact fixture-facing wire schemas and canonical identities in the existing contract set, then derive corresponding DDL/grants and export encodings; this drafting step is ratified. The [wire/identity companion](wire-and-identity-contract.md) records all four WIRE designs accepted within scope, including pending-mutation unresolved and original committed-result bytes. A [machine-schema candidate](schemas/proposed/README.md) is now authored with advisory tests; SOURCE-order and SOURCE-events are separately accepted as presented; source materialization and runtime proof remain pending. Policy/error precedence, remaining physical bindings and freeze remain pending. All four PG designs, the database credential condition and all five EN designs are accepted within scope; exact physical bindings, content/retention, enrollment and run-window/capacity remain pending, and provisioning, shared-server application, network attachment and execution are not yet authorized. Keep supplied fixture contracts distinct from cold-builder-owned prompts, role-generation schemas, controller logic and checkpoint implementation. Close wire/error schemas, canonical identities, operator policy, hook/evidence and operational bindings against accepted behavior. Present substantive new choices for individual ratification; do not reopen settled semantics or treat drafting as implementation. Then settle campaign choices, freeze relevant fixtures, and implement/prove in the ratified sequence. The retrospective remains deferred until the end.

## Change log

| Revision | Date | Change |
|---|---|---|
| draft-1 | 2026-09-12 | All four EC decisions, companion runtime/local-HTTP choices, PostgreSQL engine, credential condition, all five EN, all four PG and all four WIRE designs accepted within scope; parent mutation rows reflect accepted pending-unresolved results; exact schemas/physical bindings/enrollment pending; no fixture implementation, new case or execution result |
