# Haffey Python service profile: structure and runtime artifact

This is a **profile**, not the portable application-code contract. It binds Python 3.11+, FastAPI, Pydantic v2, async SQLAlchemy/asyncpg, GCP, and GitHub. Select only the capabilities the service needs.

## Profiles

| Profile | Required structure |
|---|---|
| Minimum | `app/main.py`, typed boundary models, typed settings, structured logging, error mapping, health endpoints |
| Persistence | Minimum + domain types, repository interface, production adapter, migrations, connection lifecycle |
| Outbound | Minimum + lifespan-managed `httpx.AsyncClient`, aggregate timeout/retry budget, identity/correlation propagation |
| Protected | Minimum + authentication and authorization policy adapters, audit classification and delivery policy |
| Evented/durable | Minimum + versioned event contract, idempotent consumer, durable handoff, retry exhaustion/DLQ policy |
| High-risk | Applicable profiles + threat/risk-derived verification, provenance/SBOM/license controls, stronger evidence retention |

Do not scaffold unused layers. Add a port when domain behavior must be independent of a concrete external implementation or when multiple conforming adapters are real requirements—not because every service must have one.

## Layout

One conforming persistence-capable layout is:

```text
app/
  api/          # FastAPI boundary and dependencies
  services/     # use cases and orchestration
  domain/       # domain types, policies, errors
  ports/        # interfaces justified by selected capabilities
  adapters/     # database, HTTP, broker, identity implementations
  models/       # Pydantic boundary models
  core/         # settings, logging, middleware, lifecycle wiring
```

Imports point inward: boundaries call services; services depend on domain contracts/ports; adapters implement those contracts. A small minimum-profile service may collapse directories when dependencies remain explicit and tests can replace externals without monkey-patching internals.

## Documentation, lint, and types

- Use module docstrings when purpose is not evident. Do not add Author/Created/Revised metadata; Git owns revision history.
- Public APIs need useful docstrings, not ceremonial restatements of signatures.
- Every function signature is fully typed. Avoid `Any`; justify unavoidable dynamic boundaries locally.
- Run `ruff check`, `ruff format --check`, and `mypy --strict` for this profile.
- Environment values use typed Settings. Domain constants remain ordinary constants.

## Persistence

- SQLAlchemy 2.x async APIs and `asyncpg`; ORM rows do not cross the adapter boundary.
- One application-owned session per unit of work/request; transaction ownership is explicit.
- Translate infrastructure exceptions at the adapter boundary while preserving causal chains.
- Alembic migrations are reviewed, forward-safe, and tested. Applied shared migrations are immutable; destructive changes use expand/migrate/contract phases.
- In-memory adapters are optional test doubles for state/behavior tests, not mandatory production architecture.

## Dependencies and supply chain

- Lock production dependencies with hashes and verify them during installation.
- Pin container base images by digest for release artifacts; record the readable tag separately for maintainability.
- Scan dependencies and images under an owned vulnerability policy; generate an SBOM and provenance/attestation where the release profile requires them.
- Declare license policy, exception ownership, and update automation. Application code defines artifact inputs; delivery owns build/publish and infrastructure owns runtime provisioning.

## Container

The fixture-backed pattern copies the complete virtual environment rather than a version-specific `site-packages` directory:

```dockerfile
FROM python:3.11-slim AS builder
WORKDIR /build
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN python -m pip install --require-hashes --no-cache-dir -r requirements.txt

FROM python:3.11-slim
RUN useradd --create-home --uid 1000 appuser
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY --chown=appuser:appuser app/ ./app/
USER appuser
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
```

Release usage additionally replaces mutable base tags with policy-approved digests and retains build provenance. The existing HEB-110 fixture proves virtual-environment/runtime coherence; it does not by itself prove a production image's dependencies, provenance, license policy, or deployment.

## Toolchain and coverage configuration

Application scaffolding supplies pytest/coverage execution configuration because that makes the harness runnable. `testing` owns threshold selection and evidence quality. Do not hardcode a universal percentage here. A project records its risk-derived line/branch thresholds and critical-path rules in its test strategy.
