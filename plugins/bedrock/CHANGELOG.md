# Changelog

The package manifest is the sole authority for the current version. This file
records candidate and released changes; a version heading is not release proof.

## 8.4.0 — consumer-visible identity candidate

- Add a generated, byte-identical package identity carrier to every skill so a
  skill-only host can expose the authoritative manifest version and digest.
- Add deterministic generation, drift rejection, installed-package parity, and
  malformed, missing, stale, divergent, and contract-mutation coverage.
- Advance the Claude adapter contract to 1.1.0 for the compatible identity
  carrier surface; cold acceptance and rollout remain external gates.

## 8.3.0 — instrument-authoring candidate

- Derive relay demands and review charges from their consuming instruments,
  preserving accepted grammar and outcome taxonomies verbatim.
- Add author-time satisfiability, structural measurement, verdict-bearing pins,
  custody/reachability separation, edit-locus-derived touch sets, and premise
  falsification to relay and review-charge authoring.
- Require counterfactual detector proof when a standard defines success as an
  absence, with deterministic positive, negative, and adversarial cases.

## 8.2.0 — rule-trigger reliability candidate

- Require every reusable rule to name and classify its firing event,
  frequency, salience, enforcement, expected failure, and reliability
  disposition.
- Reject internal-state-triggered rules without an instrument, external
  detector, or explicit known-weak disposition.
- Add deterministic trigger-test behavior cases and retain the whole-corpus
  HEB-136 sweep evidence.

## 8.1.0 — package-governance candidate, pending HEB-119 acceptance

- Add enforceable lifecycle, compatibility, migration, rollback, support,
  deprecation, threat-model, rebind, and rollout contracts.
- Add machine-readable package authority, capability, skill-lifecycle, release
  evidence, and rollout-ledger records.
- Add repository/license metadata and installed-package license coverage.
- Add deterministic package-governance validation and required CI.

## 8.0.0 — recovery candidate, not consumer-released

- Correct the frontend portable contract and Haffey React/Vite profile.
- Add browser, accessibility, security, performance, and application-delivery
  seam evidence.
- Retain a 162/162 full routing population with zero excluded selections.

Earlier manifest versions were internal recovery candidates. They are preserved
in Git history and evidence records and are not retroactively represented as
tagged consumer releases.
