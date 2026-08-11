---
name: application-code
description: "Author or conform conventional backend service and application behavior, including API boundaries, concurrency, configuration, logging, errors, resilience, security, data handling, containers, and operational shell code. Use for planned implementation or restructuring. Do not use when an LLM call is central (agent-code), for new tests (testing), observed failures or flakes (debug), finished-diff review, infrastructure, or delivery workflows."
---

# Application Code

Portable authoring rules for conventional backend behavior. The core governs safety and boundary outcomes; a selected profile supplies framework, language, persistence, cloud, and toolchain choices.

## Interaction contract

**Inputs:** the intended behavior; applicable API/data/security contracts; selected stack profile or enough context to select one; operational constraints; and authority to change implementation files.

**Output:** implementation or a scoped conformance plan, with selected profile, applicable capabilities, exceptions/rebinds, and verification evidence stated explicitly.

**Authority:** this skill may author application behavior within the requested scope. It does not authorize production mutation, infrastructure changes, deployment, incident command, or release.

**Stop or escalate when:** the requested behavior conflicts with an owned contract; required security, data, or runtime assumptions are missing; the selected profile cannot satisfy the safety floor; a destructive or production action lacks authorization; or verification cannot support the requested completion claim.

## Portable core

1. **Protect concurrency boundaries.** Do not block an event loop or starve a worker pool. Select synchronous or asynchronous entry points from framework semantics, workload shape, cancellation needs, and dependency behavior—not syntax preference. Bound spawned work and define cancellation and shutdown.
2. **Validate at trust boundaries.** Parse and validate inbound data before domain behavior. Treat correlation identifiers, identity claims, headers, filenames, URLs, serialized objects, and upstream errors as untrusted.
3. **Keep configuration typed and observable.** Separate code constants from environment configuration; validate required settings at startup; keep secrets out of source, logs, errors, responses, images, and generated evidence; define reload behavior rather than assuming it.
4. **Use protocol-native APIs by default.** Preserve HTTP semantics, typed request/response contracts, and generated-client interoperability. An envelope is an opt-in API profile, not a universal wrapper. Version breaking contracts and define pagination consistency.
5. **Preserve layer boundaries proportionally.** Start with the minimum structure that makes dependencies and domain behavior clear. Add ports, adapters, audit, events, or resilience components only when the selected capability profile requires them.
6. **Log structured, classified events.** Validate or replace external correlation values; keep internal trace identity distinct; use bounded-cardinality fields; sanitize exceptions and authorization decisions; never log sensitive payloads merely because a failure occurred.
7. **Translate errors at owned boundaries.** Preserve causal chains internally while returning stable, non-sensitive external errors. Do not swallow required failures or expose raw dependency exceptions.
8. **Make resilience budgets end to end.** Timeouts, deadlines, attempts, backoff, circuit breaking, and concurrency share one request budget. Retry only eligible idempotent operations. A custom propagation field requires units, clock basis, trust validation, decrement semantics, intermediary behavior, and multi-hop non-amplification.
9. **Classify dependency criticality.** Distinguish startup-critical, serving-critical, degradable, and optional dependencies. Liveness reports process health; readiness reports whether the service can provide its declared capability without causing cascading eviction.
10. **Classify data and decisions.** Apply least privilege, tenant/ownership/relationship/attribute checks as required, not RBAC alone. Authentication profiles must define issuer, audience, keys, rotation/revocation, clock handling, service identity, and confused-deputy defenses. Never blindly forward an end-user token.
11. **Separate best-effort from durable work.** In-process background work is bounded, observable, drainable, and loss-tolerant. Required work uses a durable handoff with idempotency, retry exhaustion, and ownership.
12. **Build verifiable artifacts.** Container and dependency profiles declare runtime identity, non-root posture, immutable inputs, vulnerability/license policy, SBOM/provenance expectations, and update ownership. Provisioning and deployment remain sibling concerns.
13. **Derive performance objectives.** Tie latency, throughput, error, and resource thresholds to a declared workload, service objective, measurement window, and error budget. Numeric examples are never universal targets.
14. **Keep shell behavior portable to its declared shell.** Quote data, validate paths, use lifecycle-safe temporary files, preserve exit meaning, avoid interactive blocking, and bound destructive or Git mutation behind explicit authorization.

## Haffey Python service profile

Select this profile for Python 3.11+, FastAPI, Pydantic v2/settings, async SQLAlchemy/asyncpg, GCP, and GitHub. A different stack is a rebind only when no declared profile already covers it.

- Service structure, dependencies, container, and scaffold: [code structure](reference/01-code-structure.md)
- API, concurrency, configuration, logging, errors, resilience, calls, jobs, and performance: [service patterns](reference/02-service-patterns.md)
- Data classification, authentication, authorization, and delegation: [security and data](reference/03-security-and-data.md)
- Bash utility and operational scripts: [shell profile](reference/04-shell-scripts.md)

Profile examples illustrate the selected binding. They cannot widen the portable core, and their executable or illustrative status is declared in `validation/executable-samples.yaml`.

## Routing and handoffs

- Planned production behavior or scaffold configuration → `application-code`.
- New tests, test strategy, fixtures, or planned coverage → `testing`; this skill supplies the implementation contract being tested.
- Any observed failure or flake, including CI-only → `debug`. After diagnosis, an explicitly authorized repair returns here; regression coverage returns to `testing`.
- LLM-centered behavior → `agent-code`; conventional surrounding service behavior may use this profile where compatible.
- Infrastructure desired state or infrastructure plan/apply → `infrastructure-code`; application build/deploy workflow → `app-delivery-pipeline`.
- Finished-change judgment → `code-review`.

No handoff transfers authority silently. State the artifact, evidence, unresolved risk, and requested next operation.
