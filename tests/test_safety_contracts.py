"""Deterministic regression tests for the HEB-110 safety overlay."""

from __future__ import annotations

from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate_safety import route_safety_case, validate_safety_contracts


class SafetyContractTests(unittest.TestCase):
    def test_repository_satisfies_safety_contracts(self) -> None:
        # Arrange
        repository_root = Path(__file__).resolve().parents[1]

        # Act
        errors = validate_safety_contracts(repository_root)

        # Assert
        self.assertEqual([], errors)

    def test_cosmetic_finding_never_blocks_convergence(self) -> None:
        # Arrange
        case = {
            "severity": "COSMETIC",
            "classification": "resolvable",
            "status": "open",
        }

        # Act
        result = route_safety_case(case)

        # Assert
        self.assertEqual("CONVERGED", result)

    def test_cosmetic_decision_bearing_combination_is_invalid(self) -> None:
        # Arrange
        case = {
            "severity": "COSMETIC",
            "classification": "decision-bearing",
            "status": "open",
        }

        # Act
        result = route_safety_case(case)

        # Assert
        self.assertEqual("INVALID", result)

    def test_material_decision_bearing_finding_halts(self) -> None:
        # Arrange
        case = {
            "severity": "MATERIAL",
            "classification": "decision-bearing",
            "status": "open",
        }

        # Act
        result = route_safety_case(case)

        # Assert
        self.assertEqual("HALT_DECISION", result)


class SafetyValidatorNegativeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        repository_root = Path(__file__).resolve().parents[1]
        skills_source = repository_root / "plugins" / "bedrock" / "skills"
        fixtures_source = repository_root / "tests" / "fixtures" / "safety"
        shutil.copytree(skills_source, self.root / "plugins" / "bedrock" / "skills")
        shutil.copytree(fixtures_source, self.root / "tests" / "fixtures" / "safety")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def assert_has_error(self, needle: str) -> None:
        # Act
        errors = validate_safety_contracts(self.root)

        # Assert
        self.assertTrue(any(needle in error for error in errors), errors)

    def test_unpinned_action_reference_fails(self) -> None:
        # Arrange
        path = (
            self.root
            / "plugins/bedrock/skills/infrastructure-code/reference/05-delivery-pipeline.md"
        )
        text = path.read_text(encoding="utf-8")
        path.write_text(
            text.replace("7c6bc770dae815cd3e89ee6cdf493a5fab2cc093", "v3"),
            encoding="utf-8",
        )

        self.assert_has_error("must use a full commit SHA")

    def test_python_minor_site_packages_path_fails(self) -> None:
        # Arrange
        path = (
            self.root
            / "plugins/bedrock/skills/application-code/reference/01-code-structure.md"
        )
        text = path.read_text(encoding="utf-8")
        path.write_text(
            text.replace(
                "COPY --from=builder /opt/venv /opt/venv",
                "COPY --from=builder /usr/local/lib/python3.11/site-packages "
                "/usr/local/lib/python3.11/site-packages",
            ),
            encoding="utf-8",
        )

        self.assert_has_error("/usr/local/lib/python3.11/site-packages")

    def test_secret_state_denial_fails(self) -> None:
        # Arrange
        path = self.root / "plugins/bedrock/skills/infrastructure-code/SKILL.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text + "\nNo secrets in configuration or state.\n", encoding="utf-8")

        self.assert_has_error("No secrets in configuration or state")

    def test_pull_request_push_fails(self) -> None:
        # Arrange
        path = self.root / "tests/fixtures/safety/pr-image-build.yml"
        text = path.read_text(encoding="utf-8")
        path.write_text(text + "\n      - run: docker push example/image\n", encoding="utf-8")

        self.assert_has_error("docker push")

    def test_malformed_workflow_events_fail_cleanly(self) -> None:
        # Arrange
        path = self.root / "tests/fixtures/safety/pr-image-build.yml"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace('"on":\n  pull_request:', '"on":'), encoding="utf-8")

        self.assert_has_error("must run for pull_request events")

    def test_non_string_manifest_identifier_fails_cleanly(self) -> None:
        # Arrange
        path = self.root / "tests/fixtures/safety/manifest.yaml"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("- id: APP-002", "- id: [APP-002]"), encoding="utf-8")

        self.assert_has_error("id must be a string")

    def test_cosmetic_decision_halt_guidance_fails(self) -> None:
        # Arrange
        path = self.root / "plugins/bedrock/skills/design-review-loop/SKILL.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text + "\nA decision halts, even a COSMETIC one.\n", encoding="utf-8")

        self.assert_has_error("even a COSMETIC one")


if __name__ == "__main__":
    unittest.main()
