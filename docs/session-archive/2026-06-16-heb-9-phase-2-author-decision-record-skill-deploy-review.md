# File: docs/reviews/2026-06-16-heb-9-phase-2-author-decision-record-skill-deploy-review.md
# Author: Claude (claude.ai authoring session 2026-06-16)
# Created: 2026-06-16
# Description: Antagonistic three-hat (LAA/SA/EA) review + §11.7.4 sandbox runtime of the HEB-9 Phase-2 apply-prompt that deploys the author-decision-record skill into HE-Bedrock .claude/skills/. Serves the pre-deployment gate for the HE-Bedrock leg of HEB-9 Phase 2.

# Three-Hat Review — 2026-06-16 (HEB-9 Phase-2 author-decision-record skill deploy, HE-Bedrock leg)

| Field | Value |
|---|---|
| **Review Date** | 2026-06-16 |
| **Reviewer** | Claude — three-hat reviewer (LAA · SA · EA), claude.ai-assisted under DIRECTIVE-007; design-side per DIRECTIVE-026 |
| **Scope** | The HEB-9 Phase-2 apply-prompt deploying `author-decision-record/SKILL.md` into HE-Bedrock `.claude/skills/`, plus its compiled SKILL payload |
| **Authority** | DIRECTIVE-007 (three-hat review-until-zero, §11.7) + the HEB-9 Phase-2 review request (this session); conformance standard ENG-STD-003 v3.0.1 |
| **Outcome** | **PASS** — converged to zero open findings at Pass 4 (trajectory 10 → 5 → 1 → 0); one accepted COSMETIC residual (C-3) routed to HEB-28. The pre-deployment gate for the HE-Bedrock leg is **satisfied**. |

---

## §1 Scope

### 1.1 In-scope per the HEB-9 Phase-2 review request

- `docs/session-handoffs/apply-prompts/2026-06-16-heb-9-phase-2-deploy-author-decision-record-skill-apply-prompt.md` — the apply-prompt-as-compiler: phase/pause-point structure, pre-flight gates, the §6.7–§6.15 dry-execute pass, apply/verify/commit, push/PR, and all summary surfaces (frontmatter, cold-read, commit message, PR body, §Scope, §12, post-merge, cross-refs).
- `author-decision-record-SKILL.md` (staging payload → deployed as `.claude/skills/author-decision-record/SKILL.md`) — frontmatter-first discovery shape, Option-B pointer body, and verbatim fidelity of the load-bearing trigger to its source manifest.
- Conformance against ENG-STD-003 v3.0.1 (apply-prompt authoring), DMS v3.1.0 (§1.2/§1.3 scope basis), and the ratified HEB-9 scope (D1–D10, PP-0→PP-4).

### 1.2 Method

Four antagonistic passes under the §11.7 review-until-zero cadence, each opened with a §11.7.7 fresh re-anchor against the current bytes (no carry-forward of prior line numbers). Each pass produced dispositioned findings (BLOCKING / MATERIAL / COSMETIC / POSITIVE) and was followed by a §11.7.4 sandbox runtime pass on Claude's computer (bash 5.2; constructs verified bash-3.2-compatible). Live repo/authority state was fetched directly (HE-Bedrock `.git/refs/heads/main`, SOFIA-Reboot `validate-docs-structure.sh`, the source manifest) rather than recalled.

### 1.3 Out of scope (deliberately)

- The SOFIA-Reboot deploy leg — deferred this cycle (see §Scope ruling and §3 triage); not reviewed here beyond verifying the forcing constraint.
- The HEB-9 Phase-4 compilation DDR (manifest-format firming, six-concern generalization, `.claude/skills/` convention codification) — future work.
- Deterministic-compiler behavior (HEB-28) — the manifest→SKILL compile is provisional/non-deterministic this cycle by design.

---

## §2 Findings

All findings are recorded with the pass that raised them and the pass that resolved them — the cross-pass resolution trail is the audit substrate. Net open at convergence: **zero** (one accepted COSMETIC residual).

### 2.1 BLOCKING findings

#### Finding B-1: baseline-SHA gate could never pass (width mismatch → guaranteed halt)

**Location:** apply-prompt §1.3 (Baseline SHA).

**Description:** The Pass-1 baseline gate compared a truncated expected SHA against a differently-truncated `git rev-parse --short` actual, so the equality test could never hold — a guaranteed halt on the clean path.

**Why blocking:** A pre-flight gate that always fails halts every execution before any mutation; the deploy could not proceed.

**Disposition:** **RESOLVED (Pass 2).** Rewritten to a full-40-char exact comparison (`EXPECTED_SHA` vs `git rev-parse main`). Sandbox + live verification: `EXPECTED_SHA = 48a119bb…5a5f` is byte-identical to the current `.git/refs/heads/main`; exact match passes (len 40 = 40).

### 2.2 MATERIAL findings

#### Finding M-1: §6.9 label-existence check absent from the dry-execute pass — **RESOLVED (Pass 2)**
The §6.7–§6.15 dry-execute pass omitted the §6.9 LABEL-EXISTENCE-CHECK for `semver: minor`. Added to §1.4; single-repo scope means only HE-Bedrock's label is gated (confirmed present).

#### Finding M-2: §2.2 header exemption asserted without grounding — **RESOLVED (Pass 2)**
The header-less SKILL.md's exemption from the DMS §2.2 `# File:` rule was stated without a normative basis. Now grounded in DMS §1.2/§1.3 (generated artifact + external-tool-convention discovery path; same basis as `CLAUDE.md`/`README.md`), propagated to cold-read, commit message, PR body, and §0.5, with first-class corpus codification routed to the Phase-4 DDR.

#### Finding M-3: §6.10 mis-citation (executor-identity probe ≠ parse probe) — **RESOLVED (Pass 2)**
The FP-5 executor-identity probe was labeled as the §6.10 BASH-INTERPRETER-PROBE; these are distinct concerns (executor-shell identity vs. prompt-syntax parse validity). The probe is now correctly labeled "FP-5 … NOT a §6.10 check," and the *actual* §6.10 per-block `bash -n` sweep was authored into §1.4.

#### Finding M-4: phase-structure anchor deviation — **RESOLVED (Pass 2)**
The Pass-1 both-repos shape produced two pre-flight phases, deviating from the canonical Phase 0/1/2/3 anchor. The single-repo rescope dissolved this; the structure now anchors cleanly (Phase 0 Cold-Read · 1 Pre-Flight · 2 Apply+Commit · 3 Push+PR).

#### Finding M-5: §13.3 cp-form (explicit-filename rename vs trailing-slash MUST) — **RESOLVED (Pass 2; ratified)**
The deploy renames `author-decision-record-SKILL.md` → `SKILL.md`, requiring explicit-filename `cp`, which appears to violate §13.3's trailing-slash form. Ratified reading: §13.3 binds the *preservation* case, not a deliberate rename. Documented in the new `## §12 Documented Exceptions`, with the §6.14 primitive + §2.2 `diff -q` byte-identity check as independent anchors.

#### Finding N-1: single-repo rescope deviated from ratified PP-4b — **RESOLVED (operator-ratified Pass 3; de-attribution completed Pass 4)**
The revision dropped the SOFIA-Reboot leg, deviating from PP-4b's both-repos-one-cycle ratification, and initially presented the split as if PP-4 had blessed it. The forcing reason was verified live (below, §2.4). The rescope was **operator-ratified this session** and documented in a new `## §Scope` ruling section ("a new, operator-ratified decision … does not derive from PP-4/PP-4b"); it is routed to the close ledger as R029. The de-attribution from "PP-4" propagated to every surface — completed at Pass 4 when the final residual (commit-message Refs) was corrected (see P3-1).

#### Finding N-2: deferred-cycle mislocated the validator's home — **RESOLVED (Pass 3)**
The deferred SOFIA-Reboot cycle modeled the fix as a "master `validate-docs-structure.sh` amendment + render." Live verification showed that validator is a **SOFIA-Reboot-native RBT-3 artifact** (2026-06-03, ENG-STD-002 v2.2.0; HE-Bedrock carries neither the script nor a template). Corrected to a **direct SOFIA-Reboot (RBT) amendment**, not master-amend-then-render.

#### Finding N-3: §6.8 deterministic AMBER self-fire — **RESOLVED (Pass 3)**
Sandbox-surfaced: the embedded §6.8 full-body heredoc-escape grep matched its *own* two describe-the-pattern lines every run, so the §1.4 aggregate could never reach the clean exit-0 path (a recurring SAFE-CONTEXT AMBER → pause-as-ceremony risk, §5.5.1 #2). Fixed by rewording the primitive's describe-prose to avoid self-match, adding a `grep -v 'HEREDOC-ESCAPE-GREP'` self-exclusion, and an R027 surface-scope note. Sandbox-confirmed GREEN post-fix; the clean path is now reachable.

#### Finding P3-1: commit-message Refs still attributed to "PP-4 Phase 2" — **RESOLVED (Pass 4)**
The N-1 de-attribution propagated everywhere except the §2.3 commit-message `Refs:` line — the one summary surface that would land the mis-attribution in *immutable git history* (the §11.7.2 propagation-drift class). Corrected at Pass 4 to `Refs: HEB-9 (Stage 4 — skill compiler + deploy), Phase 2 (single-repo rescope, supersedes PP-4b).`, now consistent with the PR-body and cross-ref surfaces.

### 2.3 COSMETIC findings

- **C-1** — dangling §0.6 PR-label note reference. **RESOLVED (Pass 2).**
- **C-2** — `.MD` uppercase filename casing on the apply-prompt. **RESOLVED (Pass 2;** renamed `.md`**).**
- **C-4** — pause-points didn't name the next phase. **RESOLVED (Pass 2;** PP-1/PP-2 now name the successor phase**).**
- **N-4** — §6.10 lacked a min-block-count floor (zero-extraction would false-green). **RESOLVED (Pass 3;** `NBLOCKS < 8` AMBER floor added; HEB-35 formalizes the worked-example**).**
- **N-5** — frontmatter `phase_count` replaced with a prose-valued field. **RESOLVED (Pass 3;** clean `phases:` enumeration + load-bearing `commit_count: 1`**).**
- **C-3** — manifest→SKILL compile drift: the discrimination cue reads "internal to **one** service" vs the manifest's "a **single** service," and the "Tests:" label is dropped. **OPEN — ACCEPTED.** Non-load-bearing prose drift inherent to the provisional non-deterministic compile; routed to HEB-28 (deterministic compiler). Not gate-blocking.

### 2.4 No-drift confirmations (positive findings)

- **B-1 fix value is real** — `EXPECTED_SHA` byte-identical to live `.git/refs/heads/main` (`48a119bb…5a5f`); exact 40-char comparison passes.
- **§6.10 block sweep** — 12 bash blocks extracted, 12/12 parse clean under `bash -n`, floor (8) met → GREEN. The self-referential §1.4 block (which embeds fence-matching awk) extracts correctly as a single block; in-body self-reference is handled.
- **§6.8 / §6.14 GREEN** — escape-grep clean (self-fire eliminated); no filename-shape-vs-trailing-slash `cp` inconsistency.
- **Staging surface assertions PASS** — payload is frontmatter-first; `name` and the ratified trigger are present in the `head -6` frontmatter region.
- **Trigger fidelity** — the SKILL `description` is byte-identical to the manifest's ratified trigger (load-bearing verbatim preserved).
- **Deferral rationale verified** — SOFIA-Reboot's `validate-docs-structure.sh` greps every tracked `*.md` for a `# File:` header and does not exempt `.claude/skills/`, so the header-less SKILL.md would RED SOFIA-Reboot CI; HE-Bedrock has no validator, no pre-commit hook, and no template copy, so it deploys cleanly. The single-repo rescope is sound.
- **Propagation discipline** — at Pass 4, every "PP-4" mention is a "supersedes PP-4b" framing; no bare attribution remains; commit-Refs / PR-Refs / cross-ref Work-item surfaces are mutually consistent.

### 2.5 Normative interpretations (dispositioned)

- **`.claude/skills/` as an external-tool-convention discovery path (DMS §1.2/§1.3).** The exemption of the header-less, fixed-name `SKILL.md` from §2.2/§5 is interpreted by analogy to convention-driven repo-root files (`CLAUDE.md`/`README.md`). The interpretation is flagged PROVISIONAL and routed to the **HEB-9 Phase-4 compilation DDR** for first-class corpus codification — not left implicit.
- **§13.3 cp-form is preservation-scoped.** Ratified (M-5): the trailing-slash MUST binds source-filename preservation; a deliberate rename uses the explicit-filename form. Captured in §12 Documented Exceptions.

---

## §3 Forward-Pointer Triage

### Candidate R029 — single-repo rescope ruling
**Source:** Finding N-1 / §Scope. **Disposition:** File as ruling R029 in the session-close ruling-rationale ledger — the rescope decision + the SOFIA-Reboot forcing-discovery, superseding PP-4b. (Ruling-ID counter advances to R029.)

### Candidate HEB-28 — deterministic skill compiler
**Source:** Finding C-3. **Disposition:** Existing backlog item; the manifest→SKILL prose drift is the motivating case. No new ticket.

### Candidate HEB-35 — §6.10 worked-example hardening
**Source:** Finding N-4. **Disposition:** Existing backlog item; formalize the min-block-count floor (here added inline as `NBLOCKS < 8`) into the §6.10 worked example. No new ticket.

### Candidate (Phase 4) — `.claude/skills/` convention DDR
**Source:** §2.5. **Disposition:** Fold into the HEB-9 Phase-4 compilation DDR — codify the external-tool-convention discovery path and the DMS §1.2/§1.3 exemption.

### Candidate (RBT, new) — SOFIA-Reboot validator-exemption + deploy cycle
**Source:** §Scope deferral / Finding N-2. **Disposition:** File as a SOFIA-Reboot (RBT) cycle: (1) direct amendment of native `validate-docs-structure.sh` to exempt `.claude/skills/**` per DMS §1.3 (and address the over-broad `git ls-files '*.md'` scan-scope), with its own three-hat; (2) the SOFIA-Reboot skill deploy (reusing this byte-identical payload); (3) the Phase-3 SDD-route dogfood in SOFIA-Reboot.

### Forward-pointer triage summary

| Proposed ID | Summary | Disposition |
|---|---|---|
| R029 | Single-repo rescope ruling (supersedes PP-4b) + forcing CI-discovery | File in session-close ruling ledger |
| HEB-28 | Deterministic compiler (resolves C-3 manifest→SKILL drift) | Existing item; route C-3 here |
| HEB-35 | §6.10 min-block-count floor codification | Existing item; formalize inline floor |
| HEB-9 Phase-4 DDR | Codify `.claude/skills/` convention + DMS §1.2/§1.3 exemption | Future Phase-4 work |
| RBT (new) | SOFIA-Reboot validator-exemption + deploy + SDD dogfood | File as RBT cycle (own three-hat) |

---

## §4 Audit Outcome

> **PASS.** One BLOCKING finding (B-1) resolved at Pass 2; all MATERIAL findings (M-1–M-5, N-1, N-2, N-3, P3-1) resolved across Passes 2–4; COSMETIC findings resolved except C-3, which is accepted and routed to HEB-28. The review converged to **zero open findings at Pass 4** (trajectory 10 → 5 → 1 → 0), with the §11.7.4 sandbox runtime fully green (§6.10 12/12 + floor; §6.8/§6.14 GREEN; staging + trigger-fidelity PASS). The pre-deployment gate for the HE-Bedrock leg of HEB-9 Phase 2 is **satisfied**; the apply-prompt is execution-safe to run against HE-Bedrock.

**Execution-time watch-item (non-finding):** local `.git/packed-refs` shows a stale `origin/main`; §1.2 `verify-repo-state.sh --expect-synced` fetches first and should reconcile, but confirm `origin/main` is at `48a119bb` before running.

---

## §5 Cross-References

- *Authority: DIRECTIVE-007 (three-hat review-until-zero, §11.7); ENG-STD-003 v3.0.1 (conformance standard); DMS v3.1.0 (§1.2/§1.3 scope basis).*
- *Documents reviewed: the HEB-9 Phase-2 apply-prompt + the `author-decision-record` SKILL payload (compiled from `skill-source/author-decision-record.md`).*
- *Disposition tracking: ruling R029 (session-close ledger); HEB-28 (C-3); HEB-35 (N-4); HEB-9 Phase-4 DDR (§2.5); SOFIA-Reboot RBT cycle (§Scope deferral).*
- *Prior cycle: HEB-9 Phase-1 (PR #16 kit 2.3.0 @ `2e62313`; PR #17 close records @ `48a119bb`); ruling ledger `docs/ruling-rationale/2026-06-16-heb-9-phase-1-rulings.md` (R022–R028).*
- *Role discipline: design-side authored under DIRECTIVE-026 (claude.ai authors/reviews; Claude Code executes the repo commit).*

*End of review-of-record.*
