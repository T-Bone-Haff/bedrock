═══ RELAY 08 · AMENDMENT 3 — §7/§5/§9 coherence pass, before the commit ═══

Your T7 is upheld in full. All five findings are real, all five were introduced by
this pass, and all five were invisible to every instrument the relay carries. An
independent review of the working tree found four of them and MISSED your finding
4 — the §5 guard — which is the most important of the set.

Apply the seven edits below, then RE-RUN T7 on the corrected file and report
again. A fix pass is exactly when this defect class is introduced; the second use
pass is not ceremony.

Same rules as relay 08. Verify each FROM verbatim on disk, exactly once, before
editing. STOP on any mismatch. <LANDING_DATE> remains 2026-08-04 by operator
override. Touch only register.md. Do not commit.

───────────────────────────────────────────────────────────────────────────
A3-1 · BLOCKING · §5 — the guard names its neighbour instead of its subject
(your finding 4)
───────────────────────────────────────────────────────────────────────────

FROM:

*(The `sofia-dev-he` restatement above is a different correction and a smaller one —
+$95 on a $635 base, and for a different reason. The two sat adjacent here from
2026-07-28 to 2026-08-04, and in that position the paragraph above read as describing
the one below it. Nothing had changed in either. **New text can make old text false
without altering a byte of it**, and no hash, pre-state check or diff statistic sees
it — only reading the rendered page does. §9 carries the general form.)*

TO:

*(**The paragraph above describes the Anthropic correction of 2026-07-27 and nothing
else.** Two other restatements now sit between it and the totals — `sofia-dev-he`
at +$95 on a $635 base, and GoDaddy at +$32.50 — and neither is its subject. This
guard is stated as a subject rather than as a position because **it has now been
defeated once by the very defect it guards against.** From 2026-07-28 to 2026-08-04
the `sofia-dev-he` restatement sat directly above "roughly doubled" and was misread
as its referent; the guard was written to stop that, and it disambiguated by naming
the paragraph it was then adjacent to. On 2026-08-04 the GoDaddy restatement was
inserted into that same position, inherited the same misreading, and **the guard
did not reach it** — because a guard that names a neighbour expires the next time a
neighbour arrives. Nothing changed in any of the three paragraphs. **New text can
make old text false without altering a byte of it, and so can new text placed
between two old ones.** No hash, no pre-state check and no diff statistic sees this.
Only reading the landed file does. §9 carries the general form.)*

───────────────────────────────────────────────────────────────────────────
A3-2 · BLOCKING · §7 Timing — contradicts §7's own Render paragraph
(your finding 1)
───────────────────────────────────────────────────────────────────────────

FROM:

slack; the freshness banner on `/cost` is what actually guarantees a stale page
is legible, because a *skipped* run cannot be outrun by any start time.

TO:

slack. **A *skipped* run cannot be outrun by any start time**, so the margin is not
the guarantee — the guarantee has to be the page stating how old its data is.
`/cost` has no such control today, which is why item 18 carries one. The retired
Cloud Run banner supplied it; the static page does not, and until item 18 lands
this slack window protects nothing that a reader can see.

───────────────────────────────────────────────────────────────────────────
A3-3 · BLOCKING · §7 Deploys — reads as current publication guidance for /cost
(your finding 3)
───────────────────────────────────────────────────────────────────────────

FROM:

**Deploys are setup-time, not runtime.** The service is published by

TO:

**Deploys are setup-time, not runtime — and this paragraph is about the
`ops-surfaces` service, not about how `/cost` is published.** The service is
published by

───────────────────────────────────────────────────────────────────────────
A3-4 · MATERIAL · §7 Stage order — states the superseded plan as the plan of record
(your finding 2)
───────────────────────────────────────────────────────────────────────────

FROM:

**Stage order.** (1) register + dashboard ✅ · (2) Anthropic API pull ✅ ·
(3) GCP billing export and Aura · (4a) private hosting · (4b) collector renders.

TO:

**Stage order.** (1) register + dashboard ✅ · (2) Anthropic API pull ✅ ·
(3) GCP billing export and Aura · (4a) private hosting ✅ · (4b) ~~collector
renders~~ **superseded — see §8 items 9 and 18.**

───────────────────────────────────────────────────────────────────────────
A3-5 · MATERIAL · §9 staleness note — present tense about a retired control
(your finding 5)
───────────────────────────────────────────────────────────────────────────

FROM:

  `cost_stale_after_days=8`, `sofia_stale_after_days=None`. The spurious
  `/sofia` warning that would have begun on 2026-08-01 will not occur.

TO:

  `cost_stale_after_days=8`, `sofia_stale_after_days=None`. The spurious
  `/sofia` warning that would have begun on 2026-08-01 will not occur.
  **Bound to the retired route 2026-08-04:** every claim in this note describes the
  Cloud Run service, which no longer serves `/cost` — see §7. The page a reader
  means by `/cost` is static and has no freshness control at all until item 18
  lands. This note now records a control that worked, not one that is running.

───────────────────────────────────────────────────────────────────────────
A3-6 · COSMETIC · §9 derived-percentage note — cites figures this commit restates
(your "minor")
───────────────────────────────────────────────────────────────────────────

FROM:

  was computed from 635.50 / 651.50, while this file's own figures gave
  733.94 / 746.94. **Both round to 98%.** The dollars beside it were wrong by

TO:

  was computed from 635.50 / 651.50, while this file's figures at that moment —
  before the GoDaddy line landed later the same day — gave 733.94 / 746.94.
  **Both round to 98%. So does 766.44 / 779.44 after GoDaddy**, which makes the
  point three times rather than weakening it. The dollars beside it were wrong by

───────────────────────────────────────────────────────────────────────────
A3-7 · MATERIAL · §8 item 15 — forward pointer for the two statements you flagged
as pre-existing
───────────────────────────────────────────────────────────────────────────

Your read is better than the review's here. Item 10 and §9's token note are true of
the Cloud Run *routes* and misleading about the *pages*, and the page a reader means
by `/cost` is unaffected by that PAT. They are recorded rather than patched, because
item 17 retires both.

FROM:

Decide the posture deliberately and record what is being trusted | operator | — |

TO:

Decide the posture deliberately and record what is being trusted. **Two statements elsewhere were falsified by that same move and are deliberately not corrected here:** item 10 says an expired PAT means "both pages fail", and §9's token-expiry note says the PAT serves `/cost` and `/sofia`. Both are true of the Cloud Run *routes* and misleading about the *pages* — the page a reader means by `/cost` is static and does not touch that token. They retire with item 17 rather than being patched now | operator | — |

───────────────────────────────────────────────────────────────────────────
AFTER APPLYING
───────────────────────────────────────────────────────────────────────────

R1. Re-hash §4. Still 3da912987a7efac0893038500d884b23f8dc5a54393e441f0a4617afe37caf37.
    None of these edits go near it.

R2. RE-RUN T7 in full. Read the landed file as a document, not as a diff. You are
    looking for the same class again — text made false or misleading by a new
    neighbour. Pay particular attention to §5 and §7, which have now been edited
    twice in one session, and to anything adjacent to what A3-1 through A3-7 moved.
    An empty finding list is a valid report; not looking is not.

R3. Append this paragraph to the proposed commit message, immediately before the
    final "Section 4 unchanged" line. Verbatim:

```
A section 7 and section 5 coherence pass, folded in rather than deferred. The
first draft of this commit introduced five instances of the defect this file
already carries a note about: text made false or misleading by new text placed
beside it, with no byte of it changing. Section 7 contradicted itself about
whether /cost has a freshness control, its stage order still named the plan
that item 9 supersedes, and its deploy paragraph read as current guidance for a
page it does not publish. Section 9's staleness note described a live control
on a page that no longer has one. And the section 5 guard written on 2026-08-04
to stop "the total roughly doubled" being misread was itself defeated: it
disambiguated by naming the paragraph it was adjacent to, a new restatement was
inserted into that position, and the guard did not reach it. It now names its
subject instead of its neighbour. Every anchor matched and every hash agreed
through all five; only reading the landed file found them.
```

R4. Report at Gate 1 again. Nothing is committed until the operator's explicit go
    on the corrected file.
