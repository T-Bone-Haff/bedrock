# Agent Code v2 ratification record

**Record id:** ACV2-RATIFICATION  
**Decision date:** 2026-09-06 (America/New_York)  
**Decision owner:** Tad Haffey  
**Subject:** Bedrock `agent-code` contract 2.0.0 amendment  
**Disposition:** Design decisions ratified; amendment enters `PROVING`

## Ratified dispositions

The operator ratified the following seven dispositions as a set:

1. **ACV2-D1 — Major version.** Advance `agent-code` from contract `1.0.0` to `2.0.0`, advance the portable core from `2.0.0` to `3.0.0`, and treat the package change as major. The package version is derived at landing from the manifest authority; `10.0.0` is the current expected value, not a pre-ratified release number.
2. **ACV2-D2 — Structural and semantic validation.** Use a closed JSON Schema for structural validity and a separate reusable deterministic validator for cross-field and execution-semantic invariants. Neither validator may claim the other's work.
3. **ACV2-D3 — Conservative salvage.** A load-bearing call may parse the whole payload and may remove exactly one declared outer Markdown fence. It may not search arbitrary surrounding text for an embedded valid payload. A bounded embedded-candidate scan is permitted only for a declared best-effort call and fails on zero or multiple valid candidates.
4. **ACV2-D4 — Uncertain side effects.** Represent indeterminate side-effect outcomes explicitly as `outcome_unknown` and require reconciliation. Automatic retry is prohibited until reconciliation establishes that retry is safe.
5. **ACV2-D5 — Provider profiles.** Ship schema-bound Anthropic, OpenAI, and Gemini profiles. A prose profile without schema validation and deterministic fixtures is not a conforming profile.
6. **ACV2-D6 — Request manifest.** Bind every execution record to an ordered context/request manifest. Shipped prompts are local immutable artifacts; remotely hosted prompts must be immutable, content-addressed references whose resolved bytes and identity are recorded.
7. **ACV2-D7 — Provider-neutral adoption floor.** Provider-neutrality is not adopted until all three provider profiles pass their required proof and at least one consumer exercises two providers through the same portable interface without weakening portable semantics.

## What this ratification does and does not establish

This record authorizes specification and proving work against the dispositions above. It does **not** establish that the amendment is implemented, compatible, verified, adopted, released, or propagated to any consumer. Current v1 artifacts and evidence remain historical facts; they are not silently converted into v2 evidence.

The next decision gate is adoption of an implementation candidate after all normative obligations in `agent-code-v2-standard-amendment.md` have evidence satisfying `agent-code-v2-proving-profile.md`.

## Consumer proving amendment — 2026-09-10 America/New_York

**Decision owner:** Tad Haffey  
**Source:** operator ratifications in the HEB-154 Codex deliberation task  
**Disposition:** ratified design; execution and adoption remain unproved

The operator individually ratified the HEX adoption gate, canonical repository locus, and distribution-only status of Linear attachments, then ratified the fulfillment-recovery proving scenario. The operator further required: "Let's ensure the scenarios are full execution of the skill's use for build AND the accuracy of the resulting agents."

- Fleet use of Agent Code in Agents of HEX is gated on HEB-154 reaching `ADOPTED`. Product definition may continue. Experimental agents built specifically for this proving campaign use the candidate skill before adoption and do not establish fleet readiness by their existence.
- `docs/evidence/heb-154/agent-code-v2/` is the canonical repository locus for this amendment and its proof. Linear descriptions and attachments are distribution/reference copies, not proof custody.
- The named consumer is a purpose-built fulfillment-recovery desk, owned by Tad Haffey, with Investigator, Recovery planner, and Correspondent agents and an application-owned deterministic controller. It uses fabricated business data, functioning tools and state, real provider calls, and independently evaluated outcomes. The SOFIA workbench is not its construction dependency.
- The consumer requirement permits this executable representative application. A test-only provider adapter or prewritten response demonstration remains insufficient.
- Proving must establish both complete use of the updated skill to build the agents and the accuracy of the resulting agents. Runtime conformance, build-use evidence, and outcome accuracy have separate verdicts; all are required.
- The campaign freezes cases and acceptance criteria before implementation, includes an evaluation population withheld from the builder, preserves clarifications and corrections, evaluates facts and effects independently of agent narration, and exercises the same workload through at least two providers plus a mixed-provider configuration.
- All original stable obligations, frozen contract fixture expectations, three-provider live checks, independent review, operator acceptance, landing, and cold acceptance remain required. This amendment changes the representative consumer and strengthens its proving work; it does not waive those gates.

These decisions amend the standard's consumer gate and proving profile section 7. The effective proving-profile revision is `1.1.0`. This is a proving-profile revision, not a package or Agent Code contract release.

Concrete scenario records, hidden evaluation custody, selected provider identities, numeric evaluation thresholds and repeated-draw policy, budgets, and content-retention arrangements still require the pre-implementation freeze. Proposed details are identified in `consumer-proving-design.md`; their inclusion does not imply ratification or completed proof.

## FRD-W1 — Desk completion boundary — ratified 2026-09-10 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the W1 completion-boundary question in the HEB-154 Codex deliberation task  
**Disposition:** ratified design

The desk completes its charged task when a stock reservation is confirmed, the approved recovery arrangement is recorded against the correct order, and an accurate customer draft and operator summary exist. The business outcome is `recovery_arranged`.

Shipping execution remains downstream. A reservation and selected transport quote do not establish shipping booking, dispatch, or delivery. Message transmission and payment charging are separate effects outside this first world's charge. The agents must report the actual status and remaining work accurately.

This ratification settles W1 only. W2–W6, concrete example values, the scenario freeze, and execution/accuracy results are not ratified by this response. The current business decision set is in `business-world-and-reference-case.md`.

## FRD-W2 — Order shape — ratified 2026-09-10 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the W2 order-shape question in the HEB-154 Codex deliberation task  
**Disposition:** ratified design

Each case contains one order line with a specified model, a whole-unit quantity, and one destination. The entire quantity comes from one fulfillment source. Multiple orders may run concurrently and compete for inventory. Substitutions require explicit customer permission.

The initial proving population excludes split fulfillment across multiple sources. Partial execution remains in scope, including a successful reservation followed by failure of the order-arrangement update. This scope supports interpretation, quantity checks, competing plans, inventory contention, authorization, and recovery without requiring split-shipment construction.

This ratification settles W2. W3–W6, concrete example values, scenario freeze, and execution/accuracy results require their own evidence or dispositions. W1 remains ratified.

## FRD-W3 — Authority by fact — ratified 2026-09-10 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the W3 authority-by-fact question in the HEB-154 Codex deliberation task  
**Disposition:** ratified design

Authority is specific to each fact and its effective record version. Accepted customer requirements govern model, quantity, substitution permission, destination, deadline, and extra-cost cap. Current inventory governs availability. Applicable transport quotes govern their quoted cost, arrival estimate, and expiry. Confirmed effect records and reconciliation govern actual effects. Scoped operator approval governs permitted mutations.

A newer informal message does not override an owning source merely because of its timestamp. Refresh stale or conflicting evidence through permitted interfaces; an explicit accepted revision may resolve a conflict. If equally authoritative current records still disagree, preserve uncertainty and seek clarification from the owning authority. A missing operation response leaves the effect unresolved pending reconciliation; it does not establish failure.

This ratification settles W3. W4–W6, concrete example values, scenario freeze, and execution/accuracy results require their own evidence or dispositions. W1–W2 remain ratified.

## FRD-W4 — Acceptable recovery — ratified 2026-09-10 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the W4 acceptable-recovery question in the HEB-154 Codex deliberation task  
**Disposition:** ratified design

Any plan satisfying every hard constraint is acceptable: the correct model or an explicitly permitted substitution, complete quantity, correct destination, sufficient current stock, a valid quote, estimated arrival at or before the deadline, and extra cost for the entire order at or below the cap in the specified currency. Deadline and cost boundaries are inclusive; quote expiry is exclusive, so a quote becomes unusable at its expiry time.

No unstated cheapest or fastest objective is imposed. An agent making a comparative claim must substantiate it against the available feasible choices. The proposed West and East plans illustrate two acceptable answers; evaluation must recognize multiple correct choices without treating the example values as frozen.

This ratification settles W4. W5–W6, concrete example values, scenario freeze, and execution/accuracy results require their own evidence or dispositions. W1–W3 remain ratified.

## FRD-W5 — Approval and actual effects — ratified 2026-09-10 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the W5 approval-and-effects question in the HEB-154 Codex deliberation task  
**Disposition:** ratified design

The operator approves a specific, versioned recovery plan before any state change. One scoped approval may cover both operations: reserving the selected inventory, then recording the recovery arrangement against the order with a link to the confirmed reservation.

Each operation has a stable identity and an independently observable result. Before each operation, the deterministic controller verifies that relevant preconditions and approval still hold. Changes outside the approved scope require fresh approval.

A confirmed reservation followed by a failed or uncertain arrangement update remains partial completion. The agents must represent that status accurately, and uncertain effects require reconciliation before any retry can be established as safe. Neither a duplicate reservation nor an unsupported completion claim is an acceptable recovery.

This ratification settles W5. W6, concrete example values, scenario freeze, and execution/accuracy results require their own evidence or dispositions. W1–W4 remain ratified.

## FRD-W6 — Required agent work — ratified 2026-09-10 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the W6 required-agent-work question in the HEB-154 Codex deliberation task  
**Disposition:** ratified design

All three agents are required on the ordinary successful path, each with its own call contract and independently evaluated output. The Investigator accurately interprets requirements and establishes source-backed facts. The Recovery planner selects an acceptable plan with a supported explanation. The Correspondent produces an accurate customer draft and operator summary from confirmed outcomes.

If the Correspondent fails, completed reservation and arrangement effects remain real, but communication stays pending and the full task is incomplete. A later agent's correct answer does not erase an earlier agent's mistake from evaluation. Best-effort parsing remains separately tested and cannot excuse omitting required work.

This ratification settles W6 and completes the W1–W6 business-world decision set. Concrete example values, the complete scenario population, oracle controls, campaign freeze, and execution/accuracy results still require their own dispositions or evidence. The requirement to prove complete skill use during construction and resulting-agent accuracy remains in force.

## SP-1 — Concrete public population — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the SP-1 question following the combined-case review in the HEB-154 Codex deliberation task  
**Disposition:** public development membership and concrete values ratified; campaign not frozen

Use all 37 named variants and their concrete values in the public development pack, preserving the isolated cases, matched effect/no-effect and missing/resolved-fact cases, mirrored contention, and combined FRD-14A/B/C trio including permitted substitution. The complete public membership is listed in [the case index](scenario-and-oracle-pack.md#4-complete-public-case-index) and defined in [the concrete pack](scenarios/proposed/scenario-pack.json). Hidden instances, repeated draws, exact provider runs and original AC2/LP fixtures are outside this population count.

The reviewed pre-ratification `scenario-pack.json` byte identity is SHA-256 `d13231d3371e380a498d4229ad38960ae21c7e7028bb361b68ab15b79dc45758`. Recording this decision changes decision metadata, not the cases or their values. This identity records the approved substrate; it is not the future physical campaign freeze.

SP-2 recovery/stopping policy and SP-3 oracle/result meaning remain proposed. Hidden evaluation sampling and custody, numerical acceptance criteria, execution bindings, aggregate budgets, content policy and campaign freeze remain separate gates. This ratification authorizes neither live spend nor adoption and establishes no execution or agent-accuracy result.

## SP-2 — Bounded recovery and stopping — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratify the recommendation" to the SP-2 recommendation in the HEB-154 Codex deliberation task  
**Disposition:** proving-application recovery/stopping policy ratified; campaign budgets and freeze remain open

Allow only the clarification, reconciliation, replay, replan or restart explicitly granted by each case, within its stated limit. Designated injected generation failures receive no retry in the failing invocation. These bounded allowances are ceilings, not permission to exceed applicable authority or aggregate budgets.

Cancellation stops new agent work. Confirmed reservations remain held unless release is separately authorized; uncertain effects remain uncertain until supported reconciliation settles them. Cancellation does not imply release, reversal or compensation. Retries and restarts preserve the original logical operation identity and accumulated budget; a changed approved plan retains the pack's requirement for a new scoped identity and fresh approval.

This is the fulfillment-recovery proving application's policy, not a universal restriction on future HEX agents or a new portable Agent Code requirement. Bounded recovery makes uncertainty, authority and stopping behavior observable rather than optimizing these cases for maximum eventual completion.

The reviewed pre-ratification `scenario-pack.json` byte identity is SHA-256 `bd9fa90efc4fb3af27a681ff84bb5b00f816d427eaa08b9605803865a8240dbe`. Recording this decision changes decision metadata, not the existing case allowances, schedules, values or oracle definitions.

SP-1 remains ratified. SP-3 oracle/result meaning, exact campaign budgets, execution bindings, hidden custody, sampling, numerical acceptance, content policy and physical freeze remain separate gates. No implementation, calibration, live spend, execution result or adoption is established by this ratification.

## SP-3 — Oracle and result meaning — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "Ratified. What is next?" to the SP-3 recommendation in the HEB-154 Codex deliberation task  
**Disposition:** oracle/control acceptance design and result meaning ratified; implementation, calibration and campaign freeze remain unproved

Accept the pack's independent state, authority, knowledge, plan and communication predicates and paired controls. Evaluate facts, permissions, plans and actual effects against authoritative inputs and inspected state, not agent narration. Evaluate each claim against what its author could know when it was made: a lucky hidden-state guess, materially incomplete communication or misleading claim fails the applicable criterion.

Use deterministic checks where mechanically decidable, with independently calibrated semantic judgment for the remainder. Known correct, incorrect, incomplete and fluent-but-false controls must demonstrate evaluator discrimination before those evaluators are trusted. Consequential unresolved judgments require adjudication; a second model name alone does not establish independence.

Report natural first-attempt accuracy, recovered performance and injected-fault handling separately. Retain first failures, missing/null outputs, rejected outputs, later corrections and missed fault exposures. An unreached fault cannot be credited as successfully handled. The existing independent `build_use`, `runtime_conformance` and `outcome_accuracy` verdicts all remain required; no combined score substitutes for a failed dimension.

The reviewed pre-ratification `scenario-pack.json` byte identity is SHA-256 `92409aa9bcf5a63c379112325c159cb0854a076a7babf02bd4c0e569d24bb2c3`. Recording this decision changes decision metadata, not the case data, oracle predicates or control specimens.

SP-1–SP-3 are now individually ratified. This settles the public pack's acceptance design, not evaluator implementation or successful calibration, numerical thresholds, hidden population/custody, exact execution/provider bindings, budgets, content policy or physical campaign freeze. No agent execution, accuracy result, live spend or adoption is authorized or established by this ratification.

## EXEC-SEQUENCE — Execution-contract next step — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified the sequence and next step" to the post-SP-3 recommendation in the HEB-154 Codex deliberation task  
**Disposition:** sequence and execution-contract drafting authorized; new boundary choices remain proposed

1. Define the execution boundaries: exact tool requests/results, state transitions, reservation/reconciliation journal, restart persistence, fault-injection points and evaluator inputs. Specify the cold builder's supplied material versus evaluator-only material without prebuilding the agents to be observed.
2. Settle provider/model configurations, numeric accuracy thresholds, repeated draws, budgets, hidden-case custody, evaluator calibration and reviewable synthetic-content retention through explicit substantive ratifications.
3. Freeze the relevant physical fixtures before implementing their validators; implement and verify the Agent Code 2.0 candidate; then conduct the isolated consumer build and execution campaign using that candidate, subject to all existing gates.

The immediate deliverable is a compact [execution-contract draft](execution-contract.md) within the existing pack, beginning with tool/state/reconciliation boundaries. This authorization does not ratify new EC choices in the draft, authorize fixture/product implementation or live spend, waive the freeze, or establish proof. The retrospective remains deferred until the end.

## EC-boundary — Division of work and access — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the EC-boundary division-of-work/access recommendation in the HEB-154 Codex deliberation task  
**Disposition:** ownership and access boundary accepted; physical bindings and remaining EC decisions stay proposed

Supply independently implemented, functioning synthetic business services. The cold builder creates all three product agents and their prompts/generation contracts; the deterministic controller, authorization checks, budgets, dispatch and reconciliation logic; and application checkpointing, communication handling, tests and evidence.

The supplied services provide authoritative records and actual reservation/arrangement operations. They must not generate plans, correct agent answers, orchestrate recovery or decide whether the desk completed successfully. Fixture administration and evaluator data remain inaccessible to the application. This supplies a controlled environment whose behavior can be checked independently while preserving the full observed agent-building experiment; giving the same builder responsibility for the business-world machinery would broaden the experiment and make failures harder to attribute.

The reviewed execution-contract draft byte identity is SHA-256 `92e5faf7dd83b821520ca74f2c10b7c0e7043c661b64a152a53b02ca85219788`. Acceptance applies to the division of work and access above, not every proposed field or mechanism in that draft. Exact protocol/schema, process/transport/persistence and enforcement choices, EC-operation-journal, EC-state-commit and EC-event-evidence remain open. The physical freeze, implementation and verification gates remain in force; this ratification proves neither isolation nor functioning services and authorizes no live spend.

## EC-operation-journal — Logical effects and physical attempts — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the EC-operation-journal recommendation in the HEB-154 Codex deliberation task  
**Disposition:** operation/attempt identity, authoritative finality and single-use replay-permit design accepted; implementation and proof pending

Use one durable logical-operation record with a separate record for every physical attempt. A retry retains the operation key and receives a new attempt ID. After an uncertain result, committed reconciliation recovers the original effect/result without re-executing it; definite non-application must prove that the original attempt cannot commit later before issuing a single-use replay permit; unresolved reconciliation preserves uncertainty and prohibits automatic replay.

No-effect closure closes the prior attempt, not the logical operation permanently. Bind the replay permit to the operation, effect parameters and journal version. Permit consumption must prevent competing retries or a delayed original request from creating duplicate effects. The permit establishes service replay safety, not another business approval or extra budget: current authorization, quote validity, case allowance and aggregate budget still govern the replay. This preserves the distinction between recovering an existing reservation in FRD-14A and safely creating one after finality in FRD-14B.

The reviewed execution-contract draft byte identity is SHA-256 `f95d99b37c67ba0a64980d6ab783520fe73ace8a0075d3ed8887adb959a89384`. EC-boundary remains accepted. EC-state-commit, EC-event-evidence and exact physical schema/transport/persistence/enforcement bindings remain open. No journal implementation, successful fence or deduplication test, live spend, cold build, campaign freeze or adoption is established by this ratification.

## EC-state-commit — Separate atomic business operations — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the EC-state-commit recommendation in the HEB-154 Codex deliberation task  
**Disposition:** transaction, partial-completion, restart/cancellation and service-status behavior accepted; physical bindings and proof pending

Use two separately atomic business operations, each committing its actual state changes and journal result together. Reservation validates current authority, references and stock, decrements stock and records the reservation without amending the order. A uniqueness guard prevents another active allocation for the same run/order even under a different operation key. Arrangement validates the grant and matching confirmed reservation, conditionally updates the expected order revision, attaches the approved recovery terms and records the arrangement without another stock decrement or rewriting the original customer request.

Each operation is all-or-nothing; the pair is not one transaction. Reservation success followed by arrangement failure leaves stock held and the order unamended, with no automatic rollback. This preserves a genuine partial-completion problem whose handling and reporting can be independently evaluated. Lost responses preserve uncertainty until reconciliation: actual commitment and application knowledge remain distinct.

Restart preserves durable dispatch intent, operation identity and consumed budget. Cancellation stops new work without erasing effects. Use `arrangement_recorded` for the service state; reserve `recovery_arranged` for full desk completion, including accurate communication.

The reviewed execution-contract draft byte identity is SHA-256 `b23885c3f49b8b0901741b3c7145007778140a7d2d14911312f05b863b62578e`. EC-boundary and EC-operation-journal remain accepted. EC-event-evidence, database/transport choice, exact physical schemas and enforcement bindings remain open. This accepts the behavior above, not every proposed record field, a frozen schema, fixture implementation, successful transaction/restart test, live spend, cold build or adoption.

## EC-event-evidence — Execution-boundary injection and independent evidence — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the EC-event-evidence recommendation in the HEB-154 Codex deliberation task  
**Disposition:** event-injection and evidence design accepted; physical bindings, custody/content permission, calibration and proof pending

Inject at actual named execution boundaries, including commit, response delivery, checkpoint and parsing, rather than elapsed sleeps. Enforce prerequisites, causal order and one-shot execution. Keep simulated business time separate from real execution budgets.

Retain three correlated evidence views: actual service commitments; what the application received, knew and claimed; and independent evaluator expectations and conclusions. This distinguishes a supported correct statement from a lucky guess about hidden state. The harness supplies neither solutions nor hidden labels to the agents, and evaluation has no correction channel into the first run.

Never manufacture fault exposure. If a run fails before reaching its injection point, retain the actual failure and mark the intended fault unexposed. In particular, do not manufacture valid JSON merely to run a planned corruption. Preserve missing outputs, original versus transformed responses, subsequent corrections and recovery costs; report natural accuracy, recovered performance and injected-fault handling separately.

These rules make the experiment repeatable without scripting the agents' answers. Full construction evidence and the separate `build_use`, `runtime_conformance` and `outcome_accuracy` verdicts remain required. The reviewed execution-contract draft byte identity is SHA-256 `8caba294070e55bc2a82e541b4b95290d531e0042f21e6733d6996441e777efb`.

All four EC boundary decisions are individually ratified. This accepts their stated design, not every proposed field or exact physical hook, database/transport/access mechanism, content-retention permission, hidden custody, calibration, campaign freeze or successful proof. It authorizes no fixture/agent implementation, live spend or adoption beyond the previously ratified sequence and gates. The next work remains completion of the physical execution bindings, followed by the outstanding campaign choices and freeze before governed implementation/evaluation.

## PB-runtime — Local Compose trust-boundary model — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to the PB-runtime recommendation in the HEB-154 Codex deliberation task  
**Disposition:** local Compose trust-boundary model, including transport-only provider egress, accepted; transport, persistence and enforcement proof remain open

Use a local Docker Compose fixture with explicit application, business-fixture and offline-evaluator access boundaries. The cold-built agents and controller own their durable checkpoints. The business fixture owns authoritative state, journal, grants and fault scheduling outside the application's filesystem access. The offline evaluator receives read-only evidence and separately held expectations, with no correction channel into the first run.

Include a provider egress relay that performs transport only: no prompt construction, provider adaptation or automatic retries. The host custodian controls lifecycle and deliberate crashes. The application receives neither the Docker API nor broad host/repository mounts. The inspected Mac's Docker/Compose availability supports this local choice, but is one host's read-only observation, not an isolation or reproducibility test.

Runtime isolation does not establish cold-builder isolation. The actual builder's tools, connectors and inherited context still require a separately verified boundary. The current task remains the deliberation/authoring task, not the cold builder.

The reviewed physical runtime-binding draft byte identity is SHA-256 `49e793dbc6bba91f53460b1db268d3ca8e643afef57e49a22196c33e1eea1bfb`. Acceptance applies to the trust-boundary model and transport-only relay above, not every proposed network name, socket, route, record field or launch setting in the draft. PB-transport and PB-persistence remain proposed; exact schemas, launch configuration, campaign settings, builder custody, content permission and physical freeze remain open. No container operation, fixture/agent implementation, live spend, successful access/crash test or adoption is established or newly authorized by this ratification.

## PB-transport — Local HTTP with separate private control — accepted as amended 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** operator response to the PB-transport recommendation: "the only modification for the test that I would make is http instead of https...don't need the certificate overhead on this proving run."  
**Disposition:** PB-transport accepted with HTTP substituted for HTTPS on the local fixture interfaces; PB-persistence and exact physical bindings remain open

Use direct, versioned HTTP/JSON between the cold-built application and supplied fixture, including action and observation/hook interfaces. Omit fixture certificates, trust bundles and certificate-lifecycle setup for this synthetic local proving run. The operator's rationale is to avoid that overhead. This amends the reviewed proposal, SHA-256 `82f8385227379739d49e9f03204dc44d7626c6df9f7032e6ea061105951be1af`; its server-authenticated TLS recommendation is not accepted for these fixture interfaces.

Keep the remainder of PB-transport: scoped opaque header credentials distinct from business approval; identity-matching typed outcomes rather than HTTP-status finality; every physical dispatch recorded and budgeted, with no implicit retries and journal-governed replay; actual lost-response boundaries; non-coaching observation hooks; and private administration through the fixture's private socket and host custodian, inaccessible to the application.

The HTTP choice is bounded to the private, single-host container network with no host-published fixture/admin ports. It provides no transport encryption or cryptographic service authentication; private network placement is not TLS-equivalent protection. External model-provider connections retain end-to-end TLS, and provider credentials are not fixture credentials. Actual access enforcement remains to be proved. Broader exposure or non-synthetic business data reopens this local proving-run decision; it does not create a production or HEX-wide transport rule.

PB-runtime remains accepted. PB-persistence, exact routes/wire/error schemas, launch configuration, builder/evaluator custody, campaign settings, physical freeze and verification remain open. This acceptance changes no public scenario bytes and establishes no implementation, execution result, agent accuracy or adoption proof.

## PB-persistence — PostgreSQL engine, conditional instance enrollment — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to "Do you ratify PostgreSQL as the persistence engine, leaving enrollment of the existing instance subject to the access and lifecycle check?"  
**Disposition:** PostgreSQL engine accepted; existing-instance enrollment remains conditional, not authorized by availability alone

Use PostgreSQL behind the business-service fixture. This supersedes the unaccepted SQLite recommendation: its rationale was lower setup cost, and the operator supplied local PostgreSQL availability that a read-only inspection confirmed. The preceding document identity was SHA-256 `c74cea41371d55cb2475465ecf6db50e4233f0542ccc0aa80b76a5250172bd53`; that document still described SQLite. This ratification accepts the subsequent PostgreSQL recommendation in the deliberation task, not the superseded SQLite text.

Preserve the accepted separate reservation/arrangement transactions, atomic effect/journal commitments, durable operation/attempt history, fences, single-use replay permits, partial-completion behavior and application-owned checkpoints. Agents continue through the HTTP fixture interface rather than direct SQL. PostgreSQL-specific isolation/locking, conflict handling and consistent evidence export must be bound; no automatic business replay or finality claim follows from a database error. This engine choice does not prescribe the cold builder's checkpoint technology or HEX fleet architecture.

The proposed reuse path is dedicated HEB-154 databases and restricted fixture credentials on the available server, subject to access/lifecycle checks. Enrollment, exact database/role/network/credential bindings, campaign settings, physical freeze and execution proof remain pending. No shared server configuration change, existing-data change, database/role/certificate provisioning, restart or server-wide crash test is authorized by this ratification.

Subsequent read-only enrollment inspection found that the current authentication file declares TLS plus client certificate and SCRAM password for TCP connections, with TLS enabled in effective server settings. Its complete mounted files and parsed rule rows were read; actual fixture TCP authentication/denial was not tested, and the parsed view does not prove the last loaded rules. Whether to accept this database-specific credential setup remains a new operator decision. The prior local-HTTP decision is unchanged. Evidence and the pending recommendation are retained in the [physical binding](physical-runtime-binding.md) and its [PostgreSQL authoring/inspection report](scenarios/proposed/pb-persistence-postgresql-authoring-checks.json).

## PB-persistence — Database credential condition — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratify" to "Do you ratify accepting the database-only certificate requirement for reuse of this instance?"  
**Disposition:** database-only certificate/credential condition accepted; existing-instance enrollment remains pending

Preserve the existing PostgreSQL security for the proposed reuse path: use a fixture-specific restricted login and password plus a matching client certificate, with server-identity validation. This closes the additional credential decision surfaced by the preceding read-only inspection. Application-to-fixture traffic remains plain HTTP as ratified; external provider TLS remains unchanged. Do not weaken shared HBA/TLS settings, reuse workbench credentials or make privileged Docker exec the fixture's authentication bypass.

The reviewed physical runtime-binding draft byte identity is SHA-256 `7a1933876a851cc351ce67b44d04f03402ae80c72b0b943af01f1d528666565a`. Acceptance applies to this credential condition, not every proposal in that draft. Exact network route, database/role permissions, credential issuance/custody, resource headroom and shared-instance lifecycle arrangements remain to be settled and verified before enrollment. No database/role/certificate provisioning, network or shared-server change, restart, existing-data mutation, campaign execution or adoption is newly authorized. The preceding inspection is not a fresh runtime result or successful authentication/isolation test.

Next consolidate those remaining enrollment bindings into one reviewable proposal, retaining individual ratification for substantive choices. The [credential-ratification authoring report](scenarios/proposed/pb-persistence-credentials-authoring-checks.json) records document checks only; the retrospective remains deferred until the end.

## EN-access — Scoped authentication guard — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to "Do you ratify EN-access as the design direction—without yet authorizing its application to the shared server?"  
**Disposition:** EN-access accepted as design only; shared-server application and enrollment remain unauthorized/pending

Accept an HEB-154-specific authentication block before the existing broad PostgreSQL TCP rules: allow the exact active fixture identity/database/source under the accepted TLS, matching client certificate and SCRAM requirements; reject its other TCP database/replication paths, including plaintext and alternate IP families. Preserve the existing workbench authentication rules and database grants. The preceding ACL inspection exposed why a new login without direct grants is insufficient: the workbench database currently grants connection permission through `PUBLIC`. This ratification does not refresh that historical observation into a new access test.

Retain the controlled-application safeguards: reconcile fixture-role membership and exact allow rules, validate with the actual runtime identity before campaign admission, prove the guard first on a disposable synthetic instance, preserve a verified configuration preimage, and require a controlled reload plus an unchanged-workbench connection check. A failed validation blocks admission; restoration must respect intervening edits. Do not weaken TLS, revoke existing workbench `PUBLIC` grants, reuse workbench credentials or restart the shared server as recovery.

The reviewed physical runtime-binding draft byte identity is SHA-256 `6a0791c058b96fee48887543f13ceb3a47714c15a95784501bacee3535549a0d`. Acceptance is of EN-access's guarded design direction, not a freeze of every identifier/rule byte or acceptance of EN-route, EN-scope, EN-custody or EN-lifecycle. No shared file edit, reload, network attachment, role/database/certificate provisioning, campaign execution or adoption is authorized by this ratification. Exact bindings, implementation and actual allow/deny evidence remain pending. Application-to-fixture HTTP and provider TLS are unchanged.

Next review EN-route individually. The [EN-access authoring report](scenarios/proposed/en-access-ratification-authoring-checks.json) retains document checks only; the retrospective remains deferred until the end.

## EN-route — Dedicated internal database bridge — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "rratified" to "Do you ratify EN-route as the design direction, leaving network attachment and verification for a later authorized step?"  
**Disposition:** EN-route accepted as design only; network creation/attachment, verification and instance enrollment remain pending

Accept a dedicated HEB-154 internal database bridge per active run, connecting only the fixture and the exact enrolled PostgreSQL container. Preserve PostgreSQL's existing workbench network attachment, published-port binding and default route. Treat that server as an external dependency that the proving project's Compose lifecycle cannot recreate or remove. Do not put the fixture on the workbench bridge, attach the application/provider relay/evaluator to the database bridge, publish another host port, or use host networking/general host-gateway access.

Retain database TLS with server-identity verification and dedicated fixture credentials. Bind the fixture's HTTP listener only to its business-network interface, so the added database interface does not expose the HTTP service. Preserve the proposed IPv4-only database bridge and require checks of alternate IPv4/IPv6 paths, effective network membership and permitted/denied access before use. Network declarations alone are not isolation proof; the existing certificate inspection is not a live-handshake result. Application-to-fixture HTTP and external provider TLS remain unchanged.

The reviewed physical runtime-binding draft byte identity is SHA-256 `e903e66a78387f12cabb9464254eaffab82e5c4aaa1d89042b6d003eb3c91b05`. Acceptance applies to EN-route's design direction, not a freeze of exact network names, run-token encoding, CIDRs, endpoint addresses, launch bytes or every other proposal in the draft. EN-scope, EN-custody and EN-lifecycle remain proposed. No network/container operation, shared configuration edit/reload, database/role/certificate provisioning, campaign execution or adoption is authorized by this ratification.

Next review EN-scope individually. The [EN-route authoring report](scenarios/proposed/en-route-ratification-authoring-checks.json) retains document checks only; the retrospective remains deferred until the end.

## EN-scope — Separate run storage and runtime permissions — ratified 2026-09-11 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to "Do you ratify EN-scope as the design direction, leaving exact grants and provisioning for the later implementation gate?"  
**Disposition:** EN-scope accepted as design only; exact grants, provisioning and isolation verification remain pending

Accept one fresh fixture database per run, a restricted runtime login and a separate non-login maintenance owner. Concurrent orders within a case share that database; the designated restart retains its database, login and run identity. Initialize from a clean template without workbench schemas or data. Keep schema initialization/migration and scoped export under host-custodian maintenance authority, outside normal fixture execution.

Grant the runtime only its explicitly required operations, with no ownership, schema-change or privilege-administration authority. Preserve append-only history restrictions rather than granting the update/delete/truncate permissions used by mutable state. Remove broad `PUBLIC` access only on the new run database and its user-defined schemas/functions; leave workbench grants and system catalogs/built-ins unchanged. Exact object grants must follow the frozen schema. No broad future-object grants, privileged workbench credentials or automatic cleanup follows from this acceptance.

This makes run ownership explicit and separates maintenance authority from runtime use; the trade-off is additional database/role provisioning and a schema-specific grant map. It governs fixture persistence, not the cold-built application's separate checkpoint technology. Shared-server administrators remain trusted, shared catalog metadata can remain visible, and database separation is not resource isolation or an executed access test.

The reviewed physical runtime-binding draft byte identity is SHA-256 `62759845bddcce6a7032912d4ac5fd015b2ca1b3c6bc8dbc6d57438a6fdac494`. Acceptance applies to EN-scope's design direction, not exact identifiers, object grants, DDL, EN-custody or EN-lifecycle. No database/role/grant/certificate provisioning, shared-server edit/reload, network attachment, campaign execution or adoption is authorized. Application-to-fixture HTTP, provider TLS and the previously accepted boundaries remain unchanged.

Next review EN-custody individually. The [EN-scope authoring report](scenarios/proposed/en-scope-ratification-authoring-checks.json) retains document checks only; the retrospective remains deferred until the end.

## EN-custody — Dedicated client credentials and host custody — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratify" to "Do you ratify EN-custody on those terms, with actual issuance still separately gated?"  
**Disposition:** EN-custody accepted as design only; actual issuance, provisioning and credential-isolation verification remain pending

Accept Tad as accountable custodian and a host-controlled issuance operation scoped only to the named HEB-154 client leaf under the existing database CA. Keep that CA's private key in place and preserve existing CA/server/workbench credential material. The previously inspected initializer is not an HEB-154 issuer; a separately identified operation must avoid incidental renewal, CA regeneration and shared serial-file races. No signer is selected, built or executed by this ratification.

Retain the run key/password in restricted per-run storage outside the repository, cold-builder context, model text and evaluator evidence. Supply only the run's client certificate/key/password and public CA to the fixture, read-only with verified effective ownership for its non-root process. Do not mount the shared PKI volume or export shared private keys. Evidence records only non-secret identity and public certificate fingerprints.

Accept a maximum 30-day client-leaf lifetime covering the declared run window, with no silent renewal. Retain credentials required for restart/export until those obligations close; final retention and cleanup remain separate decisions. Disabling a run login is containment, not certificate revocation or termination of existing sessions; any session closure must target the identified HEB-154 run. Exact private-store paths, issuance implementation and validity windows remain freeze bindings.

This limits fixture exposure and issuance authority while reusing the existing trust anchor; the trade-off is a dedicated issuance operation and explicit credential lifecycle handling. It establishes intended custody, not proof of secret isolation or a live authenticated connection.

The reviewed physical runtime-binding draft byte identity is SHA-256 `c5b75dcad39724bd8ec5cd41748ffcd66191b54224c0ce3f2b3b637c437ba648`. Acceptance applies to EN-custody only, not EN-lifecycle, actual issuance/provisioning, shared-server edits/reloads, network attachment, implementation, campaign freeze, runtime proof or adoption. Application-to-fixture HTTP, provider TLS and the previously accepted boundaries remain unchanged.

Next review EN-lifecycle individually. The [EN-custody authoring report](scenarios/proposed/en-custody-ratification-authoring-checks.json) retains document checks only; the retrospective remains deferred until the end.

## EN-lifecycle — Serial run windows and bounded shared usage — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified." to "Do you ratify EN-lifecycle on these terms, with the actual run window and execution still separately gated?"  
**Disposition:** EN-lifecycle accepted as design only; actual run window, capacity checks, provisioning and execution remain pending

Accept one proving run at a time on the shared instance, preserving all concurrency required inside its case. The actual window must be separately confirmed without workbench workload, migrations, PKI renewal, container recreation, server-setting changes or host sleep. This acceptance does not authorize stopping workbench services.

Accept four fixture SQL connections with no overflow, plus at most two scoped custodian/export connections. Leave the server connection limit unchanged and keep its reserved emergency slots outside fixture use. These are usage ceilings, not measured capacity or proof that every case fits. Admission requires available ordinary connection slots and resource headroom; exact connection/statement/lock timeouts and bounded export duration remain bindings to settle. If the envelope cannot fit while preserving a case's required concurrency, revisit hosting rather than weaken the case or change shared-server resources implicitly.

At admission, record the actual instance/image, network endpoints, database/role/grant map, mounted configurations, public certificate identities, selected effective durability settings and capacity observations. Relevant unapproved drift, container recreation, unexpected shared-server loss or resource exhaustion stops admission and preserves affected evidence as unavailable. No silent replacement, repair of the first result or unrecorded rerun follows. Application-crash tests retain PostgreSQL; shared-server crash/restart and host-power-loss tests remain excluded.

Preserve and verify the scoped database export and isolated restore before cleanup. Later login disabling or removal of run-owned database/role/network objects requires the exact run manifest and appropriate approval. Retained evidence and credentials are not silently discarded. Removing the owned HBA block or attachment remains a later retirement gate after checking active-run dependencies and intervening configuration changes; no wildcard drops, shared-volume deletion or proving-project teardown of the server.

These boundaries reduce unrelated-workload interference with the proof and bound shared-resource use. The trade-off is an operator-reserved window and admission/retirement work, not evidence that a suitable window or adequate capacity already exists.

The reviewed physical runtime-binding draft byte identity is SHA-256 `a0816b94f294be7bce4271535539707c5ec130a49e599ca2857b310021b20beb`. This closes the five EN design-direction decisions only; exact enrollment, remaining physical/campaign bindings, implementation, runtime verification and adoption remain open. No provisioning, certificate issuance, shared-server edit/reload, network attachment, service stop, export/restore, cleanup or campaign execution is authorized by this ratification. Application-to-fixture HTTP and provider TLS remain unchanged.

The next recommendation is to develop the PostgreSQL schema/transaction/export contract against accepted behavior, with substantive new choices returned for ratification. The [EN-lifecycle authoring report](scenarios/proposed/en-lifecycle-ratification-authoring-checks.json) retains document checks only; the retrospective remains deferred until the end.

## PG-state — Relational state and append-only history — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "Ratified" to "Do you ratify PG-state’s relational-state-plus-append-only-history approach, leaving exact DDL/grants and the other three PG decisions open?"  
**Disposition:** PG-state accepted as design direction only; exact DDL/grants and PG-transaction, PG-finality and PG-export remain open

Accept typed relational current state plus append-only source/effect/attempt/event history, with original evidence bytes preserved separately from parsed projections where the eventual content policy permits. Current projections must not erase the history needed for independent reconstruction. This retains enforceable relational structure and before/after evidence without adding a full event-sourcing framework or treating one mutable JSON document as the complete state/history record.

The proposed relation inventory is not ratified executable DDL: exact names, columns, types, keys/constraints, canonical encodings and object/column grants remain physical bindings to settle. References to transaction order, generation fences, replay permits and final sealing in that inventory do not accept the other PG mechanisms. Content retention, exact enrollment, campaign bindings and the separate application-checkpoint choice remain open within their prior scopes.

The reviewed PostgreSQL persistence-contract draft byte identity is SHA-256 `7d18ddd6c9f279c4eb53672e07a1d683cdc742b9d58eae9538830a9548321017`. This acceptance does not authorize DDL, grant changes, provisioning, shared-server edits, network attachment, credential issuance, export/restore, fixture or agent implementation, live-provider spending, freeze or execution. No SQL correctness, access enforcement, skill-build use or resulting-agent accuracy is proved by ratification.

The next recommendation is PG-transaction, including its interaction with the still-proposed PG-finality mechanism, followed by individual PG-finality and PG-export dispositions. The [PG-state authoring report](scenarios/proposed/pg-state-ratification-authoring-checks.json) retains the scoped document checks and unchanged public-pack/reference identities. Prior evidence remains untouched; the retrospective remains deferred until the end.

## PG-transaction — Explicit locks, separate commits and no automatic effect retry — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "Ratified" to "Do you ratify PG-transaction on these terms, including no automatic effect-transaction retries, leaving numeric limits and PG-finality open?"  
**Disposition:** PG-transaction accepted as design; numeric limits, exact DDL/grants, PG-finality and PG-export remain open

Accept short Read Committed write transactions with a fixed row-lock order: run guard, operation, order, stock, then subordinate attempt/permit and schedule projections. Ordinary mutations use the short shared catalog/clock guard; publication uses the exclusive guard. Coherent multi-record reads use a short Repeatable Read read-only snapshot. This chooses explicit locking for the finite fixture over a general Serializable/retry policy or a run-wide exclusive mutation lock that would unnecessarily suppress required concurrency.

Recheck current authority, references, stock/order predicates and attempt eligibility inside the effect transaction. Commit each effect with its original terminal result and append-only history/event record. Reservation and arrangement remain separate commits; a later failure does not erase an earlier reservation. Admission commits before its hook. Hooks, barriers, provider calls, response delivery and collector waits retain neither an open transaction nor a checked-out connection.

Accept no automatic effect-transaction retries in this proving fixture. Preserve unexpected SQL failure and distinguish confirmed rollback from unknown commitment; neither silently re-executes the business effect. A confirmed rollback does not undo earlier admission or a separate committed operation. Only a confirmed finality transaction can establish its own closure; uncertainty follows the permitted journal path and remains unresolved if that path is unavailable. Unexpected deadlock/timeout may make affected fixture evidence unavailable, requiring a separately identified and authorized later run rather than silently improving the first result. This is not a portable ban on database retries.

Numeric deadlines remain to be bound against the accepted connection envelope and actual capacity. PG-finality's generation/fence/permit state machine and reconciliation identity addition remain proposed; transaction-boundary placement is not their acceptance. PG-export's final seal and snapshot/restore protocol remain proposed. Exact executable statements, DDL/constraints, grants, wire bytes, enrollment and broader campaign bindings remain open.

The reviewed PostgreSQL persistence-contract draft byte identity is SHA-256 `f1597d62f5ef99ff1c3b24b684932962ca2436de68533f4c5f06d9b1084998ec`. This ratification authorizes no provisioning, database/grant/configuration changes, network attachment, credential issuance, live-provider spend, implementation, execution, export/restore, freeze or adoption. No PostgreSQL concurrency/finality behavior, cold skill construction or resulting-agent accuracy has been proved.

The next recommendation is PG-finality, followed by PG-export, each for individual disposition. The [PG-transaction authoring report](scenarios/proposed/pg-transaction-ratification-authoring-checks.json) retains the current document checks and unchanged public-pack/reference identities. Prior ratifications and reports remain in place; the retrospective remains deferred until the end.

## PG-finality — Generation-bound fencing and single-use replay — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "Ratified" to "Do you ratify PG-finality on these terms, including pre-admission fencing and the reconciliation identity additions, leaving exact wire bytes/DDL and PG-export open?"  
**Disposition:** PG-finality accepted as design, including pre-admission fencing and reconciliation identity additions; exact wire bytes/DDL and PG-export remain open

Accept a durable logical operation record with immutable attempt identities/history, numbered generations, permanent fences against closed attempts and single-use replay permits. Effect commitment and closure compete under the same operation lock. If commitment wins, retain and resolve to the original result under the declared exposure policy. If closure wins, the old attempt cannot later commit. A committed logical operation is not reopened for another effect.

Reconciliation may durably bind and fence a named request before its first admission. Record that pre-admission fence without inventing admission or execution. Ordinary not-found is not finality: it cannot prevent a delayed request from arriving later. Permanent retirement of the logical key is also rejected because the accepted cases require safe, bounded same-key replay.

A confirmed closure issues one permit bound to operation identity, semantic effect and closed generation. Its single atomic consumption admits a fresh physical attempt for the same intended effect in the next generation. Exact redelivery creates no second executor; competing permit consumers cannot both proceed. Preserve every closed generation. Historical closure cannot establish current finality after newer admission, and identity conflict cannot close unrelated newer work.

Keep semantic effect identity distinct from original request-byte digest and physical attempt ID. Accept operation kind and semantic-effect digest as additional reconciliation inputs so a never-admitted request has a bound intended-effect identity. Changed bytes or a different intended effect cannot overwrite the original identity. The parent service-interface inventory incorporates these logical inputs; exact field encoding, canonical bytes, closed schemas and DDL/constraints/grants remain pending.

Unconfirmed closure yields no finality proof or usable permit. Lost closure replies recover the stored closure/permit, not newly minted authority. Approval, read authority, current business preconditions and case budgets still apply; a permit replaces none of them. Preserve scheduled unresolved observations and unsupported cancellation without exposing private commitment or adding a disallowed reconciliation call. No uncertainty is repaired through evaluator knowledge.

The reviewed PostgreSQL persistence-contract draft byte identity is SHA-256 `23aedffe611a7fb6b14f33b2e437bfb4e13f2d7bb27d79dcc746c602a9f0ae92`. This acceptance is not concurrency/finality proof, executable schema freeze, enrollment or permission to provision, change the shared database/configuration, attach networks, issue credentials, implement, execute, spend on providers, export/restore or adopt the skill. Actual admission/commit/closure and permit-consumption races remain required proof.

The next recommendation is PG-export. Exact wire bytes, DDL/grants, numeric limits, content policy, enrollment and broader campaign bindings remain open. The [PG-finality authoring report](scenarios/proposed/pg-finality-ratification-authoring-checks.json) retains current document checks and unchanged public-pack/reference identities. Prior ratifications and reports remain preserved; the retrospective remains deferred until the end.

## PG-export — Sealed correlated export and isolated restore — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to "Do you ratify PG-export on these terms, leaving those exact bindings and execution separately gated?"  
**Disposition:** PG-export accepted as design; exact tool versions/commands, deadlines, row encoding, restore-instance configuration, content/retention permissions and execution remain open

Accept a private final service seal only after the declared terminal boundary or recorded harness abort/deadline, never at an application-restart checkpoint. Bound the wait for active short transactions and stop further fixture mutations. Preserve still-pending attempts and event states without manufacturing finality, consuming permits or releasing stock. If a trustworthy seal is unavailable, preserve partial/unavailable evidence rather than stop or restart the shared server to force success.

Accept inspection and scoped database dump from the same exported snapshot, within the already-accepted two custodian connections. Initial capture precedes admission; final capture follows the final seal. Inventory every fixture relation, including empty ones, with complete schema descriptions, exact counts and deterministic full-row digests. Preserve original dump identity, exit status and failure evidence; exclude live-volume copying and unrelated databases.

Restore into a fresh isolated PostgreSQL verification instance, not the shared workbench server and without its network or shared PKI/data mounts. Independently compare complete restored schema/data inventories, counts and row digests against source inspection. A matching archive checksum alone is insufficient. This additional work checks recoverability and evidence completeness; JSON-only state export would not exercise restoration of the actual relational fixture. Source ownership/grants remain a separate manifest, not an access-policy claim inferred from the data restore.

Keep service truth, actual delivered observations, application knowledge/checkpoints and evaluator judgments separate. Retain external producer-completion evidence and explicit gaps; a database record cannot establish what the agents received or knew. Preserve unavailable seals, incomplete exports, restore mismatches and original failures. No silent substitute, automatic unseal, evidence cleanup or repaired first result follows.

The reviewed PostgreSQL persistence-contract draft byte identity is SHA-256 `2083a820bbaf6496b48302af76c023fdc5ec591b16509b10ab456b7c9c999dff`. Exact tool versions and command lines, all deadlines, lossless row encoding, restore-instance launch/credential/resource configuration and content/retention permissions remain unresolved. This acceptance authorizes no provisioning, database/configuration/grant changes, network attachment, credential issuance, implementation, live-provider spend, execution, export/restore, cleanup, freeze or adoption. No export/restore or runtime verification has been performed.

All four PG design choices are now individually accepted within their recorded scopes; the persistence companion remains a draft with proposed or pending exact physical bindings. The next recommendation, not yet ratified, is fixture-facing wire schemas and canonical identities in the existing contract set, followed by corresponding DDL/grants and export encodings. Enrollment, operator/hook/evidence policies, operational limits, content/retention and broader campaign/test-strategy gates remain open. The [PG-export authoring report](scenarios/proposed/pg-export-ratification-authoring-checks.json) retains current document checks and unchanged public-pack/reference identities. Prior ratifications and reports remain preserved; the retrospective remains deferred until the end.

## WIRE-DRAFTING — Fixture wire and identity drafting — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratify" to "Do you ratify fixture wire schemas and canonical identities as the next drafting step, without authorizing provisioning or implementation?"  
**Disposition:** drafting step accepted; new wire/identity choices require individual review and ratification

Develop the fixture-facing request/result/error schemas, canonical plan/grant/effect and physical request identities, version/size/numeric rules and byte examples. Use these to constrain the later DDL/grants and export-encoding work. Keep prompts, agent generation schemas, controller logic and application checkpoints with the cold builder. The [review companion](wire-and-identity-contract.md) presents WIRE-envelope, WIRE-identity, WIRE-sources and WIRE-outcomes as proposals, not accepted consequences of this instruction.

The reviewed persistence companion's pre-edit SHA-256 is `ccc4719a052d13124f7ffb8f97ad658460843d42109ef1b26ea230aa39fa7b22`. The preceding PG-export authoring report retains SHA-256 `22dd88b0e54d0bcc3a2edf239197bef3a6eecc69a466d192a014e6b96e8714da`. No historical ratification is rewritten. The [current authoring report](scenarios/proposed/wire-drafting-authoring-checks.json) records scoped document/example checks, not runtime proof.

This authorizes no provisioning, implementation, shared-server/configuration/grant changes, network attachment, credential issuance, provider spend, execution, export/restore, cleanup, physical freeze or adoption. Operator-policy, hooks, evidence completion, enrollment/launch, operational limits, content/retention and campaign/test-strategy gates remain open. The retrospective remains deferred until the end.

## WIRE-envelope — Strict public envelope and safety ceilings — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to "Do you ratify WIRE-envelope on these terms, leaving the other three decisions, machine-schema completion and execution separately gated?"  
**Disposition:** WIRE-envelope strictness and safety ceilings accepted as design; not empirical calibration, machine-schema completion or runtime verification

Accept one versioned, closed public HTTP/JSON action boundary at `POST /frd/v1/actions`, retaining local plain HTTP and separate private administration. Require a single UTF-8 JSON object, no BOM/compression, duplicate decoded keys, unknown fields, trailing payloads or malformed Unicode. Do not repair, salvage, coerce or silently default fixture messages. Preserve the separate Agent Code policy for LLM outputs, authenticated run/order scope and the existing prohibition on automatic transport replay.

Accept whole nonnegative wire integers in `0..9007199254740991`, with positive quantities/revisions and strict decimal integer tokens; reject fractional/exponent forms, negative zero, numeric strings and booleans in numeric fields before lossy conversion. Accept the proposed ceilings: 1,048,576 UTF-8 octets per request/response, 262,144 per source, 256 entries per list, container depth 32 with root depth 1, identifiers of 1–128 ASCII characters and 4,096 UTF-8 octets for question/reason text. Over-limit content is unavailable, not truncated. These are accepted design ceilings, not measured runtime or provider-context limits. Full frozen-population fit checks remain required; any change to the accepted ceilings returns for explicit disposition.

Canonical digest/source definitions and action-specific result/error variants remain with WIRE-identity, WIRE-sources and WIRE-outcomes. Cross-reference in envelope notation does not ratify them. Exact machine schemas, validation/error precedence, authorization policy, deployment framing/header bindings and actual enforcement remain open. Neither an HTTP status nor an error receipt proves no effect.

The reviewed wire companion's pre-edit SHA-256 is `04501d2ad4778ad71483cd6423720bc123524374349556381a1041cba9f38d47`. The preceding wire-drafting authoring report retains SHA-256 `71515c90af4d9f43c36a265bae10efdbf6915891ec864098c28f1b04446e3fc1`. The [current authoring report](scenarios/proposed/wire-envelope-ratification-authoring-checks.json) names the document/example checks and unchanged public/reference/example identities; prior ratifications and reports remain preserved.

WIRE-identity is the next recommendation for review, not accepted by this response. No implementation, provisioning, SQL/configuration/grant changes, network attachment, credential issuance, provider spend, execution, export/restore, cleanup, freeze or adoption is authorized. The retrospective remains deferred until the end.

## WIRE-identity — Physical and semantic identity with grant-content binding — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to "Do you ratify WIRE-identity, including grant-content binding and this separation of physical and semantic identity?"  
**Disposition:** WIRE-identity accepted as design; machine-schema completion, source/outcome decisions, implementation and runtime proof remain separately gated

Accept SHA-256 over exact physical entity-body bytes independently from semantic plan/grant/effect hashes. Semantic preimages use the owning domain (`frd/plan/v1`, `frd/grant/v1` or `frd/effect/v1`), one NUL byte, then RFC 8785 JCS UTF-8 bytes of the explicit value in the wire companion. Do not add implicit newlines/wrappers or repurpose the public pack's existing digest convention. Raw source/result identities retain the separate byte inputs described there; accepting hashing does not accept the still-proposed source materialization/publication or result-union designs.

Accept immutable grant-content binding alongside approval ID in effect identity, including `grant_digest` on the mutation wire. The ID locates the grant; the digest independently binds its exact contents. Recompute identities and perform independent authority/scope checks; a matching digest cannot grant authority. Plan identity includes plan ID/revision and requirement-source identities. Effect identity includes run/order, operation kind, plan/grant identity, expected order revision, exact effect terms and the reservation identity for arrangement; request/attempt IDs, logical operation key, generation and replay permit are excluded from the semantic preimage but remain bound by the journal.

Accept deterministic sorting only for explicitly declared sets, including the wire companion's SourceRef tuple order; reject duplicates and conflicting identities rather than silently deduplicating. Preserve source bytes, response list order, approved-operation order, Unicode contents and ordered provider-context evidence. Formatting changes the physical request digest, not its business semantics. It nevertheless conflicts with an existing attempt's original bytes. An authorized replay uses fresh physical attempt/request identity and the existing service permit while preserving the approved effect identity; it still requires current authority, business predicates, case allowance and budget. Changing approved terms or grant content changes effect identity and cannot masquerade as the old logical operation.

The reviewed wire companion's pre-edit SHA-256 is `b87611935b66a68b3db17e6db2cf144b82ed64131810c8151232c6d1ff76bb87`. The preceding WIRE-envelope authoring report retains SHA-256 `8c490d1ad434c07aae1b97198f7b933e729f02c545d3540599e8660cd2e9866b`. The [current authoring report](scenarios/proposed/wire-identity-ratification-authoring-checks.json) retains scoped checks and unchanged public/reference/example identities. Selected vectors support their named comparisons only, not complete JCS interoperability, source completeness or replay safety. Prior ratifications and reports remain unchanged.

WIRE-sources is the next recommendation for review; WIRE-sources and WIRE-outcomes are not accepted by this response. Full machine schemas, source materialization, policy and operational bindings, DDL/grants and live boundary proof remain open. This acceptance authorizes no provisioning, implementation, SQL/configuration/grant changes, network attachment, credential issuance, provider spend, execution, export/restore, cleanup, freeze or adoption. The retrospective remains deferred until the end.

## WIRE-sources — Immutable source bytes and independently checked completeness — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to "Do you ratify WIRE-sources on these terms, including one-time derived source bytes and independently checked completeness?"  
**Disposition:** WIRE-sources accepted as design; exact schemas, full source materialization, implementation and runtime proof remain separately gated

Accept exact immutable source retrieval by complete source reference, with byte length and digest agreement. Return the referenced body, not a summary or the latest replacement; retain authorized access to superseded immutable revisions. Preserve Unicode contents, response order and original fields/messages. The declared context-compaction case must recover the complete original brief, including the omitted substitution restriction. Source provenance supplies trust classification; message instructions and content hashes do not create authority.

Accept explicit complete observation scope and publication/supersession information. Return all current accepted customer briefs, including equally current conflicting briefs, and the applicable published source population. Revision maximum across different record IDs cannot select a winner. Availability includes every published option matching the requested SKU/site scope, including zero-stock, expired, late and forbidden-substitution candidates; do not add feasibility, ranking or evaluator labels. Preserve the agents' suitability judgments.

Accept one-time derivation of source bytes from the pack's structured actor-visible records when fixture initialization is later authorized. Bind the actual pack identity, world, exact source location, kind/record/revision, derived JCS UTF-8 bytes, byte length and digest. Label these as derived fixture bytes, not original pack substrings. Later published revisions retain explicit provenance. This ratification does not perform full materialization, supply the exact manifest/body schemas or authorize initialization/content capture.

Accept independent completeness verification against the applicable snapshot and publication history. Valid hashes and an internally consistent response membership list are not enough. The required known-dirty case omits an equally current conflicting brief while leaving every remaining hash valid, including a correspondingly shortened membership list; the independent comparison must detect it. No actual source-service or omission-detection result is established by this acceptance. Existing byte ceilings and unavailable-rather-than-truncated behavior remain in force.

The reviewed wire companion's pre-edit SHA-256 is `6d6a33a9d020e7aa00fb9a1de429415e8618cc580732ccaf7afac59fde007436`. The preceding WIRE-identity authoring report retains SHA-256 `aa412cc966d51b95878ad0744786851101467f6b6700feba90941203852ba9ba`. The [current authoring report](scenarios/proposed/wire-sources-ratification-authoring-checks.json) retains scoped document/example checks and unchanged public/reference/example identities. Prior ratifications and reports remain unchanged.

WIRE-outcomes is the next recommendation for review and is not accepted by this response. Full machine schemas, materialization, policy and operational bindings, DDL/grants and live boundary proof remain open. This acceptance authorizes no provisioning, implementation, SQL/configuration/grant changes, network attachment, credential issuance, provider spend, execution, export/restore, cleanup, freeze or adoption. The retrospective remains deferred until the end.

## WIRE-outcomes — Typed results and durable finality — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratified" to "Do you ratify WIRE-outcomes on these terms, including pending-mutation `unresolved` and preservation of original committed-result bytes?"  
**Disposition:** WIRE-outcomes accepted as design; exact policy/error precedence, machine-schema completion and runtime proof remain separately gated

Accept the closed, action-specific payload/result/error structures in the reviewed wire companion. `committed` requires the matching durable effect. Mutation `rejected` requires a typed reason and durable no-effect closure; it is not a generic failure label. Reconciliation `closed_not_applied` requires the identified attempt and prior execution opportunities to be durably fenced, with the generation/request/effect-bound permit under accepted PG-finality. The permit does not replace current authority, case allowance or budget. `unresolved` establishes neither commitment nor no effect and supplies no retry permission.

Accept pending-mutation `unresolved` for admitted pending and exact-redelivery states. Accept reconciliation returning the original committed-result UTF-8 bytes and their raw digest, preserving original effect/attempt/commit identity while the outer observation is new. Verify that those bytes describe the matching committed operation; do not disclose a private commitment during a case's scheduled unresolved exposure. Preserve PG-finality's action-specific unresolved identity-conflict result; a generic error alternative does not override it.

Accept the companion's typed business-result/error vocabulary and HTTP mapping. Approval/source denial and unavailability remain their own business results. HTTP 200 identifies a valid business response, not business success. Transport errors, ordinary not-found, cancellation accepted/unsupported and error receipts never establish no-effect finality. Cancellation creates no new reconciliation allowance. Exact validation/error precedence, authorization-policy predicates and deployment bindings remain open, not implicitly settled by the vocabulary.

Accept the distinction between the fixture's `arrangement_recorded` service fact and the desk's `recovery_arranged` outcome. Actual commitment, accurate communication and the application's supported knowledge remain independently necessary; a valid schema or matching digest does not prove an accurate agent. Reservation and arrangement retain their separate atomic effects, revision changes and matching-allocation requirements.

The reviewed wire companion's pre-edit SHA-256 is `766dfe795a0e28bf56c3a8b93123c2c4ada8c40dcebed825e924d39bfbc106df`. The preceding WIRE-sources authoring report retains SHA-256 `ed74abddd783ec61481432235ca46e4ff3c13c3c145fb8fa1eb0698f1b93023f`. The [current authoring report](scenarios/proposed/wire-outcomes-ratification-authoring-checks.json) records scoped document/example checks and unchanged public/reference/example identities. Prior ratifications and reports remain preserved. These checks are not machine-schema validation or runtime outcome proof.

All four WIRE designs are now accepted within scope. Exact machine-schema expansion follows within the already-ratified WIRE-DRAFTING step; substantive gaps return for individual ratification. This acceptance authorizes no provisioning, implementation, SQL/configuration/grant changes, network attachment, credential issuance, provider spend, execution, export/restore, cleanup, freeze or adoption. The retrospective remains deferred until the end.

## WIRE-SCHEMA-DRAFTING — Proceed with the machine-schema candidate — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratify proceeding as you recommend" to the recommendation to produce exact request/result/error schemas, source-body/derivation schemas, positive/invalid examples and explicit non-schema checks before deriving DDL/export encodings.  
**Disposition:** authoring step accepted; substantive new bindings require individual ratification

Proceed with the machine-schema translation within the existing WIRE-DRAFTING authority. Preserve accepted business behavior, strict local-HTTP boundary, identity/finality distinctions, public/reference/previous-evidence bytes and cold-builder ownership. Test actual schemas with positive and deliberately invalid specimens. Identify byte, lexical, correlation, provenance, authority and durable-state obligations that structural validation cannot discharge.

The [candidate review](schemas/proposed/README.md) presents SOURCE-order and SOURCE-events as proposed exact source-body/provenance bindings, not accepted consequences of this instruction. Their schema examples remain proposed even when structurally valid. Local schema testing is advisory authoring evidence, not runtime fixture implementation, machine-schema closure, full source materialization, cold-build use or agent accuracy.

The pre-authoring wire companion SHA-256 is `a59791d69bf9ef03ec6bac540b5f46c4f51a8da854ec23fd2e85e66ff840e284`. The preceding WIRE-outcomes report retains SHA-256 `56789eff7c66f758a788148d4dc47135d884a8edfeac597305fdecdab757a756`. The [current report](schemas/proposed/wire-schema-authoring-checks.json) records exact artifacts, checks, scoped read depth and preserved first failures.

No provisioning, fixture implementation, SQL/configuration/grant changes, service-network attachment, credential issuance, provider spend, runtime execution, export/restore, cleanup, freeze or adoption is authorized. An isolated temporary schema-test environment is authoring support, not an enrolled fixture. Policy/error precedence and all remaining physical/campaign gates remain open. The retrospective remains deferred until the end.

## SOURCE-order — Exact post-arrangement order body — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratify SOURCE-order and SOURCE-events as each is presented", applied individually to the SOURCE-order recommendation.  
**Disposition:** SOURCE-order accepted as presented; design only, not runtime proof or physical freeze

Accept the existing order fields with service status `arrangement_recorded`, the matching `reservation_id`, one revision increment and `recovery_plan = {arrangement_id, plan_digest, approval_id, grant_digest, terms}`. Retain customer, requested SKU, quantity, destination, original source and physical shipment/delivery facts. Reservation alone leaves the order unchanged. The immutable arrangement/plan/approval references support independent joins without copying the whole grant or equating a service fact with the desk's accurate recovery outcome.

The reviewed [schema companion](schemas/proposed/README.md) had pre-edit SHA-256 `8035211c039d9d1241e44188399284c7e06662482577387f771389aeb7f2a10a`; its source-body schema had SHA-256 `405bfe834949feae843fbfb6646fedcf39899baff2ad09ffb443ce04cc4769cd`. Keep `RecoveryPlanProposed` and `OrderArrangedProposed` as stable draft-era identifiers; their historical suffix is not a pending disposition. This pass changes annotations and specimen status, not schema assertions or specimen values. Cross-field equality, exact revision transitions, state joins and actual boundary enforcement remain separate proof.

## SOURCE-events — Typed event-source catalog and provenance — ratified 2026-09-12 America/New_York

**Decision owner:** Tad Haffey  
**Source:** explicit operator response "ratify SOURCE-order and SOURCE-events as each is presented", applied individually to the SOURCE-events recommendation.  
**Disposition:** SOURCE-events accepted as presented; catalog authoring, full materialization and runtime proof remain pending

Accept a separate immutable structured catalog for event-created notices, revised/conflicting briefs and new quotes, preserving the original public-pack bytes. Bind entries to the governing specification-artifact digest and original case/event pointer; derive JCS source bytes from the actual structured record, not event prose. Use supplier-notice bodies `{record_id, revision, source_class: "supplier_data", message}` with the exact intended message. Keep visibility and trust in authenticated catalog/provenance relations, not fabricated order fields or authoritative body labels. Revised briefs and quotes retain their existing shapes and fields.

Accept `event_origin` as semantically required for event-derived entries; ordinary-original entries may omit it. Its optional schema shape does not remove the independent applicability/provenance check. Verify both the actual structured input and governing event. Event provenance remains private fixture/evaluator metadata, not actor-visible body content or an answer channel. Keep `SupplierNoticeProposed` as a stable draft-era identifier with accepted disposition.

The reviewed derivation schema had pre-edit SHA-256 `724b94b95ec8f6578e8ee8529abc3d679f42a5e2197bfb7bd0352bc037349df3`. The prior machine-schema authoring report retains SHA-256 `a393bd1c669222f040c4814913886f8e8ab5748ef2fbe3bec86381833a63cc17`. The [current source-ratification report](schemas/proposed/source-bindings-ratification-authoring-checks.json) records scoped authoring checks, stable schema assertions/specimen values and preservation of earlier evidence and the prior ratification prefix.

Neither acceptance authorizes fixture initialization, provisioning, SQL/configuration/grant changes, service-network attachment, credentials, provider spend, runtime execution, export/restore, cleanup, freeze or adoption. No complete event-source catalog was created by this acceptance. Exact policy/error precedence and remaining physical/campaign gates stay open; full skill build-use and resulting-agent accuracy remain independently required. The retrospective remains deferred until the end.
