# Anthropic Python Profile

This optional profile binds the portable `agent-code` contract to Python 3.11+ and the official Anthropic SDK using the Messages API. It does not change the portable requirements.

- Reuse a configured async client; obtain credentials from the environment; never log or artifact them.
- Prefer Anthropic's currently supported native structured-output/tool-schema capability when the chosen model and endpoint advertise it. Otherwise use the portable whole-payload and bounded-salvage seam.
- Treat `stop_reason`, usage, cache usage, request id, and content block types as provider data to normalize into the portable execution record. Unknown block or stop-reason variants fail closed until supported.
- Accumulate streamed blocks completely before schema validation. Tool-use ids are the correlation authority for matching `tool_result` blocks.
- Provider retries are disabled or bounded so the application can account for every physical attempt inside its aggregate budget. If SDK-internal retries remain enabled, expose and count them; an invisible retry is nonconforming.
- Cache controls, model identifiers, token accounting, and provider error classes are profile details. Circuit breakers and retry posture remain workload declarations, not universal Anthropic rules.

FastAPI correlation/configuration conventions apply only when the host is a FastAPI service; they are not requirements for scripts, workers, or other hosts.
