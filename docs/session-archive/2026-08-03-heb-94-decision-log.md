# Decision log — bedrock 2.2.0 amendment batch

**Session:** 2026-08-03 (US Eastern). Deliberation surface: Claude (Cowork).
**Substrate read:** `~/Documents/GitHub/bedrock` @ `main` `f7ed7f5`, working tree clean.
Read whole: `frontend-code/SKILL.md`, `frontend-code/reference/testing.md`,
`author-execution-relay/SKILL.md`, `author-standard/SKILL.md`, repo `CLAUDE.md`,
`plugin.json` (v2.1.0). `author-execution-relay/SKILL.md` sha256 `2019c239…`
verified equal to HEB-98's pin.

**Standing posture for this session (operator, 2026-08-03):**
- Ratified text on the tickets is **statement of intent, re-ratifiable**. It was
  authored under different context; challenge is licensed.
- **This log is the source of truth for the work.** Linear reconciles at the end.
- Target: **one bedrock plugin version** carrying all changes. Batch composition
  may grow.

---

## Deliberation docket

| # | Item | State |
|---|---|---|
| D1 | Invariant placement | **SETTLED** |
| D9 | Exception ladder — misfit vs. decision-record grade | **SETTLED** |
| D3 | HEB-95 responsive posture + layout conventions | open |
| D4 | `testing.md` coverage edit / effect-only exclusion | open |
| D10 | HEB-96 "one cancellation mechanism per codebase" | open |
| D11 | G5 content-hash versioning — boundary with delivery | open |
| D5 | HEB-98 shared parent clause | open |
| D6 | HEB-98 clause B placement | open |
| D12 | HEB-98 gap-1 clause A at n=0 | open |
| D7 | Skill description / trigger surface | open |
| D8 | §Scope of evidence rewrite + G4 deferral line | open |
| D2 | File shape — one file or a new reference | open (LAST) |

Closed risks: R1 (invariant capacity) — resolved by D1.e. R4 (G2 clause (c)
back-distillation admission) — folds into D8. R3 (volume) — feeds D2.

---

## D1 — Invariant placement — SETTLED 2026-08-03

### D1.e — the membership test and the standing form (ratified)

The invariant list's heading claims "every module," but the list does not obey
it: #5 binds only where HTTP calls happen, #8 only at boundaries, #9 only where
credentials exist. Its real form is a **universally-quantified conditional** —
*wherever this condition arises, this rule binds, with no local escape.*

**Ratified test:**
- **Invariant** — the rule has no local softening. A section may elaborate it,
  never qualify it.
- **Section** — mechanics, lifecycles, worked forms. What you need to comply,
  none of what makes it binding.

**Ratified standing form:** *the invariant states the rule; the section carries
the mechanics.* Widening an invariant replaces words rather than adding them.
Accepted cost, stated: the invariant list becomes more index-like — formalizing
a drift already underway (#10 is already one sentence plus a section pointer),
not starting one.

### D1.a–c (ratified together)

- **Widen #5.** Not on the ticket's "scarcity" rationale, which is not #5's.
  The unifying axis: **a resource whose correctness depends on there being one
  of it flows through one owner.** HTTP client: one, so correlation ID and error
  discipline stay uniform. `AudioContext`: one, because the browser caps them.
  Same rule, two reasons for the same rule. G1 clause 1 disappears into the
  invariant; no section prose needed for it.
- **Widen #4 to "thrice"** — visual values from tokens, runtime config from one
  typed module, media assets from one typed manifest. **Manifest half only**;
  content-hash-at-build is held for D11.
- **Responsive-by-default becomes #11.** Condition: always. Escape is
  decision-record grade — stronger than the misfit rule, not weaker.

### D1.d — G2 device permission (ratified)

**Finding: HEB-97's diagnosis is 2-for-3.** It frames G1/G2/G5 as scope gaps in
#5/#6/#4. Right for #5 and #4. Wrong for #6 — G2's three clauses have three
different homes:

- **(a)** request on explicit gesture + outcome modeled as first-class state
  → **new invariant #12**. Narrowest on the list; precedent is #9 (credentials),
  comparably narrow and explicitly binding ahead of its first consumer. The
  failure mode G2 documents is someone not knowing the rule exists while writing
  a `catch {}` — an invariant is read by everyone, a section on demand.
- **(b)** fall back to the alternate modality → **pointer** to §Accessibility
  item 6. The ticket admits this is a citation; it should not become new text.
- **(c)** scope the catch to the permission call alone → **section mechanics**,
  sharpening #6. Not a gap in #6; an application of it.

Rejected: widening #6. "Errors are rendered states" is one of the crispest lines
in the skill; folding permission outcomes into it blurs the rule.

### Resulting placement map

| Item | Invariant | Section |
|---|---|---|
| G1 clause 1 — media singletons | widen #5 | — |
| G1 clause 2 — static vs. streaming lifecycles | — | new section |
| G1 clause 3 — effect-only coverage | — | `testing.md` (D4) |
| G2 (a) | new #12 | — |
| G2 (b) | — | pointer to §A11y item 6 |
| G2 (c) | — | new section |
| G3 — ambient declarations | none | §The typed-contract seam |
| G5 — media assets | widen #4 (manifest half) | small section |
| G4-partial — `useSyncExternalStore` | none | §Components and hooks |
| HEB-96 — timeline/choreography | none | §Components and hooks |
| HEB-95 — responsive-by-default | new #11 | new section |

Net: 10 → 12 invariants, two widened.

---

## D9 — Exception ladder — SETTLED 2026-08-03

**Finding.** `frontend-code` carries **five distinct phrasings for two real tiers**:

*Site-level* (state a reason at the site, proceed, no external artifact) — the
misfit rule; "declared as a default with override-with-rationale" (coverage
floor); "Default posture; override with rationale" (audit); "adopt with
rationale rather than by default" (`noUncheckedIndexedAccess`).

*Record-level* (produce an ADR/DDR, goes through review) — "decision-record
grade" (dependency discipline, ×2); "a departure that takes a decision record"
(abandoning generation); "rebind-grade departure and takes a decision record"
(component library).

**Rebind is not an exception** — it is a declaration that the skill does not
govern the case. Currently tangled into the record-level phrasings.

Post-batch this batch adds one instance at each tier (HEB-95 fixed-frame →
record; HEB-97 effect-only → site). **Seven instances, five phrasings, zero
names.**

**Ratified: option (c), minimal.**

- The ladder is **house-wide vocabulary** and is defined **in `author-standard`**,
  under §Harden it beside "One house vocabulary." Defining it inside
  `frontend-code` would create the per-artifact ladder that rule prohibits.
  Precedent: `code-review` owns BLOCKING/MATERIAL/COSMETIC/POSITIVE; siblings cite.
- ~8 lines: two named tiers + rebind marked explicitly as **not** an exception.
- **The lighter tier is the default; escalation needs a reason** — naming a
  heavier tier otherwise invites reaching for it.
- `frontend-code` declares its binding in one line, uses the names at its seven sites.
- The other five skills are **known, recorded drift** with a follow-up ticket.
  Not fixed in this batch.

**Under-govern objection considered and rejected.** The recurrence *is* the
evidence — the same argument HEB-98 uses to promote its lock preflight ("already
being copy-pasted into every relay ... the membership signal"). Cannot accept it
there and refuse it here.

**Consequence: `author-standard` becomes a third skill in the PR.**

**Standing constraint either way:** HEB-95 and HEB-97's exception clauses use
existing phrases verbatim or the new tier names. A sixth phrasing has no argument
for it.

---

## D3 — HEB-95 responsive posture + layout conventions — SETTLED 2026-08-03

**Authority fresh-fetched, read whole:** WCAG 2.2 Understanding docs for SC 1.4.4,
1.4.10, 2.5.8; LogRocket "Container queries in 2026"; Smashing "Addressing
Accessibility Concerns With Using Fluid Type." Broader search results skimmed for
currency only.

### D3.a — the two query kinds answer different questions (ratified)

Rejected: "container-queries-first." Not a preference ordering — a
**discriminating axis**.

- **Media queries** answer *what is the environment?* — viewport, orientation,
  media type, **and user preferences**. `prefers-reduced-motion` is already
  mandated at §Accessibility item 5 and container queries cannot express it. A
  "media queries are legacy" posture would collide with the skill's own rule.
- **Container queries** answer *how much room does this component have?*
- Component-level adaptation is container-queried; page shell and environment
  response is media-queried. **Neither is a fallback for the other.**

### D3.b — fluid scale on tokens (ratified)

Takes the **identical shape** to §Accessibility item 4's contrast rule — the
skill points at the token authority and states the obligation, never a value.

- Fluid steps use `clamp()` with a **`rem` component in the middle value**. Pure
  `vw` fails SC 1.4.4 — browsers do not scale viewport units under zoom.
- **Hard rule: `max ≤ 2.5 × min` on every fluid step.**
- The token authority carries the named obligation, as it already does for contrast.

### D3.c — fixed-frame is not automatically a deviation (ratified — reframe)

**Reverses HEB-95's ratified intent.** The ticket said a fixed frame is "a
documented exception requiring a decision record." The spec supplies the
exception itself: SC 1.4.10 excepts *"content where consistent orientation to
related sections of content is important for understandability, functionality,
or both,"* persistent toolbars, games, presentations, data tables, and images
required for understanding. Instrument panels and HUDs are squarely in that
territory — such a surface may be **conforming, not excepted**.

SC 1.4.4 has **no** such exception.

Ratified clause shape:

> A fixed-frame surface is record-grade, and the record's job is to **name which
> part of the surface claims the 1.4.10 two-dimensional-layout exception and
> why** — the exception does not extend to surrounding chrome. **1.4.4 is not
> negotiable by record:** a frame that scales inversely with the viewport makes
> zoom a mathematical no-op and fails outright. Obligations either way: declared
> supported viewport range, AA met within it, a real text-resize path, and target
> sizes evaluated **at the minimum supported scale**, not at scale 1.

The record **argues the exception**; it does not **waive the criterion**.
Naming the `transform: scale()`-to-fit pattern is forward-derivable from the
spec (any transform scaling inversely with viewport cancels zoom), not distilled
from HEX.

### D3.d — evidence correction (ratified)

HEB-95 asserts three AA failures. Against the spec text it is **1-for-3**:

| Claim | Verdict |
|---|---|
| 1.4.4 Resize Text — hard fail | **Confirmed.** Any one scaling mechanism satisfies 1.4.4; `scale(min(iw/1360, ih/840))` cancels all of them. |
| 1.4.10 Reflow — fail | **Arguable, not established.** The 2D-layout exception plausibly covers the surface; the ticket does not engage it. |
| 2.5.8 Target Size — fail at scale 1 | **Probably wrong.** The **Spacing** exception permits sub-24px targets when 24px-diameter circles centered on each do not intersect. 23px chips with 6–7px gaps ≈ 29–30px pitch — likely conforming. |

Consequence for the skill: **name 2.5.8's five exceptions** (spacing, equivalent,
inline, user agent control, essential) rather than a bare 24×24 floor, or authors
over-build against a criterion that already carries the flexibility they need.

### D3.e — name the container-query friction (ratified, terse)

One bullet. A convention that mandates a tool without naming its traps sets
authors up:

- a container **cannot query itself** — measure an ancestor; expect a wrapper
- flex items need explicit sizing or the container collapses
- custom properties do not work inside container queries
- **size queries are baseline; style queries and scroll-state queries are not**
  (Firefox lacks style queries; scroll-state is Chromium-only). A skill that
  mandates a non-baseline feature is a defect.

---

## D4 — Effect-only coverage exclusion — SETTLED 2026-08-03

### D4.a + c — axis reframe, landed as an edit (ratified)

**"Effect-only" is the wrong axis and "genuinely untestable" is a false claim.**
Web Audio *is* testable — mock `AudioContext`, assert `connect()`. HEB-97 admits
this when it prices the alternative at "~370 lines of AudioContext-mock
ceremony." The real question is whether the assertion can be **non-tautological**.

Ratified frame — connects to an existing rule two sections up in the same file
(*"Snapshots are used sparingly ... a test that specifies nothing"*):

> **The exclusion covers code that can only be asserted tautologically.** A test
> that asserts the audio graph was wired the way the wiring code wires it fails
> when the code changes, not when the behavior is wrong — it specifies nothing,
> and paying mock ceremony for it buys a coverage number rather than a
> specification.

**HEB-97's test line is struck.** *"If you can assert it without hearing it, it's
mechanism code"* admits the tautological case it exists to exclude — you *can*
assert `connect()` without hearing it. Replacement, derived from the
meaningful-red discipline already in the file:

> **The test: would the assertion fail when the behavior is wrong, or only when
> the code changes?**

Checked against the streaming-state list the ticket holds under the gate —
connection state, permission state, transcript accumulation, level derivation,
teardown ordering. All five take non-tautological assertions. The ticket's
substance survives intact.

**Edit, not append.** The anti-gaming bullet's *"genuinely untestable
infrastructure"* is a capability claim the exclusion cannot satisfy; it changes
or the two rules contradict. The ticket's *"stated at the site rather than buried
in an omit list"* is a false either/or — coverage tools require an omit entry.
It is **both**: the omit entry carries its reason at the site it omits.

### D4.b — report the excluded mass at the gate (ratified)

The exclusion **is** the sanctioned exit for the 90% floor's pressure
(`author-standard`: "pressure needs an exit"). An exit with no bound is a hole.

> The gate reports the floor **and the excluded line count**. A growing exclusion
> is visible, not silent.

The honest form of the file's own *"a threshold met by omission is not met."*

---

## D10 — HEB-96 cancellation clause — SETTLED 2026-08-03

**Finding: the headline clause does not prevent the bug its own evidence cites.**
F22 is a promise that never settles because `clearTimers()` drops the timer
resolving it. Had both files used the *same* handle-array mechanism, **F22 still
happens.** Clause 2 (settle every promise) is what prevents it. The ticket's
headline and its load-bearing rule are inverted.

### D10.a — "one contract," not "one mechanism" (ratified — reframe)

"One cancellation mechanism per codebase" is also unenforceable and probably
wrong: React effect cleanup, an aborted fetch, and a beat-quantized scheduler's
teardown are different mechanisms with different lifetimes. Mandating one forces
a lowest-common-denominator abstraction or standing misfit invocation.

> **Time-sequenced work has one owner and one cancellation *contract*.**
> Choreography — scheduled sequences, staged animation, timed media — lives in a
> hook or `lib/` module, never inline in a surface, and exposes start and cancel.
> Internals are free; **the seam is uniform.**
>
> A cancelled sequence must **settle** every promise it created: a pending timer
> resolving a promise is cancelled by resolving or rejecting it, never by
> dropping the timer, or the awaiting frame is retained forever. Timer registries
> release fired entries.

### D10.b — `AbortSignal` as named house currency (ratified, with caveat)

Hand-rolled cancellation tokens — monotonic sequence counters, handle arrays as
the *public* contract — become the named anti-pattern.

Fresh-checked on MDN, not asserted:

- **`AbortSignal` / `AbortController` — "Baseline Widely available," across
  browsers since April 2018.** Safe to mandate.
- **`AbortSignal.timeout()` (Baseline 2024, newly available, April 2024) and
  `AbortSignal.any()` (Baseline 2024, newly available, March 2024)** — named as
  available conveniences, **never as required**, per D3.e's ruling that
  mandating a non-baseline feature is a defect.

---

## D11 — G5 content-hash versioning — OPEN (presented 2026-08-03)

Authority fresh-fetched: Vite static-asset guide (read whole via fetch);
`app-delivery-pipeline/reference/03-static-frontend-leg.md` (staged, read whole).

### D11.a — the rule is `frontend-code`'s, restated (ratified — reframe)

Risk-6 framing was wrong. Not delivery's rule leaking in — **`frontend-code`'s
rule stated as an outcome the author does not control.**

Vite: imported assets get hashed filenames; `public/` files are *"copied to the
dist directory as-is, without hashing."* Docs state the preference: *"prefer
importing assets unless you specifically need the guarantees provided by the
`public` directory."*

> Assets are reached through the manifest **by import**, so the bundler
> fingerprints them. `public/` is for assets that must keep a stable URL —
> referenced outside the build, `robots.txt`-class — and using it is a
> site-level exception with its reason stated. **Hand-versioned filenames are the
> symptom of an asset that skipped the bundler.**

### D11.b — the cache collision, fixed now (ratified)

**Live defect in a shipped skill, seen by no ticket.**
`app-delivery-pipeline/reference/03-static-frontend-leg.md` §5 globs
`/assets/**` → `Cache-Control: public, max-age=31536000, immutable`, with the
parenthetical *"everything Vite emits with a content hash."* Vite copies
`public/`'s **contents** to the root of `dist/`, so `public/assets/clip.mp3` →
`dist/assets/clip.mp3` — matching the glob **with no hash in the filename.** The
house rule serves un-fingerprinted assets immutable for a year.

The intent in the parenthetical is right; the glob does not implement it. And
this is *why* the hand-versioned filename exists — given `public/assets/` under
an immutable header, a version suffix was the only cache-buster available.

**Fix now, one line:** the immutable header is scoped to bundler-emitted hashed
output; anything copied verbatim from `public/` is served `no-cache` regardless
of path.

**`app-delivery-pipeline` becomes the fourth skill in this PR.** Running count:
`frontend-code`, `author-execution-relay`, `author-standard` (D9),
`app-delivery-pipeline` (here).

### D11.c — provenance and license (ratified)

**Point, don't write.** Dependency discipline #4 already carries the gate — *"A
dependency introducing a recurring cost or a proprietary license is never
routine — decision-record grade, always."* A proprietary-licensed media asset is
the same species. Extend #4's scope by a clause rather than authoring a parallel
obligation. Provenance (*where did this clip come from*) is genuinely distinct
from license and belongs in the manifest's declared fields.

---

## D5 / D6 / D12 — the relay-skill cluster — SETTLED 2026-08-03

### D5 — shared parent clause: YES, but not the ticket's parent (ratified — reversal)

**The ticket's frame fails.** It claims both gaps are *"places where a party
outside the relay's two-actor model touches the artifact"* and that *"neither of
these actors is any of the three."* Gap 1's toolchain, yes. **Gap 2's mutator is
the drafting surface — actor #1** of the skill's own declared three-actor model.

**The frame that survives.** Gap 1: executor issues `git commit`, toolchain
rewrites the bytes. Gap 2: drafting surface issues `git status`, toolchain takes
a lock. In both, **the tool did something the actor did not ask for and did not
know about.** The class is not *who touches* — it is **the tool's undeclared side
effects**, on the write path and on the read path.

Generative where the specifics are not: reaches editor format-on-save, a linter's
`--fix` in a pre-commit, `npm install` rewriting a lockfile. Mandated by the
skill's own Drafting posture — *"Phrase constraints as values, not procedures ...
Values generalize to the unscripted condition the relay's author didn't foresee."*

> **A tool operation does more than it says.** Every command a relay's author or
> executor issues runs through a toolchain with its own mutation paths — hooks,
> templates, filters, locks, caches, format-on-save. The relay never assumes the
> operation was only what it named. On the **write** path, verify the artifact the
> tool stored, not the input you handed it. On the **read** path, use the form
> that observes without mutating.

Net text goes **down**: one value plus two short applications, versus four
free-standing clauses. Closes the question the ticket flagged open at ratification.

### D6 — placement (ratified)

- **Parent** → **§Premise discipline**, whose opening line is the argument for it
  (*"Every relay carries silent premises ... and the author didn't notice they
  were premises"*). Gap 2's read-only clause sits directly under it.
- **"A third drift class"** → §Pin discipline (extends the two named drift classes).
- **"Verify the durable form"** → §Pin discipline (it is what a pin is *discharged
  against*).
- **§Output discipline's** *"validate with a hash or token-integrity check"* →
  **pointer fix.** That is the sentence HEB-98 names incomplete; landing the
  correction elsewhere while leaving it would keep it quietly wrong.
- **Stale-lock check** → §The four-block spine, identity gate, per the ticket.

### D12 — gap-1 clause A: keep, reshaped (ratified)

Clause A is a **closed enumeration** (hooks, `commit.template`, `core.autocrlf`,
`.gitattributes`) in a skill that is not git-bound — the skill violating its own
*"a procedure stops at its enumerated cases."* But dropping it contradicts the
already-being-done membership signal accepted at D9 and for the lock preflight;
the executor reached for this check unprompted.

> Where a relay pins a payload a toolchain could rewrite, the guard checks that
> the tool's mutation surfaces are inert before the operation — in git, hooks, a
> configured `commit.template`, line-ending and filter config; in another
> toolchain, its equivalents. The check is cheap and fails early. **It is not what
> makes the pin sound** — verification after the operation does not depend on
> having enumerated them correctly.

Illustrative not exhaustive; ages gracefully off git; states the n=0 reality by
naming A a convenience rather than a guarantee.

---

## D7 — Trigger surface — SETTLED 2026-08-03

- **D7.a `frontend-code` — substantive.** Topic summary gains **responsive
  layout** and **browser media and device permission**; trigger list gains the
  matching task phrasings plus **media assets**. Without it, *"make this
  responsive"* is a maybe and *"add mic input"* is a miss.
- **D7.b `author-standard` — one phrase.** Add "the exception ladder" to the
  capability list. House vocabulary siblings will cite; unfindable vocabulary is
  how a sixth phrasing gets invented. **No trigger-list change** — you arrive here
  from another skill's citation, not from a prompt.
- **D7.c — three no-changes (ratified together).** `author-execution-relay`
  (additions deepen §Premise and §Pin discipline, both already named; no new
  trigger situation). `app-delivery-pipeline` (a glob correction).
  **`plugin.json`** (no new skills, no rebind, no binding change) — **therefore
  `marketplace.json` stays untouched**, since CLAUDE.md derives it from
  plugin.json's description only when that changes. **Verify in the relay, do not
  assert.**

---

## D8 — Evidence disclosure — SETTLED 2026-08-03

### D8.a — earned tense (ratified)

§Scope of evidence currently reads anticipatorily — *"Expect the proving cascade
to teach this skill things no authority document could."* It did. Rewrite: the
first proving pass **ran**, against one consumer, and returned this amendment
set. **n=1 holds.** The two positives (D2's two-branch rule; G7a's
prototype-drift fence) stay on HEB-94 — a skill that narrates its own wins is
machinery whose subject is the apparatus.

### D8.b — the back-distillation question, resolved in the batch's favour (ratified)

HEB-97 flags G2's catch-scoping clause: *"the one no spec would have produced; it
came from the build."* On its face, the prohibited source.

**It is not.** `author-standard`'s prohibition targets treating code as
*authority* — *"canonizes whatever a model happened to emit"*; its worked call
names *"a conventions doc extracted from one AI-generated service."* Clause (c)
runs the opposite vector: not *"the code does X, therefore X is the standard"*
but *"the code did X, X was a defect, therefore don't do X."* **Learning from a
failure is not back-distillation** — a defect is evidence, never authority.

What is true: clause (c) has **no external authority behind it**, unlike every
other clause in this batch. It carries an **inline evidence note at the clause**,
per the skill's own established form (§The typed-contract seam and §Client
security both do this). No per-clause annotation regime.

### D8.c — G4 deferral line (ratified)

One line at the **end of the new streaming section**, not §Where to look — G4 is
"how streamed events reach React state," and adjacency is where the next author
will be standing. Names the deferral, points at the `useSyncExternalStore` line
in §Components and hooks, states the promotion trigger: **the first real
streaming orchestrator integration.** House pattern, twice precedented
(dependency discipline's watch surface; testing.md's deferred ruling).

---

## D2 — File shape — SETTLED 2026-08-03

### Volume, now knowable

| Landing site | Approx. words |
|---|---|
| Invariants (#4, #5 widened; #11, #12 new) | +115 |
| §Responsive layout (new) | ~400 |
| §Browser media (new) | ~350 |
| §Media assets (new, small) | ~90 |
| §Components and hooks (timeline + `useSyncExternalStore`) | ~165 |
| §The typed-contract seam (ambient declarations) | ~80 |
| §Dependency discipline #4, §Scope of evidence, §Where to look, ladder binding | ~125 |

**≈1,300–1,400 words onto a ~3,500-word body — roughly +40%.** 22.4 KB → ~31 KB.

### D2.a — no split (ratified)

**`author-construct-spec` is 39.7 KB in a single `SKILL.md` with no reference
directory.** The house already ships a bigger single file than this batch
produces; 31 KB is inside precedent.

Substantive test agrees: `reference/testing.md` is separate because *"a
quality-role consumer can load it without the authoring sections"* — **a distinct
actor consumes it.** Neither responsive layout nor browser media has that; both
serve the same actor authoring the same surface.

### D2.b — tighten the split trigger (ratified)

§Where to look states the trigger as a **disjunction** — *"if the testing content
grows to answer its own task-shaped prompt, **or** a distinct quality-role agent
becomes a real consumer."* Read literally the first half fires on nearly every
section: §Accessibility answers *"make this accessible,"* §Client security
answers *"is this XSS-safe,"* §Dependency discipline answers *"can I add this
package."* That would make the skill eight reference files and a stub.

**The role-consumer half is the real criterion; the task-prompt half is
decoration.** Rewrite as a conjunction with the role consumer load-bearing.

### D2.c — one intra-file boundary (ratified)

§Accessibility already owns the AA floor and item 7 already names *"target size
(minimum), focus not obscured, dragging alternatives."* Restating WCAG criteria
in §Responsive layout is pointer-not-mirror violated inside a single file.

**§Accessibility keeps the criteria** — D3.d's 2.5.8 exception set lands at item
7. **§Responsive layout carries the layout obligations and points at
§Accessibility.**

---

# DOCKET CLOSED — 12 items, all settled, 2026-08-03

## Authoring order (dependency-driven)

1. **`author-standard`** exception ladder — *first*; `frontend-code` binds to it
   and uses its tier names at seven sites.
   **`app-delivery-pipeline`** §5 cache fix — trivial, independent, rides along.
2. **`author-execution-relay`** — cleanly partitioned from the frontend set.
3. **`frontend-code/SKILL.md`** — largest; depends on (1).
4. **`frontend-code/reference/testing.md`** — coordinates with HEB-96's timeline
   clause in (3).
5. Integration read + self-application check.
6. Relay to Claude Code: one PR, commits separated by harvest, `plugin.json` →
   2.2.0, **verify `marketplace.json` needs no touch**.
