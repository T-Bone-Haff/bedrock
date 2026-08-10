"""Regression tests for the HEB-117 authoring and review contracts."""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml

from scripts.validate_authoring_contracts import evaluate_behavior_case, validate_authoring_contracts


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


class AuthoringContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name) / "bedrock"
        shutil.copytree(REPOSITORY_ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def assert_error(self, expected: str) -> None:
        self.assertTrue(any(expected in error for error in validate_authoring_contracts(self.root)))

    def test_repository_contracts_pass(self) -> None:
        self.assertEqual([], validate_authoring_contracts(self.root))

    def test_missing_registry_fails_closed(self) -> None:
        (self.root / "validation/authoring-contracts.yaml").unlink()
        self.assert_error("required authoring-contract registry is missing")

    def test_missing_interaction_field_fails(self) -> None:
        path = self.root / "validation/authoring-contracts.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        del payload["skills"]["code-review"]["failure_behavior"]
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        self.assert_error("field mismatch")

    def test_high_assurance_relay_without_authorization_fails(self) -> None:
        path = self.root / "tests/fixtures/authoring-contracts/valid/relay.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        del payload["authorization"]
        path.write_text(json.dumps(payload), encoding="utf-8")
        self.assert_error("valid fixture or schema failed")

    def test_provisional_relation_without_owner_fails(self) -> None:
        path = self.root / "tests/fixtures/authoring-contracts/valid/relations.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        del payload["relations"][0]["owner"]
        path.write_text(json.dumps(payload), encoding="utf-8")
        self.assert_error("valid fixture or schema failed")

    def test_review_with_blocker_cannot_approve(self) -> None:
        valid = self.root / "tests/fixtures/authoring-contracts/valid/review.json"
        invalid = self.root / "tests/fixtures/authoring-contracts/invalid/review.json"
        valid.write_bytes(invalid.read_bytes())
        self.assert_error("approves with an unresolved blocking finding")

    def test_construct_template_size_is_bounded(self) -> None:
        path = self.root / "plugins/bedrock/skills/author-construct-spec/templates/construct-spec-template.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n" * 181, encoding="utf-8")
        self.assert_error("must not exceed 180 lines")

    def test_behavior_fixture_cases_match_terminal_contracts(self) -> None:
        payload = yaml.safe_load(
            (self.root / "tests/fixtures/authoring-contracts/behavior.yaml").read_text(encoding="utf-8")
        )
        for case in payload["cases"]:
            with self.subTest(case=case["id"]):
                self.assertEqual(case["expected"], evaluate_behavior_case(case))


if __name__ == "__main__":
    unittest.main()
