# Post-freeze evidence package — manifest

Package: docs/evidence/rescue-2026-08-05-post-freeze/ — the five post-freeze
evidence items (11 content files) that survived un-versioned in
~/Downloads/Rescue/ after the 2026-08-05 corpus freeze and the 2026-08-06
corpus landing (merge b57979ae).

NOT part of the frozen commissioning corpus. The V3 commissioning population
is CORPUS-MANIFEST.md's ten relays in docs/evidence/rescue-2026-08-05/,
frozen 2026-08-05 before any resolver design existed. This package lands in
a sibling directory precisely so the frozen package's directory receives
nothing new (operator-ratified 2026-08-06). Whether any item here ever joins
the frozen population is the operator's call.

| # | path | sha256 | bytes |
|---|---|---|---|
| 1 | CORPUS-ADDENDUM-post-freeze-2026-08-05.md | 5a3670366e72bba673f441a6944e6a8676bdbbc9a17a0952c7cc34de0232c4f7 | 5795 |
| 2 | RELAY-rbt93-item18-renderer.txt | b6d1539f7331302d9df6c3dc2e5136c0d9f631fb01c56c1567fecd3ce6892eba | 18709 |
| 3 | RELAY-10-rbt93-item18-review-fixes.txt | b0a67623d8a550c81b4f66aa8209dd834da332ed4ef2ecf2baeaa4fcd9717c0f | 17512 |
| 4 | cost-index-deployed-2026-08-05.html | acd3485fdd142323c6fb32db4309dec6144a4bd10e8d8a5cce5ab6e14d9f6a6a | 21400 |
| 5 | relay-09-payloads-superseded/SHA256SUMS.txt | c429b587632ce6d316c6fe726a30deb8dfad83358b814f03b0bf06fd56d786ad | 500 |
| 6 | relay-09-payloads-superseded/dashboard-slotted.html | 396c0f0ac3aae3efc3645bfea6f2feac3e6ae4ace0b0c4ce8f8a32ae45e82db2 | 18557 |
| 7 | relay-09-payloads-superseded/gate.yml | 4094bd70bc97f3ef7502ae47da61d756805e783cb6c445bfd627d6b5bd8949cf | 2057 |
| 8 | relay-09-payloads-superseded/render-cost.yml | e5c7328ca00e768e26fb47aaab5ce04e5b31958225c27772087b69157a4e1c7d | 2903 |
| 9 | relay-09-payloads-superseded/render_cost.py | 1690765d4cef7d60adfcc9b8560b0a337a1b1a0aaf377586f892d160cec81cda | 38170 |
| 10 | relay-09-payloads-superseded/requirements-dev.txt | 3c9e94d2078f36e3a11d01da42cee795ab08a440b50bda219de1c88a5b72e3b8 | 482 |
| 11 | relay-09-payloads-superseded/test_render_cost.py | 5c5808d2bd06f6bad9ffb608355146ac262218088ae3b4be554208ed74cab5d6 | 20130 |

Descriptions live in CORPUS-ADDENDUM-post-freeze-2026-08-05.md (authored
2026-08-05 at build-leg close): relays 09/10 are the only artifacts carrying
Block 0's first-trial tables; relay 10's Block 0 count defect (18 rows
beneath "TWO of seventeen") is preserved as executed, deliberately; the
cost-index HTML is a reconstruction, not a retrieval — the only copy of what
the first publish overwrites; the seven superseded payloads are the only
bytes that can reproduce the B3 finding's four ruff errors.

Cross-pins verified at manifest authoring (2026-08-06, deliberation surface,
over device-bridge staged copies; byte counts cross-checked against the
device-side listing 11/11): the addendum's own table 3/3 MATCH (rows 2-4);
the subdirectory's SHA256SUMS.txt 6/6 MATCH (rows 6-11). The addendum and
the SHA256SUMS.txt are pinned only here (rows 1, 5).

This manifest is pinned by the landing relay, not by itself.
