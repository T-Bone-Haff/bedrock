# HEB-136 pre-registration and audit-instrument results

## Meaningful red

The first system-Python and bundled-runtime attempts could not import the
repository's pinned PyYAML dependency. Those were harness failures and are not
counted as meaningful red.

An isolated temporary Python environment was created with
`validation/requirements.txt`. Against the intentionally empty validator
scaffold, the five focused tests produced four expected failures at the target
boundary:

- missing Markdown-carrier detection;
- unlisted structured-file detection;
- rejection of an undispositioned internal-state rule; and
- rejection of pending structured-file inspections at the completion gate.

The untouched inventory case passed. This demonstrated that the test harness
could distinguish valid inventory state from the four missing behaviors.

## Implementation result

After implementing the minimum validator, one focused test remained red. Raw
filesystem traversal included five ignored `.DS_Store` files, while the
ratified population and `rg --files` correctly enumerated shipped carriers.
The validator was repaired to enumerate the declared structured enforcement
formats (`.json`, `.yaml`, `.yml`) rather than every local non-Markdown file.
The original reproducer then passed unchanged.

The final focused suite passes **11/11**. It covers live-population
agreement, fail-closed ledger removal, invalid trigger vocabulary,
undispositioned internal-state rules, count drift, pending Markdown and
structured inspections, multi-digit ordered-unit counting, and a complete
empty-finding positive fixture.

Inventory validation passes for exactly 55 Markdown carriers and 17 structured
files. Before the sweep, strict completion failed as intended on pending
carrier and structured-file inspections.

## Package regression

The first full suite run used locally installed Claude CLI `2.1.233` and failed
one pre-existing strict-host integration test: that CLI returned success for a
seeded invalid-frontmatter fixture. The repository pins Claude CLI `2.1.226` in
CI. An isolated `2.1.226` run passed the exact failing test, establishing host
version drift as the cause rather than HEB-136.

With the repository-pinned CLI identity, the pre-amendment full suite passed
**116 tests** with the existing Docker-daemon integration skipped locally. No
repository change was made for the unrelated local-host drift.

## Author-standard amendment

Six generic trigger cases cover a salient
workflow event, a high-frequency/low-salience workflow event carried only by
discipline, an undispositioned internal-state rule, an instrumented
internal-state rule, an externally detected internal-state rule, and a
known-weak internal-state rule. The original five cases all initially failed
at the intended boundary as `unknown`; the remaining authoring-contract tests
stayed green. Direct review then added the omitted external-detector case and
separated enforcement from reliability disposition in every fixture.

After the deterministic classifier was implemented, the original five
behavior cases passed while the carrier-integrity gate remained red because
`author-standard` did not yet contain the trigger contract. The amendment then
added the named event, trigger class, frequency, salience, enforcement,
expected-failure, and reliability-disposition requirements. The focused
authoring suite passed **8/8**.

The package validators detected stale context-budget evidence caused by the
larger entrypoint. Re-measurement established 889 words for `author-standard`
and 9,922 across all progressively disclosed entrypoints, below the 1,200-word
per-skill ceiling. Plugin, package-governance, and authoring validators then
passed.

The first post-amendment full suite exposed a positive release-mode test that
hardcoded the prior manifest version. The test now derives version and tag from
the sole manifest authority. Under the repository-pinned Claude CLI, the full
suite passes **118 tests** with the unavailable Docker integration skipped;
both Terraform integrations passed in the final run.

## Representative-consumer proof

Linear RBT-114 and HEB-133 were fresh-fetched and read whole. Three retained
cases exercise the historical rule: its original discipline-only
internal-state form rejects; the per-property structural-instrument conversion
ships as a workflow-event-bound instrument; and forceful wording without a
workflow binding still rejects. The focused authoring suite passes **8/8**.
The complete reasoning and evidence limits are retained in
`rbt-114-consumer-proof.md`.

## Completed sweep and count basis

The operator ratified reporting 55 Markdown carriers examined and a
deterministic semantic-unit count instead of claiming an artificial atomic
rule count. The unit algorithm counts paragraphs, list items, and substantive
table rows while excluding front matter, headings, fenced code, blank lines,
and table separator rows. Finding rows are reserved for actual internal-state
rules.

Direct review exposed a multi-digit ordered-list defect in the first counter:
it reported 988 by recognizing only single-digit markers. The corrected
detector failed meaningfully against the stale ledger with an expected count
of 992; a focused regression case now proves `9.`, `10.`, and `11.` are three
units. The corrected ledger reports 992. No semantic finding or disposition
changed.

All 55 Markdown carriers and 17 structured enforcement files are marked
inspected. The semantic sweep found zero shipped internal-state-triggered
rules, so the final finding set is empty and all disposition counts are zero.
The validator derives 55 carriers and 992 units from the live corpus; strict
completion passes with zero unresolved findings.

## Direct review

A standard-profile direct review found and repaired two pre-landing contract
defects: behavior fixtures had conflated `known-weak` disposition with
enforcement and omitted the external-detector path; the semantic-unit counter
did not recognize multi-digit ordered-list markers. The final-tree review has
zero unresolved findings and verdict `approve`. The schema-conformant result is
retained in `direct-review.json`.

## Current gate

The trigger amendment, representative-consumer proof, semantic sweep, strict
completion instrument, final package regression, and direct review are green.
The remaining gate is the separately ratified git transaction.
