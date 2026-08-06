# RBT-100 — specimen extract for ledger rows 15–17

Written 2026-08-05 by the RBT-100 claude.ai design surface, on request.

---

## READ THIS FIRST — the payload you asked for does not exist in my possession

**None of the three commands is available verbatim from this session's
transcript, because none of them was ever in it.**

All three were composed by Claude Code in its own session. What reached this
surface were **relayed summaries written by Code, containing Code's own
elisions** (`…`), transmitted through the operator. This surface never saw the
command lines. There is no copy to make.

**Therefore every specimen below is labelled `FRAGMENT (relayed)` — neither
COPIED nor RECONSTRUCTED.** A reconstruction was deliberately not attempted:
inventing plausible command text and presenting it as a defect specimen would
manufacture evidence, which is the precise failure class these specimens
document. Fragments are given exactly as relayed, ellipses included.

**This is a closed corroboration window.** The commands existed in a session
transcript that is not this surface's and is not mine to fetch. Under the rule
derived from the vault-drain leg — *a claim is window-bound if the subject of
its verification is not among the transaction's committed outputs* — these
commands were window-bound from the moment they were run, and nothing committed
them.

---

## Shared environment — what is known, and what is not

| item | value | how known |
|---|---|---|
| Executor shell | **zsh** | Code's own self-report in all three relays ("zsh parsed", "zsh does not word-split", "is a zsh glob"). Never independently confirmed. |
| Executor OS | **macOS** | Inferred from the executor running on the operator's Mac and from sibling legs establishing a macOS/BSD executor. NOT stated in any of the three relays. |
| zsh version | **UNKNOWN** | Never reported. |
| `set -o pipefail` state | **UNKNOWN** | Never reported, and directly load-bearing — with `pipefail` on, at least specimens 1 and 3 may have failed loudly instead of yielding a digest. |
| `set -u` / `set -e` state | **UNKNOWN** | Never reported. |
| macOS version, coreutils present | **UNKNOWN** | Never reported. |
| Working directory | `~/Documents/GitHub/SOFIA` (assumed) | Not stated in any relay. |
| This surface's own shell | bash, on a Linux aarch64 bridge VM | Structurally immune to all three defects — which is why it was the reader that caught none of them and the sentinel that caught all three ran in Code's environment. |

**The sentinel digest, in full:**
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

**Provenance of that value:** the relays abbreviate it as `e3b0c442…7852b855`.
The full 64 characters above were obtained by this surface **independently
computing `printf '' | sha256sum`**, not by copying it from any relay. It is the
sha256 of zero-length input. It is stated here as a computed constant, not as a
transcribed observation.

---

## Specimen 1 — zsh `:a` history modifier

**Ledger row 15, verbatim:**
> Executor's hash pipeline: zsh `:a` history modifier mangled the object name →
> empty input | executor | the sentinel fired | at a gate | **No** — not in any
> authored artifact | **Yes** — SHA-256

**Provenance: FRAGMENT (relayed).** Not copied — not present in this transcript.

**What exists, exactly as relayed by Code through the operator:**

```
"$SHA:agent-loop/…"
```

The `…` is **Code's own elision**, not mine. The full path was not transmitted.
The surrounding command — the `git cat-file` invocation, the pipe, the hashing
step — was never stated at all.

Code also named the corrected form it re-ran with. Recorded because Code named
it, not offered as a fix:

```
${SHA}:${p}
```

**Observed wrong output, as relayed:** `e3b0c442…7852b855` (abbreviated by Code).

**Mechanism, as stated by Code:** *"zsh parsed `:a` in `"$SHA:agent-loop/…"` as
its absolute-path modifier, git received a mangled object name, and the pipeline
hashed empty input."*

**Gate:** G3, commit verification. Reproduction from this record alone is not
possible.

---

## Specimen 2 — unquoted expansion not word-split in zsh

**Ledger row 16, verbatim:**
> Executor's hash pipeline: unquoted expansion not word-split in zsh →
> malformed API URL → empty input | executor | the sentinel fired | at a gate |
> **No** — same | **Yes** — SHA-256

**Provenance: FRAGMENT (relayed).** Not copied — not present in this transcript.

**What exists, exactly as relayed:**

```
set -- $pair
```

The loop containing it, the construction of `$pair`, the API URL, and the
hashing step were not transmitted. Code described the variable's content as a
`"sha path"` string — that quoted phrase is Code's description of the value, not
a copy of any literal.

**Observed wrong output, as relayed:** `e3b0c442…7852b855` (abbreviated by Code).

**Mechanism, as stated by Code:** *"zsh does not word-split unquoted parameter
expansions, so `set -- $pair` passed the whole "sha path" string as $1 and the
API URL was malformed, gh returned 404, and the empty pipeline hashed."*

**Gate:** G4, push/transport verification. Reproduction from this record alone is
not possible.

---

## Specimen 3 — unquoted `?` parsed as a zsh glob

**Ledger row 17, verbatim:**
> Executor's hash pipeline: unquoted `?` parsed as a zsh glob → `gh` never ran →
> empty input | executor | the sentinel fired | at a gate | **No** — same |
> **Yes** — SHA-256

**Provenance: FRAGMENT (relayed) — and this one carries NO command text at all.**

**What exists:** a prose description only. No fragment of the command was
transmitted in any form.

Code's statement, as relayed: *"the unquoted `?` in the contents API URL is a
zsh glob, no matches found, gh never ran, empty pipeline hashed."*

The URL was not given. Whether the `?` introduced a query string, and what
followed it, is unrecorded. **A reader wanting to reproduce this has a mechanism
and no artifact.**

**Observed wrong output, as relayed:** `e3b0c442…7852b855`, and Code reported it
**twice** on this occasion.

**Gate:** G7, post-merge content verification on the protected branch.

---

## What would be needed to complete this extract

1. Claude Code's session transcript for the RBT-100 leg, gates G3, G4 and G7 —
   the only place the command lines exist.
2. `zsh --version` and the option state (`set -o`) as they stood in that session.
3. Whether `pipefail` was set, which determines whether these were silent
   failures or merely unhandled ones.

Items 2 and 3 are recoverable if the executor's environment is unchanged. Item 1
is not recoverable from anything this surface can reach.

---

## Standing caveat

This file is a record of **what was relayed about three defects**, not a record
of the defects. It is usable as a description of three failure mechanisms and is
**not usable as a reproduction case**. Anyone treating the fragments above as
runnable specimens is doing what the sentinel exists to prevent: taking a
plausible-looking artifact for a measured one.
