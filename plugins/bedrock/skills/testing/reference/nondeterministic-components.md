# Nondeterministic evaluation contract

Mechanical gates receive deterministic tests; judgment distributions receive evaluation. An LLM or stochastic component exempts none of its deterministic parsing, validation, routing, budgeting, identity, or terminal machinery from ordinary tests.

## Evaluation identity

Every retained evaluation report records:

- dataset name, version, digest, population, sampling method, sample size, and exclusions;
- system/model/provider/version, prompt artifact version/digest, decoding parameters, and tool/capability versions;
- evaluator/judge identity, rubric version, independence relationship, calibration dataset/results, and known error asymmetry;
- preregistered metrics, thresholds, uncertainty/confidence method, repeated-draw policy, and stop rule;
- contamination/leakage controls, drift comparison, environment/time, token/spend/latency budgets, and raw-content retention policy; and
- every failed, null, excluded, or retried run. Retries do not overwrite the original observation.

## Datasets and judgments

Use representative positives, negatives, boundary cases, adversarial cases, and subgroup/risk slices. Version changes to dataset, prompt, judge, or acceptance policy independently. Do not compare runs as equivalent when a load-bearing identity changed.

Human or model judges are instruments, not authority. Calibrate cold against known labels, inspect false-pass and false-fail behavior, prevent self-judging where independence matters, and escalate low-confidence consequential calls. Confidence intervals or another justified uncertainty estimate accompany aggregate rates; one plausible output is not evidence of reliability.

## Replays and content safety

Prefer sanitized, consented, policy-permitted recorded fixtures for deterministic replay at the parser/mechanism boundary. Do not persist raw prompts or completions by default. Hash-only or derived fixtures may be appropriate when content classification forbids retention. A replay proves behavior on retained emissions, not current live-model quality.

## Meaningful red and change evidence

For deterministic mechanism, use an ordinary meaningful failing test. For judgment behavior, preregister the criterion and observe the baseline fail before claiming the change corrected it. Re-run the same identified evaluation plus any declared non-regression set. Report uncertainty and spend; do not cherry-pick draws or silently purchase retries until a threshold passes.

## Ownership boundary

`testing` authors the evaluation strategy and evidence contract. `agent-code` supplies model-call implementation constraints. A product-owned runner may execute repeated draws, budgets, and durable state, but it does not redefine the evaluation's normative pass criteria.
