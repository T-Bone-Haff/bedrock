═══════════════════════════════════════════════════════════════════════════
RBT-93 · RELAY 08 — register v0.10.0 + adopt the template of record
Posture: GATED TRANSACTION. Two gates: commit, then push. Separately given.
═══════════════════════════════════════════════════════════════════════════

═══ FRESH-FETCH GUARD ═══

You are Claude Code working in `~/Documents/GitHub/ops`. This is an EXECUTION
request relayed by the operator (Tad). Do not trust this prompt's summary of any
file — read every artifact from disk yourself. Do not carry any premise from a
prior session.

IDENTITY GATE. Verify all of the following before touching anything. On ANY
mismatch: STOP and report. Never search for a substitute repository, branch or
file.

  G1. `git --no-optional-locks remote -v` → origin is
      https://github.com/Haffey-Enterprises/ops.git
  G2. `git --no-optional-locks symbolic-ref --short HEAD` → `main`
  G3. `git --no-optional-locks rev-parse HEAD origin/main main` → all three are
      364e6655d984a5e173ce7ef36aa5febae8c8bbe1
  G4. `git --no-optional-locks status --porcelain` → EMPTY except for the two
      pre-placed files named in G6. Any other modified or untracked path: STOP
      and report it; do not stash, clean, or commit around it.
  G5. LOCK CHECK. `ls -la .git/index.lock .git/*.lock .git/refs/**/*.lock`
      → report anything found and STOP. DO NOT DELETE A LOCK. You cannot
      distinguish a stale lock from a live concurrent operation and that
      judgment is the operator's. (One was left at `.git/index.lock` earlier
      today by a read through a network mount and the operator has removed it;
      if one is present again, it is new information.)
  G6. PRE-PLACED PAYLOADS. The operator has placed two files. Verify each by
      SHA-256 before use. On mismatch: STOP.

        (a) `<EDIT_SET_PATH>` — the edit set. NOT part of the repository; it is
            an instruction artifact. Read it WHOLE before making any edit.
        (b) `./dashboard.html` — the replacement template, already in the working
            tree, replacing the tracked file.
            expected sha256: b71ca6a8d3a260b693a303d7d3713b9663915f2b1c40169ba568bf25c038c8cb
            base (what it replaces), from `git show HEAD:dashboard.html`:
            expected sha256: 1ce4866dfd450ef2e03f0dee06bc5640d4c6464911a080b2cfa87f0903175283

  G7. BASE PIN for the file you will edit:
      `git show HEAD:register.md | shasum -a 256` →
      63798b6abdbbe6542b0a12f9542734bfe24c7a069e32421e286821e1a8a003d8
      and the working-tree copy must hash the same.
  G8. MUTATION SURFACES. Report (do not change) whether this repository has git
      hooks in `.git/hooks` beyond the samples, a configured `commit.template`,
      or any `core.autocrlf` / filter setting that would rewrite content on
      write. This check is cheap and fails early; it is not what makes the pins
      sound — the post-write re-hash is.

There is no `CLAUDE.md` in this repository at `364e665`. If a user-level or
enclosing-directory doctrine file governs your conduct here, it governs; this
relay cites no path for it because none exists in the repo to cite.

═══ TASK ═══

T1. Read `<EDIT_SET_PATH>` whole.

T2. Resolve the single fill slot. Every literal `<LANDING_DATE>` token in the
    edit set is a named slot. Rule: **the UTC date on which you make the commit
    in T8, formatted `YYYY-MM-DD`.** Compute it once, state the value in your
    report, and use it for every occurrence. Nothing else in any payload is a
    slot. If you cannot determine the UTC date with certainty, STOP and ask.

T3. Capture the §4 pre-state. §4 runs from the line beginning
    `## 4. Weekly consumption` up to but excluding the line beginning
    `## 5. Monthly snapshots`. Extract and hash that range; record the value.

T4. Apply edits E1 through E9 from the edit set, in order, to `register.md`.
    For EACH edit: locate the verbatim FROM anchor on disk and confirm it occurs
    EXACTLY ONCE. If it is absent, or occurs more than once, STOP and report
    which edit and what you found — do not reconcile by guess, do not choose an
    occurrence, do not adjust the anchor to fit.

    E4c and E7 and E8 and E9 are INSERTIONS. They add lines and change no
    existing byte. Verify that property after applying each: the surrounding
    text must be byte-identical to what it was.

T5. Re-capture the §4 range and hash it. It MUST equal T3's value. If it does
    not, STOP — §4 belongs to the collector and this surface does not move
    those bytes.

T6. Verify the template adoption: `dashboard.html` in the working tree still
    hashes to b71ca6a8…c8cb, and `git diff --stat -- dashboard.html` shows it
    as modified against HEAD. You WRITE NOTHING to this file — it was
    pre-placed and your job is verification.

T7. **USE PASS — this is not optional and it is not a diff review.** Read the
    resulting `register.md` as a document, whole, top to bottom. You are looking
    for one specific failure: **text made false by the placement of new text
    next to it, without a byte of it changing.** This file has met that defect
    twice and the second instance was introduced by the pass that fixed the
    first. Report anything that now reads wrongly in its position, even where
    every anchor matched and every hash agreed. A hash proves fidelity, not
    sanity. Finding nothing is a valid report; not looking is not.

T8. Produce a PROPOSED commit — message text and `git diff --cached --stat` —
    and **STOP**. Do not commit. The message:

```
RBT-93: register v0.10.0 - the host it did not describe, the meter it did not contain

/cost moved to haffeyenterprises.com on GoDaddy Basic hosting on 2026-08-02.
Section 7 went on describing the Cloud Run service for three days, and GoDaddy
hosting had no row in this file at all - $390.00/yr bundled with email and
M365, now 32.50/mo declared in sections 2.2, 3 and 5. Verified total 733.94 to
766.44. The section 2.2 exclusion is amended to say what it always meant,
registration and not hosting, rather than being overwritten.

Fifth falsification of a completeness claim in this file, and the first where
the missing meter was the one rendering the claim.

The header As-of cell is corrected. It carried v0.8.0's date under v0.9.0, one
version after v0.8.0 fixed the same defect in the same table.

dashboard.html becomes the TEMPLATE OF RECORD - the bytes that are live. It
replaces a file that looked like the source of truth while the served page was
a reskinned derivative of it: 21,400 bytes against 20,439, a different token
set, a back-link, a noindex. A renderer templating from the old copy would have
reverted the reskin on its first run and passed every check, being faithful to
the wrong original. Stage 4a's byte-identity proof was sound and was proving
the wrong file. A decoy is worse than a stale copy: staleness announces itself.
Two defects fixed in the adopted bytes - a header comment recommending an
access control that was applied on 2026-08-02, and an undefined --space-9 that
silently voided the page's bottom padding.

Section 8 item 9 SUPERSEDED, not completed as written. Its premise was already
false when written. New items 14 to 18: projections, the unrecorded auth-posture
change, the /status/sofia.html migration, the half-orphaned Cloud Run service,
and the renderer build that replaces item 9.

New section 9 notes. A derived percentage can survive an error in both its
inputs - the page's 98% verified-share was right while both dollar figures
behind it were wrong by ninety-five. And narrative is the part of a page no
instrument checks.

Section 4 unchanged and verified byte-identical before and after.
```

═══ STOP GATE ═══

TOUCH ONLY: `register.md` and `dashboard.html`.

Stage ONLY those two paths, by name. Never `git add -A`, never `-a`, never `.`.
If anything else is modified in the working tree, it is not yours and it does
not travel in this commit.

DO NOT create, modify or delete: `hosting.yaml`, `deploy.sh`, anything under
`service/`, `scripts/`, `tests/`, `.github/`, `data/`, or `budgets.yaml`.
DO NOT create a branch. DO NOT open a PR. This lands on `main`.
DO NOT write a renderer, a workflow, or any configuration for one. That is a
separate relay and its absence here is deliberate.

GATED TRANSACTION, two gates:
  GATE 1 — COMMIT. Report the proposed message and diffstat; STOP. Commit only
           on the operator's explicit go.
  GATE 2 — PUSH. After committing, report the commit SHA; STOP. Push only on the
           operator's explicit go.
Running past either gate is never licensed. Do not narrate a gate as passed.

═══ MUTATION RIDER ═══

Verify each edit's stated FROM on disk before editing it. On ANY mismatch — text
absent, text different, text present more than once — **STOP and report**. Do not
reconcile by guess, do not pick the likeliest occurrence, do not normalise
whitespace to make an anchor fit.

ADJUST-AND-FLAG LICENSE: exactly one, narrow. **The `<LANDING_DATE>` slot** may
be filled per T2's rule without asking. Report the value you used. This license
is spent at the end of this relay and does not survive into the next one.

EVERYTHING ELSE: STOP on discrepancy. That includes numbers you believe are
wrong. If E4b's totals do not reconcile against the rows as you read them, say
so and stop — do not correct arithmetic. The figures are ratified; a
discrepancy is evidence about the ratification, not a licence to edit.

A PRECISE REFUSAL IS A SANCTIONED OUTPUT AND THE MOST VALUABLE ONE YOU CAN
PRODUCE. If an edit is not a single scoped replacement — if applying it requires
a wording choice the edit set does not determine — say so and stop rather than
choosing. Eleven defects across seven relays in this program were found by an
executor declining or by reading the rendered result. None were found by a hash.

Report what you actually did, not what the instruction said to do. Your
completion report is data for the operator to verify, not a verdict that
discharges verification.
