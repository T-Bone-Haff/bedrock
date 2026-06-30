# Reference: Test Authoring

Worked patterns for the test kinds, the test-first verification rules in full, and coverage discipline. The TDD sequence and the always-apply invariants are in `SKILL.md`; this is the detail.

## Contents

- [1. Test layout](#1-test-layout)
- [2. Test-first verification — meaningful failure](#2-test-first-verification--meaningful-failure)
- [3. Coverage discipline](#3-coverage-discipline)
- [4. AAA structure and naming](#4-aaa-structure-and-naming)
- [5. Mocking and fixtures](#5-mocking-and-fixtures)
- [6. Contract tests](#6-contract-tests)
- [7. Integration tests](#7-integration-tests)
- [8. Containerized dependencies](#8-containerized-dependencies)
- [9. Isolation](#9-isolation)
- [10. E2E](#10-e2e)
- [11. Telemetry isolation in tests](#11-telemetry-isolation-in-tests)

---

## 1. Test layout

Tests live in `tests/` at the service root:

```
tests/
├── __init__.py
├── conftest.py
├── unit/          # fast, isolated; external dependencies mocked
├── integration/   # real FastAPI app via httpx; containerized backends where needed
└── e2e/           # full-stack against a deployed environment (advisory)
```

- **Unit** — under ~1 second per test on average; externals mocked.
- **Integration** — exercise the real app via `httpx.AsyncClient`.
- **E2E** — run against a deployed environment; advisory (non-blocking) in CI.

---

## 2. Test-first verification — meaningful failure

The TDD sequence (SKILL.md) requires *observing* a failing test before implementing. The failure has to be meaningful — it has to prove the test exercises the contract.

**Qualifies as a meaningful red:**
- A framework-native assertion failure from the test's intended spec — "expected `200`, got `501`"; "expected exception `X`, none raised".
- A not-yet-implemented error raised by the **target** function while a behavioral test asserts specific output against it. The stub surface *is* the target surface, so the exception is the meaningful signal — this is the normal stub-test pattern.

**Does NOT qualify** (the test couldn't run its assertion yet — fix and rerun before claiming a red):
- Syntax errors — the test code is malformed.
- Import / module-not-found errors — stub the target minimally until the import resolves.
- Name/attribute errors at collection time — fix until the test collects.
- Any test-runner collection error — the suite is broken.

**Capture the observation** before implementation lands: put the failing-test runner output under a `Test-first verification:` heading in the failing-test commit, or — when the failing test and its implementation land atomically — state explicitly that the test was run red and show the output before the implementation.

The bar is bounded: one observed meaningful red per behavioral unit before its implementation, not "re-confirm every test fails every time." Refactors are exempt (existing tests define the contract); a bug fix needs a reproducing test that fails before the fix.

---

## 3. Coverage discipline

The floor is **90% line coverage, enforced as a CI hard gate**. Two anti-cheating rules make the number honest:

- **No omitting testable code from measurement.** The coverage omit list holds *only* files that are entirely real-infrastructure with no testable implementation. In-memory adapters, env adapters, and other test-friendly implementations are fully testable and are **never** omitted — omitting them is the most common way a green coverage number lies.
- **No measuring around the gaps.** Passing the threshold by scoping measurement away from untested code defeats the gate.

The `pytest-cov` invocation and the `--cov-fail-under` line live in the service's `pyproject.toml` (set up under the application-code skill); this discipline governs what that gate is allowed to count.

---

## 4. AAA structure and naming

Every test file carries the module comment block and follows Arrange-Act-Assert with section comments. Test names are `test_<unit>_<scenario>_<expected>`.

```python
##############################################################################
# Module: test_item_service.py
# Service: inventory-service
# Author: <author or team>
# Created: YYYY-MM-DD
# Revised: YYYY-MM-DD
# Description: Unit tests for ItemService business logic.
##############################################################################

import pytest
from unittest.mock import AsyncMock
from app.services.item_service import ItemService
from app.models.responses import ItemResponse
from app.domain.exceptions import ItemNotFoundError

class TestItemService:
    @pytest.fixture
    def mock_repository(self) -> AsyncMock:
        return AsyncMock()

    @pytest.fixture
    def service(self, mock_repository: AsyncMock) -> ItemService:
        return ItemService(repository=mock_repository)

    @pytest.mark.asyncio
    async def test_get_by_id_when_item_exists_returns_item_response(
        self, service: ItemService, mock_repository: AsyncMock
    ) -> None:
        # Arrange
        expected = ItemResponse(id="abc-123", name="Widget", owner_id="user-1")
        mock_repository.find_by_id.return_value = expected
        # Act
        result = await service.get_by_id("abc-123")
        # Assert
        assert result == expected
        mock_repository.find_by_id.assert_awaited_once_with("abc-123")

    @pytest.mark.asyncio
    async def test_get_by_id_when_item_not_found_raises_not_found_error(
        self, service: ItemService, mock_repository: AsyncMock
    ) -> None:
        # Arrange
        mock_repository.find_by_id.return_value = None
        # Act / Assert
        with pytest.raises(ItemNotFoundError):
            await service.get_by_id("nonexistent-id")
```

---

## 5. Mocking and fixtures

**Mocking policy.** Unit tests mock all external dependencies (DB, HTTP clients, brokers) — no real network or DB connections. Mocks assert they were called with the expected arguments (`assert_awaited_once_with`).

**Service-layer tests use the in-memory adapter, not a mocked port.** The in-memory adapter (a sibling of the production adapter in the application-code layout) preserves the contract the port enforces; mocking the port directly lets the test drift from that contract.

**Shared fixtures** live in `tests/conftest.py`:

```python
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.fixture(scope="session")
def anyio_backend() -> str:
    return "asyncio"

@pytest.fixture
async def async_client() -> AsyncClient:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
```

---

## 6. Contract tests

Every endpoint has a contract test asserting request/response shape under representative inputs — the typed models are the source of truth, and when implementation and contract diverge, the contract wins.

Services consuming *external* APIs maintain consumer-driven contract tests with recorded fixtures, using `respx`:

```python
import respx, httpx, pytest
from app.clients.pricing_client import PricingClient

@pytest.mark.asyncio
class TestPricingServiceContract:
    @respx.mock
    async def test_get_price_returns_expected_schema(self) -> None:
        respx.get("https://pricing-service/api/v1/prices/item-123").mock(
            return_value=httpx.Response(200, json={"item_id": "item-123", "price": 9.99, "currency": "USD"})
        )
        client = PricingClient(base_url="https://pricing-service")
        result = await client.get_price("item-123", correlation_id="test-cid")
        assert result.item_id == "item-123"
        assert result.price == 9.99
```

---

## 7. Integration tests

Integration tests exercise the real FastAPI app via `httpx.AsyncClient`:

```python
import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
class TestItemEndpoints:
    async def test_create_item_returns_201_and_item_response(self, async_client: AsyncClient) -> None:
        payload = {"name": "Widget", "description": "A test widget", "owner_id": "user-1"}
        response = await async_client.post("/api/v1/items/", json=payload)
        assert response.status_code == 201

    async def test_readyz_returns_503_when_database_unavailable(
        self, async_client: AsyncClient, monkeypatch
    ) -> None:
        async def broken_db():
            raise Exception("Connection refused")
        monkeypatch.setattr("app.core.dependencies.get_db", broken_db)
        response = await async_client.get("/readyz")
        assert response.status_code == 503
```

---

## 8. Containerized dependencies

Tests needing a real backend use `testcontainers` rather than a shared external instance:

```python
import pytest
from testcontainers.postgres import PostgresContainer
from sqlalchemy.ext.asyncio import create_async_engine

@pytest.fixture(scope="session")
async def db_container():
    with PostgresContainer("postgres:16") as pg:
        yield pg

@pytest.fixture(scope="session")
async def db_engine(db_container):
    engine = create_async_engine(db_container.get_connection_url(driver="asyncpg"))
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield engine
    await engine.dispose()
```

---

## 9. Isolation

No test relies on state left by a previous test. Use transaction rollback for DB isolation:

```python
@pytest.fixture(autouse=True)
async def rollback_transaction(db_session: AsyncSession):
    async with db_session.begin_nested():
        yield
        await db_session.rollback()
```

---

## 10. E2E

E2E tests live in `tests/e2e/`, tagged `@pytest.mark.e2e`, and run against a fully deployed environment before a production promotion. They're advisory (non-blocking) in CI — useful signal, not a merge gate.

---

## 11. Telemetry isolation in tests

The test environment disables telemetry export (traces, metrics, logs, SDK-level) **before any application import executes**, by **direct assignment** — not `setdefault` or other conditional/inheriting patterns, because a value inherited from the parent environment silently defeats the disable. This is the one sanctioned place for direct environment-variable assignment; application code itself always goes through typed Settings.
