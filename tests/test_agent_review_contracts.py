"""Regression tests for HEB-116 agent/review contracts."""

from __future__ import annotations

from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate_agent_review_contracts import _balanced_json_candidates, validate_agent_review_contracts


ROOT = Path(__file__).resolve().parents[1]


class AgentReviewContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name) / "bedrock"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_repository_contracts_pass(self) -> None:
        self.assertEqual([], validate_agent_review_contracts(self.root))

    def test_missing_registry_fails_closed(self) -> None:
        (self.root / "validation/agent-review-contracts.yaml").unlink()
        self.assertTrue(any("registry is missing" in item for item in validate_agent_review_contracts(self.root)))

    def test_salvage_enumerates_ambiguity(self) -> None:
        self.assertEqual(2, len(_balanced_json_candidates('before {"a": 1} between {"b": 2} after')))

    def test_nested_object_is_one_candidate(self) -> None:
        self.assertEqual(1, len(_balanced_json_candidates('before {"a": {"b": 2}} after')))

    def test_low_confidence_resolvable_is_rejected(self) -> None:
        path = self.root / "tests/fixtures/agent-review-contracts/valid/arbitration.json"
        text = path.read_text(encoding="utf-8").replace('"confidence": "high"', '"confidence": "low"')
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("low-confidence resolvable" in item for item in validate_agent_review_contracts(self.root)))


if __name__ == "__main__":
    unittest.main()
