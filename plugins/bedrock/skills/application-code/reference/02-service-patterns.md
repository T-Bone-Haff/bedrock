# Haffey Python service profile: runtime behavior

Framework-specific realization of the portable application-code contract for FastAPI, Pydantic settings, async SQLAlchemy, httpx, and structlog.

## API boundaries

- Prefer HTTP-native success bodies and status codes with typed Pydantic request/response models.
- Use a response envelope only when a named API profile requires it; include its compatibility and generated-client evidence.
- Map domain errors centrally. External errors expose stable codes and safe messages, never `str(exc)` by default.
- Version intentional breaking contracts and publish migration behavior.
- Use cursor/keyset pagination for large or mutating ordered collections. Offset pagination is acceptable only for bounded/stable data with documented consistency and depth limits.
- Generated OpenAPI is a contract artifact; verify representative request, response, error, pagination, and security shapes.

## Concurrency and lifecycle

FastAPI safely runs `def` handlers in a thread pool; therefore handler syntax is not the invariant. Use:

- `async def` when the path awaits non-blocking dependencies;
- `def` for bounded synchronous work that FastAPI may isolate in its worker pool; and
- an explicitly bounded executor/process/durable-job handoff for blocking or CPU-heavy work inside an async call path.

Do not call blocking libraries on the event loop. Propagate cancellation and deadlines, bound task/concurrency counts, and prove shutdown/draining behavior. Construct DB engines and HTTP clients in FastAPI lifespan; dispose/close them on success and startup/shutdown failure paths.

## Configuration

Use `pydantic-settings` with typed fields, validation, and a declared source precedence. Validate required production settings before serving. Avoid import-time settings construction when it prevents test isolation, reload, or controlled startup failure; inject or retrieve a cached immutable instance through lifecycle/dependencies.

Secrets arrive through an approved runtime secret mechanism and are represented with secret-aware types where helpful. Environment variables are a delivery mechanism, not proof that a secret is safely stored, rotated, or absent from process/debug output.

## Logging, tracing, and correlation

Use structured JSON logging with controlled field names and bounded cardinality. At the ASGI boundary:

- accept an external correlation ID only after length/character validation; otherwise replace it;
- retain external correlation separately from internal trace/span identity;
- bind and clear context on success, exception, cancellation, streaming, and disconnect paths; and
- prefer pure ASGI middleware for foundational context propagation. Use `BaseHTTPMiddleware` only when its context and streaming limitations are acceptable and tested.

Log error class/code and safe context. Protected diagnostics require a separately controlled channel, classification, access, and retention policy. Authorization logs record policy/result and surrogate identities, not complete roles/attributes or sensitive claims.

## Errors and audits

Adapters translate dependency failures to owned application/domain errors. Preserve causes internally (`raise ... from exc`) while the API mapper returns a stable safe response.

Audit events are classified:

- required security/regulated events are fail-closed or transactionally coupled through an outbox/durable handoff;
- operational/advisory events may fail open only under a declared policy with metrics and escalation.

“Always swallow audit failure” is prohibited. Audit records inherit the data-classification and log ceilings.

## Health and resilience

`/healthz` performs no dependency I/O. `/readyz` evaluates declared service capability:

- startup-critical failure prevents startup;
- serving-critical failure makes the affected capability unready;
- degradable failure reports degraded behavior without unnecessary eviction; and
- optional failure is observable but does not remove readiness.

Bound checks and avoid amplifying an outage with fan-out or expensive probes.

Outbound calls use a lifespan-managed client and one aggregate budget across attempts, waits, tool/fallback work, and downstream time. Retry only eligible idempotent operations. Prefer a supported propagation standard/profile. A custom deadline/retry header is non-conforming until units, clock basis, trust boundary, decrement rules, intermediary behavior, and multi-hop tests are defined.

## Background work

FastAPI `BackgroundTasks` or tracked `asyncio` tasks are for bounded, observable, loss-tolerant work. Record exception handling, task limit, context propagation, shutdown drain/cancel behavior, and overload response. Anything required to complete uses a durable queue/job system with idempotency, visibility, retry exhaustion, and ownership.

## Performance

Declare workload shape, concurrency, dataset, environment, percentile/window, service objective, resource limits, and error budget before setting thresholds. Measure representative behavior and retain the baseline. Values in examples are illustrative until tied to that declaration.
