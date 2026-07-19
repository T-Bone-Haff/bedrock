# File: docs/ruling-rationale/2026-06-25-heb-38-phase-1-contract-purity-rulings.md
# Author: Claude (claude.ai authoring under DIRECTIVE-026; close session 2026-06-25)
# Created: 2026-06-25
# Description: Ruling-rationale ledger for the 2026-06-25 HEB-38 Phase-1 cycle — the contract-purity /
#              standalone-buildability doctrine landed into the HE-Bedrock kit (DMS 3.1.0->3.2.0,
#              CSD 3.1.0->3.2.0, ADR/DDR/SDD/review templates) via PR #21. Captures three
#              ruling-bearing decisions (R040-R042) per DIRECTIVE-031 §31.2, arising during Phase-1
#              authoring + the Pass-1..Pass-4 review cadence + execution. Frozen at commit per §31.7.
# Revised: 2026-06-25 (HEB-38 Phase-1 close)

# Ruling-Rationale Ledger — HEB-38 Phase-1: contract-purity / standalone-buildability doctrine

## 0. Header

| Field | Value |
|---|---|
| **Anchor work item** | HEB-38 (Governance Starter Kit) — Phase-1 |
| **Session** | 2026-06-25 (claude.ai authoring + Pass-1..Pass-4 review oversight + execution close, under DIRECTIVE-026) |
| **Author** | Claude (claude.ai authoring; close session 2026-06-25) |
| **main SHA baseline** | `6d5091c` (close-PR base = post-merge `main` tip; squash of work PR #21; main-only — rebind of develop-SHA per DMS §2.3.4.1). Work authored against `49b4c17a`. |
| **Governance baseline** | DMS v3.1.0->3.2.0 · CSD v3.1.0->3.2.0 · ADR/DDR/SDD/review templates amended · ENG-STD-003 v3.0.1 · **kit VERSION 2.3.0->2.4.0 · corpus tag v2.4.0** (MINOR — additive/reference-preserving, no consumer breakage; R038 grandfather-until-touched keeps the new doctrine from making prior-conformant artifacts non-conformant; ratified 2026-06-25). The release rides this close PR. |
| **Status** | Captured at close; vendored in the HEB-38 Phase-1 close PR. Frozen at commit per DIRECTIVE-031 §31.7. |

*Two-layer ledger (DIRECTIVE-031 §31.2.1): §1 inventory + §2 detail blocks. Ruling IDs R040-R042 continue the global sequence and are **confirmed free** against live `docs/ruling-rationale/` (repo frozen max R034) and the Notion HEB-38 Phase-0 ledger (max R039, `389caeea`, 2026-06-24). These rulings postdate the frozen Phase-0 design ledger and do not amend it (§31.7). **ID-sequence caveat (see Forward Pointers):** the live check surfaced a pre-existing **R032-R034 duplicate-ID collision** between the repo `2026-06-18-heb-9-sofia-reboot-deploy` ledger and the Notion Phase-0 ledger; remediated by accept-and-disambiguate (both frozen per §31.7). Within this ledger, every `R032`-`R039` reference denotes the **HEB-38 Phase-0** ledger.*

## 1. Rulings Inventory

| ID | Subject | Disposition class |
|---|---|---|
| R040 | §4.6 trigger unification — MAJOR/MINOR/split key uniformly on SemVer-compatibility; reference-preserving structural reorg/renumber is MINOR | Versioning / classification doctrine |
| R041 | Remedy axis is total — positive (no-drift) findings carry remedy `none` by default | Review-model doctrine |
| R042 | Per-section content-contracts persist through promotion — only the AUTHORING GUIDANCE block is deleted | Template / doctrine lifecycle |

## 2. Ruling Detail

### R040 — §4.6 structural-trigger SemVer-compatibility unification

- **Ruling.** §4.6's MAJOR / MINOR / split-trigger classification keys uniformly on **SemVer-compatibility**. A change is MAJOR **iff** it breaks a downstream reference or makes a prior-conformant artifact non-conformant. Reference-preserving structural reorganization or section renumbering is **MINOR**, whether standalone or riding with additive work; content-preserving consolidation rides MINOR or stands alone as PATCH. The categorical "structural reorganization / renumbering → MAJOR" proxy is removed.
- **Disposition.** Versioning / classification doctrine (extends R037).
- **Rationale.** R037 (Phase-0) reclassified content-preserving *consolidation* by semantic effect but left §4.6's structural-reorganization/renumbering triggers categorical-MAJOR. Phase-1's own B-1 fix — the ADR §8→§9 Change-Log renumber forced by the new `## 8. Cross-References` section — is reference-preserving: MINOR by the section's compatibility logic, MAJOR by the unchanged structural-trigger text. That internal contradiction (surfaced Pass-2, refined Pass-3) is resolved by unifying every §4.6 trigger on the invariant compatibility property. Under-signaling is the worse failure mode: a reorganization that bumps only PATCH tells a consumer "don't look" when the document's shape actually changed — so a reference-preserving structural change rides MINOR, not PATCH.
- **Alternatives rejected.**
  - *Option B — route standalone reference-preserving structural reorg to PATCH* (parallel to consolidation): rejected — under-signals a reshape a reader must re-learn; MINOR gives the warranted glance.
  - *Leave §4.6 split* (consolidation by semantic effect; structural categorical-MAJOR): rejected — preserves the contradiction (the renumber is both MINOR and MAJOR).
- **Primary sources verified.** Live DMS §4.6 + §H tier logic (as amended, 3.2.0; read this session); Phase-0 R037 (Notion ledger `389caeea`); HEB-38 Pass-2 / Pass-3 reviews of record (B-1 / P2-B1).
- **Other.**
  - *Ratification venue:* claude.ai session 2026-06-25 — Pass-2 Option (a) (unify on compatibility); Pass-3 B-1 Option A (standalone reference-preserving structural reorg/renumber → MINOR, final form).
  - *Relationship to R037:* refines, does not amend — R037 is frozen (§31.7); R040 extends its semantic-effect principle to the structural triggers on the forward trail.
  - *Forward:* structural-reorg visibility nudge — a lint flagging structural reorganization inside MINOR PRs, restoring the visibility the categorical-MAJOR proxy used to provide. Deliberate-first; DIRECTIVE-025 dedup first.

### R041 — Remedy axis is total; positives default to `none`

- **Ruling.** The DIRECTIVE-007 §7.2 remedy axis is **total** over all findings. Every finding carries a remedy tag valued **add/fix**, **remove/relocate**, or **none**; `none` is the **default** — a finding carries `none` unless it asks for an add/fix or a remove/relocate. A §2.4 no-drift confirmation (positive finding) asks for nothing and therefore carries `none`, with no explicit tag required.
- **Disposition.** Review-model doctrine (extends R036 remedy axis).
- **Rationale.** R036 (Phase-0) introduced the orthogonal remedy axis (add/fix vs. remove/relocate) on the shared findings model. Phase-1 review (Pass-4) surfaced a three-surface inconsistency on whether a positive finding carries a tag: the CSD remedy block said "every finding" does, while a no-drift confirmation asks for nothing. Making the axis total with `none` as the default keeps the "every finding" universal literally true (no "actionable-only" carve-out or boundary to police), defines the axis as a total function with a bottom value, and matches the doctrine's own "naming what the finding asks for" qualifier — a confirmation asks for nothing.
- **Alternatives rejected.** *Exempt positives entirely* ("every **actionable** finding carries a tag"): rejected — requires a carve-out plus an "actionable finding" boundary definition; the `none`-default is more consistent and leaves the universal quantifier intact.
- **Primary sources verified.** Live CSD DIRECTIVE-007 §7.2 (as amended, 3.2.0; read this session); live review template §2 (§2.3 cosmetic-bullet remedy tag present; §2.4 positives untagged); Phase-0 R036 (Notion ledger `389caeea`).
- **Other.**
  - *Ratification venue:* claude.ai session 2026-06-25 — Pass-4 M-1 reconcile.
  - *Empirical floor:* single-cycle edge (positives); the rule is a closed-form clarification of an existing axis, not threshold-gated.

### R042 — Per-section content-contracts persist through promotion

- **Ruling.** The per-section content-contract HTML comments in the ADR/DDR/SDD templates **persist** in the authored instance through promotion — they are not author-time scaffolding to be deleted. Only the top-of-template `AUTHORING GUIDANCE` block (which carries the content-contracts *explainer*) is removed at the draft→PROPOSED boundary. The per-section `<!-- Contract — holds … Not … -->` comments remain as ongoing per-section discipline, invisible in render.
- **Disposition.** Template / doctrine lifecycle.
- **Rationale.** The per-section contracts are cheap to keep (HTML comments, no reader-facing cost) and they carry the §7.7 contract-purity discipline forward to amendment time, when a future amender sees the contract and respects it. DMS §7.8 ("an authored body conforms to its template's content-contracts") reads the contracts as a live reference for the authored body, not only the blank template. As landed, the per-section comments sit **outside** the AUTHORING-GUIDANCE delete scope, so they persist by construction; this ruling makes that intent explicit rather than implicit-by-silence.
- **Alternatives rejected.** *Remove-at-promotion* (treat the per-section contracts as scaffolding like the guidance block): rejected — loses the amendment-time discipline; the contract would then live only in the template, not the instance, and the doctrine would owe an explicit removal instruction it does not currently carry.
- **Primary sources verified.** Live DMS §7.8 (as amended, 3.2.0; read this session); live ADR/DDR/SDD templates (per-section comments under each body heading, outside the AUTHORING-GUIDANCE block); the AUTHORING-GUIDANCE "DELETE THIS BLOCK BEFORE PROMOTION TO PROPOSED" scope.
- **Other.**
  - *Ratification venue:* claude.ai session 2026-06-25 — post-execution Q&A.
  - *Forward:* §7.8 should state the lifecycle explicitly (one line: per-section content-contracts persist; only the guidance block is deleted at promotion) — a content-preserving §7.8 touch on a future cycle, MINOR per R040 (reference-preserving).

---

*Forward pointers (carry-forward — not rulings):*

- *§1.7 reduced-form guard false-RED = re-instance of **R027** (HEB-9 Phase-1, frozen repo ledger): reduced-form absence assertions must be surface-scoped / fence-stripped, never full-body greps on a self-describing governance document. The HEB-38 apply-prompt's guard regressed from R027; the fence-strip fix **applies** R027, it does not re-rule it. **R026** (reduced-form PostVerify N/A) likewise governs the §0.4.2 disposition. Forward action: codify R027's surface-scoping into ENG-STD-003's reduced-form-assertion guidance so apply-prompt guards stop regressing (candidate hardening; deliberate-first, DIRECTIVE-025 dedup).*
- ***HEB-24** (reduced-form-master rebind ADR) now carries a concrete data point — comment posted 2026-06-25: the DMS §2.3.4.3 "every control document carries a `## Change Log`" rule is unsatisfied by HE-Bedrock's own reduced-form-master DMS/CSD, the deviation HEB-24 is queued to capture.*
- **Corpus-release item (RESOLVED 2026-06-25):** HEB-38 Phase-1 amended corpus docs (DMS, CSD) → a corpus release is owed per the HEB-9 R022/R023 precedent. Classified **MINOR**: kit `VERSION` 2.3.0→2.4.0, annotated corpus tag **v2.4.0**, `PROVENANCE.md` refreshed (kit 2.4.0 · DMS 3.2.0 · CSD 3.2.0). The release rides this close PR (the work PR #21 omitted it). **Learning:** the work apply-prompt's manifest did not carry the corpus-release step despite amending corpus docs — ENG-STD-003 / the apply-prompt template should require a release step (VERSION + PROVENANCE + tag) whenever a corpus document is amended. Candidate codification; deliberate-first.
- ***Ruling-ID-sequence integrity (surfaced this cycle):*** *a pre-existing **R032-R034 duplicate-ID collision** — the frozen repo `2026-06-18-heb-9-sofia-reboot-deploy` ledger defines R032/R033/R034 (skill-delivery surface / decision-record authoring division / close-records destination), while the frozen Notion HEB-38 Phase-0 ledger (2026-06-24) independently defines R032/R033/R034 (reference-purity / surface enumeration / doctype scope). Phase-0 opened its counter at R032 when the global max was already R034. Remediation (ratified 2026-06-25): **accept-and-disambiguate** — both ledgers stay frozen (§31.7); collided IDs are cited by ledger-of-origin; recorded on the HEB-38 trail and a dedicated ticket. R040-R042 are unaffected (above both maxes).*
- ***ID-registry (root-cause forward action):*** *stand up a single authoritative ruling-ID registry as the global next-free-ID source of truth, so per-ledger assignment ("verify against prior max") cannot fork again across venues (repo `docs/ruling-rationale/` + Notion design ledgers). New ticket; deliberate-first; DIRECTIVE-025 dedup first.*
- *§0.2 apply-prompt cold-read narrative read "two passes" — the cycle ran four (Pass-1→Pass-4); narrative-only, no executable impact.*
- *DIRECTIVE-032 → §7.2 findings-model wiring (Pass-2 carry); HEB-39 ENG-STD-002/-003 reference-purity analogue (Phase-0 R034). All deliberate-first, DIRECTIVE-025 dedup first.*

*Substrate note: the claude.ai authoring leg ran under an intermittent Filesystem MCP (unresponsive mid-session; restored before ID verification). Live corpus exemplars and the merged-state verification were fresh-fetched in-session; the §31.2 schema was cross-checked against the project-mounted CSD copy (byte-equivalent for the unamended DIRECTIVE-031 §31.2). Ruling IDs R040-R042 confirmed free against live `docs/ruling-rationale/` (repo max R034) and the Notion Phase-0 ledger (max R039); the R032-R034 collision noted above was surfaced by that same check. The kit-VERSION / corpus-tag baseline is resolved: MINOR, 2.4.0 / v2.4.0 (see governance baseline + corpus-release pointer).*

*End of HEB-38 Phase-1 ruling-rationale ledger.*
