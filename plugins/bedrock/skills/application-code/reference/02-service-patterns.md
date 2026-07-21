# Reference: Service Patterns

How a service *behaves* at runtime — API design, async discipline, configuration, logging and observability, error handling, resilience, inter-service communication, caching, and background work. Load this when building endpoints or wiring a service's runtime behavior.

## Contents

- [1. API design](#1-api-design)
- [2. Async patterns](#2-async-patterns)
- [3. Configuration](#3-configuration)
- [4. Logging and observability](#4-logging-and-observability)
- [5. Error handling](#5-error-handling)
- [6. Resilience and reliability](#6-resilience-and-reliability)
- [7. Inter-service communication](#7-inter-service-communication)
- [8. Caching](#8-caching)
- [9. Background jobs](#9-background-jobs)
- [10. Performance](#10-performance)

---

## 1. API design

**RESTful conventions.** Resources are nouns (`/items/`); HTTP verbs match semantics; identifiers in the path (`/items/{item_id}`); filters and pagination in the query string.

**Versioning.** Version HTTP APIs via URL path prefix (`/api/v1/`). A breaking API change is a new prefix.

```python
router = APIRouter(prefix="/api/v1/items", tags=["items"])
```

**Pagination.** List endpoints paginate via `limit`/`offset` (default limit 50, max 200); override per-endpoint with documented rationale.

```python
@router.get("/")
async def list_items(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
) -> ApiResponse[list[ItemResponse]]: ...
```

**Response envelope.** Successful responses wrap in a generic `ApiResponse`:

```python
T = TypeVar("T")

class ApiResponse(BaseModel, Generic[T]):
    success: bool = True
    data: T
    correlation_id: str | None = None
```

**Error envelope.** Errors wrap in `ErrorResponse`. The five-term `FaultClass` enum is the authoritative interface for retry decisions (see §6).

```python
class FaultClass(str, Enum):
    TRANSIENT = "transient"
    PERMANENT = "permanent"
    UPSTREAM = "upstream"
    TIMEOUT = "timeout"
    AUTH = "auth"

class ErrorResponse(BaseModel):
    success: bool = False
    error_code: str
    message: str
    detail: str | None = None
    correlation_id: str | None = None
    fault_class: FaultClass | None = None
```

`fault_class` is required on inter-service error responses, optional on external-facing ones.

**Exception mapping.** Map domain exceptions to HTTP responses via FastAPI exception handlers at `app/main.py` — don't scatter status codes through route handlers. Direct `raise HTTPException(...)` is fine for HTTP-protocol concerns (auth, validation); service-layer exceptions surface through the handler mapping.

```python
@app.exception_handler(ItemNotFoundError)
async def handle_item_not_found(request: Request, exc: ItemNotFoundError) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content=ErrorResponse(
            error_code="ITEM_NOT_FOUND",
            message=str(exc),
            correlation_id=request.state.correlation_id,
        ).model_dump(),
    )
```

**OpenAPI.** Every endpoint declares `summary`, `description`, `response_model`, and a `responses` dict covering error codes. The generated OpenAPI spec at `/openapi.json` is the canonical API documentation; Swagger/ReDoc at `/docs` is exposed in non-production and gated by an `enable_docs` Settings field in production.

---

## 2. Async patterns

**Async-first.** All HTTP handlers are `async def`. Synchronous handlers block the event loop and are prohibited; so are synchronous library calls inside async handlers (use the async equivalent, or `run_in_executor`).

```python
# Correct
async def fetch_data(client: httpx.AsyncClient) -> dict:
    response = await client.get("https://example.com/data")
    return response.json()

# Prohibited — blocks the event loop
async def fetch_data() -> dict:
    response = requests.get("https://example.com/data")
    return response.json()
```

**In-process background work.** Use FastAPI `BackgroundTasks` for fire-and-forget tied to the request; `asyncio.create_task()` for work decoupled from it. Assign `create_task()` results to a surviving variable or tracking set so the task isn't garbage-collected mid-flight. For durable retriable work, see §9.

**Database sessions** are per-request via a FastAPI dependency; the engine instantiates once per process. The `async with` context manager prevents session leaks.

```python
engine = create_async_engine(settings.database_url, pool_size=10, max_overflow=5, pool_timeout=30)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
```

**Outbound HTTP** flows through a canonical `ServiceClient` (see §7) — never per-call `httpx.AsyncClient` instances.

**Event publishing** uses a canonical `event_publisher.publish()` with `<noun>.<verb>` event types (`item.created`) and an explicit `event_version` for schema versioning.

---

## 3. Configuration

**Settings class.** Configuration comes from a `pydantic-settings` `Settings` class — not scattered `os.environ` reads or module constants.

```python
class Settings(BaseSettings):
    service_name: str
    service_version: str
    app_env: str = Field(default="development")
    database_url: str
    jwt_public_key: str
    jwt_audience: str
    enable_docs: bool = Field(default=False)
    log_level: str = Field(default="INFO")
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

@lru_cache
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
```

`@lru_cache` memoizes the instance; module-level `settings = get_settings()` is fine for convenience but must not be mutated post-import.

**Secrets** come from environment variables, never from committed config. Production sources them from a secret manager surfaced as env vars; local dev uses a gitignored `.env` with a committed `.env.example` schema. **Secrets MUST NOT appear in source, logs, error messages, or API responses.**

**Service URLs** in Settings use FQDN form and `https://` between services in production.

---

## 4. Logging and observability

**Structured logging** uses `structlog` with JSON output. `print()` and bare stdlib `logging` are prohibited for application logging.

```python
log = structlog.get_logger()
log.info("item_created", item_id=item.id, owner_id=item.owner_id)
```

**Levels:** DEBUG (diagnostic, off in prod) · INFO (operational events) · WARNING (recoverable anomalies) · ERROR (operational failures) · CRITICAL (outages needing on-call).

**Correlation ID middleware** registered first in the stack mints or accepts an `X-Correlation-ID`, binds it to structlog context (so it appears in every subsequent log line), and echoes it on the response. Outbound calls forward it.

```python
class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        cid = request.headers.get("X-Correlation-ID") or str(uuid.uuid4())
        structlog.contextvars.bind_contextvars(correlation_id=cid)
        request.state.correlation_id = cid
        response = await call_next(request)
        response.headers["X-Correlation-ID"] = cid
        return response
```

**Prohibited log content (MUST NOT appear at any level):** credentials of any kind; full PII (name, email, phone, address, gov ID, financial account); full payment data; full health data; any Tier 3/Tier 4 data (see the security-and-data reference). Log surrogate identifiers (UUIDs) instead.

**Audit logging.** Audit-significant events (data mutations, security events, authorization decisions) emit via a dedicated `emit_audit()` on a separate `audit` log channel with its own retention. Audit writes are wrapped in try/except so an audit failure never fails the business operation. The audit `detail` field obeys the same prohibited-content rule.

```python
class AuditAction(str, Enum):
    AUTH_SUCCESS = "auth_success"
    AUTHZ_DENIED = "authz_denied"
    DATA_CREATE = "data_create"
    DATA_UPDATE = "data_update"
    DATA_DELETE = "data_delete"
    SECURITY_EVENT = "security_event"

def emit_audit(action, actor_id, resource_type, resource_id, correlation_id, outcome="success", **detail) -> None:
    record = AuditRecord(action=action, actor_id=actor_id, resource_type=resource_type,
                         resource_id=resource_id, correlation_id=correlation_id,
                         outcome=outcome, detail=detail)
    structlog.get_logger("audit").info("audit", **record.model_dump())
```

**Tracing and metrics.** Instrument with OpenTelemetry auto-instrumentation (FastAPI, httpx, SQLAlchemy) in lifespan — overhead is negligible and retrofitting is costly. Instrument `http_requests_total{method, endpoint, status_code}` and `http_request_duration_seconds{method, endpoint}` with `prometheus_client`, plus domain-specific business metrics; expose `/metrics`.

---

## 5. Error handling

**Domain exception hierarchy** with `DomainError` as the base, in `app/domain/exceptions.py`:

```python
class DomainError(Exception):
    """Base for domain-layer exceptions."""

class ItemNotFoundError(DomainError):
    """Raised when an item is requested but does not exist."""
```

**Layer-boundary propagation.** Adapters catch infrastructure exceptions (`SQLAlchemyError`, `httpx.HTTPError`) and translate them to domain exceptions *before* crossing the port boundary. The service layer raises and propagates domain exceptions. The API layer catches them via exception handlers and returns `ErrorResponse`. Silent swallowing across boundaries is prohibited; catch-log-continue is acceptable only when the exception is genuinely non-fatal to the operation.

---

## 6. Resilience and reliability

**Health checks.** Every service exposes `GET /healthz` (liveness — process alive, no I/O) and `GET /readyz` (readiness — every dependency checked) at the root path, not under `/api/v1`.

```python
@router.get("/healthz", response_model=HealthResponse, tags=["health"])
async def liveness() -> HealthResponse:
    return HealthResponse(status="ok", service=settings.service_name, version=settings.service_version)

@router.get("/readyz", response_model=ReadinessResponse, tags=["health"])
async def readiness(db: AsyncSession = Depends(get_db)) -> JSONResponse:
    checks, healthy = {}, True
    try:
        await db.execute(text("SELECT 1"))
        checks["database"] = "ok"
    except Exception as exc:
        log.error("readiness_db_check_failed", exc=str(exc))
        checks["database"] = "unavailable"
        healthy = False
    return JSONResponse(
        content=ReadinessResponse(status="ok" if healthy else "degraded", checks=checks).model_dump(),
        status_code=200 if healthy else 503,
    )
```

Multi-dependency readiness: each dependency checked in its own try/except (one failure doesn't short-circuit the rest), each with a bounded timeout (`asyncio.wait_for` or driver timeout), all-or-nothing (any failure → 503).

**Circuit breakers and retries.** Outbound calls carry a circuit breaker (open after a failure threshold, recover after a timeout) and bounded exponential-backoff retry on transient failures only. Both ride on the `ServiceClient` (§7).

**Retry budget and deadline propagation.** Inter-service calls forward a global retry budget (`X-Retry-Budget`) and a deadline (`X-Deadline-Ms`) so retries don't amplify across a call chain and work stops when the caller's deadline passes.

**Fault classification.** Consumers branch on the `FaultClass` enum (§1) to decide retry eligibility and propagation — never on HTTP status code alone.

**Statelessness.** Services hold no cross-request in-process state (no module-level dict mutated across requests). Process-lifetime memoization of immutable configuration (`@lru_cache` on the Settings factory — fixed at startup, never mutated across requests) is fine; cross-request in-process caching of mutable data is prohibited.

---

## 7. Inter-service communication

**Synchronous** calls flow through a canonical `ServiceClient` that integrates retry, retry-budget, deadline, circuit breaker, correlation-ID forwarding, and auth. Bypassing it loses all of those.

```python
class ServiceClient:
    def __init__(self, base_url: str, default_timeout: httpx.Timeout):
        self.client = httpx.AsyncClient(
            base_url=base_url, timeout=default_timeout,
            limits=httpx.Limits(max_connections=20, max_keepalive_connections=10),
        )

    @circuit(failure_threshold=5, recovery_timeout=30)
    @retry(stop=stop_after_attempt(3),
           wait=wait_exponential(multiplier=1, min=1, max=10),
           retry=retry_if_exception_type((httpx.ConnectError, httpx.TimeoutException)))
    async def request(self, method: str, path: str, **kwargs) -> httpx.Response:
        # forward correlation_id, retry budget, deadline headers
        ...
```

Construct `ServiceClient` instances at lifespan; per-call `httpx.AsyncClient` is prohibited.

**Synchronous vs event-driven** is an architectural choice, not a stylistic one. Use synchronous when the caller needs the callee's response to complete its own and latency allows. Use events when it's a notification/broadcast, the caller can proceed without waiting, or coupling should be loose. Picking wrong creates either tight coupling and cascading failure or needless complexity.

**Event consumers** must be idempotent (brokers deliver at-least-once), route exhausted-retry failures to a dead-letter queue, tolerate schema-version drift (handle known `event_version`s, DLQ the rest), and audit-log state-mutating consumption with the originating `correlation_id`. Event types come from a central registry, not invented per-service.

---

## 8. Caching

Caching trades consistency complexity for latency. Adopt it when the benefit demonstrably exceeds the cost — not as a default.

**Appropriate when:** read-heavy with high hit ratios; latency/load pressure is measurable against budgets; the data has a bounded freshness tolerance; the cached set is size-bounded. **Inappropriate when:** writes rival reads (thrash); zero staleness tolerance; the data is Tier 3/4 and the cache lacks equivalent encryption-at-rest; cold-starts dominate.

**Every cached value has an explicit invalidation rule** — TTL, write-through, or event-driven. Mixing patterns in one cache layer is the most common caching bug; don't, without a documented reason. Cached data inherits its source's classification tier.

---

## 9. Background jobs

Two patterns, split by durability:

**In-process** (`BackgroundTasks`, `asyncio.create_task`) — for short-lived, bounded-blast-radius, loss-tolerant work tied loosely to the request.

**Durable** (message-queue-backed) — for work that must complete regardless of the originating process, be retried with backoff and exhaustion semantics, run long, or be visible across services. The broker infrastructure itself is environment-specific; the consumer discipline (idempotency, DLQ, schema tolerance — §7) is not.

---

## 10. Performance

Default budgets (override per-service with documented rationale):

| Metric | Target |
|---|---|
| p50 read | ≤ 100 ms |
| p95 read | ≤ 500 ms |
| p50 write | ≤ 200 ms |
| p95 write | ≤ 1000 ms |
| 5xx rate (normal load) | < 0.1% |

The §4 request metrics are the measurement surface. Profile under representative load (`py-spy`, `cProfile`, `pyinstrument`) after changes to data-access or core request paths.
