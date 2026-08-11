#!/usr/bin/env python3
"""Validate the portable frontend profile, evidence, fixtures, and skill contract."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

from jsonschema import Draft202012Validator
import yaml


REQUIRED_SECURITY = {
    "xss-dom-sinks",
    "trusted-types",
    "safe-urls-dom-clobbering",
    "csrf-cookie-coupling",
    "cors-handoff",
    "third-party-scripts-sri",
    "service-workers",
    "dependency-install-scripts",
    "source-maps",
    "client-logs-analytics",
}
REQUIRED_BROWSER_FILES = {
    "package.json",
    "package-lock.json",
    "index.html",
    "tsconfig.json",
    "vite.config.ts",
    "vitest.config.ts",
    "playwright.config.ts",
    "eslint.config.js",
    "performance-budget.json",
    "scripts/check-budget.mjs",
    "src/main.tsx",
    "src/App.tsx",
    "src/browser-contract.ts",
    "src/styles.css",
    "tests/component.test.tsx",
    "tests/browser.spec.ts",
    "tests/accessibility.spec.ts",
    "tests/security.spec.ts",
}


def _read_yaml(path: Path) -> dict[str, Any]:
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top level must be a mapping")
    return value


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top level must be an object")
    return value


def _schema_errors(schema: dict[str, Any], value: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema)
    return [error.message for error in sorted(validator.iter_errors(value), key=lambda item: list(item.path))]


def _profile_semantic_errors(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    api = value.get("api_contract", {})
    if "sha256:" not in str(api.get("spec_artifact", "")) or "@" not in str(api.get("generator", "")):
        errors.append("immutable API artifact and versioned generator identity are required")

    security = value.get("security", {}).get("concerns", {})
    if set(security) != REQUIRED_SECURITY:
        errors.append("browser security coverage must disposition every required concern")

    if value.get("prototype", {}).get("posture") == "production":
        dispositions = list(security.values()) + list(value.get("production_capabilities", {}).values())
        if any(row.get("status") == "unverified" for row in dispositions if isinstance(row, dict)):
            errors.append("production profile cannot leave required concern unverified")
    return errors


def _evidence_semantic_errors(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    engines = {row.get("engine") for row in value.get("browser_runs", []) if isinstance(row, dict)}
    if not {"chromium", "firefox", "webkit"}.issubset(engines):
        errors.append("browser evidence must include chromium, firefox, and webkit")
    manual = value.get("manual_accessibility", {})
    if manual.get("status") == "pass" and not (
        str(manual.get("browser", "")).lower() == "safari"
        and str(manual.get("assistive_technology", "")).lower() == "voiceover"
    ):
        errors.append("passing manual evidence must identify Safari and VoiceOver")
    return errors


def _behavior_errors(path: Path) -> list[str]:
    payload = _read_yaml(path)
    errors: list[str] = []
    expected = {
        "frontend-code-portable-profile": "frontend-code",
        "frontend-code-prototype-promotion": "frontend-code",
        "frontend-code-browser-security-readiness": "frontend-code",
        "overlap-testing-frontend": "testing",
        "overlap-debug-frontend": "debug",
        "overlap-review-frontend": "code-review",
        "overlap-frontend-backend-enforcement": "application-code",
    }
    rows = payload.get("cases", [])
    observed = {row.get("id"): row.get("expected_owner") for row in rows if isinstance(row, dict)}
    if observed != expected:
        errors.append(f"{path}: behavior ownership drift; observed={observed}, expected={expected}")
    return errors


def validate_frontend_contracts(root: Path, *, required: bool = True) -> list[str]:
    contract_path = root / "validation/frontend-contracts.yaml"
    if not contract_path.exists():
        return [f"{contract_path}: required frontend contract is missing"] if required else []

    errors: list[str] = []
    try:
        contract = _read_yaml(contract_path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return [str(exc)]
    if contract.get("schema_version") != 1:
        errors.append(f"{contract_path}: schema_version must be 1")

    schemas: dict[str, dict[str, Any]] = {}
    for name, relative in contract.get("schemas", {}).items():
        path = root / relative
        try:
            schemas[name] = _read_json(path)
            Draft202012Validator.check_schema(schemas[name])
        except Exception as exc:  # jsonschema exposes several schema error types
            errors.append(f"{path}: invalid schema: {exc}")

    for row in contract.get("fixtures", {}).get("valid", []):
        path = root / row["path"]
        try:
            value = _read_json(path)
            found = _schema_errors(schemas[row["schema"]], value)
            found.extend(_profile_semantic_errors(value) if row["schema"] == "frontend_profile" else _evidence_semantic_errors(value))
            if found:
                errors.append(f"{path}: valid fixture failed: {found}")
        except Exception as exc:
            errors.append(f"{path}: valid fixture could not be evaluated: {exc}")

    for row in contract.get("fixtures", {}).get("invalid", []):
        path = root / row["path"]
        try:
            value = _read_json(path)
            found = _schema_errors(schemas[row["schema"]], value)
            found.extend(_profile_semantic_errors(value) if row["schema"] == "frontend_profile" else _evidence_semantic_errors(value))
            rendered = "schema: " + "; ".join(found)
            if not found:
                errors.append(f"{path}: invalid fixture unexpectedly passed")
            elif row["expected"].lower() not in rendered.lower():
                errors.append(f"{path}: expected {row['expected']!r}, observed {rendered!r}")
        except Exception as exc:
            errors.append(f"{path}: invalid fixture could not be evaluated: {exc}")

    try:
        errors.extend(_behavior_errors(root / contract["behavior"]))
    except Exception as exc:
        errors.append(str(exc))

    for relative, markers in contract.get("required_contract_markers", {}).items():
        path = root / relative
        text = path.read_text(encoding="utf-8") if path.exists() else ""
        for marker in markers:
            if marker not in text:
                errors.append(f"{path}: required contract marker is missing: {marker!r}")

    skill_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (root / "plugins/bedrock/skills/frontend-code").rglob("*.md")
    )
    for marker in contract.get("forbidden_markers", []):
        if marker in skill_text:
            errors.append(f"frontend skill corpus retains forbidden marker: {marker!r}")

    app = root / contract["browser_app"]
    observed_files = {str(path.relative_to(app)) for path in app.rglob("*") if path.is_file()} if app.exists() else set()
    missing = sorted(REQUIRED_BROWSER_FILES - observed_files)
    if missing:
        errors.append(f"{app}: browser fixture missing files: {missing}")
    else:
        package = _read_json(app / "package.json")
        if set(contract.get("required_gate_ids", [])) - set(package.get("scripts", {})):
            errors.append(f"{app / 'package.json'}: required frontend gate scripts are missing")
        lock = _read_json(app / "package-lock.json")
        if lock.get("lockfileVersion") != 3:
            errors.append(f"{app / 'package-lock.json'}: lockfileVersion must be 3")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_frontend_contracts(root)
    if errors:
        print(f"FAIL: {len(errors)} frontend contract error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: frontend profile, evidence, behavior, browser fixture, and contract markers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
