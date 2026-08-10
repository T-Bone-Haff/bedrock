# HEB-116 reconciliation baseline

Captured 2026-08-10 before implementation from `main` at `d05a238750cfa43b33d95ffb2704787bcdae732e` after fetching `origin`. Local `main`, `origin/main`, and `origin/HEAD` matched; the sole pre-existing worktree entry was the user-owned untracked root `AGENTS.md`.

The accepted HEB-111 architecture establishes provider/runner-neutral actor cores, explicit optional profiles, and capability-honest completion claims. HEB-110 supplies the safety floor. HEB-117 landed the preceding authoring contracts. RBT-72 remained an in-progress, proposed SOFIA recipe/kernel specification: useful profile input, but not durable authority or a prerequisite for the portable HEB-116 correction.

## Disposition realization

| Finding | Disposition | Repository realization |
|---|---|---|
| AGT-001 | Fix | Frontmatter routes central LLM-call implementation and excludes review/debug/relay work. |
| AGT-002 | Fix | Content capture is off by default and gated by classification, consent, redaction, access, location, and retention. |
| AGT-003 | Fix | Native/whole parsing precedes one bounded candidate grammar; only one schema-valid candidate is accepted and ambiguity fails. |
| AGT-004 | Modify | Provider-neutral core plus optional Anthropic/Python profile. |
| AGT-005 | Fix | One aggregate deadline/attempt/spend envelope covers transport, content recovery, fallback, and tools. |
| AGT-006 | Fix | Typed bounded tool-loop contract covers correlation, unknown/duplicate ids, parallelism, partial failure, stop reasons, streaming, schema versions, and iteration exit. |
| AGT-007 | Fix | Draft-2020-12 execution schema, fixtures, validator, and regression tests. |
| AGT-008 | Modify | Rationale/explanation fields are schema-specific and bounded, not universal. |
| AGT-009 | Fix | Token, spend, time, iteration, model, rate, concurrency, cancellation, and circuit-breaker posture are declared and observable. |
| AGT-010 | Modify | Installed scope is code-level LLM/tool invariants; system security remains with owning standards. |
| AGT-011 | Fix | Private run claims and private paths are removed; installed evidence is distributable and reproducible. |
| AGT-012 | Modify | Prompt artifact versions are separate from capability/schema compatibility, negotiation, and deprecation. |
| DRL-001 | Modify | Portable review core and conditional Haffey/SOFIA adapter; explicit downgrade or stop when capability is absent. |
| DRL-002 | Fix | Private prompt mirrors are removed; references are portable contracts and schemas. |
| DRL-003 | Fix | Private empirical claims are removed; claim gate requires retained distributable execution evidence. |
| DRL-004 | Fix | Cosmetic findings are nonblocking and decision-bearing defects must be BLOCKING or MATERIAL. |
| DRL-005 | Modify | Empty reviewer results are valid; optional survived attacks are specific evidence, never required praise. |
| DRL-006 | Fix | Identity includes normalized targets, locus, stance, and claim; related variants remain independently visible. |
| DRL-007 | Fix | Completion evaluates identity, severity, lifecycle, recurrence, decisions, and instrument health—not counts. |
| DRL-008 | Fix | Arbitration has independence-aware batching, complete-input caching, aggregate budgets, bounded recovery, cancellation, and fail-closed escalation. |
| DRL-009 | Fix | Frozen substrate is delimited as untrusted data; narrated instructions and approvals have no authority. |
| DRL-010 | Modify | Union/intersection/sampling/adjudicated-merge tradeoffs are declared by risk and measured; none universally dominates. |
| DRL-011 | Modify | Asymmetric error cost informs calibration while uncertainty and consequential ties escalate. |
| DRL-012 | Fix | Profiles declare privacy, spend, token, latency, classification, redaction, model/region, cancellation, retention, access, and audit controls. |
| DRL-013 | Modify | Direct, multi-perspective, and runner-backed profiles have distinct exits; only executed runner-backed gates may claim mechanical convergence. |

## Version classification

The live delta changes the meaning and binding of two public skill contracts and invalidates consumers that depended on the former Anthropic/SOFIA hard binding or emulation semantics. Under ADR-001, that is a major compatibility change. From the live `4.0.0` manifest baseline, the derived working-tree version is `5.0.0`.
