# HEB-136 representative-consumer proof — RBT-114

Status: passed on 2026-08-26 ET.

## Sources and read depth

- Linear RBT-114: fresh-fetched and read whole on 2026-08-26 ET.
- Linear HEB-133: fresh-fetched and read whole on 2026-08-26 ET.
- Amended `author-standard`: read whole on 2026-08-26 ET.

RBT-114 is the historical transaction. HEB-133 preserves the detailed
text-shaped-measurement population and the proposed per-property structural
instrument. The ticket evidence is grade B: eight recorded instances across
two execution surfaces, with instances 4–8 clustered in one two-day close-out.

## Rule under test

Historical rule:

> Use the structural instrument rather than a text match when measuring a
> property.

The rule's original trigger was the actor recognizing that it was choosing a
measurement method. That recognition happened on hundreds of low-salience
acts, including while verifying earlier instances of the same failure class.
The trigger was therefore internal-state, high-frequency, low-salience, and
carried only by discipline.

## Trigger-test result

| Case | Trigger | Frequency / salience | Enforcement | Expected | Observed |
|---|---|---|---|---|---|
| RBT-114 original | `internal-state` | high / low | discipline | reject | reject |
| Converted rule | `workflow-event` | high / low | named instrument | ship | ship |
| Forceful-wording adversarial | `internal-state` | high / low | none | reject | reject |

The original fails `author-standard` before adoption because discipline is not
a permitted disposition for an internal-state trigger. Stronger wording does
not change the result.

## Conversion

Converted rule:

> At each named property measurement, select the structural instrument from
> the per-property table.

The table binds the choice to an observable event: computing a named property.
Each row names the property and its authoritative structural instrument. The
historical examples include commit-parent measurement via
`git rev-list --parents`, deletion counts via `git diff --numstat`, PR-body
comparison via decoded JSON, and commit-body inspection via `%b` or the commit
object. The conversion changes the firing mechanism rather than asking for
more attention.

This proof does not land HEB-133's broader checklist or choose its final
carrier. It demonstrates that HEB-136's general trigger test rejects the
historical weak shape and admits the instrument-bound replacement.

## Reproduction

```text
/tmp/heb136-validation-venv/bin/python -m unittest tests.test_authoring_contracts -v
```

The retained fixture cases are:

- `rbt-114-structural-instrument-original` → `reject`;
- `rbt-114-structural-instrument-converted` → `ship`; and
- `forceful-wording-without-workflow-binding` → `reject`.

Focused result: 8/8 authoring-contract tests passed.

## Threshold disposition

- Positive workflow-event case: passed.
- Negative historical internal-state case: passed.
- Adversarial forceful-wording case: passed.
- Representative consumer: passed.
- Evidence availability: passed; all named Linear sources were read whole.

The preregistered representative-consumer threshold is satisfied.
