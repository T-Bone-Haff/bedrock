# Rescue addendum — artifacts deposited AFTER the freeze

**These two artifacts are NOT part of the frozen corpus.** `CORPUS-MANIFEST.md` states it was
frozen 2026-08-05 *before any resolver design exists, so the answer key cannot be authored to
fit*. Appending to it after the fact would break exactly that property, so it has not been
touched — its ten rows and its "NINE are the only surviving copies" count both stand as
written and remain accurate for the population it froze.

These two are deposited here for **preservation only**, and whether they should ever join the
frozen population is the operator's call, not this surface's.

| bytes | sha256 | artifact |
|---|---|---|
| 18709 | b6d1539f7331302d9df6c3dc2e5136c0d9f631fb01c56c1567fecd3ce6892eba | RELAY-rbt93-item18-renderer.txt |
| 17512 | b0a67623d8a550c81b4f66aa8209dd834da332ed4ef2ecf2baeaa4fcd9717c0f | RELAY-10-rbt93-item18-review-fixes.txt |
| — | see `relay-09-payloads-superseded/SHA256SUMS.txt` | `relay-09-payloads-superseded/` (7 files) |
| 21400 | acd3485fdd142323c6fb32db4309dec6144a4bd10e8d8a5cce5ab6e14d9f6a6a | cost-index-deployed-2026-08-05.html |

Hashes measured on disk in `Rescue/` after the move, and the two relay files equal the pins the
executor verified before running them.

## `cost-index-deployed-2026-08-05.html` — the artifact the next step destroys

**The deployed `/cost/index.html` as it stood before any renderer touched it**, and the only
copy of what the first `--publish` overwrites.

It is a **reconstruction, not a retrieval**, and that qualifier is load-bearing. GoDaddy injects
454 bytes into every served response, so an HTTP GET cannot yield the on-disk bytes. The file
here was rebuilt from `ops:dashboard.html` by swapping in the deployed comment and removing the
`--space-9` definition, and it hashes to the browser-derived `acd3485f…` at 21,400 bytes —
corroborated independently by the ETag `0x5398` and by §7's recorded figure. **It has never been
retrieved through the authoritative channel**, and the ratified `--capture-existing` RETR before
the first PUT is what would replace this reconstruction with a retrieval.

Two things decay the moment the first publish lands and are observable nowhere else afterwards:
the served page's `V0.6.0` stamp against register v0.10.1, and the `--space-9` padding collapse.
The screenshot and this file are the whole baseline for the use pass that closes RBT-93.

## What they are, and why they are worth keeping

Relays 09 and 10 of the RBT-93 item-18 build leg, 2026-08-05. Both report-and-STOP, both
executed by Claude Code, both landed in `bb1cc2204cdd9f871ecabe9c25ec9c285cd5a6fc`.

**They are the only artifacts carrying Block 0's tables.** Block 0 — the `EXTERNAL ASSERTIONS`
construct proposed on HEB-85 and trialled for the first time on these two relays — produced a
measurement that exists nowhere else in re-derivable form:

- Relay 09: **4 of 25 rows** came from the candidate grep rather than from the author.
- Relay 10: **2 of 17 rows**.
- Both times the grep-surfaced rows were the same shape — **artifacts the relay READS or
  protects, never the ones it writes.**

HEB-85's write-up of that trial is a claim *about these tables*. Without the files it rests on
one surface's summary of a document nobody can re-read, which is the condition
`CORPUS-MANIFEST.md` already records for the 2026-08-05 amendment set — five of that leg's
seventeen reconstructed ledger rows describe defects in an artifact that no longer exists.

## Known defect in relay 10, recorded rather than corrected

Relay 10's Block 0 table carries **18 rows in the order 1–14, 18, 15–17**, beneath a provenance
paragraph reading *"TWO of seventeen."* Row 18 was folded in after the review and the count,
the ordering and the note were not updated behind it. The executor found it before beginning
and reported rather than absorbing it.

**The file is preserved as executed, with the defect in place.** Correcting it now would
destroy the evidence of a defect the ledger cites — and the corrupted figure is the trial's own
metric, which is the whole reason it is worth keeping.

## Provenance

Deposited 2026-08-05 at the close of the build leg, moved from `~/Downloads/` rather than
re-copied from the authoring surface, so these are the exact bytes the executor ran against.


## `relay-09-payloads-superseded/` — and the retrospective claim it falsifies

The seven payload files relay 09 placed, **as they were before relay 10 replaced two of them.**

This directory exists because the wind-down checked a claim the retrospective had already made
and found it false. The retrospective rated the B3 finding — *`gate.yml` as delivered would
have failed on its first CI run, four ruff errors at the pinned 0.16.1* — as **"strongest of
the set: anyone can re-run and reproduce the four errors from committed artifacts alone."**

That is wrong. The committed artifacts carry `_totals`, `_end`, no `# noqa: E402`, and mode
`100755`. **They cannot reproduce a single one of the four errors.** The bytes that can exist
only in these seven files; relay 10 replaced them and git never held them. Verified during the
wind-down: the relay-09 payload still has bare `totals` and still carries the dead `noqa`.

So the strongest-rated proof in the retrospective was the one about to be deleted, and it was
rated strongest *because* the reasoning stopped at "the pins are in the repo" without asking
what the pins point at. **A hash preserved without its subject pins nothing retrievable.**

The finding is worth more than the fix: the retrospective's own question — *does this proof
still exist?* — was answered from a model of the repository rather than from the repository,
and the next step in the sequence is what caught it.
