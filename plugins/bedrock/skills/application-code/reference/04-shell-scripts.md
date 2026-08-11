# Haffey profile: Bash utility and operational scripts

Select this profile for Bash scripts shipped with an application. It binds Bash 3.2+ where macOS workstation portability is required; a script using newer features declares a different minimum version and verifies it before execution.

## Entry and failure model

- Use `#!/usr/bin/env bash` and declare the minimum Bash version.
- Default to `set -euo pipefail` for one fail-fast operation. Verification aggregators may omit `-e` deliberately and collect failures.
- Define exit meanings: `0` success, `1` work/check failure, `2` invocation or environment precondition failure.
- Avoid interactive prompts in automation; fail with the missing input or authority.

## Inputs, paths, and output

- Parse and validate arguments; reject unknown flags and missing values.
- Quote expansions and use `--` before untrusted path operands where supported.
- Resolve the repository relative to the script location or an explicit validated argument. Never embed private user paths.
- Use `mktemp -d` or a validated platform-equivalent, restrictive permissions where sensitive, and `trap` cleanup. Do not hardcode a predictable shared temporary path.
- Preserve filenames without retyping them; handle spaces and newlines deliberately. Use NUL-delimited traversal when arbitrary filenames are in scope.
- Progress goes to stdout; diagnostics to stderr. Never print secrets or secret-bearing commands.

## Expansion and pipelines

Use single-quoted heredoc delimiters for literal bodies. Do not place complex heredocs inside command substitution; write to a temporary file and pass its path. Under `pipefail`, account for early-closing consumers such as `head`; buffer or use a producer mode that does not turn expected truncation into an unexplained failure.

Avoid `eval`. Do not construct executable shell from untrusted strings. Prefer arrays for commands where the declared Bash version supports them.

## Mutation safety

Before destructive, production, or Git mutation, resolve exact targets read-only, confirm authorization, record rollback/recovery, and stop on scope drift. Git scripts verify repository identity, branch, sync/upstream state, worktree scope, and both `user.name` and `user.email`. Stage explicit paths only—never broad `git add -A`, `-a`, or `.`.

Shell scripts may implement an authorized application operation; they do not acquire deployment, infrastructure, or release authority merely by being executable.
