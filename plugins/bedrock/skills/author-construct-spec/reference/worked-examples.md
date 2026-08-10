# Worked construct-spec examples

## Small accepted and verified change

Source context: a parser accepts two JSON payloads although the contract permits one. Deliberation compares reject-all with first-payload salvage and selects reject-all because accepting ambiguity changes authority.

Decision `single-payload`: reject zero or multiple payload candidates. Rejected alternative: first-payload salvage, because payload order is not authority. Handoff: a small relay names the parser and tests. Verification: empty, single, and multiple-candidate fixtures. Graduation: not applicable; the rule remains local to this implementation.

## Rejected proposal

Source context: a request asks for a new runner but supplies no observed failure, decision record, or design comparison. The spec remains PROPOSED with missing substrate; no rationale is invented and no executor handoff is produced.

## Failed evidence move

An author copies a corpus to a new repository path, but the cold reader lacks permission. Destination verification fails, the source remains intact, and rollback is unnecessary. The relocation does not complete and no duplicate-retirement gate opens.

## Graduation example

A serialization rule is implemented and verified, and a second independent component must conform. Post-build review names the governed protocol schema as destination, verifies its owner/version/retirement contract, and the operator approves graduation. The spec points to the schema and retains the design rationale without duplicating the operative fields.
