# bedrock

**Haffey Enterprises engineering skills** — by T-Bone-Haff (Tad Haffey, Haffey Enterprises LLC).

Five self-contained Claude skills distilled from the HE-Bedrock governance corpus. They carry the *content* — the engineering standard, the doctype templates, the testing and review disciplines — with none of the self-governance machinery (no kit-versioning, no ledgers, no audit cadences). Each skill is independent and free of cross-corpus references; the only dependency a skill has is its own bundled `reference/` and `templates/` files.

## The skills

| Skill | What it does |
|---|---|
| `bedrock:application-code` | Authoring Python service code — FastAPI/async, port/adapter layering, API/config/logging/errors/resilience/security, persistence, scaffolding, and the operational shell scripts that travel with a service. |
| `bedrock:author-decision-record` | Authoring or choosing an ADR / DDR / SDD, with a pre-authoring deliberation gate that keeps rationale from being fabricated. Bundles the three doctype templates. |
| `bedrock:testing` | Test-driven sequence (observe a meaningful red before green), coverage discipline, and the unit/integration/contract/e2e patterns. |
| `bedrock:code-review` | Reviewing a finished diff via the three-hat (LAA/SA/EA) method, with a severity-tagged conformance checklist and a solo-operator self-review discipline. |
| `bedrock:debug` | Structured debugging — reproduce, hypothesize, falsify, fix the root cause. A reasoning protocol, language-agnostic. |

## Stack binding

The conventions assume **Python 3.11+ / FastAPI / async SQLAlchemy / GCP / GitHub**. They're portable across projects *on that stack*; a materially different stack is a **rebind** — a re-derivation of the equivalents — not a line-edit. `debug` is the exception: its discipline is language-agnostic.

## Install — Claude Code

Push this repo to `github.com/T-Bone-Haff/bedrock`, then:

```
/plugin marketplace add T-Bone-Haff/bedrock
/plugin install bedrock@bedrock
/reload-plugins
```

Or, for local use without pushing to GitHub, point the marketplace at the unzipped folder:

```
/plugin marketplace add /path/to/bedrock
/plugin install bedrock@bedrock
```

Or, simplest of all, drop the skill folders straight in:

```
cp -r plugins/bedrock/skills/* ~/.claude/skills/
```

## Install — Claude.ai (web / mobile)

Claude.ai takes skills as individual ZIPs, one per skill (Settings → Capabilities → Skills → upload; code execution must be enabled). Zip each folder under `plugins/bedrock/skills/` so the archive contains the folder with its `SKILL.md`, then upload the five. Once uploaded on the web, they're enabled account-wide and available in the iOS app's chats.

## Maintenance

Edit the relevant skill's `reference/` or `templates/` file directly — single source of truth per skill. There is no corpus to keep in sync.
