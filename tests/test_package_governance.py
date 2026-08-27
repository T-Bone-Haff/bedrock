from __future__ import annotations

import json
import hashlib
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import yaml

from scripts.validate_package_governance import validate_package_governance


class PackageGovernanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        source = Path(__file__).resolve().parents[1]
        shutil.copytree(
            source,
            self.root,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns(".git", "__pycache__", "node_modules"),
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def assert_has_error(self, needle: str) -> None:
        errors = validate_package_governance(self.root)
        self.assertTrue(any(needle in error for error in errors), errors)

    def write_package_identity_carriers(self) -> list[Path]:
        manifest_path = self.root / "plugins/bedrock/.claude-plugin/plugin.json"
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        registry = yaml.safe_load(
            (self.root / "plugins/bedrock/governance/registry.yaml").read_text(encoding="utf-8")
        )
        payload = {
            "schema_version": 1,
            "classification": "generated-carrier",
            "package": manifest["name"],
            "manifest_version": manifest["version"],
            "version_authority": ".claude-plugin/plugin.json#/version",
            "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
            "generator": {
                "id": "scripts/sync_package_identity.py",
                "version": "1.0.0",
            },
            "contracts": {
                "claude_adapter": registry["contracts"]["claude_adapter"],
            },
        }
        encoded = json.dumps(payload, indent=2) + "\n"
        paths = sorted((self.root / "plugins/bedrock/skills").glob("*/SKILL.md"))
        carrier_paths = [path.with_name("PACKAGE_IDENTITY.json") for path in paths]
        for path in carrier_paths:
            path.write_text(encoded, encoding="utf-8")
        return carrier_paths

    def test_repository_package_governance_passes(self) -> None:
        self.assertEqual([], validate_package_governance(self.root))

    def test_rejects_manifest_metadata_drift(self) -> None:
        path = self.root / "plugins/bedrock/.claude-plugin/plugin.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["license"] = "UNKNOWN"
        path.write_text(json.dumps(payload), encoding="utf-8")
        self.assert_has_error("license must equal 'MIT'")

    def test_rejects_marketplace_authority_drift(self) -> None:
        path = self.root / ".claude-plugin/marketplace.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["plugins"][0]["version"] = "99.0.0"
        path.write_text(json.dumps(payload), encoding="utf-8")
        self.assert_has_error("must not duplicate the manifest version authority")

    def test_rejects_license_carrier_drift(self) -> None:
        path = self.root / "plugins/bedrock/LICENSE"
        path.write_text(path.read_text(encoding="utf-8") + "\ndrift\n", encoding="utf-8")
        self.assert_has_error("license must match repository license exactly")

    def test_rejects_orphaned_skill_lifecycle(self) -> None:
        path = self.root / "plugins/bedrock/governance/registry.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["skills"][0]["owner"] = ""
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        self.assert_has_error("owner is required")

    def test_rejects_retired_skill_without_migration(self) -> None:
        path = self.root / "plugins/bedrock/governance/registry.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["skills"][0]["status"] = "retired"
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        self.assert_has_error("non-active skill requires migration treatment")

    def test_rejects_incomplete_consumer_enumeration(self) -> None:
        path = self.root / "plugins/bedrock/governance/registry.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["consumer_surfaces"] = payload["consumer_surfaces"][:1]
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        self.assert_has_error("must contain claude-ai and claude-code exactly")

    def test_rejects_vocabulary_schema_drift(self) -> None:
        path = self.root / "plugins/bedrock/governance/vocabulary.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["gate_status"] = ["passed", "failed"]
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        self.assert_has_error("gate_status must match the governing schema enum exactly")

    def test_rejects_uncontrolled_duplicate_authority(self) -> None:
        path = self.root / "plugins/bedrock/governance/authority-inventory.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["concepts"][0]["repetitions"][0]["classification"] = "defect"
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        self.assert_has_error("every repetition requires an allowed classification and drift control")

    def test_rejects_stale_context_measurement(self) -> None:
        path = self.root / "docs/evidence/heb-118/context-budget.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["measurement"]["catalog_description_characters"] = 1
        path.write_text(json.dumps(payload), encoding="utf-8")
        self.assert_has_error("catalog description measurement is stale")

    def test_rejects_missing_package_finding(self) -> None:
        path = self.root / "docs/evidence/heb-118/manifest.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["finding_reconciliation"] = payload["finding_reconciliation"][:-1]
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        self.assert_has_error("must contain PKG-001 through PKG-039 exactly once")

    def test_rejects_missing_governance_link(self) -> None:
        path = self.root / "plugins/bedrock/governance/QUICKSTART.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[missing](missing.md)\n", encoding="utf-8")
        self.assert_has_error("package-governance link target does not exist")

    def test_rejects_missing_package_identity_carrier(self) -> None:
        carrier_paths = self.write_package_identity_carriers()
        carrier_paths[0].unlink()
        self.assert_has_error("package identity carrier is missing")

    def test_rejects_malformed_package_identity_carrier(self) -> None:
        carrier_paths = self.write_package_identity_carriers()
        carrier_paths[0].write_text("{not-json}\n", encoding="utf-8")
        self.assert_has_error("package identity carrier is not valid JSON")

    def test_rejects_stale_package_identity_version(self) -> None:
        carrier_paths = self.write_package_identity_carriers()
        payload = json.loads(carrier_paths[0].read_text(encoding="utf-8"))
        payload["manifest_version"] = "0.0.0"
        carrier_paths[0].write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        self.assert_has_error("package identity carrier does not match the manifest authority")

    def test_rejects_stale_package_identity_digest(self) -> None:
        carrier_paths = self.write_package_identity_carriers()
        payload = json.loads(carrier_paths[0].read_text(encoding="utf-8"))
        payload["manifest_sha256"] = "0" * 64
        carrier_paths[0].write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        self.assert_has_error("package identity carrier does not match the manifest authority")

    def test_rejects_divergent_package_identity_copy(self) -> None:
        carrier_paths = self.write_package_identity_carriers()
        carrier_paths[0].write_text(
            carrier_paths[0].read_text(encoding="utf-8").replace("  \"package\"", "    \"package\""),
            encoding="utf-8",
        )
        self.assert_has_error("package identity carriers must be byte-identical")

    def test_rejects_package_identity_contract_drift(self) -> None:
        mutations = {
            "package": "not-bedrock",
            "version_authority": "wrong#/version",
            "generator.id": "wrong-generator",
            "generator.version": "9.9.9",
            "contracts.claude_adapter": "9.9.9",
        }
        for field, replacement in mutations.items():
            with self.subTest(field=field):
                carrier_paths = self.write_package_identity_carriers()
                payload = json.loads(carrier_paths[0].read_text(encoding="utf-8"))
                target = payload
                parts = field.split(".")
                for part in parts[:-1]:
                    target = target[part]
                target[parts[-1]] = replacement
                carrier_paths[0].write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
                self.assert_has_error("package identity carrier does not match the manifest authority")

    def test_release_mode_fails_closed_before_acceptance(self) -> None:
        errors = validate_package_governance(self.root, release=True)
        self.assertTrue(any("requires --release-evidence" in error for error in errors), errors)

    def test_release_mode_accepts_external_evidence_after_immutable_tag(self) -> None:
        manifest_path = self.root / "plugins/bedrock/.claude-plugin/plugin.json"
        manifest_version = json.loads(manifest_path.read_text(encoding="utf-8"))["version"]
        release_tag = f"v{manifest_version}"
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.name", "Bedrock Test"], cwd=self.root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        subprocess.run(["git", "commit", "-qm", "candidate"], cwd=self.root, check=True)
        source_commit = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=self.root, check=True, capture_output=True, text=True
        ).stdout.strip()
        subprocess.run(["git", "tag", "-am", "release", release_tag], cwd=self.root, check=True)
        manifest_digest = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
        gate_ids = (
            "deterministic",
            "strict-host",
            "isolated-install",
            "routing",
            "review",
            "migration",
            "cold-acceptance",
            "github-release",
        )
        evidence = {
            "schema_version": 1,
            "manifest_version": manifest_version,
            "source_commit": source_commit,
            "manifest_sha256": manifest_digest,
            "findings": {"assigned": 39, "closed": 39, "evidence": ["HEB-118"]},
            "changed_surfaces": ["package-governance"],
            "migration": {"classification": "compatible", "rationale": "Additive", "notes": None},
            "gates": [{"id": gate_id, "status": "passed", "evidence": gate_id} for gate_id in gate_ids],
            "limitations": [],
            "decision": {
                "status": "proceed",
                "authority": "operator",
                "recorded_at": "2026-08-11T21:00:00Z",
            },
        }
        rollout = {
            "schema_version": 1,
            "manifest_version": manifest_version,
            "release_tag": release_tag,
            "source_commit": source_commit,
            "surfaces": [
                {
                    "id": surface,
                    "expected_action": "verify",
                    "expected_identity": f"{manifest_version} and 13 skills",
                    "status": "verified",
                    "evidence": surface,
                    "owner": "operator",
                    "waiver": None,
                }
                for surface in ("claude-ai", "claude-code")
            ],
            "rollback": {"triggered": False, "last_accepted_tag": None, "evidence": None},
            "status": "complete",
        }
        evidence_path = self.root / "release-evidence.yaml"
        rollout_path = self.root / "rollout-ledger.yaml"
        evidence_path.write_text(yaml.safe_dump(evidence, sort_keys=False), encoding="utf-8")
        rollout_path.write_text(yaml.safe_dump(rollout, sort_keys=False), encoding="utf-8")
        self.assertEqual(
            [],
            validate_package_governance(
                self.root,
                release=True,
                release_evidence=evidence_path,
                rollout_ledger=rollout_path,
            ),
        )

    def test_seeded_governance_defect_manifest_names_existing_tests(self) -> None:
        payload = yaml.safe_load(
            (self.root / "tests/fixtures/package-governance/manifest.yaml").read_text(encoding="utf-8")
        )
        declared = {row["test"] for row in payload["defects"]}
        available = {name for name in dir(type(self)) if name.startswith("test_")}
        self.assertEqual(set(), declared - available)


if __name__ == "__main__":
    unittest.main()
