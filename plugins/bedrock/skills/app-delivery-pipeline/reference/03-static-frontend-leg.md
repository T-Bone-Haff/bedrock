# Static frontend delivery seam

`frontend-code` owns application behavior, accessibility, browser-test semantics, build configuration, and CSP compatibility. This leg consumes those declared commands and delivers the resulting static artifact; it does not redefine frontend behavior.

Build once after the frontend gates pass. Retain source/tree and dependency-lock identity, artifact digest, file manifest, source-map policy, SBOM/provenance, and browser-gate evidence. Promote the same artifact; do not rebuild per channel.

Untrusted pull requests receive no hosting credentials. A trusted preview job may publish an isolated, expiring channel after gates, with sanitized identifiers, least privilege, retention, and an explicit disclosure of which secrets/data are unavailable. Production promotion requires the protected environment and trusted release event.

## Hosting contract

Declare route fallback, custom-domain/TLS ownership, cache policy, rollback, and headers. Hashed assets may be long-lived and immutable; HTML and route manifests require revalidation. Source maps are private artifacts by default unless an explicit observability/publication decision says otherwise.

The hosting profile covers at least Content-Security-Policy (use report-only rollout and reporting where needed), Strict-Transport-Security after domain readiness, Permissions-Policy, Referrer-Policy, X-Content-Type-Options, and an anti-framing policy using CSP `frame-ancestors` (with legacy header only when needed). Retain the deployed header/config digest and verify headers at the production URL.

Post-deploy verification includes expected artifact/version, route fallback, representative static assets and caching, security headers, a browser/synthetic flow supplied by `frontend-code`, and rollback readiness.
