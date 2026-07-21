# bedrock

**Haffey Enterprises engineering skills** — by T-Bone-Haff (Tad Haffey, Haffey Enterprises LLC).

Self-contained Claude skills distilled from the HE-Bedrock governance corpus. They carry the *content* — the engineering standard, the doctype templates, the testing and review disciplines — with none of the self-governance machinery (no kit-versioning, no ledgers, no audit cadences). No skill depends on another skill being loaded; a skill's own depth lives in its bundled `reference/` and `templates/` files (some skills are a single SKILL.md). Where a skill binds to an external substrate — `design-review-loop` runs on the SOFIA `agent-loop` machinery — the binding is declared in the skill itself, never hidden.

## What's in the kit

The kit spans the authoring-through-review lifecycle on the house stacks — service, infrastructure, agent, frontend, and pipeline work alike. Each capability is a self-contained skill that Claude auto-discovers and triggers by task; the live roster is the plugin's [`skills/`](plugins/bedrock/skills) folder, every skill carries its own description, and the plugin manifest carries the current summary. This README deliberately restates neither.

## Stack binding

Bindings are declared per skill, not kit-wide. The service-side skills assume **Python 3.11+ / FastAPI / async SQLAlchemy / GCP / GitHub**; the frontend skill binds **TypeScript / React / Vite** with plain CSS on design tokens; the pipeline skill binds **GitHub Actions + GCP** on the house branch model; reasoning-protocol skills like `debug` and `author-standard` are stack-agnostic, bound to nothing; and `design-review-loop` binds to a substrate rather than a stack — the SOFIA `agent-loop` runner and the ADR/DDR/SDD doctype family, whose change is its rebind. In every case a materially different choice is a **rebind** — a re-derivation of the equivalents — not a line-edit; each skill's own declaration governs.

## Install — Claude Code

Add the marketplace and install the plugin:

```
/plugin marketplace add T-Bone-Haff/bedrock
/plugin install bedrock@bedrock
```

For local development of the kit itself, point the marketplace at a clone instead: `/plugin marketplace add /path/to/bedrock`. Do **not** copy skill folders out of the repo by hand — a copied skill is an unsynced snapshot with no update path and no staleness signal; it will silently rot the moment the next release lands.

## Install — Claude.ai / Cowork

Install through the plugin marketplace: Settings → Customize → Plugins → Add marketplace from repository (`T-Bone-Haff/bedrock`) → install **bedrock**. The skills load account-wide from the plugin. Do not upload skills as individual ZIPs — hand-uploaded copies are unsynced snapshots that compete with the plugin's skills for routing.

## Staying current

Releases are pushed, not discovered: a bedrock release completes with a push to its enumerated consumer surfaces, recorded on that release's rollout ledger — a per-release ticket in the HE-Bedrock tracker (pattern: "bedrock X.Y.Z cascade — consumer-surface rollout ledger"). The enumeration lives there, not here. Marketplace installs stay current via marketplace refresh + plugin update; live sessions need a restart to load the new version. Any snapshot a consumer keeps anyway — a vendored authority file, a pinned copy — must verify currency at time-of-use against the *current* release, not against whatever baseline it was vendored from.

## Maintenance

Edit the relevant skill's files directly — the SKILL.md and any bundled `reference/` or `templates/` files; single source of truth per skill. There is no corpus to keep in sync. Releases follow the push discipline in the `author-standard` skill.
