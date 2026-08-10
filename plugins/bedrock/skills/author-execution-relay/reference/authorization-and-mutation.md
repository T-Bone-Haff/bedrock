# Authorization and mutation identity

Authorization is valid only when authenticated actor, scope digest, base repository identity, issue time, expiry, nonce, revocation state, and intended gates all match. Reuse after execution or expiry is a replay and fails closed.

Mutation identity records path and operation plus content digest, file type, executable mode, symlink target, rename source, deletion, relevant attributes, and encoding. The executor verifies before and after state through the enforcing boundary when one exists.

Prompt-only relays may carry the same fields as evidence and tripwires, but must state that an executor can ignore them. High-assurance relays require a validating wrapper or host transaction capability; absent that capability, stop or select a lower profile without the enforcement claim.
