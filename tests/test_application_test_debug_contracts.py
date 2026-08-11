from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate_application_test_debug_contracts import (
    validate_application_test_debug_contracts,
)


ROOT = Path(__file__).resolve().parents[1]


class ApplicationTestDebugContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name) / "bedrock"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_repository_contracts_pass(self) -> None:
        self.assertEqual([], validate_application_test_debug_contracts(self.root))

    def test_missing_registry_fails_closed(self) -> None:
        (self.root / "validation/application-test-debug-contracts.yaml").unlink()
        errors = validate_application_test_debug_contracts(self.root)
        self.assertTrue(any("registry is missing" in error for error in errors), errors)

    def test_universal_async_rule_is_rejected(self) -> None:
        path = self.root / "plugins/bedrock/skills/application-code/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nEvery HTTP handler is `async def`\n", encoding="utf-8")
        errors = validate_application_test_debug_contracts(self.root)
        self.assertTrue(any("forbidden marker" in error for error in errors), errors)

    def test_unresolved_hypothesis_cannot_claim_root_cause(self) -> None:
        source = self.root / "tests/fixtures/application-test-debug/valid/diagnosis-inconclusive.json"
        value = json.loads(source.read_text(encoding="utf-8"))
        value["conclusion"] = {
            "status": "root_cause_identified",
            "confidence": "high",
            "statement": "guessed cause",
        }
        source.write_text(json.dumps(value), encoding="utf-8")
        errors = validate_application_test_debug_contracts(self.root)
        self.assertTrue(any("unsupported root cause" in error for error in errors), errors)

    def test_unauthorized_repair_action_is_rejected(self) -> None:
        source = self.root / "tests/fixtures/application-test-debug/valid/diagnosis-complete.json"
        value = json.loads(source.read_text(encoding="utf-8"))
        value["repair"] = {"authorized": False, "action": "mutate production"}
        source.write_text(json.dumps(value), encoding="utf-8")
        errors = validate_application_test_debug_contracts(self.root)
        self.assertTrue(any("valid fixture rejected" in error for error in errors), errors)

    def test_invalid_evidence_timestamp_is_rejected(self) -> None:
        source = self.root / "tests/fixtures/application-test-debug/valid/diagnosis-complete.json"
        value = json.loads(source.read_text(encoding="utf-8"))
        value["evidence"][0]["captured_at"] = "not-a-timestamp"
        source.write_text(json.dumps(value), encoding="utf-8")
        errors = validate_application_test_debug_contracts(self.root)
        self.assertTrue(any("valid fixture rejected" in error for error in errors), errors)

    def test_malformed_registry_row_fails_loudly(self) -> None:
        import yaml

        registry = self.root / "validation/application-test-debug-contracts.yaml"
        value = yaml.safe_load(registry.read_text(encoding="utf-8"))
        value["fixtures"]["valid"].append({"schema": "debug"})
        registry.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")
        errors = validate_application_test_debug_contracts(self.root)
        self.assertTrue(any("fixture path" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
