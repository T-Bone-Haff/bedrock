# bedrock

**Haffey Enterprises engineering skills** — by T-Bone-Haff (Tad Haffey, Haffey Enterprises LLC).

Self-contained Claude skills distilled from the HE-Bedrock governance corpus. They carry the *content* — the engineering standard, the doctype templates, the testing and review disciplines — with none of the private self-governance machinery. No skill depends on another skill being loaded; a skill's own depth lives in its bundled `reference/` and `templates/` files (some skills are a single SKILL.md). Portable actor contracts name optional host profiles without embedding a private runner, tracker, path, or authority corpus.

## What's in the kit

The kit spans the authoring-through-review lifecycle on the house stacks — service, infrastructure, agent, frontend, and pipeline work alike. Each capability is a self-contained skill that Claude auto-discovers and triggers by task; the live roster is the plugin's [`skills/`](plugins/bedrock/skills) folder, every skill carries its own description, and the plugin manifest carries the current summary. This README deliberately restates neither.

## Stack binding

Bindings are declared per skill, not kit-wide. The service-side skills assume **Python 3.11+ / FastAPI / async SQLAlchemy / GCP / GitHub**; the frontend skill binds **TypeScript / React / Vite** with plain CSS on design tokens; the pipeline skill binds **GitHub Actions + GCP** on the house branch model; reasoning-protocol skills like `debug` and `author-standard` are stack-agnostic. `agent-code` and `design-review-loop` expose provider/runner-neutral cores plus explicit optional profiles. A profile binds the portable contract without becoming its authority.

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

### Validation

Install the pinned validation dependency, then run the deterministic and host checks:

```sh
python3 -m pip install -r validation/requirements.txt
python3 -m unittest discover -s tests -v
python3 scripts/validate_plugin.py
bash scripts/smoke_clean_install.sh
```

`validate_plugin.py` enforces the 13-skill inventory, strict YAML frontmatter, the 1,024-character description limit, explicit positive and negative routing boundaries, unique names, plugin/marketplace coherence, relative-link and private-path safety, declared external-root dependencies and snapshot currency markers, complete code-sample accounting, evidence-manifest integrity, routing-fixture coverage, and `claude plugin validate --strict`.

Shared routing prompts live in `tests/fixtures/routing.yaml` and are surface-neutral. They cover direct, implicit, adversarial, negative, and overlap decisions. The Claude Code adapter presents the exact validated name/description catalog to each isolated model session, so the regression measures the metadata routing contract rather than unaided name association, and retains machine-readable results:

```sh
python3 scripts/run_routing_evals.py \
  --profile release \
  --output docs/evidence/heb-109/routing-results.json
```

The live adapter requires Claude authentication and incurs model usage. Pull requests use the preregistered `pr` profile: every case runs once and every draw must pass. Authenticated retained evidence uses the `release` profile: three independent draws per case, at least a 95% aggregate pass rate, at least two of three passing draws for every case, and zero excluded-route selections. The machine-readable report records fixture, catalog, and policy SHA-256 digests; results with different identities are not pooled. Each model call is capped at $0.03 and 120 seconds. Deterministic validation and the isolated install/reload smoke test do not require model inference. Branch protection must require `Plugin validation / live-routing`.

Using `--case` creates an explicitly targeted report. It can prove that selected cases passed, but the report is marked ineligible as retained full-suite release evidence.

`validation/executable-samples.yaml` accounts for every language-tagged skill example. `fixture-backed` entries name executable evidence; `illustrative` and `deferred` entries name the correction ticket that owns stronger proof. `docs/evidence/heb-109/manifest.yaml` ties validation claims to reproducible commands, retained evidence, and explicit deferrals.
