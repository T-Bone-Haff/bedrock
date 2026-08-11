# Media, permissions, and runtime capabilities

## Capability state

Feature-detect the API and secure-context preconditions before calling it.
`navigator.mediaDevices` is secure-context restricted and may be absent where
the feature is unavailable; reading a missing property does not itself throw.
Method calls reject for permission, constraints, device, policy, or runtime
reasons that are not interchangeable.

Model only observable state: `unsupported`, `unavailable`, `prompt`, `granted`,
`denied`, `active`, `ended`, `failed`, or an explicitly `indeterminate` outcome
as the capability warrants. Browsers may collapse dismissal, timeout, or denial
into the same observable result; never invent user intent. A stored permission
state does not guarantee the operation will succeed.

Permission requests occur from a user action when the platform requires or the
privacy risk warrants it. Scope the request error separately from setup/runtime
errors so application defects are not reported as user denial.

## Ownership and concurrency

Do not universalize one live session. Declare limits from resource cost,
platform constraints, user intent, privacy indicators, contention, and product
policy. Each session owns its tracks/nodes/listeners/transport and releases them
on failure, stop, replacement, navigation, and unmount. Multiple `getUserMedia`
calls and multiple streams are legitimate when the declared policy supports
them.

Static playback, capture, recognition, synthesis, peer/stream transports, and
background processing are different lifecycles. Each declares retry/reconnect,
backpressure, visibility/background behavior, privacy indication, and alternate
modality. An unavailable modality falls back to a real alternative, never a
simulation that reports false success.
