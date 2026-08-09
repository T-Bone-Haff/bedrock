#!/usr/bin/env python3
"""Deterministic Bedrock plugin validation for HEB-108 / minimum HEB-109."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import Any

import yaml


EXPECTED_SKILLS = (
    "agent-code",
    "app-delivery-pipeline",
    "application-code",
    "author-construct-spec",
    "author-decision-record",
    "author-execution-relay",
    "author-standard",
    "code-review",
    "debug",
    "design-review-loop",
    "frontend-code",
    "infrastructure-code",
    "testing",
)
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DESCRIPTION_LIMIT = 1024


def _error(errors: list[str], location: Path | str, message: str) -> None:
    errors.append(f"{location}: {message}")


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        _error(errors, path, f"cannot read file: {exc}")
        return None

    if not lines or lines[0] != "---":
        _error(errors, path, "must begin with a YAML frontmatter delimiter")
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        _error(errors, path, "missing closing YAML frontmatter delimiter")
        return None

    try:
        metadata = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        _error(errors, path, f"invalid YAML frontmatter: {exc}")
        return None
    if not isinstance(metadata, dict):
        _error(errors, path, "frontmatter must be a mapping")
        return None
    return metadata


def validate_skills(root: Path, errors: list[str]) -> dict[str, dict[str, Any]]:
    skills_dir = root / "plugins" / "bedrock" / "skills"
    if not skills_dir.is_dir():
        _error(errors, skills_dir, "skills directory is missing")
        return {}

    skill_dirs = sorted(path.name for path in skills_dir.iterdir() if path.is_dir())
    if tuple(skill_dirs) != EXPECTED_SKILLS:
        missing = sorted(set(EXPECTED_SKILLS) - set(skill_dirs))
        extra = sorted(set(skill_dirs) - set(EXPECTED_SKILLS))
        _error(errors, skills_dir, f"skill inventory mismatch; missing={missing}, extra={extra}")

    inventory: dict[str, dict[str, Any]] = {}
    seen_names: dict[str, Path] = {}
    for directory_name in skill_dirs:
        skill_path = skills_dir / directory_name / "SKILL.md"
        if not skill_path.is_file():
            _error(errors, skill_path, "required skill entrypoint is missing")
            continue
        metadata = parse_frontmatter(skill_path, errors)
        if metadata is None:
            continue

        extra_keys = sorted(set(metadata) - {"name", "description"})
        if extra_keys:
            _error(errors, skill_path, f"unsupported frontmatter keys: {extra_keys}")

        name = metadata.get("name")
        description = metadata.get("description")
        if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
            _error(errors, skill_path, "name must be a non-empty kebab-case string")
            continue
        if name != directory_name:
            _error(errors, skill_path, f"name {name!r} must match directory {directory_name!r}")
        if name in seen_names:
            _error(errors, skill_path, f"duplicate skill name; first declared at {seen_names[name]}")
        else:
            seen_names[name] = skill_path

        if not isinstance(description, str) or not description.strip():
            _error(errors, skill_path, "description must be a non-empty string")
            continue
        if len(description) > DESCRIPTION_LIMIT:
            _error(
                errors,
                skill_path,
                f"description length {len(description)} exceeds {DESCRIPTION_LIMIT}",
            )
        if "Use " not in description:
            _error(errors, skill_path, "description must contain an explicit positive 'Use ...' routing cue")
        if "Do not use" not in description:
            _error(errors, skill_path, "description must contain an explicit negative 'Do not use ...' boundary")

        inventory[name] = {
            "path": str(skill_path.relative_to(root)),
            "description": description,
            "description_length": len(description),
        }
    return inventory


def _load_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        _error(errors, path, f"invalid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        _error(errors, path, "top level must be an object")
        return None
    return value


def validate_manifests(root: Path, errors: list[str]) -> None:
    plugin_path = root / "plugins" / "bedrock" / ".claude-plugin" / "plugin.json"
    marketplace_path = root / ".claude-plugin" / "marketplace.json"
    plugin = _load_json(plugin_path, errors)
    marketplace = _load_json(marketplace_path, errors)
    if plugin is None or marketplace is None:
        return

    if plugin.get("name") != "bedrock":
        _error(errors, plugin_path, "plugin name must be 'bedrock'")
    version = plugin.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        _error(errors, plugin_path, "version must be a SemVer core string")

    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        _error(errors, marketplace_path, "plugins must be a list")
        return
    matching = [entry for entry in entries if isinstance(entry, dict) and entry.get("name") == "bedrock"]
    if len(matching) != 1:
        _error(errors, marketplace_path, f"expected exactly one bedrock entry, found {len(matching)}")
        return
    entry = matching[0]
    if entry.get("description") != plugin.get("description"):
        _error(errors, marketplace_path, "bedrock description must equal plugin.json description verbatim")
    source = entry.get("source")
    if not isinstance(source, str):
        _error(errors, marketplace_path, "bedrock source must be a string")
    elif (root / source).resolve() != (root / "plugins" / "bedrock").resolve():
        _error(errors, marketplace_path, "bedrock source must resolve to ./plugins/bedrock")


def load_routing_cases(root: Path, errors: list[str]) -> list[dict[str, Any]]:
    path = root / "tests" / "fixtures" / "routing.yaml"
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        _error(errors, path, f"cannot load routing fixtures: {exc}")
        return []
    if not isinstance(payload, dict) or payload.get("schema_version") != 1:
        _error(errors, path, "schema_version must be 1")
        return []
    cases = payload.get("cases")
    if not isinstance(cases, list):
        _error(errors, path, "cases must be a list")
        return []
    valid_cases: list[dict[str, Any]] = []
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            _error(errors, f"{path}:case[{index}]", "case must be a mapping")
            continue
        valid_cases.append(case)
    return valid_cases


def validate_routing(
    root: Path,
    skill_inventory: dict[str, dict[str, Any]],
    errors: list[str],
) -> list[dict[str, Any]]:
    path = root / "tests" / "fixtures" / "routing.yaml"
    cases = load_routing_cases(root, errors)
    known = set(skill_inventory)
    positive: set[str] = set()
    negative: set[str] = set()
    ids: set[str] = set()

    for index, case in enumerate(cases):
        location = f"{path}:case[{index}]"
        case_id = case.get("id")
        kind = case.get("kind")
        prompt = case.get("prompt")
        expected = case.get("expected")
        excluded = case.get("excluded", [])
        alternates = case.get("allowed_alternates", [])
        if not isinstance(case_id, str) or not case_id:
            _error(errors, location, "id must be a non-empty string")
        elif case_id in ids:
            _error(errors, location, f"duplicate case id {case_id!r}")
        else:
            ids.add(case_id)
        if kind not in {"positive", "negative", "overlap"}:
            _error(errors, location, "kind must be positive, negative, or overlap")
        if case.get("surface") != "portable-core":
            _error(errors, location, "surface must be 'portable-core'; adapters execute shared cases")
        if not isinstance(prompt, str) or not prompt.strip():
            _error(errors, location, "prompt must be a non-empty string")
        if expected is not None and expected not in known:
            _error(errors, location, f"unknown expected skill {expected!r}")
        if not isinstance(excluded, list) or any(item not in known for item in excluded):
            _error(errors, location, "excluded must contain only known skill names")
            excluded = []
        if not isinstance(alternates, list) or any(item not in known for item in alternates):
            _error(errors, location, "allowed_alternates must contain only known skill names")
            alternates = []
        if kind != "overlap" and alternates:
            _error(errors, location, "allowed_alternates is valid only for overlap cases")
        if expected in excluded:
            _error(errors, location, "expected skill cannot also be excluded")
        if set(alternates) & set(excluded):
            _error(errors, location, "allowed_alternates and excluded must be disjoint")
        if kind == "positive" and expected in known:
            positive.add(expected)
        negative.update(excluded)

    for skill in sorted(known):
        if skill not in positive:
            _error(errors, path, f"missing positive routing case for {skill}")
        if skill not in negative:
            _error(errors, path, f"missing negative routing case excluding {skill}")
    return cases


def run_host_validator(root: Path, errors: list[str]) -> None:
    executable = shutil.which("claude")
    if executable is None:
        _error(errors, "claude", "Claude Code CLI is required for strict host validation")
        return
    environment = os.environ.copy()
    environment.pop("CLAUDECODE", None)
    result = subprocess.run(
        [executable, "plugin", "validate", "--strict", str(root / "plugins" / "bedrock")],
        cwd=root,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        detail = (result.stdout + result.stderr).strip()
        _error(errors, "claude plugin validate --strict", detail or f"exited {result.returncode}")


def validate_repository(root: Path, *, run_host_cli: bool = True) -> tuple[list[str], dict[str, Any]]:
    errors: list[str] = []
    inventory = validate_skills(root, errors)
    validate_manifests(root, errors)
    cases = validate_routing(root, inventory, errors)
    if run_host_cli:
        run_host_validator(root, errors)

    for name, record in inventory.items():
        record["positive_cases"] = [case.get("id") for case in cases if case.get("expected") == name]
        record["negative_cases"] = [case.get("id") for case in cases if name in case.get("excluded", [])]
        record["overlap_cases"] = [
            case.get("id")
            for case in cases
            if case.get("kind") == "overlap"
            and (case.get("expected") == name or name in case.get("allowed_alternates", []))
        ]
    report = {
        "schema_version": 1,
        "skill_count": len(inventory),
        "description_limit": DESCRIPTION_LIMIT,
        "skills": [inventory[name] | {"name": name} for name in sorted(inventory)],
    }
    return errors, report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--skip-host-cli", action="store_true", help="Skip Claude CLI validation (tests only).")
    parser.add_argument("--inventory", type=Path, help="Write the derived metadata/routing inventory as JSON.")
    args = parser.parse_args()

    root = args.root.resolve()
    errors, report = validate_repository(root, run_host_cli=not args.skip_host_cli)
    if args.inventory:
        args.inventory.parent.mkdir(parents=True, exist_ok=True)
        args.inventory.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"PASS: {report['skill_count']}/{len(EXPECTED_SKILLS)} skills passed deterministic and strict host validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
