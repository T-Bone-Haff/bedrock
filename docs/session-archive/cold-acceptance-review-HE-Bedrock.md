# HE-Bedrock — Independent Cold Acceptance Review

**Review type:** Independent cold coherence & correctness review (correctness + usability axes).
**Scope:** The 17 uploaded files, judged solely on their own textual content and internal/cross-document references. File placement and upload paths were not treated as findings per the review's stated constraints.
**Outcome:** Findings report only — no merge/ship/approve recommendation.

---

## 1. Summary

The corpus is, on the whole, internally coherent and densely cross-referenced, and the *normative spine* — `CLAUDE.md`, `CLAUDE_SESSION_DIRECTIVES.md` (CSD), `DOCUMENT_MANAGEMENT_STRATEGY.md` (DMS), and the three engineering standards — holds together cleanly: the great majority of `§`-references, "per X" citations, directive numbers, reserved/retired slots, and the six version stamps cross-check and resolve correctly. The friction is concentrated in the **delivery-surface artifacts** (the apply-prompt template, the two script templates, and the verify-repo-state companion doc), several of which cite a normative section as their authority and then state something the cited section does not actually say — the single most consequential pattern in this review, because those artifacts are exactly what an author copies and follows.

Total findings: **12** — **4 BLOCKING**, **5 SHOULD-FIX**, **3 NIT**.

The **single most important issue** is that the canonical `apply-prompt-template.md` carries two authority-attributed blocks (§0.4.2 surface taxonomy "per ENG-STD-003 §13.5.8" and §0.5 artifact-authority mapping "per ENG-STD-003 §13.5.9") whose content diverges materially from the sections they cite — so an author following the template is steered into a surface model and a citation set the standards no longer carry (findings B-2, B-3). The most *visible* defect is simpler: `README.md` declares the kit version as `2.3.0` while `VERSION` and `PROVENANCE.md` both declare `2.6.0` (B-1).

---

## 2. Findings

### BLOCKING

---

#### B-1 — `README.md` kit version contradicts `VERSION` and `PROVENANCE.md`

**Severity:** BLOCKING (version-coherence mismatch within the corpus)

**Location:** `README.md`, "## Kit version" (the bold `**2.3.0**` opening the section); cross-checked against `VERSION` (sole content `2.6.0`) and `PROVENANCE.md` header (`**Kit version:** 2.6.0`).

**What's wrong:** README opens its Kit version section with `**2.3.0** — the six-document governance corpus **plus the operational layer**…`. Both other release-identity surfaces declare `2.6.0`: `VERSION` contains only `2.6.0`, and `PROVENANCE.md` declares `**Kit version:** 2.6.0`. The README claims the kit is at a version the rest of the corpus says it is two minor releases past. A reader trusting the README's own headline version is misinformed about which packaged set they hold.

**Suggested resolution:** Update README's Kit version headline to `2.6.0` to match `VERSION`/`PROVENANCE.md` (and reconcile the accompanying "What's in it" narrative to the 2.6.0 contents).

---

#### B-2 — `apply-prompt-template.md` §0.4.2 surface-type taxonomy does not match cited `ENG-STD-003 §13.5.8`, and contradicts the DMS surface model

**Severity:** BLOCKING (citation whose target does not support the claim; contradiction with current DMS metadata model)

**Location:** `apply-prompt-template.md` §0.4.2 ("Per ENG-STD-003 §13.5.8 … Surface-type taxonomy (per ENG-STD-003 §13.5.8): …"), incl. the example table rows; cross-checked against `ENG-STD-003-apply-prompt-authoring-standards.md` §13.5.8 ("Surface taxonomy") and `DOCUMENT_MANAGEMENT_STRATEGY.md` §2.3.5.2 / §2.2 rule 6.

**What's wrong:** The template attributes to ENG-STD-003 §13.5.8 a 14-term taxonomy plus a "Pattern A / Pattern B docs" model: `metadata-cell / metadata-cell-multi-version-trail / metadata-date-stamp / header-prose-log / header-prose-log-multi-line / yaml-date-stamp / yaml-cross-doc-pin / yaml-cumulative-log / body-bold-version / body-bold-date-stamp / body-table-cross-doc-pin / cross-doc-pin / append-only-log / terminator`. The section it cites, ENG-STD-003 §13.5.8, defines a *different, 7-term* vocabulary: `yaml-version / yaml-pins / yaml-last-updated / revised-line / change-log-row / footer-marker / document-id-pair`, and never mentions "Pattern A/B." Separately, the template's example rows name surfaces the current DMS model has eliminated — `Document Metadata Version table-cell` and `Document Metadata Effective Date` — whereas DMS §2.2 rule 6 makes version YAML-canonical (body cells are prose pointers, not table-cells carrying the value) and DMS §2.3.5.2 explicitly lists `Effective Date` among rows **stripped** from the metadata table. A reader populating §0.4.2 by following the cited authority cannot, because the authority says something else.

**Suggested resolution:** Re-derive §0.4.2's taxonomy and example rows from the current ENG-STD-003 §13.5.8 / DMS §2.3.4.5 / §2.3.5.5 surface set, or drop the "(per §13.5.8)" attribution if the template intends a different vocabulary.

---

#### B-3 — `apply-prompt-template.md` §0.5 artifact-authority mapping diverges from cited `ENG-STD-003 §13.5.9`

**Severity:** BLOCKING (citation whose target does not support the claim)

**Location:** `apply-prompt-template.md` §0.5 ("Artifact-authority mapping (per ENG-STD-003 §13.5.9): …"); cross-checked against `ENG-STD-003` §13.5.9 ("Artifact-authority mapping").

**What's wrong:** The template's mapping, explicitly labeled "(per ENG-STD-003 §13.5.9)", does not match the mapping §13.5.9 states:

| Artifact | Template §0.5 says | ENG-STD-003 §13.5.9 says |
|---|---|---|
| session-handoff | `DMS §2.3.2 + §4.1 + §9` | `DMS §2.3.2` |
| ADR/DDR/SDD | `DMS §2.3.1 + §5 + §7` | `DMS §2.3.1 + §4 + §6` |
| commit-script | `ENG-STD-002 §13.7 + §5/§6 + DMS §5.1` | *(no commit-script row exists)* |
| review document | *(omitted)* | `review-template.md + §11.7.5` |

The added DMS pointers are also substantively wrong as authorities: DMS `§5` is "Filename Patterns," `§7` is "Normative vs. Operational Content," and `§5.1` is the "Prefix Case Rule" — none is an ADR/DDR/SDD or commit-script *schema* authority, whereas §13.5.9's `§4` (Amendment Policy) + `§6` (Doctype Decision Tree) are apt. The template both adds a row §13.5.9 doesn't have and omits a row it does.

**Suggested resolution:** Replace §0.5's mapping with the verbatim §13.5.9 mapping (or, if commit-script guidance is wanted, source it from a section that actually carries it and cite that section).

---

#### B-4 — `commit-script-template.sh` cites `ENG-STD-002 §6.6`, which does not exist

**Severity:** BLOCKING (dangling cross-reference — target section absent)

**Location:** `commit-script-template.sh`, comment in the staging copy block (~line 438): `ENG-STD-002 §6.6's || true pattern applies only when operation failure is non-actionable`; cross-checked against `ENG-STD-002` §6, which runs §6.1 → §6.5 only.

**What's wrong:** ENG-STD-002 §6 ("Heredoc and Tempfile Discipline") has subsections §6.1–§6.5; there is no §6.6. The cited "`|| true` pattern … when operation failure is non-actionable" has no §6.6 home, so the pointer dangles. (Note: a separate `|| true` mention appears in the same file at line 438's vicinity referencing `§6.6` — the section number itself is the defect.)

**Suggested resolution:** Repoint to the section that actually states the `|| true` / non-actionable-failure convention, or remove the section number if the convention is stated only inline.

---

### SHOULD-FIX

---

#### S-1 — verify-repo-state script + companion overstate `ENG-STD-002 §5.3` as the "normative 10-check set" (circular pointer)

**Severity:** SHOULD-FIX (citation overstatement + newcomer-facing circular pointer)

**Location:** `verify-repo-state-template.sh` header ("Codifies the normative 10-check pre-flight from ENG-STD-002 §5.3" and "See … ENG-STD-002 … §5.3 for the normative check set") and `verify-repo-state-template.md` ("**Normative source:** ENG-STD-002 §5.3 (Repo-State Pre-Flight check set)" / "For the normative check set definition, see ENG-STD-002 §5.3"); cross-checked against `ENG-STD-002` §5.3.

**What's wrong:** §5.3 does not contain a 10-check set or a "check set definition." It names four *categories* ("branch + identity, sync state, working-tree cleanliness, stale state markers") and then explicitly delegates enumeration outward: "the reference `verify-repo-state.sh` provides the enumerated checks." So a newcomer told to "see §5.3 for the normative check set" arrives at a section that points right back at the script for the actual checks — a dead-end loop, and the script/companion overstate §5.3 as the enumerated-set authority when the enumeration lives only in the script itself.

**Suggested resolution:** Reword to "the categorical pre-flight discipline is ENG-STD-002 §5.3; the enumerated 10-check set is codified in this script," removing the implication that §5.3 defines the ten checks.

---

#### S-2 — Middle-severity tier named "YELLOW" in the companion doc but "AMBER" in the script it documents

**Severity:** SHOULD-FIX (terminological inconsistency against the script and the canonical vocabulary)

**Location:** `verify-repo-state-template.md` (uses "Yellow" / "YELLOW" throughout: "Yellow checks warn but don't block," the "Default severity" table column values, and "red = block, yellow = surface, info = inform"); cross-checked against `verify-repo-state-template.sh` (which implements `_amber` / emits `AMBER:`) and `ENG-STD-002` §4.3.1 (canonical vocabulary `{GREEN, AMBER, RED}`) and §4.3.3.

**What's wrong:** The script and the canonical ENG-STD-002 §4.3.1 vocabulary use **AMBER** for the warn tier; the script emits the literal prefix `AMBER:`. Its own companion doc names the same tier **YELLOW** end to end. ENG-STD-002 §4.3.3 sanctions `YELLOW:` only as a *legacy/transition* allowance for "legacy or third-party scripts," explicitly requiring forward-going scripts to use `AMBER`. The companion documents a forward-going corpus template, so "YELLOW" is drift: a reader comparing the doc's "yellow checks" against the script's `AMBER:` output sees two names for one tier.

**Suggested resolution:** Replace "YELLOW" with "AMBER" throughout `verify-repo-state-template.md` to match the script and §4.3.1.

---

#### S-3 — `commit-script-template.sh` cites `ENG-STD-002 §10.8` for "MD5 verification," but §10.8 is "Stage Order"

**Severity:** SHOULD-FIX (citation whose target does not support the claim)

**Location:** `commit-script-template.sh`, sanity-stage comment (~line 454): `Verify content matches (per ENG-STD-002 §10.8 MD5 verification)`; cross-checked against `ENG-STD-002` §10.8 ("Stage Order") and §10.2 ("Stages" — names the "Sanity — file-content verification of expected mutations" stage).

**What's wrong:** ENG-STD-002 §10.8 is "Stage Order" (pre-flight → sanity → commit); it says nothing about MD5 or content verification. The content/MD5 check the comment performs corresponds to the Sanity stage described in §10.2, not §10.8. The "per §10.8 MD5 verification" attribution mislabels its authority. (There is no MD5-named clause anywhere in §10.)

**Suggested resolution:** Repoint to §10.2 (Sanity stage) or to whichever clause names content verification; drop "§10.8."

---

#### S-4 — `apply-prompt-template.md` phase numbering disagrees with `ENG-STD-003 §5.1` and with the template's own guidance block

**Severity:** SHOULD-FIX (cross-document + internal numbering inconsistency)

**Location:** `apply-prompt-template.md` body (§0.5 "Canonical-Authority-Fetch Inventory", §0.6 "Invocation") vs its own authoring-guidance "CANONICAL PHASE STRUCTURE" block ("0.5 Invocation") and the "PHASE NUMBERING NOTE" ("Phases below use 0/0.4/0.5/1/2/3/4/5/6"); cross-checked against `ENG-STD-003` §5.1 ("Canonical Phase Shape"), which lists `0.5 Invocation`.

**What's wrong:** ENG-STD-003 §5.1 fixes the canonical shape with **Invocation at §0.5** and has no §0.5 "Canonical-Authority-Fetch Inventory" step. The template body instead places **Canonical-Authority-Fetch Inventory at §0.5** and **Invocation at §0.6**. The template's *own* guidance block and phase-numbering note still say Invocation is §0.5 — so the template contradicts both the standard and itself on what §0.5 is. Since ENG-STD-003 §5.6 prohibits "custom phase numbering" and anchors the pre-pre-flight numbers, this is a real conformance gap, not a free positional shift.

**Suggested resolution:** Reconcile the template's body numbering with ENG-STD-003 §5.1 (and update the template's guidance block to match whichever numbering is adopted).

---

#### S-5 — Concrete project tracker IDs embedded in project-agnostic artifacts

**Severity:** SHOULD-FIX (orphaned reference for a newcomer; inconsistent with the corpus's stated project-agnosticism and `{{TRACKER_PREFIX}}` discipline)

**Location:** `DOCUMENT_MANAGEMENT_STRATEGY.md` §3.6.4 ("…PROVISIONAL pending the **HEB-9** compilation DDR…"); `commit-script-template.sh` (~lines 143 and 274: "…the branch is falsely rejected (**HEB-34**)").

**What's wrong:** README states "Every document is project-agnostic: project-specific references are replaced with placeholders or documented assumptions," and the corpus consistently uses `{{TRACKER_PREFIX}}-NN` elsewhere (e.g., DMS §2.3.4.3). Against that discipline, the DMS — a consumed, project-agnostic standard — embeds a concrete `HEB-9`, and the consumer-kit `commit-script-template.sh` embeds `HEB-34` (twice). For an adopting reader with no access to the HE-Bedrock tracker, `HEB-9` / `HEB-34` are unresolvable references that "only make sense with unstated knowledge." (README's own `IRI-145` / `HEB-3` are not flagged: README is a repo-root convention file out of DMS scope per DMS §1.3.)

**Suggested resolution:** Replace the concrete IDs with `{{TRACKER_PREFIX}}-NN` (or a neutral "tracked at the project's compilation DDR" phrasing) in the DMS and the commit-script template.

---

### NIT

---

#### N-1 — `ENG-STD-003 §13.5.9` calls `DMS §2.3.1` a "frontmatter pattern"; it is a metadata-table pattern

**Severity:** NIT (terminological inaccuracy in an otherwise-resolving citation)

**Location:** `ENG-STD-003` §13.5.9 artifact-authority mapping: "ADR / DDR / SDD → DMS §2.3.1 (**frontmatter pattern**) + §4 + §6"; cross-checked against `DMS` §2.3.1 ("ADR / DDR / SDD metadata pattern") and the ADR/DDR/SDD templates.

**What's wrong:** DMS §2.3.1 specifies a **metadata table** (Document ID / Version / Status / Date / Authors), and the ADR/DDR/SDD templates carry no YAML frontmatter at all. The corpus elsewhere is careful to distinguish "YAML frontmatter" from the "Document Metadata table," so labeling §2.3.1 a "frontmatter pattern" is inaccurate. The pointer still resolves to the right section; only the parenthetical descriptor is off.

**Suggested resolution:** Change "(frontmatter pattern)" to "(metadata-table pattern)".

---

#### N-2 — ADR/DDR/SDD templates order the `Status` metadata row inconsistently with `DMS §2.3.1` and with each other

**Severity:** NIT (cosmetic ordering drift across sibling templates)

**Location:** `adr-template.md`, `ddr-template.md`, `sdd-template.md` metadata tables; cross-checked against `DMS` §2.3.1 (canonical order: Document ID, Version, Status, Date, Authors).

**What's wrong:** The three templates place `Status` differently: ADR lists `Status` **before** `Version`; DDR lists `Version` then `Platform Version` then `Status`; SDD lists `Status` **after** `Date`/`Authors`. None matches the §2.3.1 core order (Version → Status → Date → Authors), and they disagree with one another. §2.3.1 admits "(Additional fields per doctype template.)" so this isn't strictly broken, but the relative order of the canonical core rows drifts three ways.

**Suggested resolution:** Align the core rows (Document ID → Version → Status → Date → Authors) across all three templates, inserting doctype-specific rows after.

---

#### N-3 — `ENG-STD-003` metadata row label keeps the placeholder word "Substrate" rather than substituting a concrete term

**Severity:** NIT (low-confidence conformance observation against the §2.3.5.2 pattern)

**Location:** `ENG-STD-003` Document Metadata table row `**Primary Substrate (bash + markdown)**`; cross-checked against `DMS` §2.3.5.2.

**What's wrong:** DMS §2.3.5.2 says the row label uses the spec-level placeholder `{Substrate}` and "the authored standard substitutes the concrete substrate name (`Language` / `Shell` / etc.)." ENG-STD-003 retains the literal word "Substrate" as the term (qualified by "(bash + markdown)") rather than substituting a concrete substrate name the way ENG-STD-001 ("Primary Language") and ENG-STD-002 ("Primary Shell") do. The same clause permits "the most precise substrate term applicable," so this is defensible for a dual bash+markdown substrate — hence NIT, low confidence.

**Suggested resolution:** Consider a concrete dual label (e.g., "Primary Substrates") or leave as-is if "Substrate" is judged the most precise term.

---

## 3. Checked-clean

The following were verified and came back clean (scope/depth of the pass):

**Version & pin coherence**
- All six `PROVENANCE.md` document-version entries match the versions the referenced documents actually declare: `CLAUDE_SESSION_DIRECTIVES.md` 3.4.0, `DOCUMENT_MANAGEMENT_STRATEGY.md` 3.3.0, `ENG-STD-001` 3.3.0, `ENG-STD-002` 2.3.0, `ENG-STD-003` 3.0.1, and `CLAUDE.md` scaffold (unversioned — consistent with its no-YAML, header-only form and the DMS §2.3.4 exemption).
- `VERSION` (2.6.0) and `PROVENANCE.md` kit version (2.6.0) agree. (Only `README.md` dissents — finding B-1.)
- The two script-header standard pins ("ENG-STD-002 v2.3.0" in `verify-repo-state-template.sh` and `commit-script-template.sh`) match ENG-STD-002's declared 2.3.0.
- Reduced consumed-snapshot frontmatter (`doctype` + `version`, plus `document_id` for engineering standards) conforms to DMS §2.3.4 consumed-snapshot form for CSD, DMS, and all three ENG-STDs; their "Version & history" metadata rows correctly use the reduced "See YAML frontmatter `version`. Maintained by the document owner." literal.
- No internal version/footer mismatch: every footer marker is name-only per DMS §2.3.4.4 (`*End of …*` for CLAUDE.md, CSD, DMS, all three ENG-STDs, PROVENANCE, and the verify-repo-state companion).

**Directive register integrity (CSD)**
- Every `DIRECTIVE-NNN` cited in `CLAUDE.md`'s Authority map (026, 019, 012, 018, 016, 007, 034, 031, 032, 020, 006, 025, 024, 023, 029, 008, 009) resolves to a present, non-reserved directive.
- All RESERVED/RETIRED slots (DIRECTIVE-004/011/013/017/021/022/027/028/033/035/036; §26.4 RETIRED; §31.5/§31.6/§31.8 RESERVED; ENG-STD-003 §5.8.2–§5.8.5/§6.1/§11.8/§13.4 RESERVED; DMS §4.4/§4.9 RESERVED) are marked at their position and are **not** cited as live anywhere else in the corpus.

**Cross-document `§`-reference resolution (spot-to-exhaustive)**
- DMS targets cited by CLAUDE.md / CSD / templates / ENG-STDs all resolve and support their claims: §2.2 (markdown header), §2.3.1, §2.3.2 / §2.3.2.1 / §2.3.2.2, §2.3.4.x, §2.3.5.x, §2.4 (Bucket A/B), §3.1, §4.6 (PATCH/MINOR/MAJOR), §4.10/§4.11/§4.12 (atomic-refresh / pin-update / pin-propagation), §5.x (filename patterns), §6.x, §7.4–§7.9 (contract-purity family), §8.3 (3-retention).
- ENG-STD-001 targets resolve and support their claims: §1.1 (Python 3.11+), §2.4 (Bucket-B bare-date `# Revised:`), §10.1 (≥90% line coverage), §12.10 (retrospective review), §14.1 (develop/main flow), §14.5 (branch allowlist `feature/ docs/ hotfix/v* release/v*`), §25.1 (Cloud Run default / GKE on ADR).
- ENG-STD-002 targets resolve: §3.5 (Bucket-A header), §4.3.1–§4.3.5 (GREEN/AMBER/RED), §4.4 (exit codes), §5.1 (both-halves identity), §5.3 (categories — see S-1), §6.3/§6.4, §9.2 (accumulator), §10.x, §11.1/§11.2 (PR base / semver label), §14.1–§14.5 (incl. the §14.2 branch-allowlist bullet that §10.1 relies on).
- ENG-STD-003 targets resolve: §2.1 (notation), §3.1–§3.4 (substrate inheritance + exit-code override), §4.4 (pre-authoring), §5.1/§5.2 (phase shape / pre-flight — see S-4), §11.6 (leaf-identifier branch naming, which `CLAUDE.md` §3.1 relies on), §13.5.7, §13.5.8/§13.5.8.1/§13.5.8.2 (PostVerify gate), §13.5.9 (canonical-schema fetch).
- All `commit-script-template.sh` ENG-STD references resolve **except** §6.6 (B-4) and the §10.8 mislabel (S-3): §10, §6.4, §14.1, §5.1, §3.1, §10.4/§10.6/§10.7/§10.9, §7.1, §6.3, §11/§11.1, §12, §14.2 + ENG-STD-001 §14.5 all resolve.
- `verify-repo-state-template.md` cross-references resolve: ENG-STD-002 §5.3 (with the S-1 caveat), §5.1, §14.1, CSD DIRECTIVE-018, and the commit-script template.

**Terminology, roles, and vocabularies**
- The two finding-severity vocabularies are cleanly venue-scoped and mutually consistent where defined: review-finding `{BLOCKING/MATERIAL/COSMETIC/POSITIVE}` (CSD DIRECTIVE-007 §7.2, ENG-STD-002 §4.3.2, review-template) vs operator-facing script output `{GREEN/AMBER/RED}` (ENG-STD-002 §4.3.1) — the only drift is the companion-doc "YELLOW" (S-2).
- The identifier registry (`CLAUDE.md` §3.1) and its consumers are consistent: `R{N}.{M}`, `B-N`/`M-N`/`C-N`, `MS{N}-{M}`, `{{TRACKER_PREFIX}}-{leaf}-R{NNN}`, and the interstitial lexicon (§3.7) are used as defined in the review-template, DIRECTIVE-030 P5, and DIRECTIVE-031.
- "Morphing body" / "audit surface" / "contract-purity test" are defined once (DMS §7.5 / §7.7) and referenced — not redefined — by DIRECTIVE-007 §7.2.1, DIRECTIVE-023, and the ADR/DDR/SDD/review templates.

**Placeholder discipline**
- The adoption-placeholder set enumerated in `README.md` ("Adopting it," step 2) exactly matches the twelve ALL-CAPS adoption placeholders actually used corpus-wide (`PROJECT_NAME, AUTHOR_NAME, AUTHOR_ROLE, ORGANIZATION, TRACKER_PREFIX, REPO_HOST_ORG, COMPUTE_PLATFORM, PRIMARY_LANGUAGE, GIT_NAME, GIT_EMAIL, CLOUD_IDENTITY, REPO_ROOT`); none is declared-but-unused or used-but-undeclared. (Concrete tracker IDs that bypass `{{TRACKER_PREFIX}}` are the separate S-5 issue.)

**Structural integrity**
- No truncated/orphaned sections were found in the normative spine; the one apparent stray header (`### 2.4 PAUSE-POINT 1 …` inside ENG-STD-003 §5.5) is content **inside a fenced code example** illustrating an authored apply-prompt's internal numbering, not a real section header — not a defect.
- Reserved-slot numbering is internally consistent across CSD, DMS, and ENG-STD-003 (stable-numbering convention applied uniformly).

**Out of scope (not assessed, per the review constraints):** physical file placement / upload paths; existence of referenced files not uploaded (e.g., `docs/templates/session-handoff-template.md`, `scripts/verify-pin-currency.sh`) — these are file-path references, not section references, and were excluded by constraint.

---

*End of HE-Bedrock cold acceptance review.*
