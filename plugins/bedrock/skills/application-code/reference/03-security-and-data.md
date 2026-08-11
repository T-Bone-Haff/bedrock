# Haffey Python service profile: security and data

This profile applies the package safety floor to Python/FastAPI services. It does not replace consumer-owned threat modeling, compliance, incident response, or residual-risk acceptance.

## Data contract

Classify each data category and evidence artifact before handling it. The Haffey tiers are:

| Tier | Meaning | Minimum posture |
|---|---|---|
| 1 Public | Intended for public disclosure | Integrity and availability appropriate to use |
| 2 Internal | Non-public operational/business data | Authenticated access and encrypted transport |
| 3 Confidential | PII, payment/health metadata, sensitive customer data | Encryption at rest, access logging, minimization, controlled retention |
| 4 Restricted | Credentials, signing keys, highly regulated data | Strong isolation, tightly controlled access/custody, dedicated key/secret systems |

Operational and audit logs have a Tier-2 ceiling. Use surrogate identifiers; do not place Tier-3/4 content, tokens, complete identity claims, or raw exception payloads in logs.

## Boundary validation

Validate request bodies, parameters, headers, correlation values, uploaded names/content, callback URLs, identity claims, and deserialized dependency data with explicit bounds. Pydantic validates structure; authorization and semantic constraints remain application policies.

## Authentication profiles

Select and document the actual exposure topology rather than assuming a gateway:

- direct service validation;
- gateway plus service validation;
- service-to-service workload identity/mTLS/token validation; or
- an approved combination.

Every profile defines issuer/trust anchor, audience, permitted algorithms, key discovery and caching, rotation/revocation, clock skew, token lifetime, failure behavior, and identity propagation. The service validates the token intended for it even when an upstream gateway authenticated the request.

Never forward an end-user bearer token blindly. On-behalf-of calls require an explicit delegation/token-exchange contract with target audience, attenuated scopes, actor/subject distinction, lifetime, replay controls, and downstream authorization. Otherwise use the calling workload's identity and carry user context only through a separately governed claim/audit mechanism.

## Authorization

Enforce the policy required by the resource:

- role-based permissions;
- ownership and tenant boundaries;
- attributes and relationships; and
- action/resource/environment constraints.

Deny by default, prevent confused-deputy flows, and test cross-tenant/object-reference cases. Decision logs use stable policy IDs, result, and surrogate subject/resource IDs; do not log full role or attribute sets.

## Secrets and dependencies

Secrets are not source/config defaults and never appear in responses, ordinary logs, exception strings, images, fixtures, or retained evidence. Define runtime retrieval, rotation, revocation, and failure behavior. A `sensitive` wrapper or environment variable does not by itself provide storage safety.

Run SAST, secret scanning, dependency/image vulnerability scanning, SBOM/provenance generation, and license checks according to the selected risk profile. Pin executable dependencies and release image bases by immutable identity; updates remain owned and observable.

## Audit delivery

Classify audit event classes as required or advisory. Required audit evidence for a protected mutation is transactionally coupled or durably handed off before success; advisory audit loss may fail open only with metrics, alerts, and declared residual behavior. Apply data minimization, integrity, access, retention, and clock-correlation rules to the audit channel.
