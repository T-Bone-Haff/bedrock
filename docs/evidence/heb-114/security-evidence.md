# HEB-114 security evidence

Status: **local application-side population passes; delivery evidence remains
outside this claim**.

The declared population is the frontend browser-security coverage map, profile
schema negatives, runtime-envelope and URL validation, no-inline-executable-
script check, no-emitted-source-map fixture check, dependency/lock identity,
and repository secret/hygiene scans. Deployed headers and source-map delivery
remain HEB-113/app-delivery-pipeline evidence.

Results:

- runtime envelopes reject wrong/empty shapes; capability failures remain
  observable; safe navigation rejects non-HTTP(S), malformed, and cross-origin
  input in the fixture;
- built output contains no inline executable script and emits no source maps;
- exact lockfile SHA-256 is
  `780877f5da24708968edc6a231835b583cfa58bcb9f19edc130cdb521ce9306f`;
- runtime-only and full dependency audits report zero known vulnerabilities;
  the initially selected Vite 8.0.0 was replaced by fixed Vite 8.2.1 after a
  high-severity dev-server advisory was detected;
- changed-surface secret/private-path checks found no embedded credentials or
  consumer-private path in retained files.

This does not claim deployed CSP, permissions policy, headers, SRI, source-map
publication policy, hosting isolation, or production verification; those remain
with the HEB-113 delivery seam.
