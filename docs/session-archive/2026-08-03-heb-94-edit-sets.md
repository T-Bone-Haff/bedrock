# Ratified edit sets — bedrock 2.2.0

Companion to `2026-08-03-heb-94-decision-log.md`. The log carries **why**; this file
carries **what lands**. Ratified text below is the pinnable payload for the
execution relay — bytes here are the bytes that land.

Base: `~/Documents/GitHub/bedrock` @ `main` `f7ed7f5`.

---

## Edit set 1 — `author-standard` + `app-delivery-pipeline` — RATIFIED 2026-08-03

### 1a. `plugins/bedrock/skills/author-standard/SKILL.md`

**Placement:** §Harden it, as a subsection immediately after the four bullets.
The bullets are *rules*; this is a *vocabulary*, and the first bullet ("One house
vocabulary") is what says ladders are defined once, here.

**Drafting note:** the house **misfit rule** already exists, carried verbatim
across skills, and it *is* the site tier. The ladder does not replace it — it
classifies it. Same for override-with-rationale. These are two idioms at one
tier: *"this rule doesn't apply here"* vs. *"this rule applies and this instance
takes a different value."* D9 ratified the tiers by cost and audience, not by
kind. No existing text is deprecated.

> ### The exception ladder
>
> A standard needs sanctioned ways not to apply, or it gets violated silently.
> Two tiers, defined once here and cited by name:
>
> - **Site exception** — the reason is stated at the site (in the code, the
>   commit, or the artifact) and work proceeds. No external artifact, no second
>   reader. The house misfit rule is this tier's form for *"the convention
>   doesn't fit here"*; override-with-rationale is its form for *"the convention
>   fits and this instance takes a different value."*
> - **Record exception** — the departure is argued in a decision record before it
>   lands. Reserved for departures that change what downstream work may assume:
>   an architecture-shaping dependency, abandoning a generated contract, a
>   whole-project posture.
>
> **Site is the default; escalating to record needs its own reason.** Naming a
> heavier rung invites reaching for it, and a record is paid for by every future
> reader.
>
> **A rebind is not an exception.** It declares that the standard's binding does
> not hold and the equivalent conventions must be re-derived. Filing a rebind as
> an exception is how a standard ends up claiming authority over work it never
> bound.
>
> Carrier artifacts declare their binding to this ladder and use its names; they
> do not define their own tiers.

**Also:** YAML `description` capability list gains "the exception ladder" (D7.b).

### 1b. `plugins/bedrock/skills/app-delivery-pipeline/reference/03-static-frontend-leg.md`

**Placement:** §5 Cache headers, replacing the first bullet.

**Rejected alternative:** tightening the glob to match a hash pattern. Firebase
glob syntax cannot express "filename contains a content hash" without something
fragile; a layout constraint is checkable by eye where a clever glob is not.

> - **Hashed assets** (`/assets/**` — Vite's fingerprinted build output):
>   `Cache-Control: public, max-age=31536000, immutable`. The hash in the
>   filename is the cache key; the header makes the CDN and browser honor it.
>   **The header trusts the path, so the path must hold only fingerprinted
>   output** — anything copied verbatim from `publicDir` ships outside
>   `/assets/`, because an un-hashed file under this header is cached for a year
>   with no way to invalidate it. (`frontend-code` owns the authoring side:
>   assets reach the bundler through the manifest.)

---

## Edit set 2 — `author-execution-relay/SKILL.md` — RATIFIED 2026-08-03

Five edits. Description unchanged (D7.c).

### 2a. §Premise discipline — the parent

**Placement:** new bullet after *"Fresh-read the tool the relay describes"*,
before *"Drafting inherits verify-first"*.

**Drafting note:** D5's ratified parent said *"verify the artifact the tool
stored, not the input you handed it"* — a one-sentence mirror of the §Pin
discipline clause landing below. Changed to **point** instead. The batch adds a
pointer-not-mirror rule; it does not ship a mirror.

> - **A tool operation does more than it says.** Every command a relay's author
>   or executor issues runs through a toolchain with its own mutation paths —
>   hooks, templates, filters, locks, caches, format-on-save. The relay never
>   assumes the operation was only what it named. On the **write** path, verify
>   the artifact the tool stored rather than the input you handed it (§ Pin
>   discipline). On the **read** path, use the form that observes without
>   mutating (below).

### 2b. §Premise discipline — the read-only clause

**Placement:** new bullet immediately after *"Drafting inherits verify-first"*.

> - **Drafting-time inspection is read-only or it is a mutation.** The
>   verification a relay's author performs against the target is itself a touch.
>   Use the read-only form of every inspection command
>   (`git --no-optional-locks status`, `git log`, `git show`, `git cat-file`) and
>   never a form that takes a lock, refreshes an index, or writes a cache. A
>   drafting surface that cannot release what it acquires leaves the executor a
>   failure the relay never mentions — and the author is the one party guaranteed
>   not to see it.

### 2c. §Pin discipline — the third drift class

**Placement:** new bullet immediately after *"A replacement handoff pins both
ends"* — the bullet naming the two classes this extends.

> - **A third drift class: the tool interposes.** Base drift and executor drift
>   both assume the only mutation paths are the world's and the executor's.
>   Toolchains carry their own. Where a relay pins a payload a toolchain could
>   rewrite, the guard checks that the tool's mutation surfaces are inert before
>   the operation — in git, hooks, a configured `commit.template`, line-ending
>   and filter config; in another toolchain, its equivalents. The check is cheap
>   and fails early. **It is not what makes the pin sound** — verification after
>   the operation does not depend on having enumerated them correctly.

### 2d. §Pin discipline — verify the durable form

**Placement:** new bullet immediately **before** *"A hash proves fidelity, not
sanity"*. The two pair: what your hash covers, then what it proves.

> - **Verify the durable form, not the input to the tool.** A pin over a payload
>   handed to a tool is discharged against the artifact the tool stored, read in
>   its rawest available form — the commit object, not `git log --format=%B`; the
>   file on disk, not the string the executor believed it wrote. Convenience
>   readers interpose their own formatting: trailing newlines, wrapping, escape
>   handling. **A hash over a convenience read is a hash over the reader.**

### 2e. §Output discipline — the de-drift pointer

**Placement:** in-place amendment to the *"Verbatim payloads are wrap-safe"*
bullet. The sentence HEB-98 names incomplete.

> ...and where the bytes matter enough to pin, validate with a hash or
> token-integrity check **over the durable artifact (§ Pin discipline), never
> over the payload as handed in** — the executor catching a wrapped token at the
> gate is the *last* line of defense, not the discipline.

### 2f. §The four-block spine — the stale-lock gate

**Placement:** appended to block 1 (Fresh-fetch guard).

> Where the executor's operations run through a tool that takes exclusive locks,
> the identity gate checks for stale ones and treats any as **STOP-and-report,
> never delete** — the executor cannot distinguish a stale lock from a live
> concurrent operation, and that judgment is the operator's.

### 2g. §The four-block spine — the skeleton

**Placement:** the compact skeleton's identity-gate line.

**Rationale:** the skill's own Drafting posture — *"defaults beat documentation.
The correct path should be the lazy path."* A rule in prose that is not in the
skeleton gets copy-pasted around, which is how this clause came to be
hand-written into every HEX relay.

> `Identity gate: verify remote, branch, and that each named target exists as`
> `stated; check for stale tool locks and report any without deleting. On ANY`
> `mismatch: STOP and report.`

---

## Edit set 3 — `frontend-code/SKILL.md` — RATIFIED 2026-08-03

Organized by file location. Line numbers refer to the base (`main` `f7ed7f5`,
sha256 `52f57e59…`).

**Standing principle ratified during this set:** rules about the governed work
stay; claims about the skill's own epistemic status, defensive self-justification,
and design rationale narrated to the reader all go. Provenance lives in the
Linear tickets and the session decision log, never in the skill.

### 3.1 — YAML `description`

**Topic summary** gains, after "plain-CSS styling on design tokens":
`responsive layout on container queries and fluid token scales`
and after "the OpenAPI typed-contract seam to the Python backend":
`browser media and device-permission lifecycles, media-asset governance`

**Trigger list** gains: `making a surface responsive or choosing breakpoints`,
`adding audio/video/microphone/camera or any permission-gated device access`,
`adding or referencing media assets`

### 3.2 — §Binding

- **L23–27** cut *"pinning point versions into the binding would fossilize the
  standard against whichever consumer lags."* Rule stays: version movement is not
  a rebind; currency is a separate ongoing concern.
- **L29–34** currency note: cut *"The first proving consumer runs React 18 /
  Vite 6 — inside the binding; its version lag is a maintenance item, not a
  conformance finding."* Keep the pinned-authority list and *verify at adoption*.
- **L36** cut *"is a position, not an accident."* Keep the reason (a second
  design authority, a standing fight with the tokens).
- **L40** → *"Adopting one is a **rebind** — re-derive the equivalent conventions
  rather than line-edit these — and the rebind is recorded."*

### 3.3 — §Scope of evidence — DELETE ENTIRE SECTION (L42–63)

One sentence migrates to §The misfit rule (3.5).

### 3.4 — §The experience-first path

- **L67–71** cut *"— a standard that treats the working style as an exception
  invites silent non-conformance; this one names the free zone so the fence
  around it is real."*
- **L95** cut *"and both are named"*. Content of both failure modes stays.

### 3.5 — §The misfit rule

- **L107** cut *"(House-wide rule, carried verbatim across its carrier skills.)"*
- Append, migrated from deleted §Scope of evidence:

> Thin evidence is not exception grounds. Every convention here binds at full
> force from its landing; "it wasn't proven yet" is neither a site nor a record
> exception.

- Append the ladder binding:

> **Exception tiers are `author-standard`'s ladder** — *site exception* (this
> rule's own form, plus override-with-rationale) and *record exception*. This
> skill binds to those names and defines none of its own.

### 3.6 — §Always-apply invariants (10 → 12)

**#4 replaced:**

> 4. **Config from one source, thrice.** Every visual value — color, type,
>    spacing, motion — comes from the design tokens; nothing visual is hardcoded.
>    Runtime config flows through one typed config module; scattered
>    `import.meta.env` reads are the frontend's scattered-`os.environ`. Every
>    shipped media asset — audio, video, imagery, fonts — is reached through one
>    typed manifest, never by string literal at the point of use (§ Media assets).

**#5 replaced:**

> 5. **A resource that must be singular flows through one owner.** Outbound HTTP
>    goes through the canonical seam client (§ The typed-contract seam) — never
>    scattered per-call fetches. Browser media singletons — `AudioContext`,
>    `MediaStream`, `SpeechRecognition` and their kin — go through one provider or
>    module singleton reached through a seam, never constructed at point of use
>    (§ Browser media). The reasons differ — uniformity for the client,
>    browser-imposed scarcity for the media singletons — and the rule does not.

**#11 and #12 appended:**

> 11. **Responsive by default.** Every surface adapts to its environment. A
>     fixed-frame or fixed-aspect surface is a **record exception** that names
>     which part of it claims WCAG 1.4.10's two-dimensional-layout exception, and
>     why (§ Responsive layout).
> 12. **Permission-gated device access is requested on an explicit user gesture,
>     and its outcome is state.** Microphone, camera, geolocation, clipboard —
>     never requested at mount, and the outcome is modeled as first-class rendered
>     state, never swallowed (§ Browser media).

**L145** cut *"Declared misfits, not oversights."*

### 3.7 — §Components and hooks

**Bullet 3 replaced:**

> - **Effects synchronize with external systems; they are not a data-flow tool.**
>   Per React's own guidance: if it can be computed in render or handled in an
>   event handler, it is not an effect. **Components subscribe to external event
>   sources through `useSyncExternalStore`**, not `useEffect` + `setState` — the
>   latter is this same violation in its most common disguise.

**New sub-block appended to the section** (not a bullet — at ~130 words it would
be triple its neighbours, and the four bullets are general shape rules):

> **Time-sequenced work has one owner and one cancellation contract.**
> Choreography — scheduled sequences, staged animation, timed media — lives in a
> hook or `lib/` module, never inline in a surface, and exposes start and cancel.
> Internals are free; **the seam is uniform.** `AbortSignal` is the house currency
> for that seam — hand-rolled cancellation tokens (monotonic sequence counters,
> timer-handle arrays exposed as the public contract) are the named anti-pattern.
> `AbortSignal.timeout()` and `AbortSignal.any()` are convenient where available;
> both reached baseline only in 2024, so neither is required.
>
> A cancelled sequence must **settle** every promise it created: a pending timer
> resolving a promise is cancelled by resolving or rejecting it, never by dropping
> the timer, or the awaiting frame is retained forever with its whole closure.
> Timer registries release fired entries.
>
> A timeline is **mechanism code** — fake-timer testable, under the coverage gate.
> It does not qualify for the tautological-assertion exclusion
> (`reference/testing.md`).

### 3.8 — §Responsive layout — NEW SECTION

**Placement:** immediately after §Components and hooks. Sections 3.9 and 3.10
follow it, so the three new authoring sections sit contiguous.

> ## Responsive layout
>
> **Responsive is the default (invariant #11).** This section is how that gets
> built; the accessibility criteria it serves are §Accessibility's floor, cited
> rather than restated.
>
> **The two query kinds answer different questions.** Media queries answer *what
> is the environment?* — viewport, orientation, media type, and user preferences
> including `prefers-reduced-motion` and `prefers-color-scheme`. Container queries
> answer *how much room does this component have?* Page shell and environment
> response are media-queried; component-level adaptation is container-queried.
> **Neither is a fallback for the other.**
>
> **Container-query friction, named so it isn't discovered the hard way:** a
> container cannot query itself — measure an ancestor, and expect a wrapper
> element; flex items need explicit sizing or the container collapses; custom
> properties do not resolve inside container queries. **Size queries are baseline;
> style queries and scroll-state queries are not** — style queries lack Firefox,
> scroll-state is Chromium-only. Building on a non-baseline query is a site
> exception with the support gap stated.
>
> **Fluid type and space express on the design tokens.** Fluid steps use `clamp()`
> with a `rem` component in the middle value — pure `vw` does not scale under
> browser zoom and fails SC 1.4.4. **Every fluid step satisfies
> `max ≤ 2.5 × min`**, which is what keeps 200% reachable at every viewport width.
> As with contrast, the values live in the repo's design-token authority and this
> skill points at them: **the token authority carries the named obligation that
> every fluid step is rem-anchored and inside the 2.5× ratio.**
>
> **Fixed-frame surfaces.** A surface authored to one viewport and scaled to fit
> is a **record exception** (#11). Two criteria pull apart, and the record must
> treat them differently:
>
> - **SC 1.4.10 Reflow is arguable.** Its exception covers content requiring
>   two-dimensional layout for usage or meaning — maps and diagrams, data tables,
>   games, presentations, persistent toolbars, and layouts where consistent
>   orientation to related sections is important for understandability or
>   functionality. Instrument panels and HUDs live here. The record **names which
>   part of the surface claims the exception and why**; the exception does not
>   extend to surrounding chrome, which reflows on its own.
> - **SC 1.4.4 Resize Text is not.** It carries no such exception. A frame scaled
>   by a factor computed from viewport size cancels browser zoom exactly — halve
>   the viewport, halve the scale, rendered size unchanged — so zoom becomes a
>   mathematical no-op and no scaling mechanism remains. **`transform: scale()`
>   fitted to the viewport is a named anti-pattern**, not a layout technique.
>
> Where the record is granted, the obligations are: a **declared supported
> viewport range**; AA met **within** that range, not merely at the design size; a
> genuine text-resize path; and interactive target sizes evaluated **at the
> minimum supported scale rather than at scale 1**, against §Accessibility's
> target-size floor and its exceptions.

### 3.9 — §Browser media — NEW SECTION

> ## Browser media
>
> Invariant #5 says who owns a media singleton. This section says what its life
> looks like, and what happens when the user says no.
>
> **Static playback and streaming sessions are different lifecycles, and both are
> named.**
>
> *Static* — pre-rendered clips, synthesized one-shot cues — is bounded and
> fire-and-forget. The context may be long-lived; caches are keyed and bounded;
> teardown rides app teardown.
>
> *Streaming* — live capture, live synthesis, a duplex transport — is a
> **session**. Exactly one live session at a time. Teardown is deterministic and
> ordered, on stop and on unmount: release `MediaStream` tracks, disconnect nodes,
> release the context. Cancellation is explicit, never implied by garbage
> collection — the cancellation contract in §Components and hooks applies. Where a
> network transport is involved, reconnect posture is stated.
>
> **Device permission.** Invariant #12 requires the request on a user gesture and
> the outcome as state. The outcomes to model are at least: **unavailable** (no
> device, insecure context — `navigator.mediaDevices` is undefined on an insecure
> origin and property access throws — or unsupported browser), **dismissed**,
> **denied**, **granted**. Each is a rendered state; none is swallowed.
>
> When a permission-gated modality is unavailable, fall back to **the alternate
> modality §Accessibility item 6 already requires** — not to a simulation of the
> unavailable one. Simulating an input the user does not have manufactures a
> success signal: the UI reports success while the feature is dead.
>
> **Scope the catch to the permission call alone.** A single `try` spanning both
> the request and the setup that follows it reports your own bugs as the user's
> missing hardware — a defect in analyser wiring or an animation frame presents,
> permanently and silently, as "you have no microphone."
>
> **Not authored here: how streamed events reach React state.** Subscription
> lifecycle, backpressure and reconnect conventions for a live event source are
> un-governed. Components subscribe to external event sources through
> `useSyncExternalStore` (§ Components and hooks); beyond that line, there is no
> house convention to conform to yet.

**No evidence note.** Struck per R2.

### 3.10 — §Media assets — NEW SECTION

> ## Media assets
>
> Invariant #4 says media assets come from one manifest. The rest follows from how
> bundlers work.
>
> **The manifest is a typed module** carrying id, path, provenance, and whatever
> per-asset metadata the runtime needs — per-clip loudness trims, durations,
> captions. A string concatenated at a call site is not a reference; it is a lookup
> that fails silently when it misses.
>
> **Assets are reached through the manifest by import**, so the bundler
> fingerprints them. Content-hashed filenames are the consequence, not a separate
> act. `public/` (or its equivalent) is for assets that must keep a stable URL —
> referenced from outside the build, `robots.txt`-class — and using it is a **site
> exception** with its reason stated. **Hand-versioned filenames are the symptom of
> an asset that skipped the bundler**, and they interact badly with immutable cache
> headers.
>
> **License is dependency discipline's** (§ Dependency discipline, item 4): a
> proprietary-licensed or recurring-cost asset is a record exception, exactly as a
> dependency would be. **Cache posture is delivery's** — the manifest is what makes
> assets addressable to it.

### 3.11 — §The typed-contract seam

- **L181** → *"Swapping generators is a line-edit; abandoning generation is a
  **record exception**."*
- **L199–202** DELETE the *Scope of evidence* note (R2).
- **New item 6** appended:

> 6. **Vendor-surface declarations are not domain types, and item 1's ban does not
>    reach them.** Where the TS DOM lib doesn't carry a browser surface — Web
>    Speech, vendor-prefixed constructors, experimental APIs — prefer a maintained
>    types-only package; where none exists, hand-declare the minimal structural
>    shape **once**, in a single types module, never per consumer. Vendor-prefixed
>    fallbacks resolve in one place. Item 1's ban on hand-written mirrors targets
>    your own backend's models; a `SpeechRecognition` interface the platform never
>    shipped types for is not a mirror of anything you own.

### 3.12 — §Strictness

- **L213** cut *"— a ruling, not an oversight."* Keep *(real friction with
  third-party types)*.
- **L218–221** CUT the entire trailing justification: *"The upstream guidance
  reserves strict presets for teams highly proficient in TypeScript; under the
  house working model — code authored by an agent operating under this skill —
  that condition is met by construction, and a stricter machine-checkable envelope
  is pure gain."* The rule is: use these presets.
- **L211** UNCHANGED — *"On existing codebases, adopt with rationale rather than by
  default"* is a two-branch rule, not an exception. Ruled out of the ladder sweep.

### 3.13 — §Accessibility

- **L249** cut *"Scored, motion-heavy surfaces are exactly where this rule earns
  its place."*
- **Item 7 replaced:**

> 7. **Check the 2.2-specific AA criteria by name** — target size (minimum), focus
>    not obscured, dragging alternatives, accessible authentication, consistent
>    help — they are the ones a 2.1-era instinct misses. **Target size is 24×24 CSS
>    pixels with five exceptions** — spacing (undersized targets whose 24px-diameter
>    circles do not intersect), equivalent (the same function reachable from a
>    conforming control on the page), inline (constrained by surrounding
>    line-height), user-agent-controlled, and essential. Read the exceptions before
>    rebuilding a control: a dense cluster with adequate spacing already conforms.

- **L239** UNCHANGED — *"because nothing reloads"* explains a mechanism, not a
  decision. Ratified as a keep.

### 3.14 — §Client security

- **L279–280** cut *"the seam is declared here the way the service skills declare
  the container-image seam."*
- **L285–288** DELETE the *Scope of evidence* note (R2).

### 3.15 — §Dependency discipline

- **L305** → *"Default posture; **override is a site exception** with its rationale."*
- **L309** → *"a **record exception**, not an `npm install`"*
- **L311–312** → *"4. **The cost gate.** A dependency **or shipped media asset**
  introducing a recurring cost or a proprietary license is never routine — a
  **record exception**, always."* Cut *"The default stack is free by construction,
  not by luck."*
- **L313** cut *"not ambient"*.
- **L316–319** → *"Not carried: provenance-attestation requirements,
  install-script lockdown regimes, exact-version manifests. Supply-chain posture
  beyond the lockfile-and-audit floor is un-governed."*

### 3.16 — §Where to look

**Split trigger replaced:**

> Split trigger, stated: content graduates to its own home when **a distinct role
> becomes a real consumer of it independently of the authoring discipline** — and
> that is the load-bearing half. Answering its own task-shaped prompt is not
> sufficient on its own: most sections here do that, and splitting on it would
> leave this skill a stub surrounded by references.

**Authority pins replaced** (two dates — a re-pin would imply re-verification of
the whole list, which did not happen):

> - **Public authority, pinned at authoring, verify currency at adoption.**
>   *Pinned 2026-07-21:* the Rules of React (react.dev); the TypeScript TSConfig
>   reference; typescript-eslint shared-config guidance; Testing Library's guiding
>   principles; WCAG 2.2 (W3C Recommendation, rev. 2024-12-12); the OWASP XSS/CSP
>   cheat sheets and browser-storage guidance; the OAuth browser-based-apps BCP;
>   Vite documentation. *Pinned 2026-08-03:* the CSS containment and
>   container-query specifications; WCAG 2.2 Understanding documents for SC 1.4.4,
>   1.4.10 and 2.5.8; the Web Audio, MediaStream and Permissions specifications;
>   the DOM standard's `AbortController`/`AbortSignal`; Vite's static-asset
>   handling guide.

---

## Edit set 4 — `frontend-code/reference/testing.md` — RATIFIED 2026-08-03

### 4.1 — Sweep cuts

- **L7–8** DELETE the sentence *"The service-side testing skill is pytest-bound
  and names any other framework a rebind; this file* is *that rebind, derived
  fresh rather than line-edited."*
- **L38–41** REPLACE with: *"**E2e is not governed here.** No house convention
  exists for browser-automation testing; one is adopted when a real need arrives."*
- **L56** REPLACE with: *"Test-at-hardening is the frontend analogue of
  test-first."* (cuts *"honest"* and the trailing defense)

### 4.2 — §Coverage (the derived form) — SECTION REPLACED

> ## Coverage (the derived form)
>
> Coverage is measured and gated **per layer, not globally** — global line
> coverage over JSX-heavy presentation measures render execution, not behavior
> specification, and is a gamed number by construction.
>
> - **Mechanism layers** (`lib/`, `hooks/`, seams/clients, engine logic) carry an
>   **enforced floor: 90% line coverage** — the house default constant applied to
>   the derived form; declared as a default, and **override is a site exception**
>   with its rationale.
> - **Surfaces** are exercised through component tests with coverage **measured
>   and reported but ungated initially**. Whether surfaces earn their own gate,
>   and at what number, is not yet ruled.
>
> **The tautological-assertion exclusion, and its bound.** Code that can only be
> asserted tautologically is excluded from the mechanism floor. A test asserting
> that an audio graph was wired the way the wiring code wires it fails when the
> code changes, not when the behavior is wrong — it specifies nothing, and paying
> mock ceremony for it buys a coverage number rather than a specification.
>
> **The test: would the assertion fail when the behavior is wrong, or only when
> the code changes?**
>
> **Streaming-session state is not excluded.** Connection state, permission state,
> transcript accumulation, level derivation and teardown ordering are all
> observable and specifiable, and they stay under the gate.
>
> The exclusion is claimed at the site — the omit entry carries its reason where
> it omits — and **the gate reports the excluded line count alongside the floor.**
> An exclusion that grows silently turns a 90% floor over the remainder into a
> number that means nothing.
>
> **Anti-gaming rules:**
>
> - The omit list holds only what the exclusion above covers, plus infrastructure
>   with no behavior to specify; no module with assertable behavior escapes
>   measurement.
> - **Directory placement is not a dodge.** Moving mechanism logic into a surface
>   file to escape the gated layers is the named cheat; the layering rules in
>   SKILL.md make it a violation independently of coverage.
> - Coverage is confirmed at the gate quartet (type-check, lint, tests, coverage),
>   honestly — a threshold met by **undeclared** omission is not met.

**Two drafting notes, ratified.** The heading names the exclusion exactly so
SKILL.md §Components and hooks' citation resolves to matching words.
*"Undeclared"* in the final bullet is load-bearing: without it, *"a threshold met
by omission is not met"* contradicts the exclusion just sanctioned.

---

## Edit set 5 — `code-review/reference/conformance-checklist.md` — RATIFIED 2026-08-03

**Frontend code section: five amended, four new (10 → 14 items).**
No change to `code-review/SKILL.md` or its description — no new section, and the
description already names the Frontend section generically.

### 5.1 — Amended items

**Item 2** →
> No hardcoded visual values — color, type, spacing, and motion come from the
> design tokens; runtime config from the typed config module, no scattered
> `import.meta.env` reads; **media assets referenced through the typed manifest,
> never by string literal**.

**Item 5** →
> Generated contract types regenerated and drift-checked, never hand-edited; no
> hand-written mirror of a backend model — **vendor-surface declarations (Web
> Speech, prefixed constructors) are not mirrors, and are declared once in a
> single types module**.

*This item is the instrument that produces G3's false finding — HEB-97's
complaint was that "a reviewer scanning for that will flag legitimate
hand-declared browser APIs," and this checkbox is the scan.*

**Item 8** →
> Accessibility holds at the floor — semantic elements, accessible names on
> interactive elements, keyboard path intact, focus managed on navigation and
> dialog changes, motion respects reduced-motion; **target-size findings check
> 2.5.8's exceptions before demanding a rebuild**.

*Same logic: D3.d found HEB-95 over-calling a 2.5.8 failure the Spacing
exception probably covers. The place to stop that recurring is the review
instrument, not the authoring skill.*

**Item 9** →
> Tests query by role and accessible name; mechanism-layer coverage floor met
> honestly — **exclusions limited to tautologically-assertable code, claimed at
> the site, with the excluded line count reported**; no directory-placement
> dodges.

**Item 10** →
> New dependency **or media-asset** adoptions justified — architecture-shaping,
> recurring-cost, or proprietary-license adoptions are **record exceptions**.

### 5.2 — New items

> - [ ] Surfaces are responsive — a fixed-frame or scaled-to-fit surface carries a
>       record exception naming its 1.4.10 claim; fluid type steps are rem-anchored
>       and within the 2.5× ratio.
> - [ ] Browser media singletons (`AudioContext`, `MediaStream`,
>       `SpeechRecognition`) have one owner reached through a seam, none constructed
>       at point of use; streaming sessions tear down deterministically on stop and
>       on unmount.
> - [ ] Permission-gated device access requested on a user gesture with its outcome
>       modeled as state (unavailable / dismissed / denied / granted); the catch
>       scopes to the permission call; no fallback simulates the unavailable
>       modality.
> - [ ] Time-sequenced work lives in a hook or `lib/` module exposing start and
>       cancel; cancellation settles every promise it created; no hand-rolled
>       cancellation token stands in for `AbortSignal`.

---

# ALL FIVE EDIT SETS AUTHORED AND RATIFIED — 2026-08-03

| Skill | File(s) | Source |
|---|---|---|
| `author-standard` | `SKILL.md` | D9 |
| `app-delivery-pipeline` | `reference/03-static-frontend-leg.md` | D11.b |
| `author-execution-relay` | `SKILL.md` | HEB-98 / D5, D6, D12 |
| `frontend-code` | `SKILL.md`, `reference/testing.md` | HEB-95/96/97 + R1–R5 + sweep |
| `code-review` | `reference/conformance-checklist.md` | integration read F1 |

Plus `plugins/bedrock/.claude-plugin/plugin.json` → **2.2.0**.
`marketplace.json` verified untouched at execution (D7.c).
