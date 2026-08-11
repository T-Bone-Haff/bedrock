#!/usr/bin/env python3
"""Validate portable HEB-113 infrastructure and application-delivery contracts."""

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
    "terraform-github-actions": "infrastructure-code",
    "infrastructure-plan-apply": "infrastructure-code",
    "application-image-deploy": "app-delivery-pipeline",
    "static-site-promotion": "app-delivery-pipeline",
    "frontend-gate-semantics": "frontend-code",
    "existing-red-deploy": "debug",
    "finished-workflow-review": "code-review",
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


def _instant(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _semantic_apply(value: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    plan = value.get("plan", {})
    apply = value.get("apply", {})
    created = _instant(plan.get("created_at")) if isinstance(plan, dict) else None
    expires = _instant(plan.get("expires_at")) if isinstance(plan, dict) else None
    if created is None or expires is None or expires <= created:
        failures.append("stale or mismatched plan: expiry must follow creation")
    if not isinstance(plan, dict) or not isinstance(apply, dict):
        return failures
    comparisons = (
        (value.get("source"), plan.get("source"), "source-to-plan"),
        (value.get("source"), apply.get("source"), "source-to-apply"),
        (value.get("target"), plan.get("target"), "target-to-plan"),
        (value.get("target"), apply.get("target"), "target-to-apply"),
        (plan.get("digest"), apply.get("plan_digest"), "plan digest"),
    )
    for left, right, label in comparisons:
        if left != right:
            failures.append(f"stale or mismatched plan: {label} differs")
    target = value.get("target")
    authority = value.get("authority")
    if isinstance(target, dict) and isinstance(authority, dict) and target.get("environment") != authority.get("environment"):
        failures.append("stale or mismatched plan: approval environment differs")
    if isinstance(authority, dict) and apply.get("actor") not in authority.get("authorized_actors", []):
        failures.append("unauthorized apply actor")
    return failures


def _semantic_release(value: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    event = value.get("event", {})
    association = event.get("association") if isinstance(event, dict) else None
    if isinstance(association, str) and any(marker in association.lower() for marker in ("ambiguous", "unknown", "unresolved")):
        failures.append("ambiguous release association")
    artifact = value.get("artifact", {})
    deployment = value.get("deployment", {})
    verification = value.get("verification", {})
    digest = artifact.get("digest") if isinstance(artifact, dict) else None
    if isinstance(deployment, dict) and deployment.get("artifact_digest") != digest:
        failures.append("artifact identity mismatch: deployment differs")
    if isinstance(verification, dict) and verification.get("artifact_digest") != digest:
        failures.append("artifact identity mismatch: verification differs")
    intent = value.get("version_intent", {})
    if isinstance(intent, dict):
        changes = intent.get("changes", [])
        aggregate = intent.get("aggregate")
        non_none = [row.get("intent") for row in changes if isinstance(row, dict) and row.get("intent") != "none"]
        order = {"patch": 1, "minor": 2, "major": 3}
        expected = max(non_none, key=lambda item: order.get(str(item), 0)) if non_none else "none"
        if aggregate != expected and intent.get("override") is None:
            failures.append("release intent aggregation mismatch")
    return failures


def _semantic_delivery_profile(value: dict[str, Any]) -> list[str]:
    static = value.get("static_frontend")
    if static is None:
        return []
    if not isinstance(static, dict):
        return ["static frontend profile must be an object or null"]
    required = {"Content-Security-Policy", "Strict-Transport-Security", "Permissions-Policy", "Referrer-Policy", "X-Content-Type-Options", "frame-ancestors"}
    observed = set(static.get("headers", [])) if isinstance(static.get("headers"), list) else set()
    missing = sorted(required - observed)
    return [f"static frontend headers missing: {', '.join(missing)}"] if missing else []


def _workload_failures(value: object) -> list[str]:
    if not isinstance(value, dict):
        return ["workload must be a mapping"]
    spec = value.get("spec", {})
    template = spec.get("template", {}) if isinstance(spec, dict) else {}
    pod_spec = template.get("spec", {}) if isinstance(template, dict) else {}
    containers = pod_spec.get("containers", []) if isinstance(pod_spec, dict) else []
    failures: list[str] = []
    if not isinstance(containers, list) or not containers:
        return ["workload must declare containers"]
    for container in containers:
        if not isinstance(container, dict):
            failures.append("container must be a mapping")
            continue
        image = container.get("image")
        if not isinstance(image, str) or "@sha256:" not in image:
            failures.append("workload image must be pinned by digest")
        security = container.get("securityContext", {})
        if not isinstance(security, dict) or security.get("runAsNonRoot") is not True:
            failures.append("workload must run as non-root")
        if not isinstance(security, dict) or security.get("allowPrivilegeEscalation") is not False:
            failures.append("workload must disable privilege escalation")
    return failures


def _load_registry(root: Path, required: bool) -> tuple[dict[str, Any] | None, list[str]]:
    path = root / "validation/infrastructure-delivery-contracts.yaml"
    if not path.is_file():
        return None, [f"{path}: required infrastructure/delivery contract registry is missing"] if required else []
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        return None, [f"{path}: invalid registry: {exc}"]
    if not isinstance(value, dict):
        return None, [f"{path}: registry must be a mapping"]
    return value, []


def validate_infrastructure_delivery_contracts(root: Path, *, required: bool = True) -> list[str]:
    errors: list[str] = []
    registry, registry_errors = _load_registry(root, required)
    errors.extend(registry_errors)
    if registry is None:
        return errors
    if registry.get("schema_version") != 1:
        errors.append("validation/infrastructure-delivery-contracts.yaml: schema_version must be 1")

    schemas: dict[str, dict[str, Any]] = {}
    rows = registry.get("schemas")
    if not isinstance(rows, dict):
        errors.append("validation/infrastructure-delivery-contracts.yaml: schemas must be a mapping")
        return errors
    for name, relative in rows.items():
        if not isinstance(name, str) or not isinstance(relative, str):
            errors.append("validation/infrastructure-delivery-contracts.yaml: schema entries must be string pairs")
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
        relative, schema_name = row.get("path"), row.get("schema")
        if not isinstance(relative, str) or not relative:
            return ["registry fixture path must be a non-empty string"]
        if not isinstance(schema_name, str) or schema_name not in schemas:
            return ["schema unavailable"]
        value = _json(root / relative, errors)
        if value is None:
            return ["invalid JSON"]
        failures = [item.message for item in Draft202012Validator(schemas[schema_name], format_checker=FormatChecker()).iter_errors(value)]
        if not failures and schema_name == "infrastructure_apply":
            failures.extend(_semantic_apply(value))
        if not failures and schema_name == "application_release":
            failures.extend(_semantic_release(value))
        if not failures and schema_name == "delivery_profile":
            failures.extend(_semantic_delivery_profile(value))
        return failures

    fixtures = registry.get("fixtures")
    if not isinstance(fixtures, dict) or not isinstance(fixtures.get("valid"), list) or not isinstance(fixtures.get("invalid"), list):
        errors.append("validation/infrastructure-delivery-contracts.yaml: fixture groups must be lists")
        return errors
    for row in fixtures["valid"]:
        failures = fixture_failures(row)
        if failures:
            path = row.get("path", "<invalid-registry-row>") if isinstance(row, dict) else "<invalid-registry-row>"
            errors.append(f"{path}: valid fixture rejected: {failures[0]}")
    for row in fixtures["invalid"]:
        failures = fixture_failures(row)
        if not isinstance(row, dict):
            errors.append(f"<invalid-registry-row>: invalid fixture declaration: {failures[0]}")
            continue
        expected, path = row.get("expected"), row.get("path", "<invalid-registry-row>")
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
    behavior_cases = behavior.get("cases", []) if isinstance(behavior, dict) else []
    behavior_ids = [row.get("id") for row in behavior_cases if isinstance(row, dict)] if isinstance(behavior_cases, list) else []
    if len(behavior_ids) != len(set(behavior_ids)):
        errors.append(f"{behavior_path}: behavior case identifiers must be unique")
    actual = {row.get("id"): row.get("expected_owner") for row in behavior_cases if isinstance(row, dict)} if isinstance(behavior_cases, list) else {}
    if actual != EXPECTED_ROUTES:
        errors.append(f"{behavior_path}: routing boundary mismatch; expected={EXPECTED_ROUTES!r}, actual={actual!r}")

    workload_rows = registry.get("workload_fixtures")
    if not isinstance(workload_rows, dict):
        errors.append("validation/infrastructure-delivery-contracts.yaml: workload_fixtures must be a mapping")
    else:
        for disposition in ("valid", "invalid"):
            relative = workload_rows.get(disposition)
            if not isinstance(relative, str):
                errors.append(f"validation/infrastructure-delivery-contracts.yaml: workload {disposition} path must be a string")
                continue
            try:
                workload = yaml.safe_load((root / relative).read_text(encoding="utf-8"))
            except (OSError, yaml.YAMLError) as exc:
                errors.append(f"{relative}: invalid workload fixture: {exc}")
                continue
            failures = _workload_failures(workload)
            if disposition == "valid" and failures:
                errors.append(f"{relative}: valid workload rejected: {failures[0]}")
            if disposition == "invalid" and not failures:
                errors.append(f"{relative}: invalid workload was accepted")

    marker_rows = registry.get("required_contract_markers")
    if not isinstance(marker_rows, dict):
        errors.append("validation/infrastructure-delivery-contracts.yaml: required markers must be a mapping")
        marker_rows = {}
    for relative, markers in marker_rows.items():
        if not isinstance(relative, str) or not isinstance(markers, list):
            errors.append("validation/infrastructure-delivery-contracts.yaml: marker entries are malformed")
            continue
        try:
            contract = (root / relative).read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{relative}: cannot read contract: {exc}")
            continue
        for marker in markers:
            if not isinstance(marker, str) or marker not in contract:
                errors.append(f"{relative}: missing required contract marker {marker!r}")

    corpus = "\n".join(path.read_text(encoding="utf-8") for directory in (root / "plugins/bedrock/skills/infrastructure-code", root / "plugins/bedrock/skills/app-delivery-pipeline") for path in directory.rglob("*.md"))
    forbidden = registry.get("forbidden_markers")
    if not isinstance(forbidden, list):
        errors.append("validation/infrastructure-delivery-contracts.yaml: forbidden_markers must be a list")
        forbidden = []
    for marker in forbidden:
        if not isinstance(marker, str):
            errors.append("validation/infrastructure-delivery-contracts.yaml: forbidden marker must be a string")
        elif marker in corpus:
            errors.append(f"infrastructure/delivery contract: forbidden marker remains {marker!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_infrastructure_delivery_contracts(args.root.resolve())
    if errors:
        print(f"FAIL: {len(errors)} infrastructure/delivery contract error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: infrastructure/delivery contracts and fixtures validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
