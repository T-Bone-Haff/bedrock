# ADR-001 product-orchestration ownership amendment — ratification docket

## Recommendation

**RATIFIED.** Tad Haffey explicitly ratified the reviewed documentation revision on 2026-08-12. The governing ownership principle and documentation-authority repairs survived multi-perspective review. Both decision-bearing findings are resolved: ADR-001 and its documentation carriers take the major `2.0.0` treatment, while shipped-plugin conformance and package-major derivation move to HEB-128.

## Doctype and lifecycle treatment

- Doctype: ADR. The decision is a cross-product/platform ownership principle, not one service design, data-shape ruling, construct specification, or reusable procedural standard.
- Treatment: amend ADR-001 in place rather than supersede it. The accepted portable-core, adapter, routing, safety, evidence, and compatibility boundaries remain useful; only the Haffey-specific product/orchestration allocation is corrected.
- Current lifecycle: `2.0.0` ACCEPTED by explicit operator ratification on 2026-08-12; version 1.0.0 remains retained history.

## Affected authoritative files

1. `docs/adr/ADR-001-portable-core-and-surface-adapter-architecture.md` — owns the incorrect architecture assignment.
2. `docs/architecture/skill-architecture.md` — accepted carrier that assigned SOFIA kernel and HEX control-plane layers.
3. `docs/architecture/coverage-map.md` — accepted carrier that called multi-actor execution a declared SOFIA capability.
4. `docs/architecture/migration-compatibility.md` — accepted carrier that prescribed SOFIA recipe/kernel and HEX control-plane migration.

The coherence review also identified five shipped-plugin surfaces requiring later conformance: the SOFIA profile, compatibility matrix, registry, threat model, and quickstart. Those distributable changes are intentionally excluded from this documentation-only transaction and tracked by HEB-128, which owns package-major derivation and release evidence.

Review evidence lives under this docket directory and is non-authoritative evidence supporting the transaction.

## Reviewed correction

The reviewed draft establishes product-owned workflow meaning, policy, rosters, authority, state transitions, operational posture, and composition; limits Bedrock to selected reusable contracts and conventions; rejects a presumed universal kernel/DSL/control plane; separates capability from decision authority; permits bounded product-governed delegation; treats existing product implementations as evidence rather than Bedrock obligations; preserves legacy material without compatibility obligation; and keeps the separately ratified promotion standard out of this ADR.

The complete reviewed revision is the current unstaged diff for the four authoritative documentation files above. No unrelated tracked or user-authored change was present at the initial status check.

## Resolved version and provenance disposition

- ADR-001 and the three modified documentation carriers target `2.0.0` because the amendment changes normative authority.
- Path-only Markdown references require verification but no automatic edit.
- Version-pinned and semantic references are reconciled in the transaction that owns them.
- Historical evidence remains immutable.
- Repository architecture documents do not ship in the plugin, so HEB-126 does not bump the package manifest.
- HEB-128 owns later shipped-plugin conformance and derives its package major from the live manifest at landing.

## Resolved operator risk disposition

- Security, privacy, compliance, and cost introduce no additional decision for this ownership-only correction, for the reasons recorded in ADR §5.4.
- The applicable operational risk is ordinary drift between a shared contract and its consumers. Existing version, compatibility, migration, release-evidence, and cold-acceptance controls govern it.

## What this transaction does not decide

- the five-part promotion governance standard or its proving machinery;
- durability profiles D0–D3 or their product assignments;
- transactional state, immutable journal, artifact, idempotence, replay, or event-sourcing design;
- SOFIA's workbench, CLI/web UI, adoption flow, agent roster, runner, or broader implementation;
- HEX architecture, topology, authority, workflows, or operational posture;
- a universal orchestration kernel, control plane, recipe model, or DSL;
- which legacy components are eventually promoted;
- package version, commit, PR, release, consumer rollout, or external-system changes.

## Linear work graph

- HEB-126 — this ADR-001 2.0 documentation-authority transaction.
- HEB-127 — separate reusable-component promotion standard and proving gate.
- HEB-128 — shipped Bedrock portable-core 2.0 conformance and package-major transaction; blocked by HEB-126.
- RBT-113 — SOFIA-owned agent-loop redesign and Markdown document-review workbench proving slice; blocked by HEB-126 and related to RBT-72/RBT-110/RBT-111 and HEB-127.
- No HEX issue was created because this decision intentionally supplies no actionable HEX design.

## Validation

- `git diff --check`: PASS.
- `python scripts/validate_plugin.py` under the existing Anaconda Python environment: PASS, 13/13 skills.
- `python scripts/validate_package_governance.py`: PASS.
- `python -m unittest tests.test_package_governance`: PASS, 15/15.
- Four frozen review/coherence outputs validated against the frozen review-result JSON Schema.

## Ratification record

Tad Haffey explicitly directed: “Ratify the doc. Move it to APPROVED and commit to the bedrock repo.” Bedrock's canonical lifecycle token is `ACCEPTED`; the ADR records the operator approval in its status metadata. The same direction authorizes this documentation-only repository commit, but not a push, pull request, package change, or release.
