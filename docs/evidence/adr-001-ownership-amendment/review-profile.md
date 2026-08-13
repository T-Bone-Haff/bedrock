# ADR-001 ownership amendment review profile

- Profile: multi-perspective review.
- Aggregation: adjudicated merge.
- Required actor set: LAA, SA, and EA in three context-isolated invocations, followed by a separate cross-set coherence pass after their outputs are frozen.
- Substrate: the frozen proposed amendment, affected carriers, accepted baselines, ratified design intent, repository authority, selected skill contracts, and review schemas listed in `substrate-manifest.sha256`.
- Reviewer tools: read-only filesystem inspection of the frozen bundle; no network, repository writes, or external mutations.
- Evidence location: `docs/evidence/adr-001-ownership-amendment/` for retained profile, hashes, normalized results, coherence report, and adjudication ledger. Temporary frozen bytes live outside the repository and are identified by digest.
- Data classification: internal engineering design; no credentials or intentionally sensitive content.
- Redaction: none required after source inspection; finding bodies must not reproduce unrelated attachment content.
- Model/provider/region: Codex sub-agent service available to this task; region is not exposed by the host and is therefore unverified.
- Budgets: three concurrent reviewer invocations; one result per reviewer; concise schema-valid output; no retries unless the output is malformed; no runner or iterative convergence cycle.
- Spend/latency ceilings: host-managed and not observable as a monetary amount; stop on a failed required reviewer rather than silently substituting another stance.
- Retention/access: normalized findings and hashes retained in the repository draft; full sub-agent conversations are not retained as review evidence.
- Cancellation: the authoring agent may interrupt a reviewer that exceeds the host turn or produces work outside its charter; cancellation fails the requested profile unless a bounded retry succeeds.
- Ratification and writes: reviewers cannot fix, classify, ratify, commit, push, or publish. Tad Haffey retains acceptance authority.
- Completion claim: “multi-perspective review completed” only if all three stance results and the later cross-set pass are valid. This profile never claims mechanical convergence.
