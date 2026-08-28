# Product-Owned Runner Binding

This optional binding connects the portable review contract to an external runner owned by the consuming product. It is not a Bedrock runner implementation, creates no supported product binding by itself, and carries no private tracker state, repository path, prompt snapshot, credential, or runtime assumption.

Before selecting runner-backed review, resolve and record from the live product authority:

1. product workflow-binding identity, product-defined opaque immutable version, content digest, owner, and authority boundary;
2. runner identity, artifact digest, and immutable full SemVer 2.0.0 identity, including valid prerelease or build metadata when present;
3. explicit portable-core and review-schema versions plus the compatibility-manifest digest that admits the combination;
4. actor charters, arbitration capability, durable ledger, identity and lifecycle gates, cancellation, budgets, and evidence export;
5. exact command or API entrypoint, inputs, outputs, validator profile, and invocation digest;
6. a named claim subject binding the substrate, workflow binding, runner, contract and schema versions, compatibility manifest, invocation, and validator profile;
7. the complete required actor and gate populations, one identified outcome and evidence digest for every member, and ledger and evidence-manifest digests;
8. a differently-shaped verification or falsification record that names its instrument, binds the same claim-subject digest, and records confirmation or refusal; and
9. fresh execution evidence showing every required actor and gate ran against the declared substrate.

The product authority owns the workflow-binding version grammar; Bedrock treats that value as opaque and verifies its immutability through the binding digest. Runner versions use the complete SemVer grammar, not a core-only `X.Y.Z` subset. A boolean assertion such as “schemas compatible” or “fresh evidence present” is not replayable evidence and cannot support a runner-backed claim.

The product also proves that it owns sequencing, durable state, retries, and operational posture while Bedrock actors retain their bounded judgments.

If any required capability is absent, incompatible, proposed rather than accepted, or unable to emit distributable evidence, downgrade to multi-perspective or direct review, or stop when runner-backed proof is required. Do not fill gaps with copied prompts, hand-evaluated gates, tracker assertions, or an emulated loop.

Existing product implementations are prior art and evidence only. This binding neither promotes one wholesale nor admits any reusable component. Only fresh evidence from the declared binding and runner may support a runner-backed convergence claim.
