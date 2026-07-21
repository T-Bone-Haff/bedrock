# Reference: Delivery Pipeline

How infrastructure reaches an environment safely: the gate sequence, plan-before-apply, static analysis and security scanning, keyless authentication, and keeping the infra pipeline distinct from the application pipeline. Load this when building or conforming the CI/CD that delivers Terraform.

## Contents

- [1. The gate sequence](#1-the-gate-sequence)
- [2. Plan before apply](#2-plan-before-apply)
- [3. Static analysis and security scanning](#3-static-analysis-and-security-scanning)
- [4. Keyless authentication (Workload Identity Federation)](#4-keyless-authentication-workload-identity-federation)
- [5. Infra pipeline ≠ app pipeline](#5-infra-pipeline--app-pipeline)
- [6. Drift detection](#6-drift-detection)

---

## 1. The gate sequence

Every infrastructure change runs the same gauntlet on its PR, in ascending order of cost:

1. **`terraform fmt -check -recursive`** — formatting (cheap, fails fast).
2. **`terraform validate`** — syntactic and internal consistency. Safe to run frequently; no state, no cloud.
3. **`tflint`** — provider-specific mistakes, deprecated syntax, unused declarations.
4. **Security scan** — `trivy config` and/or `checkov` (§3) for misconfigurations.
5. **`terraform plan -out=tfplan`** — the plan, **saved to a file** and stored (e.g., in the state bucket) for review.
6. **Policy check** — `gcloud terraform vet` (or OPA/Conftest) against the plan, before apply.
7. **`terraform apply tfplan`** — applies the **saved, reviewed** plan, in a **separate, manually-dispatched** step (§2).
8. **Post-apply** — drift and security re-checks (§6).

Gates 1–6 run on the PR and **block merge**. Gate 7 is deliberately not automatic on merge — see §2.

---

## 2. Plan before apply

The single most important discipline: **generate a plan, review it, then apply that exact plan.** Never `apply` straight from source — not in CI, not locally.

- **In CI**, the PR job runs `terraform plan -out=tfplan` and stores `tfplan`. A human reviews the plan output — what will be added, changed, destroyed — as part of PR review. Apply runs as a **separate manually-dispatched workflow** (`workflow_dispatch`) that consumes the stored plan, so a merge alone never mutates infrastructure; a person triggers the apply against the approved plan.
- **Locally**, even when prototyping, run `terraform plan` and read it before `apply`. A `destroy` line you didn't expect is the plan earning its keep.

The plan is the artifact a human approves; apply executes the approved artifact. This is why state is locked (`03` §1) — the plan is computed against a specific state, and apply must run against that same state.

---

## 3. Static analysis and security scanning

Layer the checks; they catch different things.

- **`terraform fmt` / `validate`** — format and syntax (gate 1–2).
- **TFLint** — a linter: provider rules, deprecations, unused declarations. Not a security tool.
- **A security scanner** — misconfigurations (a bucket without uniform access, a firewall open to `0.0.0.0/0`, an unencrypted database). Use **Trivy (`trivy config`)** and/or **Checkov**.

> **Use a current scanner.** `tfsec` is deprecated — Aqua folded its rule library into **Trivy** (the check IDs carry over unchanged), and **Terrascan was archived in November 2025**. For new work use Trivy or Checkov, not tfsec or Terrascan. Checkov has the deepest Terraform-specific rule set and graph-based cross-resource analysis; Trivy gives one binary across Terraform, container images, and Kubernetes. Running both is complementary, not redundant.

Two refinements worth adopting:

- **Scan the plan, not just the source.** Checkov's `terraform_plan` mode (and Trivy against plan JSON) resolves variables, modules, and data sources, so it evaluates the *actual* planned state — fewer false positives than raw-HCL scanning. It costs creds and time, so it's a PR/pre-apply gate rather than a pre-commit one.
- **Gate on severity, expand later.** Start the scanner blocking on `HIGH,CRITICAL` only; review the baseline; widen as you burn down findings. Turning every severity on at once tends to produce noise that gets blanket-suppressed instead of fixed. Track suppressions in a dedicated log with justifications and expiry.

---

## 4. Keyless authentication (Workload Identity Federation)

CI authenticates to GCP via **Workload Identity Federation** — the runner exchanges its OIDC token for short-lived GCP credentials. **No service-account keys are created, downloaded, or stored.**

```yaml
- name: Authenticate to GCP
  uses: google-github-actions/auth@v2
  with:
    workload_identity_provider: ${{ secrets.GCP_WIF_PROVIDER }}
    service_account: ${{ secrets.GCP_PIPELINE_SA }}
```

The pipeline service account is least-privilege and is the identity allowed to read state and apply. Locally, developers use `gcloud auth application-default login` (ADC) — they don't download keys either.

> **Pin CI actions to a commit SHA, not a mutable tag.** Supply-chain compromise of popular Actions is a live threat (the Trivy Action was compromised in a March 2026 incident, CVE-2026-33634). Reference third-party actions by full commit SHA so a re-tagged malicious release can't enter the pipeline silently. This is the CI-side analogue of hash-pinning dependencies.

---

## 5. Infra pipeline ≠ app pipeline

The infrastructure delivery pipeline (`terraform plan/apply`) and the application pipeline (lint → type → test → image build → service deploy) are **separate surfaces**, even when their workflow files share a `.github/workflows/` directory. Keep them in distinct workflows with distinct path triggers:

- The **infra** workflow fires on changes to `terraform/**` (and its own pipeline files) and runs the gate sequence above. It does **not** run application tests or build images.
- The **app** workflow fires on changes to service code and runs the application gates. It does **not** run `terraform`.

This isn't bureaucracy: infra changes and app changes have different blast radius, different reviewers, and different cadence (infra changes are rarer and higher-consequence). Path-filtered separate workflows keep a Terraform change from triggering an app rebuild and vice versa. Shared org-level gates — exactly-one `semver:` label, branch-name allowlist — apply to both, but the substantive jobs are disjoint.

*The application build/test/deploy pipeline is its own concern and is not authored here — it's the boundary this skill shares with the `app-delivery-pipeline` skill. This reference covers the infra side only.*

---

## 6. Drift detection

Infrastructure drifts when something changes a resource outside Terraform (a console edit, an automated GCP action). Catch it:

- **Periodic plan.** Run `terraform plan` on a schedule against each environment; a non-empty plan with no corresponding code change is drift. Surface it, don't auto-apply it.
- **Post-apply security checks.** After apply, re-run the security scanner (and `gcloud terraform vet`) so an environment can't settle into an insecure state between PRs.
- **Reconcile through code.** Resolve drift by amending configuration and re-applying — never by hand-patching the resource and leaving the configuration behind (the same rule as manifest discipline, `04` §5).

Drift detection is the running-system complement to pre-apply scanning: scanning catches what's wrong *before* it deploys; drift detection catches what changed *after*.
