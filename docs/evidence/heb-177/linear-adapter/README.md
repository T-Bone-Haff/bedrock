# HEB-177 adapter extension: offline evidence

This candidate extends the standalone `hex-linear` package from accepted Bedrock
base `2d18b1b4c418168e3362c9a5e641b05a1579307d`. Tad ratified P1–P4 and then explicitly
authorized this isolated offline implementation gate. Staging, commits, publication
and live provider operations remain outside this gate.

The package README carries the extension contract and immutable DDR-002 provenance.
`test-strategy.json` states the deterministic test gate; `verification.json` binds
results and limitations to exact source hashes. These records concern only the
adapter package and named evidence files, not the complete Bedrock plugin or HEX
workflow. Existing HEB-170 acceptance and old live fixtures are unchanged.

## Profile and evidence limits

Application-code uses its portable core specialized to the existing standalone
Python/HTTPX library. No FastAPI service, database, deployment, credential discovery,
telemetry or background runtime is introduced. Testing retains the existing pytest
and HTTPX MockTransport stack instead of the service profile's respx/ASGI fixtures.
The unit suite checks consumer request/response behavior, not provider effects.
The official provider schema is a separately verified artifact; static validation
is not represented as a live provider contract trial.

The risk-selected coverage gate is 90% lines / 80% branches across all four runtime
modules, with no exclusions. Wrong-object, omission-versus-null, reversed-edge,
unsupported-delete, malformed response and one-attempt controls carry the critical
boundary claims; the coverage percentage is only a supplementary signal.

Advanced-method dispositions: deterministic parameterized malformed inputs cover
the selected boundary partitions; open-ended property/fuzz campaigns are not
applicable to this bounded change with no new general parser. Seeded wrong-identity,
direction, omission and success receipts provide mutation-style counterexamples;
a formal mutation-score campaign is not claimed. Cancellation and injected transport
faults apply and are tested. Concurrent provider edits, atomicity and durable recovery
are not implemented or proved; no local scheduling test can substitute for those
provider/caller contracts. Migration tests are not applicable (no persistence).
Performance/load gates are not applicable (no changed SLO or execution strategy).
Live chaos is not applicable to the offline gate. Authorization remains caller-owned;
input validation and sanitized uncertain errors are adapter security checks.

The local unit and wheel runs must pass before proposing a Git gate. Independent
review is recorded separately from author checks. Required hosted CI across the
package's Python matrix remains unavailable until a separately authorized Git gate.
No complete HEB-177 acceptance, live write, full work-record workflow, or production
recovery claim follows from this offline slice.
