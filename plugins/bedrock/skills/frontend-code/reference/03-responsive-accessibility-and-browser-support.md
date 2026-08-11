# Responsive behavior, accessibility, and browser support

## Support is declared

Name supported browser engines/versions, devices or viewport bounds, input
modalities, languages, assistive-technology evidence, and fallback behavior.
Build targets, automation engines, and the consumer support promise are three
different identities and remain explicit.

## Responsive behavior

Use media queries for environment/user preferences and container queries for
available component space. A size query requires an established size-query
container; custom properties work normally in declarations inside a matching
query, while support and evaluation of query conditions/style queries require
separate verification. Non-baseline features need a fallback or declared
support restriction.

Use relative units where they preserve user scaling, but do not treat any CSS formula or ratio as proof. Verify behavior at 200% text resize and reflow at a
320 CSS-pixel equivalent/400% zoom scenario: no loss, overlap, clipping, or
two-dimensional scrolling outside a criterion's explicit exception. A
fixed-frame exception names the exact content requiring two-dimensional layout;
surrounding chrome still reflows, and text resize remains required.

## Accessibility behavior

The consumer declares its conformance target; the Haffey profile targets WCAG
2.2 AA. Use native semantics before ARIA. Every operation has a keyboard path,
visible focus, accessible name, and necessary announcement. Manage focus on
route/dialog transitions and restore it when appropriate. Provide alternatives
to dragging, pointer precision, motion, audio/voice, and permission-gated input.

Contrast, focus visibility/obscuring, target size, text spacing, language,
errors, labels/instructions, accessible authentication, and consistent help are
evaluated where applicable. Criterion exceptions are checked before asserting
a defect or exemption.

## Evidence limits

Run applicable automated rules and real-browser behavior in the declared
engines, then retain manual keyboard/resize/reflow/contrast/target evidence and
a representative assistive-technology flow. Record exact OS, browser, AT,
versions, build, steps, observations, and limitations. One Safari/VoiceOver
flow demonstrates only that named flow and environment.
