# Bedrock repository orientation

This is the tracked, host-neutral repository orientation authority. Host-loaded
files may carry a concise contextual view but must not redefine package version,
skill semantics, release gates, or engineering doctrine.

## Repository identity and layout

`T-Bone-Haff/bedrock` contains the distributable Bedrock Claude plugin and the
consumer project template. It is not the private HE-Bedrock governance corpus.

- `plugins/bedrock/` is the installed package.
- `plugins/bedrock/.claude-plugin/plugin.json#/version` is the sole current
  package-version authority.
- `plugins/bedrock/skills/` contains the thirteen portable skill contracts and
  their bundled profiles, references, schemas, and templates.
- `plugins/bedrock/governance/` contains the installed package lifecycle,
  compatibility, policy, threat-model, quickstart, registry, and evidence
  contracts.
- `.claude-plugin/marketplace.json` registers the package and carries checked
  metadata; it does not carry an independent version.
- `validation/`, `tests/`, and `scripts/` implement the deterministic and
  evaluation gates.
- `docs/evidence/` retains repository-visible evidence. Tracker records are
  operational history, not installed authority.

## Change and release path

Changes use a feature branch and pull request into `main`. Skill-content changes
and their manifest bump land in one transaction. A merged manifest identity is
a release candidate until HEB-119 cold acceptance returns an explicit proceed
decision. Only then may the matching immutable tag, GitHub release, and
consumer-surface rollout occur.

The package's own skill contracts are the engineering standards for work in
this repository. This orientation does not mirror them.

## Host carriers and local context

Tracked `CLAUDE.md` is the Claude Code carrier for this orientation. A root
`AGENTS.md`, when an operator creates one locally for Codex, is ignored local
context: preserve it, but do not stage it or treat it as repository/package
authority. A future tracked adapter carrier must point to this file and pass a
drift check rather than becoming a second hand-maintained orientation.
