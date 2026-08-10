---
name: code-review
description: "Review a finished code change, diff, or pull request for correctness, security, performance, conformance, and fit, producing evidence-backed severity findings and a merge verdict. Use for review this PR, is this ready, what is wrong with this change, or a pre-merge self-review. Do not use to author the code, diagnose an unexplained runtime failure (debug), write tests, or review an ADR/DDR/SDD set to convergence (design-review-loop). Apply stack-specific authoring standards only when relevant or explicitly rebound."
---

# Code Review

Review a finished change for whether it should land. Read the diff as evidence, not as the author's intention or completion story.

## Interaction contract

- **Inputs:** finished diff, claimed scope, applicable authorities, and available gate evidence.
- **Output:** a review result conforming to [the result schema](reference/review-result.schema.json), with findings or an explicit no-findings result and a merge verdict.
- **Authority:** recommend disposition; repository protection or the operator performs approval and merge.
- **Capabilities:** a readable diff and applicable authority are required. Independent reviewers, domain overlays, and automated gates are optional and declared.
- **Failure:** pause on unresolved blockers, missing critical evidence, or unavailable required gates.
- **Evidence:** checked surfaces, finding loci, gate dispositions, and the selected risk profile.
- **Lifecycle:** scoped → reviewed → findings resolved or accepted as advisory debt → approved, paused, or superseded.

## Select review depth

- **Lightweight:** narrow, reversible, low-consequence changes. One structured pass may cover scope, correctness, and posture.
- **Standard:** ordinary production changes. Use separate scope/architecture, conformance/correctness, and system-posture lenses in one review record.
- **High-risk:** security, authorization, tenancy, migrations, concurrency, money, destructive operations, infrastructure mutation, or difficult rollback. Use independently produced lenses or a second reviewer and the applicable overlays.

Lead Application Architect (LAA), Solution Architect (SA), and Enterprise Architect (EA) remain useful names for the three lenses, but stance isolation is required only by the selected profile. Structural independence means a clean context or diff-only pass with declared checks—not an unverifiable elapsed-time claim.

## Findings and clean results

A finding separates:

- class and impact;
- likelihood;
- confidence;
- exploitability when security-relevant;
- locus and evidence; and
- whether it blocks this merge.

Impact alone does not determine likelihood or confidence. Advisory and cosmetic disagreement remains visible but does not block unless it encodes an unresolved decision. A clean review is legitimate: emit zero findings plus the specific checked surfaces and gate dispositions. Generic praise is not evidence.

The terminal predicate is mechanical: any unresolved blocking finding or failed required gate means `pause`; otherwise advisory debt may yield `approve-with-advisory`; no blocker yields `approve`.

## Gates and tests

Every potentially relevant gate is `passed`, `failed`, `not-relevant` with a reason, or `unavailable` with escalation. Silent omission is a defect. Test cases are derived from changed behavior, state space, and failure consequences; fixed counts such as “happy path plus two errors” are examples, never universal minima.

## Scope and legacy code

Review the changed behavior and touched boundaries. Inherited defects escalate when they are critical to the change's safe operation, owned by the same boundary, or newly reachable. Bounded unrelated debt is recorded with owner and deadline rather than absorbed silently. “Pre-standard” is not a permanent exemption.

## Domain overlays

Use [the conformance checklist](reference/conformance-checklist.md) to select overlays. Domain skills own their rules; this skill owns coverage, synthesis, finding identity, and disposition. An unavailable cross-cutting security, privacy, compliance, or operational owner is reported as a gap, not silently impersonated.

## Boundaries

Design-record review routes to `design-review-loop`. Authoring and diagnosis route to the owning skill. Review may cite those contracts but does not take over their operation.
