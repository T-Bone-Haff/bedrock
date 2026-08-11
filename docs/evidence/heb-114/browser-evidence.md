# HEB-114 browser evidence

Status: **local automated pass; CI execution pending**.

The declared automated population is the representative fixture flow in
Chromium, Firefox, and WebKit: navigation/focus, 320 CSS-pixel reflow,
container-query declaration behavior, accessibility automation and keyboard
operation, browser-security negatives, and five navigation measurements per
engine.

- Host: macOS 26.5.2 (25F84), Apple silicon; Node 24.15.0; npm 11.12.1.
- Runner: Playwright 1.62.1.
- Engines: Chromium 151.0.7922.34, Firefox 153.0, WebKit 26.5.
- Result: 21/21 passed, zero skipped.
- Candidate inputs: lockfile SHA-256
  `780877f5da24708968edc6a231835b583cfa58bcb9f19edc130cdb521ce9306f`;
  emitted JavaScript SHA-256
  `27e33bd327c2fa29229c6c3894690d012e1e4dbdaf9cea32aceff1794acb40d8`;
  emitted CSS SHA-256
  `5b978c325c8cec8555d5cd4d1a3c579881966ece826c6cdc4626803522fd4756`.

The configured CI population uses Ubuntu and Node 22.12.0 inside HEB-113's
existing deterministic job, followed by the existing live-routing job. It has
not run because no push or pull request is authorized at this stop gate. Local
WebKit is not a claim about installed Safari.
