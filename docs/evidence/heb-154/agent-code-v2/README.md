# HEB-154 — Agent Code 2.0

This is the canonical repository locus for the Agent Code 2.0 amendment and its proving work. Tad Haffey ratified this locus and the fulfillment-recovery consumer on 2026-09-10 (America/New_York). Linear descriptions and attachments are distribution/reference copies. They are not evidence custody.

## Authority and read order

1. [Ratification record](agent-code-v2-ratification-record.md) — original seven design dispositions and the ratified consumer/build/accuracy amendment.
2. [Standard amendment](agent-code-v2-standard-amendment.md) — normative Agent Code 2.0 target; includes the amended consumer obligation and controlled-evidence limit.
3. [Proving profile 1.1.0](agent-code-v2-proving-profile.md) — original frozen contract cases plus the amended, independently required build-use, runtime-conformance, and outcome-accuracy proof.
4. [Consumer proving design](consumer-proving-design.md) — ratified scope, operational interpretation, concrete scenario families, and outstanding freeze decisions.
5. [Business world and successful reference](business-world-and-reference-case.md) — all six W1–W6 business decisions ratified; the concrete FRD-01 data, oracle controls, and complete campaign remain pending freeze.
6. [Scenario-and-oracle pack](scenario-and-oracle-pack.md) — SP-1 public membership/values, SP-2 recovery/stopping and SP-3 oracle/result meaning ratified; execution bindings, evaluator implementation/calibration and freeze gates remain outstanding; includes a reproducible authoring-only integrity check.
7. [Execution-contract draft](execution-contract.md) — all four EC boundary decisions ratified: division of work/access, operation journal, state commits and event/evidence design; physical bindings remain proposed or pending; no implementation or cold-handoff claim.
8. [Physical runtime-binding draft](physical-runtime-binding.md) — PB-runtime's local Compose model, PB-transport's local HTTP/JSON, PB-persistence's PostgreSQL engine, its database-only credential condition and all five EN directions (access, route, scope, custody and lifecycle) accepted as design; exact enrollment, run-window/capacity bindings and verification remain pending; no provisioning, shared-server application, network attachment or execution authorized; not a launchable fixture or completed physical-schema pack.
9. [PostgreSQL persistence-contract draft](postgresql-persistence-contract.md) — all four PG designs accepted within scope: state/history, locking/commit/failure policy, generation-bound fencing/replay, and sealed correlated export with isolated restore. Exact physical bindings and execution remain open; the companion below now records all four WIRE designs accepted within scope. No implementation or runtime proof.
10. [Wire and identity draft](wire-and-identity-contract.md) — all four WIRE designs accepted within scope: strict envelope, physical/semantic identity, immutable complete sources and action-specific outcomes. A [machine-schema candidate](schemas/proposed/README.md) now supplies action/response schemas, source-body and derivation candidates, examples and advisory tests. SOURCE-order and SOURCE-events are separately accepted as presented; policy/error precedence, full source materialization and runtime validation remain pending. No schema-closure or runtime-evidence claim.

The proving design distinguishes ratified requirements from proposed details. It cannot override the ratification, standard, or proving profile. Product world rules and judgment rubrics belong to this consumer; they do not become portable Agent Code requirements.

## Current evidence state

This folder currently captures design authority and planning. No v2 implementation, frozen physical consumer corpus, live-provider run, agent-accuracy result, independent reproduction, or adoption result is established by these documents. The prospective evidence directories and manifests described in the proving profile must be populated by actual work and must never receive hand-authored passing outcomes.

The experimental consumer is built using the candidate skill before adoption. Fleet use by Agents of HEX follows the complete adoption gate. This sequencing avoids making the experiment depend on its own successful adoption.

The existing `AC2-*` obligations and contract-case expectations remain in force. Concrete consumer cases, oracles, sampling, thresholds, provider identities, budgets, evaluation custody, and content-retention policy must be frozen before their governed implementation/evaluation begins.

## Import provenance and limits

The original ratification, standard amendment, and proving profile were fetched in full as Markdown through the Linear attachment connector, then promoted into this locus and amended from the operator's ratifications in the current Codex task. Import identities are recorded in [authority-imports.json](authority-imports.json).

The import hashes identify UTF-8 Markdown returned by the connector, normalized to LF with one final newline, before local amendments. They are not attestations that the original remote attachment bytes were downloaded and matched. No source-byte custody claim is made for Linear. Source access in this session does not refresh the provider-document claims inherited from the original specification; claim-level provider refresh remains a required proving step.

This work began at repository commit `33bb105d33f2def89629f33dc0db08da6cf46f37` with a clean checkout. The authoring branch is `codex/heb-154-agent-code-v2-proving`. These are baseline facts for the documentation work, not the subject identity of a future implementation campaign.
