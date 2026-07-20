# Reference: MCP Server Authoring

Authoring an MCP server — a tool surface an agent consumes over the Model Context Protocol. This reference is deliberately light: most of what governs an MCP server is this skill's own disciplines applied to the tool seam, and this file mostly routes to them. It promotes to more only on demonstrated volume.

**Scope of evidence, stated honestly:** house MCP-server authoring experience is n=0 at this writing — this reference is compose-plus-public-authority until the first real server proves it. Expect that first build to teach this file things it doesn't know. (Adopting a *third-party* MCP server is the other side of this seam — a supply-chain decision, tracked as a named gap in `SKILL.md` §Security.)

## The compose (where the real rules live)

- **Tool descriptions are LLM-consumed text — the prompt-artifact discipline applies verbatim** (`SKILL.md` §Prompt artifacts). A tool description is a shipped prompt: versioned repo artifact, generation-stamped on any byte change, reviewed like code, wrap-safe. The name and description are the interface an agent reasons over; a description edit is a semantic change to every consumer.
- **Tool schemas are structured-output contracts** (§Structured output and the parse seam). Input schemas are strict — shape, vocabulary, enums — and the server validates inbound arguments as untrusted data exactly as a service validates a request body. Tool *results* are untrusted inbound data to the calling agent; design them structured and parseable, not prose.
- **Tool scoping is least-agency** (§Security). Expose the minimal toolset that does the job; separate read tools from write tools; gate write authority explicitly rather than shipping it ambiently. A server's tool list is a permission surface, not a feature list.
- **Telemetry follows the observability binding** (§Observability). The OTel GenAI conventions carry MCP-specific semantics in the same `semantic-conventions-genai` repository — bind those; invent nothing.

## The MCP-specific residue

- **Capability declaration is honest.** Declare exactly the capabilities the server implements; a declared-but-stubbed capability is a broken contract an agent will reason over as real.
- **Transport choice is deployment-shaped.** stdio for local single-consumer tools; HTTP-based transports for shared or remote servers — and an HTTP transport puts the server inside `application-code`'s ambient service invariants (auth, logging, config) like any other service.
- **Errors are structured tool results, not exceptions leaked as prose.** An agent consumes the error text; give it the same contract discipline as a success payload — what failed, whether retry is sensible, what the agent should surface.
- **Version the server's tool surface.** Renaming or re-scoping a tool is a breaking change to every consuming agent's reasoning; treat the tool list like a public API surface with a changelog.

## Public authority (pinned 2026-07-20 — verify currency at adoption)

The MCP specification and its ecosystem conventions; the OTel GenAI semantic conventions' MCP coverage. Both are moving targets — pin what you cite.
