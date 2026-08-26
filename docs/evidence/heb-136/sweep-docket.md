# HEB-136 semantic sweep docket

Status: ratified by the operator on 2026-08-26 ET.

## Bottom line

The full ratified population was read: 55 of 55 Markdown carriers whole, 992
deterministic Markdown semantic units screened, and 17 of 17 structured
enforcement surfaces whole. No shipped normative rule was classified as
internal-state-triggered. The recommendation is therefore zero rule
conversions, zero external-detector additions, and zero known-weak labels in
the existing skill corpus.

This is a semantic judgment result, not a claim that prose is infallible. A
rule may require judgment and still have a workflow-event trigger when a named
artifact step, gate, operation, or runtime signal forces the evaluation. The
internal-state class is reserved for rules whose invocation depends on the
actor noticing an otherwise unobservable cognitive condition without such a
workflow binding.

## Population disposition

| Skill | Markdown carriers read whole | Structured surfaces read whole | Trigger result |
|---|---:|---:|---|
| `agent-code` | 3 | 1 | Workflow-event only |
| `app-delivery-pipeline` | 4 | 3 | Workflow-event only |
| `application-code` | 5 | 1 | Workflow-event only |
| `author-construct-spec` | 4 | 0 | Workflow-event only |
| `author-decision-record` | 5 | 1 | Workflow-event only |
| `author-execution-relay` | 5 | 1 | Workflow-event only |
| `author-standard` | 2 | 0 | Workflow-event only |
| `code-review` | 3 | 1 | Workflow-event only |
| `debug` | 2 | 1 | Workflow-event only |
| `design-review-loop` | 5 | 1 | Workflow-event only |
| `frontend-code` | 8 | 3 | Workflow-event only |
| `infrastructure-code` | 6 | 3 | Workflow-event only |
| `testing` | 3 | 1 | Workflow-event only |
| **Total** | **55** | **17** | **0 internal-state candidates** |

The structured surfaces were inspected as enforcement mechanisms. Their
individual schema properties were not counted as human-readable rules, per
the ratified sweep boundary.

The operator ratified the final count basis on 2026-08-26 ET: 55 carriers and
992 deterministic semantic units, rather than a fabricated atomic normative-
rule count. Units are paragraphs, list items, and substantive table rows;
front matter, headings, fenced code, blank lines, and table separator rows are
excluded. Finding rows are reserved for actual internal-state rules, so the
empty finding set is the result rather than missing inventory.

Direct review corrected the initial 988-unit report to 992: the first detector
recognized only single-digit ordered-list markers and folded four additional
multi-digit rows into prose. The corrected detector and regression test change
no semantic classification or disposition.

## Borderline calls

These were the strongest candidates for an internal-state classification.
They remain workflow-event rules for the reasons below.

| Locus | Apparent internal-state dependency | Observable firing event | Recommendation |
|---|---|---|---|
| `agent-code/SKILL.md:25` | Recognizing that constrained output is preferable | Selecting the model-call profile and output contract | Workflow-event; the profile/output-schema design step forces the choice |
| `application-code/reference/01-code-structure.md:37` | Deciding that a module's purpose is not evident | Authoring or reviewing a module boundary | Workflow-event; module creation/review supplies the inspection event, though enforcement remains discipline |
| `author-execution-relay/SKILL.md:40` | Noticing that copied content is instruction-like | Constructing the relay substrate and mutation envelope | Workflow-event; relay authoring requires an explicit substrate treatment |
| `frontend-code/SKILL.md:58` | Judging runtime data risk and deployment skew | Declaring the frontend profile and authoring the API boundary | Workflow-event; the profile and evidence schemas require the disposition |

## Corpus-wide trigger families

Every normative rule encountered bound to at least one of these observable
families:

1. skill routing or profile selection;
2. artifact authoring or boundary construction;
3. pre-mutation authorization or plan verification;
4. test, review, diagnosis, or evidence gate execution;
5. runtime capability, failure, cancellation, or lifecycle signal; or
6. completion, escalation, promotion, or handoff disposition.

Frequency and salience vary within those families, but none requires an actor
to remember to notice an unnamed internal state before the rule can fire.
Structured schemas strengthen several low-salience events; rules without a
schema remain workflow discipline rather than being reclassified merely
because their enforcement is weaker.

## Recommended dispositions for ratification

1. Ratify the sweep result as **55 Markdown carriers examined, 992 semantic
   units screened, 17 structured enforcement surfaces inspected, 0
   internal-state rules found, 0 converted, 0 externally detected, and 0
   labelled known-weak**.
2. Make no sweep-driven content changes outside `author-standard`; changing
   already event-bound rules would add churn without addressing HEB-136's
   failure mode.
3. Amend `author-standard` with the preregistered trigger test so future rules
   must name the firing event, class, frequency/salience, enforcement, and
   reliability disposition.
4. Keep the historical RBT-114 structural-instrument rule as the negative
   proof specimen. Its original form is internal-state-triggered; the
   per-property structural-instrument table is the expected conversion. This
   proves the test without pretending the historical rule is still shipped in
   the current Bedrock corpus.

## Empirical floor

The underlying operational evidence is grade B and clustered around a small
number of episodes. The zero-candidate corpus result is a whole-population
semantic inspection of the current repository, not empirical proof that every
workflow-event rule will fire reliably in every future execution. The trigger
test prevents unsupported reliability claims; it does not manufacture usage
evidence.
