from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml

from scripts.validate_plugin import EXPECTED_SKILLS, run_host_validator, validate_repository


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self._write_valid_repository()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _write_valid_repository(self) -> None:
        plugin = self.root / "plugins" / "bedrock"
        (plugin / ".claude-plugin").mkdir(parents=True)
        (self.root / ".claude-plugin").mkdir()
        (self.root / "tests" / "fixtures").mkdir(parents=True)
        description = "Author the named work. Use for the matching task. Do not use for unrelated work."
        for name in EXPECTED_SKILLS:
            skill_dir = plugin / "skills" / name
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                f'---\nname: {name}\ndescription: "{description}"\n---\n\n# {name}\n',
                encoding="utf-8",
            )
        plugin_description = "Bedrock test plugin"
        (plugin / ".claude-plugin" / "plugin.json").write_text(
            json.dumps({"name": "bedrock", "description": plugin_description, "version": "1.0.0"}),
            encoding="utf-8",
        )
        (self.root / ".claude-plugin" / "marketplace.json").write_text(
            json.dumps(
                {
                    "plugins": [
                        {
                            "name": "bedrock",
                            "description": plugin_description,
                            "source": "./plugins/bedrock",
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        cases = []
        for name in EXPECTED_SKILLS:
            cases.extend(
                [
                    {
                        "id": f"{name}-positive",
                        "kind": "positive",
                        "surface": "portable-core",
                        "prompt": f"Use {name}",
                        "expected": name,
                        "excluded": [],
                    },
                    {
                        "id": f"{name}-negative",
                        "kind": "negative",
                        "surface": "portable-core",
                        "prompt": f"Do not use {name}",
                        "expected": None,
                        "excluded": [name],
                    },
                ]
            )
        (self.root / "tests" / "fixtures" / "routing.yaml").write_text(
            yaml.safe_dump({"schema_version": 1, "cases": cases}, sort_keys=False),
            encoding="utf-8",
        )

    def assert_has_error(self, needle: str) -> None:
        errors, _ = validate_repository(self.root, run_host_cli=False)
        self.assertTrue(any(needle in error for error in errors), errors)

    def test_valid_fixture_passes(self) -> None:
        errors, report = validate_repository(self.root, run_host_cli=False)
        self.assertEqual([], errors)
        self.assertEqual(13, report["skill_count"])

    def test_rejects_malformed_frontmatter(self) -> None:
        path = self.root / "plugins" / "bedrock" / "skills" / "agent-code" / "SKILL.md"
        path.write_text("---\nname: agent-code\ndescription: bad: yaml\n---\n", encoding="utf-8")
        self.assert_has_error("invalid YAML frontmatter")

    def test_rejects_overlong_description(self) -> None:
        path = self.root / "plugins" / "bedrock" / "skills" / "agent-code" / "SKILL.md"
        path.write_text(
            f'---\nname: agent-code\ndescription: "Use this. Do not use that. {"x" * 1024}"\n---\n',
            encoding="utf-8",
        )
        self.assert_has_error("exceeds 1024")

    def test_rejects_duplicate_name(self) -> None:
        path = self.root / "plugins" / "bedrock" / "skills" / "testing" / "SKILL.md"
        path.write_text(
            '---\nname: agent-code\ndescription: "Use this. Do not use that."\n---\n',
            encoding="utf-8",
        )
        self.assert_has_error("duplicate skill name")

    def test_rejects_manifest_description_drift(self) -> None:
        path = self.root / ".claude-plugin" / "marketplace.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["plugins"][0]["description"] = "drifted"
        path.write_text(json.dumps(payload), encoding="utf-8")
        self.assert_has_error("description must equal plugin.json description")

    def test_rejects_missing_negative_route(self) -> None:
        path = self.root / "tests" / "fixtures" / "routing.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["cases"] = [case for case in payload["cases"] if case["id"] != "testing-negative"]
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        self.assert_has_error("missing negative routing case excluding testing")

    def test_rejects_non_mapping_route(self) -> None:
        path = self.root / "tests" / "fixtures" / "routing.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["cases"].append("not-a-case")
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        self.assert_has_error("case must be a mapping")

    def test_rejects_unknown_overlap_alternate(self) -> None:
        path = self.root / "tests" / "fixtures" / "routing.yaml"
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        payload["cases"].append(
            {
                "id": "bad-overlap",
                "kind": "overlap",
                "surface": "portable-core",
                "prompt": "Ambiguous task",
                "expected": "testing",
                "allowed_alternates": ["missing-skill"],
                "excluded": [],
            }
        )
        path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
        self.assert_has_error("allowed_alternates must contain only known skill names")
@unittest.skipUnless(shutil.which("claude"), "Claude Code CLI is not installed")
class StrictHostValidatorIntegrationTests(unittest.TestCase):
    def test_seeded_invalid_frontmatter_fails_strict_host_validation(self) -> None:
        repository_root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as temporary:
            fixture_root = Path(temporary)
            destination = fixture_root / "plugins" / "bedrock"
            destination.parent.mkdir(parents=True)
            shutil.copytree(repository_root / "plugins" / "bedrock", destination)
            skill = destination / "skills" / "agent-code" / "SKILL.md"
            text = skill.read_text(encoding="utf-8")
            skill.write_text(text.replace('description: "', "description: invalid: ", 1), encoding="utf-8")
            errors: list[str] = []
            run_host_validator(fixture_root, errors)
            self.assertTrue(errors, "seeded invalid frontmatter unexpectedly passed strict host validation")


if __name__ == "__main__":
    unittest.main()
