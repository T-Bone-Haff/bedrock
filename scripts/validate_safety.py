#!/usr/bin/env python3
"""Deterministic safety-contract validation for the HEB-110 overlay."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from typing import Any

import yaml


FULL_SHA = re.compile(r"[0-9a-fA-F]{40}")
ACTION_REFERENCE = re.compile(r"^\s*uses:\s*([^\s@]+)@([^\s#]+)", re.MULTILINE)
COUNTED_SEVERITIES = {"BLOCKING", "MATERIAL"}
EXPECTED_FINDINGS = {"APP-002", "INF-002", "INF-004", "DLV-002", "DRL-004"}


def _read(root: Path, relative: str, errors: list[str]) -> str:
    path = root / relative
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{relative}: cannot read file: {exc}")
        return ""


def _require(text: str, needle: str, relative: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"{relative}: missing required safety contract: {needle!r}")


def _forbid(text: str, needle: str, relative: str, errors: list[str]) -> None:
    if needle in text:
        errors.append(f"{relative}: unsafe or contradictory guidance remains: {needle!r}")


def validate_action_pins(root: Path, errors: list[str]) -> None:
    scan_roots = (
        root / ".github" / "workflows",
        root / "plugins" / "bedrock" / "skills",
        root / "tests" / "fixtures" / "safety",
    )
    for scan_root in scan_roots:
        if not scan_root.is_dir():
            continue
        for path in sorted(scan_root.rglob("*")):
            if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml"}:
                continue
            text = path.read_text(encoding="utf-8")
            for match in ACTION_REFERENCE.finditer(text):
                action, reference = match.groups()
                if action.startswith("./") or action.startswith("docker://"):
                    continue
                if not FULL_SHA.fullmatch(reference):
                    relative = path.relative_to(root)
                    errors.append(
                        f"{relative}: third-party Action {action}@{reference} must use a full commit SHA"
                    )


def validate_pull_request_build_fixture(root: Path, errors: list[str]) -> None:
    relative = "tests/fixtures/safety/pr-image-build.yml"
    text = _read(root, relative, errors)
    if not text:
        return
    try:
        workflow = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        errors.append(f"{relative}: invalid YAML: {exc}")
        return
    events = workflow.get("on") if isinstance(workflow, dict) else None
    if not isinstance(events, dict) or "pull_request" not in events:
        errors.append(f"{relative}: must run for pull_request events")
    if not isinstance(workflow, dict) or workflow.get("permissions") != {"contents": "read"}:
        errors.append(f"{relative}: top-level permissions must be contents: read only")
    if "docker build" not in text:
        errors.append(f"{relative}: pull-request fixture must build the service image")
    for forbidden in ("docker push", "docker login", "google-github-actions/auth", "id-token: write"):
        if forbidden in text:
            errors.append(f"{relative}: pull-request build must not contain {forbidden!r}")


def route_safety_case(case: dict[str, Any]) -> str:
    """Evaluate only the DRL-004 severity/classification safety invariant."""
    if case.get("status") != "open":
        return "CONVERGED"
    severity = case.get("severity")
    classification = case.get("classification")
    if classification == "decision-bearing" and severity not in COUNTED_SEVERITIES:
        return "INVALID"
    if classification == "decision-bearing":
        return "HALT_DECISION"
    if severity in COUNTED_SEVERITIES:
        return "CONTINUE"
    return "CONVERGED"


def validate_convergence_fixtures(root: Path, errors: list[str]) -> None:
    relative = "tests/fixtures/safety/convergence.yaml"
    text = _read(root, relative, errors)
    if not text:
        return
    try:
        payload = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        errors.append(f"{relative}: invalid YAML: {exc}")
        return
    cases = payload.get("cases") if isinstance(payload, dict) else None
    if not isinstance(cases, list):
        errors.append(f"{relative}: cases must be a list")
        return
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"{relative}:case[{index}]: must be a mapping")
            continue
        actual = route_safety_case(case)
        if actual != case.get("expected"):
            errors.append(
                f"{relative}:case[{index}]: expected {case.get('expected')!r}, got {actual!r}"
            )


def validate_evidence_manifest(root: Path, errors: list[str]) -> None:
    relative = "tests/fixtures/safety/manifest.yaml"
    text = _read(root, relative, errors)
    if not text:
        return
    try:
        payload = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        errors.append(f"{relative}: invalid YAML: {exc}")
        return
    findings = payload.get("findings") if isinstance(payload, dict) else None
    if not isinstance(findings, list):
        errors.append(f"{relative}: findings must be a list")
        return
    identifiers: set[str] = set()
    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            errors.append(f"{relative}:finding[{index}]: must be a mapping")
            continue
        identifier = finding.get("id")
        if not isinstance(identifier, str):
            errors.append(f"{relative}:finding[{index}]: id must be a string")
            continue
        identifiers.add(identifier)
    if identifiers != EXPECTED_FINDINGS:
        errors.append(
            f"{relative}: finding coverage mismatch; expected={sorted(EXPECTED_FINDINGS)}, "
            f"actual={sorted(str(identifier) for identifier in identifiers)}"
        )
    for index, finding in enumerate(findings):
        if not isinstance(finding, dict):
            continue
        evidence = finding.get("evidence")
        if not isinstance(evidence, list) or not evidence or not all(
            isinstance(item, str) and item for item in evidence
        ):
            errors.append(f"{relative}:finding[{index}]: evidence must be a non-empty string list")


def validate_safety_contracts(root: Path) -> list[str]:
    errors: list[str] = []

    app_relative = "plugins/bedrock/skills/application-code/reference/01-code-structure.md"
    app = _read(root, app_relative, errors)
    _forbid(app, "/usr/local/lib/python3.11/site-packages", app_relative, errors)
    _require(app, "COPY --from=builder /opt/venv /opt/venv", app_relative, errors)
    _require(app, 'ENV PATH="/opt/venv/bin:$PATH"', app_relative, errors)
    _require(app, 'CMD ["python", "-m", "uvicorn"', app_relative, errors)

    infra_relative = "plugins/bedrock/skills/infrastructure-code/SKILL.md"
    infra = _read(root, infra_relative, errors)
    _forbid(infra, "No secrets in configuration or state.", infra_relative, errors)
    _forbid(infra, "Secrets come from Secret Manager via data sources", infra_relative, errors)
    _require(infra, "potentially state-resident", infra_relative, errors)

    state_relative = (
        "plugins/bedrock/skills/infrastructure-code/reference/03-state-and-environments.md"
    )
    state = _read(root, state_relative, errors)
    _forbid(state, "Secret Manager via a data source", state_relative, errors)
    _require(state, "secret payload", state_relative, errors)
    _require(state, "runtime identity", state_relative, errors)

    delivery_relative = (
        "plugins/bedrock/skills/app-delivery-pipeline/reference/02-python-service-leg.md"
    )
    delivery = _read(root, delivery_relative, errors)
    _forbid(delivery, "PR runs verify but does not build", delivery_relative, errors)
    _require(delivery, "pull requests build", delivery_relative, errors)
    _require(delivery, "push: false", delivery_relative, errors)

    drl_relative = "plugins/bedrock/skills/design-review-loop/SKILL.md"
    drl = _read(root, drl_relative, errors)
    _forbid(drl, "even a COSMETIC one", drl_relative, errors)
    _require(drl, "decision-bearing defect must be `BLOCKING` or `MATERIAL`", drl_relative, errors)

    convergence_relative = (
        "plugins/bedrock/skills/design-review-loop/reference/convergence-machinery.md"
    )
    convergence = _read(root, convergence_relative, errors)
    _forbid(convergence, "even a COSMETIC one", convergence_relative, errors)
    _forbid(convergence, "Orthogonal to severity", convergence_relative, errors)
    _require(
        convergence,
        "decision-bearing defect must use `BLOCKING` or `MATERIAL`",
        convergence_relative,
        errors,
    )
    _require(
        convergence,
        "not a conforming runner-backed profile",
        convergence_relative,
        errors,
    )

    reviewer_relative = (
        "plugins/bedrock/skills/design-review-loop/reference/reviewer-instrument.md"
    )
    reviewer = _read(root, reviewer_relative, errors)
    _require(
        reviewer,
        "Never emit a choice requiring operator action as `COSMETIC`",
        reviewer_relative,
        errors,
    )

    validate_action_pins(root, errors)
    validate_pull_request_build_fixture(root, errors)
    validate_convergence_fixtures(root, errors)
    validate_evidence_manifest(root, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_safety_contracts(args.root.resolve())
    if errors:
        print(f"FAIL: {len(errors)} safety validation error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: HEB-110 deterministic safety contracts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
