# Product-Owned Runner Binding

This optional binding connects the portable review contract to an external runner owned by the consuming product. It is not a Bedrock runner implementation, creates no supported product binding by itself, and carries no private tracker state, repository path, prompt snapshot, credential, or runtime assumption.

Before selecting runner-backed review, resolve and record from the live product authority:

1. product workflow-binding identity, immutable version, owner, and authority boundary;
2. runner identity, immutable SemVer, and compatible portable-core and review-schema versions;
3. actor charters, arbitration capability, durable ledger, identity and lifecycle gates, cancellation, budgets, and evidence export;
4. exact command or API entrypoint, inputs, outputs, and validator profile;
5. proof that the product owns sequencing, durable state, retries, and operational posture while Bedrock actors retain their bounded judgments; and
6. fresh execution evidence showing every required actor and gate ran against the declared substrate.

If any required capability is absent, incompatible, proposed rather than accepted, or unable to emit distributable evidence, downgrade to multi-perspective or direct review, or stop when runner-backed proof is required. Do not fill gaps with copied prompts, hand-evaluated gates, tracker assertions, or an emulated loop.

Existing product implementations are prior art and evidence only. This binding neither promotes one wholesale nor admits any reusable component. Only fresh evidence from the declared binding and runner may support a runner-backed convergence claim.
