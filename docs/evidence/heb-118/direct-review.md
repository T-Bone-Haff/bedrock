# HEB-118 direct review

**Profile:** standard, three lenses in one evidence record. Package lifecycle
and release safety are consequential, but HEB-118 performs no infrastructure or
consumer mutation and reserves the release decision to HEB-119.

## Scope and architecture lens

- The delta is limited to package governance, metadata, orientation, evidence,
  validation, tests, and CI integration. No skill body or routing fixture
  changes.
- The manifest remains the sole current-version authority; marketplace,
  changelog, tag, and evidence are checked carriers.
- Portable-core, Claude-adapter, prompt-format, and package identities remain
  separate. Unsupported Codex/OpenAI, Cursor, and SOFIA runner capabilities are
  not claimed.
- The tracked orientation authority is host-neutral. The user-owned untracked
  root `AGENTS.md` remains local, ignored, and untouched.
- `8.1.0` is the correct compatible minor: consumers receive additive
  governance and metadata without a breaking skill, route, host, or safety
  change.

## Correctness and conformance lens

- All 39 package findings appear exactly once: 19 upstream-verified and the
  exact 20-finding HEB-118 residual set implemented here.
- Schemas are Draft 2020-12 valid; vocabulary enums and templates are checked
  for parity; lifecycle rows reject missing owners and invalid retirement.
- Manifest and marketplace repository/license/homepage/keywords are checked;
  marketplace cannot carry a competing version.
- Installed license equality, packaged-governance presence, local links,
  context measurements, authority repetitions, consumer surfaces, and release
  evidence identities are deterministic gates.
- The quickstart covers explicit, implicit, overlap/handoff, unavailable
  capability, and non-trigger behavior. The rebind specimen emits all six
  required outputs without claiming Vue support.

## System and safety lens

One material design defect was found and resolved during review:

- **HEB118-DR-001 — resolved:** the first final-release validator required a
  completed rollout ledger at the immutable tagged commit. Rollout necessarily
  follows tag/release creation, so this made the gate circular or required an
  illegal moved tag. The repaired design keeps candidate validation local and
  accepts operator-supplied release-evidence and rollout exports at final
  closure, verifying both against the unchanged annotated tag.

The repaired release simulation proves that sequence and the negative test
proves early invocation fails closed. The threat model covers malicious skill
content, poisoned references, marketplace/source compromise, external-runner
drift, untrusted CI, sensitive capture, state secrets, browser/token misuse, and
dependency supply chain with residual owners.

## Gate disposition and verdict

- deterministic/package/domain/safety: passed
- Docker/Terraform required integration: passed locally with required flags
- strict host: passed
- isolated install/reload and installed governance: passed
- retained full routing: passed and identity-current; PR routing must still run
- frontend cross-browser/dependency audit: required CI evidence from unchanged
  HEB-114 fixture
- HEB-119 cold acceptance and release: not part of this merge

**Findings:** zero unresolved blocking or material findings.

**Pre-PR verdict:** approve for staging and PR, contingent on all required GitHub
checks. Final merge approval is withheld until those checks are green.
