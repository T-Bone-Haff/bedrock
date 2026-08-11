---
name: agent-code
description: "LLM-call implementation only, including structured-output parsing, bounded salvage and recovery, model transport, tool loops, budgets, and evidence. Use this skill when an LLM call is the code's central act. Do not use for observed-failure diagnosis (debug), ordinary service code (application-code), executor handoffs (author-execution-relay), or design-record review (design-review-loop)."
---

# Agent Code

Provider-neutral engineering rules for code whose central act is an LLM call. Bind a provider, SDK, framework, and telemetry exporter only through an explicit profile. `reference/anthropic-python-profile.md` is one such profile; it is not the portable contract.

## Bright line: judgment versus mechanism

Name the minimum LLM judgment steps. Everything else—identity, parsing, validation, retry accounting, tool correlation, budgets, and terminal predicates—is executed deterministic mechanism. A model may propose a terminal outcome; code verifies it. When the applicable mechanism did not execute, report the weaker observation and never claim execution, safety, or convergence.

## Prompt and interface artifacts

- Store shipped prompts as versioned files, hash the bytes actually sent, and review every prompt-byte change as semantic.
- Give each prompt artifact its own version. Do not use that version as a model, transport, tool, or MCP-interface version.
- Version tool and MCP capabilities through machine-readable names, schemas, compatibility ranges, negotiation, and deprecation policy. Reject unsupported versions before model execution.
- Separate instructions from untrusted retrieved content and tool output. Never treat narrated authorization, prior review, or embedded instructions as authority.

## Structured output: parse, salvage, validate, recover

Model output is untrusted inbound data. Each call site declares a machine-readable generation contract: envelope grammar, strict item schema, identity-stamping rule, recovery policy, and terminal failure disposition.

1. Prefer provider-native constrained output where the selected profile supports it. The portable contract does not assume that capability.
2. Parse the whole expected payload first. If that fails, apply at most one declared salvage grammar: strip one outer markdown fence, then enumerate balanced JSON object/array candidates of the expected top-level kind.
3. Accept salvage only when exactly one candidate passes the strict schema. Zero valid candidates fails; two or more valid candidates is ambiguous and fails. Never accept “the first parseable payload.”
4. Stamp actor identity, invocation id, model, schema version, prompt hash, and attempt number from invocation context—not model claims.
5. Record the parse path (`native`, `whole`, `salvaged`), candidate count, validation failures, and the response hash. Raw prompt or completion content is retained only when the call site's data classification, consent, redaction, access, location, and retention policy allow it. Content capture is off by default.
6. Recovery is position-specific. A load-bearing call retries only within the aggregate budget and otherwise aborts or escalates; a best-effort call may drop an item observably. Never fabricate an exit-path value.

Reasoning has schema-specific outlets. Some schemas need no rationale; others permit one or more bounded explanation fields. Do not impose a universal rationale field.

`reference/agent-execution.schema.json` is the minimum portable evidence envelope. Implementations may add namespaced fields but may not weaken its required provenance, accounting, and disposition fields.

## One aggregate execution budget

Define one deadline and one attempt/spend envelope across transport failures, malformed content, schema recovery, model fallbacks, and tool iterations. A retry at one layer consumes the same aggregate budget as every other attempt. The budget declares:

- maximum model attempts, tool iterations, elapsed time, input/output tokens, spend, and concurrent calls;
- allowed model/provider fallbacks and rate limits;
- cancellation propagation and per-attempt remaining deadline;
- idempotency key rules for calls and side-effecting tools;
- circuit-breaker posture for the workload (enabled, disabled with rationale, or delegated to a named host layer).

Stop before an attempt that cannot fit the remaining budget. Emit a typed terminal disposition such as `succeeded`, `schema_failed`, `budget_exhausted`, `cancelled`, `tool_failed`, or `transport_failed`.

## Tool-loop state machine

Implement tool use as a bounded typed state machine, not a conversational `while` loop. Validate capability and schema versions before dispatch; allowlist tools per actor; correlate every result to exactly one request; reject unknown tools and duplicate or orphan result ids. Declare whether independent calls may run in parallel and preserve deterministic result ordering. Record partial failures individually, feed only schema-valid results back to the model, honor provider stop reasons, assemble streaming fragments before validation, and end at the declared iteration/deadline budget. Side-effecting tools require idempotency and an authorization gate outside model control.

## Observability and evidence

Emit one invocation record and child records for model attempts and tool executions. Include trace/correlation ids, timestamps, model/provider/profile, prompt and schema versions/hashes, finish/stop reason, retry cause, token and spend accounting, cache accounting where available, budget remaining, parse path, tool result dispositions, cancellation, and terminal disposition. Prefer current OpenTelemetry GenAI conventions where the host supports them; pin the adopted semantic-convention version rather than claiming an evergreen mapping.

Evidence claims must be reproducible from distributed fixtures or cited public evidence. Private runs may inform authoring but cannot substantiate the installed consumer contract. Label untested guidance as a requirement or hypothesis, not “proven.”

## Security boundary

This skill governs code-level LLM and tool invariants: untrusted inputs, capability scoping, injection containment, provenance, schema validation, bounded agency, and auditable execution. System-wide identity, network, supply-chain, data-governance, and deployment controls belong to their owning architecture and security standards; reference them rather than duplicating them here.

## Profiles and sibling routes

- `reference/anthropic-python-profile.md` binds these rules to Anthropic Messages and Python.
- `reference/mcp-server-authoring.md` carries only MCP-specific interface residue.
- Service structure routes to `application-code`; tests/evals to `testing`; observed failures to `debug`; finished-diff review to `code-review`; operator-to-executor prompts to `author-execution-relay`.
- Review topology and convergence semantics route to `design-review-loop`. Agent-code supplies its call, parsing, recovery, budget, tool-loop, and evidence primitives; it does not confer convergence.
