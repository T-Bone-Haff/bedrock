# Linear adapter extraction

Observed 2026-09-24 (America/New_York; native-shell date).

Tad authorized bringing only the finalized Python Linear adapter into Bedrock
and confirmed `main` as the destination. The originating product is HEX; the
runtime is a normal Python library that accepts a caller-owned Linear token.
The existing distribution/import names (`hex-linear` / `hex_linear`) are kept
so the originating consumer can use this package without a code fork.

## Exact scope

- Nine package files under `packages/hex-linear`: runtime, typed models,
  packaging metadata, usage instructions, tests and schema checker.
- One credential-free CI workflow for package tests, schema validation and
  wheel build/import on Python 3.11 and 3.14.
- A root README pointer and this compact extraction/review evidence.

Runtime, tests, packaging metadata and schema checker come byte-for-byte from
[HEX commit 0b82e1e](https://github.com/Haffey-Enterprises/HEX/tree/0b82e1ebd4d7edb64b5a3096aafb555818566266/packages/hex-linear).
Only the package README is adapted: its example uses caller-supplied issue/team
identifiers and its design link points to the immutable originating record.
No HEX branch history, PostgreSQL/recovery fixtures, native applications,
credential/bootstrap helpers, Keychain policies, or historical incident corpus
is imported. Source lineage and hashes are in [verification.json](verification.json).

The [originating design](https://github.com/Haffey-Enterprises/HEX/blob/0b82e1ebd4d7edb64b5a3096aafb555818566266/docs/ddr/DDR-002-shared-linear-client.md)
and [bounded live evidence](https://github.com/Haffey-Enterprises/HEX/blob/0b82e1ebd4d7edb64b5a3096aafb555818566266/docs/evidence/heb-164/linear-client/final-validation.json)
remain in HEX. Those records include HEX-specific runtime deferrals and access
recovery; copying them wholesale would recreate the excluded scope in Bedrock.
This directory carries no duplicate decision authority over those records.

## Verification and limits

The extracted source passes all 45 package tests on Python 3.14.6/macOS. All ten
GraphQL documents validate against the pinned official schema with a rejected
invalid-query control. A newly built extraction wheel was installed separately;
all 45 originating HEX tests passed against that installed package, with its
import location explicitly checked. This proves package reconsumption without
the HEX source checkout; it does not claim a deployed HEX agent integration.

A separate reviewer read the complete package and checked credential handling,
mutation uncertainty, error parsing and standalone dependencies. The structured
[review record](review.json) preserves checked surfaces and limitations. Its
pre-PR verdict pauses for CI; final gate closure belongs to the exact-head PR
checks and review disposition before merge.

Prior live evidence covers one description update and one additional test issue
with a comment, typed updates and two filtered pages. It remains a bounded
single-workspace observation; no new live API calls occur for this extraction.
No concurrency, assignment-clear or unattended OAuth-renewal proof is claimed.
The owner is Tad Haffey; future API additions or credential-boundary changes
trigger review. Additional consumers are prospective, not empirically proven.

## Delivery boundary

This is a separately installable library addition outside `plugins/bedrock/`.
The skill package, marketplace catalog and project template remain byte-identical
to the PR base. No plugin version bump, marketplace rollout, tag or release is
part of this change. Use a PR merge commit to retain the reviewed source identity.
Install from a pinned Bedrock commit using pip's Git subdirectory support, or
build the wheel from `packages/hex-linear`. The preserved HEX work branch is
historical evidence, not an actively maintained alternate distribution.
