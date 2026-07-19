# File: docs/ruling-rationale/2026-06-18-heb-9-sofia-reboot-deploy-rulings.md
# Author: Claude (claude.ai authoring + close session 2026-06-18)
# Created: 2026-06-18
# Description: Ruling-rationale ledger for the 2026-06-18 HEB-9 session — skill-delivery-surface
#              disposition + the SOFIA-Reboot deploy leg of the author-decision-record skill +
#              D9 discovery-acceptance. Captures three ruling-bearing decisions (R032-R034) per
#              DIRECTIVE-031 §31.2, plus two Phase-4 forward-pointer seams surfaced by the D9
#              dogfood. Frozen at commit per §31.7.
# Revised: 2026-06-18 (HEB-9 SOFIA-Reboot leg — surface decision + deploy + D9 close) — DRAFT for ratification

# Ruling-Rationale Ledger — HEB-9: skill-delivery surface + SOFIA-Reboot deploy + D9 acceptance

## 0. Header

| Field | Value |
|---|---|
| **Anchor work item** | HEB-9 (Governance Starter Kit; parent HEB-6) — Phase-2 SOFIA-Reboot leg + skill-delivery-surface disposition + D9 acceptance |
| **Session** | 2026-06-18 (claude.ai design-side: surface deliberation, deploy apply-prompt authoring + three-hat oversight, post-merge D9 close) |
| **Author** | Claude (claude.ai authoring + close session 2026-06-18) |
| **Leg merge SHA** | SOFIA-Reboot `develop` @ `b35e3fda` (`b35e3fdac935d999927a3803bcd37918188c2a3d`; squash of PR #10; develop-based) — independently confirmed |
| **Close-records destination** | HE-Bedrock `main` per **R034** (vendoring follow-up PR pending) |
| **Governance baseline** | CSD v3.1.0 · DMS v3.1.0 (HE-Bedrock master) / v3.0.0 (SOFIA-Reboot consumer) · ENG-STD-001 v3.3.0 · ENG-STD-002 v2.3.0 · ENG-STD-003 v3.0.1 · kit VERSION 2.3.0 · corpus tag v2.3.0. No governance-document version changed this leg (skill deploy only). |
| **Deployed artifact** | `author-decision-record` compiled skill, byte-identical (sha256 `b1bd05a8d7535bc2f81a33b9b554f91303a4f71500171b7914b6f47998873a61`, 3523 bytes) into SOFIA-Reboot `.claude/skills/` (bootstrap) |
| **Status** | Captured at close; vendored in the HEB-9 SOFIA-Reboot-leg close follow-up (HE-Bedrock, per R034). Frozen at commit per DIRECTIVE-031 §31.7. |

*Two-layer ledger (DIRECTIVE-031 §31.2.1): §1 inventory + §2 detail blocks. Ruling IDs R032-R034 continue the global sequence (prior max R031, HEB-9 Phase-2 HE-Bedrock leg; verified against the frozen Phase-2 ledger). These rulings postdate the frozen PP-0…PP-4b HEB-9 design & decisioning ledger (Notion) and do not amend it (§31.7).*

## 1. Rulings Inventory

| ID | Subject | Disposition class |
|---|---|---|
| R032 | Skill-delivery surface — primary surface claude.ai-in-principle, `.claude/skills/` write-execution surface; both-surfaces contract; claude.ai-app delivery deferred; Phase-3 dogfood on the Code native surface | Design direction |
| R033 | Decision-record authoring division of labor — claude.ai authors design + captures, Code renders the document under skill guidance, design-review stays claude.ai; §34.1 STOP gate keeps it §026-clean; literal-§026-line refinement routed to Phase-4 | Design direction / operating-model refinement (routed) |
| R034 | Close-records destination = HE-Bedrock — infrastructure-deploy records stay in Bedrock even when the deploy lands in a consumer repo | Process / routing |

## 2. Ruling Detail

### R032 — Skill-delivery surface disposition

- **Ruling.** The `author-decision-record` skill's **primary intended surface is claude.ai in principle** — the deliberation moment (doctype discrimination + DIRECTIVE-034 §34.1 substrate gate) is its highest-value use, and DIRECTIVE-026 places that moment at claude.ai. `.claude/skills/` (Claude Code) is the **write-execution** surface. The compiled-skill contract is **both-surfaces**, named explicitly (so "deploy to `.claude/skills/`" does not imply Claude-Code-only by accident). **claude.ai-app delivery (account-global ZIP) is DEFERRED** — not built this cycle. The **Phase-3 dogfood runs on the Claude Code native surface**, in-repo. The full both-surfaces contract, whether to build the claude.ai delivery path, and the repo-relative-pointer resolution rule route to the **Phase-4 compilation DDR**.
- **Disposition.** Design direction.
- **Rationale.** Surface mechanics re-verified against current Anthropic docs this session (fresh-fetch, not inherited from the prior Design Note): Claude Code project skills auto-discover in-repo from `.claude/skills/` with pointers resolving; claude.ai custom skills are account-global ZIP uploads (Settings > Features), per-user, no per-project scoping, and run in the code-execution container (repo-relative pointers do not resolve unless the repo is brought in). The skill's value-moment (claude.ai) and its clean-delivery surface (Claude Code) pull opposite ways. Deferring claude.ai delivery honors the empirical floor (one skill; zero dogfood data at decision time) and avoids building account-global ZIP + pointer-resolution machinery that fights the regen cascade (D6) before evidence justifies it.
- **Alternatives rejected.** (a) Build the claude.ai delivery path now — rejected: premature against a single instance; a manual, account-global, pointer-breaking path that fights idempotent regen (D6). (b) Treat `.claude/skills/`-only as the contract — rejected: the contract is named both-surfaces to prevent Claude-Code-only-by-accident.
- **Primary sources verified.** Current Anthropic docs (platform.claude.com Agent Skills overview; code.claude.com skills) — fresh-fetched this session; DIRECTIVE-026 role split; DIRECTIVE-034 §34.1.
- **Other.**
  - *Captured:* HEB-9 comment trail (Design Note resolution, 2026-06-18).
  - *Empirical floor:* decision made on mechanics + the governance model, not dogfood data; the Phase-3 dogfood is the first evidence and may justify revisiting the claude.ai-delivery deferral.

### R033 — Decision-record authoring division of labor

- **Ruling.** For decision-record authoring under the deployed skill: **claude.ai authors the design** (the deliberation) and **captures** to Linear/Notion; a kickoff hands Claude Code the **ratified substrate**; the skill **drives the document authoring** in-repo; **design-review stays at claude.ai** (three-hat). The skill's DIRECTIVE-034 §34.1 **STOP-if-absent gate** keeps this DIRECTIVE-026-clean — Code renders decided design and pauses rather than inventing it. This cuts against the literal "claude.ai authors … SDDs" line of DIRECTIVE-026, so the **division-of-labor refinement routes to the Phase-4 compilation DDR**.
- **Disposition.** Design direction / operating-model refinement (routed).
- **Rationale.** Follows from selecting the Code-surface dogfood (R032). The skill's value spans the deliberation moment (claude.ai) and the write-execution moment (Code); the dogfood tests the rendering moment on the native surface where pointers resolve. DIRECTIVE-026's intent (design judgment + review at claude.ai) is honored; only its literal "authors SDDs" line is in tension, hence the routed refinement rather than a unilateral re-reading of the directive.
- **Alternatives rejected.** (a) Code authors the decision record from scratch (independent design judgment) — rejected per DIRECTIVE-026 §26.2 (role-inversion). (b) Pre-author the record at claude.ai and ship it as apply-prompt bytes — rejected: hollows the dogfood (the skill would have nothing to drive).
- **Primary sources verified.** DIRECTIVE-026 §26.1–26.5; DIRECTIVE-034 §34.1; the HEB-9 surface-decision comment trail (2026-06-18).
- **Other.**
  - *Phase-4 inputs:* the §026 refinement this routes now has empirical inputs from the D9 dogfood — **Seam 1** and **Seam 2** (see Forward Pointers). The Phase-4 DDR should address R033's routed refinement together with both seams (one comprehensive §026 treatment).

### R034 — Close-records destination = HE-Bedrock

- **Ruling.** Close-records for the HEB-9 SOFIA-Reboot deploy leg (the deploy apply-prompt, the three-hat Pass 1–3 reviews, the consolidated review-of-record, the D9 acceptance record, and this ledger) **vendor into HE-Bedrock** (`docs/session-handoffs/apply-prompts/`, `docs/reviews/`, `docs/ruling-rationale/`) — **not SOFIA-Reboot** — even though the deploy mutation landed in SOFIA-Reboot.
- **Disposition.** Process / routing.
- **Rationale.** The **design subject** is governance structure + operating components (Product-1 infrastructure — a kit-produced skill), which is HE-Bedrock's domain; SOFIA-Reboot was the **deployment target**, not the design subject. The close-records are governance-**process** artifacts (an apply-prompt authored against ENG-STD-003, three-hat reviews under DIRECTIVE-007, a D9 acceptance of the skill). Routing them to HE-Bedrock keeps the HEB-9 trail **unified in one repo**, consistent with Phase-1 (PR #17) and the Phase-2 HE-Bedrock leg (PR #19). The deployed `SKILL.md` is a **vendored** artifact; vendored artifacts point upstream for provenance (consumer-points-to-upstream), and the cross-repo bridge is carried by the HEB-9 ticket (the index) + the SOFIA-Reboot PR #10 commit's `Refs: HEB-9 / HE-Bedrock PR #18`.
- **Alternatives rejected.** SOFIA-Reboot destination (the deploy landed there; a DDR-001-style co-location case) — rejected: the mutation landed in SOFIA-Reboot but the design subject is Bedrock-domain, and co-locating would fragment the HEB-9 trail across two repos; the provenance bridge (ticket + commit refs) preserves discoverability without co-location.
- **Primary sources verified.** HEB-9 prior close-records (PR #17 / #19, HE-Bedrock) — established precedent; the SOFIA-Reboot PR #10 commit refs (`HEB-9` / HE-Bedrock PR #18).
- **Other.**
  - *Generalizable rationale, NOT codified here:* "infrastructure deploys keep their close-records in Bedrock even when they land in a consumer repo" is a clean candidate principle, but is **not** minted as a corpus rule off this single instance (threshold discipline) — promote only on recurrence.
  - *Conscious property (not a gap):* the deployed file lives in SOFIA-Reboot while its provenance/review trail lives in HE-Bedrock; the bridge is the HEB-9 ticket + the commit refs.

---

## Forward Pointers — Phase-4 compilation DDR inputs (carry-forward, NOT rulings)

The D9 dogfood flushed two un-codified governance seams. These are **open questions routed to the Phase-4 DDR**, not decisions made here; no provisional ruling IDs (DIRECTIVE-031 §31.2.4 piggyback). Listed separately, not bundled. The authoring-session reads below are **non-binding inputs** for Phase-4 deliberation, not dispositions.

- **Seam 1 — who builds the §034 deliberation substrate?** DIRECTIVE-034 §34.2 ("the author STOPs and produces the deliberation artifact first") names the *what* without naming the *instance*; DIRECTIVE-026 says a task reaching Claude Code that requires significant design judgment → Code stops and flags rather than designing. D9 P-1 had Code build the §034 substrate itself. *Authoring-session read (non-binding):* building deliberation substrate is design judgment → claude.ai's per §026; §34.2's "produce it" is performed by the design instance. → Phase-4 §026↔§034 cross-reference.
- **Seam 2 — does explicit operator direction override §026's authoring role-split?** D9 G-1 B authored a **guardrailed PROPOSED ADR** on explicit operator override — substrate-grounded, non-fabricated, uncommitted, and refusing to manufacture pro-Kafka rationale against the evidence. *Authoring-session read (non-binding):* evidence that a **narrow operator-override clause** (for PROPOSED / review-pending drafts) is bounded and safe, and that treating §026 as absolutely non-overridable would forbid the very Code-surface workflow R033 ratified. → Phase-4 §026 refinement.
- **Seams compound:** P-1 substrate-build (Seam 1) → §034 gate clears → G-1 B authors on override (Seam 2) = the executor instance producing an ADR draft, the act §026 reserves to claude.ai. The Phase-4 DDR should treat R033's routed refinement + both seams as **one comprehensive §026 treatment** (per operator direction, 2026-06-18).
- **ADR-route "stubbed" wording** (restated, already on the HEB-9 trail, 2026-06-17 finding): the byte-identical skill understates the built `adr-template.md`; → Phase-4 manifest recompile (D6, no hand-edit of the generated SKILL.md).

---

*Substrate note: this ledger was authored against fresh-fetched live exemplars + authorities this session — the Phase-1 ledger schema (`docs/ruling-rationale/2026-06-16-heb-9-phase-1-rulings.md`), current Anthropic skill-surface docs, and independent filesystem reads of the SOFIA-Reboot leg merge (`develop` @ `b35e3fda`) and the deployed `SKILL.md` byte-identity. The Notion mirror is a child of the HE-Bedrock hub and does not amend the frozen PP-0…PP-4b design ledger (§31.7).*

*End of HEB-9 SOFIA-Reboot-leg ruling-rationale ledger (R032-R034).*
