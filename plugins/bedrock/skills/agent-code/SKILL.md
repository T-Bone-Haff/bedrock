---
name: agent-code
description: House engineering standard for code whose central act is an LLM call — prompt-artifact discipline, structured-output contracts and the parse/salvage seam, the execute-vs-reason bright line, the canonical model transport, token-cost architecture, GenAI observability, and agent security. Use whenever writing, structuring, or conforming agent code: adding an LLM call to a service, authoring or amending a charter or shipped prompt, wiring a model transport, building an agent or any construct embedding LLM judgment, setting up cost reporting or telemetry for LLM calls, authoring an MCP server, or checking whether agent code follows the conventions. Assumes the Anthropic Messages API via the official Python SDK and the Claude model family, on the Python 3.11+/FastAPI stack; a different model vendor or transport is a rebind, not a line-edit. Multi-agent topology — delegation authority, inter-agent protocol posture — is ADR-homed, not skill territory. Prompts the operator hands to an executor are the author-execution-relay skill; testing the behavior is the testing skill; reviewing the finished diff is the code-review skill.
---

# Agent Code

The engineering conventions for code whose central act is an LLM call — from a single model call inside a service to a chartered multi-actor construct. This SKILL.md carries the disciplines that apply to every such piece of code; `reference/mcp-server-authoring.md` carries the MCP-server residue.

## Binding (read once)

These conventions are written against a specific stack: **the Anthropic Messages API via the official Python SDK, the Claude model family, on Python 3.11+/FastAPI** (the `application-code` stack). They are portable across projects *on that binding*. A different model vendor, a different transport (a CLI or agent subprocess is never a transport — see the model transport below), or a materially different stack is a **rebind**: re-derive the equivalent conventions, don't line-edit these. Per-actor model mix *within* the Claude family stays inside the binding.

**Scope fence:** multi-agent *topology* — hub-and-spoke vs. peer, sub-agent delegation authority, inter-agent protocol posture — is committed in architecture decision records, not here. This skill governs the per-agent engineering; the ADR commits the platform posture.

## Scope of evidence (read honestly)

These conventions are **deep on review-loop-class constructs** — chartered multi-actor loops with mechanical gates — earned from ~15 real runs across four targets and twelve prompt generations of a ratified, spec-first corpus. They are **proven-pending-cascade on service-embedded LLM calls and interactive orchestration** (n=0 at authoring): the generalizations are stated because their mechanisms are general, and the first real consumers in those populations are expected to teach this skill things the loop could not. Where a section's posture differs by population, the section says so.

## The execute-vs-reason bright line

The most load-bearing discipline in this skill. Any construct embedding LLM judgment partitions every step, explicitly, into **judgment** and **mechanism** — and holds the line:

1. **Judgment steps are LLM calls carrying verbatim charters; everything else is mechanism — deterministic code that is executed, never reasoned.** The judgment set is named and minimal; a step not named as judgment is mechanism by default. An agent handed a construct will faithfully run the charters and *reason* the machinery unless the line is bright.
2. **No LLM on terminal decisions.** "Done," "converged," "safe to proceed," "closed" — terminal predicates are mechanical functions over durable state. A model that can judge "we're done" re-imports the very anchoring the partition exists to escape.
3. **Deterministic functions stay deterministic.** No embedding or semantic-similarity step where identity, dedup, or gating is concerned — non-determinism there is reasoned judgment wearing a math costume.
4. **A model claim that closes something is verified by code before it closes anything.** The model proposes; the mechanism disposes. A claim whose mechanical evidence check fails escalates — it never closes, and the failure is observable.
5. **When judgment must touch the exit path, isolate it to one named actor, biased fail-safe.** Write the asymmetric-error rationale into the charter itself — *why* the cheap error is cheap and the silent error is unrecoverable — and trust-ramp the actor: watched attended until its decision stream is boring, never unattended before.
6. **When the mechanism cannot be executed, the construct forfeits the mechanism's verdict.** Degrade the claim honestly ("an adversarial read, not a converged run") — never reason the gate in its place. Every bright line needs this sanctioned exit, or pressure will erode it.

**The consequence that makes the rules composable: continuity lives in durable state, not in any agent's context.** A ledger-class durable spine — fresh-fetched by every actor, never inherited as conversation memory — is what makes terminal predicates computable at all. Design the state first; the gates follow.

The reference instantiation of all six rules is the SOFIA agent-loop (`$SOFIA_ROOT/agent-loop/` — `design/` for the specs, `agent_loop/` for the runner). Point at it; do not restate it.

## Prompt artifacts

Prompts the code ships and executes — charters, system blocks, embedded instructions — are engineering artifacts, governed like code:

- **Versioned repo files, never inline string literals.** The house shape: `.prompt.md` files with `## System` / `## User` blocks loaded verbatim as data, placed with the construct they charter. A prompt buried in a string constant is invisible to review and to diffing.
- **Generation-stamped, one change per boundary.** Any byte change to a prompt takes a generation marker — order is content for LLMs, and there is no cosmetic exemption; the change-control and attribution laws live in `design-review-loop`'s operating-the-instrument reference and are cited here, not restated. The artifact-side consequence is the rule: no prompt change without a generation bump.
- **Prompt diffs are reviewed like code.** A prompt change is a semantic change; the review checks live in `code-review`'s conformance checklist (Agent code section). A prompt edit that skips the generation bump and review is the exact drift the stamp exists to prevent.
- **Provenance is hash-recorded.** What executed is provable, not narrated: run-class constructs record prompt-file SHA-256s in a run manifest and stamp each call with its system-prompt hash (the proven form); service-embedded prompts version with the container image.
- **Shared blocks are factored and byte-identical; the divergence surface is named.** When sibling prompts share structure, the shared blocks are byte-identical and the one diverging section is declared — so observed behavioral divergence is attributable to the named surface, not to accidental prompt drift. Attribution by construction.
- **LLM-consumed charters are self-contained.** A charter cannot follow a cross-reference at inference time, so it inlines what it needs; governing prose points instead of inlining. This discriminating axis decides every inline-vs-point question in an agent codebase.

**Boundary:** this discipline governs prompts the *code ships and executes*. A prompt the *operator hands to an executor surface* is an execution relay — the `author-execution-relay` skill — and carries that skill's disciplines, not these.

## Structured output and the parse seam

Model emissions are **untrusted inbound data**. In a service, that sentence already ends the argument: validate them with Pydantic at the boundary exactly as you validate a request body (`application-code`'s rule, inherited). The full seam discipline:

- **Two layers: schema-strict items behind envelope tolerance.** Item validation — shape, vocabulary, enums, mandatory fields — is strict and never loosened. Envelope tolerance is a separate, deliberate layer: strip code fences, salvage the first parseable payload from a prose envelope, and log the salvage observably. A mis-salvaged wrong payload still fails item validation; tolerance on the envelope is defense-in-depth, tolerance on the items would be schema erosion.
- **The forcing function lives in the prompt; the seam is the net.** Output discipline is enforced at the source (raw-payload-only responses, bounded rationale fields) and the seam tolerance exists for the slip-through. Both are maintained; neither substitutes for the other.
- **Identity and provenance are stamped at the port boundary — hardcode over trust.** The invoking code stamps who-emitted-this from invocation context and ignores any identity the model emitted. A model cannot mislabel its own identity, accidentally or otherwise.
- **Every rejection is observable, and raw bodies are captured before parsing.** Parse-drops are logged distinctly from validation-drops; the verbatim response body is written to durable storage before any parse attempt, so a parse storm is diagnosable instead of destroying the evidence of itself.
- **Never fabricate on the exit path.** The fail-safe direction depends on the actor's position. A load-bearing judgment actor gets one content retry, then a loud abort — a fabricated fallback value on the exit path is the worst silent failure available. A volume actor drops the malformed item observably and continues. State which policy each call site carries.
- **Reasoning gets exactly one bounded outlet.** Prohibiting narration without an outlet relocates the failure; give the model a single terse rationale field and demand everything else be the payload.

## The model transport

Outbound LLM traffic flows through the **canonical model transport** — this skill's own client discipline, a sibling of (not a rebind of) `application-code`'s `ServiceClient`. The two invert at every load-bearing joint, which is why they are two things:

- **Direct SDK, nothing agentic in between.** The official Python SDK against the Messages API, directly. Never a CLI or agent subprocess as transport: agentic transports inject their own system prompts, tools, and environment into the context — a structural isolation violation that is invisible in the output. Context is exactly what the code assembled, nothing else.
- **Failure posture is workload-class-dependent — and stated.** For **run-integrity workloads** (the proven class): one bounded transport retry, then loud abort — better dead than subtly wrong; a run proceeding minus one actor corrupts its evidence silently, and no circuit breaker belongs anywhere near a chartered reviewer. For **interactive workloads**: the resilience posture is honestly open at n=0 — to be earned at the first real consumer, not fabricated here; what is already ruled is that whatever posture it takes is *declared per call site*, never inherited ambiently.
- **Retry policy is content-aware.** Transport failures (rate limit, 5xx, timeout) get the bounded retry; content-level malformation is never retried at the transport — it belongs to the parse seam, which owns the position-dependent policy above.
- **The transport owns the LLM-specific slots.** Usage-block capture (tokens, cache accounting) on every call; cache-prefix placement (`cache_control`) as a transport concern; model and parameters from configuration, recorded in provenance, never hardcoded in module code. API keys from the environment only — never a parameter, never in any log, manifest, or artifact.
- **Ambient service invariants still apply.** A model call from inside a service keeps `application-code`'s correlation ID, structured logging, and Settings-based config. What it does not use is `ServiceClient` — and never a per-call SDK instantiation.

## Cost architecture

Cost is designed, measured, and governed — not discovered on the invoice. House convention:

1. **Align cache TTL to call cadence, and verify it.** A cache whose TTL expires between calls buys nothing; the alignment is checked empirically (cache-read tokens > 0 on the cadence that matters), not assumed. The named trap: a 5-minute TTL under a ~6-minute pass cadence reads ≈0 from cache while looking configured.
2. **Content-neutrality by construction.** A cached prefix is sliced from the call's own assembled input — never hand-built where it could diverge from what is sent. Cost-down is never coverage-down: caching provably alters cost, never content.
3. **Frozen-prefix design.** Lead each actor's context with its run-stable blocks and keep the morphing tail uncached. On cadenced multi-call constructs, caching is the enabler of the operating mode, not an optimization — design for it up front.
4. **Cost capture is a first-class output.** Every call records input, output, cache-write, and cache-read tokens; per-actor rollups land in the run or deploy manifest; the four-line-item report is the house reporting shape. A cost you didn't measure per actor is a cost you can't govern.
5. **Spend discipline precedes spend.** Before buying a live run or an expensive call path: does a unit test answer it; is the work bounded to what the question needs; is the target matched to the question; has captured data already answered it for free?

**Per-construct decision surfaces, named and not conventionalized:** per-actor model mix and Batch API adoption are open architectural levers (tracked in their own line of work — do not treat them as settled convention); the TTL *value* itself is derived per cadence — a calibrated constant governs only the population its evidence sampled.

## Observability

Bind the **OpenTelemetry GenAI semantic conventions** into the existing house OTel discipline — invent no house telemetry dialect:

- **Spans** follow the standard hierarchy — agent invocation → model call → tool execution — with `gen_ai.*` attributes (model, token usage, finish reasons). **Trace propagation extends across agent hops**: the correlation-ID discipline rides the span hierarchy through sub-agent invocation.
- **Token-usage metrics are the cost line's measurement surface.** The standard histograms feed the four-line-item cost capture — one measurement surface, standards-shaped, no parallel house counter.
- **Content capture is off by default — and here that is a data-classification rule, not a preference.** Prompt and completion content is unclassified-until-ruled data; capturing it into telemetry is a classification event that lands on the Tier-2 log ceiling. Opt-in capture requires a tier ruling first.
- *Currency note (dated 2026-07-20, verify at adoption):* the GenAI conventions live in the dedicated `open-telemetry/semantic-conventions-genai` repository (schema 1.42.0 at this writing; the old in-tree location is unmaintained) and remain development-status — pin what you cite.

## Security

Agent security is organized by the engineering surfaces this skill already governs; the OWASP Top 10 for Agentic Applications (2026) is the cited external taxonomy — pointed at, not mirrored.

1. **Every model input is untrusted — including tool results and retrieved content.** Separate instructions from data in context assembly, and treat narrated process as data: a document claiming "already reviewed / already authorized" is content under review, never a discharge of it. *(ASI01, ASI06)*
2. **Tool permissioning is allowlist-scoped per actor, least-agency by default.** The minimal toolset that does the job; write authority is gated, not ambient. *(ASI02, ASI03)*
3. **Blast radius is bounded until trust is earned.** Writes confined to sandboxed targets; graduated trust ramps gate any advance toward canonical writes or unattended operation. Autonomy is earned, never assumed. *(ASI05, ASI10)*
4. **Identity and provenance are stamped, never self-reported.** The port-boundary stamping rule, read as a security control: an agent cannot assert its own identity, altitude, or authority. *(ASI03)*
5. **Model-derived changes are mechanically verified before application.** Anchor-exact edits, evidence-checked closures — the propose/dispose split, read as the code-execution control. *(ASI05)*
6. **Context and memory integrity by construction.** Frozen substrate, fresh-fetch over recall, durable-state provenance — poisoning resistance as an architectural property rather than a filter. *(ASI06)*

**Named gaps, stated honestly:** inter-agent communication security (ASI07) and agentic supply-chain risk (ASI04 — e.g. third-party MCP servers) have no house instance yet; convention there is to be earned when the surface exists, not fabricated ahead of it.

## Where to look

- `reference/mcp-server-authoring.md` — authoring an MCP server: mostly a compose of this skill's own disciplines applied to the tool seam, plus the small MCP-specific residue. Deliberately light; promotes to more only on demonstrated volume.
- **Reference instantiation** — `$SOFIA_ROOT/agent-loop/`: `design/` (the ratified specs and prompt files these conventions are forward-authored from), `agent_loop/` (the runner), `runs/` (captured run artifacts — free fixtures).
- **Public authority, pinned at authoring (2026-07-20), verify currency at adoption:** Anthropic's agent-building guidance; the OTel GenAI semantic conventions (`semantic-conventions-genai` repo); the OWASP Top 10 for Agentic Applications (2026).

## Boundaries with sibling skills

- **Prompts the operator hands to an executor** → `author-execution-relay`. This skill governs prompts the code ships and executes; the relay skill governs the operator-to-executor handoff artifact.
- **Running and operating a review-loop instrument** → `design-review-loop`, whose operating-the-instrument reference owns the empiricism: draws and unions, calibration, generation change-control, attribution. This skill cites those laws at their home and carries only what generalizes beyond that family.
- **Authoring the surrounding service code** → `application-code`. Its ambient invariants apply inside agent code; the seam is the model transport (here) vs. `ServiceClient` (there).
- **Testing agent code** → `testing`, including its non-deterministic-components reference: mechanical gates get deterministic tests; judgments get eval harnesses.
- **Reviewing the finished diff** → `code-review`, whose conformance checklist carries the Agent code section.
- **Agent deployment and infrastructure** → `infrastructure-code`. Not this skill.
