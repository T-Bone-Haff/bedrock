# Fulfillment-recovery wire and canonical identity draft

| Field | Value |
|---|---|
| Document ID | FRD-WIRE-IDENTITY |
| Parent construct | [Execution contract](execution-contract.md), [physical binding](physical-runtime-binding.md), [PostgreSQL contract](postgresql-persistence-contract.md) |
| Revision | draft-1 |
| Status | PROPOSED; all four WIRE designs accepted within their recorded scopes; exact physical bindings remain pending; not implementer-complete or execution authorization |
| Owner | Tad Haffey |
| Recorded | 2026-09-12 (America/New_York) |
| Review trigger | Individual WIRE ratification; machine-schema expansion; before physical freeze |
| Doctype ruling | Companion to the existing internal proving fixture, not an agent design or reusable standard |
| Deliberation substrate | Accepted EC, PB, EN and PG decisions; WIRE-DRAFTING ratification |
| Supersedes | None |

## 1. Scope and review decisions

Define the public fixture's data boundary without supplying the cold builder's prompts, role-generation schemas, controller, provider adapters or application checkpoint implementation. The [public pack](scenarios/proposed/scenario-pack.json) and [reference](scenarios/proposed/frd-01.json) retain their bytes and business meanings. This document does not introduce cases, permission to spend, an approval-policy implementation or an evaluator answer channel.

The operator authorized this drafting step and has now separately accepted WIRE-envelope, WIRE-identity, WIRE-sources and WIRE-outcomes within their recorded scopes. These design acceptances do not establish machine-schema completion, complete physical bindings or runtime proof.

| Decision | Recommendation | Alternative / trade-off |
|---|---|---|
| WIRE-envelope | Accepted design: one versioned, closed HTTP/JSON action boundary; strict lexical rules, safe integers and finite byte limits. Machine-schema completion and runtime validation remain pending | Permissive coercion/additive fields reduce rejection but hide drift and cross-language identity disagreements. Strictness makes incompatible changes explicit. |
| WIRE-identity | Accepted design: separate physical-byte SHA-256 from domain-separated JCS plan/grant/effect identities, including immutable grant-content binding; exact machine-schema artifacts and runtime proof remain pending | Hashing only parsed JSON loses transport evidence; hashing only raw bytes makes harmless formatting a different business effect. Canonicalization adds one precisely bounded dependency. |
| WIRE-sources | Accepted design: preserve immutable source bytes, one-time derived-source provenance and explicit complete publication scope, independently checked; preserve response array order. Full materialization, exact schemas and runtime proof remain pending | Latest-revision selection or a truncated list is simpler but can conceal conflicting briefs or restore an incomplete source as if complete. Explicit inventories add modest fixture metadata. |
| WIRE-outcomes | Accepted design: closed, action-specific results, pending-mutation unresolved and original committed-result bytes on reconciliation; ordinary errors and cancellation never imply durable no-effect finality. Exact policy/error precedence, machine schemas and runtime proof remain pending | A universal success/failure response is smaller but conflates known rejection, unknown effect, service truth and application knowledge. |

This is an accepted design grammar within an unfinished physical draft, not a completed physical-schema contract. The [machine-schema candidate](schemas/proposed/README.md) now supplies a JSON Schema 2020-12 translation and raw artifact bindings, checked against the declared record fields and specimens. SOURCE-order and SOURCE-events are separately accepted exact body/provenance designs; the schema candidate and all remaining physical gates retain their unfinished status. Lexical, byte-limit and relational obligations that JSON Schema alone cannot enforce remain explicit. No translation silently settles open policy or error precedence; schema completion remains a physical-freeze gate.

## 2. WIRE-envelope — Strict public boundary

**Accepted design:** Tad ratified WIRE-envelope on 2026-09-12 (America/New_York); see the [ratification record](agent-code-v2-ratification-record.md). Acceptance covers the strict versioned public envelope and the safety ceilings below, not empirical calibration, a completed machine-schema bundle or runtime proof. WIRE-identity, WIRE-sources and WIRE-outcomes have separate acceptances in §§3–5, including the outcome/error mapping below. Error precedence, policy and deployment bindings remain open.

Use `POST /frd/v1/actions` on the already-accepted local plain-HTTP fixture listener. Private administration remains on its separate Unix socket. No redirect, automatic retry, proxy replay or failover; provider TLS and the separately accepted database credentials remain unchanged.

Both directions use `application/json`, UTF-8, no BOM or content compression. JSON consists of exactly one object, with only JSON whitespace outside it. Reject invalid UTF-8, unpaired surrogates, duplicate decoded member names at any depth, non-JSON literals, trailing payloads and unknown fields. Do not salvage, coerce, default a missing field, strip prose or repair a fixture message. This strict fixture boundary does not change Agent Code's separately governed LLM-output salvage policy.

Accepted safety ceilings: request and response body each at most 1,048,576 UTF-8 octets; each source body at most 262,144 octets; root container depth 1 and maximum nested container depth 32; identifier length 1–128 ASCII characters; question/reason text at most 4,096 UTF-8 octets; each list at most 256 elements. A source or complete observation too large to fit is unavailable, not truncated or silently paginated. These are deliberately roomy design ceilings, not empirically calibrated limits, measured provider/context budgets or SQL deadlines. Check the full eventual frozen public/hidden fixture population against them before accepting the launch manifest; an over-limit hidden input is a fixture-design problem, not an agent error. Any change to an accepted ceiling returns for explicit disposition rather than silently relaxing it.

Use whole, nonnegative safe integers `0..9007199254740991`; positive quantities/revisions start at 1. Numeric tokens must match `0|[1-9][0-9]*`: no fractions, exponent notation, negative zero, numeric strings or booleans. Validate tokens before floating-point conversion. Signed environmental deltas are private-administration data and outside this public schema. Checked increments and sums must remain in range, not wrap or round. This wire range is deliberately narrower than PostgreSQL bigint. JSON Schema's integer predicate alone does not enforce these lexical rules; string length keywords do not enforce UTF-8 byte limits. [JSON Schema validation vocabulary](https://json-schema.org/draft/2020-12/json-schema-validation)

### Closed-record notation

`{field: Type}` lists every required field; `field?: Type` is the only optional-field notation. No other members are allowed. `A | B` is an exclusive tagged union. `T[]` is an ordered list (0–256); `T[1+]` requires at least one element. `Set<T>` is a duplicate-free list with the explicit semantic sorting rule in §3, not permission to reorder evidence. `null` is a value only where listed. All record types below are scoped to this draft.

```text
Id        = ASCII string matching [A-Za-z0-9][A-Za-z0-9._:-]{0,127}
Digest    = string matching sha256:[0-9a-f]{64}
UInt      = integer 0..9007199254740991, subject to lexical validation
Positive  = UInt >= 1
Text      = Unicode scalar string, 1..4096 UTF-8 octets
Kind      = "inventory.reserve" | "arrangement.record"
SourceRef = {kind: "order" | "customer_brief" | "supplier_notice" | "quote" | "stock",
             record_id: Id, revision: Positive, content_digest: Digest}
Request   = {protocol_revision: "frd-wire-1", run_id: Id, request_id: Id,
             order_id: Id, action: Action, payload: PayloadForAction}
Response  = {protocol_revision: "frd-wire-1", request_id: Id,
             observation_id: Id, observed_at_minute: UInt, result: ResultForAction}
          | {protocol_revision: "frd-wire-1", request_id: Id,
             observation_id: Id, observed_at_minute: UInt, error: ActionError}
```

The trusted caller is resolved from the opaque transport credential, never from a model-supplied role or an ID. Require envelope run/order agreement with authenticated scope and all nested identities. Treat identifiers as exact case-sensitive values, not sortable time, paths or authority. Store only the non-secret credential identity in evidence, not the credential header. Header name/value binding remains an enrollment detail.

Use an observation envelope only after a valid request has been correlated to the run and its business clock. A pre-envelope failure uses `ProtocolError = {protocol_revision: "frd-wire-1", error_code: ProtocolCode, receipt_id: Id}` without invented request/order/time values. A receipt is correlation, not a durable SQL receipt or effect proof. If no trustworthy error can be emitted, close/lose the reply and retain external evidence if available.

HTTP mapping accepted with WIRE-outcomes: parsed business results (including denial, rejection and unresolved) use 200; `ProtocolCode` is `invalid_json` or `invalid_envelope` → 400, `unauthenticated` → 401, `forbidden_scope` → 403, `body_too_large` → 413, `unsupported_media_type` → 415, `unsupported_revision` → 400. `ActionError` is `{code: "identity_conflict" | "unauthorized_replay" | "run_sealed" | "fixture_unavailable", message: Text}`; codes map to 409 except `fixture_unavailable` → 503. HTTP 200 denotes a valid business response, not business success. Exact validation/error precedence, listener-level unknown route/method handling and deployment framing limits remain transport-bindings work. Never infer no effect from an HTTP status, an error receipt, an exception or a dropped connection. No error contains a replay instruction, replacement plan or private commitment details.

## 3. WIRE-identity — Bytes are not business semantics

**Accepted design:** Tad ratified WIRE-identity on 2026-09-12 (America/New_York), including grant-content binding and separation of physical and semantic identity; see the [ratification record](agent-code-v2-ratification-record.md). The hash inputs, domain framing, semantic projections and explicit-set ordering below are accepted design. WIRE-sources and WIRE-outcomes have separate design acceptances in §§4–5. Full machine-schema artifacts, actual source materialization, implementation and cross-runtime/SQL proof remain separately gated. Acceptance supplies no new replay, approval or content-capture authority.

Use `sha256:` followed by 64 lowercase hexadecimal digits. Digests detect identity/integrity; they are not signatures, authentication or authority. Recompute rather than trust caller-supplied values.

For semantic identity, use RFC 8785 JSON Canonicalization Scheme (JCS). It fixes JSON serialization and recursive property ordering, preserves array order and Unicode string contents, and emits UTF-8. It does not normalize Unicode. The accepted wire rules additionally restrict numeric tokens and explicitly normalize the few fields defined as sets before semantic hashing. Do not substitute Python `sort_keys`, PostgreSQL JSON rendering or locale sorting for a general JCS implementation. [RFC 8785 §§3.1–3.2.4](https://www.rfc-editor.org/rfc/rfc8785.html#section-3)

For each domain below, semantic preimage is precisely:

```text
UTF8(domain) || one byte 0x00 || JCS(value)
```

No newline, BOM, implicit wrapper, digest field or terminating NUL is added. A raw digest, by contrast, is simply SHA-256 of the stated bytes without a domain prefix. Never migrate the existing public pack's hash convention to JCS implicitly.

| Identity | Domain and exact value / byte input |
|---|---|
| Physical request | Raw HTTP entity-body octets sent for that transmission, after HTTP transfer framing is removed, before JSON parsing. Compression is forbidden. Excludes HTTP headers and credentials. |
| Physical response | Raw entity-body octets, independently recorded as prepared, sent and received where actually observed; a prepared digest does not prove receipt. |
| Source content | Raw immutable source-body UTF-8 octets defined in §4; source-ref identity also includes kind/record/revision. |
| Plan | Domain `frd/plan/v1`; value `{run_id, plan: Plan}` with its requirement-reference set sorted below. |
| Grant | Domain `frd/grant/v1`; value `{run_id, grant: Grant}` excluding an external `grant_digest` wrapper field. Plan digest is recomputed and must agree with full approved plan. |
| Effect | Domain `frd/effect/v1`; value `{run_id, order_id, operation_kind, plan_digest, approval_id, grant_digest, expected_order_revision, terms: Terms, reservation_id}`. Reservation uses explicit null; arrangement uses the confirmed reservation ID. |
| Original terminal result | Raw UTF-8 bytes of the stored terminal result object alone, encoded once with JCS at its original commit; distinct from each later response envelope and its observation identity. |

```text
Terms = {quote_ref: SourceRef, site: Id, sku: Id, quantity: Positive,
         destination: Id, estimated_arrival_time: UInt,
         extra_transport_cost_minor: UInt, currency: "USD", expires_at: UInt}
Plan  = {plan_id: Id, revision: Positive, order_id: Id, order_revision: Positive,
         requirement_source_refs: Set<SourceRef>[1+], terms: Terms}
Grant = {approval_id: Id, issuer_id: Id, policy_id: Id, policy_revision: Id,
         plan_digest: Digest, approved_plan: Plan,
         issued_at_minute: UInt, expires_at_minute: UInt,
         allowed_operations: ["inventory.reserve", "arrangement.record"],
         arrangement_requires_matching_reservation: true}
```

Plan identity intentionally includes plan ID/revision and source identities, not merely outcome-equivalent terms. Effect identity includes immutable grant content as well as approval ID. Replacing a grant or accepted brief is not the same approved effect, even if quantity/site are unchanged. Exclude operation key, request/attempt IDs, generation and permit from the effect preimage: the key names the operation; the digest independently checks its semantics. The journal still binds both and the cross-key order guard still applies. Adding `grant_digest` to the mutation wire is an accepted WIRE-identity refinement of PG-finality, not a new approval channel: the ID locates the immutable grant and the digest independently binds its exact content.

A same-attempt redelivery still requires the original exact request bytes. Reformatting those bytes is an identity conflict even when the semantic digest is unchanged. An authorized replay instead uses a fresh attempt/request identity and the service's permit, changing the physical digest while preserving the approved effect identity. Current authority, business predicates, case allowance and budget remain independently required. Changing the approved grant or terms changes effect identity and cannot reuse the old logical key as if nothing changed.

Sort `Set<Id>` by ASCII value. Sort `Set<SourceRef>` by `(kind, record_id, numeric revision, content_digest)` with exact ASCII string comparison. Reject duplicate references and same `(kind, record_id, revision)` with differing content digests; do not deduplicate silently. Only explicit request/plan sets receive this semantic normalization. Preserve raw request bytes, source bytes, response list order, approved operation order and every ordered provider-context manifest unchanged. Thus reordered requirement references may have one plan digest while their physical request digests differ. Changing Unicode composition changes content identity.

Scope checks are relational, not accomplished by hashes alone: quote_ref must name a quote; requirement refs must name accepted customer briefs; Plan.order_id/revision, grant plan and requested Terms must agree with authenticated run/order and current applicable authority. Approval expiry must be later than issuance and no later than its bound quote expiry. Its exact policy-determined duration remains open. A valid digest of an invalid proposal is still an invalid proposal, not authority.

## 4. WIRE-sources — Complete observations, original bodies

**Accepted design:** Tad ratified WIRE-sources on 2026-09-12 (America/New_York), including one-time derived source bytes and independently checked completeness; see the [ratification record](agent-code-v2-ratification-record.md). Acceptance covers exact immutable source retrieval, explicit publication/supersession scope, unfiltered scoped availability, source-byte provenance and the independent completeness obligation below. Full source materialization, exact body/manifest schemas, implementation and real omission-detection proof remain pending. WIRE-outcomes has its separate acceptance in §5. Neither acceptance grants content-capture permission or authorizes fixture initialization.

```text
Source = {source_ref: SourceRef, body_utf8: Unicode scalar string,
          body_length_bytes: UInt}
Publication = {publication_id: Id, catalog_epoch: UInt, source_ref: SourceRef,
               supersedes: Set<SourceRef>, published_at_minute: UInt}
ObservationScope = {catalog_epoch: UInt, complete: true,
                    member_refs: Set<SourceRef>}
```

`body_utf8` is the exact source document decoded as UTF-8. JSON escaping in the outer HTTP envelope is not part of the source body. Re-encode the decoded string without newline/Unicode normalization; byte length and raw content digest must match. Every source body has the agreed raw-record shape for its kind; it contains actual source data, not interpreted evaluator requirements. Trust class comes from fixture-authenticated source provenance, not an instruction in its message.

The current public pack contains structured objects, not separately preserved source-body files. At initialization, materialize each original actor-visible record as JCS UTF-8 **once**, with a manifest binding pack digest, world ID, exact JSON pointer, kind/record/revision, resulting bytes, byte length and digest. These are honestly labeled derived fixture source bytes, not claimed original pack substrings. Preserve every original field and message; never add oracle fields. `frd-01.json` and the full pack differ in some wrapper fields, so each derivation names its actual input rather than silently merging them. Later published revisions use the same explicit provenance path. Materialization and its exact manifest schema remain pre-freeze work.

An order-context read returns all current customer briefs and all published supplier notices for the scoped order, plus the current order source. Same-minute equal-authority conflicts both remain current until explicit supersession. Revision maximum across unrelated record IDs cannot select a winner. Source lookup is exact by the entire SourceRef and permission; no fallback to latest, excerpt or summary. A superseded but authorized immutable source remains readable by its exact identity. A newer quote is absent before its publication event.

Availability returns all matching published stock and quote sources within the explicit SKU/site scope, including zero-stock, expired, late and forbidden-substitution candidates. It does not add feasibility, approval, ranking or failure-oracle labels. Returned `member_refs` must equal the returned full-body source identities, without duplicates. Its `complete: true` is a service assertion that the evaluator must independently test against the snapshot and publication history; an internally consistent omitted record can still be a fixture defect. No body-free list is advertised as a complete observation.

The completeness proof must include a known-dirty observation that omits an equally current conflicting brief while retaining valid hashes for every remaining record, including an internally consistent shortened membership list. The independent snapshot/publication comparison must detect the omission. Comparing the response's bodies only with its own membership list is insufficient. This is a required later boundary test, not a passing result established by this ratification.

Source order is delivery evidence. The ordinary fixture may choose deterministic presentation order, but the declared context-order perturbation must survive into the application evidence without being “fixed” by semantic hashing. FRD-13B source recovery returns the full original accepted source, including its substitution restriction.

## 5. WIRE-outcomes — Action schemas and durable finality

**Accepted design:** Tad ratified WIRE-outcomes on 2026-09-12 (America/New_York), including pending-mutation `unresolved` and preservation of original committed-result bytes; see the [ratification record](agent-code-v2-ratification-record.md). Acceptance covers the action-specific result/error structures and HTTP mapping, durable commitment/no-effect distinctions, and separation of service truth from application knowledge. Exact policy/error precedence, machine-schema completion and runtime proof remain gated. No result creates a new retry, reconciliation or cancellation allowance.

Payload/result definitions below refine all nine logical actions in the parent; action identity comes from the correlated request, not an unvalidated response claim. Literal `tag` fields distinguish every result variant. The generic ActionError alternative in §2 is also possible but establishes no finality. It does not override accepted action-specific PG-finality results: a reconciliation identity mismatch remains `unresolved` with `identity_conflict`, and scheduled unresolved exposure must not disclose private commitment. This preserves those settled cases without choosing the remaining validation/error precedence.

| Action | Closed payload | Closed result variants |
|---|---|---|
| `order_context.read` | `{}` | `{tag: "context", scope: ObservationScope, order: Source, customer_briefs: Source[1+], supplier_notices: Source[], publications: Publication[]}` |
| `source.read` | `{source_ref: SourceRef}` | `{tag: "source", source: Source}` or `{tag: "unavailable" \| "denied", reason: Text}` |
| `availability.read` | `{skus: Set<Id>[1+], sites: Set<Id>[1+]}` | `{tag: "availability", scope: ObservationScope, skus: Set<Id>[1+], sites: Set<Id>[1+], inventory: Source[], quotes: Source[], publications: Publication[]}` |
| `requirements.clarify` | `{field: "deadline" \| "destination", question: Text, source_refs: Set<SourceRef>}`; envelope request_id supplies correlation | `{tag: "accepted_revision", source: Source, publication: Publication}` or `{tag: "unresolved" \| "unavailable", reason: Text}` |
| `approval.request` | `{plan: Plan, plan_digest: Digest}` | `{tag: "granted", grant: Grant, grant_digest: Digest}` or `{tag: "denied" \| "unavailable", reason: Text}` |
| `inventory.reserve` | `Mutation` with `reservation_id: null` | `CommittedReservation` or `Rejected` or `{tag: "unresolved", reason: UnresolvedReason}` |
| `arrangement.record` | `Mutation` with `reservation_id: Id` | `CommittedArrangement` or `Rejected` or `{tag: "unresolved", reason: UnresolvedReason}` |
| `operation.reconcile` | `{operation_key: Id, attempt_id: Id, original_request_digest: Digest, operation_kind: Kind, semantic_effect_digest: Digest}` | `ReconciledCommit` or `{tag: "closed_not_applied", closure: Closure}` or `{tag: "unresolved", reason: UnresolvedReason}` |
| `operation.cancel` | `{operation_key: Id, attempt_id: Id}` | `{tag: "accepted" \| "unsupported"}`; neither variant includes private effect or closure data |

```text
Mutation = {operation_key: Id, attempt_id: Id, plan_digest: Digest,
            approval_id: Id, grant_digest: Digest, expected_order_revision: Positive,
            terms: Terms, reservation_id: Id | null,
            semantic_effect_digest: Digest, replay_permit_id?: Id}
OperationIdentity = {run_id: Id, order_id: Id, operation_key: Id,
                     operation_kind: Kind, semantic_effect_digest: Digest}
AttemptIdentity = {operation: OperationIdentity, attempt_id: Id,
                   generation: UInt, original_request_digest: Digest}
Reservation = {reservation_id: Id, committed_attempt: AttemptIdentity,
               plan_digest: Digest, approval_id: Id, grant_digest: Digest,
               terms: Terms, stock_id: Id, stock_revision_before: Positive,
               stock_revision_after: Positive, committed_at_minute: UInt}
Arrangement = {arrangement_id: Id, committed_attempt: AttemptIdentity,
               plan_digest: Digest, approval_id: Id, grant_digest: Digest,
               reservation_id: Id, terms: Terms, order_revision_before: Positive,
               order_revision_after: Positive, committed_at_minute: UInt,
               service_status: "arrangement_recorded"}
CommittedReservation = {tag: "committed", operation_kind: "inventory.reserve",
                        effect: Reservation}
CommittedArrangement = {tag: "committed", operation_kind: "arrangement.record",
                        effect: Arrangement}
Terminal = CommittedReservation | CommittedArrangement | Rejected
ReconciledCommit = {tag: "committed", original_result_utf8: string,
                    original_result_digest: Digest}
Closure = {closed_attempt: AttemptIdentity, fence_event_id: Id,
           closed_at_minute: UInt, replay_permit_id: Id}
Rejected = {tag: "rejected", reason: RejectionReason, closure: Closure}
RejectionReason = "no_stock" | "allocation_exists" | "stale_order"
                | "stale_source" | "stale_quote" | "expired_quote"
                | "invalid_authority" | "expired_authority" | "terms_mismatch"
                | "reservation_mismatch" | "order_write_rejected"
UnresolvedReason = "pending" | "journal_unavailable" | "identity_conflict"
                 | "finality_unproven" | "not_found" | "stale_generation"
```

`ReconciledCommit.original_result_utf8` must decode to a committed Terminal of the matching operation kind, never Rejected, and its exact UTF-8 digest must verify. It returns original effect/attempt/commit data, not a newly executed effect. It does not return a private record on scheduled unresolved exposure. This nested string preserves the immutable original result bytes while allowing the outer observation to be new. The same Terminal may be returned structurally on an exact duplicate transmission; transmission evidence still has distinct receipts.

A Closure is valid only after the accepted PG-finality transaction has durably fenced the named original/current attempt and all prior execution opportunities, with no committed effect. Its generation and original request digest must match the identified attempt; scope and semantic identity bind its single-use permit. No `effect_applied: false` boolean, generic rejection or SQL rollback exception substitutes for that proof. An expired or consumed permit, changed identity or old generation does not reopen an attempt. Returning an old closure while newer work is open must instead be unresolved. Reconciliation repeated before permit consumption returns the same closure and permit.

The accepted mutation `unresolved` variant handles admitted pending/exact-redelivery states already present in PG-finality without inventing rejection. It is not an additional retry allowance. The typed rejection-reason vocabulary above is accepted; exact predicate and precedence binding remains operator-policy/transaction work. `order_write_rejected` identifies the declared fault, not an arbitrary caught SQL exception. No_stock may be avoided by permitted preflight detection in the contention cases; the wire contract does not force a bad dispatch to obtain a rejection.

Committed records must match approved terms and actual state: reservation stock revision advances once with the decrement; arrangement order revision advances once, references its confirmed reservation and never decrements stock again. The service status is not the desk's `recovery_arranged` outcome. Communications and knowledge checkpoints remain separately necessary. Cancellation accepted/unsupported conveys no effect disposition; FRD-10D neither reveals private commitment nor acquires a new reconciliation allowance.

## 6. Verification, amendments and remaining gates

The [identity examples](scenarios/proposed/wire-identity-examples.json) are synthetic authoring vectors, not service responses or evidence of a successful agent. They retain exact preimage/byte representations and derived digests. Authoring checks must compare them independently, change one load-bearing field and require discrimination, and preserve the first check results. They do not implement the fixture canonicalizer or validate real traffic.

| Existing obligation | Required later boundary proof | Known-dirty discrimination |
|---|---|---|
| FRDX-access / FRDX-sources | Real HTTP request parser plus full versioned observation and exact source read | Duplicate decoded key, oversized UTF-8, integer rounding, unknown field, missing conflicting brief, false complete scope and normalized source bytes must fail the appropriate detector |
| FRDX-finality | Actual journal/HTTP admission, closure, replay and reconciliation with these identities | Alter grant/terms/reservation; reuse attempt with changed bytes; use old closure or consume permit twice; detector must observe rejection/no extra executor without treating generic errors as finality |
| FRDX-reservation / FRDX-arrangement | Independent state/result joins across actual commits and lost replies | Counterfeit committed result, mismatched source or second decrement must fail even with valid schema/digests |
| FRDX-evidence / FRDX-restart / FRDX-cancel | Prepared/sent/received/checkpointed bytes joined without conflating knowledge | Lost reply claimed received, scheduled private truth disclosed, reset attempt identity or prohibited post-cancel reconciliation must be detected |

Later deterministic contract/integration tests use the selected Bedrock Haffey pytest profile without selecting a service framework. They gate fixture acceptance/landing; authoring checks are advisory. This table is not a schema-valid final test strategy: numeric coverage thresholds, exact paths, full advanced-method selections and budgets remain campaign work. No meaningless zero thresholds or import failures count as meaningful-red execution evidence.

Amendments: retain this companion and original identity vectors; preserve the authored machine-schema candidate and tests; append the separate SOURCE-order and SOURCE-events acceptances; align schema annotations, specimen disposition metadata, artifact bindings and current status pointers without changing schema assertions or specimen values. Preserve all prior reports and public/reference/checker/example bytes. No installed skill, package, fixture implementation, database, credential or service-network changes. Isolated temporary authoring dependencies do not provision the proving fixture. No evidence moved or deleted.

Before implementer-complete: expand/validate exact machine schemas and all source-body/derivation-manifest schemas against the four accepted WIRE designs; settle validation/error precedence and authorization-policy predicates; materialize and identity-bind the complete source population; add positive/dirty action-union examples and real parser/canonicalizer cross-runtime vectors; bind hook/admin/external-evidence schemas, DDL/grants and full-row export encoding; finish enrollment/launch/limits/content-retention/test-strategy/campaign bindings. Surface substantive gaps for individual ratification rather than silently deciding them in schema code. A local wire schema cannot close those other gates.

Read depth: parent execution/business/reference authorities and selected construct-spec/testing instructions were read whole; missing portions of truncated rereads were explicitly repaired. All public event schedules and distinct actor-visible initial object shapes were read as complete scoped projections, not a whole human reread of every public-pack field or any hidden/native population. Relevant RFC 8785 and JSON Schema passages were read, not their entire documentation corpora. The [authoring report](scenarios/proposed/wire-drafting-authoring-checks.json) names mechanically checked surfaces and exclusions. No Docker/SQL/live-provider/agent verification occurred.

All four WIRE designs are accepted within their recorded scopes. The [machine-schema candidate and review](schemas/proposed/README.md) and its [authoring report](schemas/proposed/wire-schema-authoring-checks.json) record the prior translation pass. SOURCE-order and SOURCE-events are now separately accepted as presented; the [source-ratification report](schemas/proposed/source-bindings-ratification-authoring-checks.json) records current scoped authoring verification. The [WIRE-outcomes report](scenarios/proposed/wire-outcomes-ratification-authoring-checks.json) and all earlier reports remain historical evidence. The prior translation pass read the wire companion whole after repairing its truncated identity section, selected skills/references whole, complete initial-source and event-schedule projections, and scoped parent state/status and latest ratification passages. A bulk status read was truncated and replaced by complete amendment-passage reads; no whole-parent reread is claimed. Hidden/native populations and live substrate were not inspected. Authoring validation is separate from full source materialization, runtime implementation, verification, freeze and adoption. The retrospective remains deferred until the end.

## Change log

| Revision | Date | Change |
|---|---|---|
| draft-1 | 2026-09-12 | All four WIRE designs accepted within scope; machine-schema candidate and advisory tests authored, with SOURCE-order/SOURCE-events separately accepted as presented; exact policy/physical bindings and full materialization pending; no runtime implementation or execution |
