# HEB-109 seeded-defect evidence

`python3 -m unittest tests.test_validate_plugin.ValidatorTests -v` first failed the newly added cases because the Wave 1 validator did not detect missing relative targets, private absolute paths, undeclared external roots, stale snapshot declarations, uninventoried examples, missing evidence, or invalid thresholds.

After implementing the deterministic checks, the same cases pass by proving that each seeded defect produces its expected actionable diagnostic. The tests mutate isolated temporary repositories; they do not alter the distributable plugin.
