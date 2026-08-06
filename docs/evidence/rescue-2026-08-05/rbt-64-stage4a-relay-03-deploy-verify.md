# RBT-64 stage 4a — RELAY 03: DEPLOY, VERIFY, LAND THE REGISTER

**Posture: GATED TRANSACTION.** Three gates. **STOP at each and wait for the
operator's explicit go.** Running past a gate is never licensed. The operator may
elect at a gate to batch-authorize a named span; halt-on-anomaly is retained in
full inside any batch, and any anomaly voids the remainder.

**This relay supersedes Relay 02 in full.** Relay 02's Phases 0–3 are complete;
its remaining phases are restated here with every amendment already folded in.
Do not work from Relay 02 for anything below.

---

## ═══ FRESH-FETCH GUARD ═══

You are Claude Code on the operator's machine, working
`/Users/thaffey/Documents/GitHub/ops`. This is an EXECUTION request relayed by
the operator from the claude.ai design surface.

**Re-read from disk. Do not trust this prompt's summary of any of it:**

- `hosting.yaml` — the deploy authority. If it and this relay disagree on a
  value, **`hosting.yaml` wins and you flag it.**
- `deploy.sh` — read it before running it.
- `register.md` §1, §2.1, §4, §5, §7, §8, §9.
- `/Users/thaffey/Downloads/rbt-64-register-edits-v0.7.0.md` — SHA-256
  `6b0c71babf0ca0595e56dc10a0dfa45d940071f2c8d7c40c94e4b48f0621a139`.
  **If the hash differs or the file is absent, STOP** — do not reconstruct it.
- The `bedrock:application-code` skill, if you touch service code.

### Identity gate

```bash
LC_ALL=C gcloud config get-value account
LC_ALL=C gcloud projects describe ops-he --format='value(projectId)'
LC_ALL=C git -C . rev-parse --abbrev-ref HEAD
LC_ALL=C git -C . rev-parse HEAD
LC_ALL=C git -C . ls-remote origin main
```

**Required:** account `tad@haffeyenterprises.com` · `ops-he` reachable · branch
`main` · local HEAD **== remote main == `7807c115259bbf06aa84630a8497c808fa01bda6`**.
**Any mismatch: STOP.** Do not switch identity and do not fast-forward yourself.

**The identity split is deliberate and is not a defect** — flag it if you like,
but do not correct it. GCP acts run as `tad@haffeyenterprises.com`; git commits
are authored `T-Bone-Haff <tad@tadhaffey.com>`, matching every prior human commit
in this repo; the GitHub PAT was minted under the personal identity because it
owns the org. All three are recorded on HEB-84.

### Carried state — claims to verify, not context to trust

| Item | Value |
|---|---|
| Project / number | `ops-he` / `773579591723`, org root, billing linked |
| Org ID | `841579372972` (`haffeyenterprises.com`, `C01znhwpi`) |
| Published HEAD | `7807c115259bbf06aa84630a8497c808fa01bda6` |
| `register.md` blob | `ae3ca91110681cc8a65ce2e28acca463f0b70bac` — untouched |
| **§4 invariant** | `e62b11dc75335efac320d0e1d56d1a379844934a79f0b46f7c9a652c33cead54` |
| `dashboard.html` SHA-256 | `1ce4866dfd450ef2e03f0dee06bc5640d4c6464911a080b2cfa87f0903175283` |
| Secret | `github-content-pat` **exists**, version 1, user-managed / `us-central1` |
| PAT expiry | **2027-07-28** · reminder `trig_015Yem4wGZa4xXmoSvCy4w4y` fires 2027-06-28 |

**Two org policies constrain everything below:**

- **`gcp.resourceLocations` — ENFORCED**, us-central1/us-central2 families only.
  This bit once already: `--replication-policy=automatic` places a secret in
  `global` and was rejected. **It governs every regional resource, not just
  Cloud Run.** If any command below creates something with a location, check it.
- **`iam.allowedPolicyMemberDomains` — ENFORCED** at `[C01znhwpi]`. A grant to
  any principal outside that directory — including `tad@tadhaffey.com` — is
  rejected outright. **There is no fallback grant. Do not attempt one.**

---

## ═══ TASK ═══

### PHASE 4 — Provision and deploy

#### 4.0 — Verify the secret. Do not create it.

The operator created the container and added version 1 **ahead of this gate**,
because the token was sitting in a volatile clipboard and a round-trip risked
losing a one-time credential. **Verify, do not create.**

```bash
LC_ALL=C gcloud secrets describe github-content-pat --project=ops-he \
  --format='value(name,replication.userManaged.replicas[0].location)'
LC_ALL=C gcloud secrets versions list github-content-pat --project=ops-he
```

Expect one ENABLED version, replication `us-central1`. **Never read the value.**

Then correct `hosting.yaml`, which records a provisioning fact that did not
happen. A `[PROVISION]` section stating something untrue is precisely what that
annotation exists to prevent:

```yaml
  replication: user-managed
  locations: [us-central1]
  # `automatic` places the secret in `global`, which
  # constraints/gcp.resourceLocations rejects org-wide. Co-located with the
  # service that reads it.
```

Working-tree edit only. It commits in Phase 6.

#### 4.1 — Runtime service account

Cloud Run's default runtime identity is the Compute Engine default SA, which
holds **Editor on the project** — far more agency than a two-route HTML fetcher
should have.

```bash
LC_ALL=C gcloud iam service-accounts create ops-surfaces-run \
  --project=ops-he --display-name="ops surfaces — Cloud Run runtime"

LC_ALL=C gcloud secrets add-iam-policy-binding github-content-pat \
  --project=ops-he \
  --member=serviceAccount:ops-surfaces-run@ops-he.iam.gserviceaccount.com \
  --role=roles/secretmanager.secretAccessor
```

`secretAccessor` **on that one secret** is its entire authority. Nothing
project-wide. `disableServiceAccountKeyCreation` is enforced org-wide — that
blocks service-account **keys**, not service accounts. **No key is minted
anywhere in this build.** If a step appears to want one, STOP: that is a design
error, not a permission to request.

#### 4.2 — Materialise the IAP service agent, and read its address

```bash
LC_ALL=C gcloud beta services identity create \
  --service=iap.googleapis.com --project=ops-he
```

This provisions the agent deterministically **and returns its email. Use the
returned address.** Do not build it from a string template — this build has
twice been bitten by trusting a label instead of reading the thing.

#### 4.3 — Deploy

```bash
./deploy.sh --dry-run    # read the command it prints before running it
./deploy.sh
```

**Do not hand-type a `gcloud run deploy` invocation.** Every value comes from
`hosting.yaml`; that is the entire point of the file.

#### 4.4 — The two IAM grants

```bash
LC_ALL=C gcloud run services add-iam-policy-binding ops \
  --project=ops-he --region=us-central1 \
  --member=serviceAccount:<IAP_AGENT_FROM_4.2> \
  --role=roles/run.invoker

LC_ALL=C gcloud iap web add-iam-policy-binding \
  --project=ops-he --region=us-central1 \
  --resource-type=cloud-run --service=ops \
  --member=user:tad@haffeyenterprises.com \
  --role=roles/iap.httpsResourceAccessor
```

**Read both policies back** rather than trusting the binding commands' success.
A grant violating `allowedPolicyMemberDomains` fails, and the failure must be
legible.

#### 4.5 — Prove `hosting.yaml` actually governs

**This check exists because the fix for the config-homing defect is itself
vulnerable to that defect.** If an env-var name were wrong, pydantic would fall
back to its default — and the defaults are correct — so the pages would render
perfectly while `hosting.yaml` governed nothing. "It rendered" is evidence the
defaults are right, which was never in doubt.

```bash
LC_ALL=C gcloud run services describe ops --project=ops-he --region=us-central1 \
  --format='value(spec.template.spec.containers[0].env)'
```

**All eleven must be present on the revision:** `OPS_SURFACES_GCP_PROJECT_ID`,
`GITHUB_PAT_SECRET_NAME`, `COST_{OWNER,REPO,REF,PATH}`,
`SOFIA_{OWNER,REPO,REF,PATH}`, `STALE_AFTER_DAYS`. Report the count and any
missing name.

> ### ⛔ GATE 4 — report and STOP.
> Service URL · deployed revision · the IAP agent address as returned · both
> IAM policies read back · the eleven env vars. Nothing is verified as working
> yet — that is Phase 5.

---

### PHASE 5 — Verification. This is the point of all of it.

#### 5.1 — Unauthenticated, from the shell. No cookies, no credentials.

```bash
URL="$(LC_ALL=C gcloud run services describe ops --project=ops-he \
  --region=us-central1 --format='value(status.url)')"
LC_ALL=C curl -sS -o /dev/null -w '%{http_code} -> %{redirect_url}\n' "$URL/cost"
LC_ALL=C curl -sS -o /dev/null -w '%{http_code}\n' -L "$URL/cost"
```

**Expect a redirect to Google sign-in, or 403. Never the page.** A 200 carrying
content here is a live exposure — stop and report at the top of your output.

#### 5.2 — The operator clicks

In the Chrome profile signed in as `tad@haffeyenterprises.com` (verified
2026-07-27, single-account, `authuser=0`). Ask him to confirm each:

1. `/cost` renders, showing verified total **$635.50** and Anthropic **$343.61**.
   **Visual check only** — `$635.50` is computed in-browser from `const DATA` and
   does not exist as literal text in the source. A grep for it will fail; that is
   expected, not a defect.
2. The freshness banner names the source commit and shows a plausible age.
3. `/sofia` renders the status page with its own banner.
4. **`/readyz`** reports the secret read and both upstreams reachable.
   **Not `/healthz`** — house convention reserves that for liveness with no I/O.
5. He bookmarks `/cost` in that profile and re-opens it from the bookmark.

#### 5.3 — Byte-level. A tool's report is not the artifact.

```bash
LC_ALL=C git show origin/main:dashboard.html | shasum -a 256
```

Compare against the served page **with the injected banner removed** — the
banner carries `data-ops-surfaces-banner="1"`, which makes it mechanically
strippable. Expect
`1ce4866dfd450ef2e03f0dee06bc5640d4c6464911a080b2cfa87f0903175283`.

Metadata, status codes and success messages have each been individually correct
and individually useless in this estate. The bytes are the only thing that talks
about the artifact.

> ### ⛔ GATE 5 — report and STOP.
> Every check with its actual output. **Retire nothing.** The weekly render
> trigger `trig_015vzZzj57MGzntFRV3PE2YB` and the Cowork artifact
> `haffey-cost-register` retire only after this gate passes, and that is the
> operator's act on a different surface.

---

### PHASE 6 — Register v0.7.0, one coherent pass

Apply **all eight blocks** from
`/Users/thaffey/Downloads/rbt-64-register-edits-v0.7.0.md`, plus the four
additions specified inside it, plus:

- **Block 2 fill-slot resolved** — `ops-he` exists; add it to both §2.1 tables.
- **Block 7 fill-slot resolved** — `<PAT_EXPIRY_DATE>` = **`2027-07-28`**. Add
  that the T−30 reminder is live as `trig_015Yem4wGZa4xXmoSvCy4w4y`, firing
  2027-06-28.
- **New rows in §2.1** for `gen-lang-client-0426926761` (personal estate) and
  `orbital-citizen-492521-i1` (corporate estate), both billing-disabled.
- **Narrow §2.1's completeness wording to *billed* projects.** "Zero unknown
  lines" holds for cost lines and did not hold for the project inventory; the
  register must not blur the two.
- **New Block 9** — §8 item 2 gains a pointer to **HEB-84** for disposition,
  keeping its cost framing here.
- **`ops-he` meter note:** record that the project carries GCP's default API
  surface (31 services at creation, none billing at rest), so a future reader
  does not rediscover it as an anomaly.

#### ⚠️ THE §4 INVARIANT — the hardest guard in this relay

§4 belongs to the collector. Hand-authoring the register has silently reverted a
committed collector row **twice**. Prove you did not:

```bash
LC_ALL=C awk '/^## 4\./{f=1} /^## 5\./{f=0} f' register.md | shasum -a 256
```

**Before and after. The two hashes MUST be identical**, and both must equal
`e62b11dc75335efac320d0e1d56d1a379844934a79f0b46f7c9a652c33cead54`. If they
differ by a single byte, **revert the register edit entirely and STOP.** Do not
attempt to repair §4 — you own none of it.

> ### ⛔ GATE 6 — report and STOP. **Do not commit.**
> Git transactions are the operator's. Report `git status`, the full `git diff`,
> the §4 hashes side by side, and `register.md`'s whole-file SHA-256 before and
> after. Stage by explicit path only — never `git add -A`, `-a`, or `.`

---

## ═══ STOP GATE ═══

**Touch only:** `register.md` (**§1–3 and §5–9 only**) · `hosting.yaml` ·
`service/**` only if a Phase 5 failure requires it.

**Nothing in `Haffey-Enterprises/SOFIA` is touched.** `/sofia` reads that repo;
this relay does not write to it.

**GCP mutations** are permitted only in Phase 4, and only after Gate 4's
preceding step. **No commit, no push, no PR, no merge.**

**Secrets:** never printed, echoed, redirected, written to a file, or passed as a
CLI argument. Redact and say what you redacted.

---

## ═══ MUTATION RIDER ═══

- **Verify each stated FROM before editing.** `register.md` against blob
  `ae3ca911…`; `dashboard.html` against its SHA-256; every carried-state value in
  the guard. **Any mismatch: STOP — do not reconcile by guess.**
- **Adjust-and-flag license — one, narrow, fresh for this relay:** if a `gcloud`
  invocation here uses a flag or surface the installed SDK (571.0.0) has renamed
  or moved, you may adapt it to achieve the stated intent, and **you must flag
  every adaptation** with the original and the substitute. **Syntax only.** It
  does not extend to any ratified value — project, region, principal, instance
  limits, auth flags, replication location — and it does not extend to skipping
  a verification. **Spent at Gate 6.**
- **Everything else: STOP on discrepancy.**
- **Never filter an IAM policy by member address.** `projectCreator` is held via
  a `domain:` binding, which a member filter structurally cannot match — it
  returns empty, and empty reads as absent. **Read whole policies and search
  them.**
- **Reading before landing is sanctioned, not instruction-creep.** A hash proves
  the bytes are the ratified bytes; it says nothing about whether they are sane
  to land. Anything the read surfaces is gate input, **never a licence to edit**.
- **Refusal with reasons is a sanctioned output.** Relay 01's refusal to render
  a verdict, 01b's refusal to widen posture for a POST, and Gate 2's refusal to
  pick between two contradicting artifacts were each the most valuable thing that
  pass produced. If a phase is mis-scoped, say so rather than forcing it through.
- **A green result is not a result.** Six times this build an instrument that
  could not reach its subject returned something that read like an answer — a
  vacuous `diverged: false`, an IAM filter that could not match, a subcommand
  that did not exist, a grep of the wrong file, a Chrome read that failed as "not
  running", and a SHA-256 of empty input. **Every one was caught by checking the
  result rather than the report.** Report actual commands and actual output,
  verbatim. A completion narrative is data to be verified, never a verdict that
  discharges verification.
