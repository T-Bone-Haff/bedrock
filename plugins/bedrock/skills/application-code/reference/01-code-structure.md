# Reference: Code Structure

The *shape* of a service — language, layout, layering, dependencies, types, and the project scaffold. Load this when scaffolding a new service or deciding where code goes and how layers may depend on each other.

## Contents

- [1. Language and framework](#1-language-and-framework)
- [2. Repository layout and layering](#2-repository-layout-and-layering)
- [3. Naming conventions](#3-naming-conventions)
- [4. Module comment block](#4-module-comment-block)
- [5. Docstrings, constants, linting, types](#5-docstrings-constants-linting-types)
- [6. Dependency management](#6-dependency-management)
- [7. Port/adapter architecture](#7-portadapter-architecture)
- [8. Persistence — models, migrations, repositories](#8-persistence--models-migrations-repositories)
- [9. Container and build](#9-container-and-build)
- [10. Project scaffold and toolchain](#10-project-scaffold-and-toolchain)

---

## 1. Language and framework

**Python 3.11+** is the language for services; target 3.11 or later.

**FastAPI** (>= 0.110.0) is the web framework for HTTP services. Use the `lifespan` context manager for startup/shutdown — not the deprecated `@app.on_event` decorators.

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: initialize resources (DB pools, HTTP clients, brokers)
    yield
    # Shutdown: dispose resources gracefully

app = FastAPI(lifespan=lifespan)
```

**Approved libraries** (minimum-version floors; re-check currency when you adopt). Reaching outside this set is a deliberate choice worth recording.

| Category | Library | Floor |
|---|---|---|
| Web framework | fastapi | 0.110.0 |
| ASGI server | uvicorn[standard] | 0.27.0 |
| Validation | pydantic (v2 idioms only) | 2.6.0 |
| Settings | pydantic-settings | 2.2.0 |
| HTTP client | httpx (async) | 0.26.0 |
| Retry | tenacity | 8.2.0 |
| Circuit breaker | circuitbreaker | 2.0.0 |
| ORM | sqlalchemy (async, v2) | 2.0.0 |
| Postgres driver | asyncpg | 0.29.0 |
| Migrations | alembic | 1.13.0 |
| Logging | structlog | 24.1.0 |
| Tracing | opentelemetry-api/sdk + fastapi/httpx/sqlalchemy instrumentation | 1.23.0 |
| Metrics | prometheus-client | 0.20.0 |
| Auth | pyjwt (RS256 only) | 2.8.0 |
| Test | pytest, pytest-asyncio, pytest-cov, respx, testcontainers | — |
| Lint/format | ruff | 0.4.0 |
| Types | mypy | 1.9.0 |
| Security | bandit, pip-audit, cyclonedx-bom | — |

---

## 2. Repository layout and layering

Code follows a layered, dependency-directional structure:

```
api/ → services/ → ports/ → adapters/
            ↓
         domain/ ← models/
```

| Layer | May import | May NOT import |
|---|---|---|
| `api/` (route handlers) | `services/`, `models/` | `adapters/`, `repositories/`, `domain/` (except types) |
| `services/` (business logic) | `ports/`, `domain/`, `models/` | `adapters/`, `repositories/`, `api/` |
| `ports/` (abstract interfaces — `Protocol`/`ABC`) | `domain/` | `adapters/`, `services/`, `api/` |
| `adapters/` (port implementations) | `ports/`, external libs | `services/`, `api/` |
| `domain/` (types, exceptions — lowest layer) | stdlib, Pydantic | everything else |
| `models/` (Pydantic request/response) | `domain/` (types) | `services/`, `adapters/`, `api/` |

A route handler importing from `adapters/` is a layering violation. The direction is the rule.

**Adapter placement.** In-memory test doubles live in their own `app/adapters/in_memory/` directory, mirroring the production adapter's filename (production `app/adapters/postgres/item_repository.py`, in-memory `app/adapters/in_memory/item_repository.py`). Service-layer tests use the in-memory adapter rather than mocking the port directly — this preserves the contract the port enforces.

---

## 3. Naming conventions

- **Modules/packages:** lowercase_with_underscores (`item_service.py`, `audit_log/`)
- **Classes:** PascalCase (`ItemService`, `AuditRecord`)
- **Functions/methods:** lowercase_with_underscores (`get_by_id`, `emit_audit`)
- **Constants:** UPPERCASE_WITH_UNDERSCORES (`DEFAULT_TIMEOUT`)
- **API request models:** end in `Request` (`ItemCreateRequest`); responses end in `Response`; error envelopes end in `ErrorResponse`
- **Domain exceptions:** end in `Error` (`ItemNotFoundError`)

Examples and templates use placeholder names (`Item`, `item_*`, `<service-name>`); real services replace them with domain-specific names.

---

## 4. Module comment block

Every Python module begins with a comment block, positioned immediately after any module-level docstring:

```python
##############################################################################
# Module: <filename.py>
# Service: <service-name>
# Author: <author or team>
# Created: YYYY-MM-DD
# Revised: YYYY-MM-DD
# Description: <one-paragraph description of module purpose and responsibility>
##############################################################################
```

The `# Revised:` line carries a bare date — no parenthetical ticket. Application-code edits are high-frequency and low-decision-density, so the per-edit stamp stays light. Test modules follow the same discipline; the `Description:` names what the test covers.

---

## 5. Docstrings, constants, linting, types

**Docstrings.** Public functions, methods, and classes carry Google-format docstrings. Private helpers (`_`-prefixed) may omit them when name and signature are self-explanatory; substantive private helpers should still have them.

```python
def calculate_total(items: list[Item], discount: float = 0.0) -> Decimal:
    """Calculate the total cost of items with an optional discount.

    Args:
        items: List of items to total.
        discount: Discount fraction (0.0 to 1.0). Defaults to no discount.

    Returns:
        Total cost as Decimal, rounded to 2 decimal places.

    Raises:
        ValueError: If discount is outside the valid range.
    """
```

**Constants vs config.** Module-level constants are for type vocabularies (`HTTP_RETRY_STATUSES = {502, 503, 504}`), domain/math constants (`SECONDS_PER_DAY = 86400`), and enums. Environment-specific values (URLs, credentials, flags) come from Settings (see the service-patterns reference), never module constants.

**Linting.** Code passes `ruff check` and `ruff format --check`. Minimum rule sets: `E`, `F`, `W`, `I`, `B`, `C4`, `UP`, `RUF`.

**Types.** Every function signature carries complete annotations.

```python
# Complete
async def fetch_items(filter: ItemFilter | None = None) -> list[Item]: ...

# Incomplete — not acceptable
def fetch_items(filter=None): ...
```

`Any` is permitted only with a comment explaining why a more specific type can't be expressed. `# type: ignore` requires a comment naming the upstream typing limitation. `mypy --strict` is the canonical checker and a hard CI gate.

---

## 6. Dependency management

**Lockfiles.** Generate hash-pinned `requirements.txt` / `requirements-dev.txt` from `.in` sources with pip-tools (or equivalent):

```bash
pip-compile --generate-hashes requirements.in -o requirements.txt
```

Ad-hoc `pip freeze > requirements.txt` is prohibited — it carries no hash pins.

**Hash-verified install.** Production installs use `pip install --require-hashes -r requirements.txt`. The flag rejects any package whose content hash doesn't match the lockfile, blocking supply-chain substitution. Dev dependencies may pin more loosely.

**Vulnerability scanning.** Run `pip-audit` in CI to surface known CVEs in dependencies.

**Updates.** Review updates regularly. A major-version bump to a core library is a migration worth documenting before you take it.

---

## 7. Port/adapter architecture

A service exposes its capabilities through ports (abstract interfaces) implemented by adapters (concrete bindings to infrastructure). Service-layer logic depends only on ports, never on adapters — this is what makes the in-memory test double (§2) a drop-in substitute for the production adapter.

- **Port** — a `Protocol` or `ABC` in `ports/` describing the contract the service depends on (e.g., `ItemRepository` with `find_by_id`, `save`).
- **Adapter** — an implementation in `adapters/<backend>/` (e.g., `adapters/postgres/item_repository.py`) binding the port to a real backend.
- **Wiring** — adapters are constructed at lifespan/startup and injected via FastAPI dependencies; the service never imports a concrete adapter.

The payoff: swapping Postgres for another store, or a real backend for an in-memory test double, touches only the adapter layer and the wiring — never the service logic.

---

## 8. Persistence — models, migrations, repositories

Persistence is an **adapter-layer concern**. ORM models, the Alembic environment, and the repository implementation live under `app/adapters/postgres/` (or whatever the backend is) — never in `domain/` or `models/`. The service layer depends only on the port (§7); it never sees an ORM object. This is the rule that keeps the in-memory test double a true substitute for the real store.

### 8.1 ORM models

ORM models are distinct from domain types and from Pydantic API models. A `Quote` domain type (in `domain/`) and a `QuoteRow` ORM model (in `adapters/postgres/`) are two different things; the repository translates between them. Use SQLAlchemy 2.0 declarative style with `Mapped` / `mapped_column` — not the legacy `Column` assignment form.

```python
# app/adapters/postgres/orm.py
from datetime import datetime, timezone
from sqlalchemy import String, DateTime, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class QuoteRow(Base):
    __tablename__ = "quotes"
    id: Mapped[str] = mapped_column(String, primary_key=True)
    item_id: Mapped[str] = mapped_column(String, index=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
```

Tables are plural snake_case (`quotes`, `audit_records`). Timestamps are timezone-aware UTC. Don't put business logic on ORM models — they're row-mapping structures, not domain objects.

### 8.2 Migrations

Schema changes go through **Alembic**, one migration per schema change. Autogenerate the migration, then **read and correct it** — autogenerate misses constraints, index renames, server defaults, and data migrations, so it's a starting draft, never a trusted output.

```bash
alembic revision --autogenerate -m "add quotes table"
# review the generated file before applying
alembic upgrade head
```

A migration that has been applied anywhere shared is immutable — fix forward with a new migration, never edit a merged one. Each migration's `downgrade()` is real and tested, not a stub. Destructive changes (drop column, narrow a type) are split: ship the additive half, migrate the data, drop the old half in a later migration — never in one irreversible step.

### 8.3 Repository implementation

The repository is the adapter that implements the port. It takes the per-request `AsyncSession` (§2 of the service-patterns reference), translates ORM rows to domain types on the way out and domain types to rows on the way in, and **translates infrastructure exceptions to domain exceptions at the boundary** — a `SQLAlchemyError` never escapes the adapter (consistent with the layer-boundary rule in the service-patterns reference, §5).

```python
# app/adapters/postgres/quote_repository.py
class PostgresQuoteRepository:  # implements the QuoteRepository port
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def find_by_id(self, quote_id: str) -> Quote | None:
        row = await self._session.get(QuoteRow, quote_id)
        return _to_domain(row) if row else None

    async def save(self, quote: Quote) -> None:
        try:
            self._session.add(_to_row(quote))
            await self._session.flush()
        except IntegrityError as exc:
            raise DuplicateQuoteError(quote.id) from exc
```

Translation functions (`_to_domain` / `_to_row`) are explicit and live with the repository. Don't leak ORM objects past the port boundary, and don't let the service layer hold a `QuoteRow` — that's the coupling the port exists to prevent.

---

## 9. Container and build

Services build as multi-stage Docker images that run as a non-root user.

- **Builder stage** installs hash-verified dependencies (`pip install --require-hashes`) and compiles what needs compiling.
- **Runtime stage** copies only the installed environment and application code — no build toolchain in the final image.
- The container runs as a **non-root user**; the process listens on the port from Settings.
- Scan the image for known vulnerabilities before deployment.

```dockerfile
# Builder
FROM python:3.11-slim AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --require-hashes --no-cache-dir -r requirements.txt

# Runtime
FROM python:3.11-slim
RUN useradd --create-home --uid 1000 appuser
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --chown=appuser:appuser app/ ./app/
USER appuser
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

*Provisioning what runs this image — cluster setup, IAM, networking, deploy automation — is the `infrastructure-code` skill's job, not a code-authoring concern. The seam is the image: this skill builds it; `infrastructure-code` provisions and runs it.*

---

## 10. Project scaffold and toolchain

A new service repo carries a `pyproject.toml` configuring the toolchain and the coverage gate. (Writing the tests is the `testing` skill; this is the config that makes them runnable and gated.)

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
addopts = "--cov=app --cov-report=term-missing --cov-fail-under=90"

[tool.ruff]
# E, F, W, I, B, C4, UP, RUF at minimum
[tool.ruff.lint]
select = ["E", "F", "W", "I", "B", "C4", "UP", "RUF"]

[tool.mypy]
strict = true
```

Coverage floor is **90% line coverage from day one** — a hard gate, not a target to grow into.

Minimum repo files: layered `app/` tree (§2), `tests/` tree, `requirements.in`/`requirements-dev.in` + compiled lockfiles, `Dockerfile` (§9), `.env.example` (committed) with `.env` gitignored, and a `README.md` carrying service name, one-paragraph description, data-classification tier (see the security-and-data reference), and a local-dev quickstart.

### 10.1 Day-one core primitives

A fresh service stands up a small set of `app/core/` primitives before any business endpoint. These are *shown* throughout the service-patterns and security references but are listed here so a scaffold doesn't have to rediscover them — build them once, at the start, and every endpoint inherits them:

| Primitive | Location | Reference |
|---|---|---|
| `Settings` class + `get_settings()` | `app/core/config.py` | service-patterns §3 |
| Structured-logging config | `app/core/logging.py` | service-patterns §4 |
| Correlation-ID middleware | `app/core/middleware/correlation_id.py` | service-patterns §4 |
| `ApiResponse` / `ErrorResponse` / `FaultClass` envelopes | `app/models/envelope.py` | service-patterns §1 |
| `DomainError` base + exception handlers | `app/domain/exceptions.py` + `app/main.py` | service-patterns §5 |
| `ServiceClient` | `app/core/service_client.py` | service-patterns §7 |
| `emit_audit()` + `AuditAction` | `app/core/audit.py` | service-patterns §4 |
| `/healthz` + `/readyz` | `app/api/health.py` | service-patterns §6 |
| Auth dependencies (`get_current_user`, `require_roles`) | `app/core/auth.py` | security-and-data §3–4 |
| Async engine + `get_db_session` dependency | `app/core/db.py` | service-patterns §2 |

Build only what the service actually needs — a service with no inbound auth skips the auth dependencies, a service with no downstream calls skips `ServiceClient` — but most services need most of this, and standing them up first is cheaper than retrofitting.
