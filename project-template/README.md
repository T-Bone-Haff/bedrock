# {{PROJECT}}

{{One-line description.}}

## Engineering conventions

This project follows the **bedrock** engineering skills (`application-code`, `testing`, `code-review`, `author-decision-record`, `debug`), which are installed in Claude (account + Claude Code plugin) and trigger automatically. The conventions are not vendored into this repo — they're ambient.

Stack assumption: Python 3.11+ / FastAPI / async SQLAlchemy / GCP / GitHub. A materially different stack is a rebind, captured as an ADR (see `CLAUDE.md`).

## Layout

- `CLAUDE.md` — repo-root orientation (what this project is, its stack, where things live)
- `docs/adr/` — Architecture Decision Records (platform principles)
- `docs/ddr/` — Design Decision Records (specific design rulings)
- `docs/sdd/` — Service Design Documents (per-service designs)
- `docs/reviews/` — review-of-record artifacts

Service code, tests, and scaffolding are generated under the `application-code` and `testing` skills.

## Starting from this template

1. Copy this `project-template/` to a new repo directory and rename it.
2. Fill in `CLAUDE.md` (replace every `{{PLACEHOLDER}}`).
3. Author the defining ADR (`author-decision-record` skill).
4. Scaffold the first service (`application-code` skill).
