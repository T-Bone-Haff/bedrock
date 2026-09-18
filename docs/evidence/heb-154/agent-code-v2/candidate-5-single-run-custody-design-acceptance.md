# Candidate-5 single-run custody — design acceptance record

| Field | Value |
|---|---|
| Record ID | `C5-MIN-CUSTODY-ACCEPTANCE-1` |
| Status | RATIFIED |
| Decision date | 2026-09-17 America/New_York |
| Operator | Tad Haffey |
| Lifecycle transition | `PROPOSED` → `ACCEPTED-DESIGN` |

## Decision

Tad Haffey stated: “Ratify the design. Let's properly name and capture that file as the approved construct spec, committed and pushed in the bedrock repo.”

That decision accepts the design embodied by `candidate-5-minimal-custody-construct-spec.md` revision 4, SHA-256 `464b52c4f05959796b2e2819430f88c52dbd9055d3210f167f8693ccf24efeca`, frozen in Git commit `d94641b5186359560715955a978046cf0bce18fd`.

The accepted lifecycle artifact is `candidate-5-single-run-custody-construct-spec.md` revision 5, SHA-256 `e4e5a6266c63e0077c19df357fed2ce4d96aa2b008e38c5a618ae610d614d829`.

## Acceptance basis

- Host closure-audit result SHA-256: `db18ec6b25dcc2bbfd45073978f4474fca78d51dd3c4558850882945e9a2e0c5`.
- Host closure-audit report SHA-256: `5f58e62bf9313fd04d9ccb416e7329153928872e7cf811952c150b7208755477`.
- Audit outcome: both exact retained findings closed at the design-text layer; all ten frozen requirement checks satisfied.
- Promotion diff: title, lifecycle, provenance, authority-history clarification, evidence-location inventory and change-log metadata only. Operative decisions, amendments, correctness invariants, risks, failure behavior and obligations are unchanged.

## Scope and exclusions

This decision accepts the design only. It does not establish implementation, verification or graduation and does not authorize provider access, credentials, spending, calibration execution, launch, permanent final freeze or evidence deletion.

## Evidence preservation and rollback

The exact reviewed revision-4 source remains at its original path and in the frozen Git commit above. The accepted artifact is an additive lifecycle promotion, not a destructive move. If the promotion metadata is found defective, withdraw revision 5 and return to the immutable revision-4 source; do not rewrite the reviewed bytes or their audit evidence.
