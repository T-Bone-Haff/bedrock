# RBT-100 — shell specimen extract (code)

Extracted 2026-08-05 from the RBT-100 execution session (Claude Code, executor
surface). Three specimens: the zsh/bash semantic divergences at the commit,
push and merge gates, each of which silently fed empty input to `sha256` and
returned the digest of the empty string in the shape of a verified content hash.

**The defects are the payload.** Commands below are reproduced as composed. They
are not corrected, normalized, or annotated beyond the four fields requested.

---

## PROVENANCE OF THE LEDGER ROWS — READ FIRST

**I do not have ledger rows 15–17 and have not reproduced them.**

No ledger with numbered rows was produced on this surface during this session.
That artifact exists on the deliberation surface, not here. Reconstructing its
row text from the specimen content would be fabrication wearing the shape of a
citation — the exact failure class this ticket exists to instrument — so the
rows are omitted rather than approximated.

What follows in their place is the nearest artifact I actually hold: clauses
(3), (4) and (5) of **Addition 3 to T5**, as supplied by the operator at G8 and
as they stand in the ratified D4 draft. These are the three shell specimens as
the record states them, and they are what rows 15–17 are presumed to correspond
to — but that correspondence is an assumption I cannot verify from here.

### Addition 3, clauses (3)–(5) — COPIED verbatim from the G8 relay message

> (3), (4) and (5) At the commit, push and merge gates, three UNRELATED zsh/bash
> semantic divergences — the `:a` history modifier, the absence of word
> splitting on unquoted expansions, and an unquoted `?` parsed as a glob — each
> silently fed empty input to sha256 and returned
> `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`, the digest
> of the empty string, in the shape of a verified content hash.

> **`e3b0c442…7852b855` is the sha256 of empty input and is never a content
> value. A pin-verification pipeline should treat it as a sentinel and halt.**
> That check fired THREE times in this leg, against three independent causes,
> unprompted — while D1 fired once by design, D2 once by design, and D3's
> negative control once by probe. **The best-commissioned instrument in this leg
> is the one nobody set out to build**, and it enters the record with more
> observed fires than the three this ticket was written to commission.

---

## ENVIRONMENT — COMMON TO ALL THREE SPECIMENS

**Provenance of this section: CAPTURED AT EXTRACT TIME**, not recorded at the
time of the specimens. Same session, same tool surface, same machine, and no
intervening shell reconfiguration is known to have occurred — but it is a
later reading, not a contemporaneous one.

```
shell binary      /bin/zsh
ZSH_VERSION       5.9
BASH_VERSION      <unset>            (no bash in the execution path)
uname -a          Darwin MacBook-Pro-6.local 25.5.0 Darwin Kernel Version 25.5.0:
                  Tue Jun  9 22:28:34 PDT 2026; root:xnu-12377.121.10~1/RELEASE_ARM64_T6050 arm64
git               2.50.1 (Apple Git-155)
gh                2.96.0 (2026-07-02)
shasum            6.02
base64            BSD base64 (macOS; usage: base64 [-Ddh] [-b num] [-i in_file] [-o out_file])
```

Option state, from `setopt` at extract time:

```
pipefail             NOT SET
nomatch              not reported set
shwordsplit          NOT SET
interactive_comments not reported set
errexit              NOT SET
```

**Bearing on reproduction, stated as fact rather than as a fix:**

- `pipefail` is **off**. A non-zero exit on the left of a pipe does not fail the
  pipeline, so `<failing producer> | shasum -a 256` exits 0 and prints a hash.
- `shwordsplit` is **off** — zsh's default. Unquoted parameter expansions do
  **not** word-split. This is the direct cause of specimen 2 and is the single
  largest behavioural divergence from bash in this set.
- The commands were executed by the Claude Code `Bash` tool, which invokes zsh.
  Specimen 3's diagnostics carry an `(eval):NN` prefix, indicating the script
  body was evaluated rather than run from a file; the other two do not show a
  prefix in their captured output.
- The operator's own interactive terminal (a separate surface, seen elsewhere in
  the same session) had `interactive_comments` **off** by default. That surface
  is not where these three specimens ran.

---

## SPECIMEN 1 — commit gate — the `:a` history modifier

**Provenance: COPIED from this session's transcript.** Reproduced from the tool
invocation as composed, including surrounding lines, since the `SHA=` assignment
is load-bearing for reproduction.

### 1. Command, verbatim

```
cd /Users/thaffey/Documents/GitHub/SOFIA
SHA=$(git rev-parse HEAD)
echo "commit: $SHA"
echo
echo "=== message as stored in the commit object ==="
git --no-optional-locks cat-file -p "$SHA" | sed -n '/^$/,$p' | sed '1d'
echo "=== trailer check (must be empty) ==="
git --no-optional-locks log -1 --format='%b' | grep -iE "co-authored-by|generated with|claude" || echo "  none"
echo
echo "=== re-hash FROM THE COMMIT OBJECT (durable form) ==="
git --no-optional-locks cat-file -p "$SHA:.github/workflows/agent-loop-tests.yml" | shasum -a 256
git --no-optional-locks cat-file -p "$SHA:agent-loop/tests/test_replay_hermeticity.py" | shasum -a 256
echo
echo "=== files in the commit ==="
git --no-optional-locks show --stat --format='' "$SHA"
echo "=== parent ==="
git --no-optional-locks rev-parse "$SHA^"
echo "=== tree state after commit ==="
git --no-optional-locks status --short --branch
```

### 2. Environment

Common section above. `SHA` held
`10b8413320bf8e284e8774727161d217d2f93356` at execution.

### 3. Observed wrong output, verbatim

```
=== re-hash FROM THE COMMIT OBJECT (durable form) ===
deea2d215ad99c125839b6672d4a8983530180846b1be629fdbd93dd02562e97  -
fatal: Not a valid object name /Users/thaffey/Documents/GitHub/SOFIA/10b8413320bf8e284e8774727161d217d2f93356gent-loop/tests/test_replay_hermeticity.py
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

Note the first of the two hashes is **correct**. Only the second line's object
name was mangled; the pair therefore presented as one good hash and one bad one
rather than as a uniformly broken command.

---

## SPECIMEN 2 — push gate — no word splitting on unquoted expansion

**Provenance: COPIED from this session's transcript.**

### 1. Command, verbatim

```
cd /Users/thaffey/Documents/GitHub/SOFIA
BR=feature/rbt-100-civerification-commission-the-instruments-that-prove-the
echo "=== remote branch tip (ls-remote) ==="
git ls-remote origin "refs/heads/$BR"
echo "local HEAD: $(git rev-parse HEAD)"
echo
echo "=== blob content fetched FROM THE REMOTE, hashed locally ==="
for pair in "34c71fc0437d0368bf3c62636a7b4f69d42e3ab7 .github/workflows/agent-loop-tests.yml" \
            "eb07ea9b5eebac57894564c3543bbc3e04e5f073 agent-loop/tests/test_replay_hermeticity.py"; do
  set -- $pair
  printf '%s\n  ' "$2"
  gh api "repos/Haffey-Enterprises/SOFIA/git/blobs/$1" --jq '.content' | tr -d '\n' | base64 -d | shasum -a 256
done
```

### 2. Environment

Common section above. The operative option is `shwordsplit` **off**: `set -- $pair`
assigned the entire `"<sha> <path>"` string to `$1`, leaving `$2` empty.

### 3. Observed wrong output, verbatim

```
=== blob content fetched FROM THE REMOTE, hashed locally ===

  gh: Not Found (HTTP 404)
base64: stdin: (null): error decoding base64 input stream
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -

  gh: Not Found (HTTP 404)
base64: stdin: (null): error decoding base64 input stream
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

Note the blank line after each `printf` label: `$2` was empty, so the path label
printed as nothing. Both iterations failed identically.

---

## SPECIMEN 3 — merge gate — unquoted `?` parsed as a glob

**Provenance: COPIED from this session's transcript.** The vestigial `for b in
… do :; done` line is present as composed and is reproduced rather than removed.

### 1. Command, verbatim

```
cd /Users/thaffey/Documents/GitHub/SOFIA
echo "=== PR final state ==="
gh pr view 71 --json number,state,mergedAt,mergedBy,mergeCommit,baseRefName \
  --jq '{number,state,mergedAt,mergedBy:.mergedBy.login,mergeCommit:.mergeCommit.oid,base:.baseRefName}'
echo
echo "=== the merge commit on the remote ==="
gh api repos/Haffey-Enterprises/SOFIA/commits/a252ae98edf79bda4ddc321af1c5cab6b5ab91bc \
  --jq '{sha:.sha, message:.commit.message, parents:[.parents[].sha]}'
echo
echo "=== blobs re-hashed from the MERGED tip on develop ==="
for b in "34c71fc0437d0368bf3c62636a7b4f69d42e3ab7 .github/workflows/agent-loop-tests.yml"; do :; done
gh api repos/Haffey-Enterprises/SOFIA/contents/.github/workflows/agent-loop-tests.yml?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc --jq '.content' | tr -d '\n' | base64 -d | shasum -a 256
gh api repos/Haffey-Enterprises/SOFIA/contents/agent-loop/tests/test_replay_hermeticity.py?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc --jq '.content' | tr -d '\n' | base64 -d | shasum -a 256
```

### 2. Environment

Common section above. The `?` in the query string is unquoted and zsh attempts
filename generation on it; with no match, the command is not run at all. The
`(eval):NN` line prefixes in the output indicate evaluation of the script body.

### 3. Observed wrong output, verbatim

```
=== blobs re-hashed from the MERGED tip on develop ===
(eval):12: no matches found: repos/Haffey-Enterprises/SOFIA/contents/.github/workflows/agent-loop-tests.yml?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
(eval):13: no matches found: repos/Haffey-Enterprises/SOFIA/contents/agent-loop/tests/test_replay_hermeticity.py?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

The two diagnostics carry different line prefixes — `(eval):12` and `(eval):13`.

---

## CROSS-SPECIMEN CONSTANT

All three produced:

```
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

which is `sha256("")` — the digest of empty input, and never a content value.
Independently confirmed on the deliberation surface at G4 by
`printf '' | sha256sum`.
