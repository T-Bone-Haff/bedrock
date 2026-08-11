# Haffey React, TypeScript, Vite, and plain-CSS profile

This profile binds the portable frontend core to React 19.2, TypeScript 6.0,
Vite 8, plain CSS, npm lockfiles, Vitest/Testing Library, and Playwright. Point
versions are currency: verify them at adoption and retain the lockfile and
evidence identity used by the consumer.

## Required posture

- React function components and hooks; render remains pure and Strict Mode is
  enabled in development. Effects synchronize owned external systems.
- TypeScript uses `strict`, `noUnusedLocals`, `noUnusedParameters`,
  `noFallthroughCasesInSwitch`, and normally `noUncheckedIndexedAccess` for a
  new repository. Escape hatches carry a site rationale.
- Vite's type transform is not a type check. Run `tsc --noEmit` separately and
  require a production `vite build`.
- Runtime configuration has one typed module. Every `VITE_` value is public.
- `package-lock.json` is committed and clean installs use `npm ci`. Declare a
  Node engine compatible with the selected Vite release.
- Plain CSS is the default styling profile. Reusable design decisions use the
  repository's token authority; intrinsic, content-derived, algorithmic, and
  component-private geometry may remain local with a clear name or rationale.
- Media assets enter through a typed manifest when application code owns their
  identity. Stable public URLs are declared exceptions with cache ownership
  handed to delivery.

## Component-system decision

The Haffey default is bespoke components over repository design tokens. A
consumer may select an accessible component library without rebinding the
portable core after evaluating semantic output, keyboard/focus behavior,
supported browsers, styling/theming authority, bundle and runtime cost,
maintenance, licensing, and escape/migration cost. Architecture-shaping
adoption is recorded through the consumer's decision process.

Brand or prototype guidance from `haffey-design` is optional process input. It
is never a runtime or installed-skill dependency; production token values live
in the consumer repository's declared design authority.

## Browser profile

Current Vite 8 documentation defines its default production target as Baseline
Widely Available for the major: Chrome/Edge 111, Firefox 114, Safari/iOS 16.4. A consumer declares
its own support matrix and polyfill/legacy policy rather than inheriting these
numbers silently. Development support and production output support are not the
same claim.

## Gates

The profile supplies commands for dependency integrity/audit, typecheck, lint,
unit/component/contract tests, declared coverage, production build, bundle
budgets, and applicable Playwright engines. `frontend-code` owns what these
gates prove; `app-delivery-pipeline` owns where and how they run and the build,
artifact, hosting, header, source-map, promotion, and rollout lifecycle.
