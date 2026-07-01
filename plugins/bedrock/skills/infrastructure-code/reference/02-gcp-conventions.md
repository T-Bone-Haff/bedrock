# Reference: GCP Conventions

The GCP-specific layer — provider configuration, resource naming and labelling, environment-conditional hardening, IAM, API enablement, and the conventions for the platform's service set. Load this when provisioning any Google Cloud resource. The Terraform *shape* (file layout, naming, ordering) is `01-module-structure-and-style.md`; this is what goes inside the resources.

## Contents

- [1. Provider configuration and pinning](#1-provider-configuration-and-pinning)
- [2. Naming and labels](#2-naming-and-labels)
- [3. Environment-conditional hardening](#3-environment-conditional-hardening)
- [4. IAM and service accounts](#4-iam-and-service-accounts)
- [5. Networking and private access](#5-networking-and-private-access)
- [6. API enablement](#6-api-enablement)
- [7. The service set](#7-the-service-set)

---

## 1. Provider configuration and pinning

The `terraform` block (in `versions.tf`) pins the binary and the provider; the default provider config lives in `providers.tf`.

```hcl
# versions.tf
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
  }
}
```

```hcl
# providers.tf
provider "google" {
  project = var.project_id
  region  = var.region
}
```

Always define a default provider configuration. If you need a second region or project, use a provider `alias`, define the default first, and put `alias` as the first parameter of the aliased block. Review version pins regularly (a tool like Dependabot automates the PRs) — pinning buys stability at the cost of missing fixes, so the pin is a thing you maintain, not set and forget.

---

## 2. Naming and labels

Resource *names* in GCP are project-scoped and often immutable, so build them from a suffix local rather than hand-typing the environment tail:

```hcl
locals {
  name_suffix   = var.environment
  common_labels = {
    environment = var.environment
    managed_by  = "terraform"
  }
}

resource "google_sql_database_instance" "state" {
  name = "app-state-${local.name_suffix}"
  # ...
  settings {
    user_labels = local.common_labels
  }
}
```

Every resource that supports labels carries at least `managed_by = "terraform"` and `environment` — `managed_by` so a human in the console knows not to hand-edit it, `environment` so cost and audit queries can slice by tier. Add `sensitivity = "high"` on resources holding secrets (Secret Manager secrets, signing keys).

For units, follow GCP's own convention: binary prefixes (Gi, Mi) for storage, decimal (G, M) for everything else.

---

## 3. Environment-conditional hardening

One module serves all environments; the *hardening* flexes on `var.environment`. Production gets the protective settings; non-production trades them for cost and iteration speed. Drive this from the variable, not from separate prod/non-prod modules.

```hcl
resource "google_sql_database_instance" "state" {
  name                = "app-state-${local.name_suffix}"
  database_version    = "POSTGRES_15"
  deletion_protection = var.environment == "prod"

  settings {
    tier              = var.db_tier
    availability_type = var.environment == "prod" ? "REGIONAL" : "ZONAL"

    backup_configuration {
      enabled                        = true
      point_in_time_recovery_enabled = var.environment == "prod"
    }

    ip_configuration {
      ipv4_enabled = false           # private IP only — see §5
      ssl_mode     = "ENCRYPTED_ONLY"
    }
  }
}
```

The conditional levers, by service:

- **`deletion_protection = var.environment == "prod"`** on clusters, databases, and any stateful resource — prod can't be `terraform destroy`'d out from under you; non-prod stays disposable.
- **`availability_type` REGIONAL** (Cloud SQL) and **HA tiers** (Memorystore `STANDARD_HA`) in prod; ZONAL/BASIC elsewhere.
- **`binary_authorization` ENFORCE** (GKE) in prod; DISABLED in non-prod.
- **Point-in-time recovery** and longer backup retention in prod.

These are defaults, not law (the misfit rule applies) — but a stateful prod resource without deletion protection is the kind of exception that needs a stated reason.

---

## 4. IAM and service accounts

**Additive, never authoritative.** Use `google_project_iam_member` / `google_service_account_iam_member` (additive — grants one binding) rather than `google_project_iam_policy` / `_iam_binding` (authoritative — overwrites *all* bindings, silently stripping roles Google manages automatically). The authoritative forms are a foot-gun on any project that also has console- or Google-managed bindings.

```hcl
resource "google_service_account" "ingestion" {
  account_id   = "ingestion-${local.name_suffix}"
  display_name = "Ingestion service (${var.environment})"
  project      = var.project_id
}

resource "google_project_iam_member" "ingestion_pubsub" {
  project = var.project_id
  role    = "roles/pubsub.publisher"
  member  = "serviceAccount:${google_service_account.ingestion.email}"
}
```

**Least privilege.** One service account per workload, scoped to exactly the roles it needs — not a shared catch-all with `roles/editor`. **Keyless.** Pods authenticate via Workload Identity (`workload_pool = "${var.project_id}.svc.id.goog"` on the cluster, plus a `roles/iam.workloadIdentityUser` binding mapping the KSA to the GSA); CI authenticates via Workload Identity Federation (see `05-delivery-pipeline.md` §4). Never create a `google_service_account_key`, never download one, never commit one.

---

## 5. Networking and private access

Default to private. Services don't get public IPs; databases and caches are reachable only on the VPC.

- **Cloud SQL / Memorystore** use private IP. This requires a Service Networking connection: reserve a `google_compute_global_address` (purpose `VPC_PEERING`) and a `google_service_networking_connection`, and `depends_on` it from the instance so the private range exists first.
- **GKE** runs as a **private cluster** (`enable_private_nodes = true`), with `master_authorized_networks` listing the CIDRs allowed to reach the control plane.
- **Cloud SQL** sets `ipv4_enabled = false` and `ssl_mode = "ENCRYPTED_ONLY"`; **Memorystore** sets `transit_encryption_mode = "SERVER_AUTHENTICATION"`.

Non-production and production live in **separate GCP projects** — never shared databases, secret stores, or service identities across the boundary. (The project provisioning itself is enterprise-bound and ADR-homed; the isolation *requirement* is a convention.)

---

## 6. API enablement

Enable required services with `google_project_service`. When a module enables APIs, gate it behind an `enable_apis` variable (default `true`) and set `disable_services_on_destroy = false` — otherwise destroying one instance of the module can disable an API another instance still needs.

```hcl
resource "google_project_service" "required" {
  for_each = var.enable_apis ? toset(var.required_apis) : toset([])

  project                    = var.project_id
  service                    = each.value
  disable_on_destroy         = false
}
```

---

## 7. The service set

Conventions for the platform's GCP services. Each is a sketch of the load-bearing settings, not a full resource — the hardening conditionals (§3), labels (§2), and private access (§5) apply throughout.

**GKE.** Private cluster, Workload Identity enabled, `release_channel` `REGULAR`, managed Prometheus on. **Use GKE Standard for self-managed stateful workloads** (a clustered database) where you need node-pool and storage-class control; Autopilot is acceptable for stateless services but constrains the node/storage control a self-managed stateful database wants. *(This is a design-over-code call: where a predecessor ran a stateful database on Autopilot, design intent for self-managed clustered storage wins — flag it rather than inherit it. The stateful-workload manifests are `04-kubernetes-and-stateful-workloads.md`.)*

**Cloud Run.** The default for stateless FastAPI services. `ingress = "INGRESS_TRAFFIC_INTERNAL_ONLY"` unless the service is deliberately public; `min_instance_count` 0 in non-prod (scale to zero), ≥1 in prod; VPC access for private backends.

**Cloud SQL (PostgreSQL).** Private IP, SSL-only, automated backups with PITR in prod, `deletion_protection` in prod, declared `database_flags` for connection/checkpoint logging.

**Firestore.** The immutable-snapshot store. Native mode; one database per environment; rules and indexes are themselves IaC.

**Pub/Sub.** Topics and subscriptions with explicit `message_retention_duration`, a **dead-letter topic** with `max_delivery_attempts`, and a `retry_policy` (min/max backoff). Set `retain_acked_messages = true` where replay/audit needs it.

**Memorystore (Redis).** `STANDARD_HA` in prod / `BASIC` elsewhere, transit encryption on, private (authorized network).

**Secret Manager.** `user_managed` replication pinned to the region; `sensitivity = "high"` label. Secrets are *referenced* by services at runtime (and by Terraform via data sources), never written into config or state.

**Artifact Registry.** One Docker repository per environment; the build pipeline pushes here, the runtime pulls. Images tagged with both semantic version and commit SHA (the tagging discipline is the `application-code` skill's; the registry is provisioned here).

**GCS.** Versioning enabled on buckets holding state or snapshots; `prevent_destroy` on the state bucket; uniform bucket-level access; access restricted to the pipeline SA and admins.
