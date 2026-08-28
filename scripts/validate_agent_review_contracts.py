#!/usr/bin/env python3
"""Deterministically validate the HEB-116 portable agent/review contracts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from typing import Any

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


SHA256 = re.compile(r"^[0-9a-f]{64}$")
SEMVER = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def _balanced_json_candidates(text: str) -> list[Any]:
    """Return non-overlapping balanced object/array spans; never choose the first."""
    candidates: list[Any] = []
    start = 0
    while start < len(text):
        while start < len(text) and text[start] not in "[{":
            start += 1
        if start >= len(text):
            break
        stack: list[str] = []
        quoted = escaped = False
        completed = False
        for end in range(start, len(text)):
            char = text[end]
            if quoted:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    quoted = False
                continue
            if char == '"':
                quoted = True
            elif char in "[{":
                stack.append(char)
            elif char in "]}":
                if not stack or (stack[-1], char) not in {("[", "]"), ("{", "}")}:
                    break
                stack.pop()
                if not stack:
                    try:
                        candidates.append(json.loads(text[start : end + 1]))
                    except json.JSONDecodeError:
                        pass
                    start = end + 1
                    completed = True
                    break
        if not completed:
            start += 1
    return candidates


def _load_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{path}: top level must be an object")
        return None
    return value


def _validate_agent(value: dict[str, Any], path: Path, errors: list[str]) -> None:
    required = {"schema_version", "invocation_id", "actor_id", "profile", "prompt", "output_schema", "budget", "attempts", "parse", "usage", "terminal_disposition"}
    if not required <= value.keys():
        errors.append(f"{path}: agent execution missing required fields")
    parse = value.get("parse", {})
    if not isinstance(parse, dict) or not SHA256.fullmatch(str(parse.get("response_sha256", ""))):
        errors.append(f"{path}: invalid response provenance")
    budget = value.get("budget", {})
    attempts = value.get("attempts", [])
    if isinstance(budget, dict) and isinstance(attempts, list) and len(attempts) > int(budget.get("max_attempts", 0)):
        errors.append(f"{path}: aggregate attempt budget exceeded")


def _validate_review(value: dict[str, Any], path: Path, errors: list[str]) -> None:
    kind = value.get("kind")
    if kind == "reviewer_result":
        if not isinstance(value.get("findings"), list) or not isinstance(value.get("survived_attacks"), list):
            errors.append(f"{path}: reviewer arrays are required")
    elif kind == "arbitration_result":
        if value.get("classification") == "resolvable" and value.get("confidence") == "low":
            errors.append(f"{path}: low-confidence resolvable is invalid")
        if value.get("classification") == "resolvable" and not value.get("authority_locus"):
            errors.append(f"{path}: resolvable arbitration requires authority_locus")
        for field in ("finding_id", "input_sha256"):
            if not SHA256.fullmatch(str(value.get(field, ""))):
                errors.append(f"{path}: invalid {field}")
    else:
        errors.append(f"{path}: unknown design-review result kind")


def evaluate_runner_profile_case(case: dict[str, Any]) -> str:
    profile = case.get("profile")
    if profile == "direct":
        return "direct-review-complete"
    if profile == "multi-perspective":
        return "multi-perspective-review-complete"
    if profile != "runner-backed":
        return "stop-unavailable"
    if not all(
        (
            isinstance(case.get("product_binding_id"), str)
            and bool(case["product_binding_id"].strip()),
            isinstance(case.get("product_binding_version"), str)
            and bool(SEMVER.fullmatch(case["product_binding_version"])),
            isinstance(case.get("runner_id"), str) and bool(case["runner_id"].strip()),
            isinstance(case.get("runner_version"), str)
            and bool(SEMVER.fullmatch(case["runner_version"])),
            case.get("schemas_compatible") is True,
            isinstance(case.get("invocation"), str) and bool(case["invocation"].strip()),
            case.get("fresh_gate_evidence") is True,
        )
    ):
        return "stop-unavailable"
    return "runner-backed-claim-permitted"


def validate_agent_review_contracts(root: Path, *, required: bool = True) -> list[str]:
    errors: list[str] = []
    registry_path = root / "validation/agent-review-contracts.yaml"
    if not registry_path.is_file():
        return [f"{registry_path}: required agent-review contract registry is missing"] if required else []
    try:
        registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return [f"{registry_path}: invalid registry: {exc}"]
    for relative in registry.get("schemas", {}).values():
        schema = _load_json(root / relative, errors)
        if schema is not None and schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            errors.append(f"{relative}: schema must declare draft 2020-12")
        if schema is not None:
            try:
                Draft202012Validator.check_schema(schema)
            except SchemaError as exc:
                errors.append(f"{relative}: invalid JSON Schema: {exc.message}")
    schema_documents = {
        name: _load_json(root / relative, errors)
        for name, relative in registry.get("schemas", {}).items()
    }
    for relative in registry.get("fixtures", {}).get("valid", []):
        path = root / relative
        value = _load_json(path, errors)
        if value is None:
            continue
        if "actor_id" in value:
            _validate_agent(value, path, errors)
            schema = schema_documents.get("agent_execution")
        else:
            _validate_review(value, path, errors)
            schema = schema_documents.get("design_review_result")
        if schema is not None:
            failures = sorted(Draft202012Validator(schema).iter_errors(value), key=lambda item: list(item.path))
            if failures:
                errors.append(f"{path}: valid fixture or schema failed: {failures[0].message}")
    invalid_rows = registry.get("fixtures", {}).get("invalid", [])
    for row in invalid_rows:
        path = root / row["path"]
        if row["expected"] == "ambiguous salvage":
            if len(_balanced_json_candidates(path.read_text(encoding="utf-8"))) < 2:
                errors.append(f"{path}: ambiguous salvage fixture did not produce multiple candidates")
        else:
            value = _load_json(path, errors)
            fixture_errors: list[str] = []
            if value is not None:
                _validate_review(value, path, fixture_errors)
            if not any(row["expected"] in error for error in fixture_errors):
                errors.append(f"{path}: invalid fixture was accepted")
    for relative, markers in registry.get("required_contract_markers", {}).items():
        text = (root / relative).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"{relative}: missing required contract marker {marker!r}")
    corpus = "\n".join(path.read_text(encoding="utf-8") for directory in (root / "plugins/bedrock/skills/agent-code", root / "plugins/bedrock/skills/design-review-loop") for path in directory.rglob("*.md"))
    for marker in registry.get("forbidden_markers", []):
        if marker in corpus:
            errors.append(f"agent/review contract: forbidden marker remains {marker!r}")
    for relative in registry.get("forbidden_paths", []):
        if (root / relative).exists():
            errors.append(f"agent/review contract: forbidden path remains {relative!r}")
    runner_cases = registry.get("runner_profile_cases")
    if not isinstance(runner_cases, list) or not runner_cases:
        errors.append("agent/review contract: runner_profile_cases must be a non-empty list")
    else:
        case_ids = [case.get("id") for case in runner_cases if isinstance(case, dict)]
        if len(case_ids) != len(runner_cases) or len(case_ids) != len(set(case_ids)):
            errors.append("agent/review contract: runner profile case ids must be unique")
        for index, case in enumerate(runner_cases):
            if not isinstance(case, dict) or not isinstance(case.get("input"), dict):
                errors.append(f"agent/review contract: runner profile case[{index}] is invalid")
                continue
            actual = evaluate_runner_profile_case(case["input"])
            if actual != case.get("expected"):
                errors.append(
                    f"agent/review contract: runner profile case {case.get('id')!r} "
                    f"expected {case.get('expected')!r}, got {actual!r}"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_agent_review_contracts(args.root.resolve())
    if errors:
        print(f"FAIL: {len(errors)} agent/review contract error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: agent/review contracts and fixtures validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
