# File: docs/ruling-rationale/2026-06-26-heb-36-kit-validators-rulings.md
# Author: Claude (claude.ai authoring session 2026-06-26) under DIRECTIVE-026
# Created: 2026-06-26
# Description: Ruling-rationale ledger for HEB-36 (kit-level validators, Phase-2.5) — deployment model.
#              Three rulings — R044 (single consolidated kit-rendered validator), R045 (contract-purity
#              grep homed inside it; mechanized now into SOFIA-Reboot's native validator, kit-promotion
#              staged), R046 (HE-Bedrock self-applies; mechanism rides HEB-44). Single-layer per
#              DIRECTIVE-031 §31.2.1 (≤3 rulings). Frozen at commit per §31.7. This Notion-mirrored copy
#              is the vendored filesystem record; the Notion design-decision page is the product-design SoR.

# HEB-36 — Kit-Level Validators (Phase-2.5) Deployment-Model Ruling-Rationale Ledger (2026-06-26)

**Ticket:** HEB-36 — Kit-level validators (Phase-2.5): promote+harden the doc-structure validator + implement the DIRECTIVE-023 contract-purity grep.
**Session:** claude.ai design/authoring 2026-06-26 (DIRECTIVE-026).
**Author:** Claude (claude.ai authoring session).
**Baseline SHA:** HE-Bedrock `main` @ `c895f3f` (main-only, HEB-24) — live-verified at session open (local == origin).
**Governance baseline:** CSD 3.3.0 · DMS 3.2.0 · kit VERSION 2.5.0 · annotated corpus tag `v2.5.0` (ENG-STD-001 3.3.0 / -002 2.3.0 / -003 3.0.1).
**Status:** Deployment-model deliberation settled; rulings **R044–R046** ratified per-item (claude.ai 2026-06-26). Execution leg: **RBT-47** — the DIRECTIVE-023 contract-purity check inside `validate-docs-structure.sh` + CI wiring — landed in SOFIA-Reboot `develop` @ `f4e74c0` (PR #20). This ledger is vendored via the HEB-36 close-records PR and **frozen at commit** per §31.7; HEB-36 itself stays In Progress (kit-promotion of the validator under R045 + self-application under R046 → HEB-44 remain).
**Ruling counter:** **R044–R046** — continue the global sequence (prior global max **R043** [HEB-38 Phase-2], re-verified 2026-06-26 against the repo `docs/ruling-rationale/` set + the Notion Phase-2 SoR `38bcaeea…`, per HEB-41 discipline).

Per DIRECTIVE-031 §31.7 this ledger is **frozen once committed**; supersessions record on the Linear trail and in a new ledger, never by amendment here. This vendored file mirrors the Notion product-design decision system-of-record.

> **Single-layer ledger (§31.2.1).** Three rulings this session (R044–R046); the §1 inventory layer is omitted per the ≤3-ruling operator-judgment exception. Detail blocks only.

---

## R044 — The kit-level document-checker class deploys kit-rendered as a single consolidated validator

**Ruling.** The document-structure / contract-purity checker class is governed **kit-side** and rendered into consumers via the DDR-001 `-template` strip — **not** consumer-native-per-project. It is consolidated into **one** validator script that is the single home for all mechanical document form / format / content validation; new mechanical doc-checks home into that one script rather than spawning siblings. The rendered checker is a **script** (invocation-agnostic); CI-invocation wiring stays **consumer-local** (HE-Bedrock has no CI, so it runs the script manually/master-side; a consumer wires it into its own CI / pre-commit / manual flow).

**Disposition.** Architectural direction — deployment model + single-home consolidation rule for a newly-recognized consumer activity class.

**Rationale.** Consumer-**authoring-validation** was under-modeled in the original Bedrock design: the kit modeled governance *standards* (CSD/DMS/ENG-STDs) plus operational *tooling* (commit-script, verify-repo-state), but not "every consumer authors documents that need mechanical structural validation beyond author/review/directives." This is a codification-breadth-shift, surfaced once a consumer (SOFIA-Reboot) began authoring and stood up RBT-3. The validator is the **structural safety floor** — the mechanical backstop for when the soft controls (DIRECTIVE-007 author/review, the directives) fail. Every consumer authors → every consumer needs the backstop → one rendered gate all consumers inherit. Consolidation into one script prevents the script-proliferation failure mode (N CI workflows + N wirings + N merge points). **Enforcement-closes-the-sweep:** once the validator (carrying the contract-purity grep) deploys with a consumer's governance refresh, every doc touch *after* that point is gated at PR time — converting the consumer from sweep-and-hope to gated-going-forward, and closing HEB-38 root-cause gaps #2 (additive-only review cadence re-accretes) and #3 (the un-generalized lesson) **mechanically**, as the hard backstop under the soft DIRECTIVE-007 §7.2.1 lens.

**Alternatives rejected.**
- *Consumer-native-per-project.* Rejected — re-creates the gate in every project, no single governed source, the status quo that surfaced the gap; "don't create fresh every time for every project."
- *Separate standalone grep / per-check scripts.* Rejected — script-proliferation; a later fold-in into the validator is exactly the relocation the single-home rule avoids.
- *Kit-render the CI-workflow YAML.* Rejected — assumes consumer CI; HE-Bedrock has none. Separate the portable *script* (kit-rendered) from its *invocation wiring* (consumer-local) instead — the `verify-repo-state` precedent.

**Primary sources verified.** DDR-001 (render recipe; master-side-only vs. kit-rendered taxonomy; Executor Contract / §13.5.9); live `scripts/` inventory (`verify-pin-currency.sh` = master-side-only; `verify-repo-state.sh` = kit-rendered precedent, instantiated from `scripts/templates/verify-repo-state-template.sh`); DMS §1.2 governed set, §3.1/§3.2, §7.4–§7.9; CSD DIRECTIVE-023 / -007 §7.2.1 / -026; RBT-35 (Done) venue note + standing conditional; RBT-3 (validator bootstrap, GitHub-Actions CI). All @ `c895f3f`.

**Other.**
- *Empirical floor:* the deployment **model** is not N=1 — the render mechanism is ACCEPTED (DDR-001) and has already carried two scripts (commit-script, verify-repo-state) into SOFIA-Reboot (HEB-12 Leg-1). No threshold override required for the model itself.
- *Breadth-shift:* original Bedrock design omitted authoring-validation as a first-class consumer activity; "this is the safety mechanism for when all the other parts fail."
- *RBT-35 discharge:* this ruling is the "kit-level validator introduced later" event RBT-35's standing conditional named.
- *Ratification venue:* claude.ai session 2026-06-26 — items 1 + 2, ratified per-item, HEB-36.

---

## R045 — Contract-purity grep homed inside the validator; mechanized now into SOFIA-Reboot's native validator; kit-promotion staged for SOFIA-Reboot next-authoring as the validating second case

**Ruling.** The DIRECTIVE-023 contract-purity check (R043 spec) is mechanized as a check **inside** the single validator (not standalone). Because the validator's kit-promotion is staged at the N=1 floor, the grep is implemented **now** into SOFIA-Reboot's consumer-native validator, riding to the kit at promotion with **zero relocation**. The validating second case for the exemption-list / governed-set master-freeze is **SOFIA-Reboot's next authoring cycle(s)** through the deployed gate — **not** the LILY render (demoted to eventual non-gating cross-consumer corroboration). The kit `-template` is authored **fresh against the DDR-001 recipe** at promotion (not by mutating the converged native script — ENG-STD-003 §13.5.9 prior-art-as-authority). The RBT-35 governed-set collection (PR #9) + glob-magic hardening (PR #11) fold into the kit master at that promotion.

**Disposition.** Sequencing / empirical-floor split + grep physical home.

**Rationale.** The grep's **portability** is N=1-immune: its surface is the doctrine-defined DMS §7.4 instantiated-identifier classes on morphing bodies — corpus-universal by construction, anchored to the ratified R043 check-spec, not to any consumer's layout. So it can be implemented now with confidence it won't rework for a second consumer; it just travels **inside** the validator (single-home rule, R044) rather than ahead of it. The genuinely N=1-sensitive piece is **exemption/governed-set completeness**, which SOFIA-Reboot's ongoing authoring traffic stress-tests directly and imminently — without waiting on HEB-14 → HEB-12 (stalled; HEB-14 Backlog). Cross-consumer *universality* is largely guaranteed by the shared DMS (exemptions are DMS §1.2/§3.1-path-anchored), so a second *consumer* (LILY) is corroboration, not the gate. **R027 surface-scoping** is a hard constraint on the grep impl: morphing-body doctypes only, fence-stripped, audit surfaces (`## Change Log`, cross-ref home) + audit-surface doctypes (ledgers / reviews / handoffs) excluded whole, concrete-ID-anchored — no false-RED on §7.4 / §24.1 teaching tokens or self-describing governance prose.

**Alternatives rejected.**
- *Kit-render the grep standalone now.* Rejected — its N=1-immunity makes "sooner to the kit" possible, but it buys nothing real (LILY doesn't render until HEB-12 regardless) and costs a second script + CI wiring + a later merge into the validator.
- *LILY render as the gating second case.* Rejected — gated behind stalled HEB-14; the real N=1 risk is exemption completeness, which SOFIA-Reboot's next authoring tests sooner and more directly.
- *Mutate SOFIA-Reboot's converged native script into the kit **`-template`**.* Rejected — ENG-STD-003 §13.5.9 prior-art-as-authority forbidden pattern; author the template fresh against DDR-001.

**Primary sources verified.** CSD DIRECTIVE-023 contract-purity check-spec; R043 (Notion Phase-2 SoR `38bcaeea…` + repo `2026-06-26-heb-38-phase-2-enforcement-rulings.md`); DMS §7.4–§7.9 (the §7.7 test, surface-types, content-contracts); R027 origin (HEB-9 Phase-1 reduced-form-assertion class); RBT-35 (PR #9 governed-set, PR #11 glob-hardening; SOFIA-Reboot `develop` @ `f4e74c0`); DDR-001 Executor Contract / §13.5.9; HEB-12 / HEB-14 gating state (both Backlog). All @ `c895f3f`.

**Other.**
- *Empirical floor — split:* grep portability N=1-immune (no override); validator/exemption master-freeze is N=1, staged for SOFIA-Reboot next-authoring (the available second case, not a stalled cross-consumer gate).
- *Interim protection:* SOFIA-Reboot enforces contract-purity in its native validator immediately at the governance refresh — nothing goes unguarded during staging.
- *Ratification venue:* claude.ai session 2026-06-26 — item 2 (grep home) + item 3a (RBT-35 discharge / second-case), ratified per-item, HEB-36.

---

## R046 — HE-Bedrock self-applies the validator (no CI); the self-instance mechanism rides HEB-44

**Ruling.** HE-Bedrock runs the validator over its **own** corpus — dogfooding the contract-purity doctrine it carries as the source-of-truth carrier — **manually at the DIRECTIVE-029 governance-maintenance cadence**; **no CI** in HE-Bedrock. The runnable self-instance is **not** bespoke-built for the validator now; it **rides the general "Bedrock-as-consumer-of-its-own-kit" self-render decision** (HEB-44, filed this session).

**Disposition.** Principle ratified + mechanism routed to a dependency.

**Rationale.** Dogfooding is strong — a self-violation in the carrier of the contract-purity standard is categorically the worst case (the same logic that drove R043's keystone). But HE-Bedrock has no CI (its rebind model, HEB-24), so self-application is manual at the governance cadence (a governance-document amendment is already a DIRECTIVE-029 trigger). Building a one-off self-instantiation for the validator *ahead* of the general self-render mechanism would be the don't-build-into-a-home-you'll-relocate trap one tier up, at the Bedrock-self level. The general mechanism ("render the kit for the kit's own author/creator") had **no existing ticket** — it lived only in operator memory — so HEB-44 was filed (DIRECTIVE-025 dedup: not a duplicate of HEB-24's reduced-form-master leg; genuine seam — HEB-24 captures *how Bedrock holds* its corpus, HEB-44 asks whether Bedrock *also renders an instance for self-use*).

**Alternatives rejected.**
- *Bespoke self-instantiate the validator now (mirroring the ad-hoc **`verify-repo-state`** self-instance).* Rejected — a one-off ahead of the general mechanism; relocation trap.
- *CI in HE-Bedrock.* Rejected — out of scope; HE-Bedrock runs no CI by its rebind model (HEB-24).
- *Skip self-application.* Rejected — forgoes carrier-level dogfooding, the strongest case for catching a self-violation early.

**Primary sources verified.** HEB-38 ("the HE-Bedrock kit itself is also in scope as the source-of-truth carrier"); CSD DIRECTIVE-029 §29.1 audit cadence / §29.4 single-source-of-truth; live `scripts/` inventory (`verify-repo-state.sh` ad-hoc self-instance precedent); HEB-24 (reduced-form master, nearest neighbor); HEB-44 (filed 2026-06-26, this session). All @ `c895f3f`.

**Other.**
- *Empirical floor:* lightest-pressure item — HE-Bedrock corpus is small and largely hand-curated; principle ratified, build not urgent.
- *Forward pointer (queue-piggyback under R046, §31.2.4):* HEB-44 carries the self-render deliberation; this ruling does not pre-decide its scope/render-path/cadence.
- *Ratification venue:* claude.ai session 2026-06-26 — item 3b, ratified per-item, HEB-36.

---

*End of HEB-36 kit-level-validators (Phase-2.5) deployment-model ruling-rationale ledger.*
