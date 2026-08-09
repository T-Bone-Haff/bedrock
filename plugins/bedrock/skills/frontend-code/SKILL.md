---
name: frontend-code
description: "Author or conform frontend code on the house TypeScript, React, Vite, and plain-CSS stack, including components, hooks, responsive layout, design-token use, API clients, browser permissions and media, accessibility, security, testing, and prototype hardening. Use when implementing or structuring browser-facing application behavior. Do not use for backend services (application-code), build/deploy workflows (app-delivery-pipeline), or reviewing a finished diff (code-review). A materially different framework or styling architecture is a rebind."
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
concern.** Maintenance of version currency is a separate,
ongoing concern from conformance to these conventions.

*Currency note (dated 2026-07-21, verify at adoption):* authored against
React 19.2 public guidance, TypeScript ~5.8 documentation, typescript-eslint
v8.x shared configs, and current Vite documentation (v8, Rolldown-bundled,
Node 20.19+ baseline).

**No component library.** The house ships a
bespoke design system: design tokens are the single visual source of truth, and
components are authored against them directly. A component library imports a
second design authority and a standing fight between its opinions and the
tokens. Adopting one is a **rebind** — re-derive the equivalent conventions
rather than line-edit these — and the rebind is recorded.

## The experience-first path

The house builds front-ends **experience-first**: prototype the experience
fast, then harden into conformant code. This path is the paved road.

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

The failure modes run both directions: prototype code
drifting into production un-re-authored (the review checklist catches it), and
conformance machinery leaking into prototype space and killing the speed the
flow exists for.

## The misfit rule

These are strong defaults, not scripture. Where a convention genuinely doesn't
fit the work in front of you, state the exception and why in the code or
commit, then proceed — don't silently violate it, and don't contort the work
to satisfy a rule that doesn't earn its place here. A recurring misfit is a
signal the convention should change, not a thing to keep working around.

Thin evidence is not exception grounds. Every convention here binds at full
force from its landing; "it wasn't proven yet" is neither a site nor a record
exception.

**Exception tiers are `author-standard`'s ladder** — *site exception* (this
rule's own form, plus override-with-rationale) and *record exception*. This
skill binds to those names and defines none of its own.

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
4. **Config from one source, thrice.** Every visual value — color, type,
   spacing, motion — comes from the design tokens; nothing visual is
   hardcoded. Runtime config flows through one typed config module; scattered
   `import.meta.env` reads are the frontend's scattered-`os.environ`. Every
   shipped media asset — audio, video, imagery, fonts — is reached through one
   typed manifest, never by string literal at the point of use (§ Media assets).
5. **A resource that must be singular flows through one owner.** Outbound HTTP
   goes through the canonical seam client (§ The typed-contract seam) — never
   scattered per-call fetches. Browser media singletons — `AudioContext`,
   `MediaStream`, `SpeechRecognition` and their kin — go through one provider or
   module singleton reached through a seam, never constructed at point of use
   (§ Browser media). The reasons differ — uniformity for the client,
   browser-imposed scarcity for the media singletons — and the rule does not.
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
11. **Responsive by default.** Every surface adapts to its environment. A
    fixed-frame or fixed-aspect surface is a **record exception** that names
    which part of it claims WCAG 1.4.10's two-dimensional-layout exception, and
    why (§ Responsive layout).
12. **Permission-gated device access is requested on an explicit user gesture,
    and its outcome is state.** Microphone, camera, geolocation, clipboard —
    never requested at mount, and the outcome is modeled as first-class
    rendered state, never swallowed (§ Browser media).

**What deliberately does not transfer from the service-side house shape:** the
async-first invariant (the browser's execution model makes it meaningless as a
law) and the data-classification tier machinery (server-owned; the client
carries exactly one line of it — no sensitive data into client-side logs or
third-party analytics).

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
  in an event handler, it is not an effect. **Components subscribe to external
  event sources through `useSyncExternalStore`**, not `useEffect` + `setState` —
  the latter is this same violation in its most common disguise.
- **Props are typed interfaces, and seams stay narrow.** A component's props
  are its contract; passing whole objects where two fields suffice couples the
  surface to a shape it doesn't own.

**Time-sequenced work has one owner and one cancellation contract.**
Choreography — scheduled sequences, staged animation, timed media — lives in a
hook or `lib/` module, never inline in a surface, and exposes start and cancel.
Internals are free; **the seam is uniform.** `AbortSignal` is the house currency
for that seam — hand-rolled cancellation tokens (monotonic sequence counters,
timer-handle arrays exposed as the public contract) are the named anti-pattern.
`AbortSignal.timeout()` and `AbortSignal.any()` are convenient where available;
both reached baseline only in 2024, so neither is required.

A cancelled sequence must **settle** every promise it created: a pending timer
resolving a promise is cancelled by resolving or rejecting it, never by dropping
the timer, or the awaiting frame is retained forever with its whole closure.
Timer registries release fired entries.

A timeline is **mechanism code** — fake-timer testable, under the coverage gate.
It does not qualify for the tautological-assertion exclusion
(`reference/testing.md`).

## Responsive layout

**Responsive is the default (invariant #11).** This section is how that gets
built; the accessibility criteria it serves are §Accessibility's floor, cited
rather than restated.

**The two query kinds answer different questions.** Media queries answer *what is
the environment?* — viewport, orientation, media type, and user preferences
including `prefers-reduced-motion` and `prefers-color-scheme`. Container queries
answer *how much room does this component have?* Page shell and environment
response are media-queried; component-level adaptation is container-queried.
**Neither is a fallback for the other.**

**Container-query friction, named so it isn't discovered the hard way:** a
container cannot query itself — measure an ancestor, and expect a wrapper
element; flex items need explicit sizing or the container collapses; custom
properties do not resolve inside container queries. **Size queries are baseline;
style queries and scroll-state queries are not** — style queries lack Firefox,
scroll-state is Chromium-only. Building on a non-baseline query is a site
exception with the support gap stated.

**Fluid type and space express on the design tokens.** Fluid steps use `clamp()`
with a `rem` component in the middle value — pure `vw` does not scale under
browser zoom and fails SC 1.4.4. **Every fluid step satisfies `max ≤ 2.5 × min`**,
which is what keeps 200% reachable at every viewport width. As with contrast, the
values live in the repo's design-token authority and this skill points at them:
**the token authority carries the named obligation that every fluid step is
rem-anchored and inside the 2.5× ratio.**

**Fixed-frame surfaces.** A surface authored to one viewport and scaled to fit is
a **record exception** (#11). Two criteria pull apart, and the record must treat
them differently:

- **SC 1.4.10 Reflow is arguable.** Its exception covers content requiring
  two-dimensional layout for usage or meaning — maps and diagrams, data tables,
  games, presentations, persistent toolbars, and layouts where consistent
  orientation to related sections is important for understandability or
  functionality. Instrument panels and HUDs live here. The record **names which
  part of the surface claims the exception and why**; the exception does not
  extend to surrounding chrome, which reflows on its own.
- **SC 1.4.4 Resize Text is not.** It carries no such exception. A frame scaled
  by a factor computed from viewport size cancels browser zoom exactly — halve
  the viewport, halve the scale, rendered size unchanged — so zoom becomes a
  mathematical no-op and no scaling mechanism remains. **`transform: scale()`
  fitted to the viewport is a named anti-pattern**, not a layout technique.

Where the record is granted, the obligations are: a **declared supported viewport
range**; AA met **within** that range, not merely at the design size; a genuine
text-resize path; and interactive target sizes evaluated **at the minimum
supported scale rather than at scale 1**, against §Accessibility's target-size
floor and its exceptions.

## Browser media

Invariant #5 says who owns a media singleton. This section says what its life
looks like, and what happens when the user says no.

**Static playback and streaming sessions are different lifecycles, and both are
named.**

*Static* — pre-rendered clips, synthesized one-shot cues — is bounded and
fire-and-forget. The context may be long-lived; caches are keyed and bounded;
teardown rides app teardown.

*Streaming* — live capture, live synthesis, a duplex transport — is a
**session**. Exactly one live session at a time. Teardown is deterministic and
ordered, on stop and on unmount: release `MediaStream` tracks, disconnect nodes,
release the context. Cancellation is explicit, never implied by garbage
collection — the cancellation contract in §Components and hooks applies. Where a
network transport is involved, reconnect posture is stated.

**Device permission.** Invariant #12 requires the request on a user gesture and
the outcome as state. The outcomes to model are at least: **unavailable** (no
device, insecure context — `navigator.mediaDevices` is undefined on an insecure
origin and property access throws — or unsupported browser), **dismissed**,
**denied**, **granted**. Each is a rendered state; none is swallowed.

When a permission-gated modality is unavailable, fall back to **the alternate
modality §Accessibility item 6 already requires** — not to a simulation of the
unavailable one. Simulating an input the user does not have manufactures a
success signal: the UI reports success while the feature is dead.

**Scope the catch to the permission call alone.** A single `try` spanning both
the request and the setup that follows it reports your own bugs as the user's
missing hardware — a defect in analyser wiring or an animation frame presents,
permanently and silently, as "you have no microphone."

**Not authored here: how streamed events reach React state.** Subscription
lifecycle, backpressure and reconnect conventions for a live event source are
un-governed. Components subscribe to external event sources through
`useSyncExternalStore` (§ Components and hooks); beyond that line, there is no
house convention to conform to yet.

## Media assets

Invariant #4 says media assets come from one manifest. The rest follows from how
bundlers work.

**The manifest is a typed module** carrying id, path, provenance, and whatever
per-asset metadata the runtime needs — per-clip loudness trims, durations,
captions. A string concatenated at a call site is not a reference; it is a lookup
that fails silently when it misses.

**Assets are reached through the manifest by import**, so the bundler
fingerprints them. Content-hashed filenames are the consequence, not a separate
act. `public/` (or its equivalent) is for assets that must keep a stable URL —
referenced from outside the build, `robots.txt`-class — and using it is a **site
exception** with its reason stated. **Hand-versioned filenames are the symptom of
an asset that skipped the bundler**, and they interact badly with immutable cache
headers.

**License is dependency discipline's** (§ Dependency discipline, item 4): a
proprietary-licensed or recurring-cost asset is a record exception, exactly as a
dependency would be. **Cache posture is delivery's** — the manifest is what makes
assets addressable to it.

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
   **record exception**.
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

6. **Vendor-surface declarations are not domain types, and item 1's ban does
   not reach them.** Where the TS DOM lib doesn't carry a browser surface — Web
   Speech, vendor-prefixed constructors, experimental APIs — prefer a maintained
   types-only package; where none exists, hand-declare the minimal structural
   shape **once**, in a single types module, never per consumer. Vendor-prefixed
   fallbacks resolve in one place. Item 1's ban on hand-written mirrors targets
   your own backend's models; a `SpeechRecognition` interface the platform never
   shipped types for is not a mirror of anything you own.

## Strictness

- **tsconfig:** `"strict": true` is the floor, plus `noUnusedLocals`,
  `noUnusedParameters`, `noFallthroughCasesInSwitch`. One deliberate step
  beyond strict: **`noUncheckedIndexedAccess` on by default for new repos** —
  it is not in the strict family, and it is the absent flag that catches real
  bugs: every index and record lookup honestly admits `undefined`. On existing
  codebases, adopt with rationale rather than by default.
  `exactOptionalPropertyTypes` is **considered and not defaulted** (real
  friction with third-party types).
- **Lint:** the typescript-eslint **`strict-type-checked` +
  `stylistic-type-checked`** presets, plus `eslint-plugin-react-hooks` (the
  Rules of React name the plugin as their enforcement mechanism),
  `react-refresh`, and `eslint-plugin-jsx-a11y` (§ Accessibility).
- **Escape hatches are governed, not banned.** `@ts-expect-error` with a
  description over `@ts-ignore`; `as`-casts and `any`-adjacent constructs are
  justified at the site or they are review findings.
- **The gate quartet:** type-check (`tsc`), lint, tests, and the coverage
  floor (`reference/testing.md`). This skill names what must pass; where the
  pipeline runs is the app-delivery-pipeline skill's territory.

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
   reduced path or a stop.
6. **Voice is an additional modality, never the only one.** Every
   voice-reachable action stays reachable by keyboard and visible UI.
7. **Check the 2.2-specific AA criteria by name** — target size (minimum),
   focus not obscured, dragging alternatives, accessible authentication,
   consistent help — they are the ones a 2.1-era instinct misses. **Target size
   is 24×24 CSS pixels with five exceptions** — spacing (undersized targets
   whose 24px-diameter circles do not intersect), equivalent (the same function
   reachable from a conforming control on the page), inline (constrained by
   surrounding line-height), user-agent-controlled, and essential. Read the
   exceptions before rebuilding a control: a dense cluster with adequate spacing
   already conforms.

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
   changes. The header itself is homed in the app-delivery-pipeline
   skill.
3. **Credentials never in `localStorage` or `sessionStorage`.**
   Script-readable storage falls entirely to a single XSS. Preference order:
   httpOnly-cookie sessions (or a backend-for-frontend) first; in-memory-only
   bearer tokens with silent refresh where a cookie architecture is genuinely
   unavailable.
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
   people to ignore it. Default posture; override is a site exception with its
   rationale.
3. **Minimal-dependency posture.** Prefer the platform — the web's own APIs
   are the stdlib. Every new runtime dependency is a justified act; anything
   that shapes architecture (a state-management library, a UI framework) is
   a **record exception**, not an `npm install`.
4. **The cost gate.** A dependency or shipped media asset introducing a
   recurring cost or a proprietary license is never routine — a **record
   exception**, always.
5. **Node baseline declared in `engines`** — the toolchain floor is explicit.

Not carried: provenance-attestation requirements, install-script lockdown
regimes, exact-version manifests. Supply-chain posture beyond the
lockfile-and-audit floor is un-governed.

## Where to look

- `reference/testing.md` — the frontend testing discipline: framework stance,
  test kinds, the mechanism-vs-experience TDD split, and the per-layer
  coverage form. **Deliberately separable**: it is self-contained so a
  quality-role consumer can load it without the authoring sections. Split
  trigger, stated: content graduates to its own home when **a distinct role
  becomes a real consumer of it independently of the authoring discipline** —
  and that is the load-bearing half. Answering its own task-shaped prompt is not
  sufficient on its own: most sections here do that, and splitting on it would
  leave this skill a stub surrounded by references.
- **Design-token authority** — per repo, named in the repo's own orientation
  (its CLAUDE.md or design-handoff directory). This skill points; the repo's
  token source is the single authority for every visual value. For
  brand-level prototyping assets, the `haffey-design` skill (Cowork-side) is
  the adjacent authority — same pointer rule.
- **Public authority, pinned at authoring, verify currency at adoption.**
  *Pinned 2026-07-21:* the Rules of React (react.dev); the TypeScript TSConfig
  reference; typescript-eslint shared-config guidance; Testing Library's
  guiding principles; WCAG 2.2 (W3C Recommendation, rev. 2024-12-12); the
  OWASP XSS/CSP cheat sheets and browser-storage guidance; the OAuth
  browser-based-apps BCP; Vite documentation. *Pinned 2026-08-03:* the CSS
  containment and container-query specifications; WCAG 2.2 Understanding
  documents for SC 1.4.4, 1.4.10 and 2.5.8; the Web Audio, MediaStream and
  Permissions specifications; the DOM standard's `AbortController`/`AbortSignal`;
  Vite's static-asset handling guide.

## Boundaries with sibling skills

- **Reviewing a finished frontend diff** → `code-review`, whose conformance
  checklist carries the Frontend code section.
- **The backend side of the contract seam** → `application-code`; its Pydantic
  models are the contract this skill's generated types consume.
- **The build/test/deploy pipeline, hosting, and the CSP header** → the
  app-delivery-pipeline skill. This skill names what must pass and
  what the app must be ready for; delivery owns where it runs.
- **Code whose central act is an LLM call** — including a real orchestrator
  client behind a frontend seam — → `agent-code` for the call discipline; this
  skill governs the seam interface and the surface that consumes it.
- **Brand and design-token content for prototyping** → the `haffey-design`
  skill; production token values live in each repo's design authority.
  Pointer-not-mirror, both directions.
- **Structured debugging** → `debug`; **authoring a reusable standard** →
  `author-standard`; **decision records** → `author-decision-record`.
