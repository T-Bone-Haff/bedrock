═══════════════════════════════════════════════════════════════════════════
  HEB-86 LANDING — author-construct-spec + author-decision-record fourth
  doctype + author-standard boundary + 2.1.0.
  Transport: PRE-PLACED (all nine paths). Posture: GATED TRANSACTION.
  Commit → push → PR. MERGE IS NOT AUTHORIZED. Authored on claude.ai.
═══════════════════════════════════════════════════════════════════════════

═══ FRESH-FETCH GUARD ═══════════════════════════════════════════════════

You are Claude Code in the **bedrock** repository. This is an EXECUTION
request relayed by Tad. Re-read from disk, by explicit path — do not trust
this prompt's summary or prior-session memory:

  /Users/thaffey/Documents/GitHub/bedrock/CLAUDE.md
  /Users/thaffey/Documents/GitHub/vault/CLAUDE.md

**Deliberately NOT in this list:** the `author-execution-relay` skill. It is
authoring-side only — its own Scope section states that executor behavior is
governed by the relay artifact it produces, "not by the executor loading this
skill." Your authority is this document plus the two doctrines above. The
omission is deliberate; do not go looking for it.

IDENTITY GATE — verify and report each:

  1. remote origin = https://github.com/T-Bone-Haff/bedrock.git
  2. branch = `main`
  3. HEAD = 7fb654ae4a9e525a9b6726d2e060915528cdb752
  4. `git --no-optional-locks status --porcelain` shows **exactly eight**
     entries — seven ` M` and one `??` for the untracked directory
     `plugins/bedrock/skills/author-construct-spec/` — and nothing else

Use `git --no-optional-locks` for every status check. Plain `git status`
refreshes the index and, from a sandboxed bridge, leaves a lock nobody can
unlink. On ANY mismatch: STOP and report.

═══ PRE-GATE — verify all nine targets, then STOP ═══════════════════════

**Transport is PRE-PLACED for all nine.** The ratified bytes are already on
disk. You verify; you do not write. No file content changes in this
transaction.

SEVEN MODIFIED — base pin from `git show HEAD:<path> | shasum -a 256`,
replacement pin from the working tree:

  plugins/bedrock/skills/author-decision-record/SKILL.md
    BASE        67e83fb7f0917a5237df3c7983d5d1ad75a97075de74984ac210f07fd8680f3c
    REPLACEMENT 402157b269273c0e349f48b7d5f16a576ed82380a295ab21afe579480f0341b7

  plugins/bedrock/skills/author-decision-record/templates/adr-template.md
    BASE        1540825bc9fe86c9c07b647e37b44446d8f5997966110d046c6182ae3d5cb607
    REPLACEMENT 802f0f637c1abad3de45dde4477c2f30e458bab7bfaf197b451165ce26687f8d

  plugins/bedrock/skills/author-decision-record/templates/ddr-template.md
    BASE        59068b3a2741f497e92bff240da238d4f8b6b57471c8ff7a76ab8c09ba9668f9
    REPLACEMENT 2002fcf1d9a0747fb1cb6092227965cc194f0686276fe7cccf933918560a9c76

  plugins/bedrock/skills/author-decision-record/templates/sdd-template.md
    BASE        ba21f228601afa6872ab42ed00935a1cd4db20099f41a7fd9163a7a75b84894b
    REPLACEMENT cb346baecb595d660b323114f6e449d1cbfe1084eeca199b8f3d4fc55eedb071

  plugins/bedrock/skills/author-standard/SKILL.md
    BASE        ff042cccb28c2f340892becab73b1ca0021487031c0d34cbb4861f2d77dad367
    REPLACEMENT 8ba40ca9bf3f4c55419ab72cc3cbffde6487582901b29efb66f08c5561797c18

  plugins/bedrock/.claude-plugin/plugin.json
    BASE        456831c75a6210d80b1d61d74cee28639336cd0d6c72e7d1f05b590f1dceb470
    REPLACEMENT e1344476c664c1d732a8de539092ba79befa18d1b6cfc73c7c672b6bd88105bc

  .claude-plugin/marketplace.json
    BASE        8c658c03509996805dc0f8d453dc6c8d5df16f0178923f4152cb4ff77f79bcd1
    REPLACEMENT 64dae20e2c063d75e1bf804be426b1e71ae76fd5058a5ac858fe89ae6b2d3dce

TWO NEW — no base pin; assert `git cat-file -e HEAD:<path>` FAILS for each:

  plugins/bedrock/skills/author-construct-spec/SKILL.md
    REPLACEMENT f48eae9e0f9a8f6c822f27e0a7fb8a830c6ca346c9ddd1e15b48f111747ea5a6
  plugins/bedrock/skills/author-construct-spec/templates/construct-spec-template.md
    REPLACEMENT cb4d15af3c37c09df25a620003e0553fbe9d6786c05c1f4e1864379f53566e88

**A REPLACEMENT mismatch means the tree is not what was ratified — STOP.**
**A BASE mismatch means the branch point moved — STOP.**

**VERSION — derive it, do not take it from me.** Read the version from
`git show HEAD:plugins/bedrock/.claude-plugin/plugin.json`. It must be
**2.0.0**; the base pin above already implies it, and this is the independent
check. The ruling is a **MINOR** bump — one new skill plus amendments to two,
matching the per-skill MINOR precedent of the 1.10.0 / 1.11.0 / 1.12.0
landings; 2.0.0 was an explicitly ruled milestone rollup, not a pattern. So
the working tree must read **2.1.0**. If your derivation disagrees with
2.1.0, STOP and report both.

**Also assert:** `plugin.json`'s `description` and `marketplace.json`'s
`plugins[0].description` are **byte-identical to each other**, per
`CLAUDE.md`'s rule that the marketplace description is derived verbatim from
plugin.json's. Both changed in this transaction; both must still match.

Then STOP.

── GATE B — CREATE THE BRANCH ────────────────────────────────────────────

    git checkout -b feature/heb-86-author-construct-spec

`main` is protected: never commit to it. The working tree's changes carry
onto the new branch. Confirm the branch name, confirm HEAD is still
`7fb654ae`, confirm porcelain still shows the same eight entries. Then STOP.

── GATE C — COMMIT, ALL NINE PATHS, ONE COMMIT ───────────────────────────

    git add plugins/bedrock/skills/author-construct-spec/SKILL.md \
            plugins/bedrock/skills/author-construct-spec/templates/construct-spec-template.md \
            plugins/bedrock/skills/author-decision-record/SKILL.md \
            plugins/bedrock/skills/author-decision-record/templates/adr-template.md \
            plugins/bedrock/skills/author-decision-record/templates/ddr-template.md \
            plugins/bedrock/skills/author-decision-record/templates/sdd-template.md \
            plugins/bedrock/skills/author-standard/SKILL.md \
            plugins/bedrock/.claude-plugin/plugin.json \
            .claude-plugin/marketplace.json

**Nine paths, named explicitly. Never `-A`, `-a`, or `.`** Confirm nine
staged and nothing else before committing.

**One commit, not several.** The new skill and `author-decision-record`'s
fourth routing entry are mutually dependent: landing either alone ships a
dangling cross-reference. `CLAUDE.md` additionally requires the version bump
to ride in the same transaction as the skill-content change.

Reading the full diff before landing is sanctioned conduct, not
instruction-creep. Anything it surfaces arrives as gate input, never as a
licence to edit.

Commit message, verbatim:

```
HEB-86: author-construct-spec skill + author-decision-record fourth doctype + 2.1.0

WHAT CHANGED

- NEW skill `author-construct-spec` with its template. Governs the construct
  spec: a design document for a change to one construct, whose consumer is an
  implementer building it from the document alone. Carries the two-jobs
  routing (floor / operative rule / cadence), the shape (frame, piece spine,
  obligation sets), what the implementation target must declare, and the
  acceptance-time graduation of operative rules into standing contract
  documents.

- `author-decision-record` gains the fourth doctype. Its None-of-these branch
  now routes construct specs instead of sending them to a code comment; the
  Routing section gains the entry and its two-branch deliberation substrate;
  the doubt gate makes an unclean routing call the operator's; body integrity,
  the amendment lifecycle and the cold read are declared doctype-independent.
  Three harvested disciplines land: one-line pre-acceptance Change Log rows,
  a correction amends the clause rather than appending after it, and the row
  for the version being authored is not history. Ticket-identifier homes go
  from three to four, admitting the metadata frame.

- The three ADR-family templates gain the FILL / STANDING comment classes.
  Each carried exactly one standing order — Change Log ordering and version
  increments — formatted identically to fill guidance and therefore lost on
  first tidy. STANDING comments are never deleted.

- `author-standard`'s sibling-boundary enumeration admits the fourth doctype.

- plugin.json and marketplace.json: description admits construct specs;
  MINOR bump to 2.1.0.

WHY, BY POINTER

Authored from HEB-86 and the two accepted SOFIA construct specs as worked
examples; RBT-72's spec is the counterexample, not a source. The deliberation
trail, the census measurements, the three-hat review and the cascade findings
are in HEB-86 and are deliberately not in these documents.

VERIFICATION

Nine paths, pre-placed and pin-verified at both ends before staging. Skill
and template cross-checked for divergence after every amendment; the skill
declares precedence over its template. Two known gaps are carried, named in
the PR description rather than in the artifacts.

Refs HEB-86.
```

Then STOP.

── GATE C-V — VERIFY THE COMMIT ──────────────────────────────────────────

Report: the commit SHA; sole parent `7fb654ae…`; `git diff --name-only
HEAD~1 HEAD` = exactly the nine paths; **all nine re-hashed out of the
commit** (`git show HEAD:<path> | shasum -a 256`) against the REPLACEMENT
pins above; `git log -1 --format=%B` verbatim; porcelain empty. Then STOP.

── GATE D — PUSH ─────────────────────────────────────────────────────────

    git push -u origin feature/heb-86-author-construct-spec

Report the remote ref and the SHA it points at. Then STOP.

── GATE E — OPEN THE PR ──────────────────────────────────────────────────

Open a PR into `main` titled:

    HEB-86: author-construct-spec skill + author-decision-record fourth doctype

Body: the WHAT CHANGED block from the commit message, followed verbatim by:

```
## Known gaps, carried deliberately

**The template mirrors the skill and has no currency mechanism.** The
template restates a substantial share of the skill's normative text as
STANDING comments that are never deleted. Reviewed and predicted before
landing; it produced one real divergence during authoring, which is why the
skill now declares precedence over its template. Thinning the STANDING blocks
is the fix and is deferred to usage evidence rather than guessed at now.

**The floor's second clause has no test.** "Or later change something they
should not" swings an independent routing measurement of a 41,006-character
document by roughly ±3,500 characters depending on how broadly it is read. It
is the judgment-heavy part of the discipline and no honest test was available
at authoring time.

## Empirical basis

Three instances of the doctype exist, all changes to one construct in one
repository. The delta branch of the substrate gate rests on those three; the
greenfield branch is reasoned from the sibling doctypes, not observed. A
generality probe against two hypothetical sibling constructs found the
load-bearing machinery transfers and the calibration does not — worked
examples, three record-location premises, and the "Required tests" field name
are all shaped by the source construct.

## Proving

Not yet fired. The first consumer is SOFIA's RBT-72 spec. The skill's own
falsifier — a construct spec that follows everything and still cannot be
built from — is stated in its opening.
```

Report the PR number and URL. **Then STOP.**

═══ STOP GATE ═══════════════════════════════════════════════════════════

Touch only, and stage only, the nine paths named at GATE C.

**NOT authorized at any point in this transaction:**

  ✗ **merge** — the merge is a separate ratification and is not in this relay
  ✗ tag, release, force-push, auto-merge, branch deletion
  ✗ any commit to `main`
  ✗ any edit to any file — this is verify-and-commit; the bytes are ratified
  ✗ any other skill under `plugins/bedrock/skills/` — nine paths, no more
  ✗ `docs/`, `project-template/`, `README.md`
  ✗ any Linear ticket

**Each of the pre-gate, B, C, C-V, D and E is its own gate requiring Tad's
explicit go.** Running past a gate is never licensed. He may elect, live at a
gate, to batch a named span of the remainder; that election is his at
transaction time and this relay does not pre-authorize it. Halt-on-anomaly is
retained in full — any anomaly voids the remainder of a batch and re-atomizes
the gates.

At GATE E, **report what CI checks the PR triggers and their status. Do not
fix a red check** — report it as gate input and STOP.

═══ MUTATION RIDER ══════════════════════════════════════════════════════

**This transaction mutates no file.** The mutations are to git history and to
the remote, and each is gated.

ADJUST-AND-FLAG LICENCE: **none.** Declared spent at completion.

TRIPWIRES:
  · Any BASE pin mismatch → the branch point moved → STOP.
  · Any REPLACEMENT pin mismatch → the tree is not the ratified bytes → STOP,
    reporting both computed and expected.
  · Version on disk ≠ 2.1.0, or version at HEAD ≠ 2.0.0 → STOP.
  · The two descriptions not byte-identical → STOP.
  · A tenth path in porcelain at any point → STOP; unrelated dirt does not
    ride in this commit.
  · `main` checked out at any commit step → STOP.
  · Any instruction here contradicting the tree → the tree wins, you STOP.

═══ ON COMPLETION ═══════════════════════════════════════════════════════

Report the commit SHA and the PR URL prominently. A third surface will
re-hash all nine landed artifacts against the pins above, so
`authored = ratified = staged = committed` is provable without trusting any
single reporter — your account of having verified is itself a claim.

The branch is pushed and the PR is open. **The merge is Tad's, in a later
transaction, and is not licensed here.**
