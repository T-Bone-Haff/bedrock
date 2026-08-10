# Conformance checklist

Select checks from changed behavior and risk. Each applicable check receives a gate disposition; do not mark the whole section N/A without a reason.

## Base change checks

- Scope and diff agree; no undeclared side effects or unrelated files.
- Public inputs, outputs, errors, and compatibility behavior are explicit.
- Configuration and secrets use the owning domain contract.
- Logs, telemetry, and evidence avoid sensitive-content leakage.
- Tests cover the changed state space, boundary conditions, and credible failures.
- Relevant lint, format, type, test, build, scan, and deployment checks have dispositions.
- New dependencies have provenance, maintenance, license, and rollback treatment.
- Unsupported or deferred cross-cutting assurance is named honestly.

## Backend and agent overlays

For backend code, consult `application-code`; for LLM-centered behavior consult `agent-code`; for planned tests consult `testing`. Check event-loop blocking, boundary validation, error translation, retry budgets, untrusted model/tool data, structured-output framing, tool-loop bounds, and cost/evidence controls only where applicable.

## Frontend overlay

Consult `frontend-code`. Check accessible names and keyboard paths, focus and motion, browser-permission state, teardown, XSS/URL sinks, credential exposure, generated-contract drift, responsive behavior, real-browser coverage where risk requires it, and dependency/media provenance.

## Infrastructure overlay

Consult `infrastructure-code`; do not mirror its complete standard here.

- Terraform plans identify state lineage, configuration revision, provider lockfile, artifact digest, expiry, and stale-plan behavior.
- Secret values are not materialized into state unless the explicit risk contract permits and protects it.
- Destructive changes, imports, moved resources, bootstrap, drift, and recovery are addressed when present.
- Identity, IAM ownership, and executable dependencies are least-privilege and immutable.
- Kubernetes changes address workload identity, security context, disruption, rollout, storage, backup/restore, and digest identity as applicable.

## Application-delivery overlay

Consult `app-delivery-pipeline`.

- Pull requests prove buildability without granting untrusted code publication or deployment credentials.
- Promotion reuses an immutable artifact; production mutation is not blindly canceled.
- Release-event identity, merge queues, rollback, migrations, smoke verification, provenance, and SBOM posture are explicit where applicable.
- Workflow actions and other executable dependencies are immutable and permissions are minimal.

## Risk-triggered overlays

Apply each when the diff introduces or changes the named risk:

| Trigger | Required review questions |
|---|---|
| Migration or data conversion | Forward/backward compatibility, expand/contract order, partial failure, rollback, verification, and owner. |
| Concurrency or state machine | Atomicity, ordering, races, retries, cancellation, idempotency, and impossible states. |
| Authentication/authorization | Identity source, audience, scope, confused-deputy paths, revocation, default deny, and audit. |
| Multi-tenancy | Tenant derivation, isolation at every store/cache/log boundary, cross-tenant tests, and operator access. |
| Money or irreversible action | Exact arithmetic, duplicate suppression, reconciliation, approval, rollback/compensation, and audit. |
| Performance or capacity | Workload model, limit, measurement method, backpressure, degradation, and regression threshold. |
| Deployment ordering | Dependency compatibility, migration order, health versus readiness, partial rollout, and rollback. |
| Dependency/license | Source, lock/pin, integrity, license obligations, advisories, ownership, and removal path. |

## Gate treatment

- `passed`: command/evidence and observed subject are named.
- `failed`: produces or supports a blocking finding when required for safe landing.
- `not-relevant`: reason names the missing applicability trigger.
- `unavailable`: reason, risk, owner, and escalation are recorded; a required unavailable gate pauses.

## Validator changes

When reviewing a checker, account for every authority requirement as detected violation, fail-loud behavior, or documented deliberate gap. Inspect presence assumptions, nullable predicates, and parse/merge steps that may destroy evidence before comparison.
