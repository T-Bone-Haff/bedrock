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
import hashlib
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
installed = json.loads((root / "installed.json").read_text(encoding="utf-8"))
serialized = json.dumps(installed)
if "bedrock@bedrock" not in serialized:
    raise SystemExit("clean-install smoke failed: bedrock@bedrock is absent from plugin list")

matches = [row for row in installed if row.get("id") == "bedrock@bedrock"]
if len(matches) != 1:
    raise SystemExit("clean-install smoke failed: expected one bedrock installation record")
record = matches[0]
install_path = Path(record.get("installPath", "")).resolve()
if not install_path.is_relative_to((root / "config").resolve()):
    raise SystemExit("clean-install smoke failed: install path escaped isolated configuration")
required = (
    ".claude-plugin/plugin.json",
    "LICENSE",
    "CHANGELOG.md",
    "governance/README.md",
    "governance/registry.yaml",
    "governance/release-evidence.schema.json",
    "governance/rollout-ledger.schema.json",
)
missing = [relative for relative in required if not (install_path / relative).is_file()]
if missing:
    raise SystemExit(f"clean-install smoke failed: installed governance files are missing: {missing}")
manifest = json.loads((install_path / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
if manifest.get("version") != record.get("version"):
    raise SystemExit("clean-install smoke failed: installed record and manifest versions differ")

registry_text = (install_path / "governance/registry.yaml").read_text(encoding="utf-8")
adapter_match = re.search(r"^  claude_adapter: ([0-9]+\.[0-9]+\.[0-9]+)$", registry_text, re.MULTILINE)
if adapter_match is None:
    raise SystemExit("clean-install smoke failed: Claude adapter contract is unavailable")
expected_identity = {
    "schema_version": 1,
    "classification": "generated-carrier",
    "package": manifest["name"],
    "manifest_version": manifest["version"],
    "version_authority": ".claude-plugin/plugin.json#/version",
    "manifest_sha256": hashlib.sha256((install_path / ".claude-plugin/plugin.json").read_bytes()).hexdigest(),
    "generator": {
        "id": "scripts/sync_package_identity.py",
        "version": "1.0.0",
    },
    "contracts": {
        "claude_adapter": adapter_match.group(1),
    },
}
expected_identity_bytes = (json.dumps(expected_identity, indent=2) + "\n").encode("utf-8")
carrier_paths = sorted((install_path / "skills").glob("*/PACKAGE_IDENTITY.json"))
if len(carrier_paths) != 13:
    raise SystemExit(f"clean-install smoke failed: expected 13 package identity carriers, found {len(carrier_paths)}")
if any(path.read_bytes() != expected_identity_bytes for path in carrier_paths):
    raise SystemExit("clean-install smoke failed: installed package identity carrier drift")

for filename in ("details-first.txt", "details-reloaded.txt"):
    text = (root / filename).read_text(encoding="utf-8")
    if "Skills (13)" not in text:
        raise SystemExit(f"clean-install smoke failed: {filename} does not report 13 skills")

first = (root / "details-first.txt").read_text(encoding="utf-8")
reloaded = (root / "details-reloaded.txt").read_text(encoding="utf-8")
if first != reloaded:
    raise SystemExit("clean-install smoke failed: component inventory changed after reload")

print("PASS: isolated install and reload discovered bedrock@bedrock with 13 skills, identity carriers, and packaged governance")
PY
