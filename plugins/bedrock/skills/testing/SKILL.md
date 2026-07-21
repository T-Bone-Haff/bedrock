---
name: testing
description: House testing discipline for Python service code — test-driven-development sequence, unit/integration/contract/e2e tests, mocking, fixtures, coverage, and test isolation. Use whenever writing tests, deciding how to test something, adding a test for new behavior, or setting a service's test discipline: "write tests for X", "how should I test this", "what's the coverage requirement", "test this endpoint", or any time you're implementing behavior that should be specified test-first. Assumes pytest on a Python/FastAPI/async stack; on a different stack, treat the conventions as a rebind. Writing the code under test is the application-code skill — this skill is about specifying and verifying its behavior with tests.
---

# Testing

How service behavior is specified and verified with tests. This SKILL.md carries the test-driven sequence and the invariants that hold for every test; load the reference for worked patterns (layout, mocking, fixtures, contract/integration/container/e2e).

## Stack binding (read once)

These conventions are written against **pytest** on the Python/FastAPI/async stack (`pytest`, `pytest-asyncio`, `pytest-cov`, `respx`, `testcontainers`, `httpx`). They're portable across projects on that stack; a different language or test framework is a **rebind** — re-derive the equivalents, don't line-edit.

## The TDD sequence

Code that implements behavior is preceded by a test that specifies its contract:

1. **Write the failing test** against the intended interface.
2. **Run it and observe a *meaningful* red** — a real assertion failure that exercises the contract (e.g. "expected 200, got 501"; "expected `ItemNotFoundError`, none raised"), or a not-yet-implemented error raised by the *target* under a behavioral assertion. A syntax/import/collection error is **not** a meaningful red — it means the test couldn't run yet; fix until it executes its assertion, then observe the red.
3. **Implement the minimum** to go green.
4. **Refactor** while keeping green.
5. **Confirm coverage** holds (§ below).

Why the observed red matters: writing tests *alongside* the code and running them green without ever seeing them fail proves nothing — the red is what proves the test specifies behavior the code doesn't yet have. Capture it (the failing-test runner output in the commit message, or an explicit note when test and implementation land atomically). The reference has the full meaningful-vs-not-meaningful breakdown.

**What counts as behavior** (so is test-first): anything with conditional logic, iteration, non-trivial call chains, or external effects — including in-memory adapters, migration scripts, seed loaders, utilities. **Exempt:** empty stubs, type stubs / re-exports, config-only files, fixture data, docs. **Refactors and bug-fixes** don't need a *new* failing test for the refactor itself — but a bug fix needs a reproducing test that fails before the fix lands.

## Always-apply invariants

1. **Coverage floor is 90% line coverage, enforced in CI** — and you don't game it. The omit list holds only files that are entirely real-infrastructure with no testable logic; in-memory/test-friendly adapters are testable and are **never** omitted.
2. **Unit tests mock all external dependencies** (DB, HTTP, brokers) — no real network or DB connections in unit tests. Mocks assert they were called as expected.
3. **AAA structure** (Arrange-Act-Assert) with section comments, and the module comment block on every test file.
4. **Naming:** `test_<unit>_<scenario>_<expected>` — e.g. `test_get_item_by_id_when_item_not_found_raises_not_found_error`.
5. **Test isolation:** no test depends on state left by another. Use transaction rollback or fresh fixtures.
6. **Service-layer tests use the in-memory adapter, not a mocked port** — it preserves the contract the port enforces (the in-memory adapter is part of the application-code layout).
7. **Disable telemetry export in the test environment before any app import**, by direct assignment — not `setdefault`-style conditional patterns, which a parent-env value silently defeats.
8. **Every endpoint has a contract test** asserting request/response shape under representative inputs; the typed models are the source of truth.
9. **Mechanical gates get deterministic tests; judgments get eval harnesses.** An LLM in the system exempts nothing around it from this sequence — the deterministic machinery (parsers, gates, routers, verifiers) is TDD'd and covered as always; the judgment steps themselves are evaluated per `reference/nondeterministic-components.md`.

## Where to look

Load `reference/test-authoring.md` for the worked patterns: the test-tree layout; the full test-first meaningful-failure rules; coverage and omit discipline; AAA with a worked example; mocking and shared fixtures (`conftest.py`); contract tests (`respx`); integration tests (`httpx.AsyncClient`); containerized dependencies (`testcontainers`); isolation via transaction rollback; and e2e.

Load `reference/nondeterministic-components.md` when the code under test embeds LLM judgment: the gates-vs-judgments split, recorded-fixture regression, LLM-as-judge with cold calibration, and what meaningful-red means for a judgment.

## Boundary with application-code

The **`pyproject.toml` toolchain config** — the `pytest-cov` gate, `asyncio_mode`, the coverage threshold line — lives in the `application-code` skill, because standing it up is part of scaffolding a service. **This skill owns writing the tests and the coverage *discipline*** (what gets measured, the no-omit-cheating rule, the test kinds). If you're scaffolding the harness, that's application-code; if you're writing or shaping tests, you're here.

**Frontend testing** → the `frontend-code` skill's testing reference — the vitest/Testing Library rebind of this discipline for the TypeScript/React stack; this skill's pytest binding does not gate frontend test work.
