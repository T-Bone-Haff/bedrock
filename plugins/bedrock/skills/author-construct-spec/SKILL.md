---
name: author-construct-spec
description: "Internal engineering machinery only; product or feature requirements documents (PRDs) are explicitly outside this skill and have no Bedrock route. Use this skill to author or amend an implementation-complete construct spec for one runner, harness, instrument, pipeline, or other internal mechanism when an implementer must build it from the document alone. Never infer construct-spec ownership merely because a request says specification or requirements. Do not use for reusable standards (author-standard), finished-code review, or general architecture documentation; author-decision-record owns engineering doctype selection and integrity."
---

# Author a Construct Spec

A construct spec defines a change to one internal mechanism so a competent implementer can build it from the durable artifact set without conversation or private tracker access.

## Interaction contract

- **Inputs:** a doctype ruling, real deliberation or observed behavior, current authorities, and verified target facts.
- **Output:** an implementer-complete specification with stable obligations, evidence treatment, and lifecycle state.
- **Authority:** the author shapes the spec; the operator owns ambiguous routing, design acceptance, and graduation.
- **Capabilities:** a repository-readable durable artifact set is required. A tracker is optional process context, never required contract authority.
- **Failure:** stop on ambiguous doctype, invented rationale, inaccessible authority, or evidence relocation that cannot be verified and rolled back.
- **Evidence:** cold-buildability, obligation reconciliation, and destination integrity for copied evidence.
- **Lifecycle:** proposed → accepted design → implemented → verified → graduated or retired.

## Route before authoring

Use the portable tests even when the local organization uses different names:

- A platform or cross-service principle is a decision record.
- The standing design of one service is a service-design record.
- A reusable rule is a standard.
- A product or feature requirement has no Bedrock construct-spec route.
- A change to one internal mechanism for a cold implementer is a construct spec.

The Haffey ADR/DDR/SDD taxonomy is one profile, not a universal ontology. When two homes remain plausible, present the discriminator and stop for the operator.

The core contract is self-contained here. `author-decision-record` may help select the doctype when available, but loading it is not required to author a construct spec once the ruling and substrate are supplied.

## Required shape

Use the [minimal template](templates/construct-spec-template.md). It carries only operative structure; detailed evidence and lifecycle guidance is in [lifecycle and evidence](reference/lifecycle-and-evidence.md).

The spec contains:

1. scope, orientation, authorities, and non-goals;
2. decisions and rationale grounded in supplied substrate;
3. amendments, including deliberate non-changes where ambiguity matters;
4. correctness invariants and stable obligation IDs;
5. verification instruments and whether each gates landing;
6. risks, failure behavior, and deferred work with triggers; and
7. lifecycle state and evidence required for the next transition.

One invariant per section is a readability heuristic. Keep coupled invariants together when splitting them would hide their relationship; state those links explicitly.

Use stable semantic IDs such as `parse-single-payload` or `AUTH-expiry`, independent of display order. Reordering does not change identity. Split, merge, or rename IDs only at an explicit revision boundary with a redirect/relation map.

## Evidence and rationale

Preserve concise, durable rationale that prevents future misimplementation. Keep contract-critical rationale repository-native. Tracker discussions may preserve deliberation history but cannot be required for a cold reader.

Evidence movement is non-destructive by default: copy or link, verify destination content, permissions, provenance, and reachability, retain rollback, then retire a duplicate only at a separate gated step. Never delete source material merely because a destination was intended.

## Acceptance and graduation

Design acceptance means the operator accepts the proposed design. It does not mean implementation succeeded. Record implementation and verification separately.

A rule becomes standing authority only after:

1. the design is accepted;
2. the implementation exists;
3. the required verification passes;
4. a post-build review confirms the rule and its destination; and
5. the operator approves graduation.

If no governed destination type, owner, authority, location, version policy, supersession path, and retirement path exist, the rule remains in the verified spec; do not invent an undocumented “standing contract document.”

## Boundaries

- Doctype selection and ADR/DDR/SDD authorship → `author-decision-record`.
- Reusable standards and templates → `author-standard`.
- Executor handoff → `author-execution-relay`.
- Finished implementation review → `code-review`.
- Target implementation conventions → the target's domain skill.
