"""Regression tests for HEB-116 agent/review contracts."""

from __future__ import annotations

from pathlib import Path
import shutil
import tempfile
import unittest

import yaml

from scripts.validate_agent_review_contracts import (
    _balanced_json_candidates,
    evaluate_runner_profile_case,
    validate_agent_review_contracts,
)


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

    def test_forbidden_product_specific_profile_path_fails_closed(self) -> None:
        path = (
            self.root
            / "plugins/bedrock/skills/design-review-loop/reference/haffey-sofia-profile.md"
        )
        path.write_text("legacy product profile\n", encoding="utf-8")
        errors = validate_agent_review_contracts(self.root)
        self.assertTrue(any("forbidden path remains" in item for item in errors), errors)

    def test_runner_profile_case_expectations_are_enforced(self) -> None:
        path = self.root / "validation/agent-review-contracts.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["runner_profile_cases"][0]["expected"] = "stop-unavailable"
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        errors = validate_agent_review_contracts(self.root)
        self.assertTrue(any("runner profile case" in item for item in errors), errors)

    def test_runner_backed_claim_requires_replayable_binding_and_invocation(self) -> None:
        complete = {
            "profile": "runner-backed",
            "product_binding_id": "product-review-workflow",
            "product_binding_version": "1.0.0",
            "runner_id": "product-review-runner",
            "runner_version": "2.1.0",
            "schemas_compatible": True,
            "invocation": "product-review run --profile convergence",
            "fresh_gate_evidence": True,
        }
        self.assertEqual("runner-backed-claim-permitted", evaluate_runner_profile_case(complete))
        for field in ("product_binding_id", "product_binding_version", "runner_id", "runner_version", "invocation"):
            with self.subTest(field=field):
                incomplete = dict(complete)
                incomplete.pop(field)
                self.assertEqual("stop-unavailable", evaluate_runner_profile_case(incomplete))


if __name__ == "__main__":
    unittest.main()
