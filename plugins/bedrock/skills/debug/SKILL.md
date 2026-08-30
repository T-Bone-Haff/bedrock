---
name: debug
description: "Diagnose an observed error, regression, failure, or flake, including CI-only and environment-specific failures. Use to contain active harm, preserve evidence, reproduce when safe, isolate variables, form and falsify hypotheses, identify cause or report insufficient evidence, and verify an authorized repair. Do not use for planned implementation, new tests without an observed failure, generic error-handling guidance, finished-diff review, or incident command."
---

# Debug

A stack-neutral diagnosis contract. Debugging explains observed behavior through evidence and falsification; it does not become generic implementation guidance or incident command.

## Interaction contract

**Inputs:** observed symptom and time window; affected scope; available logs/traces/state/change history; environment and version identity; operational risk; and explicit authorization for any experiment, mitigation, or repair.

**Output:** a diagnosis record conforming to [the schema](reference/diagnosis-record.schema.json), completed from [the template](templates/diagnosis-record.md). The record may conclude `root_cause_identified`, `contributing_factors_only`, or `insufficient_evidence`.

**Authority:** read-only diagnosis is the default. This skill may propose experiments, containment, mitigation, and fixes. It performs a mutation only when that specific action is authorized and bounded. Incident severity, communications, business decisions, release, and residual-risk acceptance belong to their owners.

## 1. Choose the operating mode

- **Active harm:** contain blast radius, preserve evidence, communicate the technical state to incident ownership, and prefer reversible restoration before deeper diagnosis when delay increases harm.
- **Offline diagnosis:** preserve the relevant baseline, then investigate before remediation.

Containment is not a root-cause claim. Restoration, causal diagnosis, and permanent correction are separate outcomes with separate evidence and owners.

## 2. Preserve evidence before mutation

Capture the minimum sufficient logs, traces, dumps, state snapshots, configuration/version identity, recent changes, and timeline. Record source, capture time and clock basis, digest or other integrity signal where consequential, classification, redaction, access, retention, and custody. Do not collect sensitive content by default or move it into an uncontrolled record.

## 3. Reproduce when safe and feasible

A reliable minimal reproduction is preferred because it becomes the falsification instrument and regression test. Reproduction is not an absolute precondition: one-off corruption, races, hardware faults, security events, and production-only failures may require diagnosis from preserved state, timelines, traces, comparisons, and bounded inference. Never invent a reproduction or claim certainty beyond the evidence.

## 4. Isolate by failure shape

Select the least invasive technique that can distinguish candidates: minimal reproduction, binary search/bisection, recent-change analysis, environment/config/version diff, input minimization, dependency substitution, concurrency scheduling, fault injection, or observability comparison. State why the technique fits and what it cannot distinguish.

## 5. Establish that the reading is about the claim subject

Every observation arrives through an instrument whose transport, wrapper, vantage, execution environment, configuration, or normalisation can manufacture the watched result. Before an observation enters the hypothesis loop or supports closure, name the claim subject and ask whether the same instrument could have produced the same output if that subject were different. If the answer is yes or unavailable, the measurement is unavailable; do not treat it as evidence that the subject failed.

Use a discrimination control shaped differently from the reading where possible:

- test a known-good comparable before believing an absence;
- run a contrary or known-dirty case beside a mechanism whose success is silence;
- derive the expected value where the subject lives;
- use the owning parser, API, or schema, including its configuration and normalisation; or
- widen the scope enough to represent “nothing happened.”

Carry the control in the same run when practical. Test identity, not mere liveness or status: a control that answers the same way for the subject and contrary case falsifies the instrument. Record that outcome as unavailable evidence, not as a subject failure.

Do not prescribe corrective action from an unavailable reading. When a false failure would authorize changing a healthy subject, require stronger discrimination before acting.

These are diagnosis-time rules. Standard proving, relay-premise controls, and reviewer structural measurement remain owned by `author-standard`, `author-execution-relay`, and `design-review-loop`; cite them rather than restating their contracts.

## 6. Run the hypothesis loop

For each numbered iteration record:

1. hypothesis;
2. checkable prediction;
3. falsifier;
4. experiment or observation;
5. evidence obtained;
6. disposition: supported, falsified, or unresolved; and
7. unexplained evidence.

Seek falsification, not confirmation. A hypothesis that leaves material evidence unexplained is incomplete. Confidence is `low`, `medium`, or `high` and must follow the evidence, not fluency.

## 7. Bound experiments

Before any probe that writes, loads, exposes data, or affects customers, record authorization, blast radius, protected-data treatment, observability, rollback, time/resource budget, and stop conditions. Prefer read-only and lower-environment probes. Stop immediately on unexpected harm, lost observability, exceeded budget, invalid rollback, privacy boundary breach, or scope expansion.

## 8. Decide cause and action honestly

Name a root cause only when the evidence and falsification record distinguish it from viable alternatives. Otherwise report contributing factors or insufficient evidence and hand off what would resolve the uncertainty.

A verified cause does not authorize a fix. Request or cite repair authorization, then hand implementation to the owning domain skill. A temporary mitigation records residual risk, owner, expiry/rollback, and root-cause follow-up.

## 9. Verify and close

Closure requires evidence proportionate to where the failure existed:

- local reproducer or regression test;
- relevant deterministic suite;
- environment/deployment or canary evidence when applicable;
- an observation window tied to the prior recurrence pattern; and
- assessment of recurrence, adjacent failure modes, rollback, and residual risk.

A local green alone cannot close a production or CI-only defect. If the required environment was unavailable, the record stays open or explicitly incomplete.

## Stop and escalation states

Stop without guessing when evidence is insufficient, the time/risk budget is exhausted, specialist access is required, the next experiment exceeds authority, safety cannot be preserved, or competing causes remain materially indistinguishable. The handoff carries symptom, scope, timeline, evidence locations/classification, attempts, hypotheses/falsifiers, current confidence, containment, unresolved questions, and the exact capability or decision needed.

## Routing boundary

Every existing failure or flake routes here first. Planned test authoring remains `testing`. Planned implementation remains the domain authoring skill. After diagnosis, authorized production repair routes to that domain skill and regression coverage routes to `testing`. Incident coordination remains external.
