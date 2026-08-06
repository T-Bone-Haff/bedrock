# Rescue corpus manifest — handoff-artifact verification work

Frozen 2026-08-05, BEFORE any resolver design exists, so the answer key
cannot be authored to fit. Ten artifacts: NINE are the only surviving copies
of a relay; the tenth, rbt-100-execution-relay, is retained as a known-clean
control and DOES survive elsewhere (it is this leg's own, already landed).

ONLY-SURVIVING-COPY — the population, stated because the first version of this
line overstated it. This surface checked SOFIA, bedrock, ops and vault. The
RBT-93 drain surface independently checked SOFIA, HE-Bedrock, bedrock and vault.
NEITHER arm is complete; the union is, and it is the union that supports the
claim. HE-Bedrock was reachable only from that surface, ops only from this one.

This manifest excludes itself: a manifest cannot pin its own bytes,
because writing the pin changes them.

Plan of record: project doc claude/handoff-artifact-verification-plan.md

| bytes | sha256 | artifact |
|---|---|---|
| 20488 | b30002f933c7b20be65df16253b6183b838f61d6b9ea7e9289fbd67357296b72 | rbt-100-execution-relay.md |
| 23629 | 948536d932400759422377d3d44b623a4457318d61d7ade7d3ad1a3bff2a8165 | rbt-64-stage4a-relay-02-build.md |
| 14943 | eeeac07a21ce3114fecea967b004e95cf1e1ce5dec1b20876888099c58bc5bc0 | rbt-64-stage4a-relay-03-deploy-verify.md |
| 11744 | 143116f8545a0f1e84aba2639a56dc3550e73151c42d3f960d01ae7ea59b19ac | rbt-93-relay-08-amendment-3.md |
| 10452 | 5697c546c7a860ac3eaf3415da0ef42e2926545ab65371ac3de40e2c2e45e078 | rbt-93-relay-08.md |
| 13189 | 78ca9e0e215fec5b2719e239a43fa911ac41c2964cbd1be92aaa6a57516b822c | relay-10-two-commits-r2.md |
| 11381 | 25b37573ce9a5bb8bff0184ee7f48d37386f00c8a8ee81ba6d236e7dd318ee20 | relay-10-two-commits.md |
| 8962 | 5e19fcffa29a72e62398a7497604aefc37359a8a29f640d5591e705aeae2766d | relay-heb-86-amend.md |
| 15087 | 850d47a72e96ef3645719dafdae0f96c998b52e9eb740fdf08624544348f5aa8 | relay-heb-86-landing.md |
| 8895 | 60ca8a57fdbece46d62b7e00e6a46729aac9e0325ddfde6b111fab0e447ebd89 | relay-sofia-handoff-record.md |
