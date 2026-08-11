# HEB-114 performance evidence

Status: **local fixture budgets pass**.

Predeclared fixture budgets:

- five initial-navigation repetitions per browser engine, each at or below 1500 ms;
- total compressed emitted JavaScript and CSS at or below 120000 bytes.

The results characterize this fixture and environment only. They are not a
universal product-performance claim.

Final measurements on macOS 26.5.2, Node 24.15.0, Playwright 1.62.1:

| Engine | Navigation-to-ready milliseconds (5 repetitions) |
|---|---|
| Chromium 151.0.7922.34 | 39.840, 23.871, 20.601, 21.119, 19.190 |
| Firefox 153.0 | 44.769, 31.878, 30.366, 29.046, 29.605 |
| WebKit 26.5 | 49.118, 26.764, 34.183, 25.878, 33.842 |

All 15 measurements are below 1500 ms. Emitted gzip size is 60,556 bytes
(60,071 JavaScript + 485 CSS), below 120,000 bytes. Browser-launch time,
network latency beyond loopback, production hosting, low-end devices, memory,
and long-session resource behavior were not measured.
