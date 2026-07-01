# Reference: State and Environments

How Terraform state is stored, secured, and partitioned, and how environments are laid out so each has its own state. Load this when configuring remote state, standing up a new environment, or deciding how to split state files.

## Contents

- [1. Remote state in GCS](#1-remote-state-in-gcs)
- [2. State as a blast-radius boundary](#2-state-as-a-blast-radius-boundary)
- [3. Environment-per-directory layout](#3-environment-per-directory-layout)
- [4. Secrets and state hygiene](#4-secrets-and-state-hygiene)

---

## 1. Remote state in GCS

State lives in a GCS backend, never on local disk. The GCS backend locks state automatically (so two runs can't corrupt it) and keeps state — and the sensitive values in it — out of version control.

```hcl
# backend.tf
terraform {
  backend "gcs" {
    bucket = "myorg-tfstate-prod"
    prefix = "platform/networking"
  }
}
```

The state bucket has **versioning enabled** (so a corrupt or accidentally-deleted state can be recovered) and **`prevent_destroy`** on the bucket resource itself. Its access is restricted to the **pipeline service account and admins** — state is a sensitive artifact; a read of it is a read of every secret any resource exposed.

The `prefix` partitions multiple state files within one bucket — use it to give each configuration (each blast-radius boundary, §2) its own state object. When you need a value from another state, prefer a provider data source (look the resource up by name/tag) over reading the other state directly; share data, not whole state files.

---

## 2. State as a blast-radius boundary

A single state file is a single failure and locking domain: every apply locks all of it, and a bad change can touch anything in it. So **split state by blast radius and approval boundary**, not by whim:

- Foundational infrastructure (org IAM, shared networking, the state bucket itself) is its own state, changed rarely, approved by the platform owner.
- Each application's infrastructure is its own state.
- Large stacks split further — networking, data, compute as separate states — so a compute change can't lock or threaten the database.

The rule of thumb: configurations with **different approvers, different change frequency, or different blast radius belong in different state files** (different `prefix`, or different bucket). This also keeps each state small, which keeps plans fast and readable.

---

## 3. Environment-per-directory layout

Without HCP Terraform workspaces, the canonical multi-environment layout is **a directory per environment**, each calling the shared modules with environment-specific inputs and its own backend and state:

```
.
├── modules/
│   ├── runtime/
│   ├── networking/
│   └── data/
├── dev/
│   ├── backend.tf        # prefix = "env/dev"
│   ├── main.tf           # calls ../modules/* with dev inputs
│   ├── variables.tf
│   └── dev.auto.tfvars
├── staging/
│   ├── backend.tf        # prefix = "env/staging"
│   └── ...
└── prod/
    ├── backend.tf        # prefix = "env/prod"
    └── ...
```

Each environment directory has its **own backend/state**, its **own `.tfvars`** carrying the environment-specific values (the variables that have no default — §5 of `01`), and calls the **same modules** so the environments stay structurally identical and only their inputs differ. Promotion is a code change merged through environments (the delivery flow — `05-delivery-pipeline.md`), not a hand-edit in one place.

---

## 4. Secrets and state hygiene

**State is plaintext.** Marking a variable or output `sensitive = true` keeps it out of plan/apply *output*, but Terraform still writes it to state in the clear. Many resources and data sources (database passwords, generated keys, secret versions) land in state regardless. So:

- **Keep secrets out of state where you can** — reference Secret Manager at runtime rather than materializing the secret value through Terraform.
- **Treat the whole state file as a secret** — the GCS backend (§1) is the encryption-and-access boundary; that's why bucket access is locked down.
- **Never commit** `*.tfstate`, `*.tfstate.*` backups, `.terraform.tfstate.lock.info`, the `.terraform/` directory, saved plan files (`-out`), or any `.tfvars` carrying secrets.
- **Always commit** the `.terraform.lock.hcl` dependency lock (so provider versions are reproducible), all `.tf`, a `.gitignore`, and a `README.md`.

A starting `.gitignore`:

```gitignore
*.tfstate
*.tfstate.*
.terraform/
.terraform.tfstate.lock.info
*.tfplan
*-secret.auto.tfvars
```

Secrets that must reach a resource come from Secret Manager via a data source, or from the CI runner's environment — never hardcoded, never in a committed `.tfvars`.
