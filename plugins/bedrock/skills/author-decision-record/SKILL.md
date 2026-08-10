---
name: author-decision-record
description: "Select the correct engineering decision-record type, then author, amend, or de-drift an ADR, DDR, or SDD while preserving deliberation, provenance, lifecycle metadata, and body integrity. Use when recording why an architecture or design choice was made, documenting a service design, choosing among the house doctypes, or repairing an existing ADR, DDR, or SDD. If selection identifies an implementation-complete construct spec, route its authorship or amendment to author-construct-spec. Do not use for direct construct-spec authorship, reusable standards (author-standard), implementation handoffs (author-execution-relay), product PRDs, finished-code review, or convergence review of a record set (design-review-loop)."
---

# Author a Decision Record

Select and author a durable engineering decision without inventing its deliberation or hiding its dependencies.

## Interaction contract

- **Inputs:** decision scope, real deliberation, current related records, and a risk-domain assessment.
- **Output:** a decision record with typed relations and lifecycle metadata.
- **Authority:** the author may select and shape the record; the operator owns ambiguous routing and acceptance.
- **Capabilities:** a durable artifact home is required. Trackers and graph validators are optional context/capabilities.
- **Failure:** remain proposed or stop when rationale, relation targets, owners, or provisional-dependency controls are missing.
- **Evidence:** cold read, relation validation, and stale-reference sweep.
- **Lifecycle:** proposed → accepted or accepted-with-conditions → superseded, rejected, deferred, or retired.

## Deliberation gate

Do not fabricate rationale or alternatives from a thin request. Use a real comparison, investigation, spike, operator deliberation, or observed system behavior. If it is missing, leave an explicit gap and keep the record PROPOSED.

## Portable record contract and Haffey profile

The portable contract requires context, decision, rationale, alternatives where a choice existed, consequences, ownership, verification, risks, lifecycle, and typed relations. Organizations may map these fields to their own doctypes and homes.

The Haffey profile uses:

- ADR for a platform or cross-service principle;
- DDR for a specific multi-component, data-shape, or technology ruling;
- SDD for the standing design of one service; and
- `author-construct-spec` for an implementer-complete change to one internal mechanism.

Choose the highest useful boundary, not automatically the highest altitude. Linked records at different levels are valid when they have different owners, lifecycles, or decisions and do not duplicate authority. Ambiguous selection returns to the operator.

## Provisional dependencies

An SDD or other downstream record may proceed against a proposed upstream decision when it records the dependency, owner, unresolved assumptions, risk, expiry, and promotion criteria. Block only when uncertainty makes the downstream design unsafe or fictional. A provisional relation cannot silently graduate while its target remains unresolved.

## Body integrity

Preserve concise context, alternatives, rationale, and consequences; those are enduring decision information. Separate operative obligations into identifiable sections. Remove process narration and correction diaries from current-state clauses, but do not strip the “why” that makes the decision intelligible.

Use simple revision identity by default. Use SemVer only when machine consumers and compatibility rules interpret it. Accepted records require owner, verification state, review trigger, supersession/retirement treatment, and accountability.

Security, privacy, compliance, cost, and operational risk receive explicit consideration or a reasoned not-applicable result. Route domain obligations to their owning standards rather than copying their numeric policy.

## Relations and stale references

Relations conform to [the typed relation schema](reference/record-relations.schema.json): `supersedes`, `implements`, `depends-on`, and `conditions`, with stable targets, direction, state, and optional version constraints.

A stale relation is an invalid state, not deferred housekeeping. Repair it in a bounded transaction with dependency-impact analysis, owner, expiry for any temporary exception, and verification before closure. Detect cycles, missing targets, incompatible constraints, orphaned implementations, and broken supersession chains where a graph capability exists; otherwise record the unavailable check.

## Templates

Use the ADR, DDR, or SDD template as a minimal carrier. `FILL:` comments are removed when satisfied. `STANDING:` is the sole machine-readable directive syntax and remains for later amendments.

## Boundaries

Construct-spec authorship → `author-construct-spec`; reusable standards → `author-standard`; executor handoffs → `author-execution-relay`; code review → `code-review`; record-set convergence → `design-review-loop`.
