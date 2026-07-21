# Reference: Pipeline Spine

The disciplines shared by both legs — workflow anatomy, security posture, the org-level gates, required status checks, release automation, and deploy environments. Load this when building or conforming any app pipeline; then load the leg reference for the repo's stack.

## Contents

- [1. Workflow anatomy](#1-workflow-anatomy)
- [2. Security posture](#2-security-posture)
- [3. Shared org-level gates](#3-shared-org-level-gates)
- [4. Required status checks are first-class](#4-required-status-checks-are-first-class)
- [5. Release automation](#5-release-automation)
- [6. Deploy environments](#6-deploy-environments)

---

## 1. Workflow anatomy

Every app workflow shares the same skeleton:

- **Triggers.** `pull_request` into `develop`/`main` runs the verify gates; `push` to those branches runs verify post-merge, and deploy where the leg defines one. Feature branches get CI through their PR, not through push triggers — a push trigger on `feature/*` doubles every run for no added signal.
- **Path filters when the repo hosts more than one surface.** The app workflow does not fire on `terraform/**` and the infra workflow does not fire on app code — the bright line and its rationale are `infrastructure-code`'s delivery-pipeline reference §5. A single-surface repo (a lone SPA) needs no path filters; don't add them ceremonially.
- **Least-privilege `permissions:`.** Top level declares `contents: read`. A job that needs more (`id-token: write` for WIF, `contents: write` for tagging) escalates **at the job level, only for itself**. A workflow with blanket write permissions is a finding.
- **Concurrency.** One in-flight run per workflow+ref; a newer push cancels the stale run (`concurrency` group on `${{ github.workflow }}-${{ github.ref }}`, `cancel-in-progress: true`). CI minutes spent verifying a commit that's already been superseded are pure waste.
- **One job per gate cluster, named for what it proves.** `verify`, `build`, `deploy` — job names become required-check names (§4), so name them as the contract they are, not after their implementation.

## 2. Security posture

Two disciplines are homed in `infrastructure-code`'s delivery-pipeline reference §4 and pointed at, not restated: **SHA-pinning of third-party actions** (with the live supply-chain rationale) and **WIF keyless authentication to GCP**. Both bind app workflows exactly as they bind infra workflows.

What this skill adds on top, app-side:

- **No long-lived credentials, enumerated.** The two named anti-patterns, both from real prior practice: the **CI personal-access-token** (legacy SOFIA carried `SOFIA_RELEASE_TOKEN` with 90-day rotation ceremony — release automation runs on the job-scoped `GITHUB_TOKEN` instead, §5) and the **service-account JSON key in a GitHub secret** (Firebase's official GitHub integration provisions exactly this — the frontend leg's keyless alternative is `03` §3). A pipeline that stores either is a BLOCKING finding, not a style choice.
- **`GITHUB_TOKEN` is scoped by `permissions:`, never supplemented by a PAT.** If a job seems to need a PAT, the job is misdesigned — restructure it or surface the design gap; don't mint the token.
- **Artifact attestations are a currency-conditional, not a default.** GitHub's `attest-build-provenance` establishes build provenance, but private repositories require GitHub Enterprise Cloud — not currently the house plan. Adopt when the plan supports it (the service leg's digest outputs are already attestation-shaped); until then, absence is a known constraint, not an oversight.

## 3. Shared org-level gates

Two gates run on every app PR regardless of leg — the same pair `infrastructure-code`'s reference §5 notes as shared with the infra pipeline. **They are homed here**; the infra reference mentions them, this section defines them:

- **Exactly one `semver:` label** (`semver: major` / `semver: minor` / `semver: patch`) on the PR. Zero or multiple fails the gate. This is the input to release automation (§5) — enforcing it at PR time is what lets the release job trust the label at merge time.
- **Branch-name allowlist.** The head branch matches the house model (`feature/*`, `hotfix/*`, `release/*` per the repo's declared branch model). A branch that doesn't parse is rejected at PR, where fixing it costs a rename — not at release, where it costs archaeology.

Both are cheap, run first, and fail fast.

## 4. Required status checks are first-class

A gate that isn't a **required status check** under branch protection is advice, not a gate. The pipeline's job structure exists to be required:

- **The verify jobs of the repo's leg are required checks on `develop` and `main`.** Merging past a red gate is not an override mechanism; overrides happen by fixing or by explicitly amending the gate, in that order of preference.
- **Repos may bind additional required checks derived from their design records.** The exemplar: SDD-001 §7.2 makes the knowledge-service BUILD leg complete only when the conformance harness's 1b gateway-behavioral contract set runs un-skipped as required checks, all green. The pipeline's obligation is structural — surface such sets as **distinct, stably-named checks** so branch protection can require them individually, and keep them un-skippable once flipped.
- **Flipping a check to required is a deliberate act, captured where the repo captures decisions** — never a silent branch-protection edit. SDD-001 names the flip as the build's own act; that pattern generalizes.

## 5. Release automation

Releases are computed from the merged PR's `semver:` label — the gate in §3 guarantees exactly one exists.

- **On push to `main`**, the release job reads the label from the just-merged PR, bumps from the latest tag (`vMAJOR.MINOR.PATCH`), and creates an **annotated tag + GitHub Release** with generated notes.
- **It runs on the job-scoped `GITHUB_TOKEN`** with `contents: write` escalated on the release job only. No PAT (§2).
- **A `semver: major` release passes a manual gate first** — a protected deploy environment with required reviewers (§6), the platform-native mechanism. Third-party approval actions (legacy used `trstringer/manual-approval`) reimplement what Environments now provide, with a worse audit trail.
- **The tag is the version the service leg stamps onto its image** (`02` §3) — release automation and image tagging are one discipline, not two.

## 6. Deploy environments

GitHub **Environments** are the deploy-gating primitive:

- **Deploy jobs declare their environment** (`environment: production`, with `url:` set to the deployed surface). Environment-scoped secrets and variables live on the environment, not repo-wide — a PR-triggered job can't read production credentials.
- **Protected environments carry required reviewers** — this is where human deploy approval lives (and the major-release gate, §5). Approval evidence lands in the deployment log, not in an issue thread.
- **Preview deployments are ephemeral and PR-scoped** — the frontend leg's preview channels (`03` §4) are the current instance; a service-leg preview environment is future scope, adopted when a consumer needs it, not pre-built.
