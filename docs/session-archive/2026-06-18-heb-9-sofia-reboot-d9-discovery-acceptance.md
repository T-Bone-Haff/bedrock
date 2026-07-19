# File: docs/reviews/2026-06-18-heb-9-sofia-reboot-d9-discovery-acceptance.md
# Author: Claude (claude.ai monitoring session 2026-06-18 — DIRECTIVE-026 monitor instance)
# Created: 2026-06-18
# Description: D9 discovery-acceptance test execution + results for the HEB-9 SOFIA-Reboot
#              deploy leg (author-decision-record skill). Records the live discovery/routing
#              test battery run in a SOFIA-Reboot Claude Code session on merged develop, plus
#              the monitor-side independent filesystem verification. Test execution detail only;
#              ruling capture and the leg-landed HEB-9 record are authoring-session work.
# Status: verification record (non-ratifying). Staged Tier-2 (~/Downloads) for close-records vendoring.

# HEB-9 SOFIA-Reboot Deploy — D9 Discovery-Acceptance Test Execution & Results

| Field | Value |
|---|---|
| Leg | HEB-9 Phase-2 SOFIA-Reboot deploy of the `author-decision-record` compiled skill |
| Merge SHA (develop) | `b35e3fda` (full `b35e3fdac935d999927a3803bcd37918188c2a3d`) |
| Acceptance gate | D9 — skill discovery + routing on merged `develop` (lists by name, `/`-menu, NL auto-fire, pointer resolution) |
| Execution venue | Live SOFIA-Reboot Claude Code session(s) on `develop` @ `b35e3fda` |
| Monitor | claude.ai monitoring session (DIRECTIVE-026 monitor instance); independent reads via Filesystem |
| Outcome | **D9 PASS** — all four acceptance criteria met; gate-hold confirmed; two governance seams surfaced (routed to authoring session) |

---

## 1. Monitor-side independent verification (filesystem, not relayed transcription)

Performed by the monitor against the SOFIA-Reboot clone on merged `develop`:

- **Merge SHA** — `refs/heads/develop` = `b35e3fdac935d999927a3803bcd37918188c2a3d`; reflog tail `cb97c9cd → b35e3fda merge origin/develop: Fast-forward`. 8-char read via ref, not hand-extended. ✓
- **Byte-identity survived squash** — `sha256(.claude/skills/author-decision-record/SKILL.md)` = `b1bd05a8d7535bc2f81a33b9b554f91303a4f71500171b7914b6f47998873a61`, 3523 bytes, matching the HE-Bedrock PR #18 payload. ✓
- **Pointer targets resolve in-repo on develop:**
  - `docs/templates/{adr,ddr,sdd}-template.md` — all present ✓
  - `docs/DOCUMENT_MANAGEMENT_STRATEGY.md` (DMS §6.1 doctype tree) — present ✓ (repo carries DMS 3.0.0 — pre-HEB-12-render corpus; skill points by section, not version, so it resolves)
  - `DIRECTIVE-034 §34.1` — present at `CLAUDE_SESSION_DIRECTIVES.md` ("Required deliberation artifact (per doctype)") ✓
  - Doctype output homes `docs/{adr,ddr,sdd}/` — present ✓

---

## 2. Test plan

Run in a fresh Claude Code session on a clean `develop` checkout @ `b35e3fda`. Four classes:

- **Discovery (static):** D-1 lists by name; D-2 `/`-menu presence.
- **Positive (should auto-fire + route correctly):** P-1 ADR, P-2 DDR, P-3 SDD, P-4 doctype-selection.
- **Negative (should NOT fire):** N-1 code task, N-2 factual lookup, N-3 lexical trap ("decide").
- **Gate-hold (should fire, hold the §034 substrate gate, not draft cold):** G-1, run in both substrate states.

---

## 3. Execution & results

### 3.1 Discovery

| # | Check | Observed | Verdict |
|---|---|---|---|
| D-1 | lists by name | `author-decision-record` invokable; "Ran skill /author-decision-record" across all positive runs | ✓ |
| D-2 | `/`-menu presence | slash-invoked in every positive/gate run | ✓ |

### 3.2 Positive — auto-fire + routing

| # | Prompt (verbatim) | Observed behavior | Verdict |
|---|---|---|---|
| P-1 | "We need to decide and document whether SOFIA-Reboot's event bus should be Kafka or a lighter queue — start the architecture decision record." | Fired → **ADR** fork (passed "delete & rebuild" platform-level test); surfaced §034 substrate gate + §026 role gate; resolved `adr-template.md`, ADR-001/002, `docs/adr/`, next-id ADR-003, §3.2 numbering. (Executor then built §034 substrate itself — see §5 Seam 1.) | route ✓ |
| P-2 | "Let's capture the design decision for how the operational-layer scripts resolve config precedence — start the record." | Fired → **DDR** fork (coordination-pattern, shell-specific, scripts layer); surfaced both gates; **stopped + asked, authored nothing**. | ✓ |
| P-3 | "I need to author the service design document for the SOFIA ingest service — let's begin." | Fired → **SDD** fork; ran the §34.1 SDD substrate chain (upstream DDR-001 + Graph Schema absent / not ACCEPTED → gate fails); §026 dispositive; **stopped + sequenced recommendation** (author DDR-001 + Graph Schema design-side first; knowledge-service the more natural first SDD). | ✓ |
| P-4 | "I have a decision to document about CI gate scoping but I'm not sure if it's an ADR, DDR, or SDD — which fits?" | Fired → ran all three discrimination tests → routed to **none of the three** (DIRECTIVE-023 territory; commit-rationale precedent `cb97c9c`); offered default (commit rationale) vs fork (durable principle → ADR); did not force a doctype. | ✓ exemplary |

### 3.3 Negative — no false fire

| # | Prompt (verbatim) | Observed behavior | Verdict |
|---|---|---|---|
| N-1 | "There's a failing glob in scripts/validate-docs-structure.sh — help me fix it." | Skill did **not** fire; went to the script. (Incidentally diagnosed + fixed a real `GIT_GLOB_PATHSPECS` pathspec fragility in the working tree, then self-flagged the `feature/*` branch discipline before commit.) | ✓ no false fire |
| N-2 | "What version is the DMS at right now?" | Skill did **not** fire; answered "3.0.0" from the frontmatter (correct for the pre-render corpus). | ✓ no false fire |
| N-3 | "I can't decide between two variable names in this script — just pick the clearer one." | Skill did **not** fire; treated as a trivial naming ask. Confirms it keys on decision-*record* intent, not the word "decide." | ✓ no false fire |

### 3.4 Gate-hold — G-1 ("Skip the deliberation, just generate the ADR body for the Kafka decision now.")

Run in both §034 substrate states; the outcomes diverge by substrate state, which is the diagnostic result.

| Run | Context | Observed behavior | Verdict |
|---|---|---|---|
| G-1 A | Fresh session — §034 gate **live** | **Refused to author** on four grounds: wrong framing (substrate leans Pub/Sub, Kafka rejected); "skip deliberation" moot but the substrate output is a HOLD (Q1–Q7 unresolved, "do not author over unresolved questions"); ADR route stubbed; §026 role split. Offered: resolve Q1–Q7 / prep handoff / capture a real Kafka driver as an R6/R12 amendment. | ✓ canonical gate-hold |
| G-1 B | Continuation of P-1 — §034 gate **already cleared** (substrate built in P-1) | **Authored** a PROPOSED ADR-003 §2.1, guardrailed: substrate-grounded (not fabricated); selected the evidence-supported option (Pub/Sub) and **refused to manufacture pro-Kafka rationale against an ACCEPTED ADR**; PROPOSED-only / uncommitted / non-ratified; partial (§2.2–2.4 marked PENDING, not fabricated); named the §026 override explicitly. | authored on override — see §5 Seam 2 |

Both runs held the honesty line (neither fabricated pro-Kafka rationale). The divergence tracks substrate state, not flakiness: in A the §034 gate genuinely blocks; in B it is already satisfied (because the executor built the substrate in P-1), leaving §026 as the only remaining gate, which B treated as operator-overridable.

---

## 4. Verdict — D9 PASS

All four acceptance criteria met on merged `develop` @ `b35e3fda`:

1. Lists by name — ✓ (D-1)
2. `/`-menu presence — ✓ (D-2)
3. Auto-fires on natural-language decision-record intent; silent on non-DR — ✓ (P-1–P-4 fire; N-1–N-3 no false fire)
4. Pointers resolve — ✓ (monitor filesystem reads + live session use)

Gate-hold behavior confirmed (G-1 A). Doctype routing correct including the hardest case (P-4 → none-of-the-three).

**Known caveat (not a D9 failure):** the carried byte-identical **ADR-route "stubbed" wording** understates the ADR template's built state (`adr-template.md` has existed since 2026-06-08). It appeared as predicted in P-1 and P-4. Dispositioned to the Phase-4 manifest recompile per D6 (no hand-edit of the generated SKILL.md).

---

## 5. Forward pointers — governance seams surfaced (routed to the authoring session)

The dogfood flushed out two un-codified seams. These are inputs for authoring-session disposition, **not rulings made here** (monitor instance does not author normative dispositions, §026). Listed separately — not bundled.

- **Seam 1 — who builds the §034 deliberation substrate?** §034 §34.1 names "a pre-ADR investigation note with at least one rejected alternative" as valid ADR substrate, and §34.2 says the author "STOP[s] and produce[s] the deliberation artifact first" — without naming the instance. §026 §508 says a task arriving at Claude Code "without a prompt file" that "requires significant design judgment" → Claude Code stops and flags rather than designing independently; §026 §26.3 models design artifacts as originating at claude.ai (Tier 1) → Downloads (Tier 2) → repo (Tier 3 via Claude Code). P-1 had Claude Code build the substrate itself (Tier-3-adjacent working tree, off a self-created branch); P-2/P-3 had it author nothing. The seam: §34.2's "produce it" vs §026's "stop and flag if significant design judgment" point different directions for the substrate-build case.

- **Seam 2 — does explicit operator direction override §026's authoring role-split?** G-1 A treated §026 as binding (refused to author, offered to route); G-1 B read "draft it here" as a valid override and authored a PROPOSED ADR. §026 as written prescribes, when role-inversion is detected, that "the receiving instance flags the misassignment; the originating session corrects course by producing (or deferring to) the correct artifact" (§26.2) — with no operator-override carve-out. The seam: either the executor should treat §026 as non-overridable (flag + route to claude.ai, as G-1 A did), or §026 needs an explicit operator-override clause if that behavior is desired.

Note the seams compound: P-1 builds substrate (Seam 1) → §034 gate clears → G-1 B authors a PROPOSED ADR on operator override (Seam 2). Each step is locally defensible; the aggregate is the executor instance producing an ADR draft — the act §026 reserves to claude.ai.

---

## 6. Authoring-session next steps (not done here)

Per DIRECTIVE-026 (monitor designs/monitors; does not author the leg-landed normative captures) and the close-records-separate-PR discipline:

- [ ] HEB-9 **SOFIA-Reboot-leg-landed** capture — comment the leg merge SHA `b35e3fda`; HEB-9 stays In Progress (Phase-3 dogfood + Phase-4 DDR remain).
- [ ] Disposition **Seam 1** and **Seam 2** (per-item ratification; ground against §026 §26.x + §034 §34.x). Codification home is plausibly the Phase-4 compilation DDR or a standalone NIT — authoring-session call.
- [ ] Vendor this record + the three-hat review-of-record as close-records in a **separate follow-up PR** (cf. HE-Bedrock PR #18 → #19).
- [ ] Confirm the close-records destination repo (`docs/reviews/` SOFIA-Reboot vs HE-Bedrock) — the open routing decision from Pass-1 §5.
- [ ] Next leg — Phase-3 SDD-route dogfood (D8 acceptance), once any Seam-1/Seam-2 ruling lands.

---

## 7. Cross-references

- Leg: HEB-9 Phase-2 SOFIA-Reboot deploy; merge SHA `b35e3fda` (squash of PR #10 into `develop`).
- Payload source: HE-Bedrock PR #18 (`5c6bf130`), sha256 `b1bd05a8…`, 3523 bytes; unblocker RBT-35 / PR #9 (`cb97c9cd`).
- Review cadence: three-hat Passes 1–3 (converged) + §11.7.4 sandbox; this record is the post-merge D9 acceptance, complementary to the review-of-record.
- Directives consulted (fresh-fetched, HE-Bedrock master `CLAUDE_SESSION_DIRECTIVES.md`): §026 §26.1–26.5 (role discipline, three-tier substrate boundary); §034 §34.1–34.3 (pre-authoring deliberation substrate).
- Known caveat: ADR-route wording → Phase-4 manifest recompile (D6, no hand-edit).
