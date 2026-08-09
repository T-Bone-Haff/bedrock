#!/usr/bin/env python3
"""Run shared Bedrock routing fixtures through the Claude Code adapter."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from typing import Any

try:
    from scripts.validate_plugin import load_routing_cases, validate_repository
except ModuleNotFoundError:  # Direct execution sets scripts/ as sys.path[0].
    from validate_plugin import load_routing_cases, validate_repository


OUTPUT_SCHEMA = json.dumps(
    {
        "type": "object",
        "properties": {
            "skill": {"type": ["string", "null"]},
            "reason": {"type": "string"},
        },
        "required": ["skill", "reason"],
        "additionalProperties": False,
    }
)


def _parse_result(stdout: str) -> dict[str, Any]:
    payload = json.loads(stdout)
    if not isinstance(payload, dict):
        raise ValueError("Claude response envelope must be an object")
    structured = payload.get("structured_output")
    if isinstance(structured, dict):
        return structured
    result = payload.get("result")
    if isinstance(result, str):
        parsed = json.loads(result)
        if isinstance(parsed, dict):
            return parsed
    raise ValueError("Claude response did not contain a structured routing result")


def check_authentication(executable: str) -> str | None:
    environment = os.environ.copy()
    environment.pop("CLAUDECODE", None)
    result = subprocess.run(
        [executable, "auth", "status"],
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        status = json.loads(result.stdout)
    except json.JSONDecodeError:
        return "could not determine Claude authentication status"
    if status.get("loggedIn") or environment.get("ANTHROPIC_API_KEY"):
        return None
    return "Claude routing adapter is not authenticated; run `claude /login` or provide ANTHROPIC_API_KEY"


def build_routing_prompt(case: dict[str, Any], skills: list[dict[str, Any]]) -> str:
    catalog = "\n".join(
        f"- {skill['name']}: {skill['description']}" for skill in sorted(skills, key=lambda item: item["name"])
    )
    return (
        "Select the single Bedrock skill that should handle the user request below. "
        "Treat the validated routing catalog as authoritative: apply each description's explicit scope and "
        "exclusions, and do not infer ownership from a skill name alone. Choose null when no description "
        "authorizes the request. Return only the requested structured result and do not solve the request.\n\n"
        "Validated Bedrock routing catalog:\n"
        f"{catalog}\n\n"
        "User request:\n"
        f"{case['prompt']}"
    )


def run_case(
    executable: str,
    plugin_dir: Path,
    case: dict[str, Any],
    skills: list[dict[str, Any]],
    model: str,
    max_budget_usd: float,
    timeout_seconds: int,
) -> tuple[bool, str | None, str, float, list[str]]:
    prompt = build_routing_prompt(case, skills)
    environment = os.environ.copy()
    environment.pop("CLAUDECODE", None)
    try:
        result = subprocess.run(
            [
                executable,
                "--bare",
                "--print",
                "--plugin-dir",
                str(plugin_dir),
                "--tools",
                "",
                "--model",
                model,
                "--max-budget-usd",
                str(max_budget_usd),
                "--no-session-persistence",
                "--output-format",
                "json",
                "--json-schema",
                OUTPUT_SCHEMA,
                prompt,
            ],
            cwd=plugin_dir,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired:
        return False, None, f"routing process exceeded {timeout_seconds} seconds", 0.0, []
    if result.returncode != 0:
        return False, None, (result.stderr or result.stdout).strip(), 0.0, []
    try:
        envelope = json.loads(result.stdout)
        routed = _parse_result(result.stdout)
    except (json.JSONDecodeError, ValueError) as exc:
        return False, None, str(exc), 0.0, []
    selected = routed.get("skill")
    expected = case.get("expected")
    alternates = case.get("allowed_alternates", [])
    passed = selected == expected or (case.get("kind") == "overlap" and selected in alternates)
    if selected in case.get("excluded", []):
        passed = False
    cost = envelope.get("total_cost_usd", 0.0) if isinstance(envelope, dict) else 0.0
    model_usage = envelope.get("modelUsage", {}) if isinstance(envelope, dict) else {}
    models = sorted(model_usage) if isinstance(model_usage, dict) else []
    return passed, selected, str(routed.get("reason", "")), float(cost or 0.0), models


def build_report(
    *,
    model: str,
    runs: int,
    max_budget_usd: float,
    timeout_seconds: int,
    cli_version: str,
    results: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "adapter": "claude-code",
        "claude_cli_version": cli_version,
        "requested_model": model,
        "resolved_models": sorted({name for result in results for name in result["models"]}),
        "runs_per_case": runs,
        "max_budget_usd_per_case_run": max_budget_usd,
        "timeout_seconds_per_case_run": timeout_seconds,
        "passed": sum(1 for result in results if result["passed"]),
        "total": len(results),
        "total_cost_usd": round(sum(result["cost_usd"] for result in results), 8),
        "results": results,
    }


def write_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--model", default="haiku")
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--case", action="append", dest="case_ids")
    parser.add_argument("--max-budget-usd", type=float, default=0.03, help="Per-case-run budget ceiling.")
    parser.add_argument("--timeout-seconds", type=int, default=120, help="Per-case-run wall-clock limit.")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    executable = shutil.which("claude")
    if executable is None:
        print("FAIL: Claude Code CLI is required for the Claude routing adapter", file=sys.stderr)
        return 2
    auth_error = check_authentication(executable)
    if auth_error:
        print(f"FAIL: {auth_error}", file=sys.stderr)
        return 2
    if args.runs < 1:
        parser.error("--runs must be at least 1")
    if args.timeout_seconds < 1:
        parser.error("--timeout-seconds must be at least 1")

    fixture_errors: list[str] = []
    repository_errors, inventory = validate_repository(args.root.resolve(), run_host_cli=False)
    fixture_errors.extend(repository_errors)
    cases = load_routing_cases(args.root.resolve(), fixture_errors)
    if fixture_errors:
        for error in fixture_errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 2
    if args.case_ids:
        requested = set(args.case_ids)
        cases = [case for case in cases if case.get("id") in requested]
        missing = requested - {str(case.get("id")) for case in cases}
        if missing:
            print(f"FAIL: unknown case ids: {sorted(missing)}", file=sys.stderr)
            return 2

    results: list[dict[str, Any]] = []
    plugin_dir = args.root.resolve() / "plugins" / "bedrock"
    version_result = subprocess.run(
        [executable, "--version"], capture_output=True, text=True, check=False, timeout=10
    )
    cli_version = version_result.stdout.strip() or "unknown"
    for case in cases:
        for run_number in range(1, args.runs + 1):
            passed, selected, detail, cost_usd, models = run_case(
                executable,
                plugin_dir,
                case,
                inventory["skills"],
                args.model,
                args.max_budget_usd,
                args.timeout_seconds,
            )
            record = {
                "case": case["id"],
                "kind": case["kind"],
                "run": run_number,
                "expected": case.get("expected"),
                "selected": selected,
                "passed": passed,
                "detail": detail,
                "cost_usd": cost_usd,
                "models": models,
            }
            results.append(record)
            print(
                f"{'PASS' if passed else 'FAIL'} {case['id']} run={run_number} "
                f"expected={case.get('expected')!r} selected={selected!r}",
                flush=True,
            )
            if not passed:
                print(f"  detail: {detail}", flush=True)
            if args.output:
                write_report(
                    args.output,
                    build_report(
                        model=args.model,
                        runs=args.runs,
                        max_budget_usd=args.max_budget_usd,
                        timeout_seconds=args.timeout_seconds,
                        cli_version=cli_version,
                        results=results,
                    ),
                )

    report = build_report(
        model=args.model,
        runs=args.runs,
        max_budget_usd=args.max_budget_usd,
        timeout_seconds=args.timeout_seconds,
        cli_version=cli_version,
        results=results,
    )
    if args.output:
        write_report(args.output, report)
    return 0 if report["passed"] == report["total"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
