# Compatibility and support matrix

Only combinations backed by retained evidence are supported.

| Surface | Verified identity | Distribution and reload behavior | Evidence | Status |
|---|---|---|---|---|
| Claude Code | 2.1.226 | Refresh/update marketplace, update plugin, then start a new session. | strict validation and isolated install/reload in required CI | supported |
| Claude.ai / Cowork | Hosted service observed 2026-08-11 | Marketplace changes take effect in the next new session. | propagation behavior recorded; full 13-skill cold inventory remains HEB-119 evidence | candidate; not release-accepted |
| Codex/OpenAI adapter | None | No adapter is distributed. | none | unsupported |
| Cursor adapter | None | No adapter is distributed. | none | unsupported |
| SOFIA runner-backed convergence | No package binding | Requires an external versioned recipe and kernel capability. | none in this package | unavailable; lower-assurance profiles only |

The portable skill core has contract version `1.0.0`; the distributed Claude
adapter contract has version `1.0.0`. These are compatibility identities, not
the package version. The manifest remains the package-version authority.

Support covers installation, discovery, deterministic package validation, and
the declared skill contracts on verified rows. It does not promise incident
response, production operations, regulatory compliance, or cross-agent
security assurance; see the product coverage map and threat model.

A host upgrade, manifest-schema change, routing-adapter change, or generated
carrier format change invalidates the corresponding evidence row until it is
rerun. Unsupported surfaces fail closed: name the missing adapter or capability
and do not claim compatibility by similarity.
