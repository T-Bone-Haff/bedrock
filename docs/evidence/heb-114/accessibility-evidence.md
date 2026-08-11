# HEB-114 accessibility evidence

Status: **automated pass; required representative manual flow passed with
stated limitations**.

The automated population is the fixture's applicable Axe rules, keyboard flow,
focus transition, and 320 CSS-pixel reflow in three engines. The manual
population is one representative macOS Safari + VoiceOver flow. Results will
name exact OS/browser/AT/build identities, steps, observations, and limitations.
No universal WCAG or assistive-technology certification is claimed.

Automated result: the representative view produced zero detected Axe 4.12.1
violations; keyboard activation and route-focus movement passed; 320 CSS-pixel
reflow had no horizontal document overflow. The same population passed in
Chromium 151.0.7922.34, Firefox 153.0, and WebKit 26.5.

Manual target identity was verified as macOS 26.5.2 (25F84), Safari 26.5.2
(21624.2.5.11.8), and VoiceOver 10 (993). With VoiceOver enabled, Safari loaded
the production-preview fixture. Option-Tab moved focus to `Open details` and
displayed a distinct VoiceOver focus ring. Return activated the control, changed
the view to `Details ready`, and moved the accessibility focus to that level-two
heading. The System Settings VoiceOver switch was verified on for the flow and
restored to off afterward.

The observed manual population is limited to that representative keyboard,
activation, view-change, and focus-placement flow. VoiceOver's audible speech
wording was not captured in a readable transcript, so no claim is made about
the exact spoken phrase. Manual 200% text resize, 400% zoom, contrast-ratio
measurement, target-size measurement, other pages, other assistive
technologies, and other macOS/Safari versions were not exercised. Automated
three-engine checks cover the declared 320 CSS-pixel reflow and applicable Axe
population only; neither the automated nor manual result is a universal WCAG
or assistive-technology certification.
