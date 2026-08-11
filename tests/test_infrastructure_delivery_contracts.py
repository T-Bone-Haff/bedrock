from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate_infrastructure_delivery_contracts import validate_infrastructure_delivery_contracts


ROOT = Path(__file__).resolve().parents[1]


class InfrastructureDeliveryContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name) / "bedrock"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_repository_contracts_pass(self) -> None:
        self.assertEqual([], validate_infrastructure_delivery_contracts(self.root))

    def test_missing_registry_fails_closed(self) -> None:
        (self.root / "validation/infrastructure-delivery-contracts.yaml").unlink()
        errors = validate_infrastructure_delivery_contracts(self.root)
        self.assertTrue(any("registry is missing" in error for error in errors), errors)

    def test_stale_state_invalidates_apply(self) -> None:
        path = self.root / "tests/fixtures/infrastructure-delivery/valid/infrastructure-apply.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["apply"]["target"]["state_serial"] += 1
        path.write_text(json.dumps(value), encoding="utf-8")
        errors = validate_infrastructure_delivery_contracts(self.root)
        self.assertTrue(any("stale or mismatched plan" in error for error in errors), errors)

    def test_mutation_cancellation_is_rejected(self) -> None:
        path = self.root / "tests/fixtures/infrastructure-delivery/valid/delivery-profile.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["concurrency"]["mutation"] = "cancel_in_progress"
        path.write_text(json.dumps(value), encoding="utf-8")
        errors = validate_infrastructure_delivery_contracts(self.root)
        self.assertTrue(any("valid fixture rejected" in error for error in errors), errors)

    def test_apply_actor_requires_explicit_authority(self) -> None:
        path = self.root / "tests/fixtures/infrastructure-delivery/valid/infrastructure-apply.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["apply"]["actor"] = "unexpected-actor"
        path.write_text(json.dumps(value), encoding="utf-8")
        errors = validate_infrastructure_delivery_contracts(self.root)
        self.assertTrue(any("unauthorized apply actor" in error for error in errors), errors)

    def test_static_profile_requires_complete_header_set(self) -> None:
        path = self.root / "tests/fixtures/infrastructure-delivery/valid/delivery-profile.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["static_frontend"]["headers"].remove("Content-Security-Policy")
        path.write_text(json.dumps(value), encoding="utf-8")
        errors = validate_infrastructure_delivery_contracts(self.root)
        self.assertTrue(any("static frontend headers missing" in error for error in errors), errors)

    def test_ambiguous_release_is_rejected(self) -> None:
        path = self.root / "tests/fixtures/infrastructure-delivery/valid/application-release.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["event"]["association"] = "ambiguous"
        path.write_text(json.dumps(value), encoding="utf-8")
        errors = validate_infrastructure_delivery_contracts(self.root)
        self.assertTrue(any("ambiguous release association" in error for error in errors), errors)

    def test_old_absolutism_is_rejected(self) -> None:
        path = self.root / "plugins/bedrock/skills/infrastructure-code/SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nStateful means StatefulSet\n", encoding="utf-8")
        errors = validate_infrastructure_delivery_contracts(self.root)
        self.assertTrue(any("forbidden marker" in error for error in errors), errors)

    def test_mutable_workload_image_is_rejected(self) -> None:
        path = self.root / "tests/fixtures/infrastructure-delivery/valid/safe-workload.yaml"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("@sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef", ":latest"), encoding="utf-8")
        errors = validate_infrastructure_delivery_contracts(self.root)
        self.assertTrue(any("pinned by digest" in error for error in errors), errors)

    def test_malformed_registry_row_fails_loudly(self) -> None:
        import yaml
        path = self.root / "validation/infrastructure-delivery-contracts.yaml"
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
        value["fixtures"]["valid"].append({"schema": "application_release"})
        path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")
        errors = validate_infrastructure_delivery_contracts(self.root)
        self.assertTrue(any("fixture path" in error for error in errors), errors)

    def test_duplicate_behavior_case_fails_loudly(self) -> None:
        import yaml
        path = self.root / "tests/fixtures/infrastructure-delivery/behavior.yaml"
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
        value["cases"].append(dict(value["cases"][0]))
        path.write_text(yaml.safe_dump(value, sort_keys=False), encoding="utf-8")
        errors = validate_infrastructure_delivery_contracts(self.root)
        self.assertTrue(any("identifiers must be unique" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
