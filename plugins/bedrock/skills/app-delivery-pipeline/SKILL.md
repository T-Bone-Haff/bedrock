---
name: app-delivery-pipeline
description: "Application-artifact CI/CD only; exclude every Terraform or infrastructure plan/apply job and every executor relay or handoff, even when either uses GitHub Actions or delivery gates. Use this skill to author or conform portable application build, test, artifact, provenance, promotion, deploy, preview, migration, and rollout workflows, including the static-frontend delivery seam. The Haffey profile binds GitHub Actions and GCP. Do not use for application or frontend behavior, infrastructure mutation, existing failures, or finished-diff review."
---

# App Delivery Pipeline

Deliver an application artifact through declared gates and authorities. The portable contract is authoritative; GitHub Actions, GCP, and any branch model are profile choices.

## Interaction contract

- **Inputs:** application source identity; selected delivery profile; authoring-skill gate contract; release intent; environment authority; migration and rollback constraints.
- **Output:** one built artifact promoted by digest, with release, provenance, deployment, verification, and rollback evidence.
- **Authority:** PR verification cannot deploy to a protected environment. Promotion requires the profile's trusted event, environment approval, and desired-state authority.
- **Capabilities:** declare CI, artifact store, signing/attestation, deploy target, preview isolation, browser/synthetic verification, source-map handling, and rollback mechanisms. Never claim unavailable attestation or convergence.
- **Failure:** fail closed on ambiguous release intent, mutable artifact identity, missing provenance, untrusted credentials, conflicting desired-state writers, unsafe migration ordering, or incomplete post-deploy verification.
- **Evidence:** retain gates, artifact digest, SBOM, builder/workflow/source identity, inputs, attestation/signature verification, release decision, approvals, deployment, migrations, post-deploy checks, and rollback at the declared retention.
- **Lifecycle:** record profile/version, supported release-event model, environment and branch/topology binding, adoption state, expiry/review trigger, and rebind/deprecation path.

## Portable core

1. Resolve the operation first. Application build/test/artifact/promotion/deploy belongs here; Terraform and infrastructure plan/apply belong to `infrastructure-code` regardless of workflow host.
2. Declare a profile conforming to `reference/delivery-profile.schema.json`. Main-only, trunk, release-branch, merge-queue, and batched systems are profiles, not exceptions to one mandatory branch model.
3. Separate verification concurrency from mutation concurrency. Supersede stale PR verification when safe; serialize or queue environment mutation and never cancel an in-flight deployment merely because a newer revision arrived.
4. Build once from a trusted source identity. Promote the same content-addressed artifact through environments; labels and tags are pointers, not immutability proof.
5. Model release events explicitly, including merge commit, squash, queue/batch, revert, direct push, and ambiguous association. Aggregate all change intents; `semver:none` is explicit, auditable, and incompatible conflicts fail closed unless an authorized override is retained.
6. Emit an application release manifest conforming to `reference/application-release-manifest.schema.json`. Bind source, event, intent, artifact digest, desired-state owner, provenance, migrations, approvals, deployment, verification, and rollback.
7. Establish a provenance floor: SBOM plus builder, workflow, source, inputs, retention, and verification evidence. State private-repository or platform limits; never substitute a claim for a generated and verified record.
8. Separate migration ownership and ordering. Prefer expand/contract; state compatibility window, backup/restore gate, execution owner, idempotency/retry behavior, and rollback limits.
9. Verify behavior after platform rollout: endpoint or synthetic check, dependency/readiness signal, and an explicit rollback decision. Rollout success alone is not application health.

## Haffey profile

The house binding uses SHA-pinned GitHub Actions, least-privilege permissions, GCP Workload Identity Federation, Artifact Registry, protected GitHub Environments, and GCP deployment targets. Select the applicable reference:

| Surface | Reference |
|---|---|
| Workflow spine, event/release model, concurrency, identity, provenance | `reference/01-pipeline-spine.md` |
| Service image, registry, desired state, migrations, rollout | `reference/02-python-service-leg.md` |
| Static frontend artifact, preview trust, hosting, headers, caching | `reference/03-static-frontend-leg.md` |

A different CI host, registry, cloud, deploy target, or topology is a declared profile rebind, not a silent line substitution.

## Boundaries

- Terraform and every infrastructure plan/apply job, including protected GitHub Actions jobs → `infrastructure-code`.
- Application behavior and container definition → `application-code`; this skill runs its declared gates and builds the artifact.
- Frontend behavior, accessibility, browser gate semantics, and CSP compatibility → `frontend-code`; this skill runs the declared gates and delivers the resulting static artifact.
- Existing red or flaky pipeline → `debug`.
- Finished workflow review → `code-review`.
- Executor prompt/handoff → `author-execution-relay`.

## Minimum completion report

Report profile/rebinds, source and release-event identity, aggregated version decision, gate results, artifact digest, SBOM/provenance verification, desired-state owner, approvals, migration outcome, deployment and behavioral checks, rollback status, residual risk, and CI-only gates.
