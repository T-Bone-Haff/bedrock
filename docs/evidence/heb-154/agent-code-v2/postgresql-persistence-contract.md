# Fulfillment-recovery PostgreSQL persistence contract

| Field | Value |
|---|---|
| Document ID | FRD-POSTGRESQL-PERSISTENCE |
| Parent construct | [Execution contract](execution-contract.md), refined by [physical runtime binding §5](physical-runtime-binding.md) |
| Revision | draft-1 |
| Status | PROPOSED; all four PG design choices accepted within their recorded scopes, but exact physical bindings remain proposed or pending; not an implementation-complete handoff, enrollment or execution authorization |
| Owner | Tad Haffey |
| Recorded | 2026-09-12 (America/New_York) |
| Review trigger | Ratification of a PG decision; completion of wire/DDL bindings; before physical freeze or implementation |
| Doctype ruling | Companion specification for the existing internal proving fixture, not a new standing standard or agent architecture |
| Deliberation substrate | Accepted EC-operation-journal, EC-state-commit, EC-event-evidence and PB/EN decisions; operator instruction to proceed with the PostgreSQL persistence contract |
| Supersedes | None; preserves accepted behavior and public scenario bytes |

## 1. Purpose, authority and limits

Make the fixture's state changes, uncertainty and independent evidence implementable without solving the agents' work. This proposal describes relations, constraints, transaction boundaries, lock ordering, durable fences and an export protocol. Exact executable DDL, request/result schemas and numeric operational limits remain explicit freeze work, after substantive choices are settled.

Authorities are the [ratification record](agent-code-v2-ratification-record.md), [business world](business-world-and-reference-case.md), [public pack](scenarios/proposed/scenario-pack.json), parent execution contract and physical binding. The public pack retains SHA-256 `46cd351ab957e974829695c0562093ab664e1fb81249b9124a3a58a144fdf0b0`. Its case values, recovery allowances and acceptance predicates are unchanged. All five EN design directions are accepted, but exact enrollment, actual window/capacity checks and provisioning remain separately gated.

Preserve separately atomic reservation and arrangement, the cross-key allocation guard, no implicit release, and the distinction between actual effect, delivered observation and application knowledge. The cold builder still owns agents, controller, provider adapters and application checkpoint technology. Neither fixture SQL nor an evaluator repairs their decisions. No provider/model, framework, live spend, content-capture permission, hidden instance or adoption is selected here.

Read depth: parent execution contract, business-world document, reference JSON, scenario guide, README, authoring checker and selected Bedrock construct-spec/testing instructions and references whole. Public-pack common contract, every world's complete initial state and every case's complete event schedule/state predicates were read as scoped projections; remaining JSON fields were not all reread. Physical persistence/enrollment/lifecycle passages and relevant sequence/EC ratifications were scoped reads. PostgreSQL documentation below was read in relevant passages, not as a whole documentation corpus. A truncated combined vendor-document response was disclosed and the governing passages reread separately. No new Docker, SQL, credential or capacity inspection occurred. The [authoring report](scenarios/proposed/postgresql-persistence-authoring-checks.json) retains input identities and actual checks; no database behavior has been tested by this draft.

## 2. Decisions for review

These are four coupled design choices, not four new acceptance verdicts. PG-state's storage approach, PG-transaction's transaction/failure policy, PG-finality's fencing/replay design and PG-export's sealed snapshot/restore design are individually accepted within their recorded scopes. The overall draft remains PROPOSED because its exact physical bindings are not complete or accepted wholesale. Design acceptance does not freeze executable bindings or prove behavior.

| Decision | Recommendation | Alternative and trade-off |
|---|---|---|
| PG-state | Accepted design direction: typed relational current state plus append-only source/effect/attempt/event history; preserve original evidence bytes separately from parsed projections. Exact relation/column/type/constraint and grant bindings remain open | One mutable JSON document is initially smaller but obscures constraints and before/after evidence. Full event-sourcing machinery would add reconstruction infrastructure the fixture does not need. |
| PG-transaction | Accepted design: explicit Read Committed writes with a fixed row-lock order, short shared catalog/clock guard, database constraints, coherent read-only snapshots and no automatic effect-transaction retry; numeric limits remain open | Serializable transactions can protect broader predicates, but need an explicit serialization-retry policy and still do not resolve unknown commit or wire replay. A run-wide exclusive mutation lock would unnecessarily serialize unrelated work. |
| PG-finality | Accepted design: one durable operation row, immutable attempt identities/history, generation-bound fences and single-use replay permits, including pre-admission fencing and reconciliation operation-kind/semantic-digest fields; exact wire bytes/DDL remain open | Lookup-only absence cannot stop a delayed request; permanently retiring the logical key prevents the already-required same-key replay. This design adds explicit state transitions and identity fields to the unfinished reconciliation wire schema. |
| PG-export | Accepted design: a declared final service seal, shared MVCC snapshot for inspection/dump, and isolated restore with full relation comparison; retain application knowledge and failures separately. Exact versions, commands, deadlines, row encoding, restore configuration and content/retention permissions remain open | Independent snapshots can disagree. Copying a live data volume is the wrong scope. A single JSON state export is simpler but does not exercise restoration of the actual relational fixture. |

Recommendation: expand the exact fixture-facing machine schemas against the accepted wire and identity designs, then derive the corresponding DDL/grants and export bindings. Request/result/error variants and identity encodings determine storage keys, replay comparisons and evidence encodings. This drafting step is ratified; the [wire/identity companion](wire-and-identity-contract.md) records all four WIRE designs accepted within scope, including pending-mutation unresolved and original committed-result bytes. A [machine-schema candidate](schemas/proposed/README.md) is authored and locally tested; SOURCE-order and SOURCE-events are separately accepted as presented; full source materialization and runtime proof remain pending. Policy/error precedence and the exact physical bindings remain open. Drafting does not authorize implementation or freeze; §8 retains the remaining gates.

## 3. PG-state — Current projections with durable history

**Accepted design direction:** typed relational current state plus append-only history and separately preserved original evidence bytes. Tad ratified this approach on 2026-09-12 (America/New_York); see [PG-state ratification](agent-code-v2-ratification-record.md#pg-state--relational-state-and-append-only-history--ratified-2026-09-12-americanew_york). Exact DDL and grants remain open. The relation inventory and storage types below remain proposed physical bindings; references to other PG mechanisms do not independently accept them. PG-transaction, PG-finality and PG-export have separate acceptances in §§4–6. Evidence-byte retention still requires the content policy.

### Representation and ownership

Use one run database with a fixture-owned schema. A singleton `run_control` row carries the immutable run/world/schema identities, controlled business minute, catalog epoch and admission/seal state. All run-scoped relations reference its unique run identity. Reject a database whose identity disagrees with the launch manifest. Do not infer ownership from its name.

Use typed columns for keys, revisions, quantities, monetary minor units, currencies, state tags and foreign-key joins. Proposed storage types are opaque `text` identifiers with exact, case-sensitive comparison; `bigint` counters/amounts/minutes; 32-byte SHA-256 digests; and `bytea` for byte-sensitive payloads. Positive/nonnegative checks follow the owning field. Signed environmental deltas are the explicit exception. Checked arithmetic and wire bounds must agree before DDL freeze; no float conversion, truncation or overflow recovery. Generated internal UUIDs are opaque identities, never commit-order evidence.

Preserve exact source/request/result bytes where the content policy permits them, alongside their digests and parser/schema identity. `jsonb` may serve as a validated searchable projection, not the authoritative original: it discards whitespace, object-key ordering and duplicate keys. Duplicate-key rejection occurs before ordinary JSON conversion. Do not use a database rendering to reconstruct a supposedly original payload. [PostgreSQL JSON representation](https://www.postgresql.org/docs/17/datatype-json.html)

Source revisions and effect results remain immutable. Current-state projections may change only in the transactions below, with corresponding append-only history. The fixture is trusted machinery; grants and constraints limit its authority but do not make a compromised fixture an independent judge. The evaluator independently reconstructs and compares state.

### Proposed relation and constraint inventory

Names below are proposed schema names. Rows group closely related relations; this is not a claim that executable DDL already exists. Every foreign key includes run identity and, where needed, order/operation identity to prevent a valid ID from another scope satisfying a join. No cascading history deletion.

| Relation(s) | Required information and relational constraints | Runtime mutation class |
|---|---|---|
| `run_control` | Exactly one run identity; immutable world/input/schema digests; nonnegative business minute/catalog epoch; admission state and optional seal identity | Update only declared clock/catalog/admission columns under the guard protocol |
| `order_state` | Unique run/order; original customer/requested SKU/quantity/destination/disruption and physical-fulfillment facts; positive revision; nullable reservation/arrangement references and recovery terms; initial source identity | Only arrangement linkage, recovery terms, service status and revision may update; original request and shipping/delivery facts unchanged |
| `stock_state` | Unique run/stock ID and run/site/SKU; nonnegative available quantity; positive revision | Update available/revision only with a corresponding movement |
| `source_revision`, `source_publication` | Unique source-kind/record/revision plus original bytes/digest; order scope and provenance; publication/supersession events identify exactly which revisions become visible/current | Insert only; the accepted set is derived from explicit publication/supersession, not maximum revision across records |
| `quote_revision` | Unique quote/revision; source identity; site/SKU/whole quantity/destination/arrival/cost/currency/expiry; typed values agree with preserved body; publication via source history | Insert only; unpublished quotes cannot appear early |
| `plan_record`, `approval_grant` | Immutable submitted plan bytes/digest and terms; grant ID, policy/issuer identity, plan/order/quote/requirement references, issue/expiry and allowed operation sequence | Insert only through authenticated fixture actions; no replacement plan, oracle-derived permission or stock hold |
| `operation_state` | Unique operation key in run; fixed order/kind/semantic digest; current generation/phase; initial attempt identity and optional committed effect/result reference | Identity immutable; phase/generation/result pointer updated under the operation lock |
| `attempt_state` | Unique attempt ID in run; fixed operation/generation/request digest; admission or pre-admission-tombstone origin; current phase and terminal reference | Identity immutable; current phase only changes with append-only events; at most one newly admitted executor per generation |
| `replay_permit` | Unique permit ID and operation/closed-generation pair; semantic digest; fence event; optional consuming attempt; consumption cannot be reassigned | Insert at closure; single conditional consumption update in replay admission |
| `reservation` | Immutable effect/operation/committed-attempt IDs; order/plan/grant/quote; stock/site/SKU/quantity/destination; business minute and before/after stock revisions | Insert only; unique operation and unique run/order allocation in this no-release world |
| `arrangement` | Immutable effect/operation/committed-attempt IDs; matching reservation and approved terms; order before/after revision with after = before + 1 | Insert only; unique operation, reservation and run/order; no second decrement |
| `stock_movement` | Unique movement ID; exact stock identity, signed delta, before/after quantities/revisions and originating reservation or environmental event, exactly one origin | Insert only; one movement per reservation; unique stock/resulting-revision; whole environmental event shares one transaction identity |
| `operation_result` | Immutable original typed terminal body/digest, operation/generation/attempt, committed effect or fenced rejection, and service transaction/event identity | Insert only; unique terminal result per attempt and at most one committed result per logical operation |
| `service_event` | Immutable event ID, kind/origin, operation/attempt or environmental identity, business minute, explicit predecessors and original payload/digest | Insert only; local state transitions and their event/outbox record commit together |
| `event_delivery`, `schedule_state` | Event publication/ack state separate from payload; one-shot schedule identity, prerequisites, reached/claimed/applied/unavailable state and associated event IDs | Narrow projection updates; no event deletion or automatic refiring of an uncertain external hook |

The unconditional unique reservation per run/order implements the accepted active-allocation guard because release is not a permitted operation in this world. Adding release would require a deliberate replacement constraint and history contract; do not prebuild that machinery. Arrangement reuses the reservation's allocation, not the now-reduced free stock.

The stored initial-world bytes retain the complete supplied baseline, including its empty output/forbidden-effect stores. Customer drafts, operator summaries, agent attempts and budget checkpoints remain application-owned artifacts, not writable fixture business tables. Their final evidence joins by run/order/artifact identity. No shipping, sending, payment or reversal action exists; empty fixture stores alone cannot prove that the application avoided an external effect, so network/access and dispatch evidence remain independently required.

### Grant map and reconstruction

Custodian-owned initialization creates schema, constraints and precise grants; runtime performs no DDL and owns no object. Proposed runtime grants are schema usage, required reads, inserts to named history relations, and column-specific updates to named projections. No delete/truncate, grant option, blanket future-object grants, new extension, privileged function or workbench-role reuse. History must not gain update permission merely to acquire a row lock: lock its mutable parent instead. Final grants must include the actual lock statements' privilege requirements and be tested using the real restricted identity.

Initial load and each source publication preserve all records, including equally current conflicting briefs, expired/infeasible quotes and untrusted notices. Store no evaluator requirements, feasible-set labels or expected outcomes in product-facing relations. Any typed authorization-policy interpretation comes from the separately bound visible-fact policy, not copied oracle answers.

Reconstruction checks compare initial stock + all environmental deltas − reservations with current stock, and verify each stock revision's before/after chain. Order revision advances only with a matching arrangement; immutable request/physical-fulfillment fields remain unchanged. Attempt history must reproduce its current projection; committed results must resolve to matching real effects. Primary/foreign keys and checks enforce local structure; cross-relation arithmetic and protocol correctness also require transaction logic and independent tests, not a fictitious cross-table `CHECK` guarantee.

## 4. PG-transaction — Explicit locks and separate commits

**Accepted design:** Tad ratified the transaction/locking and failure policy on 2026-09-12 (America/New_York), explicitly including no automatic effect-transaction retries. Numeric limits remain open; see the [ratification record](agent-code-v2-ratification-record.md). References below to generations, permit consumption, closure transitions and final sealing locate their transaction boundaries. PG-finality and PG-export have separate acceptances in §§5–6. Exact DDL/grants, implementation and runtime proof remain pending.

### Locking protocol

Use explicit Read Committed write transactions for this finite fixture. Do not rely on unlocked read/check/write sequences: successive statements can observe different committed states. PostgreSQL row locks and a consistent acquisition order supply the mechanism below; design acceptance is not proof that every writer follows it. [Read Committed](https://www.postgresql.org/docs/17/transaction-iso.html) [Row locks and deadlocks](https://www.postgresql.org/docs/17/explicit-locking.html)

Acquire only needed locks, always in this order:

1. `run_control` row: `FOR SHARE` for ordinary admission/effect/finality and environmental-stock transactions; `FOR UPDATE` for clock/catalog/grant publication and final sealing. An exclusive operation takes that mode at the outset, never upgrades after taking subordinate locks.
2. Logical operation rows, ordered by exact operation key; normally one.
3. Order rows, ordered by exact order ID; normally one.
4. Stock rows, ordered by exact stock ID; a multi-stock environmental event takes all affected rows in that order.
5. The operation's attempt/permit projections and the local schedule-state row, if changed. No path holding these subordinate locks may then acquire an earlier lock.

The shared run guard does not serialize ordinary mutations with one another. It prevents authority, quote publication and business time from changing during their short checks/commits. Different operations still compete on stock; same-order operations serialize on that order. Historical immutable grants/sources/effects need no extra lock. Every writer, including private scheduler and approval channel, follows this protocol. New write paths require reconciliation with this list.

For an absent operation, use a unique-key insert-if-absent then a separate locked read in the same transaction; compare the existing immutable identity rather than overwriting it on conflict. In Read Committed, an insert conflict need not be visible to that statement's initial snapshot. A subsequent statement supplies the needed view. No generic upsert rewrites effect identity. [Concurrent insert behavior](https://www.postgresql.org/docs/17/transaction-iso.html)

Hooks/barriers, provider calls, HTTP response delivery and collector waits occur outside transactions and without checked-out pool connections. A short atomic admission commits and releases its connection before the hook. The effect transaction reacquires locks and rechecks all predicates after the hook. At most four fixture connections and no overflow remain the accepted ceiling; parked requests cannot consume the pool and starve the counterpart needed to release a barrier. Use no session advisory locks, global table mutation lock, prepared transaction or distributed transaction.

Read-only business actions that assemble multiple related records use a short Repeatable Read read-only transaction, producing one coherent declared-scope observation. That observation is not a future reservation promise. Publication visibility and source identities still govern the response.

### Transaction matrix

| Transaction | Atomic work | Outside it / failure behavior |
|---|---|---|
| Mutation admission | Validate transport/schema/scope; bind immutable operation/attempt identity; consume a replay permit if required; append admission/transmission evidence | No stock/order effect. Repeated delivery does not enqueue a second executor. Pre-commit hook follows after connection release. |
| Reservation effect | Recheck open run, current generation/attempt fence, grant and exact current references; lock order/stock; test allocation guard and available quantity; decrement stock and increment stock revision; insert reservation, movement, original result and service event; mark operation/attempt committed | Order remains unamended. Zero business changes on rejection. Response may be delivered or really dropped only after transaction resolution. |
| Arrangement effect | Recheck open run, fence, current grant/references and matching confirmed reservation; lock order; enforce expected revision; insert arrangement; attach approved recovery terms/reservation; advance order once; insert original result/event; mark committed | No stock update. Preserve original customer request and physical-fulfillment status. Failure leaves reservation held. |
| Declared business rejection / pre-commit fault | After checks and before business writes, close/fence the eligible attempt and append typed result/history, using the same operation lock as commitment | No speculative partial writes. FRD-09A's named order-write rejection is deliberate service behavior, not a swallowed SQL exception. |
| Environmental stock change | Lock all affected stock; apply every declared delta/revision change plus movements and one-shot event consumption together | Neither order is credited with the environmental effect; no partial West/East update. |
| Source/quote/clock/grant publication | Exclusive run guard; append authenticated publication/history and update minute/catalog epoch as applicable; record one-shot event consumption | No unsolicited proposal or hidden-answer lookup. This protocol does not define the pending approval-policy logic. |

Every current precondition is checked inside the effect transaction, not merely at admission. Reservation checks stock; arrangement checks its confirmed allocation. Expired authority blocks a new effect, but historical reconciliation still returns a matching original commitment. State mutation, original terminal result and local service-event/outbox insertion share one commit.

### SQL failure, uncertainty and limits

Accept **no automatic effect-transaction retry in this proving fixture**. Known rollback is different from unknown commit, but neither should introduce hidden attempts. The trade-off is that an unexpected deadlock/timeout may make fixture evidence unavailable and require a separately identified, authorized later run instead of improving availability silently. This is a fixture-specific accepted policy, not a portable prohibition on database retries.

| Observation | Required interpretation |
|---|---|
| Expected business predicate fails before writes | Commit the named no-effect rejection/fence, then return its typed result. |
| SQL error with confirmed transaction abort/rollback | No writes from that transaction survive; retain infrastructure-failure evidence. Earlier admission or an earlier business operation may still exist. A separate finality transaction may fence the attempt; only its confirmed commit supports a no-effect closure. Do not re-execute the business effect. |
| Connection loss, timeout or cancellation around commit without authoritative outcome | Preserve unknown. Do not infer rollback from a disconnected client, reapply the mutation, or return success. Resolve the operation journal through the permitted path; if unavailable, remain unresolved. |
| Unexpected constraint violation | Retain the failure; do not map every constraint/SQL error to a convenient business rejection. Only explicitly specified, correctly identified constraint branches may receive a typed domain disposition. |
| Fixture cannot persist required admission/history | Withhold business execution. Preserve external collector failure evidence if available; no synthetic durable receipt. |

Configure finite pool-acquisition, connection, lock, statement, total-transaction, hook and export deadlines in the run manifest; their exact values require the pending capacity/campaign pass. Lock timeout must be shorter than the enclosing statement/transaction deadlines, and no hook extends a SQL transaction. Verify session-effective settings on checkout and prevent pool reuse from leaking per-operation settings. Keep shared server settings unchanged. PostgreSQL distinguishes statement/lock cancellation from transaction-timeout session termination; neither a client deadline nor its wording establishes finality. [PostgreSQL timeout settings](https://www.postgresql.org/docs/17/runtime-config-client.html)

Internal SQL/finality/collector work retains its own attempt identity, phase and cost; it is not a new product tool dispatch or fresh application budget. No HTTP/SDK/connection-layer replay is enabled. A replayed application effect still requires PG-finality, current business authority and the case's remaining allowance.

## 5. PG-finality — Fences before and after admission

**Accepted design:** Tad ratified the operation/generation/fence/single-use-permit design on 2026-09-12 (America/New_York), including pre-admission fencing and the reconciliation identity additions; see the [ratification record](agent-code-v2-ratification-record.md). Exact wire bytes and DDL remain open; PG-export has its separate acceptance in §6. Acceptance is not proof of race safety or permission to implement, provision or execute the fixture.

### Identity and the wire dependency

Keep three separate identities: canonical semantic effect digest, original physical request-byte digest, and attempt ID. Semantic identity includes operation kind, run/order, approved plan/authority and exact effect parameters, but excludes transport request/attempt IDs and replay permit. Canonical bytes and numeric/string bounds must be fixed jointly with the wire schema; the public world's existing digest encoding is not silently repurposed as a protocol standard.

The [wire companion's WIRE-identity](wire-and-identity-contract.md) now supplies the accepted encoding design: raw physical-body SHA-256, domain-separated JCS plan/grant/effect identities and an immutable `grant_digest` included in mutation/effect identity alongside approval ID. Same-attempt bytes must still match exactly; a permitted fresh attempt changes physical identity but not approved semantics. WIRE-envelope has separately accepted the numeric/byte safety ceilings. These refinements do not freeze the unfinished machine schemas, source materialization, DDL/grants or replay implementation, and do not create authority or budget.

**Accepted wire refinement, exact bytes pending:** reconciliation supplies the operation kind and semantic effect digest in addition to the parent's operation key, uncertain attempt ID and original request digest. Without this, a never-admitted operation has no stored semantic identity to bind its replay permit to. The authenticated run/order scope and identity checks still apply. The original request digest binds the named delayed attempt; the semantic digest binds the permitted later effect. A mismatch against an existing operation/attempt returns unresolved identity conflict and never overwrites it. No arbitrary caller data grants effect authority. Field presence and purpose are accepted; the closed physical schema, canonical encodings and exact wire bytes remain to be bound.

A permit is an opaque service-issued ID, scoped to the authenticated run/order/operation, semantic digest and closed generation. It is not a substitute transport credential, approval or budget. Its row and consumption history may appear in private evidence; database/provider credentials may not.

### Accepted state-machine design

`generation` starts at 0. Each generation has at most one newly admitted physical executor. The logical operation can be `open`, `closed` or `committed`. A newly created row is bound to its initial attempt in the same transaction, so an unbound externally visible operation state is unnecessary. `committed` is absorbing. A closed generation is immutable history; replay opens the next generation, never the closed attempt.

| Input/state | Serialized transition and observable result |
|---|---|
| Initial request, operation absent | Create operation bound to semantic identity, create generation-0 admitted attempt and admission event; only the newly admitted handler may proceed to the effect seam. |
| Same attempt and identical bytes delivered again | Record another transmission, but no new executor, generation or permit consumption. Return original terminal result if available, otherwise pending/unresolved according to the wire contract. |
| Same attempt with changed bytes, or existing key with different semantic identity | Deny the conflicting transmission without changing the original operation or its business state; retain the conflict. |
| Different attempt without the current permit | Reject as unauthorized replay; do not create another effect opportunity. |
| Effect transaction for an admitted attempt | Under operation lock, require open phase, matching current generation/attempt and no terminal fence; commit effect/result/history atomically or perform the specified closure. |
| Finality request, no operation row | Create a bound operation row and a **pre-admission tombstone**, then close generation 0 with the named original attempt/request digest fenced. Issue one permit in that same transaction. This records a fence, not a fictional admission or execution. |
| Finality request, matching open attempt | Acquire the same operation lock as effect commit. If commitment won, return its original result. If closure wins, fence the named/current attempt, close the generation and record no effect plus one permit. A later worker must recheck and cannot commit. |
| Repeated reconciliation of the same closed current generation | Return the existing closure and same unconsumed permit; do not mint another permit or advance generation. |
| Valid permit with fresh attempt ID and identical semantic effect | Atomically consume it once, increment generation, admit the new attempt and append linked events. Business revalidation still precedes its effect. |
| Second permit consumer, stale generation, delayed original or old closure after newer admission | No new effect opportunity. Do not report an old no-effect proof as current finality while a newer attempt is open. Preserve historical closure; current result is unresolved unless a matching commitment is known. |

The operation-row uniqueness/lock serializes concurrent first admission and pre-admission closure. Closure must fence every prior admitted attempt and the named delayed original, not merely set a flag on a response object. If the named request cannot be matched to the current or initial attempt, do not close unrelated newer work. Lock acquisition failure or unconfirmed closure commit returns no finality proof. A permit is exposed only after the closure transaction is known committed; lost closure replies are recovered from the stored closure/permit, not reconstructed as new authority.

The proof races have explicit outcomes: effect commits first → original result; fence commits first → old attempt cannot commit; two replay consumers → one admitted generation; same new attempt redelivered → one executor. The cross-key order-allocation constraint independently blocks a second logical key from allocating again.

Service truth and public projection remain separate. FRD-07B must return the scheduled unresolved observation even though private state contains a commitment. FRD-10D's unsupported cancellation does not reveal it. These are declared exposure boundaries, not edits to the journal. No cancellation result is substituted for finality and no finality call is added where the case disallows one.

## 6. PG-export — A correlated, restorable evidence cut

**Accepted design:** Tad ratified the sealed, correlated export and isolated restore on 2026-09-12 (America/New_York), preserving application knowledge and failures separately; see the [ratification record](agent-code-v2-ratification-record.md). Exact tool versions/command lines, deadlines, row encoding, restore-instance configuration and content/retention permissions remain open. The procedure and required properties are accepted; command fragments below are not a frozen launch/export configuration. Execution, provisioning, export/restore and cleanup remain separately gated.

### Final service seal

Use a private final-seal operation only after the declared terminal boundary or recorded harness abort/deadline, never at an application restart seam or while required case work remains. Seal takes the run guard exclusively, waits only within its frozen deadline for active short transactions, then sets admission closed and records seal identity/reason, still-pending attempts and one-shot-event states. Every late admission/effect checks this state. After sealing, business, clock/catalog, finality and schedule transitions stop; read-only export and delivery bookkeeping may continue, with any post-cut bookkeeping retained separately rather than folded into the original snapshot. No automatic unseal or continuation is allowed after final export; any separately authorized continuation preserves the first evidence cut and gets distinct later evidence.

Sealing is administrative containment, not application-visible proof that uncertain work never happened. Do not mark pending attempts `closed_not_applied`, manufacture a controller terminal answer, consume a replay permit or release stock merely to produce a tidy export. If an active transaction or unavailable fixture prevents a trustworthy seal, retain partial evidence as unavailable; do not stop/restart the shared server to make the export pass.

### Snapshot, dump and restore

1. Allocate an out-of-band export ID and verify the exact enrolled instance/run database, schema manifest and seal. For the initial snapshot, admission has not opened; for the final snapshot, the final seal applies. No in-case snapshot is mislabeled final.
2. Open one custodian Repeatable Read read-only transaction, call `pg_export_snapshot()`, and retain that transaction through inspection/dump. Its snapshot ID is an ephemeral session coordination token, not durable evidence by itself. PostgreSQL allows other sessions to import it only while the exporter remains open. [Snapshot synchronization](https://www.postgresql.org/docs/17/functions-admin.html#FUNCTIONS-SNAPSHOT-SYNCHRONIZATION)
3. In that transaction, enumerate every fixture user relation and record its column/type/key description, exact row count and digest of the complete deterministically ordered rows. Include zero-row relations. Freeze a lossless row encoding before implementation: declared column order, typed nulls/integers/strings, byte payload encoding and stable primary-key sort; no locale-dependent rendering, `SELECT *` contract or omitted row cap. Also record all visible service-event/effect/attempt identities, not a maximum sequence number.
4. Use the second and only other custodian SQL connection for a serial custom-format `pg_dump` of that one run database with `--snapshot` and a bounded lock wait. No parallel jobs, `pg_dumpall`, live-volume copy, unrelated database or new replication slot. Freeze exact compatible server/client/image versions, arguments and total export deadline; retain actual exit status, stderr, byte length and archive digest. `pg_dump` supports an externally supplied snapshot; its lock-wait option does not replace a total wall-time bound. [pg_dump snapshot and timeout options](https://www.postgresql.org/docs/17/app-pgdump.html)
5. Close the exporter on success or failure and retain the original export attempt. Materialize service events from the committed outbox without redoing mutations. Collect application/transport/hook evidence through explicit producer completion/flush acknowledgements and predecessor links. An absent acknowledgement, missing origin stream or unresolved cross-process boundary remains an evidence gap; a database snapshot cannot fill it in. Bytes prepared/sent by the service are not proof that the application received or checkpointed them.
6. Restore the archive once into a fresh, isolated disposable PostgreSQL verification instance with no workbench network or shared PKI/data mounts. The launch identity, temporary credentials and resource limits for this instance remain physical bindings, not permission to create it now. Use an empty target database, controlled non-superuser restore owner, serial `pg_restore --single-transaction --no-owner --no-privileges`; never `--clean`, `--create`, disabled constraints/triggers or a shared-instance target. These restore flags avoid installing source ownership/ACLs and fail the restore transaction on error. [pg_restore](https://www.postgresql.org/docs/17/app-pgrestore.html)
7. Independently enumerate restored relations and compare the complete schema/data manifests, exact counts and row digests to the inspection from step 3. Compare logical contents, not a second dump's archive bytes. Treat source runtime grants/ownership as a separately retained non-secret enrollment manifest; this data restore does not prove runtime access policy. Verify source byte digests, state/history reconstruction and typed results. Preserve mismatches and partial exports; no grading from an unverified substitute copy.

The accepted two-connection maintenance envelope covers exporter plus dump; catalog/manifest inspection reuses the exporter, not a hidden third connection. Restore runs off the shared instance and is not a campaign concurrency exception. Storage/content/retention permissions remain pending: no credential secret belongs in the fixture database or export, and this draft does not authorize raw model-content recording.

The evidence manifest binds archive identity, inspection identity, export/seal IDs, run/schema/implementation identity, source grant/configuration observations and every included external artifact digest. Missing artifacts remain explicitly missing. Sequence allocation, event UUID order and wall-clock timestamps are not commit-order watermarks. A verified database cut establishes service truth at that cut, not everything the application knew and not its outcome-accuracy verdict.

## 7. Verification obligations — planned, not executed

Use the selected Bedrock testing Haffey pytest profile for later implementation. The table refines existing FRDX obligations; it creates no new oracle population or acceptance verdict. These are proposed deterministic integration/contract checks gating fixture acceptance and eventual landing. They are not executable tests or a schema-valid completed strategy: numeric line/branch thresholds, exact test paths and campaign settings remain explicit freeze work. Do not invent zero thresholds to fill the schema.

| Existing obligation | Clean execution boundary | Known-dirty counterpart and required discrimination |
|---|---|---|
| FRDX-sources / FRDX-access | Actual source load/read and restricted SQL identity; complete conflicting/current source set; raw byte round-trip; allowed operations work | Collapse conflicting briefs; normalize byte-sensitive evidence; grant history UPDATE; omit an empty relation from inventory. Completeness/identity/access checks must each detect the named defect. |
| FRDX-reservation | Two live connections contend for the same stock; both mirrored schedules and different-key same-order requests; independent stock reconstruction | In a disposable variant, bypass the necessary duplicate-allocation or stock-safety checks/constraints and force actual duplicate allocation or over-allocation. State detector must fail on that known-bad state; a mutation still blocked by another guard is not the required dirty specimen. |
| FRDX-arrangement | Real transaction boundaries before/after reserve and arrange; lost reply versus definite rejection; immutable request fields | Split effect from journal commit, advance order twice, or recheck already-reserved free stock. Direct state/result comparison detects each defect while retaining the first failure. |
| FRDX-finality | Actual admission/commit/closure races, including reconcile-before-first-admission, exact redelivery, two permit consumers, old generation and changed semantic digest | Skip the inside-transaction fence, mint a second permit, or substitute not-found for closure. Release a delayed original and prove the detector catches the extra execution opportunity/effect. No mocked journal response counts as this proof. |
| FRDX-restart / FRDX-cancel | Actual application process termination at the accepted seams; same service database/run identity; scheduled unresolved and unsupported-cancel views | Reset generation/budget/world, auto-resume a closed attempt, or expose private commitment to cancelled application. State/attempt/knowledge evidence must reject the counterfeit continuation. |
| FRDX-exposure | Park both sides of a case barrier without SQL locks or checked-out connections; exactly one declared hook exposure | Hold a needed lock/connection through the barrier or refire an uncertain hook. Deadline/pool/exposure evidence must distinguish fixture failure from agent behavior. |
| FRDX-evidence | Seal, exported snapshot, serial dump, external producer boundaries, isolated restore and complete row comparison | Use separate snapshots around a concurrent commit, omit first failure/event/empty table, falsify source digest, or restore a truncated/wrong archive. Named comparison must fail; preserve both export and cleanup failures. |

Keep actual SQL/network/process tests in disposable synthetic environments first; exact shared-instance validation still follows EN-access authorization. Expected SQL rollback tests must distinguish declared failure injection from unexpected infrastructure defects. Unexpected fixture failure makes affected proof unavailable; it neither proves agent error nor permits dropping a known first agent failure from its population.

Risk selection: include controlled concurrency, process/connection fault injection, access-boundary checks, schema/byte contracts and paired state/evidence controls. Property/fuzz expansion awaits frozen schema/budgets. Upgrade/downgrade migrations are not a claim of this fresh-database fixture; fresh initialization and isolated restore are required. Production load, shared-server crash/host power loss, distributed failover and hostile administrator defense remain out of scope. None of these deterministic checks replaces cold skill construction, live provider conformance or independent agent accuracy.

## 8. Amendments, remaining bindings and lifecycle

| Artifact | Operation | Result |
|---|---|---|
| This companion | Record all four accepted PG designs; preserve proposed or pending exact physical bindings | One reviewable PostgreSQL work surface with explicit acceptance scope |
| README, physical binding and parent evidence/next-gate pointers | Identify accepted PG-export and recommend wire/identity binding next | Discoverable detail without falsely closing exact schema or earlier gates |
| Ratification record | Retain prior decisions and append the operator's PG-export acceptance | Design only; exact versions/commands, deadlines, row encoding, restore configuration, content/retention permissions and execution remain open |
| Public pack/reference, installed skill/package, database/configuration | No change | Preserve scenario values and the pre-implementation state |

Before calling this implementer-complete, bind executable DDL/constraints and exact column grants; canonical effect/request/source/result encodings and closed schemas; authorization-policy and hook byte contracts; finite operational limits; launch identities and actual enrollment/run window; source and restore-instance manifests; full-row export encoding; external evidence completion protocol; content/retention policy; schema-valid test strategy; and all broader campaign choices. Some are mechanical consequences of accepted designs; substantive additions return for explicit ratification. Do not silently infer them from table names here.

All four PG design choices are accepted within their recorded scopes. Exact physical bindings remain proposed or pending, including wire bytes, DDL/grants, operational limits and the export-specific bindings in §6. Implementation, SQL/concurrency/finality/access/export proof, fixture freeze, cold build, accuracy evaluation and adoption are not performed. This document provides no stored-function implementation, live migration, launch configuration, generated product code or executable handoff. The [PG-state](scenarios/proposed/pg-state-ratification-authoring-checks.json), [PG-transaction](scenarios/proposed/pg-transaction-ratification-authoring-checks.json) and [PG-finality](scenarios/proposed/pg-finality-ratification-authoring-checks.json) authoring reports remain historical evidence; the [PG-export authoring report](scenarios/proposed/pg-export-ratification-authoring-checks.json) records checks after this acceptance. Those checks cover document/data relationships, not SQL behavior.

Ratified current authoring step (WIRE-DRAFTING): bind fixture-facing request/result/error schemas, canonical plan/grant/effect and request identities, version/size/numeric rules and byte examples in the existing contract set. Those definitions constrain the DDL/grant and export-encoding work that follows. Keep agent prompts, role-generation schemas, controller logic and application checkpoint implementation with the cold builder. The exact operator-policy rules, hooks, external evidence completion, enrollment/launch, operational limits, content/retention and campaign/test-strategy work listed above still require closure; completing wire schemas alone does not pass physical freeze.

Prior evidence remains in place with its original identity. Rejected proposals can be explicitly superseded; do not rewrite earlier passing reports against new inputs. No evidence is relocated or deleted. The retrospective remains deferred until the end.

## Change log

| Revision | Date | Change |
|---|---|---|
| draft-1 | 2026-09-12 | All four PG and all four WIRE designs ratified within scope, including sealed correlated export, isolated restore and typed finality results; exact schemas/physical bindings and execution remain open; no runtime work performed |
