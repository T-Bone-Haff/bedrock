# File: rbt-100-execution-relay.md
# Author: Thaddeus Haffey (Executive Architect), drafted on claude.ai
# Created: 2026-08-05
# Posture: GATED TRANSACTION — eight named gates, operator go required at each.
# Ratified: six design rulings (2026-08-05) + three premise corrections.

═══════════════════════════════════════════════════════════════════════════════
BLOCK 1 — FRESH-FETCH GUARD
═══════════════════════════════════════════════════════════════════════════════

You are Claude Code working the SOFIA repository. This is an EXECUTION request
relayed by the operator. Do NOT trust this prompt's summary of any authority —
re-read each from disk or from its pinned URL. Prior-session memory is not an
authority here.

**Re-read, whole, before touching anything:**

1. `/Users/thaffey/Documents/GitHub/SOFIA/CLAUDE.md` — the branch model. Line 30
   carries the retired direct-commit exemption. 42 lines; read all of it.
2. `https://linear.app/t-bone-haff-sofia/issue/RBT-100` — the leg's authority.
   The description is the authority; the ticket carries no comments as of
   2026-08-05.
3. `/Users/thaffey/Documents/GitHub/SOFIA/.github/workflows/conformance.yml` —
   the xfail precedent's CI wiring. Lines 125–158 are the `conformance-1b` job.
4. `/Users/thaffey/Documents/GitHub/SOFIA/conformance/contracts/gateway_seam.py`
   — lines 126–131 carry the flip protocol this leg's D2 copies.
5. `/Users/thaffey/Documents/GitHub/SOFIA/conformance/README.md` — lines 104–106, the
   do-not-un-skip rule.
6. `/Users/thaffey/Documents/GitHub/SOFIA/agent-loop/pyproject.toml` — line 18,
   the `--cov-fail-under=100` addopts. 40 lines; read all of it.

**IDENTITY GATE.** Verify, and STOP-and-report on ANY mismatch — never
search-and-substitute, never "find the right repo":

- remote is `https://github.com/Haffey-Enterprises/SOFIA.git`
- `develop` is at `9229dfc35006d509632bfffd4acf1f389f73ddcc`. If it has moved,
  STOP and report the new tip — do not rebase, do not proceed on a moved base.
- you are on `develop` at that tip, OR already on
  `feature/rbt-100-civerification-commission-the-instruments-that-prove-the`
  branched from it. Any other branch: STOP and report. Do NOT create, switch,
  or delete a branch before Gate 1.
- `.github/workflows/agent-loop-tests.yml` exists and is 54 lines
- `agent-loop/tests/test_author_replay.py` exists and is 1206 lines
- `agent-loop/tests/test_author_arm.py` exists and is 697 lines
- `agent-loop/tests/test_replay_hermeticity.py` does NOT exist

**LOCK CHECK.** Check for a stale `.git/index.lock`. If one exists: STOP and
report it. Do NOT delete it — you cannot distinguish a stale lock from a live
concurrent operation, and that judgment is the operator's.

**Use read-only inspection forms throughout:** `git --no-optional-locks status`,
`git log`, `git show`, `git cat-file`. Never a form that takes a lock or
refreshes an index during inspection.

═══════════════════════════════════════════════════════════════════════════════
BLOCK 2 — TASK
═══════════════════════════════════════════════════════════════════════════════

Four deliverables. D1 arrives as pinned bytes. D2 and D3 are SPECIFICATIONS —
their exact bytes depend on runtime facts the drafting surface cannot validate
(it cannot run pytest), so they are yours to author and yours to prove. D4 is
the landing comment.

───────────────────────────────────────────────────────────────────────────────
T1 — D1: the shallow-clone canary + the expiry comment
    TRANSPORT: executor-writes. Both ends pinned.
───────────────────────────────────────────────────────────────────────────────

Replace `.github/workflows/agent-loop-tests.yml` in full with the payload at
this EXPLICIT path — resolve nothing, search for nothing:

    /Users/thaffey/Downloads/rbt-100/agent-loop-tests.yml

If that file is absent or does not match the replacement pin below, STOP and
report. Do not reconstruct the payload from this relay's prose.

- **BASE PIN** — verify BEFORE writing:
  `sha256:8d94b6b87e6fee6f262a36970be36af5b1ad3369052dae6b1ba89388ec43b2e0`
  Mismatch = the file moved since this was authored = STOP and report.
- **REPLACEMENT PIN** — verify AFTER writing, against the file on disk:
  `sha256:deea2d215ad99c125839b6672d4a8983530180846b1be629fdbd93dd02562e97`
  Mismatch = your write drifted = STOP and report. A transcription defect is
  NOT a license to edit toward the pin.

The change is exactly two hunks: the `fetch-depth: 0` comment rewritten to name
the canary as the mechanism licensing its own deletion, and a new
`agent-loop-tests-shallow` job. If your diff shows any third hunk, STOP.

**Do not rename the canary job.** Its id and `name:` are both
`agent-loop-tests-shallow`, deliberately distinct from `agent-loop-tests`. A
context-name collision would make it satisfy or fail a required status check.

**Do not add `continue-on-error`.** Its absence is the design.

───────────────────────────────────────────────────────────────────────────────
T2 — D2: the documents-layer conformance guard (RED-bearing)
    TRANSPORT: specification. You author; you prove.
───────────────────────────────────────────────────────────────────────────────

Create `agent-loop/tests/test_replay_hermeticity.py`. A NEW module — do not add
this to `test_author_replay.py` or `test_author_arm.py`, whose module-scoped
fixtures would entangle it.

**The assertion.** Build the author fixture over the two mounted tapes with a
RECORDING wrapper around the real blob reader, then assert every revision the
reader was asked for is `HEAD`:

```python
requested: list[tuple[str, str]] = []
real = build_git_document_source(REPO_ROOT)

def recording(rev: str, path: str) -> bytes | None:
    requested.append((rev, path))
    return real(rev, path)

tapes = [ReplayTape(RUNS_ROOT / name) for name in FIXTURE_RUNS]
author_fixture(tapes, prompt_path=AUTHOR_PROMPT, document_blob=recording)

non_head = sorted({rev for rev, _ in requested if rev != "HEAD"})
assert not non_head, f"non-HEAD revisions requested: {non_head}"
```

Constants mirror `test_author_replay.py` lines 59–65 (`AGENT_LOOP`, `RUNS_ROOT`,
`REPO_ROOT`, `AUTHOR_PROMPT`, `FIXTURE_RUNS`). Re-derive them; do not import
them from a test module.

**The assertion passes vacuously if the reader is never called.** That is
CORRECT and is not a loophole — after RBT-72 vendors per-pass snapshots there is
no git read to make, and "no non-HEAD revision was requested" is exactly the
claim.

**The marker.** `@pytest.mark.xfail(raises=AssertionError, strict=True, ...)`,
carrying a reason that says, in substance — wording is yours, these claims are
not:

- The documents layer's hermeticity lives in TEST DISCIPLINE, not in
  construction — unlike H17's substrate rule, which three constructors in
  `replay.py` (753–759, 1241–1247, 3324–3330) enforce by raising.
- It is false TODAY because `test_author_replay.py` (L3-T6) and
  `test_author_arm.py` (L3-T7) BOTH reconstruct pass-1 document state at their
  run's recorded `sofia_head_sha` — an obligation dischargeable only from
  committed history. **That is an obligation in conflict with the hermeticity
  rule, NOT a careless fixture.** Do not write it as carelessness.
- RBT-72's `replay.py` re-base vendors per-pass document snapshots, at which
  point the obligations are dischargeable without git and this property becomes
  true BY CONSTRUCTION — the move H17 already made. **D2 is H17's analogue for
  the documents layer.**
- `strict=True` so the flip is unmissable: an XPASS fails the suite and forces
  someone to delete the marker.
- An XPASS here is a finding to REPORT — never to un-mark, "fix", or widen in
  passing. Cite the precedent: `conformance/contracts/gateway_seam.py` lines
  126–131 and `conformance/README.md` lines 104–106.

**COMMISSIONING — the RED must be OBSERVED, not asserted.** Run the test ONCE
with the marker absent or commented out. Capture the actual failure output,
including the non-HEAD revisions it names. That capture is a required output at
Gate 2. Then apply the marker and confirm the suite reports it as `xfailed`.

**Tripwire.** If `author_fixture`'s signature is not
`(tapes, *, prompt_path, document_blob)` as stated at `replay.py:3775–3780`,
STOP and report rather than adapting.

───────────────────────────────────────────────────────────────────────────────
T3 — D3: the emissions-layer regression guard (arrives GREEN)
    TRANSPORT: specification. You author; you prove.
───────────────────────────────────────────────────────────────────────────────

Same new module. **Label it in its own docstring as a REGRESSION GUARD, NOT
EVIDENCE** — it arrives green because `641c3b35` already fixed the defect.

**The commissioning is self-proving and the synthetic fixture is the negative
control.** Do NOT commission this by reverting `test_author_replay.py:176`.

Build a synthetic author tape inside the test whose recorded `emission_path` is
a path that GENUINELY RESOLVES on this machine — a real file under `tmp_path`,
outside the tape's own folder — and whose content is a DECOY, materially
different from the tape's own vendored emission of the same file name.

Then assert both halves:

1. **The trap is armed.** Reading the recorded absolute path directly yields the
   DECOY content, and the tape's own `emissions/` copy yields different content.
   Without this the guard could pass against a path that never resolved, which
   is the exact defect class it exists to catch.
2. **The reader rebases.** The reconstructor resolves through
   `ReplayTape._emission_path` (`replay.py:634`) and reads the TAPE's copy —
   never the decoy. An un-rebased reader, as shipped before `641c3b35`, would
   read the decoy and fail this assertion.

**Tripwire.** `_emission_path` is private and reached across a class boundary.
RBT-100 records that promoting it was flagged and deliberately NOT fixed. Do not
promote it, do not add a public alias, do not refactor it. If the guard cannot
be written without touching it, STOP and report.

───────────────────────────────────────────────────────────────────────────────
T4 — the suite must remain whole
───────────────────────────────────────────────────────────────────────────────

After T1–T3, `pytest` in `agent-loop/` must report: all tests passing, exactly
one `xfailed` (D2), and 100.00% line+branch coverage per `pyproject.toml:18`.

If coverage moves off 100.00%, STOP and report the missing lines. Do NOT add a
`# pragma: no cover`, do NOT widen an omit list, and do NOT lower the gate.

───────────────────────────────────────────────────────────────────────────────
T5 — D4: the landing comment on RBT-100
───────────────────────────────────────────────────────────────────────────────

Draft it; do NOT post it. It is operator output, posted at Gate 8.

It must carry: the commits and their SHAs; the base and replacement pins for
T1; what was proven and BY WHICH INSTRUMENT; and — plainly, not by omission —
what was NOT proven. Specifically it must state that D3 is a regression guard
rather than evidence, and that the deliberation surface authoring this leg could
neither run pytest nor read check-runs, so every suite result and CI conclusion
in the record is RELAYED, not observed.

It must also carry the **premise correction ratified 2026-08-05**, added to the
ticket's existing *"What we thought before the fetch"* section — NOT applied to
the description, which stays untouched mid-leg:

> RBT-100's Item 1 asymmetry table prices the documents row as *"can a careless
> fixture break it? — Yes, and it did."* A whole read of both author-side
> modules does not sustain "careless." `test_author_replay.py` (L3-T6) and
> `test_author_arm.py` (L3-T7) each carry a document-chain obligation
> dischargeable only from committed history — `test_author_arm.py`'s is
> `test_the_arms_reconstructed_chain_closes_on_the_stored_copy`, which hashes
> the arm's reconstructed document against `STORED_FINAL`. The conforming site,
> `test_reviewer_replay.py:438`, is a unit test of the blob reader itself and
> is not reconstructing a document state at all — so the three call sites are
> not three instances of one rule with one conformer and two violators. What is
> true, and is verified rather than asserted: the fixtures are MODULE-SCOPED, so
> the dependency reaches tests with no document obligation whatever — including
> `test_recorded_chain_order_is_pass_then_sequence` and
> `test_the_reconstructed_system_block_hashes_to_every_calls_recorded_value`.
> Separately, `test_author_replay.py`'s own header (lines 12–15) claims the blob
> source is injected *"except in the L3-T6 tests"*; the module-scoped fixture
> reaches two non-L3-T6 tests, so the header over-claims its own hermeticity.
> The retrospective's *"the author-side fixtures were written so they could not
> fail"* bullet is NOT corrected — it is about the emissions layer and it stands.

═══════════════════════════════════════════════════════════════════════════════
BLOCK 3 — STOP GATE
═══════════════════════════════════════════════════════════════════════════════

**TOUCH ONLY these paths.** This is an allowlist, not a description of intent:

- `.github/workflows/agent-loop-tests.yml`   (replace)
- `agent-loop/tests/test_replay_hermeticity.py`   (create)

**Nothing else.** Not `replay.py`. Not `test_author_replay.py`. Not
`test_author_arm.py`. Not `pyproject.toml`. Not the RBT-72 spec. Not
`conformance/`. If landing this appears to require touching any of them, STOP
and surface the exact contradiction — that discovery is a finding worth having,
not an obstacle to route around.

**Stage by explicit path only.** Never `git add -A`, `-a`, or `.`. If the
working tree carries unrelated dirt, report it; it does not ride in this commit.

**POSTURE: GATED TRANSACTION.** Execute through commit → push → PR → merge →
cleanup, STOPPING at each gate below for the operator's explicit go. **Running
past a gate is never licensed.** The operator may, live at a gate, elect to
batch-authorize a named span of remaining gates; that election is theirs alone
and this relay pre-authorizes none of it. Any anomaly voids the remainder of a
batch and re-atomizes the gates.

**THE GATES:**

- **G0 — identity.** Report the identity-gate results and the T1 base-pin check.
  Report the payload file's presence and its hash. STOP.
- **G1 — branch.** Propose creating
  `feature/rbt-100-civerification-commission-the-instruments-that-prove-the`
  from `develop` at the pinned tip — the name Linear supplies for RBT-100. Do
  not create it until the go. STOP.
- **G2 — instrument commissioning.** Report: D2's OBSERVED pre-marker failure
  output verbatim, including the non-HEAD revisions named; D2 reporting
  `xfailed` once the marker is applied; D3's negative-control demonstration
  (that the decoy genuinely resolves and genuinely differs); and the full suite
  result with the coverage figure. STOP.
- **G3 — commit.** Propose the commit message and the exact staged path list as
  an artifact to ratify. Do not commit until the go. STOP.
- **G4 — push.** STOP.
- **G5 — PR open.** Report the PR number and the `semver:` label applied —
  `gates` fails closed at zero labels, so exactly one is required. Expect a
  cancelled run if the PR is created with a label already on it; that is the
  concurrency group superseding a double-fire, not an abort. STOP.
- **G6 — canary conclusion.** THE GATE THIS LEG EXISTS FOR. Report every check's
  conclusion, read from the check-runs API rather than `gh pr checks`, and name
  which reader produced which value. `agent-loop-tests-shallow` MUST be RED. If
  it is green, the leg's central premise is falsified — STOP and report that as
  a finding; do NOT proceed to merge and do NOT adjust the canary to make it
  fail. STOP.
- **G7 — merge.** Note `strict: true` is set on `develop`, so the branch must be
  up to date. STOP.
- **G8 — landing comment + cleanup.** Post D4 to RBT-100; delete the feature
  branch with `-d`, never `-D`, so git's own merged-adjudication is obtained for
  free. STOP.

═══════════════════════════════════════════════════════════════════════════════
BLOCK 4 — MUTATION RIDER
═══════════════════════════════════════════════════════════════════════════════

**Verify each target's stated FROM on disk before editing.** T1's base pin is
the FROM for the only replacement in this relay. On ANY mismatch: STOP and
report — do not reconcile by guess, and do not edit toward a pin.

**ADJUST-AND-FLAG LICENSE: NONE.** No class of discrepancy in this relay is
yours to reconcile. Every one is STOP-and-report. This is deliberate: the leg's
entire subject is what counts as evidence, and an executor smoothing a
discrepancy is the failure mode it exists to instrument.

**Reading the full content or diff before landing is sanctioned conduct**, not
instruction-creep. Anything it surfaces arrives as GATE INPUT — never as a
license to edit.

**A refusal with reasons is sanctioned output, not a failure.** If any task here
is mis-scoped, under-determined, or asks for a judgment this relay does not
supply, say so and say why. Refusals across this programme stand at n = 11
across six relays; seven were caught by the executor rather than by drafting,
and the eleventh was against the session record of this very work. Your reasons
are read as feedback on the relay's scoping.

**Do not narrate completion past a gate.** A done-story reads as a fact to
ratify rather than a request to gate. Report what you did as data to verify.
