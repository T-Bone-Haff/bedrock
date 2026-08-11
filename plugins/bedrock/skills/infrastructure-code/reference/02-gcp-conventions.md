# GCP identity, IAM, service, and cost profile

This reference binds the portable contract to GCP. Confirm project, region, environment, owner, data classification, and recovery objectives before resource authoring.

## Identity and IAM ownership

Use one narrowly scoped runtime or pipeline service account per trust boundary and prefer Workload Identity Federation over long-lived keys. A principal's authentication proves identity; IAM policy and environment approval grant authority.

Every managed policy surface declares one ownership model:

- **additive:** Terraform manages named members without claiming the whole policy;
- **authoritative:** Terraform intentionally owns the complete binding or policy, with import/reconciliation and protected review;
- **external:** Terraform must not mutate the policy and records the external owner.

Neither additive nor authoritative is universally safer. Reject mixed ownership of the same role/resource unless a ratified migration plan defines the transition.

## GCP resource profile

- Enable APIs deliberately and retain dependency ordering.
- Use native labels when supported and the compensating inventory from the infrastructure profile otherwise.
- Configure Artifact Registry cleanup and immutability controls, but deploy by digest; a tag remains a pointer.
- Give public ingress, database/network paths, customer-managed encryption, deletion protection, retention, and cross-region design explicit risk decisions.
- Treat GKE, Cloud Run, Cloud SQL, Pub/Sub, Secret Manager, Firestore, Memorystore, and networking as separate capability choices. Do not provision a service only because it appears in a house list.

## Cost and quota evidence

For material changes report expected units and growth driver, budget/alert ownership, quota headroom, idle/non-production controls, egress exposure, and the operator who accepts uncertainty. Estimates are evidence with assumptions, not guarantees.
