# ADR-001 ownership amendment — adjudication ledger

Aggregation policy: adjudicated merge. The seven merged defects were frozen in an input object with SHA-256 `99058ca48c06bd96a1df94693da5fd2bb5eee66d16cd86dcfcef471aab7d587b`. A separate bounded arbiter classified each defect under the frozen arbiter contract; it did not fix records or decide completion.

| Canonical finding | Sources merged | Severity | Classification | Confidence | Disposition |
|---|---|---|---|---|---|
| `2f82da…feb35` | LAA + EA + cross-set | BLOCKING | resolvable | high | Removed partial promotion criteria; made the separate promotion standard an explicit prerequisite in migration. |
| `75dc98…5860` | LAA + SA + cross-set | MATERIAL | resolvable | high | Replaced the verification disjunction with the current reviewed/escalated state. |
| `3ccb4d…1290` | LAA + cross-set | MATERIAL | resolvable | high | Added `Successor: None`. |
| `1fa13f…006b` | LAA | MATERIAL | resolvable | high | Added the ratified preservation obligation without compatibility obligation. |
| `d0fa76…1da8` | SA | MATERIAL | decision-bearing | high | Operator disposed after review: security, privacy, compliance, and cost are not applicable for the stated reasons; operations is limited to ordinary shared-contract version drift and its existing compatibility/release controls. Corrected in ADR §5.4. |
| `661d3a…7e42` | EA + SA + cross-set | BLOCKING | decision-bearing | high | Operator disposed after review: ADR-001 and documentation carriers target 2.0.0; HEB-126 does not change the non-shipped package version, and HEB-128 owns later shipped-plugin conformance and package-major derivation. |
| `5547db…f76c` | SA + cross-set | MATERIAL | resolvable | high | Corrected the ADR's universal recipe/kernel prerequisite. Shipped governance-carrier corrections are routed to HEB-128 so their package-major transaction remains separate from HEB-126. |

## Arbiter evidence

The arbiter returned seven schema-shaped `arbitration_result` objects. Their `input_sha256` values were:

- `561328338af02494d5e07417730989cedf7ac2addccefc0469b4e2bcc7943614`
- `1e0b38453d1d6284bde2f64ff0302f2454c2b2ae8729fb7ecc0c18a0081fc3ea`
- `b06526cd8752ab97ee1dd86067d6411cdb86e7a237eb0563666be9cd83aa6341`
- `85bebfa70cebbccca87ffb0fd7f3963dd9eadd4490dfc0b58e43c572c38bf247`
- `834e09d13764500026cba4ad28c86797c60c76bba00b7cef3d8d9e7f98e8ce8e`
- `3d4b42166498aae48417e205973be50347bb649eefa086bcb74dabdeb2b4da25`
- `c5c9e6492fd088c60e727117ce0421cc1289932076303dd49f1c4f96d8b99525`

The host did not retain provider-native structured-output or attempt telemetry, so this is multi-perspective arbitration evidence, not runner evidence or a mechanical convergence result.

## Post-review operator dispositions

On 2026-08-12, Tad Haffey supplied the missing risk-domain judgment, removed product-specific examples from the general ADR, and ratified the ADR/carrier major treatment as 2.0.0. He distinguished non-shipped documentation authority from later shipped-plugin implementation. The author therefore limited HEB-126 to four documentation files, routed plugin conformance/package-major work to HEB-128, and retained product-specific material only in the explicitly named SOFIA compatibility profile and frozen review evidence. A targeted cross-reference/coherence sweep and deterministic validators were rerun after the correction.
