# Compatibility and support matrix

Only combinations backed by retained evidence are supported.

| Surface | Verified identity | Distribution and reload behavior | Evidence | Status |
|---|---|---|---|---|
| Claude Code | 2.1.226 | Refresh/update marketplace, update plugin, then start a new session. | strict validation and isolated install/reload in required CI | supported |
| Claude.ai / Cowork | Hosted service observed 2026-08-27 | Marketplace changes take effect in the next new session; the host exposes skill-local supporting files but not the package-root manifest. | v8.3.0 fresh-session and full-client-restart probes proved 13 skills and current content while package version remained unavailable; v8.4.0 adds the generated skill-local carrier for forward-repair acceptance under HEB-140 | candidate; repair not release-accepted |
| Codex/OpenAI adapter | None | No adapter is distributed. | none | unsupported |
| Cursor adapter | None | No adapter is distributed. | none | unsupported |
| External product runner-backed review | No package binding | Requires a product-owned workflow binding and versioned runner with compatible schemas, exact invocation, and fresh gate evidence. | none in this package | unavailable; direct and multi-perspective profiles remain supported |

The portable skill core has contract version `2.0.0`; the distributed Claude
adapter contract has version `1.1.0`. These are compatibility identities, not
the package version. The manifest remains the package-version authority.

Portable-core 2.0 moves workflow meaning, actor rosters, authority assignments,
state transitions, retries, budgets, durable execution, and operational posture
to the consuming product. The former product-specific runner reference is
replaced by a generic external binding contract. Direct and multi-perspective
review require no runner. Consumers of the former bundled reference path must
select the generic binding and supply their own declared runner evidence; no
existing product implementation is promoted or mapped automatically.

Support covers installation, discovery, deterministic package validation, and
the declared skill contracts on verified rows. It does not promise incident
response, production operations, regulatory compliance, or cross-agent
security assurance; see the product coverage map and threat model.

A host upgrade, manifest-schema change, routing-adapter change, or generated
carrier format change invalidates the corresponding evidence row until it is
rerun. Unsupported surfaces fail closed: name the missing adapter or capability
and do not claim compatibility by similarity.
