#!/usr/bin/env python3
"""Validate the HEB-117 authoring and code-review interaction contracts."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

import jsonschema
import yaml


SCOPED_SKILLS = (
    "author-construct-spec",
    "author-decision-record",
    "author-execution-relay",
    "author-standard",
    "code-review",
)
REQUIRED_FIELDS = {
    "task_class",
    "positive_cues",
    "negative_boundary",
    "inputs",
    "outputs",
    "authority",
    "required_capabilities",
    "optional_capabilities",
    "failure_behavior",
    "evidence",
    "lifecycle",
}


def evaluate_behavior_case(case: dict[str, Any]) -> str:
    """Evaluate the deterministic portion of a contract behavior fixture."""
    kind = case.get("kind")
    data = case.get("input", {})
    if kind == "relay-profile":
        if data.get("risk") == "high" or data.get("reversible") is False:
            return "high-assurance"
        return "standard" if data.get("separated_executor") else "small"
    if kind == "provisional-dependency":
        return "accept" if all(data.get(field) for field in ("owner", "expires", "promotion")) else "reject"
    if kind == "stale-relation":
        return "close" if all(data.get(field) for field in ("repaired", "impact_checked", "verified")) else "keep-open"
    if kind == "evidence-relocation":
        complete = all(data.get(field) for field in ("copied", "integrity", "permissions", "rollback"))
        return "retire-duplicate" if complete else "retain-source"
    if kind == "authorization":
        valid = all(data.get(field) for field in ("actor_authenticated", "scope_match", "fresh", "nonce_unused"))
        return "accept" if valid and not data.get("revoked") else "reject"
    if kind == "substrate":
        return "stop" if data.get("policy") == "untrusted-data" and data.get("attempts_scope_change") else "continue"
    if kind == "review-terminal":
        if not data.get("checked_surfaces") or data.get("blockers") or data.get("failed_required_gates"):
            return "pause"
        return "approve-with-advisory" if data.get("advisory") else "approve"
    if kind == "standard-exception":
        return "accept" if all(data.get(field) for field in ("owner", "scope", "risk", "expires")) else "reject"
    if kind == "consumer-demand":
        allowed = data.get("accepted_values", [])
        demanded = data.get("demanded_value")
        return "accept" if data.get("consumer_read_whole") and demanded in allowed else "reject"
    if kind in {"instrument-demand", "relay-instrument-demand"}:
        required = [
            "consumer_read_whole",
            "taxonomy_verbatim",
            "verdict_pins_complete",
            "structural_instrument",
            "dry_run_passed",
            "unavailable_declared",
            "report_field_declared",
        ]
        if kind == "relay-instrument-demand":
            comparison_involved = data.get("comparison_involved")
            if not isinstance(comparison_involved, bool):
                return "reject"
            if comparison_involved:
                required.extend(
                    [
                        "population_derivation_declared",
                        "expected_state_oracle_declared",
                        "subject_declared",
                        "discrimination_declared",
                    ]
                )
        return "accept" if all(data.get(field) for field in required) else "reject"
    if kind == "population-comparison":
        comparison_available = all(
            data.get(field)
            for field in (
                "derivation_available",
                "canonicalization_declared",
                "expected_state_oracle_declared",
                "subject_declared",
            )
        )
        subject_matches = data.get("subject_matches")
        observed_matches_expected = data.get("observed_matches_expected")
        cross_check_present = data.get("cross_check_present")
        if (
            not comparison_available
            or data.get("comparison_ambiguous")
            or not isinstance(subject_matches, bool)
            or not isinstance(observed_matches_expected, bool)
            or not isinstance(cross_check_present, bool)
        ):
            return "stop-unavailable"
        if not subject_matches:
            return "stop-subject-mismatch"
        second_derivation_agrees = data.get("second_derivation_agrees")
        falsification_control_refused = data.get("falsification_control_refused")
        discrimination_results = [
            result
            for result in (second_derivation_agrees, falsification_control_refused)
            if isinstance(result, bool)
        ]
        if not discrimination_results or not all(discrimination_results):
            return "stop-unavailable"
        if not observed_matches_expected:
            return "stop-state-change"
        cross_check_matches_expected = data.get("cross_check_matches_expected")
        if cross_check_present and not isinstance(cross_check_matches_expected, bool):
            return "stop-unavailable"
        if cross_check_present and not cross_check_matches_expected:
            return "report-relay-defect-and-proceed"
        return "proceed"
    if kind == "touch-derivation":
        edit_loci = set(data.get("edit_loci", []))
        touch_set = set(data.get("touch_set", []))
        settled_support = set(data.get("settled_support", []))
        reconciled = edit_loci <= touch_set <= edit_loci | settled_support
        return "accept" if edit_loci and reconciled else "reject"
    if kind == "custody-reachability":
        required = ("permissions_checked", "code_paths_checked", "actor_flows_checked")
        if not all(data.get(field) for field in required):
            return "incomplete"
        return "reachable" if data.get("production_reference_found") else "unreachable"
    if kind == "premise-falsification":
        if not data.get("control_executed"):
            return "unavailable"
        confirmed = data.get("premise_supported") and data.get("contrary_control_refused")
        return "confirmed" if confirmed else "falsified"
    if kind == "success-as-absence":
        proved = data.get("empty_result") and data.get("counterfactual_executed") and data.get("counterfactual_detected")
        return "proved" if proved else "unproved"
    if kind == "rule-trigger":
        trigger_class = data.get("trigger_class")
        frequency = data.get("frequency")
        salience = data.get("salience")
        enforcement = data.get("enforcement")
        disposition = data.get("disposition")
        if trigger_class == "internal-state":
            if enforcement == "instrument" and disposition == "converted-to-instrument":
                return "ship-instrumented"
            if enforcement == "external-detector" and disposition == "external-detector":
                return "ship-instrumented"
            if disposition == "known-weak":
                return "ship-known-weak"
            return "reject"
        if trigger_class == "workflow-event":
            if disposition == "known-weak":
                return "ship-known-weak"
            if frequency == "high" and salience == "low" and enforcement == "discipline":
                return "strengthen"
            valid_pair = (enforcement, disposition) in {
                ("discipline", "workflow-discipline"),
                ("instrument", "converted-to-instrument"),
                ("external-detector", "external-detector"),
            }
            return "ship" if valid_pair else "reject"
        return "reject"
    return "unknown"


def _load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_authoring_contracts(root: Path, *, required: bool = True) -> list[str]:
    errors: list[str] = []
    registry_path = root / "validation" / "authoring-contracts.yaml"
    if not registry_path.exists():
        if required:
            errors.append(f"{registry_path}: required authoring-contract registry is missing")
        return errors
    try:
        registry = _load_yaml(registry_path)
    except (OSError, yaml.YAMLError) as exc:
        return [f"{registry_path}: invalid YAML: {exc}"]
    if not isinstance(registry, dict) or registry.get("schema_version") != 1:
        errors.append(f"{registry_path}: schema_version must be 1")
        return errors
    skills = registry.get("skills")
    if not isinstance(skills, dict) or tuple(sorted(skills)) != tuple(sorted(SCOPED_SKILLS)):
        errors.append(f"{registry_path}: skills must contain exactly {list(SCOPED_SKILLS)}")
        return errors
    for name, contract in skills.items():
        location = f"{registry_path}:skills.{name}"
        if not isinstance(contract, dict):
            errors.append(f"{location}: contract must be a mapping")
            continue
        missing = sorted(REQUIRED_FIELDS - set(contract))
        extra = sorted(set(contract) - REQUIRED_FIELDS)
        if missing or extra:
            errors.append(f"{location}: field mismatch; missing={missing}, extra={extra}")
        for field in REQUIRED_FIELDS:
            value = contract.get(field)
            if isinstance(value, str) and not value.strip():
                errors.append(f"{location}.{field}: must not be empty")
            if isinstance(value, list) and (not value or not all(isinstance(item, str) and item for item in value)):
                errors.append(f"{location}.{field}: must be a non-empty string list")
        skill_path = root / "plugins" / "bedrock" / "skills" / name / "SKILL.md"
        try:
            skill_text = skill_path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{skill_path}: cannot read interaction-contract carrier: {exc}")
            continue
        if "## Interaction contract" not in skill_text:
            errors.append(f"{skill_path}: missing human-readable Interaction contract")
        for label in ("Inputs", "Output", "Authority", "Capabilities", "Failure", "Evidence", "Lifecycle"):
            if f"**{label}:**" not in skill_text:
                errors.append(f"{skill_path}: interaction contract is missing {label}")
        if name == "author-standard":
            trigger_contract = (
                "## Rule triggers and reliability",
                "workflow-event",
                "internal-state",
                "frequency",
                "salience",
                "instrument",
                "external detector",
                "known-weak",
                "expected failure",
            )
            for fragment in trigger_contract:
                if fragment not in skill_text:
                    errors.append(f"{skill_path}: rule-trigger contract is missing {fragment!r}")
            if "counterfactual" not in skill_text or "absence" not in skill_text:
                errors.append(f"{skill_path}: success-as-absence contract is missing")
        if name == "author-execution-relay":
            instrument_contract = (
                "## Build the execution instrument",
                "outcome taxonomy verbatim",
                "Dry-run",
                "custody",
                "reachability",
                "edit-locus rows",
                "claim subject",
                "population derivation",
                "expected-state oracle",
                "differently-shaped derivation",
                "discrimination control",
                "subject mismatch",
                "state changed",
                "arithmetic or transcription defect",
                "falsification control",
                "confirmed",
                "falsified",
                "unavailable",
            )
            for fragment in instrument_contract:
                if fragment not in skill_text:
                    errors.append(f"{skill_path}: execution-instrument contract is missing {fragment!r}")

    relay_templates = root / "plugins/bedrock/skills/author-execution-relay/templates"
    for path in relay_templates.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for fragment in (
            "instrument contract",
            "Claim subject",
            "Verdict-bearing inputs/pins",
            "Population derivation / expected-state oracle",
            "Structural instrument / discrimination control",
            "differently-shaped derivation",
            "subject mismatch",
            "typed count or member list",
            "state mismatch",
            "arithmetic or transcription defect",
        ):
            if fragment.lower() not in text.lower():
                errors.append(f"{path}: relay instrument template is missing {fragment!r}")
    reviewer_instrument = root / "plugins/bedrock/skills/design-review-loop/reference/reviewer-instrument.md"
    reviewer_text = reviewer_instrument.read_text(encoding="utf-8")
    for fragment in ("## Author the charge from its consumer", "outcome taxonomy verbatim", "Falsification control"):
        if fragment.lower() not in reviewer_text.lower():
            errors.append(f"{reviewer_instrument}: review-charge instrument is missing {fragment!r}")

    manifest_path = root / "tests" / "fixtures" / "authoring-contracts" / "manifest.yaml"
    try:
        manifest = _load_yaml(manifest_path)
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{manifest_path}: invalid YAML: {exc}")
        return errors
    rows = manifest.get("schemas") if isinstance(manifest, dict) else None
    if not isinstance(rows, list) or len(rows) != 3:
        errors.append(f"{manifest_path}: schemas must contain exactly three fixture rows")
        return errors
    for index, row in enumerate(rows):
        location = f"{manifest_path}:schemas[{index}]"
        if not isinstance(row, dict) or set(row) != {"schema", "valid", "invalid"}:
            errors.append(f"{location}: requires schema, valid, and invalid paths")
            continue
        try:
            schema = _load_json(root / row["schema"])
            jsonschema.Draft202012Validator.check_schema(schema)
            validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
            validator.validate(_load_json(root / row["valid"]))
            invalid_payload = _load_json(root / row["invalid"])
        except (OSError, json.JSONDecodeError, jsonschema.SchemaError, jsonschema.ValidationError) as exc:
            errors.append(f"{location}: valid fixture or schema failed: {exc}")
            continue
        if not list(validator.iter_errors(invalid_payload)):
            errors.append(f"{location}: invalid fixture unexpectedly conforms")

    behavior_path = root / "tests/fixtures/authoring-contracts/behavior.yaml"
    behavior = _load_yaml(behavior_path)
    cases = behavior.get("cases") if isinstance(behavior, dict) and behavior.get("schema_version") == 1 else None
    if not isinstance(cases, list) or not cases:
        errors.append(f"{behavior_path}: cases must be a non-empty list")
    else:
        seen: set[str] = set()
        for index, case in enumerate(cases):
            location = f"{behavior_path}:cases[{index}]"
            if not isinstance(case, dict) or not isinstance(case.get("id"), str) or case["id"] in seen:
                errors.append(f"{location}: case requires a unique id")
                continue
            seen.add(case["id"])
            observed = evaluate_behavior_case(case)
            if observed != case.get("expected"):
                errors.append(f"{location}: observed {observed!r}, expected {case.get('expected')!r}")

    review = _load_json(root / "tests/fixtures/authoring-contracts/valid/review.json")
    if review["verdict"] != "pause" and any(item["blocking"] for item in review["findings"]):
        errors.append("valid review fixture approves with an unresolved blocking finding")
    invalid_review = _load_json(root / "tests/fixtures/authoring-contracts/invalid/review.json")
    if invalid_review["verdict"] != "pause" and any(item["blocking"] for item in invalid_review["findings"]):
        pass
    else:
        errors.append("invalid review fixture must exercise the blocking terminal predicate")

    template = root / "plugins/bedrock/skills/author-construct-spec/templates/construct-spec-template.md"
    if template.exists() and len(template.read_text(encoding="utf-8").splitlines()) > 180:
        errors.append(f"{template}: minimal template must not exceed 180 lines")
    decision_templates = root / "plugins/bedrock/skills/author-decision-record/templates"
    for path in decision_templates.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "STANDING —" in text:
            errors.append(f"{path}: use the canonical STANDING: directive syntax")

    evidence_manifest = root / "docs/evidence/heb-117/manifest.yaml"
    try:
        evidence = _load_yaml(evidence_manifest)
    except (OSError, yaml.YAMLError) as exc:
        errors.append(f"{evidence_manifest}: invalid YAML: {exc}")
        return errors
    claims = evidence.get("claims") if isinstance(evidence, dict) and evidence.get("schema_version") == 1 else None
    if not isinstance(claims, list) or not claims:
        errors.append(f"{evidence_manifest}: claims must be a non-empty list")
    else:
        for index, claim in enumerate(claims):
            location = f"{evidence_manifest}:claims[{index}]"
            if not isinstance(claim, dict) or not all(claim.get(field) for field in ("id", "command", "evidence")):
                errors.append(f"{location}: requires id, command, and evidence")
                continue
            for relative in claim["evidence"]:
                if not isinstance(relative, str) or not (root / relative).is_file():
                    errors.append(f"{location}: evidence path does not exist: {relative!r}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_authoring_contracts(root)
    if errors:
        print(f"FAIL: {len(errors)} HEB-117 contract error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(SCOPED_SKILLS)}/{len(SCOPED_SKILLS)} HEB-117 interaction contracts validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
