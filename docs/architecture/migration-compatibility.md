# Bedrock portable-core migration and compatibility notes

**Status:** PROPOSED
**Version:** 0.1.0
**Date:** 2026-08-09
**Governing principle:** [ADR-001](../adr/ADR-001-portable-core-and-surface-adapter-architecture.md)

**Coverage boundary:** [Bedrock product coverage map](coverage-map.md)

## 1. Current state

The current distributable is a Claude plugin with thirteen skill directories and one package version. The repository has deterministic structure and routing validation plus a clean-install smoke test. It does not yet ship separate Codex/OpenAI or Cursor adapters, a capability registry, an authority registry, independent core/adapter versions, or a generated compatibility matrix.

The current skill names are the compatibility anchors for this migration. Existing names and explicit invocations remain valid while content is separated into portable contracts and profiles.

## 2. Target compatibility model

The generated compatibility manifest will identify:

| Identity | Meaning |
|---|---|
| Core contract version | Version of portable skill identity, routing, authority, input/output/evidence, and safety semantics. |
| Actor contract version | Version of the bounded operation a recipe invokes, including its authority and result schema. |
| Workflow recipe version | Version of actor bindings, transitions, artifacts, operator gates, assurance profiles, and completion semantics. |
| Kernel capability and version | Durable-execution features and version required by the recipe. |
| Adapter name and version | Version of one host's registration, capability mapping, enhancements, permissions, and degraded behavior. |
| Package version | Version of the distributable aggregate. |
| Generator format version | Version of generated carrier structure, independent of prompt wording and package identity. |
| Verified host range | Host versions exercised by retained conformance evidence. |
| Required capabilities | Capabilities whose absence blocks the named operation. |
| Optional enhancements | Host features that improve execution without changing core semantics. |
| Degraded behavior | Exact supported behavior when an optional capability is absent. |

Compatibility is asserted only for combinations present in the generated matrix and backed by retained evidence.

## 3. Migration sequence

1. Accept the portable-core architecture and catalog decisions.
2. Define machine-readable skill, authority, dependency, capability, and compatibility schemas.
3. Define workflow-recipe and kernel-capability schemas separately from skill and actor contracts.
4. Classify existing clauses as portable invariant, actor contract, workflow recipe, kernel policy/mechanism, Haffey profile, host adapter, contextual carrier, or defect.
5. Correct the skill clusters in the ratified dependency order, populating and verifying every skill's interaction-contract fields before its cluster gate, without changing public names unless the architecture is amended.
6. Split `design-review-loop`'s portable review semantics from SOFIA's decision-record lifecycle recipe and runner machinery while preserving explicit-invocation compatibility.
7. Add Codex/OpenAI, Claude, and Cursor adapters with explicit capability gates and generated-or-checked carriers.
8. Run shared structural, routing, behavior, degraded-mode, permission, reference, output, recipe-transition, and kernel-resumption fixtures across supported hosts.
9. Build a release candidate only after package governance is complete.
10. Perform cold acceptance and make an explicit consumer release decision.

No migration step authorizes a consumer release by itself.

## 4. Breaking-change treatment

The following require a portable-core major version and migration notes:

- removing or renaming a skill;
- changing the primary route for an established task class;
- breaking required inputs, outputs, evidence, refusal, or escalation behavior;
- changing normative authority or conflict precedence;
- making an optional capability required without a compatible degraded path;
- moving an established direct operation behind a required orchestration kernel without a compatible direct profile; or
- weakening or materially changing the safety floor.

The distributable package also takes a major version when it carries any portable-core major or independently breaks installation, explicit invocation, or the supported-host contract. An adapter-only incompatible change takes an adapter major and a package major when that adapter is part of the distribution's supported contract.

A host-only registration or enhancement change is versioned at the adapter boundary unless it changes portable semantics. A package release carries the compatible core and adapter identities; it does not collapse them into one version claim.

## 5. Prompt and generated-carrier treatment

Generated prompts and host carriers record the generator format version, source contract version, and source digest. Prompt wording can change without a core major version when routing, authority, interaction, evidence, and safety semantics remain compatible. A carrier-format break is versioned at the generator or affected adapter boundary.

Generated files are not independent authority. They are reproduced from or checked against their declared source, and drift blocks compatibility evidence.

## 6. Design-review and decision-record workflow transition

The `design-review-loop` name remains a compatibility anchor during Wave 2. Its internal monolith is separated without claiming that the capability is retired:

1. Bedrock retains the portable review, finding, decision-escalation, and assurance-profile contracts.
2. The SOFIA decision-record lifecycle recipe composes deliberation, authoring, review, correction, operator ratification, validation, and landing actors.
3. The SOFIA kernel owns durable state, invocation, evidence, budgets, retries, resumability, and deterministic transitions.
4. `agent-loop` remains the first reference implementation and proving specimen; reusable kernel primitives are extracted from observed needs rather than generalized from naming alone.
5. HEX selects and composes workflows and presents asynchronous operator dockets without becoming a second authority for actor or recipe semantics.

Direct review and multi-perspective review remain supported lower-assurance profiles. Existing consumers without the SOFIA kernel are not silently upgraded to runner-backed convergence, and they may not claim it. A future rename or split of the public skill identity requires routing and migration evidence under the governing ADR.

Prompt generations, repeated draws, calibration, replay, cost attribution, run dispositions, and cold instrument audits move to the SOFIA recipe/kernel operating surface unless a rule is independently established as a portable actor safety or evidence invariant. `agent-code` and `testing` govern implementation and evaluation discipline; they do not become runtime owners.

## 7. Current consumer impact

- No skill is removed, renamed, or merged in the proposed Wave 2 contract.
- Existing `design-review-loop` invocations remain valid while its portable actor contract and SOFIA execution binding are separated.
- The Claude plugin remains the only implemented distribution surface until adapters land.
- SOFIA and HEX are designated house orchestration consumers, not hidden requirements of every Bedrock installation.
- Claims of Codex/OpenAI or Cursor support remain future and conditional until their adapter and cold-acceptance evidence exist.
- The existing package version is not retroactively treated as a core-contract or adapter version.
- The next package version is derived at landing; this record does not pre-claim it.
- Consumer rollout remains blocked pending cross-surface acceptance and an explicit release decision.

## 8. Change log

| Version | Date | Ticket | Change |
|---|---|---|---|
| 0.1.0 | 2026-08-09 | HEB-111 | Initial migration, coverage, actor/recipe/kernel compatibility, rebind/package-major rules, and consumer impact. |
