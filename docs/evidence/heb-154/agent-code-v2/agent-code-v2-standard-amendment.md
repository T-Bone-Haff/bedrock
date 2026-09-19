# Agent Code 2.0 standard amendment

**Document id:** ACV2-STANDARD-AMENDMENT  
**Status:** `PROVING`  
**Design ratified:** 2026-09-06 (America/New_York)  
**Owner:** Tad Haffey  
**Normative subject:** `plugins/bedrock/skills/agent-code/`  
**Planned contract version:** `2.0.0`  
**Planned portable-core version:** `3.0.0`  
**Package version:** derived at landing; current expected major is `10.0.0`

**Consumer proving amendment:** ratified 2026-09-10 (America/New_York); see `agent-code-v2-ratification-record.md` and proving profile `1.1.0`.

## 1. Purpose and adoption claim

This amendment replaces the current `agent-code` contract where its evidence envelope, salvage rules, side-effect semantics, provider bindings, request identity, and provider-neutrality claim are not strong enough to support a fleet of autonomous or semi-autonomous agents.

The target adoption claim is deliberately narrow:

> Bedrock Agent Code 2.0 defines provider-neutral, fail-closed implementation semantics for bounded LLM calls and tool loops, with reproducible evidence across the declared Anthropic, OpenAI, and Gemini profiles.

That claim is unavailable until every adoption gate in section 14 passes. The standard must use `provider-portable requirement` or `provider profile` before adoption; it must not use `provider-neutral`, `proven`, or equivalent completion language for unverified behavior.

The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** are normative. An implementation is conforming only when both the closed structural schemas and the semantic validator accept its evidence.

## 2. Scope and ownership

The portable contract owns:

- invocation and artifact identity;
- ordered request/context provenance;
- generation-contract identity;
- aggregate budget declaration and accounting;
- model-attempt and tool-attempt evidence;
- parse, salvage, validation, recovery, and terminal semantics;
- side-effect uncertainty and reconciliation rules;
- portable telemetry fields and content-capture policy;
- the minimum provider-profile contract; and
- the proof required to make the provider-neutral adoption claim.

Provider profiles own exact transport mappings, SDK/API surfaces, provider status and refusal taxonomies, native structured-output subsets, tool-call correlation, streaming behavior, usage fields, provider-managed tools, retry defaults, and profile currency.

Consuming products own workflow meaning, actor topology, business authorization, tool allowlists, risk appetite, pricing inputs, data governance, operational thresholds, and deployment controls. A product may strengthen the portable rules. It MUST NOT weaken them while claiming Agent Code 2.0 conformance.

## 3. Ratified design dispositions

The binding dispositions are recorded in `agent-code-v2-ratification-record.md` and summarized here:

| ID | Binding disposition |
|---|---|
| ACV2-D1 | Major contract, portable-core, and package change |
| ACV2-D2 | Closed structural schema plus separate semantic validator |
| ACV2-D3 | Whole parse and optional single outer-fence removal for load-bearing calls; embedded scanning only for bounded best-effort calls |
| ACV2-D4 | Explicit unknown side-effect outcome, reconciliation, and retry prohibition |
| ACV2-D5 | Schema-bound Anthropic, OpenAI, and Gemini profiles |
| ACV2-D6 | Ordered request manifest; local or immutable content-addressed prompts |
| ACV2-D7 | Three-profile proof plus one two-provider consumer before provider-neutral adoption |

## 4. Normative artifact set

The implementation candidate MUST contain the following authoritative artifacts:

| Path | Required change | Authority carried |
|---|---|---|
| `plugins/bedrock/skills/agent-code/SKILL.md` | Amend | Portable normative behavior and routing boundary |
| `plugins/bedrock/skills/agent-code/reference/agent-execution.schema.json` | Replace | Closed execution-evidence structure, schema version `2.0.0` |
| `plugins/bedrock/skills/agent-code/reference/generation-contract.schema.json` | Add | Parse/recovery contract declared before execution |
| `plugins/bedrock/skills/agent-code/reference/provider-profile.schema.json` | Add | Minimum structure and lifecycle of any provider profile |
| `plugins/bedrock/skills/agent-code/reference/authority-provenance.yaml` | Add | Claim-to-authority mapping and freshness disposition |
| `plugins/bedrock/skills/agent-code/reference/anthropic-python-profile.yaml` | Add; retire prose-only profile as authority | Anthropic binding |
| `plugins/bedrock/skills/agent-code/reference/openai-python-profile.yaml` | Add | OpenAI binding |
| `plugins/bedrock/skills/agent-code/reference/gemini-python-profile.yaml` | Add | Gemini binding |
| `plugins/bedrock/skills/agent-code/reference/mcp-server-authoring.md` | Amend | MCP protocol/tool boundary without inventing protocol fields |
| `scripts/validate_agent_review_contracts.py` | Extend or split with a named shared helper | Cross-field Agent Code semantics |
| `validation/agent-review-contracts.yaml` | Amend | Schema/fixture registry and obligation mapping |
| `tests/fixtures/agent-review-contracts/` | Extend | Positive, negative, boundary, and counterfactual examples |
| `tests/test_agent_review_contracts.py` | Extend | Deterministic enforcement proof |
| `plugins/bedrock/governance/registry.yaml` | Amend at adoption | Contract/core versions, source inventory, verification facts |
| `plugins/bedrock/governance/COMPATIBILITY.md` | Amend at adoption | Support and migration impact |
| `plugins/bedrock/CHANGELOG.md` | Amend at candidate creation | Candidate history without release implication |
| package manifest and generated `PACKAGE_IDENTITY.json` carriers | Change/regenerate only in landing transaction | Package version identity |

The YAML profiles are authoritative machine-readable bindings. Optional Markdown companions MAY explain them but MUST be generated from or checked against the authoritative YAML; prose cannot override the schema-valid profile.

## 5. Execution evidence envelope 2.0

`agent-execution.schema.json` MUST be a draft 2020-12 closed schema. Every object is closed with `additionalProperties: false` unless it contains one explicitly named extension map. Extension keys MUST be reverse-domain or organization-namespaced and MUST NOT alter portable field meaning.

The top-level object MUST require:

- `schema_version` with constant `2.0.0`;
- `identity`;
- `profile`;
- `request_manifest`;
- `generation_contract`;
- `budget`;
- `model_attempts`;
- `tool_attempts`;
- `parse`;
- `usage`;
- `telemetry`;
- `terminal`; and
- `extensions`.

### 5.1 Identity

`identity` MUST include invocation id, actor id, start timestamp, end timestamp or explicit absence while active, implementation id/version/digest, and execution-record creation time. IDs MUST be non-empty and scoped so correlation cannot silently collide across concurrent calls.

### 5.2 Profile binding

`profile` MUST include profile id, semantic version, SHA-256 digest, provider, host or gateway, SDK name/version, API family/version or endpoint contract, and selected capability set. Requested model and returned model MUST be separate fields; equality MUST NOT be assumed.

### 5.3 Attempts

`model_attempts` and `tool_attempts` MUST be separate ordered arrays. Attempt identifiers MUST be unique within their kind. Each record MUST include start/end evidence, disposition, remaining aggregate budget at dispatch, physical-attempt count, retry cause when applicable, and correlation fields. The semantic validator MUST reject successful execution with no model attempt and MUST accept a valid execution containing exactly one model attempt and one tool attempt.

Tool attempts MUST declare one execution class:

- `read_only`;
- `idempotent_write`;
- `deduplicated_write`;
- `non_idempotent_write`;
- `reversible_write`; or
- `provider_managed`.

Each class MUST carry the evidence its name implies. For example, a `deduplicated_write` requires a stable deduplication key and acceptance evidence; `reversible_write` requires a reversal identity; `provider_managed` requires the provider's result/correlation evidence and an explicit statement of what the application could not observe.

### 5.4 Parse and terminal records

`parse` MUST record native/whole/outer-fence/best-effort-embedded/failed path, bytes examined, maximum bytes/depth/candidates allowed, candidates found, candidates schema-valid, duplicate-key disposition, response digest, validation failures, and whether any data was discarded before validation.

`terminal` MUST include a normalized status, reason code, source status, source finish/stop reason, success predicate result, reconciliation state, and whether follow-up execution is allowed. The portable status vocabulary MUST include at least:

- `succeeded`;
- `partial_success`;
- `refused`;
- `policy_blocked`;
- `context_exhausted`;
- `unsupported_capability`;
- `schema_failed`;
- `budget_exhausted`;
- `cancelled`;
- `tool_failed`;
- `transport_failed`;
- `outcome_unknown`;
- `reconciliation_required`; and
- `escalated`.

Provider-native values that have no profile mapping MUST fail closed as `unsupported_capability` or `outcome_unknown`, depending on whether an effect may have occurred. They MUST NOT be coerced to `succeeded`.

## 6. Generation contract and parsing

Every call site MUST bind an immutable instance of `generation-contract.schema.json` before dispatch. It MUST declare:

- call criticality: `load_bearing` or `best_effort`;
- expected top-level kind;
- output schema id/version/digest;
- accepted provider-native constrained-output mode, if any;
- maximum response bytes, nesting depth, string length, array items, and object members;
- duplicate-key behavior;
- permitted parse paths in order;
- recovery/retry policy; and
- terminal failure disposition.

The parser MUST reject duplicate object names before ordinary deserialization can collapse them. This is required because RFC 8259 describes duplicate-name receiver behavior as unpredictable.

For `load_bearing` calls, the only portable parse sequence is:

1. validate a provider-native structured value when the profile proves that the returned object is native and complete;
2. otherwise parse the whole response as the expected JSON kind;
3. if and only if declared, remove exactly one outer Markdown code fence whose body consumes the entire non-whitespace response, then parse the body; and
4. fail.

The implementation MUST NOT scan arbitrary prose for embedded JSON on a load-bearing path.

For `best_effort` calls, a declared bounded scanner MAY enumerate balanced candidates after the load-bearing sequence fails. It MUST enforce the declared byte/depth/candidate limits, validate every enumerated candidate, accept only one schema-valid candidate, and fail on zero or multiple schema-valid candidates. Candidate order MUST NOT determine acceptance.

Any parser limit breach is a typed failure, not a partial parse. Recovery consumes the same aggregate budget as all other attempts.

## 7. Aggregate budget semantics

One budget covers model transport, provider/SDK retries, fallback selection, structured-output recovery, tool execution, reconciliation calls, and streaming reconnects. The budget MUST declare maxima for physical model attempts, tool iterations, wall-clock deadline, input tokens, output tokens, spend, and concurrency.

The budget representation MUST distinguish:

- `limit`: numeric value plus unit;
- `used`: known numeric value or explicit `unknown`;
- `remaining`: mechanically derived value or explicit `unknown`;
- `source`: provider, application, estimator, or unavailable; and
- `pricing`: currency, price-table identity/version/digest, and rounding rule when spend is governed.

Unknown usage MUST NOT be normalized to zero. A spend limit without currency and immutable pricing identity is invalid. If the host or provider can retry invisibly, the profile is nonconforming unless it exposes physical attempts or the application disables that retry layer.

Before dispatch, the application MUST prove that the attempted operation can fit every still-applicable remaining limit. A limit reached at exactly its maximum is exhausted; implementations MUST use explicit inclusive/exclusive predicates rather than prose interpretation. Cancellation MUST propagate to every child operation that supports it, and unsupported cancellation MUST be recorded.

## 8. Side effects, uncertainty, and reconciliation

Authorization is an application-owned gate outside model control. Tool descriptions, retrieved content, model output, and prior narration cannot grant authority.

When a tool request may have crossed an effect boundary but its outcome is not known—for example, a timeout after dispatch—the tool attempt and invocation terminal state MUST be `outcome_unknown` with `reconciliation_required: true`. The application MUST NOT retry automatically until a declared reconciliation operation establishes one of:

- the original effect did not occur and retry is authorized;
- the effect occurred and its result is recovered;
- a deduplication or idempotency authority makes replay safe; or
- an operator explicitly resolves the uncertainty.

Reconciliation attempts consume the aggregate budget and MUST reference the uncertain attempt. Exceeding the budget does not erase uncertainty; the invocation terminates with the uncertainty intact.

## 9. Request and context integrity

`request_manifest` MUST identify the exact ordered material presented to the provider, including system/developer instructions, user content, tool definitions, retrieved resources, prior messages, compaction summaries, and provider-added context that the profile exposes.

Each manifest entry MUST include position, role/kind, media type, byte length, SHA-256 digest, source class, trust class, data classification, transformation chain, and local artifact identity or immutable hosted reference. The manifest MUST bind the serialized outbound request digest after all application transformations.

Shipped prompts MUST be versioned local files. A hosted prompt is acceptable only when the reference is immutable or version-pinned, content-addressed, and the resolved bytes are recorded or independently retrievable under the declared retention policy. A mutable prompt name or provider-side alias is not sufficient evidence.

Truncation, summarization, compaction, retrieval filtering, or instruction injection performed by the application, host, gateway, SDK, or provider MUST be declared and detectable. Silent fallback or silent context loss is nonconforming. Where provider-added bytes cannot be observed, the profile MUST state that limit and the claim must narrow accordingly.

## 10. Provider-profile contract

Every profile MUST validate against `provider-profile.schema.json` and MUST include:

- profile id, semantic version, digest, owner, provider, host/gateway, SDK range, API family/version, endpoint, and accessed date;
- capability matrix with `supported`, `unsupported`, `conditional`, or `unknown` values and evidence references;
- supported structured-output schema subset and provider injection/transformation behavior;
- request and response mapping, including requested and returned model;
- normalized status, stop/finish, refusal, policy, truncation, and incomplete mappings;
- client-managed and provider-managed tool-call forms, correlation authority, missing-id behavior, and parallel-call behavior;
- streaming assembly, interruption, usage-finalization, and cancellation behavior;
- provider and SDK retry defaults plus the mechanism used to disable or count them;
- token, cache, reasoning, billing, and unavailable-accounting mappings;
- context-window, automatic truncation, compaction, prompt-hosting, and provider-added instruction behavior;
- telemetry mapping pinned to a named OpenTelemetry GenAI semantic-convention release or commit;
- data-handling/content-capture constraints;
- capability detection and fail-closed unavailable behavior; and
- review triggers for SDK/API/model/status/schema/telemetry changes.

The initial required profiles are Anthropic Messages/Python, OpenAI Responses/Python, and Gemini GenerateContent or Interactions/Python. The profile MUST pick one exact API family per profile version; it may not merge materially different surfaces into a fictional common provider API.

Profile notes that change a portable invariant are invalid. Profile-specific fields belong in the evidence `extensions` map unless promoted by a later portable schema version.

## 11. MCP boundary correction

The MCP reference MUST distinguish protocol negotiation from application-owned tool-interface versioning.

- MCP protocol version and capabilities are negotiated through initialization and MUST be recorded from the actual client/server exchange.
- The MCP `Tool` object does not define a portable first-class tool semantic-version field. The standard MUST NOT claim that MCP itself supplies one.
- If a product versions tool behavior, the version and compatibility range MUST live in a declared application-owned convention—such as a namespaced `_meta` member, name convention, or external registry—and both peers must validate that convention.
- Tool input/output schemas, annotations, and descriptions are untrusted interface material until validated against the selected policy.

## 12. Observability, privacy, and reproducibility

The portable evidence schema MUST preserve facts even if no telemetry exporter exists. An OpenTelemetry mapping is an adapter, not the evidence authority.

The selected semantic-convention version or immutable commit MUST be recorded because GenAI conventions can move or change. Requested model, response model, host/gateway, provider, finish reasons, usage, retries, tool attempts, and terminal state MUST remain separately queryable.

Raw prompt, completion, reasoning, or tool content capture is off by default. Enabling it requires an application-owned policy specifying data classification, purpose, consent where applicable, redaction, access, storage location, encryption, and retention. Digests and structural metadata remain required even when content capture is prohibited.

Every conformance claim MUST point to distributable fixtures, replayable commands, exact dependency identities, and retained output digests. Private or irretrievable runs may inform design but cannot substantiate the installed contract.

## 13. Normative obligations

The implementation and proving profile MUST preserve these stable obligation IDs:

| ID | Obligation |
|---|---|
| AC2-schema-negative | Every declared invalid structural fixture is rejected by the closed schema. |
| AC2-schema-positive | Every declared valid structural fixture is accepted by the closed schema. |
| AC2-budget-joint | All physical attempts and tool/reconciliation work consume one aggregate budget with explicit boundary predicates. |
| AC2-terminal-truth | Success and failure terminal states are derived from complete evidence, never narration or a single field. |
| AC2-side-effect-unknown | Indeterminate effects remain unknown and cannot be retried before reconciliation. |
| AC2-salvage-bounds | Parse paths, size/depth/candidate bounds, duplicate keys, and ambiguity are enforced exactly. |
| AC2-profile-complete | Each profile validates structurally and maps every required portable concept. |
| AC2-profile-live | Each required profile has fresh, exact-identity live evidence or the adoption claim is unavailable. |
| AC2-context-integrity | Ordered request bytes, transformations, context loss, and prompt identity are observable. |
| AC2-provenance-total | Every externally derived normative claim maps to a current authority and scope. |
| AC2-otel-pin | Telemetry mapping names a stable semantic-convention identity and detects drift. |
| AC2-routing | Positive, negative, collision, and ordinary-prose routing cases select the correct skill boundary. |
| AC2-consumer | One executable representative consumer is built using the candidate skill, uses the same portable interface with two providers without conditional weakening, and separately proves build-use completeness, runtime conformance, and resulting-agent accuracy. |
| AC2-cold-review | An independent reviewer can reproduce the candidate's claim from retained artifacts alone. |

No obligation may be marked `passed` by narration. The evidence manifest MUST map each ID to its detector, control, exact population, result artifact, and digest.

## 14. Adoption gates and lifecycle

The amendment lifecycle is:

1. **RATIFIED DESIGN** — complete by ACV2-RATIFICATION.
2. **PROVING** — current state; freeze obligation IDs and counterfactual fixtures before implementation results are known.
3. **CANDIDATE IMPLEMENTATION** — implement on an isolated feature branch with a named ticket and no release claim.
4. **DETERMINISTIC PROOF** — schemas, semantic validation, fixtures, package validators, full tests, trigger audit, and routing evaluation pass.
5. **LIVE PROFILE PROOF** — exact Anthropic, OpenAI, and Gemini profile identities each pass required smokes; unavailable credentials, region, API, or feature blocks the provider-neutral claim.
6. **CONSUMER PROOF** — the identified fulfillment-recovery desk is built through complete use of the candidate skill, exercises two provider profiles through the same portable interface plus a mixed-provider configuration, and produces independently evaluated build-use, runtime-conformance, and outcome-accuracy evidence under proving profile section 7. Fabricated workloads are permitted; live execution and accurate outcomes must be observed. Experiments using the candidate precede adoption; fleet use follows adoption.
7. **INDEPENDENT REVIEW** — direct evidence-cited adversarial review closes or explicitly escalates every finding.
8. **OPERATOR ACCEPTANCE** — the operator ratifies the candidate and any residual limitations.
9. **LANDING TRANSACTION** — update the manifest-derived package major, registry, compatibility matrix, changelog, source inventory, and generated identity carriers atomically; run all release gates.
10. **COLD ACCEPTANCE** — a fresh consumer session verifies installed identity, inventory, content, and the provider-neutral claim from retained evidence.
11. **ADOPTED** — only after all preceding gates pass.

Any required provider or consumer proof that is unavailable makes the adoption claim `UNAVAILABLE`, not `PASS`, `WAIVED`, or `NOT APPLICABLE`. A narrower profile-specific release requires a new operator disposition and must not retain provider-neutral wording.

## 15. Migration and compatibility

This is a breaking change because evidence structure, terminal vocabulary, salvage behavior, provider bindings, request identity, and proof obligations change.

- V1 evidence remains valid only for the v1 contract under which it was produced.
- There is no automatic v1-to-v2 evidence conversion. A display adapter MAY present old records, but it cannot manufacture missing v2 proof.
- Consumers MUST choose a v2 profile explicitly and update parsers, terminal handling, budget accounting, and uncertain-side-effect workflows before claiming conformance.
- A transition period MAY support dual emission, but v2 acceptance is evaluated solely against the v2 record and validator.
- Rollback restores the complete v1 package identity and contract; it must not leave v2 records interpreted by v1 semantics or vice versa.

## 16. Change and review triggers

The profile or portable contract MUST be reviewed when any of the following changes: provider SDK major/minor behavior at a mapped seam, API family/version, response status or stop taxonomy, structured-output schema subset, tool correlation, automatic retry/truncation/compaction, usage/billing fields, hosted prompt behavior, MCP protocol/schema, OpenTelemetry GenAI convention identity, JSON/schema validator behavior, or a consumer reports an unmapped native state.

Profile-only compatible mapping changes increment the profile version and refresh profile proof. Any weakening or reinterpretation of a portable invariant requires an Agent Code contract change. The package version remains derived under repository governance.

## 17. Authority and provenance baseline

The authoritative mapping belongs in `authority-provenance.yaml`. The initial baseline is:

| Authority | Read depth for this specification | Governs |
|---|---|---|
| Current Bedrock Agent Code skill, evidence schema, provider/MCP references, registry, compatibility matrix, changelog, and validation registry | Complete local-file reads | Existing contract and repository seams |
| [Anthropic structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) | Focused complete section read | Native schema constraints, injected instructions, refusal and truncation exceptions |
| [OpenAI Responses create reference](https://developers.openai.com/api/reference/cli/resources/responses/methods/create) | Focused field reads | Response statuses, incomplete details, automatic truncation, usage, and tool-call ceiling |
| [Gemini structured output](https://ai.google.dev/gemini-api/docs/structured-output) | Focused complete JSON-schema-support and limitations sections | Supported subset and complexity limits |
| [Gemini GenerateContent reference](https://ai.google.dev/api/generate-content) | Focused field reads | Finish reasons, function-call correlation, and provider/server tool shapes |
| [MCP 2025-11-25 schema](https://modelcontextprotocol.io/specification/2025-11-25/schema) | Focused `Tool` and initialization reads | Protocol negotiation versus tool metadata |
| [OpenTelemetry GenAI attributes](https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/) | Focused registry read | Requested/response model distinction and moved/deprecated registry status |
| [RFC 8259](https://www.rfc-editor.org/rfc/rfc8259.html) | Focused complete object-name section | Duplicate-key interoperability risk |

This baseline proves only that the specification addresses the cited current seams as accessed on 2026-09-06. It does not substitute for the live profile proofs or the implementation evidence required for adoption.

## 18. Known risks retained for proving

- The three providers expose materially different API families; a profile can accidentally hide semantic mismatch behind common names.
- Usage and billing may arrive late, be absent, or differ across streaming and asynchronous responses.
- Gateways and SDKs can add retry, truncation, caching, or model substitution outside the application's direct observation.
- Provider-managed tools can cross side-effect boundaries without application-level dispatch evidence.
- Content-addressed request evidence can still be operationally irretrievable if retention is not tested.
- A consumer may appear portable while carrying provider branches outside the declared adapter seam.
- The current empirical floor is zero v2 implementations and zero v2 live cross-provider consumers; therefore no adoption inference is permitted from this design alone.

These are proof targets, not reasons to soften the contract.

## 19. Controlled-consumer evidence limit

The ratified fulfillment-recovery consumer is a purpose-built executable application with a fabricated business world. Its proof can establish behavior in that declared population and the usability of the candidate skill in the observed build. It does not establish fleet-wide operational reliability, broad user validation, or accuracy on untested tasks. Provider-portability claims remain bound to the exact proved profiles, selected configurations, and retained evidence. Consumer business rules and accuracy rubrics belong to this proving application and are not promoted into the portable Agent Code contract.
