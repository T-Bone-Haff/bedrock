# Reference: Module Structure and Style

The *shape* of a Terraform module — file layout, naming, formatting, the ordering conventions, and how modules and repositories are organized. Load this when scaffolding a new module or deciding where configuration goes and what to call it.

## Contents

- [1. File layout](#1-file-layout)
- [2. The comment-block header](#2-the-comment-block-header)
- [3. HCL formatting](#3-hcl-formatting)
- [4. Resource naming and order](#4-resource-naming-and-order)
- [5. Variables](#5-variables)
- [6. Outputs and locals](#6-outputs-and-locals)
- [7. count and for_each](#7-count-and-for_each)
- [8. Module structure](#8-module-structure)
- [9. Helper scripts and the unforgiving substrate](#9-helper-scripts-and-the-unforgiving-substrate)
- [10. Repository structure](#10-repository-structure)

---

## 1. File layout

A module's configuration is split across canonically-named files so a maintainer always knows where to look. Start every module with `main.tf`; add the others as the module grows.

| File | Holds |
|---|---|
| `main.tf` | Resources and data sources (the default home; split out as it grows) |
| `variables.tf` | All `variable` blocks, alphabetical |
| `outputs.tf` | All `output` blocks, alphabetical |
| `versions.tf` | The single `terraform` block: `required_version` + `required_providers` |
| `providers.tf` | `provider` blocks and their configuration |
| `backend.tf` | Backend configuration (remote state — see `03-state-and-environments.md`) |
| `locals.tf` | Local values referenced across more than one file |

As a module grows past a comfortable `main.tf`, split resources into files by logical group — `network.tf`, `iam.tf`, `database.tf`, `pubsub.tf` — named so it's immediately clear where a given resource lives. No matter how you split, a maintainer should be able to guess the filename from the resource.

> **`versions.tf` vs `terraform.tf`.** HashiCorp's canonical name for the file holding the `terraform` block is `terraform.tf`. This corpus uses `versions.tf`, a widely idiomatic community variant, because it names the file by what it carries. Either is fine; be consistent within a repo. (Don't put `required_version`/`required_providers` in `main.tf` — it belongs in its own file.)

---

## 2. The comment-block header

Every `.tf` file and every Kubernetes manifest begins with a comment-block header, mirroring the module comment block in the `application-code` skill:

```hcl
##############################################################################
# File: <path/to/file.tf>
# Module: <module-name>
# Author: <author or team>
# Created: YYYY-MM-DD
# Revised: YYYY-MM-DD
# Description: <one-paragraph description of what this file provisions>
##############################################################################
```

The `# Revised:` line carries a bare date — no parenthetical ticket. Infrastructure edits, like application-code edits, are frequent and low-decision-density, so the per-edit stamp stays light. The header uses Terraform's `#` comment form (not `//` or `/* */`, which are non-idiomatic). For YAML manifests, use the same block with `#` comments.

---

## 3. HCL formatting

`terraform fmt -recursive` is the authority — it enforces the formatting subset mechanically, so run it before every commit (pre-commit hook) and re-check it in CI with `terraform fmt -check`. The conventions it enforces, so you write them right the first time:

- Indent two spaces per nesting level.
- Align the `=` signs of consecutive single-line arguments at the same nesting level.
- Place all arguments first, then nested blocks, separated by one blank line.
- List meta-arguments (`count`, `for_each`, `provider`) first, separated from other arguments by a blank line; place meta-argument blocks (`lifecycle`) last.
- Separate top-level blocks with one blank line.

```hcl
resource "google_storage_bucket" "state" {
  # meta-argument first
  for_each = var.buckets

  name     = "${var.project_id}-${each.key}"
  location = var.region

  versioning {
    enabled = true
  }

  # meta-argument block last
  lifecycle {
    prevent_destroy = true
  }
}
```

Use `#` with a space for comments. Beyond `fmt`, run a linter — **TFLint** — to catch provider-specific mistakes, deprecated syntax, and unused declarations that `fmt` and `validate` don't.

---

## 4. Resource naming and order

**Naming.** Give every resource a descriptive **noun**, words separated by underscores, and **do not repeat the resource type** in the name — the resource address already includes it. Wrap type and name in double quotes.

```hcl
# Bad — type echoed in the name, hyphens, camelCase
resource "google_storage_bucket" "stateBucket-gcs" {...}

# Good
resource "google_storage_bucket" "state" {...}
```

Use a `name_suffix` local for the repeated `${environment}` / `${region}` tail rather than interpolating it inline on every resource (see §6).

**Order.** The order of resources doesn't affect how Terraform builds them (it resolves dependencies from references), so order for readability: define a data source *before* the resource that references it, so the file builds on itself. Within a resource block, order parameters consistently:

1. `count` or `for_each` (if present)
2. Non-block arguments
3. Nested blocks
4. `lifecycle` (if present)
5. `depends_on` (if required)

Prefer implicit dependencies (referencing another resource's attribute) over explicit `depends_on`; reach for `depends_on` only when there's a real ordering requirement Terraform can't infer.

---

## 5. Variables

Every variable declares a `type` and a `description` — the description feeds auto-generated module docs and tells the next maintainer what the name can't. Order the parameters consistently: `type`, `description`, `default` (optional), `sensitive` (optional), `validation` (optional).

```hcl
variable "db_disk_size_gb" {
  type        = number
  description = "Cloud SQL data disk size in GiB."
  default     = 20
}

variable "project_id" {
  type        = string
  description = "GCP project ID this module provisions into."
  # No default — environment-specific, the caller must supply it.
}
```

Three rules that matter more than the rest:

- **Environment-specific values get no default.** `project_id`, `region`, environment name — anything that differs per environment — must be supplied by the caller. Environment-*independent* values (disk size, retention days, machine tier) get sensible defaults so callers only override what's distinctive.
- **Boolean variables get positive names.** `enable_private_nodes`, `enable_deletion_protection` — not `disable_*` — so conditional logic reads naturally.
- **Mark secrets `sensitive = true`.** It keeps them out of plan/apply output. It does *not* keep them out of state (see `03-state-and-environments.md` §4).

Use a `validation` block only when a variable has genuinely restrictive requirements (an enum of allowed regions, a minimum replica count) — not as a reflex.

---

## 6. Outputs and locals

**Outputs.** Every output declares a `description`; order is `description`, `value`, `sensitive`. Mark any output carrying a secret, an endpoint, or a connection string `sensitive = true`. When a child module produces a value a caller needs, the parent must **re-export** it — internal module outputs aren't automatically exposed.

```hcl
output "gke_cluster_endpoint" {
  description = "GKE cluster API endpoint."
  value       = google_container_cluster.primary.endpoint
  sensitive   = true
}
```

**Locals.** Use locals sparingly — overuse hides what's happening. The canonical use is a shared naming suffix:

```hcl
locals {
  name_suffix = "${var.environment}"
  common_labels = {
    environment = var.environment
    managed_by  = "terraform"
  }
}
```

Define a local in `locals.tf` if it's referenced across files, or at the top of a file if it's local to that file. Name locals with descriptive nouns and underscores, like everything else.

---

## 7. count and for_each

Both create multiple instances from one block; choose by intent.

- **`for_each`** (over a `map` or `set`) when instances need distinct, non-positional identity — a set of named buckets, a map of service accounts. Keys are stable, so adding or removing one doesn't churn the others.
- **`count`** when instances are interchangeable, or for **conditional creation**: `count = var.enable_metrics ? 1 : 0`.

```hcl
resource "google_pubsub_topic" "events" {
  for_each = toset(var.topic_names)

  name    = "${each.value}-${local.name_suffix}"
  project = var.project_id
  labels  = local.common_labels
}
```

Both add complexity. Use them in moderation, and add a comment when the effect isn't immediately obvious. Avoid `count` over a list for things with identity — removing the first element renumbers and destroys/recreates everything after it; that's what `for_each` exists to prevent.

---

## 8. Module structure

A reusable module is a directory with a predictable shape:

```
modules/<module_name>/
├── main.tf
├── variables.tf
├── outputs.tf
├── versions.tf
├── README.md            # what it provisions, inputs, outputs, an example
└── examples/
    └── basic/
        ├── main.tf       # a runnable invocation
        └── README.md
```

- **Every module carries a `README.md`** documenting purpose, inputs, outputs, and at least one example invocation.
- **Examples live in `examples/`**, one subdirectory per example, each with its own `README.md`.
- **Local modules live at `./modules/<module_name>`** relative to the configuration that calls them.
- A module that **enables GCP APIs** exposes an `enable_apis` variable defaulting to `true`, and sets `disable_services_on_destroy = false` (see `02-gcp-conventions.md` §6).
- When **refactoring** resources into or between submodules, use `moved` blocks — Terraform doesn't track refactors and will otherwise destroy and recreate everything you moved.

---

## 9. Helper scripts and the unforgiving substrate

Prefer native Terraform resources over scripts. A `local-exec` provisioner or a wrapper script is a last resort, used only when no resource expresses the behavior — and when used, it carries a documented reason and ideally a deprecation plan. Organize what scripts you do keep:

- `scripts/` — scripts Terraform invokes (e.g., via `local-exec`).
- `helpers/` — operational scripts run by humans, not by Terraform. Document each in the `README.md` with example invocations; give them `--help` and argument-checking.
- `files/` — static files Terraform references but doesn't execute (startup scripts, configs). Reference them with `file()`; keep lengthy HereDocs out of HCL.

**Failure museum — the brace-glob directories.** A real predecessor repo accumulated directories literally named `{.github`, `{k8s`, and `{openapi,event_schemas,prompts`. They came from a setup script issuing something like `mkdir {.github,k8s,openapi}` that ran under a shell which **did not brace-expand** (POSIX `sh`, not `bash`), so the brace string was taken literally and a directory named `{.github` was created. The discipline that catches this is the same one the `application-code` shell-scripts reference codifies — *author for the unforgiving substrate, and verify the result on the filesystem rather than trusting the command exited zero.* `mkdir` of a literal brace string exits `0`; nothing fails loudly. Infrastructure scaffolding scripts must check what actually landed on disk (`test -d`), not assume expansion happened. Carry this example: the malformed directories are evidence that a structure-aware, result-verifying scaffold would have caught what a fire-and-forget one didn't.

---

## 10. Repository structure

Keep **infrastructure configuration separate from reusable module code**. Two patterns, both valid:

- **Monorepo** — local modules under `modules/`, deployed by root configurations that call them. Single source of truth; CI must target only the changed directories so one edit doesn't replan everything.
- **Module-per-repo** — each reusable module in its own repository (named `terraform-google-<name>` if published to a registry), versioned independently, consumed by pinned `version`.

Separate configurations by **approval and management boundary**: a foundational layer (org IAM, folders, shared networking) managed by the platform owner, distinct from per-application infrastructure. Configurations with different blast radius or different approvers belong in different state files (see `03-state-and-environments.md` §2) and often different directories or repos.

Always commit: all `.tf` files, the `.terraform.lock.hcl` dependency lock, a `.gitignore`, and a `README.md`. Never commit: state files, `.terraform/`, saved plan files, or `.tfvars` carrying secrets (see `03-state-and-environments.md` §4).
