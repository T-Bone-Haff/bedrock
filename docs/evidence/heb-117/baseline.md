# HEB-117 baseline

Fresh reconciliation on 2026-08-10 used `main` and `origin/main` at `9e8719e32f08f5672263766147e383da2b4ae24f`.

Before correction:

- the five scoped skill bodies plus templates/checklist totaled 1,963 lines;
- the construct-spec template was 314 lines and substantially mirrored its skill;
- authoring contracts depended on sibling skills, private tracker history, fixed actor topology, or prose-only controls;
- code review required three hats and positive findings for every change and omitted infrastructure/delivery and risk-triggered overlays;
- no machine-readable relation, relay, or review-result schema existed;
- existing validation passed 46 tests with one expected local Docker skip, strict validation passed 13/13, and isolated install discovered all 13 skills.

HEB-110 changed none of the five skill directories. Its landed safety floor nevertheless governs HEB-117: prompt-only controls are advisory, authorization is distinct from fidelity, substrate is untrusted, and safety claims require regression evidence.
