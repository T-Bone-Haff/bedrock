# RBT-100 — specimen extract for ledger rows 15–17, ledger-aligned

Second output file. Supersedes the "PROVENANCE OF THE LEDGER ROWS" section of
`rbt-100-specimen-extract-code.md`
(sha256 `b72bb11667b58a55efa1d07ed8aed882715d1763e469d986a4789a45143857de`),
which stated the ledger rows were unavailable to this surface. They are now
available and are reproduced below. **The command payloads in that file are
unchanged and remain valid**; this file adds the row text, the ledger's own
reclassification, and the per-column detail the ledger's schema asks for.

Source of the rows: `rbt-100-defect-ledger-and-control-inventory.md`, read whole
from `/Users/thaffey/Downloads/` on 2026-08-05.

**Self-report disclosure, in the ledger's own terms.** The ledger warns that
every row is self-reported by the party with an interest in how the count reads.
Rows 15–17 are *mine* — I composed all three defective commands. This extract is
therefore self-reported twice over: by the surface that ran the leg, and within
that, by the actor that caused these particular three. Nothing here was
recovered from an independent record.

---

## 1. The ledger rows, verbatim

**COPIED** from `rbt-100-defect-ledger-and-control-inventory.md`, lines 45–47.

| # | Defect | Caught by | By what act | When | Artifact alone? | Token-anchored? |
|---|---|---|---|---|---|---|
| 15 | Executor's hash pipeline: zsh `:a` history modifier mangled the object name → empty input | executor | the sentinel fired | at a gate | **No** — not in any authored artifact | **Yes** — SHA-256 |
| 16 | Executor's hash pipeline: unquoted expansion not word-split in zsh → malformed API URL → empty input | executor | the sentinel fired | at a gate | **No** — same | **Yes** — SHA-256 |
| 17 | Executor's hash pipeline: unquoted `?` parsed as a zsh glob → `gh` never ran → empty input | executor | the sentinel fired | at a gate | **No** — same | **Yes** — SHA-256 |

### Related rows that govern how 15–17 should be read

**COPIED** from the same file, lines 43–44 and 87.

> | 13 | The empty-digest sentinel was scored as a transport guard; its three fires were defects in executor-authored instruments | **another design surface** (naming class E) | re-derived a stated claim | after close | **No** | No token shape |

> | 14 | "The best-commissioned instrument in this leg" overstated: n=3 was zsh-specific, and the same control fired **zero** on another leg | **another design surface** | re-derived a stated claim | after close | **No** — needs a second leg's data | No token shape |

> | **Empty-digest sentinel** | executor, ad hoc | **3** | Rows 15–17. Not designed, not in any artifact, three independent causes |

**And the consequence the ledger draws**, lines 131–135:

> **(a) The landing comment on RBT-100 presents the five-hop pin chain as a
> headline proof, and rows 15–17 are why that reads wrong now.** The chain held at
> every hop — and three of the measurements that established it were, on first
> attempt, hashes of nothing. The chain's integrity is real; the account of how
> confidently it was established is not, and the landing comment does not say so.

### What this reclassification does to my v1 framing

My first extract presented these three as the sentinel control working — three
unprompted catches. Row 13 corrects that, and the correction is not cosmetic:

- **The sentinel is not a control that caught three defects in the system under
  test.** It caught three defects *in my own measuring instruments*, composed
  ad hoc at gate time. The thing being measured was never at risk from them.
- **The pin chain's five zero-drift hops are therefore a weaker claim than
  stated** — not because any hash was wrong, but because three of the fifteen
  measurements had to be taken twice, and the record presents them as if taken
  once.
- **"The best-commissioned instrument in this leg is the one nobody set out to
  build"** — my sentence, carried into D4 via Addition 3 — is overstated on
  n = 3 in one shell on one platform. Row 14 records that the same control
  fired **zero** on another leg.

This file records those corrections; it does not attempt to re-litigate them.

---

## 2. Why "Artifact alone? No" is the load-bearing column here

Stated because the ledger's schema asks it and the answer has a consequence the
inventory implies but does not spell out.

All three defects existed **only in ephemeral shell composition**. They were
never in the relay, never in a commit, never in a reviewable artifact of any
kind. Every designed control in this leg — the content pins, the identity gate,
the mutation rider, the lock check, the whole five-hop chain, the nine-gate
ladder — operates on *artifacts*. None of them could have fired on these,
because there was no artifact to inspect.

The only thing that could catch them was recognising a constant in runtime
output. That is why the catcher is "the sentinel fired" and not any named
instrument, and it is why the control inventory has to list the sentinel as
"executor, ad hoc — not designed, not in any artifact."

**Token-anchored: Yes — SHA-256.** All three are anchored on the same 64-hex
constant, which is what made recognition possible at all:

```
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

`sha256("")`. Independently confirmed at G4 on the deliberation surface by
`printf '' | sha256sum`.

---

## 3. The specimens

**The defects are the payload.** Commands are reproduced as composed. They are
not corrected, normalized, or annotated beyond the fields below.

Environment is common to all three and is **CAPTURED AT EXTRACT TIME**, not
recorded at the time of the specimens — same session, same tool surface, same
machine, no known intervening reconfiguration, but a later reading:

```
shell binary      /bin/zsh
ZSH_VERSION       5.9
BASH_VERSION      <unset>            (no bash in the execution path)
uname -a          Darwin MacBook-Pro-6.local 25.5.0 Darwin Kernel Version 25.5.0:
                  Tue Jun  9 22:28:34 PDT 2026; root:xnu-12377.121.10~1/RELEASE_ARM64_T6050 arm64
git               2.50.1 (Apple Git-155)
gh                2.96.0 (2026-07-02)
shasum            6.02
base64            BSD base64 (macOS)

pipefail             NOT SET     <- a failing producer does not fail the pipeline
shwordsplit          NOT SET     <- zsh default; direct cause of row 16
nomatch              not reported set
interactive_comments not reported set
errexit              NOT SET
```

Executed by the Claude Code `Bash` tool, which invokes zsh. Row 17's diagnostics
carry an `(eval):NN` prefix, indicating the script body was evaluated rather than
run from a file; rows 15 and 16 show no such prefix in their captured output.

---

### ROW 15 — commit gate — zsh `:a` history modifier

**Provenance: COPIED from this session's transcript.** Surrounding lines
retained because the `SHA=` assignment is load-bearing for reproduction.

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

`SHA` held `10b8413320bf8e284e8774727161d217d2f93356` at execution.

**Observed wrong output, verbatim:**

```
=== re-hash FROM THE COMMIT OBJECT (durable form) ===
deea2d215ad99c125839b6672d4a8983530180846b1be629fdbd93dd02562e97  -
fatal: Not a valid object name /Users/thaffey/Documents/GitHub/SOFIA/10b8413320bf8e284e8774727161d217d2f93356gent-loop/tests/test_replay_hermeticity.py
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

The first hash is **correct**. Only the second object name was mangled, so the
pair presented as one good result beside one bad one rather than as a uniformly
broken command — the harder shape to notice.

---

### ROW 16 — push gate — unquoted expansion not word-split

**Provenance: COPIED from this session's transcript.**

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

**Observed wrong output, verbatim:**

```
=== blob content fetched FROM THE REMOTE, hashed locally ===

  gh: Not Found (HTTP 404)
base64: stdin: (null): error decoding base64 input stream
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -

  gh: Not Found (HTTP 404)
base64: stdin: (null): error decoding base64 input stream
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

The blank line after each label is `$2` expanding to nothing. Both iterations
failed identically — this one had no correct half to sit beside.

---

### ROW 17 — merge gate — unquoted `?` parsed as a glob

**Provenance: COPIED from this session's transcript.** The vestigial
`for b in … do :; done` line is present as composed and is reproduced, not removed.

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

**Observed wrong output, verbatim:**

```
=== blobs re-hashed from the MERGED tip on develop ===
(eval):12: no matches found: repos/Haffey-Enterprises/SOFIA/contents/.github/workflows/agent-loop-tests.yml?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
(eval):13: no matches found: repos/Haffey-Enterprises/SOFIA/contents/agent-loop/tests/test_replay_hermeticity.py?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

The two diagnostics carry different line prefixes — `(eval):12` and `(eval):13`.

---

## 4. What the three have in common, and what they do not

**Common:** all three are zsh-vs-bash semantic divergences; all three are in
*measuring* instruments rather than in the system measured; all three produce a
plausible-looking 64-hex string rather than an error at the shasum step, because
`pipefail` is off; all three were composed at a gate under time pressure and
none was reviewed before execution.

**Not common — the three causes are independent**, which is why the ledger's
counting convention keeps them as three rows rather than one:

| row | zsh feature | bash behaviour | failure point |
|---|---|---|---|
| 15 | `:a` as a history/parameter modifier on `$VAR:a…` | no modifier; literal `:a` | `git` rejects a mangled object name |
| 16 | no word splitting on unquoted `$var` | splits on IFS | `gh` gets a malformed URL, 404 |
| 17 | `?` triggers filename generation | `?` glob only if a match exists; otherwise literal | `gh` never executes at all |

Row 17's failure point differs in kind from the other two: the command **did not
run**. Rows 15 and 16 ran and were refused by their tool.

---

## 5. Standing recommendation, unchanged from the record

**`e3b0c442…7852b855` is the sha256 of empty input and is never a content value.
A pin-verification pipeline should treat it as a sentinel and halt.**

That remains right. What row 13 corrects is not the guard but its scoring: it is
a guard against *the verifier's own instruments*, not against the transport it
was credited with checking. On this leg the transport was never in doubt.
