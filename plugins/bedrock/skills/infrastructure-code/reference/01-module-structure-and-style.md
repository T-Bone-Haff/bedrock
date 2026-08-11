# Terraform structure and dependency profile

This is the Haffey Terraform profile. The portable requirements are explicit dependency resolution, comprehensible module interfaces, capability-aware metadata, and evidence that the selected graph was reviewed.

## Dependency contract

- `required_version` and provider constraints express a reviewed compatibility range.
- Commit the dependency lock file. The lock selection—not a misleading exact constraint—is the reproducible provider resolution.
- Registry modules use immutable reviewed versions; source or VCS modules use immutable commits.
- CI verifies formatting, initialization from the lock, validation, lint/policy/security gates, and dependency drift.

```hcl
terraform {
  required_version = ">= 1.9, < 2.0"
  required_providers {
    google = { source = "hashicorp/google", version = "~> 6.0" }
  }
}
```

The lock file must select an allowed provider and carry checksums for supported platforms. Updating it is an explicit dependency transaction.

## Module shape

Prefer a small root with `versions.tf`, `providers.tf`, `variables.tf`, `locals.tf`, resource-focused files, `outputs.tf`, tests, and a README that states inputs, outputs, security/recovery assumptions, and ownership. Environment-specific values have no defaults. Validate identifiers and bounds close to the variable.

Use `for_each` for stable keyed identity; use `count` only when positional identity is intentional. Avoid hidden provider configuration in reusable child modules. Make dangerous outputs sensitive and expose identifiers rather than secret payloads.

## Metadata capability

Do not demand labels from resource types that cannot carry them. The infrastructure profile declares `metadata.supported`, required keys where supported, exemptions, and compensating inventory. Naming and external inventory must preserve owner, environment, system, data classification, and lifecycle when native labels are absent.

Generated files and manifest headers are repository-profile conventions, not portable safety properties. Apply them only when the repository declares them.
