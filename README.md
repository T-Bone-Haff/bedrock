# bedrock

**Haffey Enterprises engineering skills** — by T-Bone-Haff (Tad Haffey, Haffey Enterprises LLC).

Seven self-contained Claude skills distilled from the HE-Bedrock governance corpus. They carry the *content* — the engineering standard, the doctype templates, the testing and review disciplines — with none of the self-governance machinery (no kit-versioning, no ledgers, no audit cadences). Each skill is independent and free of cross-corpus references; the only dependency a skill has is its own bundled `reference/` and `templates/` files.

## The skills

| Skill | What it does |
|---|---|
| `bedrock:application-code` | Authoring Python service code — FastAPI/async, port/adapter layering, API/config/logging/errors/resilience/security, persistence, scaffolding, and the operational shell scripts that travel with a service. |
| `bedrock:author-decision-record` | Authoring or choosing an ADR / DDR / SDD, with a pre-authoring deliberation gate that keeps rationale from being fabricated. Bundles the three doctype templates. |
| `bedrock:testing` | Test-driven sequence (observe a meaningful red before green), coverage discipline, and the unit/integration/contract/e2e patterns. |
| `bedrock:code-review` | Reviewing a finished diff via the three-hat (LAA/SA/EA) method, with a severity-tagged conformance checklist and a solo-operator self-review discipline. |
| `bedrock:debug` | Structured debugging — reproduce, hypothesize, falsify, fix the root cause. A reasoning protocol, language-agnostic. |
| `bedrock:infrastructure-code` | Authoring infrastructure-as-code — Terraform/GCP conventions, remote state, environments, Kubernetes and stateful workloads, and the infra delivery pipeline. |
| `bedrock:author-standard` | Authoring a reusable standard — a skill, convention set, or template: sourcing (forward-author, never back-distill), the skill-membership test, binding declaration, hardening rules, and proving via cascade onto a real consumer. Single-file reasoning protocol, stack-agnostic. |

## Stack binding

The conventions assume **Python 3.11+ / FastAPI / async SQLAlchemy / GCP / GitHub**. They're portable across projects *on that stack*; a materially different stack is a **rebind** — a re-derivation of the equivalents — not a line-edit. `debug` and `author-standard` are the exceptions: their disciplines are stack-agnostic.

## Install — Claude Code

Add the marketplace and install the plugin:

```
/plugin marketplace add T-Bone-Haff/bedrock
/plugin install bedrock@bedrock
/reload-plugins
```

For local development of the kit itself, point the marketplace at a clone instead: `/plugin marketplace add /path/to/bedrock`. Do **not** copy skill folders out of the repo by hand — a copied skill is an unsynced snapshot with no update path and no staleness signal; it will silently rot the moment the next release lands.

## Install — Claude.ai / Cowork

Install through the plugin marketplace: Settings → Customize → Plugins → Add marketplace from repository (`T-Bone-Haff/bedrock`) → install **bedrock**. The seven skills load account-wide from the plugin. Do not upload skills as individual ZIPs — hand-uploaded copies are unsynced snapshots that compete with the plugin's skills for routing.

## Staying current

Releases are pushed, not discovered: a bedrock release completes with a push to its enumerated consumer surfaces, recorded on that release's rollout ledger — a per-release ticket in the HE-Bedrock tracker (pattern: "bedrock X.Y.Z cascade — consumer-surface rollout ledger"). The enumeration lives there, not here. Marketplace installs stay current via marketplace refresh + plugin update; live sessions need a restart to load the new version. Any snapshot a consumer keeps anyway — a vendored authority file, a pinned copy — must verify currency at time-of-use against the *current* release, not against whatever baseline it was vendored from.

## Maintenance

Edit the relevant skill's `reference/` or `templates/` file directly — single source of truth per skill. There is no corpus to keep in sync. Releases follow the push discipline in the `author-standard` skill.
