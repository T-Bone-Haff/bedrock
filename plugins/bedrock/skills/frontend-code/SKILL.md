---
name: frontend-code
description: "Author or conform browser-facing application behavior under a portable frontend contract, then bind it to a declared stack profile. Use for components, state and data seams, responsive and accessible interaction, browser capabilities and media, client security, performance obligations, or prototype promotion. Do not use for backend enforcement (application-code), planned test strategy alone (testing), an observed failure (debug), delivery or hosting machinery (app-delivery-pipeline), or a finished-diff review (code-review)."
---

# Frontend Code

One task: author or conform browser-facing application behavior. The portable
core below owns behavior, trust, capability, failure, and evidence semantics.
Stack syntax and house defaults live in focused profiles and references.

## Interaction contract

**Inputs:** the user-visible behavior; consumer context; selected or available
frontend profile; supported browsers and runtime capabilities; prototype
provenance if any; data/API trust boundaries; accessibility needs; applicable
security and performance risks; and the evidence the change must produce.

**Output:** frontend implementation or implementation guidance plus a declared
profile and an evidence disposition for every applicable gate. Output names
unverified and not-applicable checks explicitly; it never converts an absent
browser, assistive-technology, or deployment capability into a pass.

**Authority:** this skill owns frontend application behavior, component/state/
data boundaries, browser capability handling, application-side security
readiness, browser support, responsive/accessibility behavior, frontend
performance requirements, and frontend evidence obligations. A profile owns
stack-specific tools and defaults; it cannot weaken this core silently.

**Stop or hand off:** backend authorization, validation, cookie issuance, CORS,
or API enforcement routes to `application-code`; new-test strategy and test
authoring route to `testing` with this contract as the domain overlay; an
observed failure routes to `debug`; artifact construction, hosting, deployed
headers, source-map publication, promotion, and rollout route to
`app-delivery-pipeline`; a finished diff routes to `code-review`.

## Portable core

1. **Behavior is observable.** Components render state; errors, loading,
   empty, degraded, denied, and unavailable outcomes are user-visible where
   relevant. Do not hide failure in console output or unresolved promises.
2. **Boundaries point inward.** Surfaces depend on narrow behavior and seam
   interfaces, never concrete clients or vendor SDKs. State is minimal and
   colocated; derived values are computed. Framework-free policy and data
   transformations remain outside the rendering layer.
3. **Choose primitives by semantics.** Use an external-store primitive only
   when the source exposes a stable snapshot and subscription contract. DOM
   events, media lifecycles, and imperative libraries may use owned effect
   subscriptions when setup, teardown, staleness, and concurrency are explicit.
4. **Capabilities are declared, detected, and bounded.** Never infer support
   from framework choice or one browser. A missing or ambiguous browser signal
   produces an honest unavailable or indeterminate state and a usable fallback;
   capability-specific refinements are profile-gated.
5. **Resource ownership is explicit.** Network clients, timers, streams,
   observers, workers, media tracks, and other scarce resources have an owner,
   concurrency policy, cancellation contract, and deterministic cleanup on
   success, failure, replacement, and unmount.
6. **Trust is runtime-specific.** Generated types and contract drift checks reduce authoring drift but do not validate bytes received at runtime. Apply
   runtime validation, compatibility/version negotiation, and safe failure
   according to deployment skew, intermediary, client age, and data risk.
7. **The client is public and least-authority.** No secret enters source,
   build-time client configuration, browser storage, logs, analytics, or a
   shipped bundle. Treat third-party script as application code with the same
   data and authority it can observe.
8. **Accessibility and responsiveness are behavior, not lint.** Declare the
   conformance target and browser/assistive-technology evidence profile;
   preserve semantics, keyboard operation, visible and managed focus, names,
   announcements, alternatives, text resize, reflow, contrast, target access,
   and reduced-motion behavior. Automation alone never proves conformance.
9. **Performance is scenario-bound.** Declare representative user scenarios,
   environment identity, metrics, budgets, repetitions, and failure behavior.
   A synthetic score or bundle size alone is not a universal performance claim.
10. **Evidence is risk-selected.** Deterministic checks, component/contract
    tests, real-browser checks, manual accessibility evidence, security
    negatives, and performance measurements are required only where applicable,
    but every omission is `not_applicable` with rationale or `unverified` and
    escalated. Required evidence may not be silently skipped.

## Profile selection and rebinds

A frontend profile declares framework, language, build tool, styling and
component-system posture, test tools, browser automation, supported browsers,
runtime capabilities, prototype posture, API trust, security obligations,
performance budgets, and exact gates. The machine-readable contract is
`reference/frontend-profile.schema.json`.

- Select `reference/01-haffey-react-vite-profile.md` for the house React,
  TypeScript, Vite, plain-CSS profile.
- A component library is a profile decision evaluated against accessibility,
  browser support, maintenance, bundle, theming, and design-authority cost; it
  is not prohibited by the portable core.
- Tool or framework movement is a profile change when the core behavior and
  evidence contract remain intact. It is a **rebind** when changed capabilities
  require re-deriving core-equivalent rules. A rebind records preserved
  invariants, changed axes, replacement authority, migration, and proof.
- Site and record exceptions use `author-standard`'s ladder. A rebind is not an
  exception.

## Task-shaped references

| Need | Load |
|---|---|
| React/TypeScript/Vite/plain-CSS defaults, component-system decision, dependency and build posture | `reference/01-haffey-react-vite-profile.md` |
| Components, state, subscriptions, resource ownership, prototypes and promotion | `reference/02-components-state-and-prototype-promotion.md` |
| Responsive behavior, browser support, accessibility and manual evidence | `reference/03-responsive-accessibility-and-browser-support.md` |
| Permissions, media, capability states, concurrency and cleanup | `reference/04-media-permissions-and-runtime-capabilities.md` |
| API artifact identity, runtime trust, browser security and cross-skill enforcement | `reference/05-api-data-and-browser-security.md` |
| Performance, routing/forms/i18n/telemetry/offline/SSR/state selection and applicability | `reference/06-production-readiness.md` |
| Frontend test selection and evidence | `reference/testing.md` |

## Evidence and lifecycle

The evidence record conforms to `reference/frontend-evidence.schema.json` and
identifies the candidate, profile, environments, tools, inputs, outcomes,
limitations, and retained artifacts. Manual Safari/VoiceOver evidence is
representative evidence for its named flow and versions, not universal WCAG or
assistive-technology certification.

This skill is used while authoring or conforming behavior. Planned tests remain
owned by `testing`; diagnosis by `debug`; delivery by `app-delivery-pipeline`;
finished-change approval by `code-review`. Missing required evidence stops the
claim and the applicable landing gate; it does not broaden this skill's
authority into those sibling operations.
