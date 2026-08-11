# HEB-115 reconciliation baseline

Captured 2026-08-10 from freshly fetched `main` at `6cc85677b4a70b86d38d445bdcd202ef0f8f49ac`. Local `main`, `origin/main`, `origin/HEAD`, and the GitHub remote head matched with zero divergence. The only pre-existing worktree entry was the user-owned untracked root `AGENTS.md`.

HEB-115 was Planned with no comments, blocked only by completed HEB-111, and blocking HEB-118. HEB-116 and HEB-117 were Done through PRs 27 and 26. HEB-113 and HEB-114 remained separate Planned streams; HEB-122 remained Backlog and outside this work.

## Reconciliation

The accepted architecture requires portable actor contracts with explicit profiles and capability-honest evidence. The pre-change application and testing contracts instead treated the Haffey FastAPI/pytest binding as universal, while debug lacked a declared output/schema and safety/authorization boundary.

### application-code

| Disposition | Findings | Realization |
|---|---|---|
| Fix | APP-001, APP-002, APP-005, APP-007–010, APP-012–014, APP-016, APP-018 | Preserve routing/container safety; remove revision metadata; correct pagination, audit, correlation, middleware, logging, propagation, background work, token delegation, and supply-chain contracts. |
| Modify | APP-003, APP-004, APP-006, APP-011, APP-015, APP-017, APP-019 | Govern event-loop safety; use proportional capability profiles and HTTP-native defaults; classify readiness; define authn/authz profiles; derive performance objectives. |

### testing

| Disposition | Findings | Realization |
|---|---|---|
| Fix | TST-001, TST-002, TST-006–008, TST-010–013 | Preserve routing; correct double choice, lifespan, database isolation, provider contracts, gate identity, flakes, advanced methods, and nondeterministic evaluation. |
| Modify | TST-003–005, TST-009, TST-014 | Risk-based coverage, behavioral assertions, durable meaningful-red evidence, versioned contract conflict triage, and clear structure without mandatory metadata/comments. |

### debug

| Disposition | Findings | Realization |
|---|---|---|
| Fix | DBG-001, DBG-005–010 | Preserve routing and add evidence custody, experiment safety, layered verification, isolation selection, stop/escalation, and durable records. |
| Modify | DBG-002–004 | Prefer safe reproduction without making it absolute; separate containment/restoration, diagnosis, and permanent correction. |

## Version classification

The implemented delta changes established public binding, authority, evidence, output, and failure semantics. Under ADR-001 this is a portable-core and package major change. Derived from the live `5.0.0` manifest baseline, the working-tree version is `6.0.0`. This classification does not authorize release.
