# Reference: Non-Deterministic Components

How to test code whose behavior includes LLM judgment. The TDD sequence and the always-apply invariants are in `SKILL.md`; this is the discipline for the components where "run it again" doesn't give the same answer. The governing split is one sentence: **mechanical gates get deterministic tests; judgments get eval harnesses.**

## 1. The split — and what it does not exempt

Partition the component the way `agent-code`'s execute-vs-reason bright line already requires: judgment steps (LLM calls) vs. mechanism (deterministic code). Then:

- **Every mechanism is tested exactly as this skill always demands** — TDD sequence, meaningful red, coverage floor, no exceptions. Parsers, admission gates, identity derivation, routers, evidence verifiers: all deterministic, all unit-tested, all at threshold. The presence of an LLM in the system exempts nothing around it — the reference instantiation (the SOFIA agent-loop) holds 100% line+branch coverage on its runner precisely because the runner is mechanism.
- **Judgment steps get eval harnesses** — the disciplines below. An eval harness is not a weaker unit test; it is a different instrument for a different object: a distribution of behavior rather than a fixed input/output contract.

The classic failure this split prevents: mocking the LLM and calling the system tested (the mechanism was tested; the judgment never was), or conversely treating the whole system as untestable because one step is non-deterministic.

## 2. Recorded-fixture regression

Captured real outputs are the cheapest eval substrate you will ever own.

- **Capture verbatim at the seam.** Raw model response bodies, persisted before parsing, become replay fixtures for free — the parse seam, the validators, and the downstream mechanism can all be regression-tested against real emissions at $0 per run.
- **Replay before you spend.** A captured run answers most what-happened and does-it-still-parse questions without a live call. New live spend is for genuinely emergent questions a fixture cannot answer.
- **Fixture outcomes are data, not aspiration.** A replay suite asserts what the system *does* with real captured inputs — including the malformed ones. Keep the malformed emissions; they are the regression suite for the tolerance layers.

## 3. LLM-as-judge, calibrated cold

When a judgment's quality is itself scored by a model (or by hand-rules over model output), the judge earns trust the same way any instrument does — by calibration against known answers, never by plausibility:

- **Pre-register the pass criteria before the run.** Criteria committed in advance (in the spec, in git) — so the scoring cannot rationalize whatever happens. When you are both experimenter and audience, hindsight rationalization is the default failure mode.
- **Score cold, against ground truth.** Judge outputs are hand-audited after the run, against the actual inputs — not live, and not by trusting the judge's own confidence. Low-confidence judgments get individually checked.
- **Watch the judge's error asymmetry.** A judge on a load-bearing path is biased fail-safe, and the calibration checks that the bias held — a false "pass" from a judge is the silent error; a false "fail" costs one glance.

The full instrument-operating discipline — how many draws buy recall, positive controls, generation change-control, attribution — lives in `design-review-loop`'s operating-the-instrument reference for the loop family; carry those laws from there when you are operating that class of instrument, and treat their transfer to a new instrument family as a design bet to be proven, not an inheritance.

## 4. Meaningful red for a judgment

The TDD sequence's observed-red rule has an honest rebind for judgment steps: the "failing test" is a **behavioral eval with a pre-registered pass criterion, observed failing before the charter earns it**. A charter change that claims to fix a behavior owes the same evidence a bug fix owes — the eval that failed before, passing after, on the same fixtures. What does *not* qualify: eyeballing one good output and declaring the behavior present — that is the judgment-world equivalent of a test that never ran red.

## 5. Cost discipline in test design

Eval harnesses spend real tokens. The spend rules apply to test design too: replay captured fixtures before buying live calls; bound live evals to the passes the criterion needs; a deterministic assertion over captured state needs no live event at all.
