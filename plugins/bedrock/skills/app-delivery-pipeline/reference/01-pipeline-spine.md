# Portable pipeline spine and Haffey workflow profile

## Event and release model

The delivery profile declares trusted verification and release events. Resolve source association for merge commits, squash merges, merge queues/batches, reverts, direct pushes, and manual release. Ambiguous association fails closed; do not guess a “just merged PR.”

Aggregate version intent across every included change. Support `semver:major`, `semver:minor`, `semver:patch`, and explicit `semver:none`; incompatible or missing intent fails closed unless an authorized override with rationale is retained. A revert records whether it reverses version intent. Version publication is derived from a trusted release decision, never only a mutable branch name.

## Workflow trust

PR verification starts without deployment credentials. Use least-privilege `permissions`, SHA-pinned third-party actions, protected environments, and short-lived federation. Treat fork and untrusted preview code as hostile. Never run untrusted code in a privileged event context.

Cancel stale verification when safe. Serialize environment mutation using an environment/artifact key and `cancel-in-progress: false`. A newer candidate may wait or be rejected; it must not interrupt a mutation already changing shared state.

## Artifact and provenance

Build once and identify by digest. Retain an SBOM plus builder, workflow revision, source commit/tree, declared inputs/dependencies, build time, artifact digest, retention, attestation/signature mechanism, and verification result. If platform attestation is unavailable or limited for private repositories, record the gap and use the strongest available signed/verifiable record without claiming equivalence.

The release manifest is the audit spine. It binds release event and intent to artifact, desired-state owner, approvals, migrations, deployment, behavioral verification, rollback, and retention.

## Haffey workflow profile

GitHub Actions uses pinned actions, protected GitHub Environments, Artifact Registry or the selected static artifact store, and GCP WIF constrained by repository, ref/environment, audience, and job intent. Branch topology is declared by the delivery profile: trunk/main-only, feature-to-main, develop-to-main, release branch, and merge queue are supported bindings when their event associations are defined.
