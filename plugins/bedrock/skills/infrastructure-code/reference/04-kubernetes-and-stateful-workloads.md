# Reference: Kubernetes and Stateful Workloads

Kubernetes manifest conventions, the split between stateless and stateful workloads, and the pattern for running a stateful database (a Neo4j-class system of record) on GKE. Load this when authoring manifests or deploying anything that needs durable storage on a cluster. The cluster itself is provisioned in `02-gcp-conventions.md` §7; this is what runs on it.

## Contents

- [1. Manifest conventions](#1-manifest-conventions)
- [2. Stateless workloads — Deployment](#2-stateless-workloads--deployment)
- [3. Stateful workloads — StatefulSet](#3-stateful-workloads--statefulset)
- [4. Running a stateful database on GKE](#4-running-a-stateful-database-on-gke)
- [5. GitOps and manifest discipline](#5-gitops-and-manifest-discipline)

---

## 1. Manifest conventions

Manifests are declarative and version-controlled. Apply them with `kubectl apply` (declarative object configuration), never imperative `kubectl create`/`edit` against live objects — the file is the source of truth (§5).

- Each manifest carries the comment-block header (`01-module-structure-and-style.md` §2) in `#` YAML comments.
- Every object carries standard labels: `app`, `environment`, and `managed-by: terraform` (or the GitOps tool), so selectors and audit queries are consistent.
- Workloads live in an explicit **namespace** per application/environment, not `default`.
- Containers declare resource `requests` and `limits`, and **liveness, readiness, and startup probes** — readiness gates traffic, liveness restarts a wedged pod, startup protects a slow-booting one from premature liveness kills.

---

## 2. Stateless workloads — Deployment

A stateless workload — one whose replicas are interchangeable and hold no durable per-pod state — is a **Deployment**. (On this platform most stateless services run on Cloud Run, not GKE; reach for a Deployment when a service genuinely needs to run on the cluster.) Replicas share nothing; any pod can serve any request; scaling is just changing the replica count.

Do **not** use a Deployment for anything that needs durable per-pod storage. A Deployment's default rolling strategy starts a new pod before terminating the old one, so two pods contend for the same `ReadWriteOnce` volume and deadlock — the new pod can't mount it, the old pod won't release. That failure mode is the line between this section and the next.

---

## 3. Stateful workloads — StatefulSet

A workload that needs **stable identity and durable per-replica storage** — a database, a broker, a clustered store — is a **StatefulSet**. It gives each replica a stable hostname (`name-0`, `name-1`, …), an ordered lifecycle, and its own persistent volume that survives rescheduling.

The load-bearing pieces:

- **`volumeClaimTemplates`** — the StatefulSet generates one PersistentVolumeClaim per replica automatically; each replica keeps its own disk across restarts.
- **A headless Service** (`clusterIP: None`) — required, and you create it; it provides the stable per-pod network identity the StatefulSet relies on.
- **A StorageClass with `volumeBindingMode: WaitForFirstConsumer`** — provisions each disk in the same zone the pod is scheduled to, respecting anti-affinity and node selectors instead of stranding a disk in the wrong zone.
- **Regional persistent disks** for HA — `pd.csi.storage.gke.io` with a regional type replicates the volume across two zones, so a zonal outage doesn't take the data down. Regional SSD for a database that needs both HA and performance.
- **Pod anti-affinity across zones** — spread replicas (and their disks) across zones for availability.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: graph            # headless service for stable network identity
spec:
  clusterIP: None
  selector:
    app: graph
  ports:
    - port: 7687
      name: bolt
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: graph
spec:
  serviceName: graph
  replicas: 3
  selector:
    matchLabels:
      app: graph
  updateStrategy:
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: graph
    spec:
      containers:
        - name: graph
          image: REGION-docker.pkg.dev/PROJECT/REPO/graph:TAG
          ports:
            - containerPort: 7687
              name: bolt
          readinessProbe: { tcpSocket: { port: 7687 }, initialDelaySeconds: 20 }
          livenessProbe:  { tcpSocket: { port: 7687 }, initialDelaySeconds: 60 }
          volumeMounts:
            - name: data
              mountPath: /data
  volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes: ["ReadWriteOnce"]
        storageClassName: regional-ssd     # WaitForFirstConsumer
        resources:
          requests:
            storage: 100Gi
```

**Persistent volumes are not deleted** when a StatefulSet or its pods are deleted — Kubernetes keeps them for data safety, so cleanup is a deliberate manual act, not a side effect of `kubectl delete`. Treat that as a feature: it's the same protective instinct as `deletion_protection` on the Terraform side.

---

## 4. Running a stateful database on GKE

The Neo4j-class system of record — a clustered, self-managed graph or relational database with no managed GCP offering — is the canonical reason to take on a StatefulSet. The pattern:

- **GKE Standard, not Autopilot** (`02-gcp-conventions.md` §7) — a self-managed clustered database wants node-pool and storage-class control that Autopilot constrains.
- **StatefulSet + regional-SSD `volumeClaimTemplates`** per §3, sized to the workload; **headless Service** for the cluster's internal addressing (members find each other by stable hostname).
- **Resource `requests` == `limits`** (Guaranteed QoS) for a database — you don't want it evicted or throttled under node pressure.
- **Backup/restore is an operational obligation, not an afterthought.** A self-managed database carries its own backup lifecycle (e.g., a scheduled dump to a versioned GCS bucket) — the cluster's managed backups don't cover data inside a self-managed pod. *The specific backup tool, cadence, and cluster topology (replica count / HA) are operational-design and ADR-homed decisions, sized to real workload after dev — not asserted here. This skill establishes that the obligation exists and where the backup target lives (a versioned GCS bucket, `02` §7); the mechanism is decided in the operational design.*

Production topology (how many replicas, what HA configuration) is deliberately deferred to the operational design — don't hardcode a premature three-node assumption into the manifest; parameterize `replicas` and size it once the workload is real.

---

## 5. GitOps and manifest discipline

Deployment configuration is declarative and version-controlled, and the cluster is reconciled *to* the committed manifests — not the other way round.

- **Manifests live in version control.** Production deployment state derives from declared manifest state, not from console actions or `kubectl edit` against live objects.
- **Manifest changes go through PR review** like any other change — a deployment change is a code change.
- **Divergence is a violation.** If live state drifts from manifest state, reconcile by amending the manifest and re-applying through the pipeline — never by patching the cluster and leaving the manifest behind.
- **Rollback is declarative too.** Roll back by pointing the workload at the previous image tag with the previous manifest state (images carry both semantic version and commit SHA, per the `app-delivery-pipeline` tagging discipline). A rollback is followed by a tracking ticket capturing what failed, and the failed image is never re-deployed without an intervening fix.

*The specific GitOps tool (Argo CD, Flux, Cloud Deploy, or plain pipeline `kubectl apply`) is enterprise-bound and ADR-homed — the discipline above holds regardless of which tool enforces it.*
