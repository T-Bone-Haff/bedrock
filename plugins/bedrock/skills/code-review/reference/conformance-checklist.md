# Reference: Conformance Checklist

The concrete checks the SA (Solution Architect) hat runs, the full per-hat question sets, and the disposition disciplines. The method, severity vocabulary, and self-review discipline are in `SKILL.md`.

## Contents

- [1. Conformance checklist](#1-conformance-checklist)
- [2. Per-hat question sets](#2-per-hat-question-sets)
- [3. No-drift confirmations](#3-no-drift-confirmations)
- [4. Out-of-scope triage](#4-out-of-scope-triage)
- [5. Retrospective review for pre-standard code](#5-retrospective-review-for-pre-standard-code)
- [6. Checkers and validators](#6-checkers-and-validators)

---

## 1. Conformance checklist

Run this against every change. Each item is a conformance question; the full rule behind it lives in the owning skill's conventions — `application-code` and `testing` for the base items, `agent-code` and `frontend-code` for their sections below — consult those when an item needs adjudication. An item that passes is a candidate **POSITIVE** finding (§3); an item that fails is an **add/fix** finding at the appropriate severity.

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

**Agent code** (when the change touches code whose central act is an LLM call — adjudicate against the `agent-code` conventions)
- [ ] Prompt changes carry a generation bump and were reviewed as semantic changes — no cosmetic exemption for prompt bytes.
- [ ] New untrusted-input paths identified and handled — tool results and retrieved content treated as untrusted model input.
- [ ] Tool-permission scope deltas justified against least-agency; write authority gated, never ambient.
- [ ] No new LLM judgment on a terminal path — terminal predicates remain mechanical functions over durable state.
- [ ] New model calls carry the structured-output contract and parse-seam discipline (strict item validation, observable drops, port-boundary identity stamping).
- [ ] Cost posture intact — cache alignment not silently broken; usage capture present on new call sites.

**Frontend code** (when the change touches frontend code — adjudicate against the `frontend-code` conventions)
- [ ] Layered import direction respected — no surface imports a concrete client or vendor SDK; seam interfaces consumed via providers.
- [ ] No hardcoded visual values — color, type, spacing, and motion come from the design tokens; runtime config from the typed config module, no scattered `import.meta.env` reads.
- [ ] Type-check and strict-type-checked lint clean; type escape hatches (`@ts-expect-error`, `as`-casts) carry site justifications.
- [ ] Prototype-origin code was re-authored at hardening, not lint-fixed — the prototype rode in as design intent, and tests specifying the kept behavior landed with the re-author.
- [ ] Generated contract types regenerated and drift-checked, never hand-edited; no hand-written mirror of a backend model.
- [ ] XSS escape hatches reviewed — `dangerouslySetInnerHTML` only over sanitized content, URL props scheme-validated, no eval-class constructs.
- [ ] No credentials in browser storage; no secrets in client config or the bundle.
- [ ] Accessibility holds at the floor — semantic elements, accessible names on interactive elements, keyboard path intact, focus managed on navigation and dialog changes, motion respects reduced-motion.
- [ ] Tests query by role and accessible name; mechanism-layer coverage floor met honestly (no omit-list or directory-placement dodges).
- [ ] New dependency adoptions justified — architecture-shaping, recurring-cost, or proprietary-license adoptions carry a decision record.

**Process**
- [ ] All automated gates passed (lint, format, type-check, tests, coverage, security scan).
- [ ] Data-classification tier documented where the change introduces or moves data.
- [ ] A decision record was filed if the change adopts a non-standard library or pattern.
- [ ] Change adds or modifies a checker/validator: the §6 coverage accounting ran.

The checklist is the SA hat's instrument; it does not replace the LAA (Lead Application Architect) and EA (Enterprise Architect) lenses (§2), which the checklist can't capture — scope-fit and posture-fit are judgment, not checkboxes.

---

## 2. Per-hat question sets

**LAA — Lead Application Architect — what is this change?**
- Does the change match the scope it claims (ticket, PR description)?
- Are the things it closes the things that scope actually covered?
- Is there scope creep — unrelated changes riding along?
- Are dependencies and side effects declared?
- Does the title/description match what the diff actually does?

**SA — Solution Architect — how does this change conform?**
- Does the code follow the conventions? (the §1 checklist)
- Did all automated gates fire and pass?
- Are tests at threshold, types clean, cross-references resolving?
- Is the change correct under edge cases and error paths — not just on the happy path?

**EA — Enterprise Architect — should this land in this shape, at this time?**
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

---

## 6. Checkers and validators

When the change under review is itself a checker — a validator, a conformance check, a lint rule, a guard — the review runs one additional accounting: **the gap between the check's authority text and its mechanization is either a violation mode or a stated reason. Every silent skip path is unaudited coverage.**

The procedure: enumerate what the check's authority text demands, then account for every case the implementation doesn't flag. Each unflagged case must be one of exactly three things — a **violation mode** (the check fires on it), a **fail-loud** (the check refuses rather than guesses), or a **documented justification** (the skip is deliberate and stated). A case that is none of the three is unaudited coverage — an add/fix finding at the appropriate severity.

Interrogate three seams specifically — the places where coverage silently narrows:

- **Presence assumptions across enforcement-tier lines.** An exemption or precedent valid on one side of an existence-constraint line does not transfer to the other; re-derive it there rather than inheriting it.
- **Null propagation in negated predicates.** In a three-valued-logic substrate, a negated equality silently drops nulls; every negated predicate over nullable data needs an explicit null ruling.
- **Parse/merge/union steps upstream of the comparison.** Any many-to-one step before the check runs — parsing that collapses duplicate keys, map-building with last-write-wins, unions that dedupe — can destroy the evidence the check exists to examine. Verify the check sees the data before the collapse, or that the collapse is itself checked.

This is the mechanized twin of "Narrated process is data" (SKILL.md): that rule is about narrative coverage that looks complete and isn't; this one is about a checker's own coverage that looks complete and isn't.
