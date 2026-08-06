# RBT-64 stage 4a — RELAY 02: BUILD

**Posture: GATED TRANSACTION.** Six gates. **STOP at every one and wait for the
operator's explicit go.** Running past a gate is never licensed. The operator may
elect at a gate to batch-authorize a named span of the remaining gates; that
election is theirs at transaction time and this relay does not pre-authorize it.
Halt-on-anomaly is retained in full inside any batch, and any anomaly voids the
remainder of the batch.

**Authority for this build:** the Relay 01b report (corporate identity). **The
Relay 01 report's GCP and org-policy answers are SUPERSEDED** — that org carries
11 policies against the personal org's 6. If both files are still on disk, 01b
wins on every GCP question.

---

## ═══ FRESH-FETCH GUARD ═══

You are Claude Code on the operator's machine. This is an EXECUTION request
relayed by the operator from the claude.ai design surface.

**Re-read from disk, do not trust this prompt's summary and do not use
prior-session memory:**

- `/Users/thaffey/Documents/GitHub/ops/register.md` — §1 (provenance rules),
  §2.1, §4, §5, §7, §8, §9.
- `/Users/thaffey/Documents/GitHub/ops/.github/workflows/collect-costs.yml`
- The `bedrock:application-code` skill — **the service you are about to write is
  governed by it.** This relay specifies the contract, not the conventions; the
  skill owns the conventions. Where they conflict, the skill wins and you flag
  the conflict.

### Identity gate

```bash
LC_ALL=C gcloud config get-value account
LC_ALL=C git -C /Users/thaffey/Documents/GitHub/ops rev-parse --abbrev-ref HEAD
LC_ALL=C git -C /Users/thaffey/Documents/GitHub/ops remote get-url origin
```

**ACTIVE ACCOUNT MUST BE `tad@haffeyenterprises.com`.** Branch `main`, remote
`Haffey-Enterprises/ops`. **Any mismatch: STOP.** Do not switch identity
yourself.

### Published-state gate

```bash
LC_ALL=C git -C /Users/thaffey/Documents/GitHub/ops rev-parse HEAD
LC_ALL=C git -C /Users/thaffey/Documents/GitHub/ops ls-remote origin main
```

Relay 01 found local **one commit behind** remote. A pin on local HEAD says
nothing about the published state, and this build's whole premise is that the
served content comes from **the remote**. Report both. **If local is behind, say
so and stop before Phase 2** — the operator fast-forwards; you do not.

> **⚠️ AMENDED 2026-07-27 after Gate 0, on the executor's finding.**
>
> **Every FROM pin in this relay is stated against the REMOTE state.** Therefore
> **no FROM verification and no §4 baseline may be captured until local and
> remote have converged.** Capturing the §4 baseline against a behind tree is
> worse than useless: `2228d41` modified `register.md` +1/−0 — a collector §4
> upsert — so a baseline taken at `b589f26` would either falsely fail the
> invariant or, far worse, **falsely pass it against content that no longer
> matches the remote.**
>
> This was an ordering defect in the relay: the guard *reported* divergence where
> it should have *required convergence* before any pin is read. Sequence is:
> converge → then capture baselines → then edit → then re-hash.
>
> A hash captured before convergence may be recorded for the audit trail. It is
> **not** the invariant's "before" value.

### Ratified constants — these are decisions, not defaults

| Setting | Value |
|---|---|
| Project ID | `ops-he` · fallback `haffey-ops-he` if globally taken |
| Project parent | **organization root — no folder.** Not `SOFIA Workloads` |
| Billing account | `0110D5-2FC7E6-C24506` |
| Region | `us-central1` (forced by `gcp.resourceLocations`) |
| Cloud Run service | `ops` |
| Secret | `github-content-pat` |
| IAP principal | `tad@haffeyenterprises.com` **only** |
| `--max-instances` | `2` |
| `--min-instances` | `0` |
| Auth | `--iap --no-allow-unauthenticated` |
| Cron | `0 12 * * 1` → `17 6 * * 1` |

**`iam.allowedPolicyMemberDomains` is ENFORCED at `[C01znhwpi]`.** A grant to any
principal outside that directory — including `tad@tadhaffey.com` — **will be
rejected by org policy.** There is no fallback grant. Do not attempt one.

---

## ═══ TASK ═══

### PHASE 0 — Pre-flight. Measure what was only derived.

Relay 01b **derived** `projectCreator` from a role definition rather than
measuring it, because `testIamPermissions` is a POST and outside a read-only
relay's verb set. Close that floor before creating anything.

```bash
LC_ALL=C gcloud organizations list
```

Confirm exactly one org with `displayName` = `haffeyenterprises.com`; capture its
ID as `<ORG_ID>`. **If displayName differs, STOP.**

```bash
LC_ALL=C gcloud organizations test-iam-permissions <ORG_ID> \
  --permissions=resourcemanager.projects.create
LC_ALL=C gcloud beta billing accounts get-iam-policy 0110D5-2FC7E6-C24506 \
  --format=json | LC_ALL=C grep -c 'billing.admin\|billing.user'
```

**`resourcemanager.projects.create` must come back granted. If it does not,
STOP** — the whole build is blocked and the fix is an IAM grant, not a
workaround.

**Do not filter IAM policies by member address anywhere in this relay.** Relay
01b established that `projectCreator` is held via a `domain:` binding, which a
member filter structurally cannot match — the filter returns empty and empty
reads as absent. **Read whole policies and search them.**

> ### ⛔ GATE 0 — report and STOP.
> Report: active account, org ID and displayName, the `test-iam-permissions`
> result verbatim, local-vs-remote HEAD. Nothing has been created.

---

### PHASE 1 — Project, billing, APIs

```bash
LC_ALL=C gcloud projects create ops-he \
  --name="Haffey Enterprises Ops" \
  --organization=<ORG_ID>
```

**If the ID is globally taken**, retry once with `haffey-ops-he` and **report the
substitution prominently** — it propagates into `hosting.yaml`, the register, and
the bookmark. Do not try a third name; stop and ask.

```bash
LC_ALL=C gcloud beta billing projects link <PROJECT_ID> \
  --billing-account=0110D5-2FC7E6-C24506

for API in run.googleapis.com iap.googleapis.com secretmanager.googleapis.com \
           artifactregistry.googleapis.com cloudbuild.googleapis.com; do
  LC_ALL=C gcloud services enable "$API" --project=<PROJECT_ID>
done

LC_ALL=C gcloud services list --enabled --project=<PROJECT_ID> \
  --format='table(config.name)'
LC_ALL=C gcloud projects describe <PROJECT_ID> \
  --format='value(projectId,projectNumber,parent.type,parent.id,lifecycleState)'
LC_ALL=C gcloud beta billing projects describe <PROJECT_ID>
```

**Verify the result, not the report.** Four tools in this build's history reported
success while storing or running nothing. Confirm from the `list --enabled`
output that all five APIs are enabled, confirm `parent.type` is `organization`
(**not `folder`**), and confirm `billingEnabled: true`.

> ### ⛔ GATE 1 — report and STOP.
> Report: final project ID, project **number** (needed for the IAP service
> agent), parent type/id, billing-enabled state, and the five enabled APIs.

---

### PHASE 2 — Repo authoring. No GCP calls in this phase.

#### 2.1 The service

Create `service/` in `Haffey-Enterprises/ops`. Conform to
`bedrock:application-code`; this relay gives the **contract**, not the style.

**Behaviour contract:**

| Route | Behaviour |
|---|---|
| `/` | Minimal index linking `/cost` and `/sofia`. No data. |
| `/cost` | Fetch `dashboard.html` from `Haffey-Enterprises/ops`, ref `main`; inject the freshness banner; return as HTML |
| `/sofia` | Fetch `docs/design/preview/sofia-landing.html` from `Haffey-Enterprises/SOFIA`, ref **`develop`**; inject the banner; return as HTML |
| `/healthz` | JSON: reachability of both upstreams, secret-read status, service revision. Behind IAP like everything else |

**Fetching.**

- Read the PAT from Secret Manager **via the Secret Manager client library**,
  authenticating as the service's own runtime identity (ADC). **Never** as an
  environment variable containing the value, never written to disk, never logged,
  never in a URL.

> **⚠️ AMENDED 2026-07-27 after Gate 1 — the original relay contradicted itself.**
> Phase 2.1 said "never an environment variable containing the value" while
> Phase 4's deploy sketch carried `--set-secrets=…`, which does exactly that.
> **`--set-secrets` is dropped.** The service calls Secret Manager directly.
>
> **Caching the fetched secret in process memory for the instance lifetime is
> permitted** — the constraint is about exposure surface, not call frequency.
> Consequence to accept knowingly: a rotated secret takes effect on the next cold
> start rather than the next request. With `min-instances=0` and weekly traffic
> that is a non-issue, and rotation still requires **no deploy** — it adds a new
> Secret Manager version and the next instance picks it up.
- **No caching.** Fetch on every request; respond `Cache-Control: no-store`. The
  design's entire freshness claim is "current the moment a commit lands," and a
  cache silently converts that into a lie.
- Use the GitHub REST API, not `raw.githubusercontent.com` — raw does not give
  you the commit metadata the banner needs.
- Two calls per route: the contents endpoint for the bytes, and
  `GET /repos/{owner}/{repo}/commits?path={path}&sha={ref}&per_page=1` for the
  last commit touching that path.

**The freshness banner** — this is a ratified requirement, not decoration.
Injected immediately after the opening `<body>` tag (match `<body[^>]*>`; the tag
carries attributes). It states:

- source `owner/repo@ref` and path
- last-commit short SHA and its ISO-8601 date
- age in human terms — "2 hours ago", "9 days ago"
- fetch timestamp

**If the source commit is older than 8 days, render the banner in a warning
treatment.** The cost register is weekly; anything past 8 days means the
collector was delayed or skipped. **This is the mechanism that makes a stale page
distinguishable from a current one** — without it, a skipped collection is
invisible, and every failure this build has met has been silence rather than
error.

**Errors are named, never bare.** Any upstream failure renders a readable page
stating which upstream failed, the HTTP status, and the likely cause — with
**401/403 explicitly naming a possibly-expired PAT**, since a silently expired
token is the design's identified single point of quiet failure. Never return a
blank 500.

#### 2.2 `hosting.yaml`

Declarative record of the auth posture, at the repo root. Ratified item: *a
setting that exists only in a console is a setting nobody audits.* It carries
project, region, service name, secret name, both source pointers, and the exact
deploy flags from the constants table. `deploy.sh` reads it; nothing is
hand-typed at deploy time.

#### 2.3 Cron

`.github/workflows/collect-costs.yml`: `0 12 * * 1` → `17 6 * * 1`. **Update the
header comment too** — it currently justifies the 12:00 UTC time by ordering
against a 13:00 UTC renderer that is being retired. Replace that rationale with
the real one: a measured 2h24m05s schedule delay against a 09:00 ET read.

#### 2.4 `dashboard.html`

**Do not regenerate it.** The working-tree copy is the v0.6.0 render, SHA-256
`1ce4866dfd450ef2e03f0dee06bc5640d4c6464911a080b2cfa87f0903175283`. **Verify that
hash before staging.** If it differs, STOP — something changed it since the
design surface read it, and pinning over an unexamined change is exactly the
failure this pin exists to prevent.

#### 2.5 Register v0.7.0

Apply the eight blocks in
`/Users/thaffey/Downloads/rbt-64-register-edits-v0.7.0.md`, **plus**:

> **⚠️ AMENDED 2026-07-27 after Gate 0.** The original relay named this file
> without a path and without existence-verification — it had been delivered into
> the conversation and had **never existed on this machine**. That is a premise
> defect on the authoring side, and the executor was right to refuse to
> reconstruct eight ratified blocks by inference. The file is now placed on disk
> at the path above. **Verify it exists and read it whole before applying
> anything; if it is absent, STOP again rather than reconstructing it.**

- **Block 2 fill-slot** — `ops-he` is now real, so add it to both §2.1 tables.
  Use the actual project ID from Phase 1 if it was substituted.
- **New rows in §2.1** for `gen-lang-client-0426926761` (personal) and
  `orbital-citizen-492521-i1` (corporate), both billing-disabled.
- **Narrow §2.1's completeness wording** to *billed* projects. "Zero unknown
  lines" holds for cost lines and did not hold for the project inventory; the
  register must not blur the two.
- **New Block 9** — §8 item 2 gains a pointer to **HEB-84** for disposition while
  keeping its cost framing here.

**⚠️ THE §4 INVARIANT — this is the hardest guard in the relay.**

§4 belongs to the collector. Hand-authoring the register has silently reverted a
committed collector row **twice**. Prove you did not:

```bash
cd /Users/thaffey/Documents/GitHub/ops
LC_ALL=C awk '/^## 4\./{f=1} /^## 5\./{f=0} f' register.md | shasum -a 256
```

**Run this before and after your edits. The two hashes MUST be identical.** If
they differ by a single byte, **revert the register edit entirely and STOP.** Do
not attempt to repair §4 — you own none of it.

Also report SHA-256 of the whole file before and after, and confirm the base
matches git blob `ae3ca91110681cc8a65ce2e28acca463f0b70bac`.

> ### ⛔ GATE 2 — report and STOP. **Do not commit.**
> Git transactions are the operator's. Report: full `git status`, full `git diff`
> for tracked files, a list of new files, the §4 before/after hashes side by
> side, and the `dashboard.html` hash check.
>
> **The operator commits and pushes.** After the push, re-run the published-state
> check and confirm remote `main` carries `dashboard.html` — **the service fetches
> from the remote, so an unpushed commit means `/cost` serves the old render or
> 404s.**

---

### PHASE 3 — The secret. You do not handle the credential.

**The operator creates the PAT** at GitHub → fine-grained tokens: `contents:read`
only, resource owner `Haffey-Enterprises`, repositories `ops` **and** `SOFIA`,
expiry **1 year**. Report the expiry date — it becomes a register §9 line and a
T−30 reminder.

You create the container and the grants:

```bash
LC_ALL=C gcloud secrets create github-content-pat \
  --project=<PROJECT_ID> --replication-policy=automatic
```

**The operator runs the version-add themselves**, so the token never enters your
context:

```bash
gcloud secrets versions add github-content-pat --project=<PROJECT_ID> --data-file=-
# paste token, then Ctrl-D
```

Then verify — **without printing the value**:

```bash
LC_ALL=C gcloud secrets versions access latest \
  --secret=github-content-pat --project=<PROJECT_ID> | wc -c
LC_ALL=C gcloud secrets versions access latest \
  --secret=github-content-pat --project=<PROJECT_ID> | grep -c '^github_pat_'
```

Expect a plausible length and a count of `1`. **A count of 0 or a length near 0
means an empty or malformed secret** — which has happened in this estate before,
reported as success by the storing tool. **Verify the input before storing and
the result after; the storing tool will never tell you.**

> ### ⛔ GATE 3 — report and STOP.
> Report the byte count, the prefix-match count, and the PAT expiry date. Never
> the value, or any part of it.

---

### PHASE 4 — Deploy and IAP

> **⚠️ AMENDED 2026-07-27 after Gate 1. Two additions and one deletion.**

**4.0 — Dedicated least-privilege runtime service account.** Cloud Run's default
runtime identity is the **Compute Engine default service account, which holds
Editor on the project**. That is far more agency than a two-route HTML fetcher
needs, and it would make the service the most privileged thing in `ops-he`.

```bash
LC_ALL=C gcloud iam service-accounts create ops-surfaces-run \
  --project=ops-he --display-name="ops surfaces — Cloud Run runtime"

LC_ALL=C gcloud secrets add-iam-policy-binding github-content-pat \
  --project=ops-he \
  --member=serviceAccount:ops-surfaces-run@ops-he.iam.gserviceaccount.com \
  --role=roles/secretmanager.secretAccessor
```

`roles/secretmanager.secretAccessor` **on that one secret** is its entire
authority. Nothing project-wide. (`disableServiceAccountKeyCreation` blocks
service-account **keys**, not service accounts — creating this SA is compliant,
and no key is ever minted for it.)

**4.1 — Materialise the IAP service agent explicitly, and read its address
rather than constructing it.** The executor correctly anticipated that
`service-773579591723@gcp-sa-iap.iam.gserviceaccount.com` may not exist until IAP
is first used, which would make the Phase 4 binding fail for a timing reason that
looks like a permission fault.

```bash
LC_ALL=C gcloud beta services identity create \
  --service=iap.googleapis.com --project=ops-he
```

This provisions the agent deterministically **and returns its email**. **Use the
returned address.** Do not build it from a string template — that is the same
move as reading a capability instead of the label that usually implies it, and
this build has now been bitten twice by the label.

**4.2 — Deploy.**

```bash
LC_ALL=C gcloud run deploy ops \
  --project=ops-he --region=us-central1 --source=service/ \
  --no-allow-unauthenticated --iap \
  --max-instances=2 --min-instances=0 \
  --service-account=ops-surfaces-run@ops-he.iam.gserviceaccount.com
```

**`--set-secrets` is deliberately absent** — see the Phase 2.1 amendment. The
service reads Secret Manager through its own identity; the value never becomes an
environment variable.

Derive the exact flag set from `hosting.yaml` — **do not hand-type flags here.**
If `hosting.yaml` and this relay disagree, `hosting.yaml` wins and you flag it.

Then the two IAM grants:

```bash
LC_ALL=C gcloud run services add-iam-policy-binding ops \
  --project=<PROJECT_ID> --region=us-central1 \
  --member=serviceAccount:service-<PROJECT_NUMBER>@gcp-sa-iap.iam.gserviceaccount.com \
  --role=roles/run.invoker

LC_ALL=C gcloud iap web add-iam-policy-binding \
  --project=<PROJECT_ID> --region=us-central1 \
  --resource-type=cloud-run --service=ops \
  --member=user:tad@haffeyenterprises.com \
  --role=roles/iap.httpsResourceAccessor
```

The runtime service account also needs
`roles/secretmanager.secretAccessor` on `github-content-pat`.

**`iam.disableServiceAccountKeyCreation` is enforced org-wide** — the service
runs as a service *identity*; **no service-account key is created anywhere in
this build.** If any step appears to want one, STOP: that is a design error, not
a permission to request.

> ### ⛔ GATE 4 — report and STOP.
> Report the service URL, the deployed revision, and the full effective IAM
> policy on both the service and the IAP resource. **Read the policy back rather
> than trusting the binding command's success** — a grant that violated
> `allowedPolicyMemberDomains` fails, and the failure should be legible.

---

### PHASE 5 — Verification. This is the point of all of it.

**Unauthenticated, from the shell** — no cookies, no credentials:

```bash
LC_ALL=C curl -sS -o /dev/null -w '%{http_code} -> %{redirect_url}\n' <SERVICE_URL>/cost
LC_ALL=C curl -sS -o /dev/null -w '%{http_code}\n' -L <SERVICE_URL>/cost
```

**Expect a redirect to Google sign-in or a 403 — never the page.** A 200 with
content here is a live exposure and an immediate stop-and-report.

**Then the operator clicks**, in the Chrome profile signed in as
`tad@haffeyenterprises.com` (verified 2026-07-27). Have them confirm, item by
item:

1. `/cost` renders, and the figures are the **v0.6.0** ones — verified total
   **$635.50**, Anthropic **$343.61**.
2. The freshness banner names the source commit and shows a plausible age.
3. `/sofia` renders the status page with its own banner.
4. `/healthz` reports both upstreams reachable.
5. **Bookmark `/cost` in that profile** and re-open it from the bookmark.

**Byte-level check — a tool's report is not the artifact:**

```bash
LC_ALL=C git -C /Users/thaffey/Documents/GitHub/ops show origin/main:dashboard.html | shasum -a 256
```

Compare against the served page **with the injected banner removed**. They must
match. Metadata, status codes and success messages have each been individually
correct and individually useless in this estate; the bytes are the only thing
that talks about the artifact.

> ### ⛔ GATE 5 — report and STOP.
> Report every check above with its actual output. **Do not retire anything.**
> Retiring the weekly render trigger `trig_015vzZzj57MGzntFRV3PE2YB` and the
> Cowork artifact `haffey-cost-register` is ratified **only after** this gate
> passes, and it is the operator's act on a different surface.

---

## ═══ STOP GATE ═══

**Touch only:**

| Path | Repo |
|---|---|
| `service/**` (new) | `ops` |
| `hosting.yaml` (new) | `ops` |
| `deploy.sh` (new) | `ops` |
| `.github/workflows/collect-costs.yml` | `ops` |
| `register.md` — **§1–3, §5–9 only** | `ops` |
| `dashboard.html` — **stage only, do not modify** | `ops` |

**Nothing in `Haffey-Enterprises/SOFIA` is touched by this relay.** `/sofia` reads
that repo; it does not write to it.

**Stage by explicit path. Never `git add -A`, `-a`, or `.`** — a broad stage
sweeps unexamined working-tree dirt into this operation's commit. Relay 01 found
`dashboard.html` already dirty; assume there is more.

**No commit, no push, no PR, no merge.** Git transactions are the operator's.

**GCP mutations are permitted only inside Phases 1, 3 and 4, and only after that
phase's preceding gate has been released.**

**Secrets:** never printed, echoed, redirected, written to a file, or passed as a
CLI argument. Redact and say what you redacted.

---

## ═══ MUTATION RIDER ═══

- **Verify each target's stated FROM before editing.** `dashboard.html` against
  its SHA-256; `register.md` against git blob `ae3ca911…`;
  `collect-costs.yml` must currently contain `0 12 * * 1`. **Any mismatch: STOP
  and report — do not reconcile by guess.**
- **The §4 invariant is absolute.** Before/after hashes identical, or the register
  edit is reverted whole.
- **Adjust-and-flag license — exactly one, narrow:** if a `gcloud` invocation in
  this relay uses a flag or surface that the installed SDK (571.0.0) has renamed
  or moved, **you may adapt the invocation to achieve the stated intent, and you
  must flag every adaptation** with the original and the substitute. This license
  covers command *syntax* only. **It does not extend to any ratified value** —
  project ID, region, principal, instance limits, auth flags — and it does not
  extend to skipping a verification. **The license is spent at Gate 5** and does
  not survive into a later relay.
- **Everything else: STOP on discrepancy.**
- **Reading before landing is sanctioned, not instruction-creep.** A hash proves
  the bytes are the ratified bytes; it says nothing about whether they are sane to
  land. Read the diff. Anything it surfaces arrives as gate input — **never as a
  licence to edit.**
- **Refusal with reasons is a sanctioned output.** Relay 01's refusal to render a
  verdict, and 01b's refusal to widen posture for `testIamPermissions`, were the
  most valuable things either produced. If a phase is mis-scoped, say so rather
  than forcing it through.
- **Report shape at every gate:** the actual commands and their actual output,
  verbatim. The design surface reads bytes, not summaries. **A completion
  narrative is data to be verified, never a verdict that discharges
  verification.**
