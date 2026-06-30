# Reference: Conformance Checklist

The concrete checks the SA hat runs, the full per-hat question sets, and the disposition disciplines. The method, severity vocabulary, and self-review discipline are in `SKILL.md`.

## Contents

- [1. Conformance checklist](#1-conformance-checklist)
- [2. Per-hat question sets](#2-per-hat-question-sets)
- [3. No-drift confirmations](#3-no-drift-confirmations)
- [4. Out-of-scope triage](#4-out-of-scope-triage)
- [5. Retrospective review for pre-standard code](#5-retrospective-review-for-pre-standard-code)

---

## 1. Conformance checklist

Run this against every change. Each item is a conformance question; the full rule behind it lives in the `application-code` and `testing` conventions — consult those when an item needs adjudication. An item that passes is a candidate **POSITIVE** finding (§3); an item that fails is an **add/fix** finding at the appropriate severity.

**Structure and style**
- [ ] Module comment block present on every new file.
- [ ] Type annotations complete on every function signature; type-check clean.
- [ ] Docstrings on all public functions, methods, and classes.
- [ ] Layered import direction respected — no `api → adapters` reach-through, no cross-layer violation.
- [ ] Naming follows convention (request/response/error models, domain exceptions, modules).

**Behavior and safety**
- [ ] No hardcoded configuration, URLs, or secrets — config comes from Settings, secrets from the environment.
- [ ] No synchronous/blocking calls inside `async` functions.
- [ ] Structured logging used throughout; no `print()` or bare stdlib logging.
- [ ] Correlation ID propagated on downstream calls.
- [ ] Audit emitted for data mutations and security events.
- [ ] Domain exceptions extend the domain base and surface via exception handlers — no scattered status codes, no silent cross-layer swallowing.
- [ ] Inbound data validated by a Pydantic model at the boundary.
- [ ] Outbound HTTP goes through the canonical client, not per-call instances.
- [ ] No Tier 3/4 data in logs; sensitive data classified and handled per tier.

**API**
- [ ] New endpoints declare full OpenAPI metadata (summary, description, response model, error responses).
- [ ] Request/response shapes are typed models; a contract test asserts them.

**Tests**
- [ ] Tests cover the happy path and at least two error scenarios.
- [ ] Coverage threshold met, honestly — no testable code omitted from measurement.
- [ ] Behavior was specified test-first where the TDD discipline applies.

**Process**
- [ ] All automated gates passed (lint, format, type-check, tests, coverage, security scan).
- [ ] Data-classification tier documented where the change introduces or moves data.
- [ ] A decision record was filed if the change adopts a non-standard library or pattern.

The checklist is the SA hat's instrument; it does not replace the LAA and EA lenses (§2), which the checklist can't capture — scope-fit and posture-fit are judgment, not checkboxes.

---

## 2. Per-hat question sets

**LAA — what is this change?**
- Does the change match the scope it claims (ticket, PR description)?
- Are the things it closes the things that scope actually covered?
- Is there scope creep — unrelated changes riding along?
- Are dependencies and side effects declared?
- Does the title/description match what the diff actually does?

**SA — how does this change conform?**
- Does the code follow the conventions? (the §1 checklist)
- Did all automated gates fire and pass?
- Are tests at threshold, types clean, cross-references resolving?
- Is the change correct under edge cases and error paths — not just on the happy path?

**EA — should this land in this shape, at this time?**
- Does the change integrate with the broader posture, or pull against it?
- Is the reversibility appropriate to the risk?
- Does it commit the project to a position that warrants a decision record first?
- Is the timing right?

Each hat aggregates its findings into a verdict (`proceed` / `proceed-with-changes` / `pause`) per the rule in `SKILL.md`. All three at `proceed` is the approval bar.

---

## 3. No-drift confirmations

POSITIVE findings record that a surface was checked and found conformant — "checked the layering, no violations"; "verified secrets come from the environment." They are required, not decorative. A review whose only findings are negatives hasn't shown it verified the clean cases; it's shown it noticed the broken ones. The positive findings are what let a later reviewer (or a future you) trust that an area was actually looked at, rather than re-reviewing it from scratch.

Keep them proportionate — confirm the load-bearing surfaces, not every line. The point is an honest record of what was verified.

---

## 4. Out-of-scope triage

Reviews surface things outside their scope. Those don't get fixed in this review and don't get absorbed into its findings — they get **routed**: a backlog item, a tracked note, a pointer to the right venue. Each routed item carries a one-line summary, which finding surfaced it, and a proposed disposition (file new / fold into existing / reject with reason).

The one exception: an out-of-scope finding that is BLOCKING for some other gate that would otherwise miss it — surface that one rather than only routing it, because routing-and-forgetting would let a real defect slip.

The discipline protects the review from sprawling into a rewrite of everything it touches, while making sure nothing real is lost.

---

## 5. Retrospective review for pre-standard code

Code written before the conventions were adopted is grandfathered — the review discipline applies to changes from adoption forward, not retroactively across the whole codebase.

The trigger: when pre-standard code receives a **substantive** modification, the change reviews the **whole touched file** against the checklist and three hats, not just the diff — because a substantive touch is the natural moment to bring the file up to standard, and reviewing only the diff leaves the surrounding non-conformance invisible. Trivial touches (typo, formatting, version-string bump) don't trigger it. A file that's completed retrospective review can carry a marker in its module comment block so the next reviewer knows it's already been brought current.
