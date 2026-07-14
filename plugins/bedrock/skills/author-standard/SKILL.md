---
name: author-standard
description: Author — or decide whether to author — a reusable standard: a Claude skill, an engineering convention set, a template, or any artifact meant to govern future work. Carries the sourcing rule (forward-author from established authority, never back-distill from an uncontrolled build), the membership test (task-triggered skill vs. always-on principle), binding declaration, shape and hardening disciplines, and the proving step (cascade onto a real consumer). Use whenever creating or extending a skill, standard, convention document, checklist, or template; deciding whether something should be a skill; or distilling a body of conventions into reusable artifacts. Authoring a single decision record is the author-decision-record skill; mechanical skill packaging and evals are the generic skill-creator — this skill governs whether to author, from what authority, and how to prove the result.
---

# Author a Standard

A *standard* here is any reusable artifact that governs future work: a Claude skill, a convention set, a template, a checklist, a house vocabulary. This skill's one job is to make that artifact an **authority worth obeying** — sourced honestly, scoped to one job, bound explicitly, and proven against a real consumer before it's trusted.

**Binding:** these disciplines are stack- and domain-independent — they govern the authoring of reusable artifacts, whatever those artifacts bind to.

## Should it exist? (the membership test)

A skill is a **task-triggered unit**. The test: does it fire on a recognizable task someone would actually ask for? "Write tests," "review this diff," "author a decision record" fire on a task — they're skills. "Root cause over workarounds," "give a direct recommendation" fire on *every* task — they're standing behavior, and they belong in preferences or always-loaded context, never in a triggered unit. **If you can't name the task-shaped prompt that should invoke it, it isn't a skill.**

Two more gates before authoring:

- **One clean job per skill.** A grab-bag is either several skills or none yet. If the candidate's contents answer different task-shaped prompts, split before drafting.
- **Smallest artifact that captures the value.** A directive line beats a skill; a skill beats a corpus; a corpus beats a governed system. Reach for the heavier form only when the lighter one has demonstrably failed to carry the content.

## Source it (forward-author, never distill)

Forward-author from **established authority plus your own exercised judgment** — public practice, documented standards, decisions that survived real use. Never back-distill a standard from code or output that was generated without authoring discipline: that canonizes whatever a model happened to emit, and it's circular — "code as authority" wearing a process costume. The two directions produce similar-looking documents and run opposite vectors.

**Set coherence:** every member of a skill set must be the same kind of object — an upstream authority. One member that's secretly a downstream description of an uncontrolled build breaks the set silently, even when it reads like the others. "What kind of object is this?" is load-bearing, not stylistic.

## Bind it (declare the binding)

"Project-agnostic" almost never means universal — it means portable across projects *on the same binding* (stack, toolchain, audience, context). Declare the binding up front, and name a materially different binding as a **rebind**: a re-derivation of the equivalent conventions, not a line-edit. The temptation is to strip every specific to fake universality — that guts the artifact, because the value is in the specifics. Every reusable artifact carries a binding; declare it rather than pretend it's absent.

## Shape it (structure follows content)

Let the structure follow what the content needs — never impose a skeleton because a template or a sibling artifact has one. A pure reasoning protocol may be one self-contained page with no reference folder; a conventions corpus may need several. Symmetry across artifacts looks disciplined, but uniform structure on non-uniform content is ceremony wearing rigor's costume.

And remember what a form can and cannot give: **shape, not substance.** A blank template is dangerously easy to fill with plausible-looking nothing; where the substance is absent, the easy fill is the trap. (For decision records specifically, the deliberation gate lives in `author-decision-record`.)

## Harden it (drafting rules)

- **One house vocabulary.** A shared ladder (severity, status, tiers) is defined once, house-wide; each artifact declares only its own binding to it (which tier means what *to this tool*). Per-artifact vocabularies are drift surfaces; crosswalks between competing ladders rot.
- **Point, don't mirror.** When any reusable or orientation artifact — a skill, a README, a repo-root CLAUDE.md, a template — needs an authority's enumerated content (a vocabulary, a skill list, a taxonomy, a mapping owned elsewhere), point to the authority; don't restate it inline. An inline restatement is a standing drift surface: it goes stale the next time the authority moves, and "fixing" it by re-copying just re-plants it. The decision-record-body form of this rule lives in `author-decision-record`; this is the class-level rule it instantiates.
- **Name the discriminating axis at the assignment site.** When a value or rule is justified by multiple entangled properties, every later assignment that matches one axis but not another reads as a contradiction until the discriminator is stated where the assignment happens — not only where it was first derived.
- **Pressure needs an exit.** Prohibiting a gaming behavior without releasing the pressure that produces it just relocates the failure. Pair every anti-gaming rule with a sanctioned exit in the fail-safe direction (at the cap, drop — don't re-label).

## Prove it (the standard earns trust against a consumer)

- **Cascading onto a real consumer is itself a test of the standard.** Expect the first adoption to surface self-violations the authors walked past — the standard shipping the very pattern it prohibits is the classic. Don't trust a standard that has never met a consumer.
- **Remediation self-applies its rule.** When a fix operates in the same medium as the rule it enforces, run the rule against the remediation — the fix for a restatement violation must not itself restate.
- **Consumer divergence has three resolutions, not one.** When an implementation does something the standard doesn't say: *neuter* (fix the implementation), *promote* (the standard has a gap the implementation already filled — bring the standard up), or *demote* (the standard over-claims — retract it). Don't default to neuter; ask whether the implementation is the teacher. Single-instance promotions need an explicit threshold call.
- **Check joint satisfiability before ruling deviation.** A consumer that cannot conform may be the first probe deep enough to expose two of the standard's own rules as mutually unsatisfiable. If so, the fix is an upstream repair, not a downstream waiver — and the burden of justification flips.

## Distribute vs. remediate

A release of a standard is not complete until it has been **pushed to the enumerated consumer surfaces** — the kit owns that enumeration, and a surface with no push path is a finding, not a footnote. Push means the update and its staleness signal arrive unbidden: the knock, never the remediation. The consumer still adopts and remediates its own corpus on its own cycle — push is not auto-remediation, and reaching into a consumer to hand-edit its documents conflates two duties that want separate owners and separate cadences.

Two rules keep the channel honest:

- **Staleness is signal-bearing, never silent.** A pull-only channel where nothing prompts the pull leaves consumers quietly stale across releases; every enumerated surface needs a mechanism by which lag announces itself.
- **Snapshot consumers verify currency against a fresh baseline.** A vendored authority or hand-synced copy is checked at time-of-use against the *current* release — a currency check run against a stale baseline is vacuously green, which is worse than no check at all.

When a governing posture has already shifted, bringing old artifacts up is **propagation, not a new decision** — the target shape already exists; apply it without re-deliberating it.

## Worked calls

- *Membership:* "Author a decision record" → names a task-shaped prompt → skill. "Design over code" → holds on every task → standing principle; route to preferences, not the skill set.
- *Sourcing:* Conventions written from framework documentation, community practice, and rulings that survived real use → forward-authored authority. A conventions doc extracted from one AI-generated service that was never reviewed → back-distillation; reject as a source, however clean it reads.
- *Proving:* A document template cascaded onto its first real consumer was caught priming authors for the exact interstitial review-history capture the doctrine prohibits — the carrier carried the defect. The catch is the proving step working, not the authoring step failing.

## Boundaries with sibling skills

- **Authoring a single ADR / DDR / SDD** → the `author-decision-record` skill. That skill owns decision-record *instances*, including their deliberation gate; this skill owns the reusable *class* — including the templates those records are written from.
- **Reviewing a finished change** → the `code-review` skill. This skill authors the authorities that reviews cite.
- **Mechanical skill packaging, zipping, and eval tooling** → the generic `skill-creator`. Use it downstream of this skill's judgments; it does not decide whether the artifact should exist or what authority it rests on.
