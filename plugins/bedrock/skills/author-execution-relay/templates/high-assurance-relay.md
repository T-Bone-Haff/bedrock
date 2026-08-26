# High-assurance execution relay

Attach a relay document conforming to `reference/relay.schema.json` and evidence that the execution boundary validates it.

The schema carries transaction identity and controls; the authored relay also carries this instrument contract:

- consumer configuration, parser, schema, wrapper, or gate read whole and pinned;
- its accepted grammar and outcome taxonomy carried verbatim;
- an exact author-time dry-run proving the command, actor, checkout, inputs, and output are jointly satisfiable;
- touch allowlist derived bidirectionally from ratified edit-locus rows; and
- custody evidence separated from production reachability evidence.

| Property or premise | Verdict-bearing inputs/pins | Population | Structural instrument or falsification control | Outcomes / unavailable | Report field |
|---|---|---|---|---|---|
| <property> | <pins> | <population or n/a> | <independent command/API/parser and contrary control> | <verbatim tokens; unavailable behavior> | <field> |

## Required controls

- authenticated, scoped, fresh, revocable, replay-resistant authorization;
- canonical mutation manifest and repository base identity;
- executable allowlist enforcement;
- separated authority, instructions, untrusted data, and evidence;
- explicit operator gates and halt-on-anomaly behavior; and
- independent durable-form verification with unavailable behavior and premise dispositions of `confirmed`, `falsified`, or `unavailable`.

If any required control is unavailable, stop or deliberately select a lower profile without claiming high-assurance enforcement.
