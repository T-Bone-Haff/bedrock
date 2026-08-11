# Reference: Frontend Testing and Evidence

This is the frontend domain overlay consumed by `testing`. It declares what
frontend evidence means; `testing` remains the primary owner of planned test
strategy and test authoring, and `debug` owns any observed failure or flake.

## Select tests from risk

| Boundary | Evidence that can establish it |
|---|---|
| Framework-free policy and data logic | Unit, property, fuzz, mutation, or contract tests as risk warrants |
| Components and hooks | DOM behavior through accessible roles/names and real user interactions |
| External seams | Versioned consumer/provider contract and runtime-invalid/skewed negative cases |
| Browser behavior | Real-browser tests against every declared engine/profile |
| Accessibility | Automated rules plus manual keyboard, resize/reflow, contrast/target review, and representative AT flows |
| Security | Executable negative cases plus a coverage map of client, backend, delivery, and external owners |
| Performance | Repeated representative scenarios under declared environment and budgets |

Tests observe behavior, not implementation details. Snapshots are supporting
evidence only. Query by semantic role and accessible name where available.
Mocks replace a declared seam, not arbitrary internals.

## Meaningful red and promotion

Mechanism behavior that can be specified before implementation follows the
`testing` skill's meaningful-red discipline. Experience behavior discovered in
a prototype is specified during promotion assessment and hardening. A clean
prototype may graduate without wholesale re-authoring when provenance,
architecture, tests, accessibility, security, maintenance, and known debt are
explicitly assessed and the production profile passes. Targeted rework or
disposal follows the evidence; mandatory rewrite is not a gate.

An already observed failure routes to `debug`. After diagnosis, its reproducer
may become regression coverage owned by `testing` and the relevant authoring
skill.

## Coverage

Coverage thresholds are declared per consumer profile and risk; this standard
does not universalize one line percentage. Each profile names line/branch/
state or mutation expectations, critical paths, allowed exclusions, and the
decision each threshold gates. Exclusions are explicit and justified; moving
behavior into an ungated directory is not an exclusion.

## Real-browser contract

Browser evidence names engines and versions, production build identity,
viewport/locale/timezone/device capabilities, and which behavior is genuinely
exercised. Applicable paths include:

- navigation, history, focus placement, dialogs and recovery;
- text resize and reflow without clipping, overlap, loss, or unusable controls;
- feature detection and fallback for permissions/media/runtime capabilities;
- resource replacement, cancellation, contention, cleanup and privacy state;
- API version skew, malformed or hostile data, stale clients and partial rollout;
- offline/update/service-worker behavior when the selected profile enables it.

A browser engine unavailable locally is `unverified`, not skipped-to-green.
Required CI must run the declared engines without skips. Browser automation
does not substitute for a named manual assistive-technology flow.

## Accessibility evidence

Automated evidence may detect semantics, names, some contrast defects, focus
order mistakes, and selected resize/reflow failures. Manual evidence records:

- exact OS, browser, assistive technology, versions, build and flow;
- keyboard order, focus visibility/placement, announcements and alternatives;
- 200% text resize and 400%/320-CSS-pixel reflow behavior;
- contrast and target-size review with applicable exceptions;
- observed results, limitations, and unresolved defects.

The evidence record says `pass`, `fail`, `unverified`, or `not_applicable`; only
`not_applicable` accepts a rationale in place of proof. Representative evidence
must not be described as universal certification.

## Test hygiene

Control clocks, randomness, locale, timezone, storage, network, permissions,
service workers, and identifiers when they affect outcomes. Restore globals,
timers, mocks, permissions, contexts, streams, workers, and storage after each
test. Await observable completion rather than sleeping. A flaky browser test is
a defect and routes to `debug`, never an accepted environmental shrug.
