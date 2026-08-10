# <Construct change>

| Field | Value |
|---|---|
| Document ID | <stable ID> |
| Status | PROPOSED / ACCEPTED-DESIGN / IMPLEMENTED / VERIFIED / GRADUATED / RETIRED |
| Revision | <simple revision; SemVer only if machine consumers require it> |
| Owner | <accountable owner> |
| Review trigger | <date, event, or condition> |
| Doctype ruling | <discriminator and result> |
| Deliberation substrate | <durable repository-native pointers> |
| Supersedes | <none or stable IDs> |

## Purpose and scope

State the change, where the construct sits, terms a cold implementer needs, and what closes the work.

### Authorities and preserved invariants

- <authority and exact applicability>
- <settled invariant not reopened>

### Out of scope

- <non-goal and trigger that would reopen it>

## Decision <stable-semantic-id> — <name>

### Decision and rationale

State what changes and the durable rationale that prevents likely misimplementation. If rationale would be invented, leave the spec PROPOSED and record the missing substrate.

### Amendments

| Path or artifact | Operation | Required result |
|---|---|---|
| `<path>` | add / modify / delete / no-change | <testable result> |

### Correctness invariants

- **<stable-id>:** <property that must hold>
- **<linked-id>:** <coupled property, if separation would obscure correctness>

### Obligations

| ID | Obligation | Instrument | Gates landing | Evidence |
|---|---|---|---|---|
| `<stable-id>` | <testable obligation> | <test/eval/audit> | yes/no | <retained pointer> |

### Risks and failure behavior

- <failure mode> → <guard, refusal, or escalation>

## Evidence handling

For any evidence copied or linked elsewhere, record source, destination, checksum or equivalent integrity evidence, access verification, rollback, and the later duplicate-retirement gate. Do not delete the source in the relocation step.

## Lifecycle gate

| Transition | Required evidence | Result |
|---|---|---|
| design acceptance | operator decision | pending / passed |
| implementation | implementation identity | pending / passed |
| verification | obligation evidence | pending / passed |
| graduation | destination lifecycle + post-build review + operator decision | pending / passed / not-applicable |

## Relation redirects

When stable IDs split, merge, or rename at a revision boundary, map old IDs to current IDs here. Otherwise omit this section.

## Change log

| Revision | Date | Change |
|---|---|---|
| <revision> | YYYY-MM-DD | <current-state summary> |

<!-- STANDING: prior published rows remain frozen; amend the unpublished current row in place. -->
