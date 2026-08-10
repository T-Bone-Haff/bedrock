# File: docs/adr/ADR-001-portable-core-and-surface-adapter-architecture.md
# Author: Tad Haffey — Executive Architect, Haffey Enterprises LLC; Codex — drafting agent
# Created: 2026-08-09
# Description: ADR-001 — Portable core, orchestration, and surface adapter architecture. Bedrock separates portable actor contracts from workflow execution and host integrations.

# ADR-001: Bedrock uses portable actor contracts with capability-gated orchestration and surface adapters

| Field | Value |
|---|---|
| **Document ID** | ADR-001 |
| **Status** | PROPOSED |
| **Version** | 0.1.0 |
| **Date** | 2026-08-09 |
| **Authors** | Tad Haffey (decision owner); Codex (drafting agent) |
| **Supersedes** | None — first Bedrock architecture principle. |

---

## 1. Context

Bedrock currently ships thirteen skills through a Claude plugin manifest. The skill bodies mix portable engineering invariants, Haffey-specific operating choices, host assumptions, and references to capabilities that are not present in the distributable package. Some skills assume sibling skills or private execution machinery, while package prose claims self-containment. Routing is validated for the current catalog, but the package does not yet define a cross-host capability, authority, dependency, output, or lifecycle contract.

Bedrock must settle those boundaries before substantive skill rewrites. Otherwise each correction can independently choose what is portable, what is house policy, what a host must provide, which artifact wins on conflict, and whether a skill describes one reasoning act or an entire durable workflow. The existing design-review machinery exposes that last ambiguity: a review method has grown into an executable author-review-ratification loop and is intended to become the first orchestration specimen for SOFIA and HEX. This record ends that architectural indecision without discarding the specimen.

## 2. Decision

Bedrock is a versioned, Agent Skills-compatible portable skill corpus whose actor and governance semantics are owned by a host-neutral core, composed by separately versioned workflow recipes, executed by capability-gated orchestration kernels, and exposed through thin surface adapters.

### 2.1 Product responsibility

The portable core owns:

- skill identity, task boundary, and routing precedence;
- normative engineering invariants and explicit profile seams;
- input, output, evidence, escalation, refusal, and failure contracts;
- shared vocabulary and schemas where mechanical identity is required;
- bundled relative resources, fixtures, and contract-critical rationale; and
- lifecycle status and compatibility requirements for each skill.

The portable core does not own host authentication, user-interface behavior, repository permissions, runtime agent topology, durable workflow state, scheduling, retries, command registration, hook installation, or marketplace transport. Those concerns belong to orchestration kernels, workflow recipes, surface adapters, or other declared external capabilities.

Bedrock does not claim complete ownership of every engineering or operational domain. A coverage map names owned capabilities, explicit handoffs, and unowned or deferred domains. An absent owner is reported as a gap rather than covered by implication.

### 2.2 Core and adapter boundary

Canonical skill content uses portable frontmatter, relative resource paths, and vendor-neutral contracts. Codex/OpenAI, Claude, and Cursor integrations are adapters over that core. An adapter may add host-native discovery, commands, hooks, agents, permissions, or user-interface affordances, but it may not silently change a skill's normative meaning, routing boundary, required evidence, or failure semantics.

Host-specific enhancement is conditional on a declared capability. When an optional capability is absent, the adapter follows the declared degraded behavior. When a capability is required for the requested outcome, the adapter fails before work begins with the missing capability, affected operation, and available alternatives. It does not emulate success or claim evidence it could not produce.

Model Context Protocol is the preferred portable boundary for executable integrations. A non-MCP integration must expose an equivalent versioned capability and failure contract.

### 2.3 Authority and dependency

Every normative rule has one owner. Other surfaces point to that owner, generate a checked carrier, or carry a deliberately bounded contextual restatement. Hand-maintained duplicate authority is non-conforming.

Every reusable clause is classified by authority:

- **normative contract** — a requirement owned by one declared authority and usable for conformance;
- **profile** — a named, versioned choice that binds only consumers selecting that profile;
- **heuristic** — defeasible guidance labeled with its decision boundary and never sufficient by itself to declare non-conformance;
- **example** — an illustration that cannot widen or override the governing contract; or
- **generated carrier** — runtime-ready context derived from a declared source and checked for drift.

Optional guidance is a heuristic or profile, never an unlabeled weaker form of normative text. When classifications conflict, the normative owner wins; when ownership is unresolved, execution stops for disposition.

A skill's core task must not depend on another skill being loaded unless the dependency is explicit, versioned, machine-readable, and checked before execution. Bundled references and templates use relative paths and ship with the owning skill. External repositories, environment variables, command-line tools, services, models, and host capabilities are declared with version requirements, optionality, detection, and failure behavior.

Conflicts resolve through declared ownership and precedence. If two applicable authorities have no declared ordering or materially disagree, execution stops for disposition; an adapter may not choose silently.

### 2.4 Skill identity and routing

The thirteen current skill names remain stable through the contract migration. Each retains one primary job. Internal progressive-disclosure references may split without creating a new routable skill. A new, merged, renamed, or retired skill requires evidence that the routing or task boundary improves enough to justify migration cost.

Routing is determined first by requested operation, then by subject domain:

1. authoring, reviewing, diagnosing, testing, and executing are distinct operations;
2. the operation-owning skill is primary;
3. a domain skill may supply an explicitly allowed secondary overlay; and
4. unresolved overlap stops with the competing routes and the missing discriminator.

The catalog-wide precedence and per-skill dispositions are defined in the repository's skill architecture record.

Routing metadata and progressively disclosed content are governed by evidence budgets. Each routable description and the package aggregate have pre-registered size and confusion thresholds; skill bodies and templates load only the material needed for the selected operation. The architecture fixes that form now. Numeric thresholds remain held until routing, context-cost, cold-task, and completion evidence calibrate them.

### 2.5 Interaction and evidence contracts

Every skill declares:

- accepted task class and required inputs;
- produced artifact or result shape;
- evidence required for claims of completion or convergence;
- authority reserved to the operator or an external system;
- refusal and escalation conditions;
- required and optional capabilities; and
- behavior when a required input, authority, or capability is unavailable.

Prompt text is advisory unless an executable boundary enforces it. A skill must label advisory controls honestly and must not describe a prompt-only stop, approval, scope, or safety instruction as mechanically enforced.

### 2.6 Safety floor

No profile or adapter may weaken the package safety floor. The floor includes controlled sensitive-content capture, separation of untrusted code from trusted credentials, honest secret/state behavior, token audience and delegation controls, cookie/CSRF coupling, pinned executable dependencies, and evidence-backed artifact buildability. An affected operation is blocked when the safety floor cannot be satisfied.

### 2.7 Versioning and compatibility

The portable core contract, each adapter contract, and the distributable package have distinct version identities. A generated compatibility manifest maps their compatible ranges, required capabilities, optional enhancements, degraded behavior, and verified host versions.

A portable-core major change includes removing or renaming a skill, changing an established routing owner, breaking a declared input/output/evidence contract, changing authority or precedence, or increasing required capabilities without a compatible degraded path. Adapter-only host changes follow the adapter's version lifecycle.

The distributable package takes a major version when it includes a portable-core major, removes or renames a public skill, breaks installation or explicit invocation on a supported host, removes a supported host range, or makes a previously optional adapter capability mandatory without a compatible degraded path. Compatible core additions and adapter enhancements do not force a package major. The package version describes the aggregate release and does not substitute for either contract version.

Prompt-generation format has its own version and provenance. Generated carriers record generator version, source contract version, and source digest. Regeneration alone does not redefine the portable contract; a generated-format incompatibility is versioned at the affected generator or adapter boundary.

### 2.8 Actor, recipe, kernel, and control-plane boundary

Bedrock skills define bounded task and actor contracts. An actor contract states the reasoning responsibility, authority, inputs, outputs, evidence, refusal, and escalation behavior for one operation. A routable skill may supply one actor contract or coordinate a bounded manual operation, but its prose is not a durable workflow engine.

A workflow recipe composes actor contracts into a versioned state machine. The recipe owns the permitted transitions, artifact and authority references, admission rules, completion predicate, operator gates, and assurance profiles for that workflow. A recipe may reference Bedrock contracts, but it may not copy them into a second normative authority.

An orchestration kernel owns durable execution: workflow state, actor invocation, validated structured transitions, event and evidence persistence, budgets, retries, scheduling, resumability, and deterministic gate evaluation. Actors propose drafts, findings, classifications, and actions; the kernel admits outputs and advances state. Free-form conversation among agents is not the workflow state or the transition mechanism.

A control plane selects and composes workflows, presents their state, and carries operator decisions back to a halted workflow. Within the Haffey architecture, SOFIA is the orchestration-kernel and workflow-recipe owner, `agent-loop` is the first reference implementation evolving through the decision-record lifecycle, and HEX is the control plane that selects, composes, observes, and operates SOFIA workflows.

The first reference workflow covers the decision-record lifecycle rather than review alone: deliberate, author, review, correct, ratify when a new decision is required, validate, and land. Stance-isolated design review remains a subloop. The operator is the authority for unresolved decisions and release gates, not the courier of routine artifacts and feedback between actors.

Three assurance profiles preserve proportionality:

1. direct review performs one authority-cited adversarial read and does not claim mechanical convergence;
2. multi-perspective review runs isolated review actors and an explicit aggregation policy but does not claim durable convergence without the kernel; and
3. runner-backed convergence uses a declared recipe and executable kernel and is the only profile that may emit a mechanically established convergence result.

The SOFIA and HEX roles do not make either system a hidden dependency of Bedrock's portable core. A consumer without the required kernel capability may use a supported lower-assurance profile or fail before execution; it may not emulate runner-backed success.

### 2.9 Rebinding contract

A rebind is required only when a changed stack, host, authority corpus, doctype family, or execution capability changes part of the governing contract rather than selecting another already-declared profile. Every rebind produces:

1. the invariants preserved unchanged;
2. the axes and assumptions that changed;
3. the replacement authority and responsibility mapping;
4. migration and compatibility treatment;
5. exceptions, degraded modes, and refusal boundaries; and
6. proving evidence for the rebound contract.

A different configuration within an existing profile is not a rebind. A document that merely says "rebind" without these outputs is incomplete.

## 3. Rationale

The portable-core boundary lets one engineering contract survive host changes while keeping host-native affordances honest. It prevents the weakest host from limiting every surface and prevents the richest host from silently becoming the product definition. Capability gates turn missing integrations into inspectable states instead of hidden assumptions.

Separating actor, recipe, kernel, control-plane, adapter, and package authority also makes correction tractable. A house stack choice can change without reopening a provider-neutral safety invariant; a workflow can change scheduling or model allocation without silently changing an actor contract; a host manifest can evolve without rewriting skill semantics; and a conflict can be traced to one owner. Stable skill names preserve the routing behavior already demonstrated while content and execution machinery are reorganized behind those identities.

## 4. Alternatives Considered

### 4.1 One Claude-specific plugin as the canonical product

This would match the only currently shipped manifest and minimize near-term packaging work. It was rejected because host mechanics, house policy, and engineering invariants would remain inseparable; Codex and Cursor support would require either false compatibility claims or later architectural extraction.

### 4.2 Independent first-class forks for each host

Each host could optimize its own skill bodies, manifests, commands, and permission model. This was rejected because normative fixes and safety rules would have multiple owners, cross-host routing would drift, and no mechanical answer would exist when forks disagreed.

### 4.3 A universal bundle that assumes every integration exists

One bundle could describe all hooks, agents, commands, runners, and user-interface features and let hosts ignore unsupported instructions. This was rejected because ignored instructions create false completion and enforcement claims, while optional behavior becomes impossible to test or version coherently.

### 4.4 Portable core with implicit, best-effort integrations

The core could remain vendor-neutral while adapters probe opportunistically for tools and degrade informally. This was rejected because consumers could not distinguish a supported degraded mode from accidental under-execution, and evidence produced by different hosts would not be comparable.

### 4.5 Put the complete agent loop inside `design-review-loop`

The skill could own reviewer and author prompts, durable state, arbitration, convergence, cost policy, replay, and unattended operation as one package. This was rejected because a single skill would become both normative actor authority and runtime implementation, while the reusable orchestration lessons could not serve later authoring, coding, validation, and landing loops without duplication.

### 4.6 Let autonomous agents coordinate through free-form conversation

Agents could hand prose directly to one another until they collectively judge the work complete. This was rejected because conversation would become unversioned workflow state, completion would return to model judgment, failures would not resume deterministically, and the operator would have no durable decision or evidence seam.

## 5. Consequences

### 5.1 Positive

- One authority governs skill semantics across supported hosts.
- Host-native features remain available without becoming undeclared requirements.
- Missing capabilities and conflicts have deterministic failure behavior.
- Skill corrections can separate portable invariants from Haffey profiles.
- SOFIA can reuse one durable kernel across multiple workflow recipes while `agent-loop` remains a concrete proving specimen.
- HEX can remove routine operator relay without absorbing the domain authority of the actors it dispatches.
- Compatibility, evidence, and release decisions become mechanically inspectable.

### 5.2 Constraints imposed

- Adapters cannot carry independent normative copies of the core.
- A private runner or tracker cannot load-bear on an installed skill's contract unless it is a declared, versioned, capability-gated dependency with exact unavailable behavior.
- Actor, recipe, kernel, control-plane, and adapter contracts cannot silently absorb one another's authority.
- Model allocation, draw count, retry, and budget changes are run-profile or kernel-policy changes unless they alter actor or recipe semantics.
- The operator remains the authority for unresolved decisions and release gates even when workflow execution is unattended.
- New top-level skills require routing and context evidence, not taxonomy preference.
- Claims of enforcement, convergence, safety, or completion require evidence from the declared capability path.
- A consumer release cannot precede cross-surface conformance and an explicit release decision.

### 5.3 Risks

- The adapter boundary may become ceremonial if no schema or parity check enforces it. The signal is an adapter-only normative clause or unexplained cross-host output difference.
- Stable skill names may preserve a poor boundary. Routing confusion and context-cost measurements are the revisit signal.
- Generalizing the kernel from one specimen may encode decision-record assumptions as universal workflow law. A second workflow family that cannot use a purported kernel primitive is the revisit signal.
- Recipe and actor versions may drift. A workflow whose pinned actor contracts cannot be resolved or whose semantics changed incompatibly is not executable.
- Capability declarations may become stale. A host-version mismatch or undeclared degraded path blocks release evidence.
- Layering can increase navigation cost. Cold-task completion time and unresolved-reference failures are the revisit signal.

## 6. Compliance

Compliance is currently partly aspirational. The repository validates current skill structure, routing fixtures, and clean installation, but it does not yet validate the full core/adapter contract.

Conformance will be enforced by:

- a machine-readable skill, authority, dependency, capability, and compatibility registry;
- versioned workflow-recipe and actor-binding schemas with deterministic transition validation;
- generated-or-checked adapter carriers;
- shared positive, negative, overlap, degraded-mode, and unavailable-capability fixtures;
- duplicate-authority, path, package, and vocabulary drift checks; and
- cold acceptance on every supported surface before release.

Until those mechanisms land, changes are checked against this record and the skill architecture record during design review. A claim that depends on an unimplemented mechanism remains conditional.

## 7. Cross-References

- [Skill architecture and routing contract](../architecture/skill-architecture.md)
- [Product coverage map](../architecture/coverage-map.md)
- [Migration and compatibility notes](../architecture/migration-compatibility.md)
- [Wave 1 validation evidence](../evidence/heb-108/validation-results.md)

## 8. Change Log

| Version | Date | Ticket | Change |
|---|---|---|---|
| 0.1.0 | 2026-08-09 | HEB-111 | Initial portable-core, authority, coverage, rebind, orchestration, versioning, and capability-gated adapter architecture draft. |

<!-- STANDING — do not delete. Append new rows at the TOP. 0.X.0 for
     PROPOSED-phase revisions; 1.0.0 at first ACCEPTED. ONE LINE per row:
     version, date, ticket, and a summary of at most 200 characters — the
     deliberation goes to the ticket. Prior rows are frozen; the row for the
     version you are currently authoring is amended in place until that
     version commits. -->
