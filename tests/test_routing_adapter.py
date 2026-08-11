from __future__ import annotations

import json
import unittest

from scripts.run_routing_evals import (
    _extract_usage,
    _parse_result,
    build_report,
    build_routing_prompt,
    evaluate_thresholds,
)


class RoutingAdapterResultTests(unittest.TestCase):
    def test_reads_structured_output(self) -> None:
        payload = {"structured_output": {"skill": "debug", "reason": "failure diagnosis"}}
        self.assertEqual(payload["structured_output"], _parse_result(json.dumps(payload)))

    def test_reads_json_result_fallback(self) -> None:
        result = {"skill": None, "reason": "no matching skill"}
        self.assertEqual(result, _parse_result(json.dumps({"result": json.dumps(result)})))

    def test_rejects_non_object_envelope(self) -> None:
        with self.assertRaisesRegex(ValueError, "envelope must be an object"):
            _parse_result("[]")

    def test_recovers_billed_usage_from_typed_error_envelope(self) -> None:
        payload = json.dumps(
            {
                "subtype": "error_max_budget_usd",
                "total_cost_usd": 0.033976,
                "modelUsage": {"resolved-model": {"costUSD": 0.033976}},
            }
        )
        self.assertEqual((0.033976, ["resolved-model"]), _extract_usage(payload))

    def test_unstructured_failure_has_no_claimed_usage(self) -> None:
        self.assertEqual((0.0, []), _extract_usage("transport failed"))

    def test_prompt_embeds_authoritative_catalog_and_request(self) -> None:
        prompt = build_routing_prompt(
            {"prompt": "Diagnose a flaky test."},
            [
                {"name": "testing", "description": "New tests only. Do not use for flakes."},
                {"name": "debug", "description": "Use for an existing flaky test."},
            ],
        )

        self.assertIn("- debug: Use for an existing flaky test.", prompt)
        self.assertIn("- testing: New tests only. Do not use for flakes.", prompt)
        self.assertIn("do not infer ownership from a skill name alone", prompt)
        self.assertIn("not binding authority", prompt)
        self.assertIn("select that skill rather than returning null", prompt)
        self.assertTrue(prompt.endswith("Diagnose a flaky test."))

    def test_thresholds_require_aggregate_case_and_exclusion_gates(self) -> None:
        policy = {
            "minimum_overall_pass_rate": 0.75,
            "minimum_case_pass_rate": 0.5,
            "excluded_selection_limit": 0,
        }
        results = [
            {"case": "a", "passed": True, "selected_excluded": False},
            {"case": "a", "passed": False, "selected_excluded": False},
            {"case": "b", "passed": True, "selected_excluded": False},
            {"case": "b", "passed": True, "selected_excluded": False},
        ]
        evaluation = evaluate_thresholds(results, policy)
        self.assertTrue(evaluation["passed"])
        results[-1]["selected_excluded"] = True
        self.assertFalse(evaluate_thresholds(results, policy)["passed"])

    def test_report_carries_reproducibility_identity_and_evaluation(self) -> None:
        results = [
            {
                "case": "a",
                "passed": True,
                "selected_excluded": False,
                "cost_usd": 0.01,
                "models": ["resolved-model"],
            }
        ]
        report = build_report(
            model="haiku",
            profile="pr",
            policy={
                "minimum_overall_pass_rate": 1.0,
                "minimum_case_pass_rate": 1.0,
                "excluded_selection_limit": 0,
            },
            runs=1,
            max_budget_usd=0.03,
            timeout_seconds=120,
            cli_version="1.2.3",
            fixture_digest="fixture-sha",
            catalog_digest="catalog-sha",
            policy_digest="policy-sha",
            results=results,
            max_total_budget_usd=3.0,
        )
        self.assertEqual(2, report["schema_version"])
        self.assertEqual("fixture-sha", report["identity"]["fixture_sha256"])
        self.assertEqual(3.0, report["max_total_budget_usd"])
        self.assertFalse(report["budget_exhausted"])
        self.assertTrue(report["evaluation"]["passed"])
        self.assertTrue(report["evaluation"]["retained_evidence_eligible"])

    def test_targeted_report_cannot_claim_retained_release_evidence(self) -> None:
        results = [
            {
                "case": "a",
                "passed": True,
                "selected_excluded": False,
                "cost_usd": 0.0,
                "models": [],
            }
        ]
        report = build_report(
            model="haiku",
            profile="release",
            policy={
                "minimum_overall_pass_rate": 1.0,
                "minimum_case_pass_rate": 1.0,
                "excluded_selection_limit": 0,
            },
            runs=1,
            max_budget_usd=0.03,
            timeout_seconds=120,
            cli_version="1.2.3",
            fixture_digest="fixture-sha",
            catalog_digest="catalog-sha",
            policy_digest="policy-sha",
            results=results,
            suite_scope="targeted",
            planned_case_ids=["a"],
        )
        self.assertTrue(report["evaluation"]["passed"])
        self.assertFalse(report["evaluation"]["retained_evidence_eligible"])

    def test_report_fails_when_aggregate_budget_is_exceeded(self) -> None:
        results = [
            {
                "case": "a",
                "passed": True,
                "selected_excluded": False,
                "cost_usd": 0.031,
                "models": ["resolved-model"],
            }
        ]
        report = build_report(
            model="haiku",
            profile="release",
            policy={
                "minimum_overall_pass_rate": 1.0,
                "minimum_case_pass_rate": 1.0,
                "excluded_selection_limit": 0,
            },
            runs=1,
            max_budget_usd=0.03,
            timeout_seconds=120,
            cli_version="1.2.3",
            fixture_digest="fixture-sha",
            catalog_digest="catalog-sha",
            policy_digest="policy-sha",
            results=results,
            max_total_budget_usd=0.03,
        )
        self.assertFalse(report["evaluation"]["gates"]["budget"])
        self.assertFalse(report["evaluation"]["passed"])
        self.assertFalse(report["evaluation"]["retained_evidence_eligible"])


if __name__ == "__main__":
    unittest.main()
