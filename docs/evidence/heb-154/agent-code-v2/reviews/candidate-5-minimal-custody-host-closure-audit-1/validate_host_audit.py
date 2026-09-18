#!/usr/bin/env python3
"""Validate the bounded Candidate-5 host closure-audit result."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
from typing import Any


CONSTRUCT_SHA = "464b52c4f05959796b2e2819430f88c52dbd9055d3210f167f8693ccf24efeca"
EXPECTED = [
    (
        "a483dab16a88cee4e058406b9c7dc0f55afc2748bf774bfb68dd241918c981f0",
        "HCA-1",
        ["HCA1-POPULATION", "HCA1-CAPTURE", "HCA1-CONSUME", "HCA1-FAIL", "HCA1-MARKER"],
    ),
    (
        "ca41c23463c9e226eaa315edc4f970be81c8a898479d99e6e7a55f15f94bb4a1",
        "HCA-2",
        ["HCA2-LOGGING", "HCA2-SILENCE", "HCA2-REBIND", "HCA2-PROVE", "HCA2-FAIL"],
    ),
]
SHA256 = re.compile(r"^[0-9a-f]{64}$")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def exact_keys(value: dict[str, Any], expected: set[str], locus: str) -> None:
    require(set(value) == expected, f"{locus}: keys {sorted(value)} != {sorted(expected)}")


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_host_audit.py AUDIT_RESULT", file=sys.stderr)
        return 2
    try:
        value = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        require(isinstance(value, dict), "root must be object")
        exact_keys(
            value,
            {"schema_version", "kind", "audit_id", "source_construct_sha256", "authorization", "claim", "checks", "limitations"},
            "root",
        )
        require(value["schema_version"] == "1.0.0", "schema_version")
        require(value["kind"] == "host_closure_audit", "kind")
        require(value["audit_id"] == "C5-HOST-CLOSURE-AUDIT-1", "audit_id")
        require(value["source_construct_sha256"] == CONSTRUCT_SHA, "source_construct_sha256")
        require(bool(SHA256.fullmatch(value["source_construct_sha256"])), "source hash shape")
        require(value["authorization"] == "proceed with the audit", "authorization")
        require(value["claim"] == "host closure audit completed", "claim")
        require(isinstance(value["limitations"], list) and value["limitations"], "limitations")
        require(all(nonempty(item) for item in value["limitations"]), "invalid limitation")
        checks = value["checks"]
        require(isinstance(checks, list) and len(checks) == len(EXPECTED), "checks population")
        for index, (check, expected) in enumerate(zip(checks, EXPECTED, strict=True)):
            locus = f"checks[{index}]"
            finding_id, target, requirement_ids = expected
            require(isinstance(check, dict), f"{locus}: must be object")
            exact_keys(check, {"finding_id", "target", "outcome", "requirements", "basis", "authority_refs"}, locus)
            require(check["finding_id"] == finding_id, f"{locus}: finding_id")
            require(check["target"] == target, f"{locus}: target")
            require(check["outcome"] in {"closed", "not_closed", "unavailable"}, f"{locus}: outcome")
            require(nonempty(check["basis"]), f"{locus}: basis")
            require(isinstance(check["authority_refs"], list) and check["authority_refs"], f"{locus}: authority_refs")
            require(all(nonempty(item) for item in check["authority_refs"]), f"{locus}: invalid authority ref")
            requirements = check["requirements"]
            require(isinstance(requirements, list) and len(requirements) == len(requirement_ids), f"{locus}: requirements")
            outcomes = []
            for req_index, (requirement, requirement_id) in enumerate(zip(requirements, requirement_ids, strict=True)):
                req_locus = f"{locus}.requirements[{req_index}]"
                require(isinstance(requirement, dict), f"{req_locus}: must be object")
                exact_keys(requirement, {"requirement_id", "outcome", "basis", "ref"}, req_locus)
                require(requirement["requirement_id"] == requirement_id, f"{req_locus}: requirement_id")
                require(requirement["outcome"] in {"satisfied", "not_satisfied", "unavailable"}, f"{req_locus}: outcome")
                require(nonempty(requirement["basis"]), f"{req_locus}: basis")
                require(nonempty(requirement["ref"]), f"{req_locus}: ref")
                outcomes.append(requirement["outcome"])
            expected_outcome = "closed" if all(item == "satisfied" for item in outcomes) else (
                "unavailable" if any(item == "unavailable" for item in outcomes) else "not_closed"
            )
            require(check["outcome"] == expected_outcome, f"{locus}: aggregate outcome")
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
