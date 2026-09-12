# FRD machine-schema candidate

Status: authored and locally tested candidate, not physical freeze or a complete fixture. The four WIRE designs and **SOURCE-order** and **SOURCE-events** below are accepted within their recorded scopes. Recorded 2026-09-12 (America/New_York).

This is a companion to the [accepted wire design](../../wire-and-identity-contract.md), not a new standard or agent solution. Tad ratified proceeding with this translation, examples and non-schema obligations. Prompts, generation schemas, controller and checkpoints remain cold-builder-owned.

## Artifacts and use

- [Wire schema](frd-wire.schema.json): root validates requests. Select the response definition using the already-correlated request action, never by guessing from a response tag. Denial/unresolved shapes intentionally overlap across actions. Generic errors cannot override action-specific finality/exposure rules.
- [Source bodies](frd-source-body.schema.json): select by kind, actual input artifact and lifecycle state. Preserve the pack brief's `order_id`; the reference brief genuinely lacks it and has a separate definition. Do not make that field globally optional or repair original bytes. Accepted SOURCE definitions retain their draft-era identifiers (`RecoveryPlanProposed`, `OrderArrangedProposed`, `SupplierNoticeProposed`) for reference stability; the suffix is historical, not a pending disposition.
- [Derivation entry](frd-source-derivation.schema.json): one source's actual input identity/pointer, body, length/digest and selected definition; not a complete-population assertion. Its pointer resolves to a structured record, not a description of that record.
- [Bindings](wire-schema-bindings.json): exact file identities, action entry points, source applicability and remaining gates. File hashes are not semantic plan/grant/effect hashes.
- [Examples](wire-schema-examples.json) and [tests](test_wire_schema.py): synthetic structural specimens and advisory detectors. Some examples carry shape-only identities or simplified observations; none is an approved business response, canonical terminal-result vector, runtime outcome or frozen case. Existing canonical identity vectors remain separate and unchanged.

All schemas use JSON Schema 2020-12. The local test registry rejects unregistered references; URI identifiers do not authorize network retrieval. Integer semantics do not reject integral fractional/exponent tokens; string lengths do not count UTF-8 bytes; content annotations do not validate nested JSON. [Validation vocabulary](https://json-schema.org/draft/2020-12/json-schema-validation), [local registry API](https://python-jsonschema.readthedocs.io/en/v4.25.1/referencing/).

## Obligations beyond schema validation

| Existing obligation | Separate required check | Evidence here / remaining proof |
|---|---|---|
| FRDX-access / FRDX-sources | UTF-8/scalar validity, duplicate decoded keys, integer tokens, byte/depth/list ceilings, media/framing | Specimen lexical/byte controls only; actual HTTP enforcement remains required |
| FRDX-sources | Body decoding/schema, raw length/digest, kind/record/revision, exact pointer, authenticated trust and publication scope | Complete initial public/reference record shapes checked; selected byte/pointer specimens checked. Full materialization and per-case source catalogs remain pending |
| FRDX-sources / FRDX-evidence | Independent catalog membership and preserved delivery order | Synthetic omission control detects a missing conflicting brief despite valid remaining hashes and shortened membership. Not a real service/snapshot result |
| FRDX-approval / FRDX-finality | Recomputed domain-separated JCS, authenticated scope, accepted refs, current policy/expiry, exact-attempt bytes and permitted replay | Existing vectors validate structurally; no full JCS interoperability, policy or replay proof |
| FRDX-finality / FRDX-arrangement | Original committed-result decoding/digest/kind/attempt/JCS bytes; independent durable effect/fence/permit joins | Selected byte/committed-kind controls only; schema-valid counterfeit commitment, stale closure and private-state disclosure still need actual boundary detection |
| FRDX-restart / FRDX-cancel / FRDX-evidence | Dispatch/receipt/checkpoint knowledge, budgets, cancellation and scheduled exposure | No runtime proof; schema-valid error/cancellation supplies no effect conclusion |

Source-ref sets must also reject identical kind/record/revision with differing digests: `uniqueItems` alone only detects identical full objects. Canonical ordering, cross-field equality, revision increments, grant duration and authorization require separate checks. Retain authenticated request/observation correlation outside the response body.

## SOURCE-order — Accepted post-arrangement order binding

Accepted design: retain existing order fields; set service `status` to `arrangement_recorded` and `reservation_id`; advance revision once; populate `recovery_plan` with `{arrangement_id, plan_digest, approval_id, grant_digest, terms}`. Terms uses the accepted structure. Preserve customer, requested SKU, quantity, destination, original source and shipment/delivery facts. Reservation alone leaves the order unchanged.

The prior state-commit design required attached terms, reservation and service status without specifying this exact nested shape. Tad separately ratified this shape as presented. Including immutable arrangement/plan/approval references makes the order independently joinable without copying the whole grant or claiming desk completion. A smaller terms-only projection reduces duplication but requires more external joins. `RecoveryPlanProposed` and `OrderArrangedProposed` embody the now-accepted choice; their stable identifiers and schema assertions are unchanged. Acceptance does not establish relational enforcement or runtime proof.

## SOURCE-events — Accepted typed event-source provenance

Accepted design: author a separate immutable structured source-record catalog for event-created notices, revised/conflicting briefs and new quotes before materialization. Bind each entry to the original case/event pointer and specification-artifact digest; derive JCS bytes from the structured record itself. Preserve the public pack unchanged. Do not parse event prose into source bodies at runtime or claim prose strings were original structured records.

For notices, use `{record_id, revision, source_class: "supplier_data", message}` with the exact intended supplier message. Keep order visibility and trust in the authenticated catalog/provenance, permitting shared notices without fabricating order fields. A body label never elevates supplier instructions to authority. Revised briefs/quotes retain their existing shapes and fields.

The derivation entry's `event_origin` is required by the accepted design for event-derived records, while its schema remains optional for ordinary originals. An independent provenance check must distinguish applicability and verify both actual structured input and governing event. Event provenance is private fixture/evaluator metadata, not added to actor-visible bodies or an evaluator answer channel.

The complete initial public source population contains no notice bodies; notices and later revisions/quotes are described in the complete event schedules. Initial examples therefore cannot certify those physical records. A separately bound catalog preserves the original accepted identities; the alternative of embedding records directly in the pack would change them. Tad ratified this design as presented. The catalog remains to be authored; acceptance does not add scenarios or permit materialization/initialization.

## Verification and remaining gates

The [source-ratification report](source-bindings-ratification-authoring-checks.json) records this acceptance/status pass, unchanged schema assertions and specimen values, current checks and preserved earlier evidence. The prior [authoring report](wire-schema-authoring-checks.json) retains commands/results, identities, the interrupted first run and a complete targeted reproduction. The initial legacy reference resolver failed before specimen validation. Its oversized output was truncated and is explicitly partial evidence. In the same pinned engine, the maintained registry accepted the unchanged positive and rejected the dirty specimen. No schema was weakened to get that result.

Use an isolated environment with [authoring dependencies](requirements-authoring.txt), then run from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 <authoring-python> -m pytest -q --tb=short -p no:cacheprovider docs/evidence/heb-154/agent-code-v2/schemas/proposed/test_wire_schema.py
```

This is deterministic advisory schema authoring, not the final schema-valid campaign strategy. Line/branch thresholds, advanced-method selections, budgets and runtime gates remain pending. No fake zero thresholds or reference/import failures count as meaningful-red runtime evidence. Real parser, SQL races, access, fault/restart/cancellation and full agent build-use/accuracy proof remain required.

Before machine-schema closure: reconcile exact error precedence and operator-policy predicates; bind typed event sources and provenance applicability; complete relational/byte checks against the eventual full population; identify the reviewed final artifacts. Hook/admin/external-evidence schemas, DDL/grants, export encoding, enrollment/launch/limits/retention and campaign freeze remain separate gates. No fixture services, database objects, credentials, provider calls or agents were created. The retrospective remains deferred until the end.
