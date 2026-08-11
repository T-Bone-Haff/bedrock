---
name: testing
description: "Author new tests, test strategy, fixtures, and planned coverage. Use for test-first specification of new or changed behavior, risk-based test selection, isolation, contract testing, coverage design, and deterministic or nondeterministic evaluation. Do not use to diagnose any observed failing or flaky test, including CI-only flakes (debug), to implement production behavior, or to review a finished diff. Select a stack profile; a materially different unprofiled test stack is a rebind."
---

# Testing

Portable discipline for specifying planned behavior and evaluating whether it holds. A test-stack profile supplies framework syntax and fixtures; the core owns evidence quality, isolation, and honest gate claims.

## Interaction contract

**Inputs:** the behavior or risk to test; its owning contract; selected test profile; applicable environments; determinism classification; and the decision the evidence will gate.

**Output:** tests and/or a schema-valid strategy stating test level, doubles, isolation, coverage rationale, gate status, evidence retention, and limitations.

**Authority:** this skill may author tests and testing strategy. It does not diagnose an already observed failure, change production behavior, quarantine a flake without the declared owner/expiry contract, or authorize promotion.

**Stop or hand off:** an existing failure or intermittent result routes to `debug`; a specification conflict is triaged as implementation defect, specification defect, or intentional versioned break; missing environment or capability evidence produces an explicit unverified result.

## Test-first workflow

1. Express the intended observable contract in a test.
2. Run it before implementation and observe a meaningful failure at the target boundary. Collection/import defects are harness failures, not a meaningful red.
3. Implement the minimum behavior under the owning authoring skill.
4. Refactor while the contract remains green.
5. Run the applicable risk-selected suite and coverage gates.

Meaningful-red is a workflow discipline, not mandatory Git-history narration. Durable evidence is the retained regression test plus an inspectable demonstration of the failure mode when the change warrants it. A bug report already containing an observed failure routes through `debug`; its reproducer becomes regression coverage after diagnosis.

## Test taxonomy and doubles

- **Unit:** one behavioral unit, no real network/process/database. Prefer fakes or in-memory adapters for state/behavior contracts; use mocks when the interaction itself is the contract.
- **Integration:** real boundaries inside a controlled environment, including application lifecycle, serialization, persistence, or broker behavior.
- **Contract:** versioned consumer and provider artifacts, publication, ownership, compatibility verification, and migration behavior—not merely a mocked HTTP response.
- **End to end:** a declared user/system path in a named environment. Each suite explicitly states whether it blocks merge, deployment, promotion, or nothing.
- **Evaluation:** a versioned instrument for nondeterministic judgment, with dataset/model/prompt/judge identity, sampling, uncertainty, contamination controls, drift, and budget.

Assert observable state and behavior by default. Interaction assertions are appropriate only when calls, ordering, attempts, or non-occurrence are themselves the contract. A safe refactor that preserves behavior should not require mock choreography changes.

## Isolation and fixtures

- No test consumes state left by another. Control clocks, randomness, locale, environment, concurrency, and identifiers where they affect outcomes.
- Lifecycle-aware application fixtures must execute startup and shutdown and prove cleanup on success and failure.
- Database isolation must cover connections opened by the application, multiple requests, failures, and parallel workers; a transaction on a test-only session is insufficient.
- External services are replaced or containerized according to test level. Test doubles declare what they simulate and what they cannot prove.
- Telemetry export is disabled before application import in the Haffey profile; other profiles provide their equivalent.

## Coverage and risk

Coverage is a signal, not proof. Each strategy declares justified line and branch thresholds, critical paths/states, allowed exclusions, and any mutation-quality requirement. Equal line coverage may yield different gates when branch, state, mutation, or risk coverage differs. Never exclude testable code merely to pass.

Select advanced methods by risk: property-based, fuzz, mutation, concurrency, migration, performance/load, security, fault-injection, and chaos testing each require an applicability decision and an explicit `not_applicable` rationale when considered but omitted.

## Flakes and quarantine

An observed flake routes immediately to `debug`. Retries may gather evidence or protect a bounded gate only when capped and visible; they do not turn a flake green. Quarantine requires an owner, issue, scope, entry evidence, expiry, restoration criteria, and escalation when the maximum duration is reached.

## Profiles and references

- [Haffey pytest/FastAPI profile](reference/test-authoring.md): pytest layout, lifespan, persistence, contract, container, and E2E patterns.
- [Nondeterministic evaluation contract](reference/nondeterministic-components.md): deterministic-mechanism/evaluation split and statistical evidence.
- Machine-readable output: [test strategy schema](reference/test-strategy.schema.json).

Clear naming and structure are required; module revision headers and mandatory Arrange/Act/Assert comments are not.

## Routing boundary

Planned tests and strategy stay here. Observed failures/flakes route to `debug`, even if the requested wording says “use testing.” Production implementation routes to its domain skill. A finished test diff routes to `code-review` for review.
