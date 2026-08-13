# Ratified design intent — Bedrock orchestration ownership boundary

This file freezes the operator-supplied design intent for review. It is review substrate, not an independently reusable governance standard.

## Governing principle

Product-owned orchestration with evidence-driven extraction and promotion of reusable components into Bedrock.

## Ownership boundary

- Products own workflow meaning, policy, agent or actor rosters, authority, state transitions, operational posture, and product-specific composition.
- Bedrock owns only selected reusable actor contracts, schemas, primitives, standards, templates, and evidence conventions that pass an evidence-driven promotion test.
- No universal orchestration kernel or domain-specific language is presumed.
- Product controllers may use bounded reusable command/result seams.
- Capability is separate from decision authority; invocation grants exist outside prompts and models.
- Authorized agents may delegate to bounded sub-agents under product policy, including parallel specialist testing, with declared fanout, depth, aggregate budget, tool, data, and authority constraints.
- SOFIA's current `agent-loop` is an incubator and evidence source, not something to promote wholesale.
- Legacy material is evidence and input: evaluate useful implementation candidates and preserve the rest without compatibility obligation.

## Promotion-test status

The operator separately ratified a five-part promotion test covering real-product proof, same-reason reuse likelihood, removal of product assumptions, reuse value versus stable-contract maintenance, and originating-product reconsumption without a private fork. This ADR transaction may reference the promotion principle but must not silently establish the separate reusable governance standard or its proving process.

## Adjacent context that this transaction must not decide

- Durability profiles D0–D3, including SOFIA's initial D2 posture and potentially consequential HEX D3 flows.
- Transactional current state, immutable journals, versioned artifacts, logical idempotence, or whether full event sourcing is later warranted.
- Separation of execution evidence from domain reasoning beyond the boundary needed by Bedrock contracts.
- SOFIA's initial Markdown document-review workbench, CLI/web surfaces, or adoption into governed SOFIA reasoning.
- HEX implementation, topology, workflow meanings, or operating posture.
- A universal orchestration runtime, kernel, control plane, recipe schema, or DSL.
