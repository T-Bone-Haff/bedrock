# File: docs/reviews/2026-06-18-heb-9-sofia-reboot-deploy-three-hat.md
# Author: Claude — claude.ai design-side three-hat reviewer (DIRECTIVE-026 authoring instance), Haffey Enterprises LLC
# Created: 2026-06-18
# Description: Consolidated three-hat review-of-record (LAA/SA/EA) for the HEB-9 SOFIA-Reboot leg —
#              deploy of the byte-identical author-decision-record compiled skill into SOFIA-Reboot
#              .claude/skills/. Folds review Passes 1-3 (§11.7.5) into one citable artifact; serves the
#              pre-execution readiness gate for the apply-prompt. Outcome: PASS — CONVERGED.

# Three-Hat Review-of-Record — HEB-9 SOFIA-Reboot deploy of author-decision-record skill (2026-06-18, pre-execution readiness gate)

| Field | Value |
|---|---|
| **Review Date** | 2026-06-18 |
| **Reviewer** | Claude — claude.ai design-side three-hat (LAA/SA/EA), DIRECTIVE-026 authoring instance, Haffey Enterprises LLC |
| **Scope** | Execution-readiness + standards-conformance of the apply-prompt `2026-06-18-heb-9-sofia-reboot-deploy-author-decision-record-skill-apply-prompt.md` (single-commit, byte-identical skill vendor into SOFIA-Reboot `.claude/skills/`), final version **v2.1**. |
| **Authority** | DIRECTIVE-007 (three-hat antagonistic review); ENG-STD-003 v3.0.1 §11.7 (review-until-zero-findings cadence) · §11.7.4 (sandbox runtime-verification + residual blind spots) · §11.7.5 (consolidated review-of-record folds all passes) · §11.7.7 (between-pass fresh-fetch); DIRECTIVE-026 (design-side authoring instance). |
| **Outcome** | **PASS — CONVERGED (zero-findings).** Four findings surfaced across the cadence (1 MATERIAL + 3 COSMETIC), **all resolved** by v2.1. Convergence reached at Pass 3 (zero new + zero unresolved), corroborated by a §11.7.4 sandbox run (16/16 blocks parse-clean; full dry-execute + Commit-1 + push-gate logic GREEN against the real payload; two negative controls behaved). The pre-execution readiness gate is **satisfied at the design + sandbox level**; the named runtime residual (macOS/BSD/bash-3.2 executor; live `gh` push/PR) is explicitly deferred to the executor — execution-ready, not zero-defect-certified. |

---

## §0 Review cadence (Passes 1–3 folded — §11.7.5)

This is the consolidated review-of-record: it folds the full antagonistic cadence into one authoritative document rather than recording only the final pass. The apply-prompt was reviewed across three passes, each re-anchored against fresh-fetched substrate (§11.7.7); the operator ratified each disposition before the next revision.

| Pass | Reviewed | Result | Operator disposition → revision |
|---|---|---|---|
| **Pass 1** | apply-prompt v1.0 | 0 BLOCKING · **1 MATERIAL (M-1)** · 2 COSMETIC (C-1, C-2) · 10 POSITIVE (empirical) | M-1 → **Path A** (trailing-slash `cp`); C-1, C-2 fixed → **v2.0** |
| **Pass 2** | apply-prompt v2.0 | M-1, C-1, C-2 **3/3 resolved**; **+1 COSMETIC (C-3)** (propagation drift from the C-1 fix) | C-3 → **restore `--limit 100`** → **v2.1** |
| **Pass 3** | apply-prompt v2.1 | **0 new findings**; C-3 resolved; **+ §11.7.4 sandbox run** (16/16 parse; full-chain GREEN; 2 negative controls) | **CONVERGED** — no further revision |

Severity-mix trajectory: **1M+2C → 1C → 0** (MATERIAL → COSMETIC → none) — the healthy §11.7.3 convergence collapse, not a re-opening series.

**Three-hat coverage.** The antagonistic passes were run from three vantages per DIRECTIVE-007: **LAA** (daily-driver — will Claude Code execute this cleanly?), **SA** (systems/migration — cross-repo source, CI behavior, branch model, rollback), **EA** (governance/pattern — ENG-STD-003 conformance, R029–R031, DDR-001, DMS scope). Findings are tagged with the surfacing hat in §2.

---

## §1 Scope

### 1.1 In-scope (per DIRECTIVE-007 + the HEB-9 SOFIA-Reboot leg)

- The apply-prompt v2.1 in full: frontmatter; §0 cold-read; §0.4 carry-forward; §0.5 canonical-authority N/A; §0.6 invocation + bash-shelling; §0.7 Phase-0 dry-execute pass (§6.7–§6.16); §1 pre-flight; §2 Commit 1; §3 (reserved); §4 push + PR; §5 post-merge; §6 cross-references.
- Conformance to ENG-STD-003 v3.0.1 (phase structure, primitive catalog, pause-points, exit-code convention, fresh-fetch family), the canonical apply-prompt template, ENG-STD-002 commit mechanics (inherited), DMS scope, DDR-001 byte-identity rationale, and the HEB-9 rulings R029–R031.
- Empirical truth of every load-bearing execution claim (payload identity, baseline SHA, bootstrap precondition, pointer resolution, CI scope, provenance SHAs).

### 1.2 Empirical-verification method (independent reads + sandbox)

Design-side verification used independent filesystem reads of both clones (not relayed transcription) for the load-bearing claims (Pass 1), re-confirmed the asserted baseline at each pass (§11.7.7), and ran a §11.7.4 sandbox exercising the bash blocks against a mock fixture seeded with the **real** payload (Pass 3). This is sampled-by-load-bearingness, not exhaustive line coverage: every claim a gate depends on was checked; descriptive prose was read but not independently re-derived.

### 1.3 Out of scope (deliberately)

- **On-executor runtime behavior** (macOS/BSD/bash-3.2; live `gh` push/PR) — structurally uncoverable from a Linux design-side sandbox. The §0.7.1 BASH-INTERPRETER-PROBE + the executor's first-block bash invocation are the catch. Deferred-to-runtime per §11.7.4. (See §2.4 R-1.)
- **The deployed skill's *content*** — a byte-identical vendor of an already-authored, already-reviewed artifact (HE-Bedrock PR #18). The known ADR-route wording imperfection is carried byte-identical by design (D6 forbids hand-editing the generated `SKILL.md`; the fix is a manifest edit + recompile in the Phase-4 DDR). Tracked, out of this PR's scope.
- **Close-records vendoring destination** (which repo's `docs/reviews/` + ledger this leg's close-records land in) — a close-out routing decision, surfaced in the vendoring note below, not an apply-prompt-correctness question.

---

## §2 Findings

All four cadence findings are **RESOLVED** in v2.1. They are recorded here with full lifecycle (surfaced → disposition → resolution → confirmation) per the review-of-record's fold-all-passes mandate.

### 2.1 BLOCKING findings

**None.** No finding blocked the readiness gate at any pass.

### 2.2 MATERIAL findings — RESOLVED

#### Finding M-1 (EA primary, LAA concurring) — §2.1 `cp`-form for a source-name-preservation case · surfaced Pass 1 · **RESOLVED v2.0, confirmed Pass 2, sandbox-validated Pass 3**

**Location:** apply-prompt §2.1 (Apply — bootstrap-create + vendor).

**Description.** v1.0 used explicit-filename `cp "$SRC" "$DEST"` for what is a source-name-**preservation** copy (source basename `SKILL.md` == destination basename `SKILL.md`). R031 (read verbatim from the frozen Phase-2 ledger) scopes ENG-STD-003 §13.3: *trailing-slash `cp` binds the preservation case; explicit-filename is the rename form.* The Phase-2 HE-Bedrock deploy was a **rename** (`author-decision-record-SKILL.md` → `SKILL.md`), so its explicit-filename form was correct and R031 was authored to sanction it; this SOFIA-Reboot leg is **preservation**, so R031's preservation→trailing-slash binding applies. v1.0 carried the Phase-2 form forward without re-applying the preservation-vs-rename distinction.

**Why MATERIAL (not BLOCKING).** Not a correctness defect — the copy produced the right bytes at the right path, triple-verified (§2.2 `test -f` + destination sha256 + §4.2 exact-diff). It was a same-ticket normative-conformance gap with no `§12` documented-exception.

**Disposition (operator-ratified): Path A** — switch §2.1 to the §13.3 trailing-slash preservation form `cp "$SRC" "$DEST_DIR/"`. Path A is the literal R031-conformant form for preservation, so **no `§12` exception is needed** (Path A is the rule, not a waiver). The Pass-1 alternative (Path B: retain explicit-filename + document + refine R031) was declined; the contingent R031-scope-refinement forward-pointer is therefore withdrawn.

**Resolution.** v2.0 §2.1 reads `cp "$SRC" "$DEST_DIR/"` with `DEST_DIR=".claude/skills/author-decision-record"`, an accurate R031/§13.3 rationale comment, and the triple-verify intact. Pass 2 re-anchored it resolved. Pass-3 sandbox: the trailing-slash `cp` landed the payload at exactly `.claude/skills/author-decision-record/SKILL.md`, byte-identical, basename preserved — confirmed by execution, not only by reading.

### 2.3 COSMETIC findings — RESOLVED

- **C-1 (EA) — §0.7.4 loose label-match · surfaced Pass 1 · RESOLVED v2.0.** v1.0 used `grep -qiE '^semver: patch'`, which could prefix-false-GREEN on a similarly-named label. Disposition: adopt canonical §6.9 exact-match. v2.0 → `command grep -Fxq "semver: patch"`. **Sandbox-validated Pass 3:** the negative control proved `-Fxq` does *not* false-GREEN on a prefix-similar `semver: patch-old`.
- **C-2 (EA) — §0.7.5 §6.14 note mis-scoped · surfaced Pass 1 · RESOLVED v2.0.** The note described cross-block re-declaration (a §11.9 concern) instead of §6.14's declaration-vs-usage-*shape* check. Disposition: re-scope. v2.0 rewrote the note to reason about shape (`DEST_DIR` directory-form in the trailing-slash `cp`; `DEST` filename-form only in verifies) with the §11.9 property correctly parenthesized as separate. (A sub-threshold semantic-label nit — "directory-shape" for a no-trailing-slash value — was recorded no-action across Passes 2–3; the §6.14 GREEN conclusion holds and the sandbox confirms no filename is discarded.)
- **C-3 (EA; propagation-drift from the C-1 fix) — §0.7.4 dropped `--limit` · surfaced Pass 2 · RESOLVED v2.1.** The C-1 remediation adopted `-Fxq` but dropped the limit flag, defaulting `gh label list` to 30 (latent false-AMBER if `semver: patch` sorts beyond 30 labels). Bounded (AMBER-only, §4.4-backstopped) but an incomplete adoption of canonical §6.9 (which carries `--limit 100`). Disposition: restore the limit. v2.1 → `gh label list --limit 100 --json name -q '.[].name' … grep -Fxq` — now exactly canonical §6.9. **Sandbox-validated Pass 3** (limit present; exact-match GREEN/AMBER both correct).

### 2.4 No-drift confirmations (positive findings)

**Empirical verification — independent filesystem reads (Pass 1; baseline re-confirmed Passes 2–3):**

- **P-1 Payload identity** — independently computed sha256 of the HE-Bedrock deployed copy = `b1bd05a8d7535bc2f81a33b9b554f91303a4f71500171b7914b6f47998873a61`, 3523 bytes — matches the §0.7.3/§2.2 gate and the cold-read claim.
- **P-2 Frontmatter** — line 1 `---`; `^name: author-decision-record`; `^description:` all present (the §2.2 greps).
- **P-3 Develop baseline** — SOFIA-Reboot `develop` = `cb97c9cd8a7478…` ⇒ short-8 `cb97c9cd`, matching `develop_sha_baseline` and §1.3; re-confirmed unchanged at Passes 2 and 3.
- **P-4 Bootstrap precondition** — no `.claude/` in SOFIA-Reboot (target absent), satisfying §0.7.2 create-mode.
- **P-5 Pointer resolution** — `docs/templates/{ddr,sdd,adr}-template.md` + `docs/DOCUMENT_MANAGEMENT_STRATEGY.md` present in SOFIA-Reboot; the skill's corpus pointers resolve in-repo.
- **P-6 CI scope** — SOFIA-Reboot CI has one active job (`validate-docs-structure`, post-RBT-35); its collection is `git ls-files -z 'docs/*.md' 'scripts/*.md'` and names `.claude/**` explicitly as out-of-scope. The frontmatter-first `SKILL.md` cannot RED CI. (LAA/SA.)
- **P-7 `verify-repo-state.sh` present** in SOFIA-Reboot `scripts/` — the §1.2 invocation resolves.
- **P-8 Provenance SHA `5c6bf130` correct, and is the corrected value** — HE-Bedrock reflog confirms PR #18's merge tip `5c6bf130…`; the author used the corrected SHA, not the `5c6bf13c` hand-extension error the Phase-2 trail flags.
- **P-9 Cross-repo branch model** — HE-Bedrock is main-based; the apply-prompt correctly drives SOFIA-Reboot on `develop` everywhere (no incorrect trunk inheritance). (SA.)
- **P-10 Wrong-repo guards + env-discipline** — §0.7.1 asserts both origins (SOFIA-Reboot target + HE-Bedrock source); `$SOFIA_REBOOT_ROOT` used exclusively (no `$IRIS_ROOT` leakage, no opener-boilerplate bad binding); per-block path re-derivation (§11.9); `cp` triple-verified. (EA/LAA.)

**Sandbox / mock-test (Pass 3, §11.7.4) — executed against a mock fixture with the real payload + correct origin URLs:**

- **S-1 Parse pass** — the genuine §6.10 awk-extraction + per-block `bash -n`: **16/16 blocks parse clean, 0 failures** (corroborates the apply-prompt's "16/16" claim).
- **S-2 Logic pass** — full chain ran **GREEN end-to-end**: §0.7.1 cross-repo identity → §0.7.2 bootstrap → §0.7.3 sha256-gate → §1.1–§1.4 pre-flight → §2.1 M-1 Path A `cp` (exact-path, byte-identical) → §2.2 verify → §2.3 staged-count + commit → §4.1 commit-count → §4.2 exact-diff → final `diff -q` byte-identical.
- **S-3 Negative controls behaved** — C-1/C-3 `-Fxq` did **not** false-GREEN on prefix-similar `semver: patch-old`; the §1.3 wrong-SHA control fired **RED** (drift halt live).

**Structural conformance (read-verified, no drift):**

- Canonical phase shape; §0.7 Phase-0 dry-execute home (HEB-4-R014); §0.4.2 + §0.5 correctly N/A (no governance amendment; byte-identical vendor of an already-reviewed artifact per §13.5.5), with the apply-prompt's own authoring authorities accounted for.
- §1.6 header N/A grounded in R030 (compiled-skill out of DMS §1.2/§1.3 scope; frontmatter-first); sha256-gate substitutes as integrity check.
- Exit-code convention §3.4 1-tier flat (`exit 1` failures; §0.7.4 AMBER echo-only per §6.16); both heredocs single-quoted (§6.8).
- Pause-points substantive per §5.5.1 (PP-0 dry-execute, PP-1 commit + LAA/SA/EA note, PP-2 PR URL).
- PR body follows §11.3 structure; the "Out of scope" line faithfully reflects the 2026-06-18 skill-delivery-surface resolution.
- D6 byte-identity correctly applied: the skill body is corpus-pointer-based with no placeholder substitution → repo-independent bytes; vendoring the sha256-verified bytes equals a recompile and removes a re-staging drift path (the ratified cross-repo-source deviation).

**R-1 Runtime residual (recorded, deferred — NOT a clearance):** the sandbox is Linux/bash-5.2 and took the `sha256sum` branch; macOS `shasum -a 256`, `mktemp` portability, bash-3.2, and live `gh` push/PR (§4.3–§4.5) are unexercised. The cross-platform `if command -v shasum` and §0.7.1 `BASH_VERSION` probe are the runtime guards. Per §11.7.4 / DIRECTIVE-032 §32.4.1, convergence + a clean sandbox is **not** zero-defect certification; this residual is held explicitly and deferred to the executor.

### 2.5 Normative interpretation — RESOLVED

**Question (surfaced Pass 1).** Under R031, is explicit-filename `cp` conformant for a preservation case, or does R031 bind trailing-slash for all preservation and reserve explicit-filename for rename?

**Disposition.** Operator ratified the literal R031 reading — **preservation → trailing-slash (Path A)**. v2.1 implements it. No R031 amendment is pending; the Pass-1 contingent refinement (which would have applied only under Path B) is **withdrawn**. No institutional drift left open.

---

## §3 Forward-Pointer Triage

No new backlog item is mandated by this review. For completeness:

| Proposed routing | Summary | Source | Disposition |
|---|---|---|---|
| — | R031-scope refinement (admit explicit-filename for fixed-verbatim-verified preservation) | M-1 / §2.5 | **Withdrawn** — contingent on Path B; operator chose Path A, which needs no R031 amendment. |
| (No new ticket) | ADR-route wording understates built state (adr-template exists since 2026-06-08) | HEB-9 comment 2026-06-17 | **Already dispositioned** to PP-2 ADR-route activation / Phase-4 manifest recompile. Carried byte-identical here by design (D6). Not re-filed. |
| (Operator close-out decision) | Close-records vendoring destination (HE-Bedrock HEB-9 trail vs SOFIA-Reboot work-local) | this review §1.3 + vendoring note | Decide at vendor time (see below). Not an apply-prompt defect. |

---

## §4 Audit Outcome

> **PASS — CONVERGED (zero-findings).** Across three antagonistic passes the cadence surfaced 1 MATERIAL (M-1, §2.1 `cp`-form under R031) and 3 COSMETIC (C-1 label match, C-2 §6.14 note scope, C-3 `--limit` propagation drift); **all four are resolved** in apply-prompt v2.1, each operator-ratified per item. Pass 3 reached the §11.7 convergence condition — a pass with zero new and zero unresolved findings — and a §11.7.4 sandbox run independently corroborated it (16/16 blocks parse-clean; full dry-execute + Commit-1 + push-gate logic GREEN against the real payload; both negative controls behaved). Every load-bearing execution claim is empirically verified.

**Gate status.** The pre-execution readiness gate is **SATISFIED at the design + sandbox level.** The sole residual the design-side process cannot certify is on-executor runtime (macOS/BSD/bash-3.2; live `gh`), explicitly deferred to the executor with the §0.7.1 probe as the runtime catch (§2.4 R-1). The apply-prompt is **execution-ready**; this is execution-readiness, not zero-defect certification.

---

## §5 Cross-References

- **Authority:** DIRECTIVE-007; ENG-STD-003 v3.0.1 §11.7 / §11.7.4 / §11.7.5 / §11.7.7; DIRECTIVE-026; DIRECTIVE-032 §32.4.1.
- **Artifact reviewed:** apply-prompt v2.1 — `docs/session-handoffs/apply-prompts/2026-06-18-heb-9-sofia-reboot-deploy-author-decision-record-skill-apply-prompt.md` (staged at `~/Downloads/` for execution).
- **Pass record (folded herein):** Pass 1 (v1.0; 0B/1M/2C/10P) · Pass 2 (v2.0; 3/3 resolved + C-3) · Pass 3 (v2.1; 0 new + sandbox → convergence).
- **Rulings:** R031 (§13.3 cp-form preservation-scoped → Path A) · R030 (SKILL.md out of DMS scope) · R029 (single-repo rescope) — frozen ledger `docs/ruling-rationale/2026-06-16-heb-9-phase-2-rulings.md`. Design rulings PP-0…PP-4 + D6 — Notion HEB-9 Design & Decisioning Ledger.
- **Canonical primitive:** ENG-STD-003 §6.9 (LABEL-EXISTENCE-CHECK; `--limit 100 … grep -Fxq`). Byte-identity rationale: DDR-001 + HEB-9 D6.
- **Payload provenance:** HE-Bedrock PR #18 (merged @ `5c6bf130`), sha256 `b1bd05a8…`, 3523 bytes. Unblocker: RBT-35 / SOFIA-Reboot PR #9 (merged @ `cb97c9cd`).
- **Tracking ticket:** HEB-9 (Phase-2 SOFIA-Reboot leg; stays In Progress — Phase-3 dogfood + Phase-4 DDR remain).
- **Calibration exemplar (same review type):** HEB-9 Phase-2 HE-Bedrock-leg three-hat review-of-record (the rename case R031 was authored against) — the nearest prior three-hat on a skill-deploy apply-prompt.
- **Vendoring:** see the vendoring note appended below; vendor as a close-record in a follow-up commit/PR separate from the work PR, per the close-records-separate-PR discipline (cf. HE-Bedrock PR #18 work / PR #19 close-records).

---

<!-- VENDORING NOTE (operator decision — not part of the citable body; delete or keep per convention)

Destination repo is the one open close-out routing question. Two defensible homes:
  (a) HE-Bedrock docs/reviews/ — co-locates ALL HEB-9 review-of-record artifacts on the tracking
      repo, consistent with the Phase-2 close-records pattern (PR #19). Recommended for HEB-9-trail
      cohesion.
  (b) SOFIA-Reboot docs/reviews/ — work-local records in the repo the deploy targets, the DDR-001-style
      pattern. Co-locates the review with the SKILL.md it reviews.
The # File: header path above (docs/reviews/2026-06-18-heb-9-sofia-reboot-deploy-three-hat.md) is
repo-relative and valid under either choice. Pair this review-of-record with the session's
ruling-rationale ledger (R032-onward) in the same close-records PR. Per DIRECTIVE-031 §31.7, this is a
point-in-time frozen record once vendored — supersessions go on new pages + the Linear trail, never by
retro-edit.
-->
