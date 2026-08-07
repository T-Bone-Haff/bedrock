# Post-freeze evidence package — manifest

Package: docs/evidence/rescue-2026-08-05-post-freeze/ — 13 content files.

Rows 1-11 are the five post-freeze evidence items that survived un-versioned
in ~/Downloads/Rescue/ after the 2026-08-05 corpus freeze and the 2026-08-06
corpus landing (merge b57979ae). Rows 12-13 were added at the close of the
RBT-93 item 18 publish leg; see "Addition — 2026-08-06" below.

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
| 12 | cost-index-captured-2026-08-06.html | acd3485fdd142323c6fb32db4309dec6144a4bd10e8d8a5cce5ab6e14d9f6a6a | 21400 |
| 13 | ftp-jail-check.py | 6e0765fbf631f805fe80b92862e776df4294112ac9eec5d467e1e81c2d08f0c7 | 6470 |

Row 12 carries the same sha256 as row 4. That is not an error — see the
Addition below, where it is the point.

Row 13 is tracked mode 100755. It is a runnable probe, not a document.

Descriptions for rows 1-11 live in CORPUS-ADDENDUM-post-freeze-2026-08-05.md
(authored 2026-08-05 at build-leg close): relays 09/10 are the only artifacts
carrying Block 0's first-trial tables; relay 10's Block 0 count defect (18
rows beneath "TWO of seventeen") is preserved as executed, deliberately; the
cost-index HTML is a reconstruction, not a retrieval — the only copy of what
the first publish overwrites; the seven superseded payloads are the only
bytes that can reproduce the B3 finding's four ruff errors. That third
description is SUPERSEDED as of 2026-08-06; see the Addition.

Cross-pins verified at manifest authoring (2026-08-06, deliberation surface,
over device-bridge staged copies; byte counts cross-checked against the
device-side listing 11/11): the addendum's own table 3/3 MATCH (rows 2-4);
the subdirectory's SHA256SUMS.txt 6/6 MATCH (rows 6-11). The addendum and
the SHA256SUMS.txt are pinned only here (rows 1, 5).

## Addition — 2026-08-06, the RBT-93 item 18 publish leg

Two files added at the close of the publish leg. Rows 1-11 are untouched and
their hashes are unchanged.

**Row 12 — cost-index-captured-2026-08-06.html.** The deployed
`/cost/index.html` retrieved through the authoritative channel by the
renderer's `--capture-existing`, which RETRs the live file immediately before
the first STOR. This is the retrieval row 4 records as never having been
performed.

**It is byte-identical to row 4** — same sha256, same 21,400 bytes. So the
reconstruction was right: the rebuild from `ops:dashboard.html`, the ETag
`0x5398` corroboration and §7's recorded figure all agreed with what the
server actually held. That agreement is the finding, and it is why both files
are kept rather than one.

**What row 12 does not prove.** Because the two files are byte-identical,
neither can establish its own provenance by hash — hashing row 12 returns the
number row 4 already had. The evidence that row 12 arrived by RETR rather
than by reconstruction is this paragraph and the publish record, not the
bytes. A later reader who diffs the two files, finds nothing, and concludes
one is redundant has it backwards: **the duplication is the result.**

**Supersession, stated rather than edited in.** The addendum's qualifier for
row 4 — "It has never been retrieved through the authoritative channel" — was
true when authored on 2026-08-05 and is false as of 2026-08-06.
CORPUS-ADDENDUM-post-freeze-2026-08-05.md is NOT amended: it is dated at the
build-leg close and correcting it there would back-date it, which is the same
reason relay 10 keeps its broken row count. The supersession lives here.

**Row 13 — ftp-jail-check.py.** The read-only FTPS probe run as measurement
M4 on 2026-08-06 against the rotated credential. It prints PWD, the NLST
reply verbatim as `repr` so slashes and whitespace are visible, LIST, the
peer certificate issuer as a known-value transport control travelling inside
the same measurement, and what three candidate basename rules make of each
entry. It settled two design questions that had until then been argued from
reasoning rather than measured: the severity of defect N2, and whether the
positive half of the jail gate was safe to adopt.

It is preserved as a **method, not an artifact.** The reading it produced
decays — an NLST against a live GoDaddy account stops being re-derivable if
the account is re-hosted — so this script is the only thing that can retake
it.

Credential handling, since the file is now public to anyone with the repo:
`getpass` only, never in argv, never in an environment variable it sets, no
verbose flag anywhere, and nothing written, uploaded, renamed or deleted. The
one piece of infrastructure it names, the FTPS host, is already committed in
this same package at `relay-09-payloads-superseded/render_cost.py:56`, so
landing it discloses nothing new.

Verification of rows 12-13 (2026-08-06, deliberation surface, over the device
bridge): both hashed on the device after placement and both `cmp`-clean
against their sources in `~/Downloads`; row 12 additionally `cmp`-clean
against row 4. The content-file count in the opening line was updated behind
this addition — 11 to 13 — because relay 10's preserved defect in this same
package is a row added without its count following it.

This manifest is pinned by the landing relay, not by itself. The 2026-08-06
addition is pinned by the relay that lands it, on the same terms.
