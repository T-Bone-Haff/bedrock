---
name: application-code
description: House engineering standard for authoring Python service and application code — FastAPI services, async patterns, port/adapter layering, API design, configuration, structured logging, error handling, resilience, security, service scaffolding, and the operational shell scripts that travel with a service. Use this whenever writing, structuring, scaffolding, or conforming application or service code: building an endpoint or service, setting up a new service repo, adding config/logging/auth/resilience/caching to a service, wiring inter-service calls, writing a startup or verification or commit shell script, or checking whether code follows the conventions. Assumes a Python 3.11+/FastAPI/async-SQLAlchemy/GCP/GitHub stack; on a materially different stack, treat the conventions as a rebind, not a line-edit. Writing the tests themselves is the testing skill; reviewing a finished diff is the code-review skill — this skill is about authoring the code.
---

# Application Code

The engineering conventions for authoring Python service code. This SKILL.md carries the invariants that apply to *every* piece of code plus a map into the detailed references; load a reference file for the area you're working in.

## Stack binding (read once)

These conventions are written against a specific stack: **Python 3.11+, FastAPI, async SQLAlchemy/asyncpg, GCP, GitHub.** They're portable across projects *on that stack*. A materially different choice on any axis — another language, a non-FastAPI framework, a different cloud or VCS host — is a **rebind**, not a small substitution: it means re-deriving the equivalent conventions for that stack, not editing individual lines here. Name the rebind explicitly when you do it.

## The misfit rule

These are strong defaults, not scripture. Where a convention genuinely doesn't fit the work in front of you, state the exception and why in the code or commit, then proceed — don't silently violate it, and don't contort the code to satisfy a rule that doesn't earn its place here. A recurring misfit is a signal the convention should change, not a thing to keep working around.

## Always-apply invariants

These hold for every module you write, regardless of which area you're in. If you remember nothing else from the references, hold these:

1. **Async-first.** Every HTTP handler is `async def`; no synchronous/blocking calls inside async code.
2. **Complete type annotations** on every function signature; code passes `mypy --strict` and `ruff`.
3. **Layered, directional imports.** `api → services → ports → adapters`, with `domain`/`models` at the base. A handler reaching into `adapters/` is a violation.
4. **Config comes from Settings**, not module constants or scattered `os.environ`. Secrets come from the environment — never source, logs, errors, or responses.
5. **Structured logging only** (`structlog`, JSON), with a correlation ID bound per request and forwarded on outbound calls. No `print()`, no bare stdlib logging.
6. **Domain exceptions** extend a `DomainError` base and surface to HTTP via exception handlers — no scattered status codes, no silent cross-layer swallowing.
7. **Validate inbound data with Pydantic** at the boundary before it reaches the service layer.
8. **Every module carries the comment block**; every public function/class carries a Google-format docstring.
9. **Outbound HTTP flows through the canonical `ServiceClient`** (retry, deadline, circuit breaker, correlation-ID, auth) — never per-call `httpx` clients.
10. **Classify the data.** Tier 3/4 data never lands in logs (the log ceiling is Tier 2); it's encrypted at rest.

## Where to look

Load the reference for the area you're working in — each is self-contained and cross-links the others where needed.

| You're working on… | Read |
|---|---|
| Scaffolding a service; file/layer layout; naming; deps; types; container; the `pyproject` toolchain + coverage gate | `reference/01-code-structure.md` |
| Building endpoints; async; config/Settings; logging & observability; error handling; resilience (health checks, retries, circuit breakers); inter-service calls; caching; background jobs; performance | `reference/02-service-patterns.md` |
| Handling sensitive data; data-classification tiers; authentication (JWT); authorization (RBAC); service-to-service auth | `reference/03-security-and-data.md` |
| Writing an operational/utility shell script (startup, verification, repo-state, commit helper) — strict mode, heredoc/tempfile traps, exit codes, git pre-flight | `reference/04-shell-scripts.md` |

## Boundaries with sibling skills

- **Writing tests** → the `testing` skill. This skill carries the *toolchain* that makes tests runnable and gated (the `pytest-cov` 90% gate in `pyproject.toml`, in `01-code-structure.md` §10) because that's part of scaffolding a service — but the test layout, naming, mocking, fixtures, and AAA discipline live in `testing`.
- **Reviewing a finished diff** → the `code-review` skill. This skill is about *authoring* code that conforms; deciding whether an existing change conforms is a review task.
- **Infrastructure — provisioning, networking, IAM, Kubernetes manifests, and the Terraform delivery pipeline** → the `infrastructure-code` skill. The seam is the container image: this skill *builds* it, `infrastructure-code` *provisions and runs* it.
- **Git workflow and branching, and the application build/test/deploy pipeline** remain out of scope here — shared version-control and (forthcoming) app-CI/CD concerns, not code-authoring ones.
