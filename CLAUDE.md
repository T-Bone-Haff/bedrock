# CLAUDE.md — bedrock

Repo-root orientation carrier for Claude (auto-loaded by Claude Code). The
tracked, host-neutral authority is [`docs/repository-orientation.md`](docs/repository-orientation.md).
This file is **context, not conventions** and does not mirror the engineering
standards in `plugins/bedrock/skills/`.

## What this is

**bedrock** is the home of the Haffey Enterprises engineering-skills plugin —
self-contained Claude skills distilled from the HE-Bedrock governance corpus —
plus the project template new consumer repos copy. The plugin manifest
(`plugins/bedrock/.claude-plugin/plugin.json`) is the sole version authority;
no other surface states a version number.

## Where things live

- `plugins/bedrock/` — the plugin: `.claude-plugin/plugin.json` (manifest) +
  `skills/` (the skill corpus; each skill self-contained)
- `.claude-plugin/marketplace.json` — the marketplace manifest; its plugin
  description is derived verbatim from plugin.json's whenever that changes
- `project-template/` — the template consumer repos copy. Its `CLAUDE.md` is a
  `{{PROJECT}}` placeholder for *consumer* repos — it is **not** this repo's
  orientation; this file is
- `docs/session-archive/` — historical session records; read-only context,
  never authority
- `README.md` — the install, staying-current, and maintenance surface
- `plugins/bedrock/governance/` — installed lifecycle, compatibility, policy,
  threat-model, quickstart, rebind, registry, and release-evidence contracts
- root `AGENTS.md`, when present, is ignored local Codex context. It is not a
  tracked package or repository authority and must not be staged implicitly

## Branch model and commit authority

`feature/*` → `main`, via PRs; never commit directly to `main`. Git
transactions are executed by Claude Code via gated relay under the operator's
per-gate ratification; the operating doctrine lives at
`~/Documents/GitHub/vault/CLAUDE.md` — re-read it from disk at execution time,
never from a relay's summary of it. Plugin versions are derived from disk at
landing, never pre-claimed.

## Project-specific rules

- Releases follow the push discipline in the `author-standard` skill; each
  release's consumer-surface enumeration lives on its rollout ledger (a
  per-release ticket in the HE-Bedrock tracker) and conforms to the installed
  rollout-ledger schema. Tracker state is operational evidence, not installed
  contract authority.
- A skill-content change lands with the plugin.json version bump in the same
  transaction.
- A manifest version on `main` remains a candidate until HEB-119 cold acceptance
  returns an explicit proceed decision. Only then may the matching immutable tag
  and GitHub release be created.
