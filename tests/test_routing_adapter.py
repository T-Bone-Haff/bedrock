from __future__ import annotations

import json
import unittest

from scripts.run_routing_evals import _parse_result, build_routing_prompt


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
        self.assertTrue(prompt.endswith("Diagnose a flaky test."))


if __name__ == "__main__":
    unittest.main()
