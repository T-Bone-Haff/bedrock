═══════════════════════════════════════════════════════════════════════════
  HEB-86 LANDING — GATE C-AMEND. Supplement to the landing relay, inserted
  between GATE C and GATE C-V. Transport: PRE-PLACED (one path).
  Posture: GATED. Amend only — no push, no PR, no merge.
═══════════════════════════════════════════════════════════════════════════

**Why this exists.** Your two gate-C observations were correct and are now
ratified as defects rather than elaborations. `[unsourced]`, `[unrouted]` and
the gates-the-landing declaration were real rules living only in the template
— the artifact the skill itself calls "a carrier, not an authority." They are
promoted into `SKILL.md`. Nothing else changes: the commit message stands, the
other eight paths stand.

Your read that they were not contradictions was right. The ruling is that a
non-contradicting divergence is still a defect when the rule exists in only
one of the two surfaces.

═══ FRESH-FETCH GUARD ═══════════════════════════════════════════════════

You are Claude Code in the **bedrock** repository, mid-transaction. The
doctrines you re-read at the landing relay's guard stand; do not re-read them
unless you have lost that context, in which case:

  /Users/thaffey/Documents/GitHub/bedrock/CLAUDE.md
  /Users/thaffey/Documents/GitHub/vault/CLAUDE.md

IDENTITY GATE — verify and report each:

  1. branch = `feature/heb-86-author-construct-spec`
  2. HEAD = 7c074c747bd80e8a36db12ad24f06f966b2d34d9
  3. HEAD~1 = 7fb654ae4a9e525a9b6726d2e060915528cdb752
  4. **The branch is NOT pushed.** `git ls-remote --heads origin
     feature/heb-86-author-construct-spec` returns zero refs. **This is the
     precondition that makes `--amend` safe; if the branch is on the remote,
     STOP — an amend would rewrite published history.**
  5. `git --no-optional-locks status --porcelain` shows **exactly one** entry:
     ` M plugins/bedrock/skills/author-construct-spec/SKILL.md`

On ANY mismatch: STOP and report.

═══ PRE-GATE — verify the one target, then STOP ═════════════════════════

**Transport is PRE-PLACED.** The ratified bytes are on disk. You verify; you
do not write.

  plugins/bedrock/skills/author-construct-spec/SKILL.md
    BASE (the version now in HEAD, being superseded)
        f48eae9e0f9a8f6c822f27e0a7fb8a830c6ca346c9ddd1e15b48f111747ea5a6
    REPLACEMENT (working tree)
        f81028c0cc1402d22c35a622611a0533c7091822b76ba5e653ba2071dfb0ca77
        39,698 bytes

**Assert the other eight paths are byte-unchanged against HEAD.** Nothing but
this one file moves. A second modified path means the tree drifted — STOP.

**Content assertions — check these three, they are the whole point:**

  a. The step-2 no-artifact branch reads *"stays in the spec, marked
     `[unsourced]`"* — previously *"flagged"* with no marker named.
  b. The no-tracker fallback in "Where things go" reads *"stays in the spec
     **marked `[unrouted]`**"* — previously *"is flagged"*.
  c. A new bullet follows the instrument rule in "The target": *"**And every
     obligation states whether it gates the landing.**"*

Diffstat should be small — three edits, one file, no deletions beyond the
replaced clauses. **Read the diff.** Anything else in it is a tripwire.

Then STOP.

── GATE C-AMEND — AMEND THE COMMIT ───────────────────────────────────────

    git add plugins/bedrock/skills/author-construct-spec/SKILL.md
    git commit --amend --no-edit

**Stage that one path, named explicitly. Never `-A`, `-a`, or `.`**

**`--no-edit` is required: the commit message does not change.** It described
the skill generically and remains accurate. Do not add a line about this
amendment — the fact that a gate caught a defect is deliberation trail and
belongs in HEB-86, not in the commit body.

Confirm before amending: exactly one path staged, and the other eight already
in HEAD.

Then STOP.

── GATE C-AMEND-V — VERIFY ───────────────────────────────────────────────

The commit SHA **will change**; `7c074c74…` is superseded and should not be
cited anywhere afterward. Report:

  · the new commit SHA
  · sole parent still `7fb654ae…` (`git rev-list --parents -n1 <new>` = two fields)
  · `git diff --name-only <new>~1 <new>` = **exactly the same nine paths**
  · all nine re-hashed **out of the new commit**, against these pins —
    eight unchanged, one superseded:

      f81028c0cc1402d22c35a622611a0533c7091822b76ba5e653ba2071dfb0ca77  author-construct-spec/SKILL.md   ← NEW
      cb4d15af3c37c09df25a620003e0553fbe9d6786c05c1f4e1864379f53566e88  author-construct-spec/templates/construct-spec-template.md
      402157b269273c0e349f48b7d5f16a576ed82380a295ab21afe579480f0341b7  author-decision-record/SKILL.md
      802f0f637c1abad3de45dde4477c2f30e458bab7bfaf197b451165ce26687f8d  author-decision-record/templates/adr-template.md
      2002fcf1d9a0747fb1cb6092227965cc194f0686276fe7cccf933918560a9c76  author-decision-record/templates/ddr-template.md
      cb346baecb595d660b323114f6e449d1cbfe1084eeca199b8f3d4fc55eedb071  author-decision-record/templates/sdd-template.md
      8ba40ca9bf3f4c55419ab72cc3cbffde6487582901b29efb66f08c5561797c18  author-standard/SKILL.md
      e1344476c664c1d732a8de539092ba79befa18d1b6cfc73c7c672b6bd88105bc  plugins/bedrock/.claude-plugin/plugin.json
      64dae20e2c063d75e1bf804be426b1e71ae76fd5058a5ac858fe89ae6b2d3dce  .claude-plugin/marketplace.json

  · `git log -1 --format=%B` verbatim — **byte-identical to the message you
    committed at GATE C**
  · version at the new commit still 2.1.0, parent still 2.0.0
  · the two descriptions still byte-identical
  · porcelain empty

Then STOP.

═══ RESUMING THE LANDING RELAY ══════════════════════════════════════════

On the operator's go after C-AMEND-V, **return to the landing relay at
GATE D (push)** and continue through GATE E (open the PR) as written there.
Everything in that relay's STOP GATE and MUTATION RIDER remains in force
unchanged — merge is still not authorized.

**One correction carries forward:** the landing relay's completion block
names the commit SHA to report. Report the **amended** SHA. `7c074c74…` no
longer exists on any branch and must not appear in the PR.

═══ STOP GATE ═══════════════════════════════════════════════════════════

Touch only, and stage only:

    plugins/bedrock/skills/author-construct-spec/SKILL.md

**NOT authorized in this supplement:**

  ✗ push, PR, merge, tag, force-push, branch deletion
  ✗ any edit to any file — the bytes are ratified
  ✗ any change to the commit message (`--no-edit`, always)
  ✗ any of the other eight paths
  ✗ amending if the branch has been pushed — STOP instead

**Each of the pre-gate, C-AMEND and C-AMEND-V is its own gate requiring
Tad's explicit go.** Running past a gate is never licensed.

═══ MUTATION RIDER ══════════════════════════════════════════════════════

**This supplement mutates no file.** It rewrites one unpublished commit, and
that is gated.

ADJUST-AND-FLAG LICENCE: **none.** Declared spent at completion.

TRIPWIRES:
  · Branch present on the remote → STOP; do not amend published history.
  · BASE pin ≠ `f48eae9e…` in HEAD → the commit is not the one this
    supplement was written against → STOP.
  · REPLACEMENT pin ≠ `f81028c0…` on disk → the tree is not the ratified
    bytes → STOP, reporting both computed and expected.
  · A second modified path in porcelain → STOP.
  · The amended message differing from the GATE C message by even one byte →
    STOP.
  · Any instruction here contradicting the tree → the tree wins, you STOP.

═══ ON COMPLETION ═══════════════════════════════════════════════════════

Report the amended SHA prominently and state plainly that `7c074c74…` is
superseded. A third surface will re-hash all nine landed artifacts against
the pins above before the push gate fires.
