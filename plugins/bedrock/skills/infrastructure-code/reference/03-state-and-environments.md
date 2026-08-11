# State, environment, bootstrap, and recovery profile

## State contract

For the Haffey profile, use a protected GCS backend with versioning, uniform access, retention appropriate to recovery objectives, and the backend's actual locking semantics. Never describe a backend as locked without verifying the selected Terraform/backend behavior. Restrict state access, audit it, and treat every state version and saved plan as sensitive.

Keep runtime secret payloads out of Terraform when possible: pass secret identifiers and let the workload retrieve values through its runtime identity. `sensitive = true` only redacts display. If a provider must receive a payload, document the exception, affected state, rotation, access, and cleanup.

```gitignore
*.tfstate
*.tfstate.*
*.tfplan
*.tfvars
.terraform/
```

Commit `.terraform.lock.hcl`; do not ignore it.

## Environments and bootstrap

Use an explicit state target per environment/profile and prevent accidental workspace or project substitution. Backend/bootstrap resources have their own lifecycle: initial creation method, import boundary, owners, break-glass procedure, drift checks, and retirement path must be recorded. Bootstrap must not depend circularly on the state it creates.

## Recovery contract

Before destructive or stateful work declare:

- RPO and RTO with accountable owner;
- backup scope, encryption, retention, and custody;
- restore procedure and most recent successful restore evidence;
- state lineage/serial recovery procedure and approval boundary;
- provider/API failure and partial-apply recovery;
- rollback impossibilities and escalation trigger.

State versioning is not a database backup. A successful snapshot is not restore proof. Restore drills must validate the recovered service or data behavior.
