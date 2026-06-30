# File: docs/reviews/YYYY-MM-DD-{{slug}}.md
# Author: {{AUTHOR_NAME}} — {{AUTHOR_ROLE}}, {{ORGANIZATION}}
# Created: YYYY-MM-DD
# Description: {{Review type}} of {{what}}. {{One sentence on scope and what gate this review serves.}}

# {{Review title — e.g. "Pre-merge review — pricing-service quote endpoint"}}

| Field | Value |
|---|---|
| **Date** | YYYY-MM-DD |
| **Reviewer** | {{name — role}} |
| **Scope** | {{one-sentence scope}} |
| **Outcome** | **{{PROCEED / PROCEED-WITH-CHANGES / PAUSE}}** — {{one-line qualification}} |

<!-- Most reviews are inline PR comments. Use this written record for substantial or
     architectural changes that warrant a durable artifact. Findings carry a severity
     (BLOCKING / MATERIAL / COSMETIC / POSITIVE) and a remedy (add/fix · remove/relocate · none).
     Each hat (LAA / SA / EA) produces a verdict; all three at PROCEED is the approval bar. -->

---

## 1. Scope

**In scope:** {{what this review covers — files, paths, the change under review}}

**Out of scope:** {{what it deliberately doesn't cover — routed to triage in §3 if surfaced}}

## 2. Findings

### BLOCKING
- **B-1** — {{finding}}. *Location:* `{{file:line}}`. *Remedy:* {{add/fix | remove/relocate → where}}. *Why blocking:* {{...}}.

### MATERIAL
- **M-1** — {{finding}}. *Location:* `{{file:line}}`. *Remedy:* {{...}}.

### COSMETIC
- {{finding}} — `{{location}}` — {{remedy}}.

### POSITIVE (no-drift confirmations)
- {{surface}} — checked {{aspect}}; conformant.

*(Delete any severity with no findings. If POSITIVE is empty, the clean cases weren't verified — go back and check them.)*

## 3. Out-of-scope triage

Items surfaced but outside this review's scope, routed rather than fixed here:

| Item | Source finding | Proposed disposition |
|---|---|---|
| {{summary}} | {{which finding}} | {{file new backlog item / fold into existing / reject — reason}} |

## 4. Per-hat verdicts and outcome

| Hat | Verdict | Basis |
|---|---|---|
| LAA | {{proceed / proceed-with-changes / pause}} | {{the findings driving it}} |
| SA | {{...}} | {{...}} |
| EA | {{...}} | {{...}} |

> **Outcome: {{PROCEED / PROCEED-WITH-CHANGES / PAUSE}}.** {{Justification referencing the finding counts and dispositions — e.g. "2 BLOCKING (B-1, B-2) must clear before merge; 3 MATERIAL folded in scope; 1 item routed to backlog."}}
