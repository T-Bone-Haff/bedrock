# Convergence Machinery

This is a portable capability contract, not executable machinery. A profile is runner-backed only when a declared versioned runner actually implements and executes these gates against a durable ledger.

## Ledger invariants

- Finding identity includes normalized targets, locus, stance, and claim. Related variants remain linked but independently visible.
- Severity and lifecycle are independent fields. Counted severities are `BLOCKING` and `MATERIAL`; `COSMETIC` never blocks.
- A decision-bearing defect must use `BLOCKING` or `MATERIAL`; any other pair is invalid and aborts routing.
- Lifecycle records first admission, closure evidence, reopen events, supersession/relations, arbitration, and escalation. Reopening the same identity is recurrence.
- Every required actor and arbitration call has a typed outcome. Parse loss, missing output, exhausted budget, or invalid schema makes the instrument unhealthy.

## Mechanical exits

- `HALT_DECISION`: any open decision-bearing finding, unresolved consequential arbitration, or required operator choice.
- `CONTINUE`: open resolvable counted findings remain, the instrument is healthy, and the run budget permits another author/review pass.
- `CONVERGED`: no open counted finding, no open or escalated decision-bearing finding, no unresolved recurrence, all required actors/gates succeeded, and all evidence validates.
- `INCOMPLETE`: required capabilities did not execute, evidence is invalid/missing, the instrument is unhealthy, or the run budget ended without satisfying another exit.

Raw finding counts and count plateaus are diagnostic metrics, not identity-aware convergence predicates. A plateau may trigger escalation under a declared policy, but cannot by itself prove oscillation or non-convergence. Recurrence, contradictory lifecycle transitions, and unresolved identity relations are evaluated directly.

## Claim gate

A runner-backed convergence claim cites the profile and runner version plus a retained manifest containing substrate/prompt/schema hashes, model/profile configuration, budgets and usage, actor outcomes, complete ledger, arbitration records, gate output, and validator output. If any applicable runner or gate was reasoned, emulated, or omitted, this is not a conforming runner-backed profile and may not claim mechanical convergence.
