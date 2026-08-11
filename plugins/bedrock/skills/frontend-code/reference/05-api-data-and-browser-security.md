# API identity, runtime trust, and browser security

## API artifact and runtime contract

Generate frontend types from an immutable/versioned API-spec artifact. Retain
spec digest/version, generator package and version, configuration digest,
command/runtime identity, and output digest. Generated files are reproducible
and not hand-edited; CI regenerates and fails on drift.

Generated types do not validate runtime bytes. Select runtime validation and
compatibility behavior from data sensitivity, operation criticality, deployment
skew, intermediary/proxy risk, stale-client lifetime, partial rollout, and
compromise impact. Malformed, hostile, unknown-version, or incompatible data
fails safely and observably. Backend enforcement remains `application-code`.

## Mandatory browser-security coverage

Every applicable profile dispositions these concerns:

- output encoding/sanitization and DOM injection sinks;
- Trusted Types readiness and browser-support limitations;
- safe URL/protocol handling and DOM-clobbering-resistant access;
- cookie/session assumptions coupled to backend CSRF defenses;
- CORS as backend policy, never a client-side authorization control;
- third-party scripts, data access, sandboxing, SRI applicability and inventory;
- service-worker scope, update, cache poisoning, logout/data cleanup and rollback;
- dependency install scripts, audit/triage, lockfile integrity and provenance;
- source-map sensitivity/publication handoff;
- client logging/analytics data minimization and credential exclusion.

Framework escaping is the default rendering path. Dangerous sinks are isolated,
reviewed, sanitized with an appropriate maintained policy, and tested. Avoid
`eval`, `new Function`, string timers, ambient `window`/`document` named-property
lookups, and unvalidated navigation/resource schemes.

## Ownership handoffs

Frontend owns app-side CSP/Trusted-Types readiness, safe runtime behavior,
dependency/script intake, SRI applicability, and source-map sensitivity.
`app-delivery-pipeline` owns deployed CSP/Permissions-Policy/HSTS and companion
headers, source-map publication, artifact provenance/promotion, hosted cache
behavior, and rollout. `application-code` owns cookie issuance, CSRF validation,
CORS, authorization, data enforcement, and server/API compatibility.
