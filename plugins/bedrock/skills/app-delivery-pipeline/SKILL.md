---
name: app-delivery-pipeline
description: House engineering standard for the application build/test/deploy pipeline — GitHub Actions workflow anatomy and security posture (SHA-pinned actions, WIF keyless auth, no long-lived credentials), the shared org-level PR gates, required status checks, label-driven release automation, and the two stack legs — Python service (verify → image build → semver+SHA tagged push to Artifact Registry → declarative deploy → rollout verification) and static frontend (gate quartet → Vite build → Firebase Hosting with preview channels, cache headers, and the CSP header). Use whenever building, wiring, or conforming an app pipeline or its parts: setting up CI for a service or SPA repo, adding a build/test/deploy workflow, wiring image build/tag/push or a hosting deploy, adding preview environments, configuring release automation or branch-protection required checks, or checking whether a workflow follows the conventions. Assumes GitHub Actions as pipeline substrate and GCP as deployment target on the house branch model, with legs bound to the application-code and frontend-code stacks; a different CI host, cloud, or branch model is a rebind, not a line-edit. The infra plan/apply pipeline is infrastructure-code's; the gate lists themselves are owned by the authoring skills — this skill homes where they run, never re-declares what they are.
---

# App Delivery Pipeline

How an application build reaches an environment: the pipeline that runs the authoring skills' gates, builds the deployable artifact, and lands it — safely, keylessly, and with every gate a required check. This is the skill `application-code`, `frontend-code`, and `infrastructure-code` each point at from their own boundary.

**Binding:** GitHub Actions as the pipeline substrate; GCP as the deployment target; the house branch model (`feature/*` → `develop` → `main`, PR-gated). The two legs bind to their authoring skills — the service leg to `application-code`'s stack and image, the frontend leg to `frontend-code`'s stack and bundle. A different CI host, a different cloud, a different branch model, or a stack leg with no house authoring skill is a **rebind**: re-derive the conventions, don't line-edit these. Within-binding movement — action versions, runner images, a new GCP deploy target — is currency, not rebind.

**Leg selection is by what the repo is,** not by what was asked: a Python service takes the service leg; a Vite SPA takes the frontend leg; both take the spine. A repo hosting both surfaces runs both legs as separate path-filtered workflows.

## Where things are

| Doing this | Load |
|---|---|
| Any pipeline work — workflow anatomy, permissions, concurrency; SHA-pinning and keyless auth posture; the semver-label and branch-name org gates; required status checks; release automation; deploy environments | `reference/01-pipeline-spine.md` |
| Service pipeline — gate sequence, image build and scan, the **semver+SHA tagging discipline** (homed there), Artifact Registry push, declarative deploy, rollout verification, the Cloud Build scale-out path | `reference/02-python-service-leg.md` |
| Frontend pipeline — the gate quartet's pipeline home, Vite build, Firebase Hosting keyless posture, preview channels, cache headers, the **CSP header** (homed there), channel mapping | `reference/03-static-frontend-leg.md` |

Load the spine plus the repo's leg; a conformance check reads all three.

## Boundaries with sibling skills

- **The infrastructure delivery pipeline** (`terraform plan/apply`, its gates and scanners) → `infrastructure-code`, whose delivery-pipeline reference §5 draws the bright line: separate workflows, disjoint jobs, path-filtered triggers. Two disciplines are homed there and pointed at from here: SHA-pinning of actions and WIF keyless auth (its §4).
- **What the gates check** → the authoring skills. `application-code` owns the toolchain and coverage gate the service leg runs; `testing` owns the tests; `frontend-code` owns the gate quartet the frontend leg runs. This skill homes *where gates run and what happens after they pass* — a gate list restated here would be the drift surface the corpus prohibits.
- **The container image** → `application-code` builds it (Dockerfile, multi-stage, non-root); this skill's service leg builds *in the pipeline*, tags, pushes, and deploys it. The registry it lands in and the cluster it runs on → `infrastructure-code`.
- **The CSP-readiness of the app** → `frontend-code`; the header itself lands in this skill's frontend leg — the seam declared there, closed here.
- **Reviewing a finished workflow diff** → `code-review`. **Debugging a red pipeline** → `debug`. **Authoring or amending this standard** → `author-standard`.

## Authority

Public authority, pinned at authoring (2026-07-21), verify currency at adoption: GitHub Actions documentation and hardening guidance (workflow syntax, `permissions:`, OIDC, Environments, artifact attestations and their private-repo constraint); the google-github-actions canonical workflows (auth via WIF, Artifact Registry push, `deploy-cloudrun`); Firebase Hosting documentation (channels, `firebase.json` headers and rewrites) — *minus its key-based GitHub integration, rejected on the keyless posture*; Vite build documentation (hashed assets and caching). House substrate: `infrastructure-code`'s delivery-pipeline reference; the boundary and seam declarations in `application-code` and `frontend-code`; SDD-001 §7.2's required-checks constraint as the design-record exemplar.

**Sourcing note:** pre-existing house workflows — HEX's initial `ci.yml`, the SOFIA-legacy pipeline set — are **consumers and reference points, not sources**; they enter only through the proving step, where divergence resolves neuter/promote/demote, surfaced per item.
