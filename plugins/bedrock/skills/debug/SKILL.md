---
name: debug
description: Structured debugging — reproduce, hypothesize, falsify, then fix the root cause. Use when something is broken, behaving unexpectedly, failing in one environment but not another, or when an error or stack trace needs diagnosis: "why is this failing", "this works locally but not in CI", "something broke after the deploy", "debug this", "help me figure out what's wrong", "this test is flaky". Drives a falsification-based hypothesis loop instead of guess-and-patch, and fixes root causes rather than masking symptoms. The discipline is language- and stack-agnostic.
---

# Debug

A discipline for diagnosis. The failure mode it exists to prevent is **guess-and-patch** — seizing the first plausible explanation, applying a fix, and moving on while the real cause survives. The antidote is to treat diagnosis as a falsification problem: form a hypothesis, then actively try to break it.

## Diagnose before you touch anything

When something behaves unexpectedly, **investigation precedes remediation.** The default impulse — assume the simplest explanation and act on it — is exactly what to suppress. Before proposing a fix, run a diagnostic step that *distinguishes between* the candidate explanations. A fix applied before the cause is known is a guess wearing a fix's clothes; if it happens to work you've learned nothing, and if it doesn't you've added a variable.

## Reproduce first

You can't fix what you can't reproduce, and a reliable reproduction is also your falsification instrument — the thing you run after each hypothesis to see whether reality agrees. Get the failure to happen on demand before theorizing about it. For a bug, the reproduction is often a failing test (which then becomes the regression test once the fix lands); for an environment-specific failure, it's the minimal set of conditions that triggers it. If you can't reproduce it, that *is* the first finding — chase the reproduction before the cause.

## The hypothesis loop

A first-pass diagnosis is a **hypothesis, not a conclusion.** Run it through this loop:

1. **State the hypothesis explicitly.** Not "the cause is X" but "the hypothesis is X; if X is true, then Y; Y is observable via Z." A hypothesis that makes no checkable prediction isn't ready.
2. **Seek the falsifier, not the confirmation.** Ask what evidence would prove the hypothesis *wrong*, then go get that evidence and look. Gathering only confirming evidence is how a wrong hypothesis survives — the bias is toward proving yourself right, and the discipline is to fight it.
3. **Treat unexplained evidence as signal, not noise.** If the hypothesis explains 80% of what you see and 20% doesn't fit, the hypothesis is *incomplete* — the 20% is the most informative thing on the table, not an anomaly to wave off.
4. **Iterate the framing when contradicting evidence surfaces** — and number the iterations (Iteration 1, Iteration 2, …), each recording what it added or refuted. Update the hypothesis; don't patch the old one with explain-aways that absorb the contradiction without changing the conclusion.
5. **Don't converge prematurely.** A hypothesis that explains everything currently visible may still be wrong — ask whether more evidence could falsify it before treating convergence as final.

## Fix the root cause, not the symptom

Once the cause is actually known, fix *it* — not the surface it manifested on. A workaround is acceptable only as an explicit, temporary measure with a named follow-up to address the root cause; an unannounced workaround with no follow-up is debt that compounds, because the real fault is still there and the next person can't see that it was knowingly left.

## Don't guess at what you can read

When the exact shape matters — a function's return type, a config value, a log line, a schema, the actual error vs. the assumed error — **read it, don't infer it.** Inferring return shapes and signatures is one of the largest sources of wasted debugging time: you build a hypothesis on an assumed shape, it's wrong, and every downstream step inherits the error. If you can't read the source directly, get the real value (grep it, log it, print it, ask whoever can run the command) before building on it.

## Disagreement is data

When you and the operator disagree about the diagnosis, the disagreement is **diagnostic data, not noise** — in both directions. If the operator pushes back on your hypothesis, investigate their reasoning before defending yours; "I'm confident" is a weaker signal than evidence, and operator pushback often carries context you don't have (workspace state, prior decisions, what actually changed). If you push back on theirs, that's also data — surface the evidence and let it adjudicate. The diagnosis converges faster when disagreement triggers investigation instead of a contest.

---

## A worked pass

*"This works in staging but fails in production."*

- **Reproduce:** confirm it fails in prod reliably and passes in staging reliably — not intermittently. (If it's intermittent, that's a different, important finding.)
- **Hypothesis 1:** "It's a config difference. If so, some setting differs between the two environments, observable by diffing the resolved config." → Diff the config. Suppose they're identical on the suspected keys. That's a *falsifier*, not a dead end.
- **Unexplained evidence:** the error is a timeout, and prod has a downstream dependency staging mocks. The timeout didn't fit Hypothesis 1 — that's the signal.
- **Hypothesis 2 (Iteration 2):** "It's the real downstream call. If so, the failure correlates with that dependency's latency, observable in the call's traces/logs." → Check. Traces show the call exceeding the deadline only in prod.
- **Root cause vs symptom:** the fix is not "raise the timeout until it stops failing" (symptom) — it's understanding why the prod path is slow (missing index? cold cache? N+1?) and fixing *that*, with the timeout adjustment as a separate, justified decision if still warranted.
