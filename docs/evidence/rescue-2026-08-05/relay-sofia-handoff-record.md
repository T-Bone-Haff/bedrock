═══════════════════════════════════════════════════════════════════════════
  SOFIA — commit the RBT-72 phase-1b session handoff record.
  Transport: PRE-PLACED (one new file). Posture: GATED TRANSACTION.
  Branch → commit → push → PR into `develop`. MERGE NOT AUTHORIZED.
  Authored on claude.ai 2026-07-29.
═══════════════════════════════════════════════════════════════════════════

**What this is.** The phase-1b handoff record exists only in `~/Downloads`.
It governs unfinished work — Steps 3 and 4 unbuilt, the Piece 2 trim on hold,
the cascade baseline, two rulings surfaced and unresolved — and a downloads
folder is not a durable home. This lands it in the archive beside the three
prior handoffs.

**It is not the harness work.** Do not branch from
`feature/rbt-72-phase-1b-harness`; that branch carries unmerged code and this
record is independent of its fate.

═══ FRESH-FETCH GUARD ═══════════════════════════════════════════════════

You are Claude Code in the **SOFIA** repository. This is an EXECUTION request
relayed by Tad. Re-read from disk, by explicit path — do not trust this
prompt's summary or prior-session memory:

  /Users/thaffey/Documents/GitHub/SOFIA/CLAUDE.md
  /Users/thaffey/Documents/GitHub/vault/CLAUDE.md

**Note the branch rule you will find there and obey it over anything you
remember:** `feature/*` → `develop` → `main`, via PRs. The prior
direct-commit exemption for deliberation artifacts is **retired** (ruled at
the RBT-10 session, 2026-07-22). This record lands via PR like everything
else.

IDENTITY GATE — verify and report each:

  1. remote origin = https://github.com/Haffey-Enterprises/SOFIA.git
  2. `develop` = 73b42b0bc9adb987d53ec225863472850c4d3ef2
  3. current branch = `feature/rbt-72-phase-1b-harness` at
     24a225a45f953e68c7f8c1593ff8a5444550c391 — the harness leg, untouched
     by this transaction
  4. `git --no-optional-locks status --porcelain` shows **exactly one** entry:
     `?? docs/session-archive/2026-07-29-session-handoff-rbt-72-phase-1b.md`

Use `git --no-optional-locks` for every status check. On ANY mismatch: STOP.

═══ PRE-GATE — verify the one target, then STOP ═════════════════════════

**Transport is PRE-PLACED.** The bytes are on disk. You verify; you do not
write.

  docs/session-archive/2026-07-29-session-handoff-rbt-72-phase-1b.md
    REPLACEMENT 40b62721278cd20172470811b24b0f2e7c8aad85f07b34f4c9848b662ffc8827
    9,656 bytes

No base pin: the path is new. **Assert `git cat-file -e
develop:docs/session-archive/2026-07-29-session-handoff-rbt-72-phase-1b.md`
FAILS.**

**Assert nothing else in the tree has moved** — one porcelain entry, and the
five paths of the harness leg are already committed at `24a225a4`.

Then STOP.

── GATE B — BRANCH FROM `develop`, NOT FROM HERE ─────────────────────────

    git checkout develop
    git checkout -b feature/rbt-72-phase-1b-handoff-record

The untracked file carries across both checkouts. **Confirm after each:** the
branch name, that HEAD is now `73b42b0b…`, and that porcelain still shows the
one untracked entry.

If `git checkout develop` reports anything other than a clean switch — a
carried modification, a conflict, a detached state — **STOP.** The harness
branch must be left exactly as found.

Then STOP.

── GATE C — COMMIT ───────────────────────────────────────────────────────

    git add docs/session-archive/2026-07-29-session-handoff-rbt-72-phase-1b.md

**One path, named explicitly. Never `-A`, `-a`, or `.`** Confirm one staged
and nothing else.

Commit message, verbatim:

```
RBT-72: archive the phase-1b session handoff record

The handoff record written at phase-1b standdown, moved from a downloads
folder into the archive beside the three prior session handoffs.

It governs unfinished work and is therefore not disposable: replay.py and
the Step 4 gates are unbuilt; the Piece 2 prose trim is held pending HEB-86;
the cascade baseline is frozen at 24a225a4; and two items are surfaced
awaiting a ruling — RBT-92 Item 4, and the double-malformation policy gap
carried to Step 3.

Contains no code and no design change. The harness leg at
feature/rbt-72-phase-1b-harness is untouched by this transaction.

Refs RBT-72.
```

Then STOP.

── GATE C-V — VERIFY ─────────────────────────────────────────────────────

Report: the commit SHA; sole parent `73b42b0b…`; `git diff --name-only
HEAD~1 HEAD` = exactly one path; the file re-hashed **out of the commit**
(`git show HEAD:<path> | shasum -a 256`) against `40b62721…`; `git log -1
--format=%B` verbatim; porcelain empty.

**Also confirm `feature/rbt-72-phase-1b-harness` still points at
`24a225a4…`** — the leg you branched away from must be exactly as found.

Then STOP.

── GATE D — PUSH ─────────────────────────────────────────────────────────

    git push -u origin feature/rbt-72-phase-1b-handoff-record

Report the remote ref and the SHA it points at, read from `git ls-remote`
rather than from a local tracking ref. Then STOP.

── GATE E — OPEN THE PR INTO `develop` ───────────────────────────────────

Base **`develop`** — not `main`. Title:

    RBT-72: archive the phase-1b session handoff record

Body: the commit message body, plus:

```
Documentation only — one new file under docs/session-archive/. No code, no
design change, no contract amended. The harness leg at
feature/rbt-72-phase-1b-harness is untouched and remains unmerged at
24a225a4.
```

Report the PR number and URL, and **report what CI checks fire and their
status. Do not fix a red check** — report it as gate input and STOP.

═══ STOP GATE ═══════════════════════════════════════════════════════════

Touch only, and stage only:

    docs/session-archive/2026-07-29-session-handoff-rbt-72-phase-1b.md

**NOT authorized at any point:**

  ✗ **merge** — a separate ratification, not in this relay
  ✗ any commit to `develop` or `main`
  ✗ any change to `feature/rbt-72-phase-1b-harness`, its commits, or its
    branch pointer
  ✗ tag, release, force-push, auto-merge, branch deletion
  ✗ any edit to any file — the bytes are ratified
  ✗ `agent-loop/**` — nothing under the construct moves here
  ✗ deleting the copy in `~/Downloads` — the operator sweeps that
  ✗ any Linear ticket

**Each of the pre-gate, B, C, C-V, D and E is its own gate requiring Tad's
explicit go.** Running past a gate is never licensed. He may elect, live at a
gate, to batch a named span of the remainder; that election is his at
transaction time and this relay does not pre-authorize it.

═══ MUTATION RIDER ══════════════════════════════════════════════════════

**This transaction mutates no existing file.** It adds one, and the rest of
the mutations are to git history and the remote — each gated.

ADJUST-AND-FLAG LICENCE: **none.** Declared spent at completion.

TRIPWIRES:
  · `develop` ≠ `73b42b0b…` → the base moved → STOP.
  · REPLACEMENT pin ≠ `40b62721…` → the file is not the ratified bytes →
    STOP, reporting both computed and expected.
  · The harness branch pointer moving at any time → STOP.
  · A second path in porcelain at any point → STOP.
  · `git checkout develop` reporting a carried modification → STOP.
  · Any instruction here contradicting the tree → the tree wins, you STOP.

═══ ON COMPLETION ═══════════════════════════════════════════════════════

Report the commit SHA and the PR URL. A third surface will re-hash the
landed file against the pin above; your account of having verified is itself
a claim.

The merge is Tad's, in a later transaction, and is not licensed here.
