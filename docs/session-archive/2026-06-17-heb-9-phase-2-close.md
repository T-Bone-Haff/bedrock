# File: docs/session-handoffs/2026-06-17-heb-9-phase-2-close.md
# Author: Claude (claude.ai oversight + close session 2026-06-17)
# Created: 2026-06-17
# Description: Close-grade session-handoff for the HEB-9 Phase-2 HE-Bedrock leg — deploy of the
#              author-decision-record skill into .claude/skills/ (PR #18, main @ 5c6bf130) + the
#              Phase-2 close-records vendoring (PR #19, main @ 51620434), executed via Claude Code
#              apply-prompt under claude.ai design-side oversight and closed post-merge. D9 discovery
#              confirmed live. Bridges to the now-unblocked HEB-9 SOFIA-Reboot leg (RBT-35 Done).
# Revised: 2026-06-17 (HEB-9 Phase-2 execution + close)

---
session_date: 2026-06-17
main_sha_baseline: 5c6bf130
session_close_status: COMPLETE (HE-Bedrock leg)
next_session_scope: HEB-9 SOFIA-Reboot leg — now unblocked by RBT-35 (Done). Re-deploy the byte-identical author-decision-record SKILL.md into SOFIA-Reboot's .claude/skills/ (develop-based; CI now scopes to the DMS governed set, so the header-less skill is outside collection and passes), then Phase-3 SDD-route dogfood (author one SOFIA SDD with the skill live; measure fire + friction — D8 acceptance).
---

# Session-Handoff — HEB-9 Phase-2: author-decision-record skill deploy into HE-Bedrock (execution + close)

*Close-grade (DMS §2.3.2.2). `main_sha_baseline` = the deploy work-PR merge (PR #18) per the Phase-1 convention; HE-Bedrock is main-only (DMS §2.3.4.1 integration-branch rebind). main subsequently advanced to `51620434` via the close-records PR #19 — a continuation session branches from `51620434`. This session was claude.ai design-side oversight (DIRECTIVE-026) of two Claude Code execution runs, plus the post-merge operator close.*

## 1. Session Summary

HEB-9 Phase-2 deployed the first compiled authoring skill into HE-Bedrock and vendored the close records. Single-repo rescope (R029) — HE-Bedrock only this leg.

1. **Deploy (PR #18, squash → `main` @ `5c6bf130`).** One file: `.claude/skills/author-decision-record/SKILL.md` (+56), sha256 `b1bd05a8…`, **frontmatter-first** (no `# File:` header — R030 external-tool-convention exemption). `.claude/` did not previously exist, so this **bootstrapped skill discovery** — `author-decision-record` is the first skill in HE-Bedrock. The apply-prompt (the compiler, D7) ran under bash with **zero REDs / zero unexpected AMBERs** across the pause-points; the §6.8 deterministic-self-fire fix (R027 surface-scoping) held GREEN.
2. **D9 discovery — confirmed live.** The skill lists by name + description and in the `/` menu, and **auto-fires** on a natural-language trigger, routing correctly via the DMS §6.1 doctype-fork and the DIRECTIVE-034 §34.1 substrate gate with no rule-dump (the D4 no-re-encode design working). The same dogfood spot-check surfaced a corpus inconsistency — see §3.
3. **Close records (PR #19, squash → `main` @ `51620434`).** Two files — ruling ledger (R029–R031) + review-of-record — verbatim, byte-intact through the squash, `# File:` headers path-match. No label (mirrors the Phase-1 close PR #17).

Rulings this cycle: **R029** single-repo rescope · **R030** deployed `SKILL.md` out of DMS §1.2/§1.3 scope (generated artifact + external-tool-convention) → exempt from §2.2 header + §5 filename, codification deferred to the Phase-4 DDR · **R031** §13.3 cp-form is preservation-scoped (deliberate rename → explicit-filename cp).

## 2. Deliverables & shape

- **Merged PR #18 (deploy, @ `5c6bf130`):** `.claude/skills/author-decision-record/SKILL.md`, one commit, label `semver: minor`.
- **Merged PR #19 (close records, @ `51620434`):** `docs/ruling-rationale/2026-06-16-heb-9-phase-2-rulings.md` + `docs/reviews/2026-06-16-heb-9-phase-2-author-decision-record-skill-deploy-review.md`, one commit (+225), no label.
- **D9:** confirmed live on `main` (lists + `/` menu + model-invocation). `/doctor` not exposed in that Code environment (non-blocking; no description-budget pressure at one skill).
- **Linear (HEB-9):** Phase-2-landed comment → D9-confirmed reply → ADR-route finding comment; state left **In Progress** (multi-phase ticket; acceptance = the D8 dogfood).
- **Close artifacts:** this handoff + the ruling-rationale ledger (R029–R031) + the review-of-record.

## 3. Carry-Forward / Next

- **HEB-9 SOFIA-Reboot leg — NOW UNBLOCKED.** RBT-35 landed (Done; SOFIA-Reboot PR #9 squash → `develop` @ `cb97c9cd`, three-hat PASS-CONVERGED, ruling R21). The fix was **Option B — governed-set collection** (the durable fix, absorbing RBT-31): `validate-docs-structure.sh` now scopes to the DMS §1.2 governed set, so `.claude/skills/**` is **outside collection entirely** (not merely exempted) and the header-less `SKILL.md` passes CI. Re-deploy the **byte-identical** payload (sha `b1bd05a8…`) into SOFIA-Reboot's `.claude/skills/` — note SOFIA-Reboot is **develop-based gitflow and HAS CI**, unlike HE-Bedrock. Then **Phase-3 SDD-route dogfood** (author one SOFIA SDD with the skill live; measure fire + friction — D8 acceptance).
- **HEB-9 Phase-4 / compilation DDR (PP-4a, post-dogfood).** Firms the provisional `skill-source/` manifest format + generalizes the contract to the six concerns. Also the home for: (a) the **ADR-route finding** bucket decision, and (b) the R031 §13.3 codification.
- **ADR-route finding (captured on HEB-9, 2026-06-17).** The compiled skill marks the ADR route "stubbed / template not yet built," but `docs/templates/adr-template.md` exists complete on disk since 2026-06-08 (`docs/adr/` still absent). The route-inactive claim is defensible; the "template not built" implication is stale. Resolve at the Phase-4 recompile — bucket it (reword "template drafted, activation deferred" / activate the route / treat as premature pre-build). Fix is a `skill-source/author-decision-record.md` manifest edit + recompile, **never** a hand-edit of the generated `SKILL.md` (D6).
- **RBT tail-work (SOFIA-Reboot side, non-blocking context for the deploy session):** RBT-38 (growable-checker deferred — F2 date-prefixed-doc slug-conformance gap + C-2 space-filename double-report), RBT-36 (pre-schema identity-straggler sweep, 8 files). Neither gates the skill deploy.
- **This handoff vendoring.** Authored after PR #19 merged, so it is **not yet on `main`** — vendor in a small follow-up commit when convenient (the close-records PR was scoped to ledger + review only).
- **Project-knowledge refresh.** No corpus release this leg (kit/corpus unchanged; tag still `v2.3.0`), but `skill-source/` now has a deployed consumer — the Phase-1 refresh advisory still stands before the next cross-corpus authoring.

## 4. Cross-References

- *Governing standards: ENG-STD-003 v3.0.1 (apply-prompt authoring); DMS v3.1.0 (§1.2/§1.3 scope; §2.3.2 this schema; §6.1 doctype fork); DIRECTIVE-007 (three-hat) / -026 (role split) / -031 (frozen ledger §31.7) / -034 (§34.1 substrate gate).*
- *Artifacts: apply-prompt `~/Downloads/2026-06-16-heb-9-phase-2-deploy-author-decision-record-skill-apply-prompt.md` (the compiler, D7); review of record `docs/reviews/2026-06-16-heb-9-phase-2-author-decision-record-skill-deploy-review.md`.*
- *Ruling ledger: `docs/ruling-rationale/2026-06-16-heb-9-phase-2-rulings.md` (R029–R031). Next ruling: **R032**.*
- *Work item: HEB-9 (Governance Starter Kit; parent HEB-6) — Phase-2. PRs #18 (deploy @ `5c6bf130`) / #19 (close records @ `51620434`). Forward: HEB-9 Phase-3 dogfood / Phase-4 compilation DDR.*
- *Unblocker: RBT-35 (Done; SOFIA-Reboot PR #9 @ `cb97c9cd`; team Reboot, Setup & Governance). Related tail: RBT-38, RBT-36.*
- *Prior cycle: HEB-9 Phase-1 close (`docs/session-handoffs/2026-06-16-heb-9-phase-1-close.md`, R022–R028).*

*End of HEB-9 Phase-2 session-handoff.*
