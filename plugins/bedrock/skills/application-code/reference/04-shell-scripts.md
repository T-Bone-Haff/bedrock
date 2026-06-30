# Reference: Shell Scripts

Discipline for the operational and utility shell scripts that travel with a service — startup, verification, repo-state checks, commit helpers. Application code is Python (the other references); this is for the bash around it. Load when writing or reviewing a shell script.

## Contents

- [1. Shebang, shell, strict mode](#1-shebang-shell-strict-mode)
- [2. Header](#2-header)
- [3. Heredoc and pipe discipline](#3-heredoc-and-pipe-discipline)
- [4. Exit codes and output](#4-exit-codes-and-output)
- [5. Error handling — fail-fast vs accumulator](#5-error-handling--fail-fast-vs-accumulator)
- [6. Filesystem discipline](#6-filesystem-discipline)
- [7. Non-interactive](#7-non-interactive)
- [8. Git pre-flight (scripts that commit)](#8-git-pre-flight-scripts-that-commit)

---

## 1. Shebang, shell, strict mode

Start every script with `#!/usr/bin/env bash` — not `/bin/bash`. `env` resolves to the user's bash; a hardcoded path can pick the wrong one (macOS ships bash 3.2 as `/bin/bash`, with a Homebrew bash 4+ elsewhere on PATH).

Author to **bash 3.2 compatibility** so scripts run on operator workstations, not just CI. That rules out associative arrays (`declare -A`), `mapfile`/`readarray` (use `while IFS= read -r line; do … done < file`), and `${var,,}`/`${var^^}` case conversion (use `tr`/`awk`).

Set strict mode at the top:

```bash
set -euo pipefail   # -e exit on error · -u error on unset var · -o pipefail propagate pipe failures
```

A **bracketed** disable is fine when a section needs different semantics (see the accumulator pattern, §5) — re-enable explicitly. A **silent** disable (`set +e` never re-enabled) is not; if you omit a flag, say why in the header.

## 2. Header

Every script carries an authorship header:

```bash
#!/usr/bin/env bash
# File: path/to/script.sh
# Author: <author> — <role>, <org>
# Created: YYYY-MM-DD
# Description: <one line>
# Compatibility: bash 3.2+
# Strict mode: set -euo pipefail   (or note the exception, e.g. "no -e: accumulator, see §5")
# Revised: YYYY-MM-DD (<ticket or short description>)
```

Shell scripts are authoring artifacts, so the `# Revised:` line carries the ticket/description parenthetical (unlike application-code modules, which use a bare date).

## 3. Heredoc and pipe discipline

The highest-value gotcha. Heredocs interact badly with `set -euo pipefail` inside command substitution — special characters in the body get expansion-attempted, and under `-e` a failed expansion aborts the script silently mid-substitution, leaving partial state that surfaces as an unrelated downstream failure.

```bash
# Prohibited — heredoc inside command substitution
git commit --message "$(cat <<'EOF'
multi-line message
EOF
)"

# Required — heredoc to a tempfile, consumed by path
COMMIT_MSG_FILE="$(mktemp -t commit-msg.XXXXXX.txt)"
trap 'rm -f "$COMMIT_MSG_FILE"' EXIT
cat > "$COMMIT_MSG_FILE" <<'EOF'
multi-line message
EOF
git commit --message-file "$COMMIT_MSG_FILE"
```

Use the single-quoted delimiter `<<'EOF'` to keep the body literal (no variable/command expansion); the `trap … EXIT` cleans up even on abnormal exit. A heredoc into a plain variable assignment is fine (it completes before assignment — no command-substitution partial-state risk).

**Pipe truncation** is the sibling trap: `git show HEAD | head -20` — `head` closes stdin early, the producer gets SIGPIPE (exit 141), and under `pipefail`+`-e` the script aborts. Buffer the producer to a tempfile first, then read from it.

## 4. Exit codes and output

- **0** success · **1** work failure (a check failed, work didn't complete) · **2** environment/precondition error (bad flags, missing tool, wrong directory). The 1-vs-2 split matters to callers parsing the code.
- Informational/progress output to **stdout**; failures to **stderr**. A `--quiet` flag suppresses informational output but keeps warnings and errors. If you use a severity prefix for operator-facing output, keep it consistent within the script.

## 5. Error handling — fail-fast vs accumulator

A script doing one discrete operation uses **fail-fast** (`set -e`): first error aborts. A script running many checks and reporting *all* failures uses the **accumulator** — drop `-e` for the loop, collect failures, exit once:

```bash
set -uo pipefail   # -e intentionally omitted: accumulator
FAILURES=()
for check in "${CHECKS[@]}"; do
    "$check" || FAILURES+=("$check")
done
if [ "${#FAILURES[@]}" -gt 0 ]; then
    printf 'FAIL: %d check(s) failed:\n' "${#FAILURES[@]}" >&2
    printf '  - %s\n' "${FAILURES[@]}" >&2
    exit 1
fi
```

The accumulator is for verification scripts; using it elsewhere wants a note in the header.

## 6. Filesystem discipline

- **No hardcoded user paths** (`/Users/x/…`) and **no hardcoded `/tmp/`** (ephemeral, may be cleared mid-session). Derive the repo root from the script's own location: `REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"`.
- **Quote every path variable**: `cp "$SRC" "$DEST/"`, never bare `$SRC`. Unquoted paths break on spaces.
- **Preserve filenames in staging copies** with a trailing-slash destination (`cp "src/foo.md" "stage/"`), so the basename is inherited rather than retyped — dotted/versioned filenames are where retyping introduces defects.

## 7. Non-interactive

No `read -p` or other interactive-input patterns — inputs come from arguments, environment, or files. If interaction is genuinely needed, the script exits and surfaces to the operator rather than blocking on a prompt. This matters doubly for AI-executed scripts: an agent can't answer a prompt, so a blocking `read` hangs the session.

## 8. Git pre-flight (scripts that commit)

A script that produces commits verifies **both halves** of the git identity, and the branch, before committing — checking email but not name (or vice versa) is a known failure class:

```bash
test "$(git config user.email)" = "$EXPECTED_EMAIL" || { echo "RED: identity email mismatch" >&2; exit 1; }
test "$(git config user.name)"  = "$EXPECTED_NAME"  || { echo "RED: identity name mismatch"  >&2; exit 1; }
test "$(git branch --show-current)" = "$EXPECTED_BRANCH" || { echo "RED: wrong branch" >&2; exit 1; }
```

For high-stakes commits, run a repo-state pre-flight first (branch + identity, sync state, working-tree cleanliness, stale markers) before any mutation.
