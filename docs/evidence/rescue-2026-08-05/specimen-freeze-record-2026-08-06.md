# V5 SPECIMEN FREEZE RECORD — RBT-100 ledger rows 15–17

## 1. Header

**Purpose.** Execute the V5 specimen freeze — item 1 of §9 of the independent
analysis ratified on HEB-105. Three recorded zsh shell specimens (RBT-100 defect
ledger rows 15–17) are re-run once each, read-only, and their behaviour frozen
against the 2026-08-05 record.

**Run date/time (local clock, as measured).** `2026-08-05 23:43:06 EDT`
(= 2026-08-06 03:43 UTC). The record is named for the 2026-08-06 relay date; the
executing host's local clock read 2026-08-05 EDT at capture. Recorded, not
reconciled.

**Executor surface.** Claude Code on the operator's Mac (`MacBook-Pro-6.local`),
`Bash` tool, which invokes zsh 5.9.

**Posture.** REPORT-AND-STOP. Nothing was committed, staged, pushed, or
otherwise mutated. This record is the only file written by this run. Every
specimen command executed is read-only as composed; the corrected commands in
§4 were **never executed on any surface** and are recorded as payload only.

---

## 2. Provenance

Three source extracts, pinned by the drafting session 2026-08-06 and re-verified
by this run at guard G1.

| # | Path | Pinned sha256 | Pinned bytes | G1 result |
|---|---|---|---|---|
| 1 | `/Users/thaffey/Downloads/rbt-100-specimen-extract-code-ledger-aligned.md` | `578d39b0ece012e03ca5af975072ecc3b1573c852743be594cd60d58639e1aca` | 13377 | **MATCH** (hash and bytes) |
| 2 | `/Users/thaffey/Downloads/rbt-100-specimen-extract-code.md` | `b72bb11667b58a55efa1d07ed8aed882715d1763e469d986a4789a45143857de` | 10349 | **MATCH** (hash and bytes) |
| 3 | `/Users/thaffey/Downloads/rbt-100-specimen-extract.md` | `0d5b2cf5c51343137993e25ae416e1f9fe6bc7904939a4dcb3e0a70b8cc210c9` | 7101 | **MATCH** (hash and bytes) |

**Canonical specimen source:** row 1 (operator-ratified D1, 2026-08-06). Every
command in §4 was copied byte-exactly from that file on disk — from the first
fenced block following each of `### ROW 15`, `### ROW 16`, `### ROW 17` — never
from the relay text and never from memory.

**Environment provenance caveat, carried forward.** The canonical source's own
environment section is explicitly labelled **CAPTURED AT EXTRACT TIME**, not
contemporaneous with the original 2026-08-05 specimen runs. Its own words: same
session, same tool surface, same machine, no known intervening reconfiguration —
but a later reading. Any comparison in §3 is therefore fresh-measurement vs.
extract-time-reading, not fresh vs. at-specimen-time.

**Guard results.**

- **G1 — Pin check:** PASS. All three hashes and byte counts matched.
- **G2 — Shell gate:** PASS. `zsh=5.9 bash=unset` in the same Bash tool used for
  every specimen.
- **G3 — Repo identity:** PASS. `origin` =
  `https://github.com/Haffey-Enterprises/SOFIA.git`; no
  `.git/index.lock` present.
- **G4 — Collision check:** PASS. This record's path did not exist before the
  write.
- **G5 — Canonical source read whole:** PASS. All command lines re-confirmed
  read-only by inspection before execution (`cd`, `echo`, `printf`, `git
  rev-parse/cat-file/log/show/status/ls-remote`, `gh pr view`, `gh api` GETs,
  `sed`, `grep`, `tr`, `base64 -d`, `shasum`, `set --`, a no-op `for … do :;
  done`). Block 0 row 7 confirmed as stated.

**Sentinel constant.** `sha256("")` =
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` — the
64-hex constant all three specimens are anchored on. Independently re-derivable
anywhere; it appears in every re-run output below.

---

## 3. Environment

**Fresh capture (T1), verbatim as emitted in the specimen shell:**

```
zsh=5.9
Darwin MacBook-Pro-6.local 25.5.0 Darwin Kernel Version 25.5.0: Tue Jun  9 22:28:34 PDT 2026; root:xnu-12377.121.10~1/RELEASE_ARM64_T6050 arm64
git version 2.50.1 (Apple Git-155)
gh version 2.96.0 (2026-07-02)
6.02
pipefail=off
shwordsplit=off
errexit=off
nomatch=on
2026-08-05 23:43:06 EDT
```

**Extract-time readings from the canonical source, verbatim:**

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

**Side-by-side and divergences named.**

| Axis | Extract-time reading | Fresh measurement | Divergence |
|---|---|---|---|
| `ZSH_VERSION` | 5.9 | 5.9 | none |
| `BASH_VERSION` | `<unset>` | `unset` | none |
| `uname -a` | Darwin 25.5.0 arm64, kernel string as shown | byte-identical | none |
| `git` | 2.50.1 (Apple Git-155) | 2.50.1 (Apple Git-155) | none |
| `gh` | 2.96.0 (2026-07-02) | 2.96.0 (2026-07-02) | none |
| `shasum` | 6.02 | 6.02 | none |
| `pipefail` | NOT SET | off | none |
| `shwordsplit` | NOT SET | off | none |
| `errexit` | NOT SET | off | none |
| `nomatch` | **"not reported set"** | **`on`** | **DIVERGENCE — see below** |
| `interactive_comments` | "not reported set" | not measured by this run | not comparable |
| `base64` | BSD base64 (macOS) | not measured by this run | not comparable |

**The one divergence, recorded and not fixed.** The extract-time section records
`nomatch` as *"not reported set"*; this run measures `nomatch=on`. The two
statements are not necessarily in conflict — "not reported set" describes the
absence of a reading, not a reading of absence — but they are not the same
statement, and the fresh measurement is the one that is directly attested. The
value matters to ROW 17: `nomatch=on` is precisely the option under which an
unmatched glob is a hard error rather than a literal, which is the mechanism of
ROW 17's `no matches found:` diagnostic. The divergence is recorded as measured.
No option was set, unset, or otherwise altered by this run.

---

## 4. The specimens

### 4.1 ROW 15 — commit gate — zsh `:a` history modifier

**Command verbatim as run** (copied from the canonical source, `### ROW 15`
first fenced block):

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

**Complete observed output of this re-run, verbatim:**

```
commit: a252ae98edf79bda4ddc321af1c5cab6b5ab91bc

=== message as stored in the commit object ===
Merge pull request #71 from Haffey-Enterprises/feature/rbt-100-civerification-commission-the-instruments-that-prove-the

RBT-100: commission the shallow-clone canary and the fixture-conformance guards=== trailer check (must be empty) ===
  none

=== re-hash FROM THE COMMIT OBJECT (durable form) ===
deea2d215ad99c125839b6672d4a8983530180846b1be629fdbd93dd02562e97  -
fatal: Not a valid object name /Users/thaffey/Documents/GitHub/SOFIA/a252ae98edf79bda4ddc321af1c5cab6b5ab91bcgent-loop/tests/test_replay_hermeticity.py
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -

=== files in the commit ===
 .github/workflows/agent-loop-tests.yml      |  68 ++++++-
 agent-loop/tests/test_replay_hermeticity.py | 274 ++++++++++++++++++++++++++++
 2 files changed, 333 insertions(+), 9 deletions(-)
=== parent ===
9229dfc35006d509632bfffd4acf1f389f73ddcc
=== tree state after commit ===
## develop...origin/develop
```

**Recorded 2026-08-05 wrong output, quoted for comparison:**

```
=== re-hash FROM THE COMMIT OBJECT (durable form) ===
deea2d215ad99c125839b6672d4a8983530180846b1be629fdbd93dd02562e97  -
fatal: Not a valid object name /Users/thaffey/Documents/GitHub/SOFIA/10b8413320bf8e284e8774727161d217d2f93356gent-loop/tests/test_replay_hermeticity.py
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

**VERDICT: PASS (reproduced).** Basis: the second `cat-file` was again refused
with `fatal: Not a valid object name` on the `:a`-consumed
`<cwd>/<sha>gent-loop/…` shape — the leading `a` of `agent-loop` absorbed by the
`:a` modifier, the path made absolute against the cwd — and the empty-input
digest appeared for that line while the first hash (`deea2d21…`) remained
correct, preserving the one-good-one-bad shape the record calls out as the harder
one to notice.

**Value differences (not decay, per D3).** `SHA` resolved to
`a252ae98edf79bda4ddc321af1c5cab6b5ab91bc` (current `develop` HEAD, the merge
commit) rather than the 2026-08-05 `10b8413320bf8e284e8774727161d217d2f93356`;
the mangled object name therefore carries the new SHA. The `=== message ===`,
`=== files ===`, `=== parent ===` and `=== tree state ===` sections show
merge-commit content absent from the original capture. The idiom is unchanged.

**Corrected command — APPENDIX A, ROW 15. NEVER RUN.** *(Authored on the
deliberation surface 2026-08-06; never executed on any surface. Braces terminate
the parameter expansion, so `:a` is literal, not a modifier.)*

```
git --no-optional-locks cat-file -p "${SHA}:.github/workflows/agent-loop-tests.yml" | shasum -a 256
git --no-optional-locks cat-file -p "${SHA}:agent-loop/tests/test_replay_hermeticity.py" | shasum -a 256
```

---

### 4.2 ROW 16 — push gate — unquoted expansion not word-split

**Command verbatim as run** (copied from the canonical source, `### ROW 16`
first fenced block):

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

**Complete observed output of this re-run, verbatim:**

```
=== remote branch tip (ls-remote) ===
local HEAD: a252ae98edf79bda4ddc321af1c5cab6b5ab91bc

=== blob content fetched FROM THE REMOTE, hashed locally ===

  gh: Not Found (HTTP 404)
base64: stdin: (null): error decoding base64 input stream
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -

  gh: Not Found (HTTP 404)
base64: stdin: (null): error decoding base64 input stream
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

**Recorded 2026-08-05 wrong output, quoted for comparison:**

```
=== blob content fetched FROM THE REMOTE, hashed locally ===

  gh: Not Found (HTTP 404)
base64: stdin: (null): error decoding base64 input stream
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -

  gh: Not Found (HTTP 404)
base64: stdin: (null): error decoding base64 input stream
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

**VERDICT: PASS (reproduced).** Basis: the `printf` label line is again blank in
both iterations — `$2` empty because zsh did not word-split the unquoted `$pair`,
leaving `set --` with a single positional — and the empty-input digest appeared
for both. The re-run's blob-section output is byte-identical to the 2026-08-05
capture.

**Value differences (not decay, per D3).** `git ls-remote origin
"refs/heads/$BR"` returned no rows: the feature branch has been deleted from the
remote since the original capture. That line is not the idiom-carrying line, and
the idiom-carrying lines executed and failed exactly as recorded. `local HEAD:`
now reports the merge commit.

**Corrected command — APPENDIX A, ROW 16. NEVER RUN.** *(Authored on the
deliberation surface 2026-08-06; never executed on any surface; a drafted
correction with no run history anywhere. zsh does not word-split unquoted
expansions; `${=pair}` requests the split explicitly.)*

```
set -- ${=pair}
```

---

### 4.3 ROW 17 — merge gate — unquoted `?` parsed as a glob

**Command verbatim as run** (copied from the canonical source, `### ROW 17`
first fenced block; the vestigial `for b in … do :; done` line reproduced as
composed):

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

**Complete observed output of this re-run, verbatim:**

```
=== PR final state ===
{"base":"develop","mergeCommit":"a252ae98edf79bda4ddc321af1c5cab6b5ab91bc","mergedAt":"2026-08-05T04:34:58Z","mergedBy":"T-Bone-Haff","number":71,"state":"MERGED"}

=== the merge commit on the remote ===
{"message":"Merge pull request #71 from Haffey-Enterprises/feature/rbt-100-civerification-commission-the-instruments-that-prove-the\n\nRBT-100: commission the shallow-clone canary and the fixture-conformance guards","parents":["9229dfc35006d509632bfffd4acf1f389f73ddcc","10b8413320bf8e284e8774727161d217d2f93356"],"sha":"a252ae98edf79bda4ddc321af1c5cab6b5ab91bc"}

=== blobs re-hashed from the MERGED tip on develop ===
(eval):12: no matches found: repos/Haffey-Enterprises/SOFIA/contents/.github/workflows/agent-loop-tests.yml?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
(eval):13: no matches found: repos/Haffey-Enterprises/SOFIA/contents/agent-loop/tests/test_replay_hermeticity.py?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

**Recorded 2026-08-05 wrong output, quoted for comparison:**

```
=== blobs re-hashed from the MERGED tip on develop ===
(eval):12: no matches found: repos/Haffey-Enterprises/SOFIA/contents/.github/workflows/agent-loop-tests.yml?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
(eval):13: no matches found: repos/Haffey-Enterprises/SOFIA/contents/agent-loop/tests/test_replay_hermeticity.py?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  -
```

**VERDICT: PASS (reproduced).** Basis: both unquoted-`?` URL lines again raised
the zsh `no matches found:` diagnostic — `gh` never executed — and the
empty-input digest appeared for both. The blob section is byte-identical to the
2026-08-05 capture, including the differing `(eval):12` / `(eval):13` line
prefixes; the `nomatch=on` measured in §3 is the option that makes this a hard
error rather than a literal.

**Value differences (not decay, per D3).** None in the idiom-carrying lines. The
two preceding informational sections returned live values (PR 71 still `MERGED`,
merge commit and parents as expected); those were not captured in the original
excerpt and are not compared.

**Corrected command — APPENDIX A, ROW 17. NEVER RUN.** *(Authored on the
deliberation surface 2026-08-06; never executed on any surface; a drafted
correction with no run history anywhere. Quote the URL so `?` is never a glob.)*

```
gh api "repos/Haffey-Enterprises/SOFIA/contents/.github/workflows/agent-loop-tests.yml?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc" --jq '.content' | tr -d '\n' | base64 -d | shasum -a 256
gh api "repos/Haffey-Enterprises/SOFIA/contents/agent-loop/tests/test_replay_hermeticity.py?ref=a252ae98edf79bda4ddc321af1c5cab6b5ab91bc" --jq '.content' | tr -d '\n' | base64 -d | shasum -a 256
```

---

## 5. Self-declaration (V2)

**Claim.** This record asserts that the three recorded zsh specimen failures of
RBT-100 defect-ledger rows 15–17 **do reproduce** — as idiom failures — in the
environment measured in §3. Each of the three produced its characteristic zsh
diagnostic and the `sha256("")` sentinel on re-run. This record makes no claim
about any environment other than the one measured, about any shell other than
zsh 5.9 as configured above, or about whether the corrected commands in §4 work
— none was executed.

**Population.** 3 of 3 specimens (rows 15, 16, 17), re-run **once each**. No
specimen was run more than once; no repetition, no averaging, no retry. n=1 per
specimen, n=3 total — the same population size the ledger's row 14 already flags
as too small to support a general claim about the sentinel control.

**Third outcome.** **None.** No specimen returned COULD-NOT-MEASURE. Both
network-dependent prerequisites held: `gh` was authenticated and the GitHub API
was reachable (attested by the live ROW 17 `gh pr view` / `gh api` responses and
by ROW 16's `gh` reaching the API and receiving a genuine `404` rather than a
transport failure). Every idiom-carrying line executed.

**Recorded but not a verdict input.** One environment divergence
(`nomatch`, §3) and a set of output-value differences (§4.1, §4.2) are recorded.
Per the ratified D3, value differences do not bear on the verdict; the verdict
judges the idiom.

---

## 6. Run-surface note

Executed on the operator's Mac because neither the cloud container nor the
device-bridge VM can host zsh reproduction (wrong shells). This constraint is
**carried from the session kickoff and was NOT verified by this run** — no
attempt was made on either alternative surface. The shell actually used here was
verified directly at guard G2 (`zsh=5.9 bash=unset`) in the same Bash tool that
ran all three specimens.
