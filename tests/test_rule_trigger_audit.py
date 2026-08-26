"""Regression tests for the HEB-136 rule-trigger audit instrument."""

from __future__ import annotations

from pathlib import Path
import shutil
import tempfile
import unittest

import yaml

from scripts.validate_rule_trigger_audit import _semantic_unit_count, validate_rule_trigger_audit


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class RuleTriggerAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name) / "bedrock"
        shutil.copytree(REPOSITORY_ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.ledger_path = self.root / "docs/evidence/heb-136/rule-trigger-audit.yaml"

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def load_ledger(self) -> dict:
        return yaml.safe_load(self.ledger_path.read_text(encoding="utf-8"))

    def write_ledger(self, payload: dict) -> None:
        self.ledger_path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")

    def assert_error(self, expected: str, *, require_complete: bool = False) -> None:
        errors = validate_rule_trigger_audit(self.root, require_complete=require_complete)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_inventory_ledger_matches_live_populations(self) -> None:
        self.assertEqual([], validate_rule_trigger_audit(self.root))

    def test_missing_ledger_fails_closed(self) -> None:
        self.ledger_path.unlink()
        self.assert_error("cannot read audit ledger")

    def test_missing_markdown_carrier_fails(self) -> None:
        payload = self.load_ledger()
        payload["scope"]["markdown_carriers"].pop()
        self.write_ledger(payload)
        self.assert_error("Markdown carrier population mismatch")

    def test_unlisted_live_structured_file_fails(self) -> None:
        extra = self.root / "plugins/bedrock/skills/testing/reference/new.schema.json"
        extra.write_text("{}\n", encoding="utf-8")
        self.assert_error("structured-file population mismatch")

    def test_internal_state_rule_without_disposition_fails(self) -> None:
        payload = self.load_ledger()
        payload["findings"] = [
            {
                "id": "testing-001",
                "carrier": "plugins/bedrock/skills/testing/SKILL.md",
                "line": 1,
                "summary": "Remember the current authority.",
                "trigger_event": "Actor notices it is relying on memory.",
                "trigger_class": "internal-state",
                "frequency": "high",
                "salience": "low",
                "enforcement": "none",
                "disposition": "pending",
                "expected_failure": "Stale authority is treated as current.",
                "ratification": "pending",
            }
        ]
        self.write_ledger(payload)
        self.assert_error("internal-state rule requires a final disposition")

    def test_complete_gate_rejects_pending_inspections(self) -> None:
        payload = self.load_ledger()
        payload["scope"]["structured_files"][0]["inspection"] = "pending"
        self.write_ledger(payload)
        self.assert_error("structured-file inspection remains pending", require_complete=True)

    def test_complete_gate_rejects_pending_markdown_inspections(self) -> None:
        payload = self.load_ledger()
        first_path = next(iter(payload["scope"]["markdown_inspections"]))
        payload["scope"]["markdown_inspections"][first_path] = "pending"
        self.write_ledger(payload)
        self.assert_error("Markdown carrier inspection remains pending", require_complete=True)

    def test_workflow_event_cannot_be_recorded_as_internal_state_finding(self) -> None:
        payload = self.load_ledger()
        payload["findings"] = [
            {
                "id": "testing-001",
                "carrier": "plugins/bedrock/skills/testing/SKILL.md",
                "line": 1,
                "summary": "Run the named test at the verification gate.",
                "trigger_event": "Verification gate is reached.",
                "trigger_class": "workflow-event",
                "frequency": "low",
                "salience": "high",
                "enforcement": "discipline",
                "disposition": "workflow-discipline",
                "expected_failure": "The named test is skipped.",
                "ratification": "ratified",
            }
        ]
        self.write_ledger(payload)
        self.assert_error("trigger_class must be internal-state for a finding")

    def test_reported_count_drift_fails(self) -> None:
        payload = self.load_ledger()
        payload["counts"]["semantic_units_screened"] += 1
        self.write_ledger(payload)
        self.assert_error("reported counts do not match ledger rows")

    def test_multi_digit_ordered_items_are_individual_screen_units(self) -> None:
        isolated_root = Path(self.temporary_directory.name) / "unit-count"
        skill_root = isolated_root / "plugins/bedrock/skills/example"
        skill_root.mkdir(parents=True)
        (skill_root / "SKILL.md").write_text(
            "9. Ninth\n10. Tenth\n11. Eleventh\n",
            encoding="utf-8",
        )
        self.assertEqual(3, _semantic_unit_count(isolated_root))

    def test_complete_empty_finding_ledger_passes(self) -> None:
        self.assertEqual([], validate_rule_trigger_audit(self.root, require_complete=True))


if __name__ == "__main__":
    unittest.main()
