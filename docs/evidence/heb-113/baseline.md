# HEB-113 reconciliation baseline

Captured 2026-08-10 after fetching `T-Bone-Haff/bedrock`. `origin/main`, GitHub's default-branch head, and the isolated worktree baseline matched at `1e35b91f4ec073744bdbdb0cf79d8bfa0563b41f`, with package version `6.0.0`. PR 28 had merged HEB-115. HEB-112 remained In Progress; HEB-113 and HEB-114 were Planned sibling streams under HEB-112; HEB-113 was blocked only by completed HEB-111 and blocked HEB-118. HEB-114 was reconciled in parallel but the ratified arbitration serialized landing: HEB-113 first, HEB-114 second.

The saved checkout's untracked root `AGENTS.md` is user-owned. This isolated worktree did not contain or modify it.

## Ratified ownership

- `infrastructure-code` owns Terraform and every infrastructure plan/apply operation, including protected jobs hosted by GitHub Actions.
- `app-delivery-pipeline` owns application artifact build/test/provenance/promotion/deploy and the static-frontend delivery seam.
- `frontend-code` owns frontend behavior and gate semantics. HEB-113 consumes those gates but does not define or implement frontend behavior.
- Existing failures route to `debug`; finished-diff review routes to `code-review`.

## Complete finding dispositions

| Skill | Disposition | Findings | Realization |
|---|---|---|---|
| app-delivery-pipeline | Fix | DLV-001–DLV-012 | Preserve operation-first routing; correct event association, version-intent aggregation including `semver:none`, verification/mutation concurrency, artifact identity, WIF/action trust, provenance/SBOM, desired-state ownership, migration ordering, post-deploy behavior, rollback, static preview trust, and hosting-header coverage. |
| app-delivery-pipeline | Modify | DLV-013 | Replace one mandatory branch topology with an explicit delivery profile supporting main-only, feature/develop, release-branch, and queue/batch event models. |
| infrastructure-code | Fix | INF-001, INF-002, INF-004, INF-007–INF-009, INF-011–INF-013, INF-015 | Preserve routing and state-safety truth; correct action pinning, IAM ownership, workload/digest/controller rules, plan custody/expiry/apply binding, mutation serialization, identity/authority, recovery, and workload delivery ownership. |
| infrastructure-code | Modify | INF-003, INF-005, INF-006, INF-010, INF-014, INF-016 | Use constraints plus lock selection; capability-aware metadata; declared additive/authoritative/external IAM; behavior-driven probes/controllers; storage versus HA truth; explicit cost and recovery objectives. |

All 29 HEB-106 infrastructure and delivery dispositions are represented: 22 Fix and 7 Modify. No finding is deferred into HEB-114, HEB-118, HEB-119, or HEB-122.

## Portable core and Haffey profile

Portable core now defines explicit interaction fields, profile declaration, capability honesty, state/artifact identity, authority, mutation concurrency, failure, evidence, recovery, release intent, provenance, migration, verification, rollback, and lifecycle. JSON Schemas and semantic fixtures make the plan/apply and release bindings executable.

The Haffey profile binds Terraform/GCP/GCS/GKE-or-Cloud-Run/GitHub-Actions/WIF for infrastructure and GitHub-Actions/GCP/Artifact-Registry-or-static-store/GitHub-Environments/WIF for application delivery. A different cloud, IaC engine, CI host, registry, orchestrator, or branch topology is a declared profile rebind, not a portable-core change.

## Version classification

This transaction changes public routing, authority, failure, output, evidence, profile, and lifecycle semantics and introduces new required schemas. Under ADR-001 it is a package-major change. The ratified first package transaction is therefore exactly `6.0.0` to `7.0.0`, bounded with the HEB-113 skill and shared-validator changes. This classification does not itself authorize release.
