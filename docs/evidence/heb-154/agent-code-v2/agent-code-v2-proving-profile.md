# Agent Code 2.0 proving profile

**Profile id:** ACV2-PROVING  
**Version:** `1.1.0`  
**Status:** preregistered for the `PROVING` lifecycle state  
**Ratification date:** 2026-09-06 (America/New_York)  
**Subject:** `ACV2-STANDARD-AMENDMENT`

**Consumer amendment ratified:** 2026-09-10 (America/New_York); authority: `agent-code-v2-ratification-record.md`, consumer proving amendment. Original contract fixture expectations remain frozen. The [public scenario-and-oracle draft](scenario-and-oracle-pack.md) instantiates proposed consumer records; the complete campaign, including hidden evaluation instances and exact execution bindings, remains unfrozen.

## 1. Proof claim and stop rule

This profile defines the evidence required before Agent Code 2.0 may claim:

> Provider-neutral, fail-closed LLM-call and tool-loop behavior across the declared Anthropic, OpenAI, and Gemini profiles.

The present empirical floor is zero Agent Code 2.0 implementations, zero v2 live provider-profile runs, and zero v2 two-provider consumer demonstrations. Ratification of the design does not raise that floor.

If any required subject, authority, credential, capability, provider run, consumer run, detector control, or retained artifact is unavailable, the claim result is `UNAVAILABLE`. No required gate can be waived inside this proving profile. A narrower claim requires a separately ratified profile.

## 2. Evidence identity and layout

Implementation work MUST receive a repository ticket before it begins. Evidence MUST be retained under:

`docs/evidence/<ticket>/agent-code-v2/`

The evidence root MUST contain:

- `manifest.yaml` — exact subject commit/tree, dirty-state declaration, commands, environments, dependency lock digests, provider profile identities, fixture population, and artifact digests;
- `obligations.yaml` — every `AC2-*` obligation mapped to detector, control, population, result, and digest;
- `deterministic/` — schema, validator, fixture, test, package, trigger, and routing results;
- `live/anthropic/`, `live/openai/`, and `live/gemini/` — sanitized request/evidence records and run manifests;
- `consumer/` — same-interface two-provider proof;
- `review/` — independent review, finding register, and dispositions; and
- `acceptance/` — operator decision, landing proof, and cold acceptance.

Secrets and raw content MUST NOT enter retained evidence. Evidence records retain digests and classified metadata unless a separately authorized capture policy permits content.

Every command MUST record exit status and complete output. A tool cap, truncated output, partial fixture selection, or missing population member makes that result partial and ineligible for a whole-population claim.

## 3. Gate matrix

| Gate | Required obligation IDs | Pass predicate |
|---|---|---|
| G1 Spec integrity | AC2-provenance-total | All normative external claims have authority, scope, access date, and current/expired disposition; every ratified design decision maps to at least one normative clause and test. |
| G2 Structural schemas | AC2-schema-positive, AC2-schema-negative | Draft 2020-12 schema validation agrees with every preregistered structural fixture; schemas and fixtures are closed and digest-bound. |
| G3 Semantic validator | AC2-budget-joint, AC2-terminal-truth, AC2-side-effect-unknown, AC2-salvage-bounds, AC2-context-integrity | The independent deterministic semantic validator agrees with every preregistered behavior fixture and rejects every counterfactual. |
| G4 Provider profiles | AC2-profile-complete, AC2-profile-live | All three profiles validate, all required mapping cells are resolved, and each exact profile passes its live population. |
| G5 Telemetry | AC2-otel-pin | Mapping is pinned, deterministic fixtures pass, and a known-drift control makes the detector fail. |
| G6 Routing | AC2-routing | Complete routing population passes current PR policy; retained release population passes the repository release policy with zero excluded selections. |
| G7 Consumer build, portability, and accuracy | AC2-consumer | The named consumer passes separate build-use, runtime-conformance, and outcome-accuracy verdicts; the complete workflow executes through two providers and a mixed-provider configuration with no portable-semantic weakening. |
| G8 Independent reproduction | AC2-cold-review | A reviewer starting from retained artifacts reproduces all deterministic results and verifies live/consumer evidence identity without author narration. |

All deterministic schema and semantic fixture cases have a threshold of 100%. The current repository release routing thresholds remain governed by `validation/eval-policy.yaml`; this profile does not silently redefine them.

## 4. Preregistered fixture population

The normative population is every case below. Case removal, expectation change, or weakening after candidate results are known requires an explicit amendment with rationale and operator ratification. New cases MAY be added when they do not hide failures in the frozen population.

Each negative case MUST have a paired positive control differing only in the named defect where practical. Each detector whose pass result is silence MUST also be run against a known-dirty control that makes it fire. Fixture files MUST embed the case id and expected detector/reason code.

### 4.1 Valid behavior cases

| Case | Expected result |
|---|---|
| AC2-V01-model-only-success | One completed model attempt, no tool attempt, valid whole parse, success predicate true: accept. |
| AC2-V02-one-model-one-tool | One completed model attempt and one correlated read-only tool attempt: accept. This is the regression control for the current false rejection. |
| AC2-V03-native-structured-success | Profile-supported native structured value with complete provider status: accept as `native`. |
| AC2-V04-outer-fence-load-bearing | Exactly one declared outer fence consuming all non-whitespace bytes: accept as `outer_fence`. |
| AC2-V05-best-effort-one-candidate | Bounded best-effort scan finds exactly one schema-valid candidate: accept as `best_effort_embedded`. |
| AC2-V06-refusal | Native refusal mapped to `refused`, no fabricated parse result: accept evidence, invocation not successful. |
| AC2-V07-context-exhausted | Native token/context limit mapped to `context_exhausted`: accept evidence, invocation not successful. |
| AC2-V08-partial-success | Declared partial result with failed items recorded and success predicate false for full completion: accept. |
| AC2-V09-unknown-effect | Timed-out side-effect attempt ends `outcome_unknown` and requires reconciliation: accept. |
| AC2-V10-reconciled-safe-retry | Reconciliation proves no effect or safe replay before retry: accept. |
| AC2-V11-provider-managed-tool | Provider-managed tool call records provider correlation, observed facts, and observation limits: accept. |
| AC2-V12-unknown-usage | Missing provider usage remains explicit `unknown` and blocks any predicate requiring known spend/tokens: accept. |
| AC2-V13-hosted-prompt-immutable | Version-pinned, content-addressed hosted prompt with resolved-byte digest and retrieval evidence: accept. |
| AC2-V14-namespaced-extension | Closed record with non-overriding reverse-domain extension data: accept. |

### 4.2 Invalid and counterfactual behavior cases

| Case | Expected rejection |
|---|---|
| AC2-I01-success-zero-model-attempts | `succeeded` cannot be established without a model attempt. This is the known false-positive control. |
| AC2-I02-success-after-parse-failed | Terminal success contradicts failed parse/success predicate. |
| AC2-I03-duplicate-model-attempt-id | Model attempt identity is not unique. |
| AC2-I04-duplicate-tool-attempt-id | Tool attempt identity is not unique. |
| AC2-I05-orphan-tool-result | Tool result lacks exactly one matching request. |
| AC2-I06-input-token-budget-exceeded | Used input tokens exceed limit. |
| AC2-I07-output-token-budget-exceeded | Used output tokens exceed limit. |
| AC2-I08-spend-budget-exceeded | Known spend exceeds limit. |
| AC2-I09-model-attempt-budget-exceeded | Physical model attempts exceed limit, including SDK/provider retries. |
| AC2-I10-tool-iteration-budget-exceeded | Tool iterations exceed limit. |
| AC2-I11-deadline-exceeded | End/dispatch evidence crosses the aggregate deadline. |
| AC2-I12-concurrency-exceeded | Concurrent child operations exceed the declared limit. |
| AC2-I13-tool-when-max-zero | Any tool dispatch violates a zero tool-iteration limit. |
| AC2-I14-duplicate-json-keys | Duplicate object name is rejected before lossy deserialization. |
| AC2-I15-malformed-nested-outer | Malformed whole payload cannot be rescued by extracting a nested valid object on a load-bearing path. |
| AC2-I16-response-oversized | Response exceeds the declared byte limit. |
| AC2-I17-response-too-deep | JSON exceeds the declared nesting limit. |
| AC2-I18-multiple-valid-candidates | Best-effort scan finds more than one schema-valid candidate and is ambiguous. |
| AC2-I19-embedded-load-bearing | Arbitrary embedded scanning is forbidden for a load-bearing call. |
| AC2-I20-fence-plus-prose | A fence not consuming the entire non-whitespace response is not an outer fence. |
| AC2-I21-refusal-as-success | Native refusal cannot normalize to `succeeded`. |
| AC2-I22-truncation-as-success | Truncated/incomplete generation cannot normalize to `succeeded` unless a separately declared partial predicate is satisfied. |
| AC2-I23-unknown-provider-status-as-success | Unmapped native status fails closed. |
| AC2-I24-hidden-sdk-retry | Unobservable physical retry makes budget evidence nonconforming. |
| AC2-I25-provider-managed-tool-unaccounted | Provider-managed tool work omitted from attempt/effect evidence is invalid. |
| AC2-I26-stream-interrupted-before-final-usage | Interruption cannot fabricate final usage or success. |
| AC2-I27-side-effect-timeout-as-tool-failed | Potentially committed effect cannot be reduced to an ordinary retryable failure. |
| AC2-I28-auto-retry-unknown-effect | Retry before reconciliation is prohibited. |
| AC2-I29-silent-context-truncation | Dropped request material without a manifest transformation is invalid. |
| AC2-I30-unversioned-compaction | Compaction/summarization without transformer identity/version/digest is invalid. |
| AC2-I31-request-response-model-collapsed | One field cannot stand for both requested and returned model. |
| AC2-I32-unknown-usage-as-zero | Unknown tokens or spend cannot be encoded as known zero. |
| AC2-I33-spend-without-currency | Spend accounting lacks currency. |
| AC2-I34-spend-without-pricing-identity | Governed spend lacks immutable price-table identity and rounding rule. |
| AC2-I35-unsupported-profile-silent-fallback | Capability failure cannot silently select a different provider/profile. |
| AC2-I36-raw-content-unclassified | Raw prompt/completion/tool content is captured without the required policy. |
| AC2-I37-mutable-hosted-prompt | Mutable hosted alias lacks immutable reference and resolved-byte digest. |
| AC2-I38-request-order-missing | Request manifest does not preserve exact ordering. |
| AC2-I39-extension-not-namespaced | Extension key violates namespace rule. |
| AC2-I40-extension-overrides-portable | Extension data attempts to change portable meaning. |
| AC2-I41-schema-allows-undeclared-property | A closed-schema negative control is accepted. |
| AC2-I42-profile-prose-only | A provider profile without a schema-valid authoritative record is nonconforming. |

### 4.3 Provider-profile structural cases

For each of Anthropic, OpenAI, and Gemini, fixtures MUST cover:

- complete current profile: accept;
- missing SDK/API identity: reject;
- unresolved required capability: reject adoption eligibility;
- unknown native terminal status without fail-closed mapping: reject;
- missing retry accounting: reject;
- missing requested/returned model mapping: reject;
- missing usage-unavailable mapping: reject;
- unpinned OpenTelemetry mapping: reject;
- expired authority access/review date: accept structurally but mark live/adoption proof stale; and
- unsupported feature with explicit unavailable behavior: accept profile, block any claim depending on that feature.

## 5. Deterministic proof procedure

All commands run from the repository root in the repository's declared dependency environment. The evidence manifest records the exact interpreter, dependency lock digest, OS/architecture, commit, and dirty state.

The candidate MUST provide commands equivalent to:

```text
python scripts/validate_agent_review_contracts.py
python scripts/validate_plugin.py plugins/bedrock
python -m unittest tests.test_agent_review_contracts
python -m unittest discover -s tests
python scripts/validate_rule_trigger_audit.py
python scripts/run_routing_evals.py --profile pr --output docs/evidence/<ticket>/agent-code-v2/deterministic/routing-pr.json
python scripts/run_routing_evals.py --profile release --output docs/evidence/<ticket>/agent-code-v2/deterministic/routing-release.json
```

Exact supported CLI syntax MUST be taken from the candidate scripts at implementation time; if it differs, the manifest records the real invocation. No command may select only the new fixtures while claiming the whole registry or test suite.

In addition, the proving harness MUST:

1. validate every schema against its metaschema;
2. enumerate the complete registered fixture population and compare it to the files on disk in both directions;
3. run structural and semantic validators independently;
4. mutate each valid control into its paired invalid case and show the named detector fires;
5. run a known-clean/known-dirty control for every silence-based detector;
6. prove deterministic results are byte-stable or explain and normalize only declared volatile fields; and
7. emit obligation results mechanically from test outcomes, never hand-authored booleans.

## 6. Live provider proof

Live runs require operator-approved credentials, region/project/account selection, and aggregate monetary/token budgets. Credentials are consumed from the environment and never retained. The live harness MUST disable recording of raw sensitive content and use synthetic, non-sensitive prompts and tools.

Each exact profile identity MUST run the following complete population:

| Live case | Required observation |
|---|---|
| LP01-basic-structured | Native structured result validates and records requested/returned model plus profile digest. |
| LP02-tool-round-trip | Client-managed tool request/result correlates exactly once and terminates correctly. |
| LP03-refusal-or-policy | A safe test or provider-supported fixture produces the native refusal/policy shape; if the provider offers no safe deterministic trigger, authoritative captured provider fixture plus live capability detection is required and the limitation is explicit. |
| LP04-output-limit | Deliberate low output limit produces native incomplete/truncation mapping and cannot succeed. |
| LP05-stream-interruption | Controlled client interruption records incomplete/unknown usage and no false success. |
| LP06-retry-accounting | Retry is disabled or a controlled transient failure proves every physical attempt is counted. |
| LP07-usage-and-cache | Returned usage/cache/reasoning fields map accurately; unavailable fields remain unknown. |
| LP08-provider-tool | If provider-managed tools are supported by the selected profile, one safe read-only call proves accounting; otherwise the capability is explicitly unsupported and is not claimed. |
| LP09-model-identity | Requested and returned model fields are independently captured, including any alias resolution. |

All retained live records MUST validate against the candidate schemas and semantic validator. Provider availability is not inferred from documentation or another provider's run. A transient provider outage may be retried within the preregistered execution budget, but the final adoption decision remains unavailable until a fresh complete run exists.

## 7. Consumer build, execution, and accuracy proof

The named consumer is the fulfillment-recovery desk, owned by Tad Haffey. It is an executable representative application built specifically for proving with fabricated business data. Its Investigator, Recovery planner, and Correspondent agents make real model calls and use functioning application boundaries; its deterministic controller owns authorization, state, budgets, dispatch, reconciliation, and completion. The SOFIA workbench is not a construction dependency. A test-only adapter, scripted agent responses, or a retrospective checklist over prebuilt agents does not satisfy AC2-consumer.

The consumer MUST execute the same workload contract through one portable interface against two selected provider profiles. The proof population is:

1. model-only structured success;
2. one client-managed read-only tool round trip;
3. output-limit failure;
4. unknown-usage handling through a deterministic provider fixture or controlled adapter seam;
5. request-manifest ordering and digest verification; and
6. one profile-specific unsupported capability that fails before execution rather than silently falling back.

The interface, generation contract, output schema, semantic validator, terminal predicate, and evidence schema MUST be identical across both runs. Only profile-owned adapter configuration and provider-native fixtures may differ. A diff check MUST prove that no consumer branch weakens salvage, budget, side-effect, context, or terminal semantics for either provider.

### 7.1 Full use of the skill to build

Before consumer construction, bind the complete candidate skill bundle, applicable references and profiles, domain brief, authorized build scope, sibling standards, dependency identities, and allowed starting components. Retain an inventory and hashes. A fresh builder session MUST receive those artifacts without inheriting this authoring conversation or the hidden evaluation answers.

Observe the build from skill selection and complete reading through contract design, implementation, tests, actual execution, finding remediation, and reproducible handoff. Every applicable normative rule in the candidate bundle MUST map to its build decision, resulting artifact or code location, exercised trigger, detector and control, and retained result. Reading the skill or reproducing its vocabulary is insufficient. Unexercised requirements remain unproved; justified capability exclusions must be explicit and must not waive a required HEB-154 gate.

Record builder identity, inputs, interventions, clarifications, departures, first-evaluation results, and later corrections. A successful repair does not erase the original observation. Distinguish a skill ambiguity or omission from an implementation error against a clear rule and from a defective acceptance instrument. Any changed skill, prompt, contract, or implementation receives a new identity and an explicit affected-evidence retest. This proves observed build usability; it does not claim causal superiority to unaided construction without a comparative experiment.

### 7.2 Full execution of the resulting application

Execute the declared user path from intake through investigation, recovery selection, authorization, actual state changes, reconciliation when needed, and customer/operator output. Include successful completion, justified escalation, partial completion, cancellation/restart, concurrency, and uncertain-effect cases. A scenario's expected early terminal path is complete only when its declared obligations and output are satisfied; every case need not call every agent when a prior failure correctly blocks it.

Run the complete consumer workload through each selected provider configuration, then a mixed-provider configuration with fixed role assignments declared before evaluation. Compare correctness and portable semantics, not literal response equality. Preserve all three providers' separate live-profile obligations in section 6.

Record which boundaries are actual integrations, simulated business services, deterministic provider fixtures, or live provider behavior. Injected failures establish handling at their named seam; they cannot be reported as observations of a provider producing that failure. Every state-changing operation must affect inspectable application state rather than merely return a scripted success response.

### 7.3 Accuracy and useful completion

For each scenario, freeze authoritative world facts, information available to each actor, allowed state transitions, permitted outcome set, required facts and limitations in the final output, and the independent acceptance procedure. Ground truth belongs to the scenario custodian and evaluator, not to a model's account of what happened.

Evaluate separately: factual correctness and material completeness of investigation; feasibility and policy compliance of the selected recovery; actual correctness of state changes; and truthfulness, completeness, and usefulness of the final communication. Explicit uncertainty is required where the actor cannot know a fact. Accurate handling may require successful recovery, a justified escalation, or truthful partial/unknown status, according to the case. Always escalating fails the solvable-case criteria. Well-formed evidence for a wrong business answer fails accuracy.

Use deterministic checks for facts and effects that can be decided mechanically. Use a versioned, independently calibrated rubric for semantic judgment that cannot. Include known correct, known wrong, materially incomplete, and fluent-but-false controls. A separate model response alone is not independent proof; record evaluator identity, independence, calibration, and operator resolution of consequential uncertainty.

Preregister repeated-draw policy, exact populations and risk slices, metrics, acceptance thresholds, uncertainty reporting, model settings, retries, exclusions, and stopping rules before candidate evaluation. Include failed and null outputs in their declared denominators. Report first-attempt and recovered performance separately. No threshold is derived after seeing results; an aggregate score cannot hide a required invariant violation or a failed mandatory case. A finite controlled campaign establishes only its stated evidence scope.

### 7.4 Joint acceptance and evidence retention

AC2-consumer has separate result slots `build_use`, `runtime_conformance`, and `outcome_accuracy`. All must pass, together with the provider-configuration checks and the six original consumer cases above. A failed slot prevents passage; unavailable evidence makes that slot unavailable and prevents adoption. No weighted average or narrative can compensate for a failed or unavailable slot.

Retain the complete scenario-to-rule-to-build-to-execution-to-oracle trace. The independent reviewer receives the candidate and complete retained evaluation evidence after builder isolation has served its purpose. Hashes alone do not prove semantic accuracy. Before live evaluation, settle a content policy that permits the reviewer to inspect the synthetic inputs and relevant outputs, or an equally reproducible alternative; synthetic data does not automatically authorize raw-content capture. Without reviewable evidence, the accuracy claim is unavailable.

The scenario design and pending freeze items are in `consumer-proving-design.md`. That document's proposed case families are not the frozen physical fixture population. Existing contract fixtures, live-provider cases, routing gates, and independent review remain required in addition to the consumer application.

## 8. Provenance proof

`authority-provenance.yaml` MUST list every externally derived normative claim with:

- stable claim id;
- normative clause/obligation IDs;
- authority type and owner;
- exact URL or repository path;
- API/spec/version identity where available;
- access date and read depth;
- quoted-field or section locator without exceeding source-use limits;
- what the source proves and explicitly does not prove;
- freshness trigger; and
- current, stale, superseded, or unavailable disposition.

A deterministic check MUST fail when a normative external claim lacks a provenance entry, when a profile cites an authority outside the inventory, or when a time/version trigger marks a required claim stale. A known-orphan claim fixture is the mandatory dirty control.

## 9. Independent adversarial review

The reviewer MUST receive only the candidate tree and retained evidence root. The reviewer must not rely on this session's narrative. The review must attempt to falsify, at minimum:

- each of the seven ratified dispositions;
- all fourteen stable obligations;
- closed-schema enforcement;
- the known zero-attempt false positive and one-model/one-tool false negative;
- budget boundary arithmetic and unknown accounting;
- load-bearing salvage restrictions;
- uncertain side-effect retry prohibition;
- profile/API-family separation;
- request-manifest byte/order integrity;
- MCP protocol-versus-custom-version distinction;
- telemetry pinning and drift detection; and
- the claim that the consumer interface is provider-independent.

Every finding receives evidence, severity, owner, disposition, and retest. An open blocking finding prevents operator acceptance. A material residual limitation requires explicit operator ratification and corresponding claim narrowing.

## 10. Landing and cold acceptance

After operator acceptance, landing is one transaction:

1. rebase/reconcile the accepted candidate;
2. derive the package major under repository governance;
3. update registry, compatibility, changelog, authority inventory, and release evidence;
4. regenerate every `PACKAGE_IDENTITY.json` carrier from the manifest authority;
5. run the complete deterministic and release gate population on the exact landing tree;
6. install/reload on every declared host surface; and
7. retain a cold-session proof of package identity, 13-skill inventory unless intentionally changed, Agent Code contract `2.0.0`, portable core `3.0.0`, profile inventory, and evidence reachability.

The package is `ADOPTED` only after the cold result and rollout evidence are operator-ratified. A candidate version heading, passing local tests, or successful live provider call is not release proof by itself.
