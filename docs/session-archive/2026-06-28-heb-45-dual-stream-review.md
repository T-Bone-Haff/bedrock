# File: docs/reviews/2026-06-28-heb-45-dual-stream-review.md
# Author: Claude (claude.ai dual-stream review session 2026-06-28) under DIRECTIVE-026 / DIRECTIVE-007 / DIRECTIVE-032
# Created: 2026-06-28
# Description: Consolidated dual-stream review-of-record for the HEB-45 in-document review-history
#              defect fix (HEB-38 Phase-1 content-contract escape). Synthesises the three-hat stream
#              (LAA/SA/EA, passes 1-3 + final), the antagonistic stream (DIRECTIVE-032, 2 passes), and
#              the §11.7.4 sandbox runtime pass into the review-of-record gating the HEB-45 work PR.
#              Vendored in Commit 2; point-in-time.

# HEB-45 Dual-Stream Review-of-Record — 2026-06-28 (Pre-Merge Gate)

| Field | Value |
|---|---|
| **Review Date** | 2026-06-28 |
| **Reviewer** | Claude — architecture team (LAA / SA / EA + antagonistic), claude.ai-assisted authoring under DIRECTIVE-026 |
| **Scope** | The HEB-45 five-carrier edit set + apply-prompt + R047 ledger — does the fix correctly, completely, and reference-preservingly remove the in-document review record across its carriers; is the freeze-bound record substantiated; and does the apply-prompt execute cleanly? |
| **Authority** | DIRECTIVE-007 (Multi-Role Review) + DIRECTIVE-032 (Antagonistic Review) run as parallel streams; §11.7 gate (zero BLOCKING + MATERIAL across both streams) plus the §11.7.4 sandbox runtime pass. |
| **Outcome** | **PASS WITH FINDINGS.** Dual-stream static convergence + §11.7.4 sandbox runtime pass reached: 0 BLOCKING across both streams; every MATERIAL finding (M-1…M-8) dispositioned and resolved. SB-1 — a locale-dependent staged-set sort — was caught in the runtime sandbox and fixed (`LC_ALL=C`). Gate satisfied. Environment-coupled legs noted as not-exercised; this is not a zero-defect certification (CSD §7 blind-spot doctrine). |

---

## §0 Framing

This review consolidates three sources into one review-of-record:

- **Three-hat stream (DIRECTIVE-007):** four passes (LAA/SA/EA). Pass-1 on the four-carrier set; pass-2 on the five-carrier set after the CSD §7.1 carrier was folded in; pass-3 verifying the post-pass-2 corrections; a final pass verifying the SB-1 fix and the antagonistic-substrate vendoring.
- **Antagonistic stream (DIRECTIVE-032):** two passes, verification-only (§32.3 — destinations named, enactment returned to the work session). Its combined-passes record is **co-vendored in this PR's Commit 2** at `docs/reviews/2026-06-28-heb-45-antagonistic-review-combined-pass1-pass2.md` (preserved verbatim per DIRECTIVE-007 §7.4).
- **§11.7.4 sandbox runtime pass:** a mock-apply of the apply-prompt against reconstructed-baseline copies, exercising the str_replace anchors, the verify blocks, the git mechanics, and the commit/message machinery.

The dual-stream design is load-bearing precisely because each stream catches what the other misses; §2.4 records the cross-stream asymmetry as audit substrate. The R047 ruling and its rationale are not restated here — they live in the ruling-rationale ledger (`docs/ruling-rationale/2026-06-28-heb-45-review-record-template-fix-rulings.md`), pointed to from §5.

---

## §1 Scope

### 1.1 In-scope

- `docs/templates/adr-template.md` — §7 Review-and-Approval removed; §8→§7 / §9→§8 renumber; metadata `Reviewers` + `Amendment Process` rows struck; §6 Compliance content-contract pointer repaired; Cross-References harmonised.
- `docs/templates/sdd-template.md` — §9 Architecture-Review removed; §10→§9 / §11→§10 renumber; new §11 Cross-References seated ahead of §12 Change Log.
- `docs/templates/ddr-template.md` — Cross-References parity touch (already clean of the defect).
- `docs/DOCUMENT_MANAGEMENT_STRATEGY.md` — §7.8 "the in-document review record" struck (aligned to §7.5); §4.4 → RESERVED; `version:` 3.2.0→3.3.0.
- `CLAUDE_SESSION_DIRECTIVES.md` — DIRECTIVE-007 §7.1 re-framed off the in-document table onto the external review of record (per DMS §7.5); §7.1 number + heading preserved; `version:` 3.3.0→3.4.0.
- `VERSION` (2.5.0→2.6.0), `PROVENANCE.md` (kit + DMS + CSD cells + Updated date).
- The apply-prompt as the execution carrier — anchor byte-exactness, str_replace uniqueness, verify coverage, two-commit structure, pause-point sequencing, **and a §11.7.4 sandbox mock-apply**.
- The R047 ledger staging file — accuracy against the edit set, §31.9 conformance, freeze-readiness.

### 1.2 Spot-check scope

- HEB-45 Linear trail (ratification capture for the §7.1 carrier, the §31.9 restructure, the CSD bump, and the antagonistic-substrate vendoring) and Notion (no separate R047 page — repo-vendored by design). Fresh-fetched at every pass.

### 1.3 Out of scope (deliberately)

- **RBT-47 validator pass** (SOFIA-Reboot @ `4afbe38`) — de-scoped to the HEB-12 re-cascade target; not a Bedrock-side gate on this PR.
- **R048 / SOFIA-Reboot adoption + instance cleanup** — later session, authored Reboot-side at the HEB-12 push.
- **DMS §4.x RESERVED-marker collapse + tail renumber** — HEB-46.

---

## §2 Findings

Findings carry **severity** (§2.1–§2.4) and **remedy** (DIRECTIVE-007 §7.2: add/fix · remove/relocate · none-default). The templates are morphing bodies (DMS §7.5), so the standing contract-purity lens (§7.2.1 / DMS §7.7) was applied as an active read — result in §2.4.

### 2.1 BLOCKING findings — none

No BLOCKING findings in any pass of either stream or the runtime sandbox. The edit set was sound from pass-1; the material findings were governance-capture, record-accuracy, freeze-sequencing, and one execution-layer portability defect — not edit-soundness defects.

### 2.2 MATERIAL findings — all dispositioned (RESOLVED)

#### M-1 (three-hat E-M1 / antagonistic P-2): CSD DIRECTIVE-007 §7.1 was an uncaught fifth carrier
**Remedy:** remove/relocate → re-frame §7.1 onto the external review of record. **Disposition:** **RESOLVED** in Commit 1 — §7.1 re-framed (in-document-table framing dropped; rule re-homed on `docs/reviews/…` per DMS §7.5; number + heading preserved; force unchanged). Raised by the three-hat stream at pass-1; the antagonistic stream's pass-1 phrase-scoped sweep missed it and confirmed it at pass-2.

#### M-2 (three-hat S-M1 / antagonistic P1-M1): defect cardinality drift in the freeze-bound record
**Remedy:** add/fix → R047 ledger + apply-prompt + PR body. **Disposition:** **RESOLVED** — "five carriers — the ADR and SDD templates, two DMS clauses, and the CSD directive clause" applied uniformly across all freeze-bound surfaces (the "three documents" roll-up that invited a recount, antagonistic P2-C1, also removed).

#### M-3 (antagonistic P1-M2): §31.6 mis-citations + Phase-5b checklist incompleteness
**Remedy:** add/fix → ledger + close-records handoff. **Disposition:** **RESOLVED** by relocating the ledger in-PR (Commit 2, §31.9); all values resolve at authoring time, so the §31.6 placeholder dependency disappeared and both cites were stripped, with a verify assertion (`§31.6` absent).

#### M-4 (three-hat E-M2): premature convergence claim in a shipping artifact
**Remedy:** add/fix → PR body. **Disposition:** **RESOLVED** — PR-body Verification now points to this vendored review-of-record for the outcome rather than pre-filling it.

#### M-5 (antagonistic P2-M1): the §7.1 ratification was asserted in the ledger but not substantiated in the trail
**Remedy:** add/fix → HEB-45 Linear trail + title/banner. **Disposition:** **RESOLVED** — three-layer capture completed: an explicit ratification comment naming the §7.1 carrier, the §31.9 restructure, and the CSD bump; the title updated to the five-carrier scope; the branch regenerated to match; the description defect-section + acceptance criteria refreshed. The ledger's "per-item ratified" claim is now true at freeze.

#### M-6 (antagonistic P2-M2): the ledger froze (Commit 2) before the named coherence gate
**Remedy:** add/fix → apply-prompt phase sequencing. **Disposition:** **RESOLVED** — PAUSE-POINT 1 is now the coherence gate, scrutinising the ledger + review staging files *before* Commit 2 freezes them; PAUSE-POINT 2 documents the §31.7 freeze semantics (pre-push `git commit --amend` is compliant — one ledger commit in the durable history; a post-push finding routes to the comment trail per §31.7). See §2.5.

#### M-7 (three-hat E2-M1): the review-of-record was an unauthored load-bearing artifact
**Remedy:** add/fix → author the RoR. **Disposition:** **RESOLVED** — this review-of-record, authored at convergence and updated after the runtime sandbox, calibrated per §7.5.2.

#### M-8 (§11.7.4 sandbox SB-1): locale-dependent staged-set sort — a conditional execution-blocker
**Remedy:** add/fix → apply-prompt §2.3 / §3.3. **Location:** the staged-set verification `git diff --cached --name-only | sort`. **Description:** the staged-set check compares a `sort`ed path list byte-for-byte to a C-ordered EXPECT string. Under the macOS executor's default `en_US.UTF-8`, `sort` collates case-insensitively (`c < d < p < v`), interleaving the `docs/*` paths between the uppercase root files — so `[ "$STAGED" = "$EXPECT" ]` is false → RED → abort at Commit 1. Demonstrated deterministically (the Linux sandbox could not run macOS BSD `sort`'s collation directly, so the trigger is conditional on the executor's `sort` honouring the locale; the fix removes the variable regardless). **Disposition:** **RESOLVED** — `LC_ALL=C sort` pinned on both staged-set checks (§2.3, §3.3); the sandbox re-run matches EXPECT deterministically. This is the recurring "static convergence then runtime reopening with a blocker" pattern; the runtime pass earned its keep.

### 2.3 COSMETIC findings — noted

Resolved cosmetics (recorded for the trail): antagonistic P1-C1/m-1 (§1.3 baseline block AMBER→RED), P1-C3/m-3 (RBT-47 framing relocated to "Forward / cascade," "not a Bedrock-side gate"), P2-C2 (§7.1 now cites `per DMS §7.5` — cite-not-restate), three-hat L-C1 (both harmonised bullets counted in §2.2), the redundant §2.2 dangling-pointer `for probe` loop (collapsed to a single `if`), and the stale "matched pair" description body (refreshed to "matched set — five carriers").

- **Dangling-pointer guard is intentionally scoped to title-bearing danglers** (antagonistic P2-C3) — broadening to a bare `→ §N` guard was considered and **rejected with rationale**: §7/§8/§9 are reused with new meanings post-renumber, so a bare-number guard would false-RED. The apply-prompt now documents this inline. Forward-robustness broadening (if ever wanted) is noted for apply-prompt-template hardening. **none.**
- **§31.9(d) placeholder guard is full-body** (three-hat L2-C1) — broader than §31.9(d)'s metadata-field scope; clean for this ledger; an explanatory narrowing note is in-place. **none.**
- **HEB-45 description "Scope/deliverables" + "Open scope calls" retain pre-settlement phrasing** — the authoritative current state lives in the title, defect section, acceptance criteria, and comments; per the banner-prefix pattern the body brief is not fully rewritten. **none** — operator hygiene only; touches nothing freeze-bound.

### 2.4 No-drift confirmations (positive findings)

Static (dual-stream) and runtime (sandbox) confirmations, so future passes need not re-derive them. Where both streams independently confirmed a fact, it is doubly grounded.

- **Carrier set is complete — no sixth carrier** *(both streams; three-hat S2-P2 / antagonistic P-1).* Independent adjacent-vocabulary sweeps surface no further carrier in the HE-Bedrock master. Every other review-vocabulary hit is the external review-of-record home, an already-correct ally routing review external (DMS §2.3.4/§2.3.5 reviewer-row strips — §2.3.5 states review accountability "lives in PR-merge process and the ruling-rationale ledger… not in document metadata"; §7.5; §2.3.1; DDR template), or an unrelated concern.
- **Reference-preserving, verified by live grep** *(both streams; S-P1 / P-3).* Zero by-number citations of ADR §7/§8/§9, SDD §9–§12, DMS §4.4, or CSD §7.1 anywhere — the only `§7.1` hit is the CSD heading itself; every `§4.4` hit is another document's own §4.4.
- **str_replace anchors present, unique, byte-exact @ `a3b8a70` — mechanically confirmed in the sandbox** *(both streams + runtime; L2-P1 / P-4).* All eight edits (E1/E2/E3 · C1/C2 · P1/P2/P3) matched `old_str` exactly once and applied, including every § / — / … / `'`.
- **Unicode-bearing verify greps match real bytes** *(runtime).* The §2.2 `grep -F` for `PROPOSED→ACCEPTED` (arrow) and `docs/reviews/…` (ellipsis) + `per DMS §7.5` matched the vendored files under `bash` — closing the prior byte-identity worry empirically.
- **Git mechanics clean under sandbox** *(runtime).* Commit-1 (7 paths) and Commit-2 (3 paths) staged sets match their EXPECT strings under `LC_ALL=C`; commit count = 2; `git diff main..HEAD --name-only` = exactly the 10 expected paths; `mktemp -t` + heredoc + `git commit -F` preserves multi-paragraph blank-line structure and Unicode (the `-m` collapse trap is avoided).
- **MINOR tier holds** *(both streams; E-P1 / P-9).* Removal + renumber is reference-preserving; existing decision records are grandfathered-until-touched (DMS §7.9), so no prior-conformant artifact becomes non-conformant. kit 2.5.0→2.6.0, DMS 3.2.0→3.3.0, CSD 3.3.0→3.4.0 — ratified.
- **§7.1 re-frame is sound** *(three-hat S2-P1).* Faithfully translates "empty is correct" into the external model, preserves the anti-fabrication force (extended to fabricating "a review-of-record itself"), cites DMS §7.5 rather than restating it, and is consistent with §7.3/§7.4/§7.5.
- **Byte-parallelism of harmonised Cross-References bullets holds** *(both streams; L-C1 / P-6).* The DIRECTIVE-034 grounding bullet and the review-of-record bullet are byte-identical across ADR/SDD/DDR (one each; no duplicates), counted by the §2.2 verify.
- **Fix-induced-drift trap caught** *(both streams; L-P1 / P-7).* The ADR §6 Compliance pointer `(→ §7)` was rewritten to `(→ the external review of record…)`; the renumber introduced no dangling reference.
- **§31.9 ledger-in-PR satisfied; ledger freeze-ready** *(both streams + runtime; E2-P1 / P-8).* Ledger vendors in the work PR (Commit 2), single-layer per §31.2.1, enumerates R047 with R048 ID-claimed-and-forward-pointed, no unfilled placeholders (sandbox-confirmed), no `§31.6`.
- **§4.4 RESERVE drops no load-bearing function** *(antagonistic P-10).* Multi-version history is served by the `## Change Log` + the external review-of-record; RESERVE form matches the §4.9 precedent byte-for-byte; no §4.x tail renumber — deferred to HEB-46.
- **Loophole closure is structural, not cosmetic** *(antagonistic P-11).* Post-strike, an in-document review section is no longer a blessed surface — the §7.7 test evicts it; §4.4 no longer prescribes it; §7.1 no longer presupposes it.
- **Contract-purity lens (§7.2.1) on the changed surfaces — clean.** The new Cross-References bullets are relocation pointers in the cross-reference home; the re-framed §7.1 points review history *to* `docs/reviews/` per §7.5; no template body gained a concrete operational ID.
- **Cross-stream asymmetry — the dual-stream design earned its keep.** The three-hat stream caught the §7.1 fifth carrier a pass before the antagonistic stream. The antagonistic stream caught the §7.1 ratification-capture gap (M-5), the §7.1-restates-§7.5 nuance, and the freeze-sequencing severity (M-6) that the three-hat stream had under-weighted. And the runtime sandbox caught SB-1 (M-8), which neither static stream surfaced. No single lens would have produced this gate.

### 2.5 Normative interpretations dispositioned

- **§31.7 "freeze at commit time" = the durable/pushed record.** A pre-push `git commit --amend` on the ledger's Commit 2 is §31.7-compliant because the durable history retains a single ledger commit; a finding arriving after push routes to the work-item comment trail per §31.7. **Disposition:** folded into the apply-prompt PAUSE-POINT 2 freeze-semantics note; ratified.
- **CSD §7.1 re-frame is MINOR under DMS §4.6.** Preserves the section number, breaks zero by-number references, and (enforcement being touch-time per §7.9) makes no prior-conformant artifact non-conformant. **Disposition:** ratified in the HEB-45 trail.

---

## §3 Forward-Pointer Triage

### Candidate HEB-46 (already filed) — DMS §4.x RESERVED-marker collapse + tail renumber
**Source:** §4.4 RESERVE (M-2 carrier 2) + antagonistic P1-C4. **Proposed disposition:** tracked — HEB-46 exists (related-to HEB-45); collapse + renumber at the next MAJOR DMS touch.

### Candidate (optional) — broaden the dangling-pointer regression guard in the apply-prompt-template
**Source:** antagonistic P2-C3 / §2.3. **Description:** a future apply-prompt-template could carry a renumber-aware guard. For HEB-45 the bare-`→ §N` broadening was correctly rejected (the numbers are reused). **Proposed disposition:** fold into a future apply-prompt-template hardening (sibling to HEB-35) or accept the current scoped guard.

### Forward-pointer triage summary

| Proposed ID | Summary | Disposition |
|---|---|---|
| HEB-46 | DMS §4.x RESERVED collapse + tail renumber | Filed; deferred to next MAJOR DMS touch |
| (optional) | Renumber-aware dangling-pointer guard in apply-prompt-template | Fold into apply-prompt-template hardening or accept current scoped guard |
| (operator) | Refresh the HEB-45 description "Scope/Open-calls" body to current state | Non-freeze-bound hygiene; optional |

---

## §4 Audit Outcome

> **PASS WITH FINDINGS.** Across both static streams (three-hat ×4, antagonistic ×2) and the §11.7.4 sandbox runtime pass: **0 BLOCKING, 0 MATERIAL open** — every material finding (M-1 through M-8) dispositioned and resolved before this gate; remaining items are COSMETIC (no-action) or out-of-scope forward-pointers. The five-carrier edit set is sound, the carrier set is independently confirmed closed at governance-corpus scope, every change is reference-preserving (live-grep + sandbox confirmed), the freeze-bound ledger is accurate and substantiated by the ratification trail, and the apply-prompt executes cleanly in the mock (after the SB-1 `LC_ALL=C` fix).

**Gate status.** The static dual-stream gate (§11.7) **and** the §11.7.4 sandbox runtime pass are **satisfied**. Commit 1 (the five-carrier kit amendment) lands as-authored; Commit 2 freezes the R047 ledger and co-vendors this review-of-record + the antagonistic substrate. PR = 10 paths across 2 commits.

**Explicitly not certified (CSD §7 blind-spot doctrine).** Zero open findings is not a zero-defect certification. Not exercised in the sandbox (environment-coupled; logic reviewed statically): the identity / `verify-repo-state.sh` / baseline-SHA pre-flight, the push and `gh pr create` legs, macOS BSD `sort`'s actual locale behaviour (Linux sandbox — SB-1's fix is robust regardless), and true bash-3.2 (the sandbox ran bash-5.x; the blocks use no bash-4+ features).

---

## §5 Cross-References

- **Authority:** DIRECTIVE-007 (Multi-Role Review) + DIRECTIVE-032 (Antagonistic Review), dual-stream; DIRECTIVE-026 (tier discipline). §11.7 / §11.7.4 gate.
- **Ruling rationale:** `docs/ruling-rationale/2026-06-28-heb-45-review-record-template-fix-rulings.md` (R047 — the "why," not restated here; freezes in Commit 2 per §31.7).
- **Antagonistic stream record (co-vendored, Commit 2):** `docs/reviews/2026-06-28-heb-45-antagonistic-review-combined-pass1-pass2.md` (verbatim per §7.4).
- **Documents reviewed:** the five-carrier edit set (ADR/SDD/DDR templates, DMS, CSD), VERSION, PROVENANCE, the apply-prompt, the R047 ledger; HEB-45 Linear trail; Notion (no separate R047 page).
- **Work item:** HEB-45. **Source:** HEB-38 (Phase-3 cascade scan). **Spawned:** HEB-46. **Re-cascade:** HEB-12. **Sequential sibling ruling:** R048 (Reboot adoption, authored at the push).
- **Sibling review:** the HEB-38 Phase-2 convergence review-of-record (same dual-stream discipline).
- **Baseline:** HE-Bedrock `main` @ `a3b8a70`.

*End of HEB-45 dual-stream review-of-record.*
