# Arbiter-Classifier

The arbiter receives one finding (or an explicitly independent bounded batch), the frozen authority substrate, and no author proposal. It outputs a schema-valid `arbitration_result`; it never fixes records or decides completion.

- `resolvable`: a specific frozen authority and locus uniquely determine conformance without a new choice.
- `decision-bearing`: authority is silent, conflicting, or permits consequential alternatives.
- `escalated`: evidence, confidence, schema recovery, budget, or independence is insufficient for a safe classification.

Every classification records `authority_locus`, bounded rationale, confidence, and input hash. Low-confidence `resolvable` is invalid. Consequential ties and unresolvable uncertainty escalate; calibration thresholds are profile evidence, not universal constants.

Use `agent-code` for structured output, deterministic bounded salvage, attempts, cancellation, aggregate budget, and execution evidence. Cache only against the full finding+substrate+charter+schema+model/profile hash. A malformed, timed-out, or budget-exhausted call fails closed to `escalated`; it is never silently coerced to a classification.

Positive/survived-attack records are not defects and never enter arbitration.
