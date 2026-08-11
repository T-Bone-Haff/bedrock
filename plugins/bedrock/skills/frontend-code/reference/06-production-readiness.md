# Production readiness and capability profiles

Every consumer profile dispositions each row as `required`, `not_applicable`
with rationale, or `unverified` and blocking/escalated. Presence in this list
does not make one implementation mandatory.

| Concern | Required declaration/evidence |
|---|---|
| Browser/runtime support | Engines/versions, devices, capabilities, fallback and update policy |
| Routing/navigation | URL ownership, history/deep links, focus/announcement, not-found/error behavior |
| Forms | Validation ownership, labels/instructions, error summary/focus, submission/idempotency behavior |
| Internationalization | Locales, message/format authority, directionality, expansion and fallback |
| Telemetry | Events/metrics, consent/data classification, sampling, failure and privacy boundaries |
| Offline/update/service worker | Applicability, cache/version strategy, stale-client behavior, logout cleanup and rollback |
| SSR/hydration | Applicability, server/client boundary, hydration mismatch, streaming/error and browser-only capability behavior |
| State library | Decision criteria, ownership, selectors, persistence, SSR, debugging, migration and bundle cost |
| Security | Complete browser-security coverage map and executable negatives |
| Accessibility | Automated plus manual evidence profile and limitations |
| Performance | Named user scenarios, environment, metrics, budgets, repetitions and failure behavior |

## Performance

Select metrics that correspond to the named user scenario: emitted/compressed
bundle size, startup/navigation/interaction latency, long tasks, memory/resource
retention, network/data cost, or domain timing. Establish budgets before the
measurement used to judge them. Retain at least the declared repetition count,
environment/tool identity, raw results, aggregation, variance/limitations, and
pass/fail calculation. A synthetic score or bundle size alone is not a universal performance claim. Do not generalize one fixture or synthetic score.

## Delivery seam

Frontend requirements end at commands, expected outputs, browser support,
evidence, app readiness, and sensitivity declarations. The delivery authority
chooses workflow placement/caching and owns artifact construction, hosting,
headers, source-map publication, promotion, deployment, rollout, and production
verification. A frontend profile may consume those results but must not redefine
their machinery.
