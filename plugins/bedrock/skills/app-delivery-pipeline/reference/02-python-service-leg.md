# Service artifact and deployment leg

Run the gate commands owned by `application-code` and `testing`; do not redefine their semantics here. In the Haffey profile, pull requests build and test with registry publication explicitly configured as `push: false` and without deployment authority. Trusted release workflows build once, scan, generate SBOM/provenance, push, and promote the digest.

Tags may carry semver and source identity for discovery, but deployment and promotion use `sha256:` digest. Registry immutability and cleanup policies strengthen custody; they do not turn a mutable tag into content identity.

Declare exactly one desired-state owner per environment. Direct deploy profiles mutate the selected service with protected authority. GitOps profiles update the authoritative declaration and observe reconciliation; they do not also issue a direct deployment.

## Migration contract

The release manifest identifies migration owner, artifact/schema identity, compatibility window, ordering, backup/restore gate, idempotency and retry policy, and rollback limit. Prefer expand/contract across compatible releases. A migration that cannot roll back must have a forward-recovery path and explicit approval before traffic transition.

## Verification and rollback

Platform rollout is necessary but insufficient. Verify an application endpoint or synthetic transaction, readiness/dependency signal, expected artifact digest, and critical dependency behavior. Define timeout, evidence, rollback trigger, rollback authority, previous digest, and schema compatibility. If rollback cannot restore service safely, stop and escalate rather than reporting success.
