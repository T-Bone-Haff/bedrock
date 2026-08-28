# HEB-128 portable-core 2.0 candidate conformance evidence

**Captured:** 2026-08-27 ET
**Baseline source:** `165663364eddbeeedb11e6a09627612f4cf399fd`
**Candidate state:** aggregate uncommitted worktree; manifest-derived candidate `9.0.0`

## Authority and identity

The accepted ADR-001 2.0.0 record and its three architecture carriers were read
whole before implementation. The candidate registry now derives and validates
the portable-core identity against that accepted authority.

- portable core: `2.0.0`;
- design-review-loop actor contract: `2.0.0`;
- Claude adapter: unchanged at `1.1.0`;
- package: major-class aggregate delta; the ratified candidate gate derived
  `9.0.0` from the then-live `8.4.0` manifest.

## Migration disposition

The product-specific bundled runner reference is replaced by
`plugins/bedrock/skills/design-review-loop/reference/product-runner-binding.md`.
Direct and multi-perspective review remain supported without a runner. A
runner-backed claim now requires a declared product workflow binding, runner
identity and immutable SemVer, compatible schemas, exact invocation, and fresh
gate evidence. No existing product implementation is promoted, supported, or
mapped automatically.

The empirical compatibility floor is zero supported external runner bindings.
Runner-backed compatibility therefore remains unavailable; it is not inferred
from prior art or from the generic binding contract.

## Deterministic and integration evidence

| Gate | Result | Evidence |
|---|---|---|
| Meaningful-red controls | PASS | Legacy product assignment/path, runner-profile disposition, portable-core drift, ADR provenance drift, and compatibility drift controls failed before implementation. |
| Agent/review contracts | PASS | `python scripts/validate_agent_review_contracts.py`; 8 focused tests. |
| Package governance | PASS | `python scripts/validate_package_governance.py`; 29 focused tests. |
| Safety | PASS | `python scripts/validate_safety.py`. |
| Complete unit suite | PASS | 138 tests passed; one unchanged Docker-dependent test skipped because the daemon was unavailable. |
| Main plugin validator | PASS | 13/13 deterministic skill validation plus strict plugin-manifest host validation. |
| Rule-trigger audit | PASS | Complete 55-carrier audit; 1,026 deterministic semantic units; zero internal-state findings. |
| Context budget | PASS | 10,558 skill-entrypoint words; design-review-loop 886 words, below the 1,200-word package limit. |
| Isolated install/reload | PASS | 13 skills, identity carriers, and packaged governance discovered. |
| Final standard-profile review | PASS | Zero unresolved findings after the `9.0.0` manifest, changelog, and generated-carrier transaction. |
| Diff hygiene | PASS | `git diff --check`. |

## Nondeterministic routing evidence

The authorized full release-profile run produced retained aggregate-candidate
evidence at `docs/evidence/heb-109/routing-results.json`:

- 54 planned and completed cases, each run three times;
- 162/162 passed, with every case at a 1.0 pass rate;
- overall, every-case, excluded-selection, and budget gates all passed;
- zero excluded selections and no budget exhaustion;
- resolved model `claude-haiku-4-5-20251001`;
- total observed cost `$1.598123` within the authorized `$6.48` ceiling;
- generated timestamp `2026-08-27T22:29:25.834146-04:00` in the project clock;
- report schema 2, complete suite, and retained-evidence eligibility confirmed.

The report was parsed mechanically in full after completion; no result sampling
or bounded search was used.

Two earlier release-profile attempts produced no routing observation and cost
`$0.00`:

1. the isolated adapter rejected missing API-key authentication before a model
   call;
2. with the approved local key environment present inside the filesystem
   sandbox, the first case failed at the transport boundary before a model
   response.

Those attempts remain diagnostic history only. After explicit operator
authorization, the complete unsandboxed three-draw run above supplied the
missing observations and passed the routing gate.

## Gates still open

- operator candidate ratification, merge, and independent cold acceptance;
- tag, release, and consumer rollout only after their separate authorization.
