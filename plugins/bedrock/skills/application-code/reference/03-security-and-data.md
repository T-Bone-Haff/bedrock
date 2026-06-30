# Reference: Security and Data

Security disciplines, the data-classification model, and authentication/authorization. Load this when handling sensitive data, adding auth to a service, or classifying what a service stores.

## Contents

- [1. Data classification tiers](#1-data-classification-tiers)
- [2. Security disciplines](#2-security-disciplines)
- [3. Authentication](#3-authentication)
- [4. Authorization (RBAC)](#4-authorization-rbac)
- [5. Service-to-service authentication](#5-service-to-service-authentication)

---

## 1. Data classification tiers

Every data category a service handles is classified. The tier drives the controls; a service spanning tiers classifies each category separately and applies the highest tier's controls to mixed workflows.

| Tier | Label | Examples | Controls |
|---|---|---|---|
| 1 | Public | Product catalog, public docs | None special |
| 2 | Internal | Order history, preferences, operational metadata | TLS in transit |
| 3 | Confidential | PII, payment metadata, health data | TLS + encryption at rest + access logged |
| 4 | Restricted | Credentials, signing keys, regulated data | Audit-logged; hardware-backed key management and zero-trust access at scale |

Document the service's tier in `README.md`.

**The log-channel ceiling is Tier 2.** Both operational logs and audit logs sit at Tier 2 Internal. Tier 3/4 data MUST NOT land in either channel — use surrogate identifiers (UUIDs) and let the high-tier data live in its classified store.

```python
# Prohibited — Tier 3 data in a log
log.info("user_updated", email="jane.doe@example.com", name="Jane Doe")

# Correct — surrogate identifier + audit record of the action, not its content
log.info("user_updated", user_id="usr-abc123")
emit_audit(action=AuditAction.DATA_UPDATE, actor_id=current_user.subject,
           resource_type="user", resource_id="usr-abc123", correlation_id=correlation_id)
```

**Encryption.** Tier 3/4 data is encrypted at rest (managed-store defaults usually suffice — verify they aren't disabled). All service-to-service traffic uses TLS 1.2+; plaintext HTTP between services in production is prohibited. Tier 3 store access is logged.

---

## 2. Security disciplines

**Input validation.** All inbound data is validated by a Pydantic model before reaching the service layer. Raw `request.json()` / dict access without a model is prohibited — it loses type safety and validation.

```python
# Correct
async def create_item(payload: ItemCreateRequest) -> ApiResponse[ItemResponse]:
    item = await service.create(payload)
    ...

# Prohibited
async def create_item(request: Request) -> dict:
    body = await request.json()
    name = body["name"]  # no validation, no type safety
    ...
```

**Output encoding.** Responses go through Pydantic response models (and FastAPI's renderers) — not raw string concatenation. Non-JSON paths use the appropriate response class (`PlainTextResponse`, `HTMLResponse`).

**Secrets.** Sourced from environment variables / a secret manager; never committed, never in source, logs, errors, or responses. Services consume rotated secrets without code change. (Settings discipline is in the service-patterns reference.)

**Static analysis.** Run `bandit` (SAST) in CI; treat HIGH-severity findings as build failures. A `detect-private-key` pre-commit hook is the minimum secret-scanning gate. Release artifacts can carry a CycloneDX SBOM.

---

## 3. Authentication

**Services don't implement their own authentication.** Authentication happens at the API-gateway tier; services validate the JWT bearer token the gateway passes. No login endpoints, password handling, or token issuance inside a service. Author against this gateway-first model even before a gateway is provisioned.

```python
bearer_scheme = HTTPBearer()

class AuthenticatedUser:
    def __init__(self, subject: str, roles: list[str], correlation_id: str) -> None:
        self.subject = subject
        self.roles = roles
        self.correlation_id = correlation_id

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> AuthenticatedUser:
    """Validate JWT and return parsed user claims. Raises 401 if missing/expired/invalid."""
    try:
        payload = jwt.decode(
            credentials.credentials, settings.jwt_public_key,
            algorithms=["RS256"], audience=settings.jwt_audience,
        )
        user = AuthenticatedUser(
            subject=payload["sub"], roles=payload.get("roles", []),
            correlation_id=payload.get("correlation_id", "unknown"),
        )
        emit_audit(action=AuditAction.AUTH_SUCCESS, actor_id=user.subject,
                   resource_type="session", resource_id="jwt", correlation_id=user.correlation_id)
        return user
    except jwt.ExpiredSignatureError:
        log.warning("auth_token_expired")
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError as exc:
        log.warning("auth_token_invalid", error=str(exc))
        raise HTTPException(status_code=401, detail="Invalid token")
```

**RS256 only** — asymmetric signing, so services validate with the public key and never hold the signing key. HS256 (symmetric) is prohibited for production: it requires a shared secret between identity provider and every service. This needs two Settings fields: `jwt_public_key` and `jwt_audience`.

---

## 4. Authorization (RBAC)

Authorization is enforced via a `require_roles()` dependency factory; both grants and denials are audit-logged.

```python
def require_roles(*required_roles: str) -> Callable:
    async def role_checker(user: AuthenticatedUser = Depends(get_current_user)) -> AuthenticatedUser:
        if not any(role in user.roles for role in required_roles):
            log.warning("authorization_denied", subject=user.subject,
                        required=list(required_roles), actual=user.roles)
            emit_audit(action=AuditAction.AUTHZ_DENIED, actor_id=user.subject,
                       resource_type="route", resource_id="unknown",
                       correlation_id=user.correlation_id, outcome="failure")
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return user
    return role_checker
```

**Role strings come from a central RBAC authority** — services consume canonical names, they don't invent them. Until that authority exists for a project, don't call `require_roles()` with arbitrary strings.

```python
# Correct — canonical role string
@router.post("/orders/{id}/approve", dependencies=[Depends(require_roles("order_approver"))])
async def approve_order(...): ...

# Prohibited — invented role names
@router.post("/orders/{id}/approve", dependencies=[Depends(require_roles("approver", "admin"))])
async def approve_order(...): ...
```

---

## 5. Service-to-service authentication

Inter-service calls use short-lived service-account tokens carrying the *calling service's* identity. **Static service-account keys MUST NOT be stored as secrets in staging or production.** Author against this even before the short-lived-token mechanism is provisioned (local dev can use an application-default-credentials placeholder).

When a call acts on a specific user's behalf, the original end-user JWT is propagated in the `Authorization` header; otherwise the call carries the service's own token. End-user identity also flows via the `correlation_id` across the call chain.
