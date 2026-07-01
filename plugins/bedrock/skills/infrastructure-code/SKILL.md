---
name: infrastructure-code
description: House engineering standard for authoring infrastructure-as-code and its delivery pipeline — Terraform modules and GCP resource conventions, remote state, environment structure, Kubernetes manifests including stateful workloads, and the plan/apply delivery pipeline. Use whenever writing, structuring, or conforming infrastructure: scaffolding a Terraform module, provisioning a GCP resource (GKE, Cloud Run, Cloud SQL, Firestore, Pub/Sub, Secret Manager, networking, IAM), configuring remote state or environments, writing Kubernetes Deployment/StatefulSet manifests, running a stateful database on GKE, or building the infra CI/CD pipeline (fmt/validate/lint/scan/plan/apply gating, Workload Identity Federation). Assumes a Terraform + GCP + GKE/Cloud Run + GitHub-Actions/Cloud-Build stack; a different cloud, IaC tool, CI host, or orchestrator is a rebind, not a line-edit. Writing application/service code is the application-code skill; the app build/test/deploy pipeline is separate.
---

# Infrastructure Code

The engineering conventions for authoring infrastructure-as-code and the pipeline that delivers it. This SKILL.md carries the invariants that apply to *every* piece of infrastructure plus a map into the detailed references; load a reference file for the area you're working in.

## Stack binding (read once)

These conventions are written against a specific stack: **Terraform (`hashicorp/google` provider, `~> 6.0`), GCP, GKE + Cloud Run, GitHub Actions driving Cloud Build.** They're portable across projects *on that stack*.

Infrastructure binds on **more axes than application code**, so a rebind is broader here. A different choice on any of these axes — another IaC tool (Pulumi, OpenTofu, CDK), another cloud (AWS, Azure), another orchestrator (a non-GKE Kubernetes, ECS, Nomad), or another CI host/runner (GitLab CI, Cloud Build standalone) — is a **rebind**, not a small substitution: it means re-deriving the equivalent conventions for that axis, not editing individual lines here. Name the rebind explicitly when you do it. The *disciplines* (pin everything, plan before apply, remote locked state, no secrets in state, least-privilege keyless auth) are stack-independent and survive a rebind; the *resource syntax* does not.

## The misfit rule

These are strong defaults, not scripture. Where a convention genuinely doesn't fit the work in front of you, state the exception and why in the code or commit, then proceed — don't silently violate it, and don't contort the configuration to satisfy a rule that doesn't earn its place here. A recurring misfit is a signal the convention should change, not a thing to keep working around.

## Always-apply invariants

These hold for every module, manifest, and pipeline you write. If you remember nothing else from the references, hold these:

1. **Format and validate before commit.** `terraform fmt -recursive` and `terraform validate` pass before code reaches version control — wired as a pre-commit hook and re-checked in CI.
2. **Pin everything.** `required_version` for the Terraform binary, a pinned `version` for every provider, an exact `version` for every registry module. Unpinned dependencies are how infrastructure drifts silently between runs.
3. **State is remote, locked, and sensitive.** State lives in a GCS backend with locking, never on local disk, and is never committed. Treat the whole state file as a secret; restrict the bucket to the pipeline service account and admins.
4. **Plan before apply — always.** Generate a plan, review it (or have it reviewed), then apply that saved plan. Never `apply` straight from source, not even locally. The plan is the artifact a human approves; apply executes the approved plan.
5. **No secrets in configuration or state.** Secrets come from Secret Manager via data sources, never hardcoded and never committed. Mark sensitive variables and outputs `sensitive = true` (knowing that still leaves them plaintext in state — see §3).
6. **Environment-specific values carry no defaults.** `project_id`, `region`, and anything that differs per environment have no default, forcing the caller to supply them. Environment-independent values (disk size, retention) get sensible defaults.
7. **Least-privilege, keyless identity.** Provision narrowly-scoped service accounts; CI authenticates via Workload Identity Federation. Never create, download, or commit a service-account key.
8. **Additive IAM on shared resources.** Use `google_*_iam_member` (additive), not `google_*_iam_policy` (authoritative) — the authoritative form silently strips Google-managed role bindings.
9. **Every resource is labeled and headed.** Resources carry `managed_by = "terraform"` and an `environment` label; every `.tf` file and manifest carries the comment-block header (§1); every module carries a `README.md`.
10. **Stateful means StatefulSet.** A workload that needs durable per-replica storage (a database) uses a StatefulSet with persistent volumes, never a Deployment — and provisioning that cluster is this skill's job, not application-code's.

## Where to look

Load the reference for the area you're working in — each is self-contained and cross-links the others where needed.

| You're working on… | Read |
|---|---|
| Module file layout; naming; HCL formatting; variables/outputs/locals ordering; `count`/`for_each`; the comment-block header; helper scripts; repo structure | `reference/01-module-structure-and-style.md` |
| Provider config + version pinning; resource naming and labels; environment-conditional hardening; IAM and service accounts; API enablement; the GCP service set (GKE, Cloud Run, Cloud SQL, Firestore, Pub/Sub, Secret Manager, Memorystore, Artifact Registry, networking) | `reference/02-gcp-conventions.md` |
| Remote state in GCS; locking; state access and hygiene; environment-per-directory layout; `.tfvars`; keeping secrets out of state | `reference/03-state-and-environments.md` |
| Kubernetes manifests; Deployment vs StatefulSet; persistent volumes; running a stateful database (Neo4j-class) on GKE; headless services; probes; GitOps/manifest discipline | `reference/04-kubernetes-and-stateful-workloads.md` |
| The infra delivery pipeline — fmt/validate/lint/scan/plan/apply gating, policy checks, drift detection, Workload Identity Federation, keeping the infra pipeline separate from the app pipeline | `reference/05-delivery-pipeline.md` |

## Boundaries with sibling skills

- **Writing application/service code** → the `application-code` skill. That skill owns the service's `Dockerfile`, `pyproject` toolchain, and code layout; this skill owns the cluster, networking, IAM, and state the service runs on. The seam is at the image: application-code *builds* the container, infrastructure-code *runs* it.
- **The application build/test/deploy pipeline** (lint → type → test → image build → service deploy) is a **separate surface** from the infra delivery pipeline (`terraform plan/apply`). This skill covers the latter only. The former is its own concern; keep app-pipeline YAML and infra-pipeline YAML in separate workflows even when they share a directory (§5).
- **Reviewing a finished diff** → the `code-review` skill. This skill is about *authoring* conformant infrastructure; deciding whether an existing change conforms is a review task.
- **Tool and topology decisions** (which GitOps tool, cluster topology/HA, whether a workload justifies GKE over Cloud Run, adopting CMEK) are **ADR-homed**, not settled here — see `author-decision-record`. This skill carries the conventions; the enterprise-bound choices are recorded as decisions.
