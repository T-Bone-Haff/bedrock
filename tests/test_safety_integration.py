"""Runtime evidence for the HEB-110 container and Terraform-state repairs."""

from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import unittest
from urllib.request import urlopen
import uuid


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SAFETY_FIXTURES = REPOSITORY_ROOT / "tests" / "fixtures" / "safety"


def _command_available(command: str, probe: list[str]) -> bool:
    executable = shutil.which(command)
    if executable is None:
        return False
    return subprocess.run(
        [executable, *probe],
        capture_output=True,
        check=False,
        text=True,
    ).returncode == 0


class ContainerSafetyIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        if _command_available("docker", ["info"]):
            return
        if os.environ.get("HEB110_REQUIRE_DOCKER") == "1":
            self.fail("Docker daemon is required for HEB-110 CI evidence")
        self.skipTest("Docker daemon is unavailable")

    def test_runtime_environment_image_starts_and_serves_health(self) -> None:
        # Arrange
        tag = f"heb-110-safety:{uuid.uuid4().hex}"
        name = f"heb-110-safety-{uuid.uuid4().hex}"
        fixture = SAFETY_FIXTURES / "python-service"
        subprocess.run(["docker", "build", "--tag", tag, str(fixture)], check=True)
        container_id = subprocess.run(
            ["docker", "run", "--detach", "--name", name, "--publish", "127.0.0.1::8080", tag],
            capture_output=True,
            check=True,
            text=True,
        ).stdout.strip()
        self.addCleanup(
            subprocess.run,
            ["docker", "image", "rm", "--force", tag],
            capture_output=True,
            check=False,
            text=True,
        )
        self.addCleanup(
            subprocess.run,
            ["docker", "rm", "--force", container_id],
            capture_output=True,
            check=False,
            text=True,
        )
        port_output = subprocess.run(
            ["docker", "port", container_id, "8080/tcp"],
            capture_output=True,
            check=True,
            text=True,
        ).stdout.strip()
        port = int(port_output.rsplit(":", 1)[1])

        # Act
        response_body = None
        status = None
        for _ in range(30):
            try:
                with urlopen(f"http://127.0.0.1:{port}/health", timeout=1) as response:
                    response_body = response.read()
                    status = response.status
                break
            except OSError:
                time.sleep(0.2)

        # Assert
        self.assertEqual(200, status)
        self.assertEqual(b"ok", response_body)


class TerraformStateIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        if _command_available("terraform", ["version"]):
            return
        if os.environ.get("HEB110_REQUIRE_TERRAFORM") == "1":
            self.fail("Terraform is required for HEB-110 CI evidence")
        self.skipTest("Terraform is unavailable")

    def _render_state(self, fixture_name: str, sentinel: str) -> str:
        source = SAFETY_FIXTURES / "terraform-state" / fixture_name
        with tempfile.TemporaryDirectory() as temporary:
            worktree = Path(temporary) / fixture_name
            shutil.copytree(source, worktree)
            environment = {
                "CHECKPOINT_DISABLE": "1",
                "TF_IN_AUTOMATION": "1",
            }
            command_environment = os.environ | environment
            subprocess.run(
                ["terraform", "init", "-backend=false", "-input=false"],
                cwd=worktree,
                env=command_environment,
                capture_output=True,
                check=True,
                text=True,
            )
            arguments = [
                "terraform",
                "apply",
                "-auto-approve",
                "-input=false",
            ]
            if fixture_name == "unsafe":
                arguments.append(f"-var=secret_payload={sentinel}")
            else:
                arguments.extend(
                    [
                        f"-var=runtime_secret_payload={sentinel}",
                        "-var=secret_resource_name=projects/example/secrets/runtime-secret",
                    ]
                )
            subprocess.run(
                arguments,
                cwd=worktree,
                env=command_environment,
                capture_output=True,
                check=True,
                text=True,
            )
            state = subprocess.run(
                ["terraform", "show", "-json"],
                cwd=worktree,
                env=command_environment,
                capture_output=True,
                check=True,
                text=True,
            ).stdout
            json.loads(state)
            return state

    def test_sensitive_value_materialized_by_terraform_is_present_in_state(self) -> None:
        # Arrange
        sentinel = f"unsafe-{uuid.uuid4().hex}"

        # Act
        state = self._render_state("unsafe", sentinel)

        # Assert
        self.assertIn(sentinel, state)

    def test_runtime_only_secret_value_is_absent_from_state(self) -> None:
        # Arrange
        sentinel = f"safe-{uuid.uuid4().hex}"

        # Act
        state = self._render_state("safe", sentinel)

        # Assert
        self.assertNotIn(sentinel, state)


if __name__ == "__main__":
    unittest.main()
