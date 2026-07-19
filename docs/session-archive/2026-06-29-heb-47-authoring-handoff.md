# File: docs/session-handoffs/2026-06-29-heb-47-authoring-handoff.md
# Author: Claude (claude.ai deliberation session 2026-06-29)
# Created: 2026-06-29
# Description: Deliberation-to-authoring session-handoff for HEB-47 (cold-acceptance-review cleanup + two standard promotions + corpus release). Carries the ratified disposition ledger, the per-file edit specification with anchors locked at develop 2d7cc0c, net-new prose drafts, the single-apply-prompt commit manifest, the release plan, and the close-records plan. Successor session authors the apply-prompt against this spec after re-confirming the baseline.

---
session_date: 2026-06-29
develop_sha_baseline: 2d7cc0cb
session_close_status: COMPLETE
next_session_scope: Author the single multi-commit HEB-47 apply-prompt (cold-review cleanup + 2 standard promotions + corpus release) per the locked edit spec in §4-§7, then run dual-stream review.
---

# HEB-47 Authoring Handoff — Cold-Acceptance-Review Cleanup + Promotions

## 1. Session summary

This deliberation session worked HEB-47 — the cold-acceptance-review cleanup ticket — to full disposition. The independent cold review of the HEB-45 PR surfaced 12 findings; B-1 (README kit-version stamp) was already corrected in HEB-45 Commit 3, leaving 11. All 11 are now ratified, plus the HEB-40 guidance codification and the HEB-5 deferral.

Two findings rose above mechanical citation-repair into **standard promotions** — cases where implementation discovered a real discipline the standard never codified (the meta-pattern: bring the standard up, don't neuter the artifact). The rest are artifact-fixes, one structural reorder, one accept-as-is. HEB-47 also absorbs the **guidance half** of HEB-40 (corpus-release manifest completeness) and dogfoods it on its own release.

Scope grew from "citation cleanup" into **citation cleanup + two standard amendments + a corpus release + HEB-40 guidance + close-records** — internally coherent: one cold-review provenance, one delivery-surface coherence frame, one release boundary. Lands as a single multi-commit apply-prompt in one work PR (operator-ratified structure), before HEB-12 re-cascade so the debt is not propagated to SOFIA-Reboot / LILY.

## 2. Baseline & fresh-fetch state

- `main @ 2d7cc0c` (synced with `origin/main`), kit `VERSION` 2.6.0, annotated corpus tag `v2.6.0`.
- Document versions: CSD 3.4.0, DMS 3.3.0, ENG-STD-001 3.3.0, ENG-STD-002 2.3.0, ENG-STD-003 3.0.1.
- **Drift check (2026-06-29):** all ten edit-target files confirmed byte-identical to the deliberation substrate — zero drift. Anchors in §4 are locked to `2d7cc0c`.
- **Authoring-session obligation (§13.5.10 temporal-coordinate):** re-confirm `2d7cc0c` is still `develop`/`main` HEAD at Phase 0. If the world moved, re-fetch the affected files and re-lock anchors before any Phase-1 mutation.

## 3. Disposition ledger (ratified)

| # | Sev | Disposition | Target file(s) |
|---|---|---|---|
| B-2 | BLOCK | **Pointer-only**: §0.4.2 taxonomy block → "surface types per ENG-STD-003 §13.5.8"; example rows → current vocab | apply-prompt-template |
| B-3 | BLOCK | **Promote** (standard) + **pointer-only** (template): add §13.5.9 commit-script row; template §0.4.3 mapping → pointer | ENG-STD-003, apply-prompt-template |
| B-4 | BLOCK | **Promote**: codify `\|\| true`-when-non-actionable as new ENG-STD-002 §9.4; script comment repoints §6.6→§9.4 | ENG-STD-002, commit-script-template.sh |
| S-1 | SHOULD | Artifact-fix: §5.3 = categorical discipline; enumerated 10-check set is in the script (3 spots) | verify-repo-state-template.sh/.md |
| S-2 | SHOULD | Artifact-fix: YELLOW → AMBER (8 occurrences) | verify-repo-state-template.md |
| S-3 | SHOULD | Artifact-fix: §10.8 → §10.2 (Sanity stage); drop "MD5 verification" as section name | commit-script-template.sh |
| S-4 | SHOULD | Artifact-fix: demote Authority-Fetch Inventory to §0.4.3; restore §0.5 = Invocation | apply-prompt-template |
| S-5 | SHOULD | DMS-half: **trim-to-kernel** §3.6.4. Script-half: drop `(HEB-34)` ×2, comment bodies intact | DMS, commit-script-template.sh |
| N-1 | NIT | Fix: §13.5.9 "(frontmatter pattern)" → "(metadata-table pattern)" — sequenced BEFORE B-3 mirror | ENG-STD-003 |
| N-2 | NIT | **Phil-2** Status-row order, commented-in-slot optional rows: DDR unchanged, ADR + SDD move Status | adr/sdd-template |
| N-3 | NIT | **Accept-as-is**: dual "Substrate (bash + markdown)" is substrate-accurate; §2.3.5.2 escape clause covers it. Rationale → close-records | (none — no edit) |
| — | — | **HEB-40 guidance**: codify corpus-release manifest-completeness as prose (ENG-STD-003 + template §0.4); guard deferred to HEB-40 | ENG-STD-003, apply-prompt-template |
| — | — | **bare-version-file** §13.5.8 gap: **deferred to HEB-5** (logged on HEB-5, comment b009e350) | (none — deferred) |

## 4. Per-file edit specification — anchors locked @ 2d7cc0c

> Convention: each edit gives the **exact current anchor** (verbatim from disk) and the **target**. The authoring apply-prompt sweeps these as Phase-0 OLD-anchors per §13.5.8 sweep-then-edit. Net-new prose (§9.4, §13.5.9 row, guidance) is drafted in §5.

### 4.1 `docs/governance/ENG-STD-002-script-authoring-standards.md` — Commit 1

**Edit 1.1 (B-4 promote) — insert new §9.4 between §9.3 and §10.** Insertion point: after the §9.3 fenced code block closes (line 475), before the `---` rule (line 477) that separates §9 from §10. New section text in §5.1 below. After insertion, §9.3's content and the §9→§10 `---`/`## 10.` boundary are otherwise unchanged.

### 4.2 `docs/governance/ENG-STD-003-apply-prompt-authoring-standards.md` — Commit 2

**Edit 2.1 (N-1) — do FIRST.** Line 1458.
- OLD: `- ADR / DDR / SDD → DMS §2.3.1 (frontmatter pattern) + §4 (amendment) + §6 (doctype decision tree)`
- NEW: `- ADR / DDR / SDD → DMS §2.3.1 (metadata-table pattern) + §4 (amendment) + §6 (doctype decision tree)`

**Edit 2.2 (B-3 promote) — add commit-script row.** Insert between the Review-document row (line 1459) and the Apply-prompt row (line 1460), matching the failure-mode prose order at line 1450 (…review document, commit-script, apply-prompt…).
- NEW row: `- Commit-script → docs/../scripts/templates/commit-script-template.sh (canonical template) + ENG-STD-002 §10 (commit-script authoring discipline)`
  (use the repo-correct relative path `scripts/templates/commit-script-template.sh`.)

**Edit 2.3 (HEB-40 guidance) — new sub-clause §13.5.8.3.** Recommended home: end of §13.5.8 (after §13.5.8.2 PostVerify gate). Prose in §5.3 below. **Tracker-free** (no "HEB-40" in the normative body — that lineage lives in Linear/close-records; see discipline note §10).

### 4.3 `docs/templates/apply-prompt-template.md` — Commit 3

**Edit 3.1 (S-4) — renumber.**
- `## 0.5 Canonical-Authority-Fetch Inventory (when this PR produces structural artifacts)` → `### 0.4.3 Canonical-Authority-Fetch Inventory (when this PR produces structural artifacts)` (note `##`→`###` — now a §0.4 sub-section).
- Its self-ref `replace §0.5 with: "**Not applicable...**"` → `replace §0.4.3 with: …`.
- `## 0.6 Invocation` → `## 0.5 Invocation`.
- No external refs to old §0.5/§0.6 exist (verified); Phase-1.7 references §0.4.2 (unmoved).

**Edit 3.2 (B-2 pointer-only) — taxonomy block (line 120).**
- OLD: the full `***Surface-type taxonomy** (per ENG-STD-003 §13.5.8): metadata-cell / … / terminator. Pattern A docs … Pattern B docs … per-file enumeration is mandatory.*`
- NEW: `*Surface types per ENG-STD-003 §13.5.8. No two governance files share an identical manifest; per-file enumeration is mandatory.*`

**Edit 3.3 (B-2) — refresh example rows (lines ~122-124).** Replace stale example surfaces:
- `Document Metadata Version table-cell` / `metadata-cell` → `YAML version:` / `yaml-version`
- `Document Metadata Effective Date` / `metadata-date-stamp` → `YAML last_updated:` / `yaml-last-updated`

**Edit 3.4 (B-3 template, pointer-only) — mapping block (line 139).**
- OLD: full `***Artifact-authority mapping** (per ENG-STD-003 §13.5.9): ruling-rationale ledger → … apply-prompt → … NOT a substitute for fresh-fetch.*`
- NEW: `*Artifact authorities per ENG-STD-003 §13.5.9. Substrate-inheritance per ENG-STD-003 §3.1 is NOT a substitute for fresh-fetch.*`

**Edit 3.5 (B-3 template, pointer-only) — forbidden-patterns block (line 141).** Keep the additive second sentence; pointer-ize the restated list.
- OLD: `***Forbidden patterns** (per ENG-STD-003 §13.5.9): paraphrase / reconstruction-from-memory / sibling-substrate-inheritance / prior-art-as-authority. All authorities fetched VERBATIM where wording matters (anchor authoring, schema conformance); reference-fetched where only substrate-presence matters (ticket descriptions, structural existence).*`
- NEW: `*Forbidden patterns per ENG-STD-003 §13.5.9. All authorities fetched VERBATIM where wording matters (anchor authoring, schema conformance); reference-fetched where only substrate-presence matters (ticket descriptions, structural existence).*`

**Edit 3.6 (HEB-40 guidance mirror) — note into §0.4.2.** Add after the §0.4.2 discipline intro (line 108 block): `*If this manifest includes a corpus document (DMS / CSD / an ENG-STD), it MUST also enumerate the corpus-release surfaces — kit VERSION, PROVENANCE.md, the annotated corpus tag, and the README kit-version headline — per ENG-STD-003 §13.5.8.3.*`

### 4.4 `docs/DOCUMENT_MANAGEMENT_STRATEGY.md` — Commit 4

**Edit 4.1 (S-5 DMS, trim-to-kernel) — §3.6.4 "Provisional internal format" paragraph.**
- OLD: `**Provisional internal format.** Only the directory's canonical placement and filename pattern are canonized here. The manifests' *internal* format (schema, body shape) is PROVISIONAL pending the HEB-9 compilation DDR, which firms it; this avoids premature canonization of a still-evolving schema (CLAUDE.md §7).`
- NEW: `**Internal format.** Only placement and filename pattern are canonized here; the internal manifest format (schema, body shape) is out of scope for this section.`
- The following `**CI recognition…**` paragraph is **untouched** (HEB-43 §24.1 seam, out of scope).

### 4.5 `scripts/templates/commit-script-template.sh` — Commit 5

**Edit 5.1 (B-4 repoint) — line 438.**
- OLD: `        # operator sees why. ENG-STD-002 §6.6's || true pattern applies only when`
- NEW: `        # operator sees why. ENG-STD-002 §9.4's || true pattern applies only when`

**Edit 5.2 (S-3) — line 454.**
- OLD: `        # Verify content matches (per ENG-STD-002 §10.8 MD5 verification)`
- NEW: `        # Verify content matches (per ENG-STD-002 §10.2 Sanity stage — file-content verification)`

**Edit 5.3 (S-5 script) — drop `(HEB-34)` ×2.**
- Line 143 OLD: `    # pattern never reaches the \`case\` and the branch is falsely rejected (HEB-34).` → NEW: `    # pattern never reaches the \`case\` and the branch is falsely rejected.`
- Line 274 OLD: `            # this point. Same guard class as _match_allowlist (HEB-34); -f state is` → NEW: `            # this point. Same guard class as _match_allowlist; -f state is`

### 4.6 `scripts/templates/verify-repo-state-template.sh` — Commit 5

**Edit 6.1 (S-1) — 2 spots.**
- Line 11 OLD: `# Codifies the normative 10-check pre-flight from ENG-STD-002 §5.3.` → NEW: `# Codifies the enumerated 10-check pre-flight; the categorical pre-flight discipline is ENG-STD-002 §5.3.`
- Lines 47-48 OLD: `# See docs/governance/ENG-STD-002-script-authoring-standards.md §5.3 for the` / `# normative check set.` → NEW: `# See docs/governance/ENG-STD-002-script-authoring-standards.md §5.3 for the` / `# categorical pre-flight discipline; the enumerated 10-check set is defined in this script.`

### 4.7 `scripts/templates/verify-repo-state-template.md` — Commit 5

**Edit 7.1 (S-1) — 3 spots.**
- Line 9 OLD: `**Normative source:** ENG-STD-002 §5.3 (Repo-State Pre-Flight check set).` → NEW: `**Categorical source:** ENG-STD-002 §5.3 (Repo-State Pre-Flight categories); the enumerated 10-check set is defined in \`verify-repo-state-template.sh\`.`
- Line 12 OLD: `…For the normative check set definition, see ENG-STD-002 §5.3.` → NEW: `…For the categorical pre-flight discipline, see ENG-STD-002 §5.3; the enumerated 10 checks are defined in the script.`
- Line 155 OLD: `- **ENG-STD-002 §5.3** — Normative source for the 10-check pre-flight set.` → NEW: `- **ENG-STD-002 §5.3** — categorical pre-flight discipline (the enumerated 10-check set lives in the script).`

**Edit 7.2 (S-2) — YELLOW → AMBER, all 8 spots.** Lines 46 ("yellow/info content", "no yellows fired"), 91 ("yellow warnings"), 110 ("Yellow checks warn but don't block"), 115-119 + 123 (severity-table column values, 6 rows), 125 ("red = block, yellow = surface…"; "ignore enough yellows"), 133 ("no YELLOW path for identity"). Map Yellow→Amber / YELLOW→AMBER / yellow→amber preserving case. Leave RED/GREEN/INFO untouched.

### 4.8 `docs/templates/adr-template.md` + `docs/templates/sdd-template.md` — Commit 6

**Target Phil-2 order:** `Document ID → [Service] → Version → [Platform Version] → Status → Date → Authors → [Supersedes] → [References]`. Optional rows stay **commented-in-slot** (preserve the existing HTML-comment pattern, relocated).

- **adr-template.md:** Status row currently at position 2 (before Version). Move it to **after** the commented Platform Version block, **before** Date. Result: ID → Version → [PV] → Status → Date → Authors → Supersedes.
- **sdd-template.md:** Status row currently after Authors (near bottom). Move it to **between** the commented Platform Version block and Date. Result: ID → Service → Version → [PV] → Status → Date → Authors → Supersedes → References.
- **ddr-template.md:** already conformant — **NO EDIT.**

## 5. Net-new prose drafts (refine wording + confirm placement at authoring)

### 5.1 ENG-STD-002 §9.4 (B-4)

```
### 9.4 Deliberate Failure Suppression (`|| true`)

Appending `|| true` (or `… 2>/dev/null || true`) to a command deliberately discards
its nonzero exit so the command cannot abort the script under `set -e` or `pipefail`.
This is permitted **only when the command's failure is non-actionable** — when a failure
carries no information the operator must act on and the correct behavior is to proceed
as if the command produced empty or absent output.

**Permitted (non-actionable).** Probes where absence is a valid, expected result — e.g.
`find "$GIT_DIR" -name 'COMMIT_MSG_*' … || true`, `git stash list … || true`,
`git remote prune --dry-run origin … || true`. If these "fail" (no matches, nothing to
prune), continuing with an empty result is correct.

**Prohibited (actionable).** Suppression of failures the operator must see — permission
denied, disk full, missing required input, a write that did not land. A `cp` into a
repository destination is always actionable; its failure code and message MUST surface
rather than be swallowed. Suppressing an actionable failure masks a real fault.

**Boundary test.** A suppression is permitted only if, were the command to fail, the
script's correct response would be to continue unchanged. If a failure should instead
change script behavior — abort, warn, retry, or branch — it is actionable and MUST NOT
be suppressed; handle it explicitly (capture the exit code, branch on it).

**Relationship to §9.2 / §9.3.** Those govern omitting `set -e` for an entire
verification script; §9.4 governs per-command suppression within an otherwise-strict
script — global fail-fast is kept, and only specific non-actionable commands are exempt.
```
Plus a `## Change Log` row for the new version (see §7).

### 5.2 ENG-STD-003 §13.5.9 commit-script row (B-3)
`- Commit-script → scripts/templates/commit-script-template.sh (canonical template) + ENG-STD-002 §10 (commit-script authoring discipline)`

### 5.3 ENG-STD-003 §13.5.8.3 manifest-completeness guidance (HEB-40)

```
##### 13.5.8.3 Corpus-Release Surface Completeness

When an apply-prompt's manifest includes any corpus document (a versioned governance
standard — DMS, CSD, or an ENG-STD), the manifest MUST also carry the corpus-release
surfaces in the same PR: the kit `VERSION` bump, the `PROVENANCE.md` refresh, the
annotated corpus tag (cut on the merge commit), and the `README.md` kit-version
headline. A corpus amendment that lands without its release surfaces is an incomplete
manifest.
```
(No tracker reference in the normative body. The mechanical pre-flight guard is the open remainder of the release-step ticket; that lineage stays in Linear / close-records.)

## 6. Commit-per-concern manifest — single apply-prompt, one work PR

| Commit | Concern | Files |
|---|---|---|
| 1 | ENG-STD-002 §9.4 promote (B-4) + version bump + Change Log | ENG-STD-002 |
| 2 | ENG-STD-003: N-1 → B-3 row → §13.5.8.3 guidance + version bump + Change Log | ENG-STD-003 |
| 3 | apply-prompt-template §0.4 restructure (S-4, B-2, B-3 template, guidance mirror) | apply-prompt-template |
| 4 | DMS §3.6.4 trim (S-5 DMS) + version bump + Change Log | DMS |
| 5 | script-templates (B-4 repoint, S-3, S-5 script; S-1, S-2) | commit-script-template.sh, verify-repo-state-template.sh/.md |
| 6 | doctype-template Status reorder (N-2) | adr-template, sdd-template |
| 7 | corpus release | VERSION, PROVENANCE.md, README.md (+ annotated tag post-merge) |

Within Commit 2, sequence N-1 before the B-3 mirror so the row reflects corrected authority. Each Apply-phase commit carries the §2.2 verify + §2.4 pause-point per ENG-STD-003 §5.3.

## 7. Corpus release (Commit 7 — dogfoods the §13.5.8.3 guidance)

Proposed bumps — **confirm at authoring**:
- Kit `VERSION`: 2.6.0 → **2.7.0** (additive standard content).
- ENG-STD-002: 2.3.0 → **2.4.0** (new §9.4, additive normative).
- ENG-STD-003: 3.0.1 → **3.1.0** (new §13.5.8.3 + §13.5.9 row, additive; N-1 editorial).
- DMS: 3.3.0 → **3.3.1** (§3.6.4 trim — contract preserved, editorial/patch).
- CSD, ENG-STD-001: unchanged.
- `PROVENANCE.md`: refresh the three changed document-version entries + kit version.
- `README.md`: headline `**2.6.0**` → `**2.7.0**`; review the "What's in it" narrative for accuracy (likely number-only).
- Annotated corpus tag `v2.7.0` cut on the merge commit.

This PR is itself the first corpus amendment to carry the full four-surface release under the just-codified §13.5.8.3 — the dogfood case.

## 8. Close-records (separate close PR, per standing two-PR discipline — confirm)

Work lands in the one PR (Commits 1-7). Close-records follow as the standard separate close PR:
- Vendor the cold review → `docs/reviews/2026-06-29-cold-acceptance-review-HE-Bedrock.md` (source at `~/Downloads/cold-acceptance-review-HE-Bedrock.md`).
- Vendor this handoff → `docs/session-handoffs/`.
- **Ruling-rationale assessment:** the two promotions (B-4 §9.4; B-3 §13.5.9 row) and the S-5 DMS contract-purity trim (a HEB-38 one-home-rule application to a new carrier) are ruling-grade candidates per DIRECTIVE-031 §31.3; the artifact-fixes are substrate, not rulings. Assess, then assign ruling IDs **after verifying global-max across both the repo `docs/ruling-rationale/` ledger and Notion** (HEB-41 lesson — claim-then-record, not local max). Capture N-3 accept-as-is rationale.
- Linear three-layer capture on HEB-47 (comment + description banner pasted in-editor by operator + state), then ledger freeze (DIRECTIVE-031 §31.7) after the coherence gate.
- **Close HEB-25 alongside** (its B-2 scope is satisfied by this PR's pointer-only fix).

## 9. Linear state — routing targets (already actioned this session)

- **HEB-5:** comment `b009e350` posted — `bare-version-file` §13.5.8 gap deferred in, to ride HEB-5's §13.5.8 rework; cross-ref HEB-40 when the type lands. No relation change (already related).
- **HEB-40:** comment `55e85a10` posted — release-surface set now four (incl. README headline); guidance half ratified + landing in HEB-47 (closed, do-not-re-deliberate barring new learning); guard half is HEB-40's open remainder, coordinating with the validator + HEB-5's `bare-version-file` type. HEB-40 stays open.
- **HEB-25:** to be closed alongside HEB-47 (B-2 satisfied).
- **HEB-39:** related — script-half S-5 fix does not pre-empt its inline-ref-purity doctrine assessment; evidence (HEB-34 provenance) preserved in git + the Linear relation.
- **HEB-14:** related — S-5 DMS-half is DMS-coherence-adjacent.

## 10. Authoring-session discipline reminders

- **Fresh-fetch + temporal coordinate (§13.5.9 / §13.5.10):** re-confirm `2d7cc0c` at Phase 0; re-lock anchors if `develop` moved. This handoff is the index + edit spec, not an authority over the live files — fetch verbatim.
- **DIRECTIVE-026 tiers:** claude.ai authors the apply-prompt (Tier-1) → operator downloads (Tier-2) → Claude Code executes repo writes (Tier-3). Never write the repo from the authoring session.
- **No tracker IDs in normative bodies:** the §13.5.8.3 guidance and the §3.6.4 trim must stay tracker-free (this is literally what S-5 fixed — do not reintroduce "HEB-NN" into ENG-STD/DMS prose).
- **Commit-message hygiene:** repeated `-m` flags, never a single multi-line `-m` (blank lines collapse through the markdown→bash tempfile pipeline).
- **Bash-block execution:** write blocks to a tempfile and run `bash <tempfile>`; do not paste inline (Claude Code's Bash tool runs under zsh; apply-prompt blocks target bash-3.2, 0-indexed arrays). Candidate block-1 guard: `[ -n "${BASH_VERSION:-}" ] || { echo RED; exit 1; }`.
- **Dual-stream review:** antagonistic + three-hat, both required for convergence; §11.7.4 sandbox runtime pass is necessary-but-not-sufficient after static convergence (watch for grep leading-dash, `LC_ALL=C sort`, awk-builtin collisions, bash/zsh gaps). Expect fix-induced drift (§32.4.1) — sequential verification, not batch.
- **Sweep by concept, not phrasing:** phrase-scoped sweeps false-close (HEB-45 §7.1 lesson). The N-2 reorder, the YELLOW→AMBER sweep, and the pointer-only conversions each want concept-level confirmation, not just string matches.

*End of HEB-47 authoring handoff.*
