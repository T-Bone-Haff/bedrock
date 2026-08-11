---
name: infrastructure-code
description: "Own every Terraform or infrastructure plan/apply workflow, including protected jobs implemented in GitHub Actions; these are infrastructure-code, never app-delivery-pipeline. Use this skill to author or conform portable infrastructure-as-code, remote state, identity, workload manifests, recovery controls, and the protected plan/apply pipeline. A different IaC engine or cloud still routes here as a declared profile rebind. The Haffey profile binds Terraform, GCP, Kubernetes, and GitHub Actions. Do not use for application artifact delivery, application or frontend behavior, existing failures, executor handoffs, or finished-diff review."
---

# Infrastructure Code

Author infrastructure and its mutation pipeline from an explicit profile. The portable contract is the authority; the Haffey profile is one binding, not a universal prescription.

## Interaction contract

- **Inputs:** approved infrastructure intent; repository and environment context; selected infrastructure profile; current state lineage; identity, recovery, and risk constraints.
- **Output:** reviewable infrastructure source plus a plan/apply record whose artifact, authority, state, and evidence are bound end to end.
- **Authority:** change only infrastructure surfaces the operator placed in scope. A plan approval authorizes only the exact unexpired plan and apply identity that were reviewed.
- **Capabilities:** declare the available IaC engine, cloud, state backend, CI identity, policy/scanning, orchestrator, artifact store, and recovery tooling. Never imply an unavailable capability.
- **Failure:** fail closed on ambiguous ownership, stale or mismatched plans, missing authority, state drift, unverified identity, destructive recovery uncertainty, or absent required evidence.
- **Evidence:** retain source/config/lock identity, plan digest and custody, state lineage/serial, apply identity, policy results, actor/approval, workload digest, and recovery proof at the profile-defined retention.
- **Lifecycle:** record profile/version, adoption state, expiry or review trigger, migration/rebind notes, and deprecation path.

## Portable core

1. Resolve the operation first. Terraform or infrastructure plan/apply work belongs here even when implemented as a GitHub Actions job.
2. Declare a profile conforming to `reference/infrastructure-profile.schema.json`; do not infer cloud, tool, branch, or topology from the repository name.
3. Constrain tool and provider compatibility in source; use the dependency lock as the selected, reviewed resolution. Registry modules use immutable reviewed versions.
4. Keep state remote where the profile supports it, protect it as sensitive, and record locking behavior honestly. Treat every value Terraform reads as potentially state-resident; a sensitivity flag redacts output but does not keep payloads out of state.
5. Separate identity from authorization. Prefer short-lived workload identity and least privilege; record whether shared IAM is additive, authoritative, or externally owned before changing it.
6. Plan before mutation. Protect the plan as a sensitive expiring artifact and bind apply through `reference/infrastructure-apply-manifest.schema.json` to source, configuration, lock, workspace, state lineage/serial, plan digest, actor, approval, and expected artifact digests.
7. Serialize mutations per state target. Verification may supersede older runs; plan/apply mutation must queue or fail closed, never cancel an in-flight apply to make a newer run win.
8. Select workload controller, storage, probes, rollout, backup, and recovery from behavior and objectives. Durable storage alone neither requires a StatefulSet nor establishes high availability.
9. Define RPO/RTO, backup custody, restore validation, rollback limits, and escalation before destructive or stateful change.
10. Label, tag, and annotate only where the target supports them. Record compensating inventory when it does not.

## Haffey profile

The current house binding is Terraform with reviewed `hashicorp/google` constraints and lock selections, GCP, GCS state, GKE or Cloud Run where justified, and GitHub Actions with GCP Workload Identity Federation. Load the relevant reference:

| Surface | Reference |
|---|---|
| Terraform shape, dependency resolution, metadata capability | `reference/01-module-structure-and-style.md` |
| GCP naming, services, identity, IAM ownership, cost controls | `reference/02-gcp-conventions.md` |
| State, environments, bootstrap, recovery | `reference/03-state-and-environments.md` |
| Kubernetes/workload controller, storage, probes, delivery seam | `reference/04-kubernetes-and-stateful-workloads.md` |
| Protected plan/apply, plan custody, apply binding, drift | `reference/05-delivery-pipeline.md` |

Changing IaC engine, cloud, state semantics, orchestrator, or CI identity is a documented rebind. Re-derive only the affected profile axes while preserving the portable contract.

## Boundaries

- Application image, service, and static-site build/test/deploy/promotion → `app-delivery-pipeline`.
- Frontend behavior and frontend gate semantics → `frontend-code`; this skill may provision its hosting infrastructure only.
- Existing failing or flaky pipeline → `debug`.
- Finished change review → `code-review`.
- Executor instructions or handoffs → `author-execution-relay`.
- Enterprise topology choices belong in a decision record; this skill implements the ratified choice.

## Minimum completion report

Report profile and rebinds, exact state target, source/config/lock and plan identities, authority and actor, policy/scanner results, mutation outcome, workload digest, recovery evidence, residual risk, and any CI-only gate.
