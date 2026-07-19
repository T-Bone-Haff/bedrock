---
name: design-review-loop
description: Run a stance-isolated, authority-cited, arbiter-gated review of a design-record set (ADR/DDR/SDD) driven to mechanical convergence. Spins up the three review hats (LAA / SA / EA) plus a cross-set coherence sweep as isolated instruments, classifies each finding resolvable-vs-decision-bearing, and drives a mechanical convergence gate that halts only to surface a decision the operator has not made. Use whenever reviewing a decision-record set, driving an ADR/DDR/SDD set to convergence, verifying an amendment batch, or asking "review these design records", "is this design-record set ready", "run the design-review loop". Reviews design records against canonical authorities + stated design intent; reviewing a finished code change is the code-review skill — this cites it for the shared LAA/SA/EA role-name authority and the BLOCKING/MATERIAL/COSMETIC/POSITIVE ladder. Assumes the SOFIA agent-loop runner as its machinery; a different doctype family or substrate corpus is a rebind.
---

# Design-Review Loop

Driving a **set** of design records (ADR / DDR / SDD) to convergence by stance-isolated adversarial review, gated so the loop halts only to surface a decision the operator has not yet made. This SKILL.md carries the method, the invariants, and the operator contract; the `references/` carry the runnable instrument charters and the convergence machinery this skill governs but does not re-implement.

**Binding:** design-record sets reviewed against a ratified **canonical-authority + stated-design-intent** substrate, run on the SOFIA `agent-loop` machinery (`$SOFIA_ROOT/agent-loop/`). The machinery, the substrate corpus, and the doctype family are the binding — declared, not hidden. A materially different binding (a non-ADR/DDR/SDD doctype family, a different authority corpus, a different runner) is a **rebind**: re-derive the stances and the authority binding, don't line-edit. The mechanical spine below is the portable part.

## What this is, and what it is not

`code-review` owns the **three-hat method** (LAA / SA / EA), the role-name authority, and the `BLOCKING / MATERIAL / COSMETIC / POSITIVE` ladder — and it is **code-scoped**: its SA hat runs a code-conformance checklist, its trigger is a diff or PR, and it is a **single-pass** review of a **single change**. This skill is the design-record adaptation, and it differs **in kind**, not degree:

- **Cardinality.** The subject is a *set* of records reviewed together, not one change.
- **SA's authority.** SA conforms records to **canonical authorities + design intent**, not a code checklist.
- **A coherence sweep.** A fourth instrument checks the set *against itself* — the blind spot author and reviewer share.
- **An arbiter and a gate.** Findings are classified and driven to **mechanical convergence** across passes; the loop halts only on a decision the operator must make.
- **An operator loop.** Decision-bearing findings are surfaced unbundled for per-item ratification, and the ruling becomes authority for the next pass.

So: reviewing a **code change** → `code-review`. Reviewing or converging a **design-record set** → here. `code-review` is the **authority** for the LAA/SA/EA expansions and the `BLOCKING / MATERIAL / COSMETIC / POSITIVE` ladder — one house vocabulary, defined once there. The discriminating axis for where it may be inlined: a charter that is **LLM-consumed** inlines the expansion (the agent-loop convention — a charter must not depend on a cross-reference it cannot follow at inference time); **governing prose** points rather than re-defines. This skill follows that split — the reviewer charters carry the expansions inline, this document uses the acronyms and cites the authority.

### Two operating scenarios — name which one you are in

- **Drive-to-convergence.** An unsettled set worked from wherever it is toward convergence. The primary scenario; the full roster runs every pass.
- **Verification pass.** An already-deliberated, near-final batch checked for defects and confirmed. Legitimate, but it is *not* the convergence scenario, and it must not narrate itself as one. The roster-per-pass rule may legitimately differ (a verification pass may re-run a subset) — but that is a rule the runner applies, not operator discretion, and the choice is recorded.

## The loop

One pass over the set:

1. **Assemble, fetched fresh.** The full document set (per-pass fresh) + the frozen per-run substrate + an immutable prior-pass ledger snapshot. Each reviewer gets its own frozen copy.
2. **Review, in isolation.** The three hats and (when scheduled) the coherence sweep each run as their **own LLM call in their own context**, judging from one altitude's authority only, unable to see any other reviewer's current-pass output. (`references/reviewer-instrument.md`.)
3. **Gather, then admit.** All scheduled reviewers finish; *then* their emissions are admitted through the mechanical admission gate in a fixed order. No admission interleaves with any review.
4. **Classify.** The arbiter classifies each admitted open finding `resolvable` vs `decision-bearing`, one isolated call per finding, biased conservative. (`references/arbiter-classifier.md`.)
5. **Route.** The mechanical gate composes the ledger state into exactly one of three exits — `CONVERGED`, `CONTINUE`, `HALT_DECISION`. (`references/convergence-machinery.md`.)

Across passes: `CONTINUE` returns to the author (fix the resolvable findings) and loops; `HALT_DECISION` surfaces to the operator; `CONVERGED` ends the run.

## Load-bearing invariants

- **Stance isolation, not content isolation.** Each hat sees the whole set, the whole substrate, the whole prior-pass ledger — full visibility — and judges from **one altitude's authority only**. Full visibility preserves seam findings; single-altitude judgment is what makes the roster a set of independent probes rather than one confirmation.
- **No cross-anchoring.** A reviewer reads an immutable prior-pass ledger snapshot, never the mutating in-pass ledger, and never another reviewer's current-pass findings. Findings are joined post-hoc, by the arbiter alone. Because every reviewer's input is a frozen snapshot, parallel and sequential scheduling are equivalent — scheduling sits *below* this invariant, not in place of it.
- **A finding cites authority or it is dropped.** Every finding carries a well-formed `cited_authority` (canonical / design-intent / coherence / soundness). "I'd have designed it differently" is not a finding; the admission gate drops it mechanically. The gate checks the citation's *shape*; the honesty of the citation lives in the reviewer charter, and nothing downstream can enforce it — so the charter carries that discipline explicitly.
- **The execute-vs-reason bright line.** The **judgment** steps (the hats, the arbiter) are LLM calls carrying verbatim charters. The **deterministic** steps — ledger read/write, admission, `hash`-identity and dedup, the counter/oscillation/router gate, the instrument-compromised and sanctioned-empty guards — are **executed against the runner (`$SOFIA_ROOT/agent-loop/agent_loop/`), never reasoned by the model.** An agent handed this construct will faithfully run the charters and *reason* the machinery unless the line is bright — and a reasoned gate is an LLM deciding "done," which is the one thing the loop exists to forbid. If the runner cannot be executed, see *Emulation* below; do not reason the machinery in its place.
- **No LLM on the "done" decision.** `CONVERGED` is a mechanical conjunction over ledger state and arbiter labels (`open_cbm == 0 ∧ no open decision-bearing finding ∧ not oscillating`). The counter counts; the router composes booleans. A smart agent that could judge "we're done" would re-import the anchoring the whole construct escapes.
- **The arbiter is the only LLM judgment on the exit path.** Everything downstream trusts its label, so it is biased to fail safe (unsure → `decision-bearing`).

## The instruments

Four stance-isolated reviewers, each a negative test biased toward rejection — the counterweight to the confirmation bias the three-hat method otherwise carries. Charters are near-verbatim in `references/reviewer-instrument.md`; the LAA/SA/EA expansions and the severity ladder are `code-review`'s authority (expanded once below for orientation, inlined in the charters per the convention above). Each line names the acronym and the **design-record** question that altitude asks — the adaptation this skill owns.

- **LAA — Lead Application Architect — *what does this record decide?*** Claim-fidelity and scope: does each record decide what it claims, no more (smuggled decisions) and no less; are dependencies and consequences declared.
- **SA — Solution Architect — *how does this record conform, and is it sound?*** Conformance to each ratified canonical authority in scope (the design-record adaptation: authorities, **not** a code checklist), plus internal correctness, cross-reference resolution, and substantiation of claimed gates.
- **EA — Enterprise Architect — *should this stand, in this shape, at this time?*** Integration with system posture, reversibility proportionate to risk, whether a position deserves its own decision record first, timing.
- **Coherence sweep — cross-set.** Not an altitude and not an antagonist hat: it checks the set **against itself** — internal, cross-document, and narrative-vs-substrate consistency — closing the blind spot author and reviewer share. Runner-scheduled: pass 1, then re-run after any pass that recorded a document change.

POSITIVE findings are **survived-attack records**, not praise: a load-bearing surface was deliberately attacked and it held. Required and proportionate — a review with no POSITIVEs verified nothing, it only flagged what broke.

## The arbiter

One classification per finding, in isolation, authority fetched fresh: **`resolvable`** (an already-ratified authority + locus *determines* the fix — name it, or it is not resolvable) vs **`decision-bearing`** (resolving it requires a choice not yet ratified — a silence, an unratified fork, a newly-discovered choice, or an unresolved authority conflict). Conservative by construction, because the two errors are not symmetric: a false `resolvable` silently manufactures the operator's alignment — the loop resolves, on its own, a choice he never made — which is invisible and unrecoverable; a false `decision-bearing` costs one glance at an escalation he waves through. Escalate when unsure. POSITIVEs are never classified. (`references/arbiter-classifier.md`.)

## The convergence machinery

The counter, the oscillation detector, and the router are pure functions over ledger state — **run, not reasoned** (see the bright line). `references/convergence-machinery.md` points to the runnable implementation and its spec and states the minimal ledger contract; it deliberately does not re-specify the gate in prose, because a prose gate is what gets emulated. Two facts the operator must hold:

- **`decision-bearing` gates convergence regardless of severity.** An open decision-bearing finding halts the loop *even if* `open_cbm == 0` — even a COSMETIC one. Silently auto-resolving or silently dropping a discovered decision, however small, is the manufactured-alignment failure the loop exists to prevent.
- **A non-decreasing open set is a decision, not a failure — and it splits two ways.** **Recurrence** (a finding closed then reopened) halts as **`oscillation`**: two altitudes are genuinely trading fixes and no higher authority settles it. **Plateau without recurrence** (the open counted count stops strictly decreasing while positive) halts as **`non-convergence`**: accumulation the operator must come rule, *not* a fight. Either surfaces to the operator *as a decision*, carrying the recurring/plateaued findings as payload (RBT-69 Piece 3 split the honest labels apart).

## The author rule

The author fixes **only `resolvable` findings, and only by conforming to the cited authority** — never by adopting a hat's suggested fix. A suggested fix can smuggle a decision; the fix is *derived* from the authority the arbiter named, or it is not made. Decision-bearing findings are never "fixed" by the loop — they are ruled by the operator, and the ruling is what the next pass conforms to.

## The operator loop (dual-operator)

This skill serves **both a human operator and an agent operator through one seam** — the same inputs (record set + frozen substrate), the same convergence signal, the same escalation shape — so the loop does not know or care which is on the other side. On `HALT_DECISION`:

- **Surface unbundled, one finding at a time.** One escalation per finding; bundling decisions is the opposite of ratify-one-at-a-time. Each escalation carries the finding, why the arbiter judged it decision-bearing, a **direct recommended disposition with rationale** (never a bare menu; no multiple-choice popup), and the honest empirical floor where the evidence is thin.
- **The ruling becomes ratified authority.** Once ruled, a decision-bearing finding becomes `resolvable` (or is closed) and the loop proceeds; the ruling is substrate for the next pass.

**Two halt classes, kept distinct.** The **mechanical router-halt** fires on a decision-bearing *finding* — it is the loop's own halt. An **authoring-gate ratification** is a different gate: it fires on a decision being *made* while authoring or amending a record, and it is owned by `author-decision-record` (its deliberation gate), pointed to here, not restated. An operator experiences both; do not route an authoring decision through the finding-classifier, or a finding through the authoring gate.

## Substrate and documents

- **Documents are per-pass fresh; substrate is per-run frozen.** Authorities changing mid-run would make findings non-reproducible and the audit incoherent; the reviewed documents evolve as the author fixes, so they are re-read each pass.
- **Substrate-selection rule.** For a review target, substrate = the ratified canonical authorities in scope + the stated design intent — **and it must include the mechanization the target claims to conform to.** A conformance check that cannot see what a record claims to match is toothless; this is a rule, not operator discretion.
- **Arbiter authority = the frozen per-run substrate**, not an operator-curated summary. Curating what the arbiter sees pre-shapes the one load-bearing classification by inclusion and omission — an independence leak on the exact seam that must stay clean.

## The cold post-run audit

A run's findings earn trust only under a **cold** audit — done after the run, never live (live scoring produces rushed judgments and misses the run). Each admitted finding is hand-ruled on validity, stance-fit, duplication, and baseline-match, against the fetched documents and substrate as ground truth; plus per-hat cost and an arbiter hand-check of every low-confidence classification. The audit's findings-about-the-instrument route back to these charters as amendments; findings-about-the-documents route to the normal tracker split. The stabilized validity vocabulary in practice — TRUE / TRUE- / OVER / FALSE-POS / HELD-MIS-SEV — is the current working vocabulary; leverage it, and treat it as not-yet-locked (its calibration semantics live in the run line, not this skill). Full audit shape: `$SOFIA_ROOT/agent-loop/design/run-supervision.protocol.md`.

## What is ratified, and what is held

Package the method honestly. **Ratified and load-bearing:** the stance-isolated roster, the arbiter classification, the mechanical spine (no-LLM-on-done, conservative arbiter bias, operator-unbundled escalation) — exercised across ~15 runs, four design-record targets, eight instrument generations. **Held, not resolved:** the automated convergence loop is nascent (looping has been operator-driven or emulated, not a full autonomous runner pass end-to-end); the three-hat roster's independence-per-cost is an open empirical question fenced against restructuring on a single sample; cross-domain transfer of the spine is unobserved, which is why this skill is authored rebind-ready but **not** generalized into a framework.

**Honest value.** The loop sells **reproducibility, honest convergence, correct operator-routing, and auditability** — not "finds more defects than a sharp adversarial read." The value engine is the adversarial framing plus a skeptic reading the real authorities; the machinery is the trust-and-safety-and-reproducibility layer around that engine. Do not price fidelity as depth.

## Emulation (the sanctioned exit)

When the runner cannot be executed, a manual review is permitted **only** as an explicitly-declared, non-autonomous **dry read** that (a) states which invariants were hand-applied and are therefore unguaranteed, and (b) **may not claim convergence** — because "converged" without a mechanical counter over a durable ledger is an LLM judgment, the one thing the construct forbids. An agent that cannot run the machinery is not blocked from a sharp adversarial review; it just cannot call the result a converged loop run. This is the pressure's fail-safe exit: at the cap, drop the claim — never relabel a reasoned gate as a real one.

## Where to look

- `references/reviewer-instrument.md` — the four stance-isolated reviewer charters (shared Contract factored once; the four `### Stance` blocks are the rebind surface).
- `references/arbiter-classifier.md` — the arbiter charter (resolvable/decision-bearing, conservative bias, output schema).
- `references/convergence-machinery.md` — pointer to the runnable gate + ledger, and the minimal ledger contract; the machinery you **run**, not reason.
- **Reference instantiation** — `$SOFIA_ROOT/agent-loop/`: `design/` (the specs this skill forward-authors from), `agent_loop/` (the runner), `runs/` (real run artifacts). The runner execution and the first skill-driven convergence run are tracked in **RBT-67**.
- **Authority cited** — `code-review` (LAA/SA/EA expansions + the severity ladder); `author-decision-record` (the authoring-gate deliberation discipline).
