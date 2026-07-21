# Reference: Python Service Leg

The pipeline for a Python/FastAPI service: verify gates → image build → tagged push to Artifact Registry → deploy → rollout verification. The spine (`01`) governs throughout; this reference adds what is service-specific. What each gate checks is owned by the authoring skills — this leg homes **where the gates run**, never re-declares what they are.

## Contents

- [1. The gate sequence](#1-the-gate-sequence)
- [2. Image build](#2-image-build)
- [3. Image tagging discipline](#3-image-tagging-discipline)
- [4. Push: Artifact Registry](#4-push-artifact-registry)
- [5. Deploy and rollout verification](#5-deploy-and-rollout-verification)
- [6. The Cloud Build scale-out path](#6-the-cloud-build-scale-out-path)

---

## 1. The gate sequence

The verify job runs on every PR and on push to `develop`/`main`, in ascending order of cost, failing fast:

1. **Lint** — `ruff check` (and format check), per `application-code`'s toolchain.
2. **Type** — the type-checker the repo's `pyproject.toml` declares.
3. **Test + coverage** — `pytest` with the coverage gate enforced exactly as `application-code` configures it (`--cov-fail-under` from `pyproject.toml`, reference `01-code-structure.md` §10). The pipeline runs the gate; it does not own the threshold — a pipeline that re-declares the number is a drift surface.
4. **Repo-specific required sets**, where the repo's design records bind them, run as **their own named jobs** — distinct checks per spine §4. The exemplar: the knowledge-service conformance harness's 1b contract set (SDD-001 §7.2) runs as its own job, separately from the service's unit gates, so branch protection can require it individually and its red is legible as *contract* red, not *test* red.

Dependency installs use the compiled lockfiles (`requirements.txt` from `requirements.in`) — CI installing anything unpinned defeats the lockfile discipline.

## 2. Image build

The image builds **in the Actions runner** — `docker/build-push-action`, building the multi-stage Dockerfile `application-code` defines (reference `01-code-structure.md` §9). The build job:

- runs **after** verify passes (`needs: [verify]`) and only on push to `develop`/`main` — PR runs verify but does not build; an image no one can deploy from a PR is CI minutes spent on ceremony;
- **scans the built image** before push (Trivy image scan — the scanner currency ruling is `infrastructure-code`'s delivery-pipeline reference §3, and it applies to images as it applies to config);
- emits the **image digest** as a job output — the digest, not the tag, is what downstream verification and (when available, spine §2) attestation consume.

## 3. Image tagging discipline

**Homed here.** Both `infrastructure-code` references that mention it (`02-gcp-conventions.md` §Artifact Registry; `04-kubernetes-and-stateful-workloads.md` §rollback) point at this section.

- **Every image pushed carries the full commit SHA as a tag.** The SHA tag is the build's identity — it exists for every `develop`/`main` build and is what deploys reference.
- **A release (spine §5) additionally applies the semantic version tag** (`vX.Y.Z`) to the *same image* — retagging the already-built, already-scanned artifact, never rebuilding. The semver tag is the human-facing name; the SHA is the machine-facing identity; rollback (infra `04`) uses them together.
- **`latest` is never pushed.** A moving tag on a deployable artifact makes "what is running?" unanswerable.
- **Tags are immutable in practice:** a tag, once pushed, is never re-pointed. Same-tag-different-digest is a pipeline bug, full stop.

## 4. Push: Artifact Registry

Push goes to the environment's Artifact Registry repository — provisioned by `infrastructure-code` (its reference `02` owns the registry conventions; the seam: infra provisions the registry, this leg pushes to it). Auth is WIF (spine §2); Docker credential setup uses the token from the auth step. The push job needs no registry-scoped long-lived secret — if one appears, the WIF wiring is broken; fix it, don't work around it.

## 5. Deploy and rollout verification

- **Deploys are declarative.** The manifests in the repo are the source of truth (infra `04`'s manifest discipline); the deploy step renders them with the new image tag (kustomize `images:` override or equivalent) and applies. **`kubectl set image` against a live deployment is the named anti-pattern** — it mutates the cluster away from the manifests, exactly the drift infra `04` §5 prohibits. Legacy practice did this; it does not carry forward.
- **Cloud Run targets** deploy via `deploy-cloudrun` with the SHA-tagged image URI — same discipline, the service YAML in-repo where configuration is nontrivial.
- **The deploy job declares its GitHub Environment** (spine §6) — that is where deploy approval and environment-scoped configuration live.
- **Rollout verification is the deploy's last step, and it is blocking:** `kubectl rollout status` per workload (GKE) or the service-ready check (`deploy-cloudrun` outputs). Readiness itself is the platform's job — the container's probes (`application-code`'s `/healthz`/`/readyz`) are what rollout status consults. The pipeline does not re-implement health checking with sleeps and curls; a hand-rolled `sleep 5 && curl` is the legacy anti-pattern this replaces.
- **A failed rollout fails the workflow.** Recovery is a rollback deploy of the previous semver+SHA pair per infra `04` — through the same pipeline, never by hand.
- **GitOps controllers (Argo/Flux) are future scope**, adopted if deploy volume earns them — a design ruling then, not pre-built now.

## 6. The Cloud Build scale-out path

The in-runner build (§2) is the default. Delegating build/push to **Cloud Build** is the sanctioned scale-out, warranted by either discriminator:

- the repo builds **many images per commit** (monorepo fan-out — the legacy platform's eleven-service build was this case, and it was the right call there), or
- the build requires **private-network access** the runner doesn't have.

When exercised: Actions still owns the pipeline — gates, tagging discipline, release, deploy all stay here; Cloud Build executes build/push only, synchronously, with its status surfaced as a required check. A Cloud Build delegation that grows its own gates is the pipeline splitting in two — the failure mode that motivated the default.
