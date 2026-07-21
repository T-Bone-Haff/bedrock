---
name: frontend-code
description: House engineering standard for authoring frontend code on the house web stack — React components and hooks, TypeScript strictness, Vite toolchain, plain-CSS styling on design tokens, the experience-first prototype→harden path, the OpenAPI typed-contract seam to the Python backend, frontend testing with vitest and Testing Library, accessibility to WCAG 2.2 AA, client-side security, and npm dependency discipline. Use whenever writing, structuring, scaffolding, or conforming frontend code: building a component, surface, or hook, hardening a prototype into governed code, wiring the API client or generating types from the backend contract, testing a component, setting up a frontend repo, adding routing or config or token-based styling, or checking whether frontend code follows the conventions. Assumes TypeScript + React + Vite + plain CSS on design tokens + vitest/Testing Library, deliberately without a component library; a materially different choice on any axis is a rebind, not a line-edit — version movement within an axis is a currency concern, never a rebind. Design-token values live in each repo's design authority — this skill points at them, never restates them. Reviewing a finished frontend diff is the code-review skill, whose conformance checklist carries the Frontend code section; the backend side of the contract seam is the application-code skill; the build/deploy pipeline belongs to the forthcoming app-delivery-pipeline skill.
---

# Frontend Code

The engineering conventions for authoring frontend code — from a hook to a full
surface. This SKILL.md carries the invariants and the authoring disciplines;
`reference/testing.md` carries the testing discipline as a deliberately
separable unit.

## Binding (read once)

These conventions are written against a specific stack, declared on **axes,
not point versions**: **TypeScript · React · Vite · plain CSS with design
tokens as the single styling source · vitest + Testing Library — and
deliberately no component library.** They are portable across projects on that
binding. A materially different choice on any axis — another framework, a
CSS framework or component library, a different test framework — is a
**rebind**: re-derive the equivalent conventions, don't line-edit these.

**Version movement within an axis is not a rebind — it is a currency
concern.** The frontend ecosystem versions faster than any stack the house has
bound; pinning point versions into the binding would fossilize the standard
against whichever consumer lags. Maintenance of version currency is a separate,
ongoing concern from conformance to these conventions.

*Currency note (dated 2026-07-21, verify at adoption):* authored against
React 19.2 public guidance, TypeScript ~5.8 documentation, typescript-eslint
v8.x shared configs, and current Vite documentation (v8, Rolldown-bundled,
Node 20.19+ baseline). The first proving consumer runs React 18 / Vite 6 —
inside the binding; its version lag is a maintenance item, not a conformance
finding.

**No component library is a position, not an accident.** The house ships a
bespoke design system: design tokens are the single visual source of truth, and
components are authored against them directly. A component library imports a
second design authority and a standing fight between its opinions and the
tokens. Adopting one is a rebind-grade departure and takes a decision record.

## Scope of evidence (read honestly)

This skill is **forward-authored from established public authority** — the
Rules of React, TypeScript and typescript-eslint strict guidance, Testing
Library's guiding principles, WCAG 2.2, OWASP client-side guidance — not
distilled from any build. Its proving base is **n=1**: one real frontend
consumer, with the first governed build serving as the cascade. Sections with
no live instance yet say so where they stand — the typed-contract seam has no
live backend behind it, and the credential-handling rules predate any real
auth surface. Expect the proving cascade to teach this skill things no
authority document could; that is the proving step working. The second
frontend build is the second proving pass and is what begins retiring the n=1
caveat.

**Evidence notes are not a compliance dial.** Every convention in this skill
binds at full force from its landing, thin evidence base and all. The notes
above and the per-section evidence lines are addressed to the skill's authors
and its proving passes — they mark where the *standard* expects to learn,
never where a *consumer* may loosen. The only sanctioned exit from any
convention here is the misfit rule: a stated exception with its reason, at the
site, every time. "It wasn't proven yet" is not an exception; it is not
addressed to you.

## The experience-first path

The house builds front-ends **experience-first**: prototype the experience
fast, then harden into conformant code. This path is the paved road, and the
conventions are shaped to serve it — a standard that treats the working style
as an exception invites silent non-conformance; this one names the free zone
so the fence around it is real.

1. **Gates bind at the governed-repo boundary, not at the keyboard.**
   Conformance applies to code entering a governed repo's source tree.
   Prototypes live in *declared prototype space* — design-handoff directories,
   scratch sandboxes, throwaway artifacts — where **no conventions gate at
   all**: hardcode values, skip tests, single-file everything, move at
   experience speed. That license is explicit and sanctioned.
2. **Hardening is re-authoring, not lint-fixing.** A prototype crosses the
   boundary as **design intent, never as code authority**. Production code is
   forward-authored against this skill *from* the prototype-as-spec — not
   produced by cleaning the prototype up until the linter goes quiet. The
   prototype teaches *what the experience is*; the skill governs *how the code
   says it*. Canonizing whatever a fast prototype happened to emit is
   back-distillation at code level.
3. **Design tokens are the thread that makes the handoff cheap.** The one
   discipline prototypes are *encouraged* — not gated — to carry is building
   on the design tokens, because a token-true prototype collapses the
   hardening distance: the experience layer transfers verbatim while the code
   layer re-authors.
4. **Tests arrive at hardening.** The behavior worth keeping is what the
   prototype discovered; hardening specifies it in tests as each piece is
   re-authored. The full split lives in `reference/testing.md`.

The failure modes run both directions and both are named: prototype code
drifting into production un-re-authored (the review checklist catches it), and
conformance machinery leaking into prototype space and killing the speed the
flow exists for.

## The misfit rule

These are strong defaults, not scripture. Where a convention genuinely doesn't
fit the work in front of you, state the exception and why in the code or
commit, then proceed — don't silently violate it, and don't contort the code
to satisfy a rule that doesn't earn its place. A recurring misfit is a signal
the convention should change.

## Always-apply invariants

These hold for every module in governed frontend code:

1. **Function components and hooks only, and the Rules of React hold** —
   components and hooks are pure in render, hooks are called only at the top
   level of React functions. Enforced, not aspired to: `eslint-plugin-react-hooks`
   in the lint config, `StrictMode` on in development.
2. **TypeScript strict, machine-verified.** Code passes `tsc` under the strict
   posture (§ Strictness) and the strict-type-checked lint presets.
3. **Layered, directional imports:** `surfaces → hooks/engine → seams →
   clients`, with `lib/` and shared types at the base. A surface importing a
   concrete client or a vendor SDK is a violation — surfaces depend on seam
   interfaces via providers.
4. **Config from one source, twice.** Every visual value — color, type,
   spacing, motion — comes from the design tokens; nothing visual is
   hardcoded. Runtime config flows through one typed config module; scattered
   `import.meta.env` reads are the frontend's scattered-`os.environ`.
5. **Outbound HTTP flows through the canonical seam client** (§ The
   typed-contract seam) — never scattered per-call fetches.
6. **Errors are rendered states.** Typed error states at the seams, error
   boundaries at the surface layer; no silent swallowing. No stray `console`
   output in production paths — console noise is neither error handling nor
   logging discipline.
7. **Every module carries the comment block; exported API carries TSDoc.**
8. **Untrusted inbound data is validated at the boundary** — per the
   discriminating axis in § The typed-contract seam.
9. **Credentials never touch browser storage, and the bundle is public** —
   § Client security.
10. **The accessibility floor is WCAG 2.2 AA** — § Accessibility. Semantic
    HTML first; everything keyboard-operable.

**What deliberately does not transfer from the service-side house shape:** the
async-first invariant (the browser's execution model makes it meaningless as a
law) and the data-classification tier machinery (server-owned; the client
carries exactly one line of it — no sensitive data into client-side logs or
third-party analytics). Declared misfits, not oversights.

## Components and hooks

- **Components render; hooks hold behavior; lib holds logic.** A component
  with nontrivial non-visual logic is a hook waiting to be extracted; a hook
  with framework-free logic is a `lib/` function waiting to be extracted.
  Extraction order matters because testability follows it (pure functions
  cheapest, hooks next, components last).
- **State is colocated and minimal.** State lives at the lowest component that
  needs it; derived values are computed, never stored in parallel state.
  Reaching for context or a state library is an architecture decision, not a
  reflex — the seam/provider pattern covers cross-cutting dependencies first.
- **Effects synchronize with external systems; they are not a data-flow
  tool.** Per React's own guidance: if it can be computed in render or handled
  in an event handler, it is not an effect.
- **Props are typed interfaces, and seams stay narrow.** A component's props
  are its contract; passing whole objects where two fields suffice couples the
  surface to a shape it doesn't own.

## The typed-contract seam

The boundary between the frontend and the house Python backend is closed by
generated types, not by discipline alone:

1. **The backend's OpenAPI spec is the single source of truth.** The backend's
   Pydantic models already are the contract; the frontend **generates** its
   request/response types from the served spec and never hand-authors a type
   that mirrors a backend model. A hand-written mirror type is the drift
   surface this seam exists to eliminate.
2. **Types-first generation, thin canonical client.** Default tooling: a
   types-only generator (`openapi-typescript` is the named default — verify
   currency at adoption), feeding a thin canonical client wrapper. The rule
   from the service side transfers: outbound HTTP flows through the canonical
   client — which also carries the correlation ID on calls into the house
   backend. Swapping generators is a line-edit; abandoning generation is a
   departure that takes a decision record.
3. **Generated artifacts are committed, regenerated by script, never
   hand-edited.** They live in a named location, and CI carries a **drift
   gate**: regenerate against the current spec and fail on diff.
4. **Contract tests hold both sides of the seam to the same spec.** The
   backend side already carries per-endpoint contract tests; the frontend side
   mirrors them — the client's request construction and response handling
   tested against the spec's shapes. When the spec moves, the seam fails
   loudly on whichever side moved.
5. **Runtime validation follows a discriminating axis, stated at the
   assignment site.** Responses from the own governed backend are
   contract-trusted — the drift gate and contract tests are what make that
   trust sound; blanket runtime re-validation of them is ceremony. Genuinely
   untrusted inbound data — third-party APIs, URL and query params,
   `postMessage` payloads, user-supplied content — gets runtime validation at
   the boundary. Mocks implement the same seam interface and stay conformant
   by construction.

*Scope of evidence:* no live backend serves the spec to a governed frontend
yet; the first real integration is this section's proving surface and may
amend it. **Until it does, the section binds as written** — the mechanisms
are the house contract discipline read from the other side of the wire.

## Strictness

- **tsconfig:** `"strict": true` is the floor, plus `noUnusedLocals`,
  `noUnusedParameters`, `noFallthroughCasesInSwitch`. One deliberate step
  beyond strict: **`noUncheckedIndexedAccess` on by default for new repos** —
  it is not in the strict family, and it is the absent flag that catches real
  bugs: every index and record lookup honestly admits `undefined`. On existing
  codebases, adopt with rationale rather than by default.
  `exactOptionalPropertyTypes` is **considered and not defaulted** (real
  friction with third-party types) — a ruling, not an oversight.
- **Lint:** the typescript-eslint **`strict-type-checked` +
  `stylistic-type-checked`** presets, plus `eslint-plugin-react-hooks` (the
  Rules of React name the plugin as their enforcement mechanism),
  `react-refresh`, and `eslint-plugin-jsx-a11y` (§ Accessibility). The
  upstream guidance reserves strict presets for teams highly proficient in
  TypeScript; on the house's two-surface model that condition is met by
  construction — the author is an agent operating under this skill, where a
  stricter machine-checkable envelope is pure gain.
- **Escape hatches are governed, not banned.** `@ts-expect-error` with a
  description over `@ts-ignore`; `as`-casts and `any`-adjacent constructs are
  justified at the site or they are review findings.
- **The gate quartet:** type-check (`tsc`), lint, tests, and the coverage
  floor (`reference/testing.md`). This skill names what must pass; where the
  pipeline runs is the forthcoming app-delivery-pipeline skill's territory.

## Accessibility

The conformance floor is **WCAG 2.2 AA** (W3C Recommendation; latest revision
2024-12-12) — cited as the authority, not restated. What this skill carries is
the engineering rules that make AA the default outcome:

1. **Semantic HTML first; ARIA only where semantics can't reach.** A `<button>`
   beats `<div role="button">` every time it is expressible.
2. **Everything keyboard-operable, focus always visible, and focus *managed*
   at SPA transitions.** Client-side route changes and dialog open/close move
   focus deliberately and announce — an SPA is precisely where keyboard and
   screen-reader experience silently dies, because nothing reloads.
3. **Accessible names on every interactive element** — enforced by
   construction through role-and-name test queries (`reference/testing.md`).
4. **Contrast is a token-layer property.** Conformance is verified once, at
   the repo's design-token authority, and this skill *points* there — it never
   restates palette values. The token authority carries the named obligation
   to be AA-contrast-verified.
5. **Motion respects `prefers-reduced-motion`** — every animation has a
   reduced path or a stop. Scored, motion-heavy surfaces are exactly where
   this rule earns its place.
6. **Voice is an additional modality, never the only one.** Every
   voice-reachable action stays reachable by keyboard and visible UI.
7. **Check the 2.2-specific AA criteria by name** — target size (minimum),
   focus not obscured, dragging alternatives, accessible authentication,
   consistent help — they are the ones a 2.1-era instinct misses.

Enforcement stack: `eslint-plugin-jsx-a11y` at lint, role-query discipline at
test, the code-review Frontend section at review. Per the experience-first
path, the gate binds at hardening — the re-author is where semantic structure
gets built in rather than retrofitted.

## Client security

External authority: the OWASP XSS and CSP cheat sheets, OWASP browser-storage
guidance, and the OAuth browser-based-apps best-current-practice line — cited,
not mirrored (pinned 2026-07-21, verify currency at adoption).

1. **XSS: trust the framework layer, review the escape hatches.** React's
   automatic escaping is the primary defense, so discipline concentrates where
   it stops: `dangerouslySetInnerHTML` only over sanitized content —
   **DOMPurify is the named default sanitizer**; URL values flowing into
   `href`/`src` are scheme-validated, because React does not defend
   `javascript:` or `data:` URLs; no `eval`, `new Function`, or
   string-argument timers, ever.
2. **CSP: this skill owns the app-side obligations; the header is
   delivery's.** The app is authored strict-CSP-ready — no inline scripts, no
   eval-class constructs, scripts and assets from self — so a strict
   (nonce/hash) policy can be adopted at the hosting layer without app
   changes. The header itself is homed in the forthcoming app-delivery-pipeline
   skill; the seam is declared here the way the service skills declare the
   container-image seam.
3. **Credentials never in `localStorage` or `sessionStorage`.**
   Script-readable storage falls entirely to a single XSS. Preference order:
   httpOnly-cookie sessions (or a backend-for-frontend) first; in-memory-only
   bearer tokens with silent refresh where a cookie architecture is genuinely
   unavailable. *Scope of evidence: no house auth surface exists yet; the
   first real login flow is this rule's proving surface. It binds as written
   from day one — credential handling is exactly where a rule must precede
   its first consumer.*
4. **The bundle is public, by construction.** Every `VITE_`-prefixed variable
   and everything in the client build ships to the browser. No secrets in
   client config, period — the frontend inversion of "secrets from the
   environment" is that *the environment itself ships*. Privileged calls live
   behind the backend seam.

## Dependency discipline

1. **The lockfile is the pin, and it is law.** `package-lock.json` committed
   always; **`npm ci` in CI and any clean build, never `npm install`** — `ci`
   is what makes the lockfile binding. The lockfile's per-package integrity
   hashes are the house hash-pinning analogue. Manifest ranges stay caret;
   upgrades are deliberate acts that move the lockfile in a reviewed commit.
2. **Audit posture, noise handled honestly.** `npm audit` runs in CI;
   high/critical advisories in production dependencies block; dev-dependency
   advisories are triaged, not auto-blocking — a gate that cries wolf trains
   people to ignore it. Default posture; override with rationale.
3. **Minimal-dependency posture.** Prefer the platform — the web's own APIs
   are the stdlib. Every new runtime dependency is a justified act; anything
   that shapes architecture (a state-management library, a UI framework) is
   **decision-record grade**, not an `npm install`.
4. **The cost gate.** A dependency introducing a recurring cost or a
   proprietary license is never routine — decision-record grade, always. The
   default stack is free by construction, not by luck.
5. **Node baseline declared in `engines`** — the toolchain floor is explicit,
   not ambient.

Deliberately not carried (under-govern until it hurts): provenance-attestation
requirements, install-script lockdown regimes, exact-version manifests.
Supply-chain posture beyond the lockfile-and-audit floor is a watch surface,
promoted when it hurts.

## Where to look

- `reference/testing.md` — the frontend testing discipline: framework stance,
  test kinds, the mechanism-vs-experience TDD split, and the per-layer
  coverage form. **Deliberately separable**: it is self-contained so a
  quality-role consumer can load it without the authoring sections. Split
  trigger, stated: if the testing content grows to answer its own task-shaped
  prompt, or a distinct quality-role agent becomes a real consumer of the
  testing discipline independently of the authoring discipline, it graduates
  to its own home.
- **Design-token authority** — per repo, named in the repo's own orientation
  (its CLAUDE.md or design-handoff directory). This skill points; the repo's
  token source is the single authority for every visual value. For
  brand-level prototyping assets, the `haffey-design` skill (Cowork-side) is
  the adjacent authority — same pointer rule.
- **Public authority, pinned at authoring (2026-07-21), verify currency at
  adoption:** the Rules of React (react.dev); the TypeScript TSConfig
  reference; typescript-eslint shared-config guidance; Testing Library's
  guiding principles; WCAG 2.2 (W3C Recommendation, rev. 2024-12-12); the
  OWASP XSS/CSP cheat sheets and browser-storage guidance; the OAuth
  browser-based-apps BCP; Vite documentation.

## Boundaries with sibling skills

- **Reviewing a finished frontend diff** → `code-review`, whose conformance
  checklist carries the Frontend code section.
- **The backend side of the contract seam** → `application-code`; its Pydantic
  models are the contract this skill's generated types consume.
- **The build/test/deploy pipeline, hosting, and the CSP header** → the
  forthcoming app-delivery-pipeline skill. This skill names what must pass and
  what the app must be ready for; delivery owns where it runs.
- **Code whose central act is an LLM call** — including a real orchestrator
  client behind a frontend seam — → `agent-code` for the call discipline; this
  skill governs the seam interface and the surface that consumes it.
- **Brand and design-token content for prototyping** → the `haffey-design`
  skill; production token values live in each repo's design authority.
  Pointer-not-mirror, both directions.
- **Structured debugging** → `debug`; **authoring a reusable standard** →
  `author-standard`; **decision records** → `author-decision-record`.
