# Reference: Static Frontend Leg

The pipeline for a Vite/TypeScript SPA: verify gates → build → hosted deploy with previews. The spine (`01`) governs throughout. The gates themselves are owned by `frontend-code` — its gate quartet names what must pass; **this leg is the pipeline home it points to.**

## Contents

- [1. The gate sequence](#1-the-gate-sequence)
- [2. Build](#2-build)
- [3. Hosting posture: Firebase Hosting, keyless](#3-hosting-posture-firebase-hosting-keyless)
- [4. Preview channels](#4-preview-channels)
- [5. Cache headers](#5-cache-headers)
- [6. The CSP header and its companions](#6-the-csp-header-and-its-companions)
- [7. Channel mapping and releases](#7-channel-mapping-and-releases)

---

## 1. The gate sequence

The verify job runs `frontend-code`'s **gate quartet**, in ascending order of cost:

1. **Lint** — `npm run lint`.
2. **Type-check** — `tsc -b` (standing alone or as the first half of `npm run build`; either way its failure is legible as a *type* failure).
3. **Test + coverage floor** — vitest with the coverage gate as `frontend-code`'s testing reference configures it. The pipeline runs the floor; it does not own the number.
4. **Build** — `vite build` must succeed on every PR; a merge that can't produce a deployable bundle is already broken.

Installs are `npm ci` from the lockfile — never `npm install` in CI. Node version is pinned in the workflow and matches the repo's declared engine.

## 2. Build

- The artifact is the **`dist/` bundle** — this leg's analogue of the service leg's image. It is built once per deploying run and the same bundle is what deploys; a deploy step that rebuilds is the retag-not-rebuild rule (`02` §3) violated in local form.
- **The bundle is public by construction** (`frontend-code` §security): `VITE_`-prefixed variables only, no secrets, ever. The pipeline adds the enforcement seam: deploy jobs get no secret whose exposure in a bundle would matter — there is nothing to leak into an artifact that is, by design, world-readable.
- Environment-specific configuration (API base URLs and the like) enters via build-time `VITE_` variables scoped to the GitHub Environment (spine §6), not via post-build file rewriting.

## 3. Hosting posture: Firebase Hosting, keyless

**Firebase Hosting is the house static host** — preview channels, declarative headers, SPA rewrites, CDN, no infrastructure to provision. Two disciplines attach:

- **`firebase.json` in the repo is the hosting configuration source of truth** — rewrites (§5), headers (§5–6), site targets. Console-side configuration edits are the hosting analogue of `kubectl set image` drift (`02` §5): reconcile through the repo.
- **Auth is WIF ADC — the same `google-github-actions/auth` step as everywhere else — driving the firebase CLI** (`firebase deploy --only hosting`, `firebase hosting:channel:deploy`). **The official Firebase GitHub integration (`firebase init hosting:github` / `action-hosting-deploy`) is the named anti-pattern:** it provisions a service-account JSON key into a GitHub secret — exactly the long-lived credential spine §2 prohibits. Do not follow the Firebase docs' default path here.

*Empirical floor, stated honestly: firebase-tools' external-account (WIF) credential support is documented in current versions but unproven by any house deploy. Verify at the first adoption. If it fails, that is a surfaced design ruling (GCS-static is the likely fallback) — never a silently minted key.*

## 4. Preview channels

- **Every PR gets a preview channel:** `firebase hosting:channel:deploy pr-<number> --expires 7d`, deployed after the verify gates pass, with the preview URL posted to the PR. The preview is the review surface for visual and UX changes — `frontend-code`'s experience-first path, extended to reviewers.
- **Channels expire; expiry is the cleanup mechanism.** No standing garbage-collection job until scale demands one.
- **Fork PRs get no preview deploy.** Deploy jobs need WIF, and WIF trust is scoped to the repo — a fork PR runs verify only. (House repos are private; this is a stated boundary, not a live concern.)

## 5. Cache headers

Homed here, set declaratively in `firebase.json` `headers`:

- **Hashed assets** (`/assets/**` — everything Vite emits with a content hash): `Cache-Control: public, max-age=31536000, immutable`. The hash in the filename is the cache key; the header makes the CDN and browser honor it.
- **`index.html` and anything served un-hashed**: `Cache-Control: no-cache` — revalidate every time. The entry document is the pointer into the hashed graph; caching the pointer is how users get a stale app with fresh assets, the classic SPA cache failure.
- **SPA rewrite:** all routes → `/index.html`, so deep links survive refresh. Root-absolute asset paths (the HEX convention) compose with this; the rewrite must not shadow `/assets/**`.

## 6. The CSP header and its companions

`frontend-code` authors the app **strict-CSP-ready** and declares the header delivery's. **It lands here**, in `firebase.json` `headers`, on `index.html`:

- **Baseline posture:** `default-src 'self'`; scripts and styles from self with **no `unsafe-inline` for scripts**, connect-src widened only to the app's named API origins. The app being CSP-ready by construction is what makes this deployable without app changes — that was the point of the seam.
- **The policy is repo-owned and app-specific** — this skill mandates its presence and its no-inline-scripts floor; the exact directive set tightens with the app and lives with the app.
- **Companion headers**, same mechanism, same floor: `X-Content-Type-Options: nosniff`, `frame-ancestors 'none'` (via CSP) unless the app is designed to be embedded, `Referrer-Policy: strict-origin-when-cross-origin`.

## 7. Channel mapping and releases

- **`main` deploys the live channel; `develop` deploys a persistent named preview channel** (`develop`, long expiry, redeployed on every push). Two branches, two standing surfaces, one live.
- **Release automation is the spine's (§5), unchanged** — the semver label gate applies to frontend PRs identically, and the tag names the deployed bundle's version. No image, so no retagging step: the release tag simply records which commit the live channel serves.
