#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
smoke_root="$(mktemp -d /tmp/bedrock-clean-install.XXXXXX)"
cleanup() {
  case "$smoke_root" in
    /tmp/bedrock-clean-install.*) rm -rf -- "$smoke_root" ;;
    *) printf 'Refusing to remove unexpected smoke path: %s\n' "$smoke_root" >&2 ;;
  esac
}
trap cleanup EXIT

export CLAUDE_CONFIG_DIR="$smoke_root/config"
mkdir -p "$CLAUDE_CONFIG_DIR"

claude plugin marketplace add "$repo_root" --scope user
claude plugin install bedrock@bedrock --scope user
claude plugin list --json > "$smoke_root/installed.json"
claude plugin details bedrock@bedrock > "$smoke_root/details-first.txt"

# A second process using the same isolated configuration is the reload boundary.
claude plugin details bedrock@bedrock > "$smoke_root/details-reloaded.txt"

python3 - "$smoke_root" <<'PY'
from __future__ import annotations

import json
from pathlib import Path
import sys

root = Path(sys.argv[1])
installed = json.loads((root / "installed.json").read_text(encoding="utf-8"))
serialized = json.dumps(installed)
if "bedrock@bedrock" not in serialized:
    raise SystemExit("clean-install smoke failed: bedrock@bedrock is absent from plugin list")

for filename in ("details-first.txt", "details-reloaded.txt"):
    text = (root / filename).read_text(encoding="utf-8")
    if "Skills (13)" not in text:
        raise SystemExit(f"clean-install smoke failed: {filename} does not report 13 skills")

first = (root / "details-first.txt").read_text(encoding="utf-8")
reloaded = (root / "details-reloaded.txt").read_text(encoding="utf-8")
if first != reloaded:
    raise SystemExit("clean-install smoke failed: component inventory changed after reload")

print("PASS: isolated install and reload discovered bedrock@bedrock with 13 skills")
PY
