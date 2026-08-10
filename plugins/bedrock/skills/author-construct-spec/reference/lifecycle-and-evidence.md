# Construct-spec lifecycle and evidence

## Evidence relocation transaction

1. Identify the source and destination.
2. Copy or add a durable link; do not delete the source.
3. Verify content integrity, permissions, retention, and cold-reader reachability.
4. Record provenance and a rollback action.
5. Use the destination in a cold-read or cold-build check.
6. At a later explicit gate, retire only a proven redundant copy.

Permission loss, link rot, partial writes, digest mismatch, and rollback failure are failed transitions. The source remains authoritative until the destination passes.

## Lifecycle distinctions

- **Accepted design:** the operator accepts the intended design.
- **Implemented:** the named implementation exists at a durable identity.
- **Verified:** required obligations passed against that identity.
- **Graduated:** a verified rule moved to a governed standing authority after post-build review and operator approval.
- **Retired:** the artifact no longer governs and points to its successor or reason.

A graduated destination declares type, owner, authority, location, revision policy, discovery, review trigger, supersession, rollback, and retirement.
