# HEB-136 proving profile

Status: evaluated; trigger contract and sweep completed.

## Decision and binding

HEB-136 amends `author-standard` so a reusable rule cannot claim reliable
coverage until its trigger is named and tested. The amendment binds future
Bedrock standard authorship and the retrospective sweep of all shipped Bedrock
skill carriers.

The sweep population is all Markdown below `plugins/bedrock/skills`: 55
carriers at preregistration. The 17 non-Markdown files below that root were
inspected as enforcement surfaces but were not counted property by property as
human-readable rules.

### Post-preregistration counting clarification

Ratified on 2026-08-26 ET after the whole-population semantic sweep: report
the 55 carriers examined and the 992 deterministic Markdown semantic units
screened. A semantic unit is a paragraph, list item, or substantive table row;
front matter, headings, fenced code, blank lines, and table separator rows are
excluded. Finding rows are reserved for actual internal-state-triggered
normative rules.

This clarification avoids manufacturing an atomic rule count that the source
format cannot support reliably. It does not change the preregistered population,
classification contract, cases, or success threshold: deterministic units
prove screen coverage, while normative-rule identification remains a semantic
judgment.

Direct review corrected the initially reported 988 units to 992 when the
detector was found to recognize only single-digit ordered-list markers. The
corrected detector recognizes multi-digit markers and is retained by a focused
regression test; the correction changes no semantic finding or disposition.

## Evidence and provenance

| Source | Access | Grade | Applicability and limit |
|---|---|---|---|
| Linear HEB-136 | 2026-08-26 ET, read whole | B | Governing work order and acceptance criteria. |
| Linear RBT-122 | 2026-08-26 ET, read whole | B | Multiple operational observations across three surfaces; many observations cluster around one transaction. |
| Linear HEB-133 | 2026-08-26 ET, read whole | B | Supplies the structural-measurement specimen and a concrete instrument-shaped remedy; its broader graduation scope remains separate. |
| `author-standard` at the HEB-136 baseline | 2026-08-26 ET, read whole | C | Current installed contract and amendment target. |

Author judgment: the evidence does not prove that an internal-state-triggered
rule is never followed. It is sufficient to rule that such prose cannot count
as reliable coverage without an instrument, external detector, or explicit
known-weak disposition.

## Trigger-test contract under proof

For each normative rule, name:

1. the event that fires it;
2. whether that event is externally observable or depends on recognizing an
   internal state;
3. expected firing frequency and salience;
4. its instrument or detector, if any; and
5. its reliability disposition.

A workflow-event trigger may be carried by discipline. An internal-state
trigger must be converted to an instrument, given an external detector, or
labelled known-weak with its expected failure. An undispositioned
internal-state rule fails the adoption gate.

## Preregistered cases

### Positive

Rule: stop for operator ratification when a named gate is reached.

Expected classification: `workflow-event`. The gate is observable, salient,
and externally enforced. Expected result: eligible to claim reliable coverage
through discipline.

### Negative and representative consumer

Historical RBT-114 rule: use the structural instrument rather than a text
match when measuring a property.

Expected classification: `internal-state`. Its original trigger is the actor
recognizing that it is choosing a measurement method, a high-frequency and
low-salience event. Expected result: barred from claiming reliable coverage in
that form. A per-property structural-instrument table bound to the act of
computing the named property is the expected conversion.

This proof evaluates the trigger test against the historical rule. It does not
implement HEB-133's broader graduation scope.

### Adversarial

Rule shape: a strongly worded imperative that says to verify current authority
but does not bind the verification to a named workflow event or output.

Expected classification: `internal-state` despite forceful wording. Expected
result: barred from claiming reliable coverage until dispositioned.

## Deterministic and judgment evidence

Deterministic checks:

- the audit ledger enumerates the exact live Markdown-carrier population;
- the structured-file inventory enumerates the exact live non-Markdown
  population;
- identifiers and loci are unique;
- required classification and disposition fields use the closed vocabulary;
- completion fails when a carrier, structured-file inspection, or identified
  internal-state disposition remains open; and
- reported carrier, semantic-unit, finding, and disposition counts are derived
  from the live corpus and ledger.

Judgment evaluations:

- whether a statement is a normative rule;
- what event actually fires it;
- whether the trigger depends on internal-state recognition;
- whether frequency and salience make discipline credible; and
- whether the proposed instrument, detector, or known-weak label preserves the
  rule's intent.

The deterministic instrument proves population and record completeness. It
does not claim semantic discovery or classification.

## Thresholds

Success requires all three preregistered cases to match their expected
classifications, all 55 Markdown carriers and all 992 deterministic semantic
units to be screened, all 17 structured files to be inspected, and every
identified internal-state rule to have one ratified disposition. The final
ledger must report zero unresolved findings.

Failure is any case misclassification, carrier-population or semantic-unit
mismatch, undispositioned internal-state rule, unsupported reliability claim,
or final count not derived from the live corpus and ledger.

Evidence is unavailable when a named historical source or exact carrier cannot
be read. Unavailable evidence pauses adoption; it is not converted to a pass or
silently removed from the population.

## Retention and reproduction

Retain the populated ledger, validator, seeded tests, validation transcript,
consumer proof, direct review, and final counts under `docs/evidence/heb-136/`
or their repository-native validation locations. Exact reproduction commands
will be recorded in the evidence manifest after the instrument reaches green.
