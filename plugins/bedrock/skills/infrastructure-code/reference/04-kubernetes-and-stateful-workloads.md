# Workload, storage, and recovery profiles

Choose the controller from workload identity and rollout semantics:

- use a Deployment for interchangeable replicas, including consumers of shared or external durable storage;
- use a StatefulSet when stable ordinal identity, stable network identity, or per-replica volume identity is required;
- use Job/CronJob for bounded work; use a platform-native service when the selected profile justifies it.

Durable storage alone does not require a StatefulSet. A regional persistent disk alone does not establish application high availability; quorum, attachment/failover semantics, topology, disruption behavior, replication, and tested recovery determine that claim.

Apply least-privilege service accounts, non-root security context, read-only filesystem where compatible, resource requests/limits derived from evidence, topology/disruption controls, and restricted network access. Probes are capability-based: startup, readiness, and liveness each require a meaningful signal and failure policy. Do not add a probe that can amplify an external dependency outage or restart a healthy process.

```yaml
containers:
  - name: app
    image: us-docker.pkg.dev/example/app@sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef
    securityContext:
      allowPrivilegeEscalation: false
      runAsNonRoot: true
```

## Delivery and authority seam

Infrastructure code owns cluster/platform resources and may declare a workload shape. `app-delivery-pipeline` owns application artifact promotion and deployment. Declare exactly one desired-state writer for each environment: direct deploy, GitOps controller, or another profile. If GitOps owns desired state, delivery changes the authoritative declaration and waits for controller reconciliation; it does not also run `kubectl apply`.

Bind workload deployment to an artifact digest. Record backup and restore ownership, RPO/RTO, disruption budget, rollout/rollback mechanics, schema compatibility, and the post-deploy behavior checks delegated to application delivery.
