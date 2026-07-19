# File: ~/Downloads/heb-38-phase-2-enforcement-edits.md
# Description: HEB-38 Phase-2 staging file (CONVERGED — post three-hat + antagonistic review) — the verbatim
#              committed text for the contract-purity ENFORCEMENT surfaces landing into the HE-Bedrock kit:
#              the DIRECTIVE-007 §7.2.1 standing contract-purity review lens, the DIRECTIVE-023 check-spec
#              (surface-scoped + concrete-ID-anchored), the review-template §2 lens integration + R041
#              none-default correction, and the version/release surfaces (CSD 3.2.0->3.3.0; kit 2.4.0->2.5.0;
#              PROVENANCE; corpus tag). Tier-1 artifact (DIRECTIVE-026) — vendored by the Phase-2 work apply-prompt.

# HEB-38 Phase-2 — Enforcement staging edits (CONVERGED)

**Anchor:** HEB-38 (Governance Starter Kit) — Phase-2 (enforcement).
**Baseline:** HE-Bedrock `main` @ `28a496a` (main-only; kit VERSION 2.4.0; CSD 3.2.0; DMS 3.2.0).
**Surfaces landed:** the two ratified DMS §7.7 delivery surfaces — the *review findings model* (here landing its **active-read leg**; the remedy-axis leg landed Phase-1) and the *CI reference check* (grep check-spec). The skill-nudge surface is Phase-4; the running grep mechanization is Phase-2.5 / HEB-36.
**Keystone (ratified):** the standing lens folds into **CSD DIRECTIVE-007 §7.2** as a new sub-subsection **§7.2.1**, co-located with the remedy axis it extends — **not** a standalone §7.6. The §7.2 remedy-axis surface *is* the DMS §7.7 "review findings model" delivery surface; no DMS §7.7 enumeration touch is owed, and no DMS edit is pulled into Phase-2.
**Reduced-form note:** HE-Bedrock's CSD is reduced-form master (HEB-24) — `doctype` + `version` only, no `## Change Log` / `# Revised` / `last_updated`. CSD bumps **only** YAML `version:`. §13.5.8 PostVerify atomic-refresh pairs are **N/A per R026** (reduced-form). *(R026 cited from recall — confirm the attribution at apply-prompt authoring per the fresh-fetch discipline; the underlying logic — a reduced-form doc has no `last_updated` / `## Change Log` surface to pair-refresh — holds regardless.)* The footer marker is a confirm-no-version surface, never mutated.
**Rulings to claim (close-records PR):** from **R043** — global max R042; re-verify across repo `docs/ruling-rationale/` + Notion at close (HEB-41 discipline). R043 = the §7.2.1 active-read lens as an extension of R036 (remedy axis). The §24.1↔§7.4 seam is **not** a Phase-2 ruling — it routes to a new dedicated §7-jurisdiction / DIRECTIVE-024-refinement ticket (see Scope ledger), explicitly **not** HEB-39.

> **Anchor-fidelity note.** The OLD-anchor verbatim text in the str_replace/insert blocks below is drawn from the live `28a496a` reads this session. Per ENG-STD-003 §13.5.2 step 5, the Phase-2 apply-prompt does the final tactical fresh-fetch verification of every OLD anchor (and the §7.2 insert-after anchor) against current file state before finalization. If `main` has moved at apply-prompt-authoring time, re-anchor per **§13.5.2** (the §13.5.10 temporal-coordinate gate governs the distinct substrate-time→execution-time gap at the Claude Code venue, not authoring-time re-anchoring).

---

## Rebuild notes — reviewer findings folded (from the reviewed staging file → this converged cut)

This file supersedes the pre-review staging file. Changes, mapped to the reconciled findings:

- **Keystone (Option 1 — three-way structural converge: P1-M1/P1-M2/P1-M8 + A-B2/A-M1/A-C1).** The lens moves from a standalone `#### 7.6` to a numbered `##### 7.2.1` under §7.2. This collapses: the restatement BLOCKER (A-B2), the standalone-vs-fold form question (P1-M1), the §7.2/§7.6/§7.7 surface-identity (A-M1 — §7.2 is the §7.7 review-findings-model surface), the §7.6↔DMS-§7.6 coordinate collision (A-C1, dissolved), and the cross-review-type scope (P1-M8 — §7.2.1 inherits §7.2's review-type enumeration).
- **Restatement strip (A-B2 / P1-M2).** §7.2.1 references the DMS §7.7 test and §7.2's subtractive loop; it renders neither. The kept increment is the *detection* obligation (an active per-section read that *raises* findings), distinct from §7.2's *tagging* of findings already raised.
- **Block 2 spec (P1-M3 + A-M2).** The surface-scoping paragraph now states the matcher is **concrete-ID-anchored** (instantiated forms only) so it does not false-RED on §7.4's / this directive's own teaching tokens (A-M2), and names the mechanized classes as a **deliberately-closed subset** of §7.4's explicitly-open prohibited set (P1-M3). The §7.6 pointer retargets to §7.2.1.
- **Blocks 4 + 5 cite retarget (keystone ripple) + C-1.** The review-template integration line and the §2 contract comment retarget §7.6 → §7.2.1; the contract comment now says §2 holds *findings from* the lens, not the lens itself (Pass-1 C-1).
- **Versioning rationale (A-M4).** The false "no prior-conformant artifact becomes non-conformant" basis is replaced with the DMS §7.9 grandfather-until-touched + aspirational-status basis (the real reason MINOR holds).
- **C-2.** The anchor-fidelity note's `§13.5.10` re-anchor cite is corrected to `§13.5.2`.
- **C-3 / my #3.** R026 verify-at-apply-prompt note added (above). The review-template §2.1/§2.3 per-finding remedy placeholders remain two-valued (`{{add/fix | remove/relocate}}`) **by design** — `none` is the positive default, carried untagged in §2.4 — confirmed-intended, no change.

**Pass-2 round (converged-cut review — three-hat + antagonistic; both PASS WITH FINDINGS, no BLOCKING, Pass-1 blockers verified cleared):**

- **§24.1 re-route (A2-M2 / P2-1 — two-way converge).** The §24.1↔§7.4 seam routes to a new dedicated §7-jurisdiction / DIRECTIVE-024-refinement ticket, **not** HEB-39 (jurisdiction mismatch — HEB-39 is the scripts/apply-prompts analogue; this seam is governance-doc-internal). Block 2 note + Scope ledger updated; ticket-create added to queued captures.
- **Block 4 gloss trim (A2-M1, trim-(a) ratified).** The review-template §2 integration paragraph trimmed to a bare reference (`per DIRECTIVE-007 §7.2.1 / DMS §7.7.`), removing the one-line gloss that re-described §7.2.1. Standing convention: prose delivery surfaces reference, don't gloss.
- **§7.2.1 form affirmed (A2-C2 / P2-2 — converge).** Lone-numbered-child shape ratified as-is (citeability rationale); authoring note updated.
- **A2-C1.** "Surfaces landed" framing tightened — Phase-2 lands the *active-read leg* of the §7.2 review-findings-model surface, not the whole surface.
- **A2-C3.** §7.2.1 closing self-claim (`It references the §7.7 test; it does not restate it`) trimmed — the reference already establishes it; the self-claim was faint construction-narrative (dogfood the doctrine one level deeper).
- **P2-3 (sequencing confirm).** HEB-36 broaden sequenced into Phase-2 close so the descriptive "kit-level-validator work item" reference resolves to a real owner (noted in queued captures).

---

## Block 1 — CSD-7.2.1-LENS  (insert)

**Target:** `CLAUDE_SESSION_DIRECTIVES.md`, DIRECTIVE-007, §7.2.
**Edit type:** insert a new sub-subsection `##### 7.2.1` at the tail of §7.2 — after the `POSITIVE findings are required` paragraph and **before** the `#### 7.3 Iterative refinement of diagnosis` heading. (No `---` separates §7.2 from §7.3; the insert is between the §7.2 tail paragraph and the §7.3 heading.)
**Insert-after anchor (verbatim tail of §7.2):**

```
This is the audit-trail substrate that prevents future audits from re-doing the work.
```

**NEW text to insert (immediately after the anchor line, preceded by one blank line):**

```markdown
##### 7.2.1 Standing contract-purity review lens

The remedy axis (§7.2) tags the direction of a finding already raised; it does not detect. This lens supplies the detection: every review pass over a morphing body (DMS §7.5) carries a standing, per-section obligation to apply the DMS §7.7 contract-purity test as an active read, raising a **remove/relocate** finding (§7.2 — naming its audit-surface home, DMS §7.5) for process-narrative or restatement that belongs on an audit surface rather than in the body. It is what makes §7.2's subtractive loop fire by construction — not only when a reviewer happens to look — across the review types §7.2 binds.
```

> *Authoring note (not committed text). Form: §7.2.1 is the first numbered sub-subsection under §7.2; the existing §7.2 bolded-paragraph leads remain the section body. Chosen over an unnumbered `**Standing contract-purity lens.**` paragraph because the review-template integration line (Block 4) and §2 contract comment (Block 5) need a stable citeable anchor (`§7.2.1`) to reference — the DMS §7.7 referenceability principle applied to the lens. **Ratified as-is (Pass-2 affirm — both passes lean affirm on the citeability rationale.)** The heavier alternative (number all §7.2 leads) is a reference-preserving MINOR carry-forward, out of Phase-2 scope, only if the asymmetry later grates.*

---

## Block 2 — CSD-D023-CONTRACT-PURITY  (str_replace)

**Target:** `CLAUDE_SESSION_DIRECTIVES.md`, DIRECTIVE-023.
**Edit type:** `str_replace` — extend the check set with one bullet and append the surface-scoping / concrete-ID-anchoring / disposition paragraph after the aspirational clause.

**OLD (verbatim):**

```markdown
- Frontmatter schema conformance for typed documents (ADR, DDR, SDD, session-handoffs)

Failures block the PR. Manual fixes land before CI passes; ad-hoc CI bypass is prohibited.

Where the CI enforcement does not yet exist, compliance is aspirational with a backlog item tracking enforcement-mechanization (per §24.1); until that lands, conformance is reviewed at PR time.
```

**NEW:**

```markdown
- Frontmatter schema conformance for typed documents (ADR, DDR, SDD, session-handoffs)
- Contract-purity reference conformance per DMS §7.4–§7.7 — within a morphing body (DMS §7.5), operational-substrate identifiers (ruling-ledger `R{N}`, tracker `{{TRACKER_PREFIX}}-NN`, review-finding `B-N`/`M-N`) MUST NOT appear inline; their one home is an append-only audit surface (DMS §7.5).

Failures block the PR. Manual fixes land before CI passes; ad-hoc CI bypass is prohibited.

The contract-purity check is **surface-scoped** and **concrete-ID-anchored**. It operates on the fence-stripped normative body and excludes the document's own audit surfaces (`## Change Log`, the designated cross-reference home) and the audit-surface doctypes whole (ruling-rationale ledgers, reviews, session-handoffs). It matches **instantiated** identifiers only (`R\d+`, `{{TRACKER_PREFIX}}-\d+`, `B-\d+`/`M-\d+`) — not the schematic or teaching-token forms (`R{N}`, `B-N`) that appear in DMS §7.4's prose and in the bullet above — so the check does not false-RED on the doctrine's own metalinguistic mentions. The mechanized classes are a **deliberately-closed subset** of DMS §7.4's explicitly open (`not an exhaustive list`) prohibited set: the check enforces the identifier classes, DMS §7.4 remains the governing rule for the full class, and the narrative class (review / session / debate prose) is not mechanically greppable and remains with the DIRECTIVE-007 §7.2.1 lens. Load-bearing contract-or-boundary references (upstream-authority pins, `§X.Y` cross-references, conformance pointers, named-gap markers) are conformant per the DMS §7.7 test; full-body greps are prohibited.

Where the CI enforcement does not yet exist, compliance is aspirational with a backlog item tracking enforcement-mechanization (per §24.1); until that lands, conformance is reviewed at PR time. The running mechanization of the contract-purity check is tracked at the kit-level-validator work item; until it lands, contract-purity is enforced by the DIRECTIVE-007 §7.2.1 lens at PR time.
```

> *Authoring note (not committed text): the "kit-level-validator work item" is HEB-36 (Phase-2.5), referred to descriptively rather than by bare `{{TRACKER_PREFIX}}-NN` because DIRECTIVE-023 is itself a morphing body and a bare tracker ID is the class §7.4 prohibits — dogfooding the doctrine. The instance resolution (descriptive reference) is ratified. The general §24.1↔§7.4 seam — §24.1's `tracked at {{backlog item ID}}` template instructs inline ID-naming, colliding with §7.4 in any morphing body — is **routed to a new dedicated §7-jurisdiction / DIRECTIVE-024-refinement ticket** (deliberate-first, DIRECTIVE-025 dedup; created at close), not resolved here. It is **not** routed to HEB-39: HEB-39's charter is the ENG-STD-002/-003 (scripts + apply-prompts) reference-purity analogue — a different artifact class — whereas the §24.1↔§7.4 seam is a collision internal to the already-landed governance-doc doctrine (CSD DIRECTIVE-024 vs DMS §7.4), squarely §7's own jurisdiction. HEB-36's charter is broadened to own the grep-impl as a separate capture; the descriptive reference points at the correct (post-broadening) owner.*

---

## Block 3 — CSD-VERSION  (str_replace)

**Target:** `CLAUDE_SESSION_DIRECTIVES.md`, YAML frontmatter.
**Edit type:** `str_replace` — bump the sole version-bearing surface (reduced-form master).

**OLD (verbatim):**

```
doctype: control-document
version: 3.2.0
```

**NEW:**

```
doctype: control-document
version: 3.3.0
```

> Reduced-form: no `## Change Log` row, no `# Revised` line, no `last_updated`. §13.5.8 PostVerify pairs N/A per R026 (confirm attribution at apply-prompt time — see header note).

---

## Block 4 — RTPL-2-INTRO  (str_replace: lens integration + R041 none-default, single edit)

**Target:** `docs/templates/review-template.md`, §2 Findings intro paragraph.
**Edit type:** `str_replace` — fold the R041 `none`-default correction and the §7.2.1 lens integration into one touch (DMS §7.9 touch-time remediation; both land on the same paragraph).

**OLD (verbatim):**

```markdown
Findings carry two independent axes: **severity** (the §2.1–§2.4 subsection they fall under) and **remedy** (add/fix vs. remove/relocate, per DIRECTIVE-007 §7.2, tagged inline on each finding). Severity sets urgency; remedy sets direction. A remove/relocate finding names where the content goes.
```

**NEW:**

```markdown
Findings carry two independent axes: **severity** (the §2.1–§2.4 subsection they fall under) and **remedy** (per DIRECTIVE-007 §7.2: **add/fix**, **remove/relocate**, or **none** — `none` is the default, so a positive / no-drift finding carries it without an explicit tag). Severity sets urgency; remedy sets direction. A remove/relocate finding names where the content goes.

Reviews of a morphing body (DMS §7.5) additionally apply the **contract-purity lens** per DIRECTIVE-007 §7.2.1 / DMS §7.7.
```

---

## Block 5 — RTPL-2-CONTRACT-COMMENT  (str_replace)

**Target:** `docs/templates/review-template.md`, the §2 content-contract HTML comment.
**Edit type:** `str_replace` — name the none-default remedy and the standing lens in the §2 contract.

**OLD (verbatim):**

```markdown
<!-- Contract — holds: dispositioned findings by severity (§2.1–§2.4), each carrying its remedy tag (DIRECTIVE-007 §7.2). Not: the corrective content itself (→ the artifact under review); review-process meta-narrative beyond finding disposition. -->
```

**NEW:**

```markdown
<!-- Contract — holds: dispositioned findings by severity (§2.1–§2.4), each carrying its remedy tag (DIRECTIVE-007 §7.2: add/fix / remove/relocate / none-default); for a morphing body, findings from the standing contract-purity lens (DIRECTIVE-007 §7.2.1 / DMS §7.7). Not: the corrective content itself (→ the artifact under review); review-process meta-narrative beyond finding disposition. -->
```

---

## Block 6 — PROVENANCE  (str_replace ×2)

**Target:** `PROVENANCE.md`.
**Edit type:** `str_replace` — kit version + updated date; CSD pin.

**OLD-a (verbatim):**

```
**Kit version:** 2.4.0
**Updated:** 2026-06-25
```

**NEW-a:**

```
**Kit version:** 2.5.0
**Updated:** {{RELEASE_DATE}}
```

**OLD-b (verbatim):**

```
| `CLAUDE_SESSION_DIRECTIVES.md` | (root) | 3.2.0 |
```

**NEW-b:**

```
| `CLAUDE_SESSION_DIRECTIVES.md` | (root) | 3.3.0 |
```

> `{{RELEASE_DATE}}` = the apply-prompt's execution/commit date (ISO `YYYY-MM-DD`), captured at Phase 0, not hardcoded here. Expected 2026-06-25 unless execution slips.

---

## Block 7 — VERSION  (str_replace)

**Target:** `VERSION`.
**Edit type:** `str_replace` — kit release bump (MINOR; additive/reference-preserving).

**OLD:** `2.4.0`
**NEW:** `2.5.0`

---

## Block 8 — Corpus tag  (post-merge, operator)

**Annotated** corpus tag **`v2.5.0`** cut on the `main` merge commit (mirrors kit VERSION). Not a Claude Code action — DIRECTIVE-018 keeps merge + tag operator-side; surfaced in the apply-prompt's post-merge carry-forward (Phase 5b). The work PR carries the VERSION + PROVENANCE bumps (the HEB-40 release-step-in-manifest lesson; Phase-1 omitted it).

---

## Scope ledger (what this does / does not do)

**Lands:** CSD DIRECTIVE-007 §7.2.1 (active-read review lens) · CSD DIRECTIVE-023 contract-purity check-spec (surface-scoped + concrete-ID-anchored) · review-template §2 lens integration + R041 none-default · CSD 3.2.0→3.3.0 · kit 2.4.0→2.5.0 + PROVENANCE + corpus tag v2.5.0.

**Does NOT do (by phase boundary / routing):** the running grep mechanization (Phase-2.5 / HEB-36) · the skill-nudge (Phase-4) · the SOFIA-Reboot cascade (Phase-3) · T12 DIRECTIVE-032→§7.2 back-pointer, which also carries the §7.2.1 lens's antagonistic-review inheritance (separate ticket) · the **§24.1↔§7.4 general seam** (routed to a new dedicated §7-jurisdiction / DIRECTIVE-024-refinement ticket, deliberate-first — **not** HEB-39, per the Block 2 note) · the R040 structural-reorg lint and R042 §7.8 lifecycle one-liner (separate deliberate-first carry-forwards).

**Queued capture actions (each pending its own ratification, at close):** broaden + restate HEB-36 (deliberation → execution; add the contract-purity grep-impl deliverable) — sequenced into Phase-2 close so the descriptive reference resolves to a real owner (P2-3) · spin T12 to its own ticket · create the dedicated §24.1↔§7.4 / DIRECTIVE-024-refinement ticket (DIRECTIVE-025 dedup first). *(The HEB-38↔HEB-36 relation is already wired — confirmed live this session — so it has dropped off the queue.)*

**Versioning rationale (MINOR, R040):** every edit is additive or reference-preserving — a new DIRECTIVE-007 §7.2.1 sub-subsection, a new DIRECTIVE-023 check bullet + surface-scoping paragraph, a content-preserving review-template touch. No downstream reference breaks. The new DIRECTIVE-023 contract-purity check *would* render a pre-existing inline-`R{N}` body non-conformant once it runs — but the check is aspirational / not-yet-mechanized (impl rides HEB-36), and **DMS §7.9 grandfathers pre-existing documents until their first substantive touch**, so no prior-conformant artifact is made non-conformant by this landing. MINOR is grounded in the §7.9 grandfather-until-touched model, not in a claim that the check breaks nothing. CSD MINOR; kit MINOR.

*End of HEB-38 Phase-2 enforcement staging edits (converged).*
