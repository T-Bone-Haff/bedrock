# bedrock

**Haffey Enterprises engineering skills** — by T-Bone-Haff (Tad Haffey, Haffey Enterprises LLC).

Self-contained Claude skills distilled from the HE-Bedrock governance corpus. They carry the *content* — the engineering standard, the doctype templates, the testing and review disciplines — with none of the self-governance machinery (no kit-versioning, no ledgers, no audit cadences). Each skill is independent and free of cross-corpus references; the only dependency a skill has is its own bundled `reference/` and `templates/` files.

## What's in the kit

The kit spans the authoring-through-review lifecycle for services on the house stack — writing application and infrastructure code, testing, reviewing diffs, structured debugging, authoring decision records and reusable standards, and driving design-record sets to convergence. Each capability is a self-contained skill that Claude auto-discovers and triggers by task; the live roster is the plugin's [`skills/`](plugins/bedrock/skills) folder, and every skill carries its own description.

## Stack binding

The conventions assume **Python 3.11+ / FastAPI / async SQLAlchemy / GCP / GitHub**. They're portable across projects *on that stack*; a materially different stack is a **rebind** — a re-derivation of the equivalents — not a line-edit. Three skills sit outside that default: `debug` and `author-standard` are stack-agnostic reasoning protocols, bound to nothing. `design-review-loop` is bound, but not to the stack — its binding is the SOFIA `agent-loop` runner and the ADR/DDR/SDD doctype family, and a different runner or doctype family is its rebind. Every other skill is bound to the stack above.

## Install — Claude Code

Add the marketplace and install the plugin:

```
/plugin marketplace add T-Bone-Haff/bedrock
/plugin install bedrock@bedrock
/reload-plugins
```

For local development of the kit itself, point the marketplace at a clone instead: `/plugin marketplace add /path/to/bedrock`. Do **not** copy skill folders out of the repo by hand — a copied skill is an unsynced snapshot with no update path and no staleness signal; it will silently rot the moment the next release lands.

## Install — Claude.ai / Cowork

Install through the plugin marketplace: Settings → Customize → Plugins → Add marketplace from repository (`T-Bone-Haff/bedrock`) → install **bedrock**. The skills load account-wide from the plugin. Do not upload skills as individual ZIPs — hand-uploaded copies are unsynced snapshots that compete with the plugin's skills for routing.

## Staying current

Releases are pushed, not discovered: a bedrock release completes with a push to its enumerated consumer surfaces, recorded on that release's rollout ledger — a per-release ticket in the HE-Bedrock tracker (pattern: "bedrock X.Y.Z cascade — consumer-surface rollout ledger"). The enumeration lives there, not here. Marketplace installs stay current via marketplace refresh + plugin update; live sessions need a restart to load the new version. Any snapshot a consumer keeps anyway — a vendored authority file, a pinned copy — must verify currency at time-of-use against the *current* release, not against whatever baseline it was vendored from.

## Maintenance

Edit the relevant skill's `reference/` or `templates/` file directly — single source of truth per skill. There is no corpus to keep in sync. Releases follow the push discipline in the `author-standard` skill.
