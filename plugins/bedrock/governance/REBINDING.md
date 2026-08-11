# Worked rebind specimen: React/Vite profile to Vue/Vite

This specimen demonstrates the rebind output contract; it does not add Vue as a
verified Bedrock profile.

## Preserved invariants

- browser behavior remains owned by `frontend-code`;
- accessibility, runtime trust-boundary validation, secure browser/session
  handling, observable capability states, test evidence, and application versus
  infrastructure/delivery ownership remain unchanged;
- prototype safety and evidence-based promotion remain required.

## Changed axes and assumptions

The component and state runtime changes from React to Vue 3. Vite, TypeScript,
plain CSS, the browser support target, and application-delivery seam remain.
React hook and external-store primitives no longer apply; Vue composition and
reactivity semantics require new lifecycle evidence.

## Replacement authority and responsibility

Vue's versioned official documentation replaces React-specific authority for
components, effects, subscriptions, state, and lifecycle. Bedrock's portable
frontend contract remains authoritative for accessibility, security, evidence,
browser behavior, ownership, and handoffs. The consumer owns selection and
pinning of the Vue toolchain until a verified profile is adopted.

## Migration and compatibility

Existing React consumers do not change. This is a new consumer-local profile,
not an in-place package migration. Explicit invocation remains
`frontend-code`. The consumer records Vue, Vite, TypeScript, browser, test, and
lint identities and proves build, hydration if used, accessibility, runtime
validation, and delivery compatibility before adoption.

## Exceptions, degradation, and refusal

React-only examples are non-applicable rather than translated mechanically.
When a portable invariant cannot be expressed or proved on Vue, the profile
remains unverified and the affected production claim stops. Lack of a component
library is not an accessibility or interaction-semantics waiver.

## Proving evidence

A representative consumer must pass typecheck, lint, unit/component tests,
production build, performance budget, Chromium/Firefox/WebKit behavior,
automated accessibility, manual keyboard/screen-reader evidence, runtime API
boundary failures, and the static/application-delivery seam. Success is every
applicable gate green with no blocking review finding; unavailable manual or
browser evidence yields an explicitly unverified profile rather than adoption.

This complete six-part output is what distinguishes a rebind from selecting an
already-declared configuration within an existing profile.
