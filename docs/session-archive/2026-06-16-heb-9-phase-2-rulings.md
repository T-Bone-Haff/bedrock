# File: docs/ruling-rationale/2026-06-16-heb-9-phase-2-rulings.md
# Author: Claude (claude.ai design-side authoring + three-hat review session 2026-06-16)
# Created: 2026-06-16
# Description: Ruling-rationale ledger for the 2026-06-16 HEB-9 Phase-2 cycle — authoring the
#              author-decision-record skill-deploy apply-prompt (HE-Bedrock) and its three-pass
#              three-hat antagonistic review + sandbox. Captures three ruling-bearing decisions
#              (R029-R031) per DIRECTIVE-031 §31.2, arising during design-side authoring + review.
#              Frozen at commit per §31.7.
# Revised: 2026-06-16 (HEB-9 Phase-2 authoring + review)

# Ruling-Rationale Ledger — HEB-9 Phase-2: author-decision-record skill deploy (HE-Bedrock) — authoring + review

## 0. Header

| Field | Value |
|---|---|
| **Anchor work item** | HEB-9 (Governance Starter Kit; parent HEB-6) — Phase-2 (skill compiler + deploy) |
| **Session** | 2026-06-16 (claude.ai design-side authoring of the deploy apply-prompt + three-hat antagonistic review to convergence; DIRECTIVE-026 — execution pending Claude Code relay) |
| **Author** | Claude (claude.ai authoring + review session 2026-06-16) |
| **main SHA baseline** | `48a119bb12ac37cdfff668ebc1b3038563675a5f` (`main` tip; PR #17 close records; main-only) |
| **Governance baseline** | CSD v3.1.0 · DMS v3.1.0 · ENG-STD-001 v3.3.0 · ENG-STD-002 v2.3.0 · ENG-STD-003 v3.0.1 · kit VERSION 2.3.0 · corpus tag v2.3.0 |
| **Status** | Captured at Phase-2 design+review close; execution (HE-Bedrock deploy) pending. Frozen at commit per DIRECTIVE-031 §31.7. |

*Two-layer ledger (DIRECTIVE-031 §31.2.1): §1 inventory + §2 detail blocks. Ruling IDs R029-R031 continue the global sequence (prior max R028, HEB-9 Phase-1; verified against the live Phase-1 ledger). These rulings supersede the frozen PP-4b both-repos-one-cycle plan (R029) but do not amend the frozen PP-0…PP-4b design ledger (§31.7) — the supersession is recorded on the trail.*

## 1. Rulings Inventory

| ID | Subject | Disposition class |
|---|---|---|
| R029 | Single-repo (HE-Bedrock) rescope — supersedes PP-4b's both-repos-one-cycle plan; forced by a SOFIA-Reboot CI-validator gap | Scope / decision-supersession |
| R030 | Deployed `SKILL.md` is out of DMS §1.2/§1.3 scope (generated artifact + external-tool-convention) — exempt from §2.2 header + §5 filename; codification → Phase-4 DDR | Standards-application |
| R031 | ENG-STD-003 §13.3 trailing-slash `cp` form is preservation-scoped — a deliberate rename uses explicit-filename `cp` | Standards-application / normative interpretation |

## 2. Ruling Detail

### R029 — Single-repo rescope (supersedes PP-4b)

- **Ruling.** HEB-9 Phase 2 deploys to **HE-Bedrock only** this cycle; the SOFIA-Reboot leg is deferred. This is a **new, operator-ratified decision (this session)** that **supersedes PP-4b's** both-repos-one-cycle plan — it does not derive from PP-4/PP-4b and is not attributed to them.
- **Disposition.** Scope / decision-supersession.
- **Rationale.** During execution prep, SOFIA-Reboot's CI gate `validate-docs-structure.sh` was found to `git ls-files '*.md'` (matches every tracked markdown at any depth) and apply a DMS §2.2 `# File:` header check, with an `is_exempt` predicate that does **not** cover `.claude/skills/`. The deployed `SKILL.md` is header-less by design (frontmatter-first is a Claude Code discovery requirement), so it would RED SOFIA-Reboot CI. HE-Bedrock has no `.github/`, no pre-commit hook, and no copy of that validator, so it deploys cleanly. Splitting lands HE-Bedrock now and defers SOFIA-Reboot behind the validator exemption. (Surfaced as Pass-2 N-1; operator chose this split as "Option B".)
- **Alternatives rejected.** (a) Deploy both repos as PP-4b planned — rejected: SOFIA-Reboot CI REDs the header-less `SKILL.md`. (b) Local validator edit inside the deploy PR ("Option C") — rejected: the local-divergence anti-pattern (the verify-repo-state.sh / commit-script workaround class). (c) Master-amend-then-render the validator ("Option A") — deferred, not adopted: heavier (entangles HEB-12 render machinery), and per R-adjacent N-2 the validator is SOFIA-Reboot-native, so the fix is a direct RBT amendment regardless.
- **Primary sources verified.** Live SOFIA-Reboot `scripts/validate-docs-structure.sh` (over-broad `*.md` scan; `is_exempt` lacks `.claude/skills/`); SOFIA-Reboot `.github/workflows/ci.yml` (validate-docs-structure on `pull_request`); HE-Bedrock has no `.github/` and no validator/template (`scripts/` + `scripts/templates/` listed) — this session.
- **Other.**
  - *Supersedes:* PP-4b (both-repos-one-cycle). The frozen PP-0…PP-4b design ledger is not amended (§31.7); this ruling records the supersession on the trail.
  - *Forward:* the SOFIA-Reboot leg → a deferred RBT cycle (validator exemption → deploy → SDD-route dogfood).

### R030 — Deployed SKILL.md is out of DMS scope (§1.3)

- **Ruling.** The deployed `.claude/skills/author-decision-record/SKILL.md` is **out of DMS §1.2/§1.3 scope** on two independent grounds — a **generated artifact** (HEB-9 D6; regen from manifest, never hand-edited) and a **convention-driven external-tool-discovery file** (Claude Code's hard-coded `.claude/skills/` path + `SKILL.md` name + frontmatter-first format). It is therefore **exempt from the §2.2 `# File:` header and the §5 lowercase-slug filename rule** — the same basis that exempts `CLAUDE.md`/`README.md`. This is exemption-by-scope, **not** a MUST-waiver.
- **Disposition.** Standards-application.
- **Rationale.** DMS §1.3 lists "Generated artifacts (build outputs, coverage reports)" and "Convention-driven repo-root files governed by external conventions" as out of scope; §2.2 is explicitly scoped *"per §1.2 scope."* The `SKILL.md` is both generated and external-tool-convention (discovery requires frontmatter as the first bytes, precluding a leading `# File:` block). (Surfaced as Pass-1 M-2; the live consequence — SOFIA-Reboot's validator does not yet *implement* this exemption — is what forced R029.)
- **Alternatives rejected.** (a) Add a `# File:` header to satisfy §2.2 — rejected: breaks Claude Code skill discovery. (b) A `§12`-documented MUST-waiver — rejected: §2.2's "per §1.2 scope" + §1.3 already exempt it; no waiver exists to document. (c) An ADR-against-the-standard — rejected: there is no standard conflict to resolve.
- **Primary sources verified.** Live DMS §1.2 (governed set), §1.3 (generated-artifact + external-tool-convention out-of-scope clauses), §2.2 ("per §1.2 scope"), DMS v3.1.0 — this session.
- **Other.**
  - *Forward:* first-class corpus codification of the `.claude/skills/` compiled-skill convention + this exemption → HEB-9 Phase-4 compilation DDR.

### R031 — §13.3 cp-form is preservation-scoped

- **Ruling.** ENG-STD-003 §13.3's trailing-slash `cp` form binds the **source-name-preservation** case. A deliberate **rename** (staging `author-decision-record-SKILL.md` → deployed `SKILL.md`) correctly uses an **explicit-filename** `cp` target. The §13.3 MUST is not universal.
- **Disposition.** Standards-application / normative interpretation.
- **Rationale.** The deploy renames; the trailing-slash form would preserve the staging name and deploy the wrong filename. The standard's own §6.14 VARIABLE-DECLARATION-VS-USAGE primitive confirms a filename-shape `DEST` used in a filename-form `cp` is the consistent (GREEN) case — i.e., §6.14 contemplates the rename. §2.2's `diff -q` byte-identity independently anchors correctness. (Surfaced as Pass-1 M-5; documented in the apply-prompt `§12 Documented Exceptions` for the audit trail.)
- **Alternatives rejected.** (a) Use the §13.3 trailing-slash form literally — rejected: deploys `author-decision-record-SKILL.md`, not `SKILL.md`. (b) Treat the rename as a `§12`-documented MUST-waiver only — superseded by the preservation-scoped interpretation (the more durable reading), with the `§12` note retained for the audit trail.
- **Primary sources verified.** Live ENG-STD-003 §6.14 (filename-vs-trailing-slash primitive) and §13.3; sandbox §6.14 GREEN (this session + reviewer sandbox).

---

*Forward pointers (carry-forward — not rulings): (1) **§6.8 HEREDOC-ESCAPE-GREP deterministic self-fire** → an ENG-STD-003 §6.8 worked-example refinement (sibling to HEB-35's §6.10 hardening) — the codified §6.8 grep self-fires AMBER when run against an apply-prompt that inlines the §6.8 primitive; the R027 surface-scoping fix (describe-prose rewording + `grep -v` exclusion) is the pattern. (2) **§6.10 min-block-count floor** → HEB-35 (already chartered). (3) **Skill delivery surface** (Claude Code vs claude.ai app) → Phase-4 compilation DDR + HEB-9 ticket (design note filed this session). (4) **Deferred SOFIA-Reboot cycle** → new RBT ticket: validator `.claude/skills/` exemption / over-broad `*.md` scan / possible removal of the doc-structure check from CI → SOFIA-Reboot deploy → SDD-route dogfood.*

*Substrate note: this Phase-2 session was claude.ai design-side (DIRECTIVE-026) — authoring the deploy apply-prompt + a three-pass three-hat antagonistic review with §11.7.4 sandbox runtime to convergence (10 → 5 → 1 → 0 findings). Execution (the HE-Bedrock deploy) is pending operator relay to Claude Code; any execution-surfaced rulings append at execution close. Filesystem MCP was responsive; live authorities (DMS, ENG-STD-003, both repos' git + CI state, GitHub label vocabularies) were fresh-fetched this session.*

*End of HEB-9 Phase-2 ruling-rationale ledger.*
