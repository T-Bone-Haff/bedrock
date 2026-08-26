#!/usr/bin/env python3
"""Validate the HEB-136 rule-trigger audit ledger."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

import yaml


LEDGER_PATH = Path("docs/evidence/heb-136/rule-trigger-audit.yaml")
MARKDOWN_ROOT = Path("plugins/bedrock/skills")
TRIGGER_CLASSES = {"workflow-event", "internal-state"}
FREQUENCIES = {"rare", "low", "medium", "high"}
SALIENCE_LEVELS = {"low", "medium", "high"}
ENFORCEMENT_TYPES = {"none", "discipline", "instrument", "external-detector"}
DISPOSITIONS = {
    "pending",
    "workflow-discipline",
    "converted-to-instrument",
    "external-detector",
    "known-weak",
}
RATIFICATION_STATES = {"pending", "ratified", "rejected"}
FINDING_FIELDS = {
    "id",
    "carrier",
    "line",
    "summary",
    "trigger_event",
    "trigger_class",
    "frequency",
    "salience",
    "enforcement",
    "disposition",
    "expected_failure",
    "ratification",
}
COUNT_FIELDS = {
    "carriers_examined",
    "semantic_units_screened",
    "internal_state_rules",
    "converted_to_instrument",
    "external_detector",
    "known_weak",
    "unresolved",
}


def _relative_files(root: Path, pattern: str) -> set[str]:
    return {
        path.relative_to(root).as_posix()
        for path in (root / MARKDOWN_ROOT).rglob(pattern)
        if path.is_file()
    }


def _load_ledger(root: Path) -> tuple[dict | None, list[str]]:
    path = root / LEDGER_PATH
    try:
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    except OSError as exc:
        return None, [f"{path}: cannot read audit ledger: {exc}"]
    except yaml.YAMLError as exc:
        return None, [f"{path}: invalid YAML: {exc}"]
    if not isinstance(payload, dict):
        return None, [f"{path}: audit ledger must be a mapping"]
    return payload, []


def _validate_population(
    *,
    label: str,
    declared: list[str],
    expected: object,
    live: set[str],
) -> list[str]:
    errors: list[str] = []
    if len(declared) != len(set(declared)):
        errors.append(f"{label} inventory contains duplicate paths")
    if not isinstance(expected, int) or expected != len(declared):
        errors.append(f"{label} expected count does not match its inventory")
    if set(declared) != live:
        missing = sorted(live - set(declared))
        stale = sorted(set(declared) - live)
        errors.append(f"{label} population mismatch; missing={missing}, stale={stale}")
    return errors


def _semantic_unit_count(root: Path) -> int:
    """Count deterministic Markdown units without claiming each unit is a rule."""

    total = 0
    for path in sorted((root / MARKDOWN_ROOT).rglob("*.md")):
        in_frontmatter = False
        in_code_fence = False
        paragraph_open = False
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line_number == 1 and line == "---":
                in_frontmatter = True
                continue
            if in_frontmatter:
                if line == "---":
                    in_frontmatter = False
                continue
            if line.startswith("```"):
                if paragraph_open:
                    total += 1
                    paragraph_open = False
                in_code_fence = not in_code_fence
                continue
            if in_code_fence:
                continue
            stripped = line.strip()
            if not stripped:
                if paragraph_open:
                    total += 1
                    paragraph_open = False
                continue
            if stripped.startswith("#"):
                if paragraph_open:
                    total += 1
                    paragraph_open = False
                continue
            is_ordered_item = re.match(r"\d+[.)]\s", stripped) is not None
            if stripped.startswith(("|", "-")) or is_ordered_item:
                if paragraph_open:
                    total += 1
                    paragraph_open = False
                structural_marks = stripped.replace("|", "").replace("-", "").replace(":", "").strip()
                if structural_marks:
                    total += 1
                continue
            paragraph_open = True
        if paragraph_open:
            total += 1
    return total


def _derived_counts(
    findings: list[dict], *, carriers_examined: int, semantic_units_screened: int
) -> dict[str, int]:
    return {
        "carriers_examined": carriers_examined,
        "semantic_units_screened": semantic_units_screened,
        "internal_state_rules": len(findings),
        "converted_to_instrument": sum(
            finding.get("disposition") == "converted-to-instrument" for finding in findings
        ),
        "external_detector": sum(
            finding.get("disposition") == "external-detector" for finding in findings
        ),
        "known_weak": sum(finding.get("disposition") == "known-weak" for finding in findings),
        "unresolved": sum(
            finding.get("disposition") == "pending"
            or finding.get("ratification") != "ratified"
            for finding in findings
        ),
    }


def validate_rule_trigger_audit(root: Path, *, require_complete: bool = False) -> list[str]:
    """Return population, record-shape, and completion errors for the audit."""

    payload, errors = _load_ledger(root)
    if payload is None:
        return errors
    if payload.get("schema_version") != 1:
        errors.append("audit ledger schema_version must be 1")
    if payload.get("ticket") != "HEB-136":
        errors.append("audit ledger ticket must be HEB-136")
    status = payload.get("status")
    if status not in {"inventory", "adjudication", "complete"}:
        errors.append("audit ledger status must be inventory, adjudication, or complete")

    scope = payload.get("scope")
    if not isinstance(scope, dict):
        return errors + ["audit ledger scope must be a mapping"]
    if scope.get("markdown_root") != MARKDOWN_ROOT.as_posix():
        errors.append(f"markdown_root must be {MARKDOWN_ROOT.as_posix()}")

    markdown_carriers = scope.get("markdown_carriers")
    if not isinstance(markdown_carriers, list) or not all(
        isinstance(item, str) and item for item in markdown_carriers
    ):
        errors.append("markdown_carriers must be a list of non-empty paths")
        markdown_carriers = []
    live_markdown = _relative_files(root, "*.md")
    errors.extend(
        _validate_population(
            label="Markdown carrier",
            declared=markdown_carriers,
            expected=scope.get("expected_markdown_carriers"),
            live=live_markdown,
        )
    )
    markdown_inspections = scope.get("markdown_inspections")
    pending_markdown_inspections: list[str] = []
    if not isinstance(markdown_inspections, dict):
        errors.append("markdown_inspections must be a mapping")
    else:
        inspection_paths = set(markdown_inspections)
        if inspection_paths != set(markdown_carriers):
            missing = sorted(set(markdown_carriers) - inspection_paths)
            stale = sorted(inspection_paths - set(markdown_carriers))
            errors.append(
                f"Markdown inspection population mismatch; missing={missing}, stale={stale}"
            )
        for path, inspection in markdown_inspections.items():
            if inspection not in {"pending", "inspected"}:
                errors.append(f"Markdown inspection for {path} must be pending or inspected")
            if inspection == "pending":
                pending_markdown_inspections.append(path)

    structured_rows = scope.get("structured_files")
    if not isinstance(structured_rows, list):
        errors.append("structured_files must be a list")
        structured_rows = []
    structured_paths: list[str] = []
    pending_inspections: list[str] = []
    for index, row in enumerate(structured_rows):
        location = f"structured_files[{index}]"
        if not isinstance(row, dict) or set(row) != {"path", "inspection"}:
            errors.append(f"{location} requires exactly path and inspection")
            continue
        path = row.get("path")
        inspection = row.get("inspection")
        if not isinstance(path, str) or not path:
            errors.append(f"{location}.path must be non-empty")
            continue
        structured_paths.append(path)
        if inspection not in {"pending", "inspected"}:
            errors.append(f"{location}.inspection must be pending or inspected")
        if inspection == "pending":
            pending_inspections.append(path)
    live_structured = set().union(
        _relative_files(root, "*.json"),
        _relative_files(root, "*.yaml"),
        _relative_files(root, "*.yml"),
    )
    errors.extend(
        _validate_population(
            label="structured-file",
            declared=structured_paths,
            expected=scope.get("expected_structured_files"),
            live=live_structured,
        )
    )

    findings = payload.get("findings")
    if not isinstance(findings, list):
        errors.append("findings must be a list")
        findings = []
    seen_ids: set[str] = set()
    for index, rule in enumerate(findings):
        location = f"findings[{index}]"
        if not isinstance(rule, dict):
            errors.append(f"{location} must be a mapping")
            continue
        missing = sorted(FINDING_FIELDS - set(rule))
        extra = sorted(set(rule) - FINDING_FIELDS)
        if missing or extra:
            errors.append(f"{location} field mismatch; missing={missing}, extra={extra}")
        rule_id = rule.get("id")
        if not isinstance(rule_id, str) or not rule_id:
            errors.append(f"{location}.id must be non-empty")
        elif rule_id in seen_ids:
            errors.append(f"duplicate rule id: {rule_id}")
        else:
            seen_ids.add(rule_id)
        carrier = rule.get("carrier")
        if carrier not in markdown_carriers:
            errors.append(f"{location}.carrier is outside the Markdown inventory")
        line = rule.get("line")
        if not isinstance(line, int) or isinstance(line, bool) or line < 1:
            errors.append(f"{location}.line must be a positive integer")
        elif isinstance(carrier, str) and (root / carrier).is_file():
            line_count = len((root / carrier).read_text(encoding="utf-8").splitlines())
            if line > line_count:
                errors.append(f"{location}.line exceeds the carrier length")
        for field in ("summary", "trigger_event", "expected_failure"):
            if not isinstance(rule.get(field), str) or not rule[field].strip():
                errors.append(f"{location}.{field} must be non-empty")
        if rule.get("trigger_class") not in TRIGGER_CLASSES:
            errors.append(f"{location}.trigger_class is invalid")
        elif rule.get("trigger_class") != "internal-state":
            errors.append(f"{location}.trigger_class must be internal-state for a finding")
        if rule.get("frequency") not in FREQUENCIES:
            errors.append(f"{location}.frequency is invalid")
        if rule.get("salience") not in SALIENCE_LEVELS:
            errors.append(f"{location}.salience is invalid")
        if rule.get("enforcement") not in ENFORCEMENT_TYPES:
            errors.append(f"{location}.enforcement is invalid")
        disposition = rule.get("disposition")
        if disposition not in DISPOSITIONS:
            errors.append(f"{location}.disposition is invalid")
        if rule.get("ratification") not in RATIFICATION_STATES:
            errors.append(f"{location}.ratification is invalid")
        if rule.get("trigger_class") == "internal-state" and disposition not in {
            "converted-to-instrument",
            "external-detector",
            "known-weak",
        }:
            errors.append(f"{location}: internal-state rule requires a final disposition")

    counts = payload.get("counts")
    if not isinstance(counts, dict) or set(counts) != COUNT_FIELDS:
        errors.append(f"counts must contain exactly {sorted(COUNT_FIELDS)}")
    else:
        derived = _derived_counts(
            [rule for rule in findings if isinstance(rule, dict)],
            carriers_examined=sum(
                inspection == "inspected" for inspection in markdown_inspections.values()
            )
            if isinstance(markdown_inspections, dict)
            else 0,
            semantic_units_screened=_semantic_unit_count(root),
        )
        if counts != derived:
            errors.append(f"reported counts do not match ledger rows; expected={derived}")

    if require_complete:
        if status != "complete":
            errors.append("complete validation requires status: complete")
        if pending_inspections:
            errors.append(f"structured-file inspection remains pending: {sorted(pending_inspections)}")
        if pending_markdown_inspections:
            errors.append(
                "Markdown carrier inspection remains pending: "
                f"{sorted(pending_markdown_inspections)}"
            )
        for index, rule in enumerate(findings):
            if not isinstance(rule, dict):
                continue
            if rule.get("disposition") == "pending" or rule.get("ratification") != "ratified":
                errors.append(f"findings[{index}] remains unresolved")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-complete",
        action="store_true",
        help="fail unless every inspection and rule disposition is complete",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors = validate_rule_trigger_audit(root, require_complete=args.require_complete)
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("PASS: HEB-136 rule-trigger audit ledger validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
