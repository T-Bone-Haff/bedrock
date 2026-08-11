# Haffey pytest/FastAPI profile

This is the pytest realization of the portable testing contract for Python/FastAPI/async SQLAlchemy services. It is a profile, not universal Bedrock law.

## Layout and markers

```text
tests/
  unit/
  integration/
  contract/
  e2e/
  conftest.py
```

Use explicit markers for suites whose environment or gate differs. Names should communicate unit, scenario, and expected outcome. Module revision headers and mandatory Arrange/Act/Assert comments are not required; clear structure is.

## Doubles by purpose

- Pure domain behavior: ordinary values or small fakes.
- Stateful repository behavior: an in-memory adapter implementing the same contract, where maintaining it earns its cost.
- Interaction contract: `Mock`/`AsyncMock` and assertions limited to the interaction that is behavior.
- HTTP dependency: `respx` for consumer behavior; do not label it provider verification.
- Real persistence/broker boundary: disposable container or isolated service in integration tests.

Mocks do not universally require call assertions. Assert calls only for behavior such as “must not publish,” ordering, attempt budget, audit emission, or exactly-once handoff.

## Lifespan-aware application fixture

The transport alone does not guarantee lifespan execution. Use an explicit lifespan manager:

```python
import pytest
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

@pytest.fixture
async def client(app):
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
        ) as value:
            yield value
```

Test startup failure and cleanup as well as the happy path. Disable telemetry export through direct environment assignment before importing the application.

## Database isolation

A nested transaction on a session owned only by the test does not isolate requests that open different sessions/connections. Use one of these declared patterns and prove it under multiple requests, failures, and parallel workers:

- bind application sessions to a test-owned connection and roll back the outer transaction;
- create a unique database/schema per worker/test and destroy it; or
- reset/truncate through a controlled fixture when transaction binding is impossible.

Test the actual dependency override/wiring. Verify no committed state remains after both success and exception paths.

## Contract testing

Endpoint tests verify the service's OpenAPI/request/response/error model. Cross-service contract tests additionally require:

- versioned consumer expectation and provider artifact;
- an owner and publication location;
- provider verification against the exact artifact;
- compatibility policy for additive and breaking changes; and
- deployment/promotion rules when verification fails.

A mocked `respx` response proves consumer handling only. It is not provider compatibility evidence.

## E2E and promotion

Each suite declares its gate, such as `merge`, `staging_deploy`, `production_promotion`, or `advisory`. A suite cannot be both required for production promotion and globally non-blocking. Advisory failures remain visible and owned.

## Coverage and advanced methods

Configure `pytest-cov` line and branch reporting from the schema-valid strategy; do not assume 90%. Critical security, money, tenant, migration, retry, and state-machine paths may require 100% state/branch coverage even when the project-wide threshold is lower.

Risk-triggered methods include Hypothesis property tests, fuzzing, mutation testing, concurrency scheduling, migration upgrade/downgrade, performance/load, security probes, fault injection, and chaos. Record the trigger, environment, budget, pass criterion, and `not_applicable` rationale.

## Flakes

On first observed intermittence, route to `debug`. If quarantine is authorized, mark it visibly with issue, owner, entry/expiry dates, retry cap, affected gate, and exit criteria. A retry pass never erases the failure observation.
