"""Regression tests for the HEB-114 frontend contract validator."""

from __future__ import annotations

from pathlib import Path
import unittest

from scripts.validate_frontend_contracts import validate_frontend_contracts


ROOT = Path(__file__).resolve().parents[1]


class FrontendContractTests(unittest.TestCase):
    """Prove the shipped frontend contract and seeded populations remain coherent."""

    def test_frontend_contracts_pass(self) -> None:
        self.assertEqual(validate_frontend_contracts(ROOT), [])


if __name__ == "__main__":
    unittest.main()
