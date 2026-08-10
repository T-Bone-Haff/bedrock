# Decision-record lifecycle and relations

Every record declares owner, status, revision policy, verification state, review trigger, successor, and retirement condition. Proposed dependencies also declare assumption, risk, expiry, and promotion criteria.

Relations are directional. `A implements B` does not imply that B depends on A unless separately recorded. Supersession chains retain all nodes; retirement changes applicability, not historical existence.

When a target changes, inspect inbound and outbound relations. Repair current references, record explicit temporary exceptions with owners and expiry, and verify graph integrity before closing the amendment.
