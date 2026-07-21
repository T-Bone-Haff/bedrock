# Convergence Machinery — run it, don't reason it

The counter, the oscillation detector, and the router are **pure functions over ledger state**. This file is deliberately **not** a re-specification of that logic — a prose gate is exactly what an agent emulates instead of executing, which silently reintroduces an LLM deciding "done." This file **points** to the runnable authority and states the **data contract** an operator must understand to read a run. The logic itself is executed, never reasoned (the execute-vs-reason bright line).

## Authority — where the machinery actually lives

- **Executable implementation:** `$SOFIA_ROOT/agent-loop/agent_loop/` — `gates.py` (counter / oscillation / router), `ledger.py` (durable store), `admission.py` (the admission gate), `identity.py` (finding identity), `arbiter.py` (the classifier port). **This is what runs.**
- **Specification:** `$SOFIA_ROOT/agent-loop/design/mechanical-gates.md` and `ledger-schema.md`. On any divergence between this summary and those, **the spec + implementation are authority.**
- **Run harness / prep:** `run-prep.contract.md` (run folder, frozen substrate, prep gates), `run-supervision.protocol.md` (attended-run discipline).

To run the gate: **execute the runner.** Do not hand-evaluate the router from a ledger you are reasoning about — that is emulation, and emulation may not claim convergence (see SKILL.md § Emulation).

## The three exits (what the router produces — not how)

The router evaluates ledger state and produces exactly one of:

- **`HALT_DECISION`** — surfaced to the operator, one finding at a time, unbundled. Its `reason` is one of three: an open `decision-bearing` finding (this takes precedence over convergence — it halts the loop **even if the counted-severity count is zero**, even a COSMETIC one); **`oscillation`** — a closed finding reopened (recurrence: real two-altitude trading); or **`non-convergence`** — the open counted set stopped strictly decreasing with no recurrence (plateau: accumulation the operator must come rule). The oscillation/non-convergence split is deliberate — see the two facts below.
- **`CONVERGED`** — the mechanical conjunction: `open_cbm == 0` **and** no open `decision-bearing` finding **and** not oscillating (neither recurrence nor plateau). No LLM anywhere in this decision.
- **`CONTINUE`** — open counted-severity findings remain and all open findings are `resolvable`: back to the author.

`open_cbm` = count of open findings whose severity is in the counted set. The backstop splits two conditions the single "oscillation" label used to conflate: **recurrence** — a finding closed then reopened — halts as **`oscillation`** (real two-altitude trading); **plateau** — the open counted-severity count failing to strictly decrease over a `plateau_N`-pass window, with no recurrence — halts as **`non-convergence`** (accumulation the operator must come rule, *not* two altitudes fighting). `oscillating = recurrence or plateau` is retained only as the internal top-precedence backstop predicate; the router disposition it produces is now split. Each carries its recurring/plateaued findings as payload, unbundled; precedence is unchanged — the backstop still outranks the open-resolvable `CONTINUE` and the static decision-halt.

## Minimal ledger contract (the fields the machinery reads)

The ledger is the durable spine — the single source of continuity; every reviewer, the arbiter, and the gate read it fresh, no agent inherits another's context. The load-bearing fields (full schema in `design/ledger-schema.md`):

- **`id`** — stable finding identity across passes, derived once at first emission from `hash(sorted(target) + normalize_locus(locus) + altitude)` and **preserved** thereafter — **`altitude` is in the key; `claim` is not**. Minting a fresh id each pass silently disables oscillation detection (a reopened finding would look brand-new); keying on the claim sentence did the same softer damage — a hat re-emitting the same finding with the claim reworded minted a fresh id each pass and inflated `open_cbm`, so the discriminator moved from the brittle claim sentence to the stable stance-at-locus. Keying on locus *alone* is forbidden (one locus legitimately carries several distinct-altitude findings). The residual risk — two genuinely-distinct findings at one `(target, locus, altitude)` — is caught by a **claim-divergence guard**: on a `dedup_open` where `normalize_claim(incoming) != normalize_claim(existing)`, the finding stays open, the incoming claim is preserved in `claim_variants`, and a `claim_divergence` event is logged — never a hidden finding, never a discarded claim. `normalize_locus` (formatting drift only; section anchors preserved) is the one place worth its own test.
- **`severity`** — the house ladder; `counted_severities = {BLOCKING, MATERIAL}` is the convergence-counted set. `COSMETIC`/`POSITIVE` never count and never block.
- **`classification`** — `unclassified` → `resolvable` | `decision-bearing`, set by the arbiter. Orthogonal to severity: a decision-bearing finding halts regardless of severity.
- **`status`** — `open` | `closed` | `escalated`. **`recurrence_count`** increments when a previously-`closed` id is re-admitted `open` (the reopen signal for oscillation).
- **Pass record** — `open_cbm_count` snapshotted **at routing time** (post-admission, post-arbiter, pre-author): one value, read by both the router and the plateau check, no drift.
- **Doc-change log** — records which document a (proposed) fix changed, in which pass; the coherence sweep re-runs after any pass that recorded a change. Kept separate from the pass record on purpose (the pass snapshot is pre-author; doc-changes are written post-routing).

## The admission gate (mechanical scope enforcement)

Before a finding enters the ledger it passes a **structural** check: `cited_authority` is present and well-formed (one of the four kinds, non-empty `ref`). A null citation, or a bare preference, is **dropped and never counted**. The gate enforces citation *shape*, not *honesty* — honesty lives in the reviewer charters.

## The guards (fail-loud, never a false CONVERGED)

- **Instrument-compromised.** A pass in which any scheduled reviewer produced ≥1 parse-dropped emission and **0** admitted findings is instrument-compromised: the runner aborts loudly (a fully-dropped reviewer must never let `CONVERGED` be reachable). Partial drops and legitimately-empty emissions do not trip it.
- **Sanctioned-empty is a violation.** An entirely empty reviewer array is a protocol violation, not a legal "nothing to report" — the charter requires at least the strongest survived attacks as POSITIVEs. Emptiness never counts as convergence.

These are the reasons the machinery is executed, not reasoned: each guard is a place where a hand-run would quietly skip the check and report a false "done."
