# Reference: Frontend Testing

The house testing discipline for frontend code. **Deliberately separable and
self-contained**: this file can be consumed by a quality-role actor without the
authoring sections of `SKILL.md` — the split trigger that would graduate it to
its own home is stated in SKILL.md § Where to look.

## Framework stance

**vitest + Testing Library + jsdom**, with `user-event` for interaction. The
governing principle is Testing Library's own maxim: *the more your tests
resemble the way your software is used, the more confidence they can give
you.* Its operational consequence is a house rule:

- **Query by role and accessible name, never by test-id or DOM structure**
  where a role query is expressible. This makes every component test an
  accessibility pressure test for free — a component a test can't find by
  role is a component a screen reader can't find either.
- **Test behavior through the DOM, not implementation details.** Component
  internals — state shape, hook call order, private functions — are not
  assertion targets; refactors that preserve behavior must not break tests.
- **Snapshots are used sparingly and never as the primary assertion.** A
  failing snapshot that gets reflexively regenerated is a test that specifies
  nothing.

## Test kinds, mapped to the layering

| Layer | Kind | Instrument |
|---|---|---|
| `lib/` and framework-free logic | Unit tests | plain vitest — cheapest, test-first |
| Hooks with real behavior | Hook tests | `renderHook`, behavior-asserted |
| Engine/surface behavior | Component tests | Testing Library render + `user-event` through the DOM |
| Seams (API client ↔ backend contract) | Contract tests | request/response shapes asserted against the generated spec types |
| Mocks | Conformance by construction | mocks implement the seam interface; the type system holds them to it |

**E2e is not governed here.** No house convention exists for browser-automation
testing; one is adopted when a real need arrives.

## The TDD split (mechanism vs. experience)

The service-side gates-vs-judgments split has a frontend twin, and the axis is
stated here so every assignment site can cite it:

- **Mechanism code** — `lib/`, seams and clients, state logic, non-trivial
  hooks — is specifiable up front and is **test-first**, with the full
  meaningful-red discipline: the failing test runs and fails on a real
  behavioral assertion before the implementation lands; a syntax or import
  error is not a meaningful red.
- **Experience code** — surfaces, visual behavior, motion — is specified
  **test-at-hardening** per the experience-first path: the prototype discovers
  the behavior; hardening writes it down as tests while re-authoring each
  piece. Test-at-hardening is the frontend analogue of test-first.

Bug fixes need a reproducing test that fails before the fix lands, on either
side of the axis.

## Coverage (the derived form)

Coverage is measured and gated **per layer, not globally** — global line
coverage over JSX-heavy presentation measures render execution, not behavior
specification, and is a gamed number by construction.

- **Mechanism layers** (`lib/`, `hooks/`, seams/clients, engine logic) carry
  an **enforced floor: 90% line coverage** — the house default constant
  applied to the derived form; declared as a default, and **override is a site
  exception** with its rationale.
- **Surfaces** are exercised through component tests with coverage **measured
  and reported but ungated initially**. Whether surfaces earn their own gate,
  and at what number, is not yet ruled.

**The tautological-assertion exclusion, and its bound.** Code that can only be
asserted tautologically is excluded from the mechanism floor. A test asserting
that an audio graph was wired the way the wiring code wires it fails when the
code changes, not when the behavior is wrong — it specifies nothing, and paying
mock ceremony for it buys a coverage number rather than a specification.

**The test: would the assertion fail when the behavior is wrong, or only when
the code changes?**

**Streaming-session state is not excluded.** Connection state, permission state,
transcript accumulation, level derivation and teardown ordering are all
observable and specifiable, and they stay under the gate.

The exclusion is claimed at the site — the omit entry carries its reason where it
omits — and **the gate reports the excluded line count alongside the floor.** An
exclusion that grows silently turns a 90% floor over the remainder into a number
that means nothing.

**Anti-gaming rules:**

- The omit list holds only what the exclusion above covers, plus infrastructure
  with no behavior to specify; no module with assertable behavior escapes
  measurement.
- **Directory placement is not a dodge.** Moving mechanism logic into a
  surface file to escape the gated layers is the named cheat; the layering
  rules in SKILL.md make it a violation independently of coverage.
- Coverage is confirmed at the gate quartet (type-check, lint, tests,
  coverage), honestly — a threshold met by **undeclared** omission is not met.

## Test hygiene

- **AAA structure** (Arrange-Act-Assert), module comment block on every test
  file, and naming that reads as a specification — `describe` blocks keyed to
  the unit under test, test descriptions stating scenario and expectation
  (`renders the empty state when items are absent`), the house
  unit/scenario/expected naming discipline in the frontend idiom.
- **Test isolation:** no test depends on state left by another; jsdom
  environment per file, fresh render per test, timers and mocks restored.
- **Async is awaited, not raced:** use Testing Library's `findBy*` /
  `waitFor` over arbitrary sleeps; a flaky test is a defect, not weather.
- **The seam is the mock boundary.** Component and surface tests mock at the
  seam interface (the same place production swaps implementations), never
  deep inside a client. Mock-at-the-seam preserves the contract the seam
  enforces — the frontend twin of "in-memory adapter over mocked port."
