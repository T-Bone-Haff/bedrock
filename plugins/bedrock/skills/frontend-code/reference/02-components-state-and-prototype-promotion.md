# Components, state, resources, and prototype promotion

## Component and data direction

Components translate typed state into semantics. Hooks coordinate behavior.
Framework-free policy and transformation logic stays outside React. Surfaces
consume narrow seam interfaces through providers or explicit props and never
construct concrete API clients or vendor SDKs.

Colocate state at the lowest shared owner, compute derived values, and use a
reducer/state machine when transition identity matters. Shared context or a
state library must name the state lifetime, ownership, update frequency,
selector behavior, server-rendering needs, debugging/telemetry needs, and why
props or a seam provider are insufficient.

## Subscription selection

- Use `useSyncExternalStore` for a true external store with stable subscribe
  and cached snapshot semantics, including server snapshot behavior when SSR
  applies.
- Use an owned effect subscription for DOM events, media/observer lifecycles,
  and imperative libraries when the source has no meaningful store snapshot.
- In either form, prevent stale callbacks, duplicate subscription, missed
  cleanup, and updates after ownership ends. Test replacement and unmount.

Timers, workers, streams, connections, animation frames, observers, and media
resources expose cancellation/cleanup. Cancellation settles pending work. A
sequence or session declares whether replacement cancels, queues, joins, or
coexists with prior work.

## Prototype safety floor

Prototype speed may relax production layering, coverage, abstraction, and
polish. It may not relax:

- no real secrets or unjustified personal/production data;
- explicit disposal, retention, audience, and promotion status;
- dependency/license/cost review proportionate to exposure;
- a usable keyboard/visible alternative for every critical path;
- no deceptive success state for an unavailable capability;
- no hidden production integration or ambient write authority.

## Promotion assessment

Promotion assesses provenance, dependency and license state, data handling,
architecture, behavior tests, accessibility, security, browser support,
performance, maintenance, disposal debt, and known limitations. Outcomes are:

- **graduate:** evidence shows the code already satisfies the production profile;
- **targeted hardening:** repair named gaps while preserving conformant code;
- **re-author:** provenance or structure prevents trustworthy targeted repair;
- **dispose:** risk or value does not justify production adoption.

The assessment is retained; blanket re-authoring and lint-only canonization are
both rejected.
