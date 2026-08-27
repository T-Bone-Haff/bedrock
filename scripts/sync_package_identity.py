#!/usr/bin/env python3
"""Generate or check Bedrock's consumer-visible package identity carriers."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

import yaml


CARRIER_FILENAME = "PACKAGE_IDENTITY.json"
CARRIER_SCHEMA_VERSION = 1
CARRIER_CLASSIFICATION = "generated-carrier"
GENERATOR_ID = "scripts/sync_package_identity.py"
GENERATOR_VERSION = "1.0.0"
VERSION_AUTHORITY = ".claude-plugin/plugin.json#/version"


def carrier_paths(root: Path) -> list[Path]:
    skills_root = root / "plugins/bedrock/skills"
    return [path.with_name(CARRIER_FILENAME) for path in sorted(skills_root.glob("*/SKILL.md"))]


def expected_carrier_payload(root: Path) -> dict[str, Any]:
    manifest_path = root / "plugins/bedrock/.claude-plugin/plugin.json"
    registry_path = root / "plugins/bedrock/governance/registry.yaml"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    return {
        "schema_version": CARRIER_SCHEMA_VERSION,
        "classification": CARRIER_CLASSIFICATION,
        "package": manifest["name"],
        "manifest_version": manifest["version"],
        "version_authority": VERSION_AUTHORITY,
        "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "generator": {
            "id": GENERATOR_ID,
            "version": GENERATOR_VERSION,
        },
        "contracts": {
            "claude_adapter": registry["contracts"]["claude_adapter"],
        },
    }


def expected_carrier_bytes(root: Path) -> bytes:
    return (json.dumps(expected_carrier_payload(root), indent=2) + "\n").encode("utf-8")


def synchronize(root: Path, *, write: bool) -> list[str]:
    expected = expected_carrier_bytes(root)
    errors: list[str] = []
    paths = carrier_paths(root)
    if not paths:
        return ["no Bedrock skill entrypoints found"]
    for path in paths:
        if write:
            path.write_bytes(expected)
        elif not path.is_file():
            errors.append(f"{path}: package identity carrier is missing")
        elif path.read_bytes() != expected:
            errors.append(f"{path}: package identity carrier is stale or noncanonical")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="Check carriers without changing them (default)")
    mode.add_argument("--write", action="store_true", help="Rewrite every carrier from its authorities")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        errors = synchronize(root, write=args.write)
    except (OSError, json.JSONDecodeError, yaml.YAMLError, KeyError, TypeError) as exc:
        print(f"FAIL: cannot derive package identity: {exc}")
        return 1
    if errors:
        print("FAIL: package identity carriers")
        for error in errors:
            print(f"- {error}")
        return 1
    action = "synchronized" if args.write else "verified"
    print(f"PASS: {len(carrier_paths(root))} package identity carriers {action}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
