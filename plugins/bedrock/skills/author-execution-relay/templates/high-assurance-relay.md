# High-assurance execution relay

Attach a relay document conforming to `reference/relay.schema.json` and evidence that the execution boundary validates it.

## Required controls

- authenticated, scoped, fresh, revocable, replay-resistant authorization;
- canonical mutation manifest and repository base identity;
- executable allowlist enforcement;
- separated authority, instructions, untrusted data, and evidence;
- explicit operator gates and halt-on-anomaly behavior; and
- independent durable-form verification with unavailable behavior.

If any required control is unavailable, stop or deliberately select a lower profile without claiming high-assurance enforcement.
