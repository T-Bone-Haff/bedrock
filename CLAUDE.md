# CLAUDE.md — bedrock

Repo-root orientation for Claude (auto-loaded by Claude Code). This file is
**context, not conventions** — what this repo is, its layout, and how changes
land. The engineering conventions are this repo's *product*: they live in the
plugin's skills (`plugins/bedrock/skills/`), which trigger on their own; this
file does not mirror them. Keep this file lean; prune as it grows.

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
  per-release ticket in the HE-Bedrock tracker), not in this repo.
- A skill-content change lands with the plugin.json version bump in the same
  transaction.
