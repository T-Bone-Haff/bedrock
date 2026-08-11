#!/usr/bin/env python3
"""Validate the portable HEB-115 application, testing, and debug contracts."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError


EXPECTED_ROUTES = {
    "planned-test": "testing",
    "observed-failure": "debug",
    "ci-only-flake": "debug",
    "authorized-repair": "application-code",
    "unauthorized-repair": "debug",
    "planned-endpoint": "application-code",
}


def _json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{path}: top level must be an object")
        return None
    return value


def _semantic_debug(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for item in value.get("evidence", []):
        if not isinstance(item, dict):
            continue
        captured_at = item.get("captured_at")
        if not isinstance(captured_at, str):
            continue
        try:
            parsed = datetime.fromisoformat(captured_at.replace("Z", "+00:00"))
        except ValueError:
            errors.append("invalid evidence timestamp: expected RFC 3339 date-time")
            continue
        if parsed.tzinfo is None:
            errors.append("invalid evidence timestamp: timezone offset is required")
    conclusion = value.get("conclusion", {})
    hypotheses = value.get("hypotheses", [])
    if (
        isinstance(conclusion, dict)
        and conclusion.get("status") == "root_cause_identified"
        and isinstance(hypotheses, list)
        and not any(
            isinstance(item, dict) and item.get("disposition") == "supported"
            for item in hypotheses
        )
    ):
        errors.append("unsupported root cause: no supported hypothesis")
    if (
        isinstance(conclusion, dict)
        and conclusion.get("status") == "root_cause_identified"
        and isinstance(hypotheses, list)
        and any(
            isinstance(item, dict)
            and item.get("disposition") == "supported"
            and item.get("unexplained")
            for item in hypotheses
        )
    ):
        errors.append("unsupported root cause: supported hypothesis retains unexplained evidence")
    return errors


def _load_registry(root: Path, required: bool) -> tuple[dict[str, Any] | None, list[str]]:
    path = root / "validation/application-test-debug-contracts.yaml"
    if not path.is_file():
        return None, [f"{path}: required application/test/debug contract registry is missing"] if required else []
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return None, [f"{path}: invalid registry: {exc}"]
    if not isinstance(value, dict):
        return None, [f"{path}: registry must be a mapping"]
    return value, []


def validate_application_test_debug_contracts(
    root: Path, *, required: bool = True
) -> list[str]:
    errors: list[str] = []
    registry, registry_errors = _load_registry(root, required)
    errors.extend(registry_errors)
    if registry is None:
        return errors
    if registry.get("schema_version") != 1:
        errors.append("validation/application-test-debug-contracts.yaml: schema_version must be 1")

    schemas: dict[str, dict[str, Any]] = {}
    schema_rows = registry.get("schemas")
    if not isinstance(schema_rows, dict):
        errors.append("validation/application-test-debug-contracts.yaml: schemas must be a mapping")
        return errors
    for name, relative in schema_rows.items():
        if not isinstance(name, str) or not isinstance(relative, str):
            errors.append("validation/application-test-debug-contracts.yaml: schema entries must be string pairs")
            continue
        schema = _json(root / relative, errors)
        if schema is None:
            continue
        try:
            Draft202012Validator.check_schema(schema)
        except SchemaError as exc:
            errors.append(f"{relative}: invalid JSON Schema: {exc.message}")
            continue
        schemas[name] = schema

    def fixture_failures(row: Any) -> list[str]:
        if not isinstance(row, dict):
            return ["registry fixture row must be a mapping"]
        relative = row.get("path")
        schema_name = row.get("schema")
        if not isinstance(relative, str) or not relative:
            return ["registry fixture path must be a non-empty string"]
        if not isinstance(schema_name, str) or schema_name not in schemas:
            return ["schema unavailable"]
        path = root / relative
        value = _json(path, errors)
        if value is None:
            return ["invalid JSON"]
        schema = schemas[schema_name]
        failures = [
            failure.message
            for failure in Draft202012Validator(
                schema, format_checker=FormatChecker()
            ).iter_errors(value)
        ]
        if schema_name == "debug" and not failures:
            failures.extend(_semantic_debug(value))
        return failures

    fixture_rows = registry.get("fixtures")
    if not isinstance(fixture_rows, dict):
        errors.append("validation/application-test-debug-contracts.yaml: fixtures must be a mapping")
        return errors
    valid_rows = fixture_rows.get("valid")
    invalid_rows = fixture_rows.get("invalid")
    if not isinstance(valid_rows, list) or not isinstance(invalid_rows, list):
        errors.append("validation/application-test-debug-contracts.yaml: fixture groups must be lists")
        return errors

    for row in valid_rows:
        failures = fixture_failures(row)
        if failures:
            path = row.get("path", "<invalid-registry-row>") if isinstance(row, dict) else "<invalid-registry-row>"
            errors.append(f"{path}: valid fixture rejected: {failures[0]}")

    for row in invalid_rows:
        failures = fixture_failures(row)
        if not isinstance(row, dict):
            errors.append(f"<invalid-registry-row>: invalid fixture declaration: {failures[0]}")
            continue
        expected = row.get("expected")
        path = row.get("path", "<invalid-registry-row>")
        if expected == "schema":
            if not failures:
                errors.append(f"{path}: invalid fixture was accepted")
        elif not any(str(expected) in failure for failure in failures):
            errors.append(f"{path}: expected failure {expected!r}, got {failures!r}")

    behavior_path = root / str(registry.get("behavior", ""))
    try:
        behavior = yaml.safe_load(behavior_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{behavior_path}: invalid behavior fixture: {exc}")
        behavior = {}
    if not isinstance(behavior, dict):
        errors.append(f"{behavior_path}: behavior fixture must be a mapping")
        behavior = {}
    actual_routes = {
        row.get("id"): row.get("expected_owner")
        for row in behavior.get("cases", [])
        if isinstance(row, dict)
    }
    if actual_routes != EXPECTED_ROUTES:
        errors.append(
            f"{behavior_path}: routing boundary mismatch; expected={EXPECTED_ROUTES!r}, actual={actual_routes!r}"
        )

    marker_rows = registry.get("required_contract_markers")
    if not isinstance(marker_rows, dict):
        errors.append("validation/application-test-debug-contracts.yaml: required markers must be a mapping")
        marker_rows = {}
    for relative, markers in marker_rows.items():
        if not isinstance(relative, str) or not isinstance(markers, list):
            errors.append("validation/application-test-debug-contracts.yaml: marker entries are malformed")
            continue
        path = root / relative
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{relative}: cannot read contract: {exc}")
            continue
        for marker in markers:
            if not isinstance(marker, str):
                errors.append(f"{relative}: required contract marker must be a string")
                continue
            if marker not in text:
                errors.append(f"{relative}: missing required contract marker {marker!r}")

    corpus = "\n".join(
        path.read_text(encoding="utf-8")
        for directory in (
            root / "plugins/bedrock/skills/application-code",
            root / "plugins/bedrock/skills/testing",
            root / "plugins/bedrock/skills/debug",
        )
        for path in directory.rglob("*.md")
    )
    forbidden_markers = registry.get("forbidden_markers")
    if not isinstance(forbidden_markers, list):
        errors.append("validation/application-test-debug-contracts.yaml: forbidden_markers must be a list")
        forbidden_markers = []
    for marker in forbidden_markers:
        if not isinstance(marker, str):
            errors.append("validation/application-test-debug-contracts.yaml: forbidden marker must be a string")
            continue
        if marker in corpus:
            errors.append(f"application/test/debug contract: forbidden marker remains {marker!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_application_test_debug_contracts(args.root.resolve())
    if errors:
        print(f"FAIL: {len(errors)} application/test/debug contract error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: application/test/debug contracts and fixtures validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
