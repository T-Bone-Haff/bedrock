# Bedrock package lifecycle

This is the normative lifecycle contract for changing, validating, versioning,
packaging, releasing, and rolling back Bedrock. The package manifest at
`../.claude-plugin/plugin.json` is the sole authority for the current package
version. Changelogs, tags, marketplace records, evidence, and rollout ledgers
are checked carriers; none may independently select a version.

Each skill directory also carries a generated `PACKAGE_IDENTITY.json`. This
ordinary visible file lets a skill-only consumer surface report package
identity without inventing a second authority. Every copy is byte-identical,
names the manifest pointer and digest, and is regenerated from the manifest and
registry by `scripts/sync_package_identity.py`. Consumers may verify the root
manifest directly when the host exposes it; otherwise they read a generated
skill carrier. If neither is visible, package identity remains unavailable and
must not be inferred from skill content.

## Candidate and release states

A manifest version on a branch or on `main` is a **candidate** until cold
acceptance makes an explicit release decision. The package cannot self-declare
that state: the immutable tag, release evidence, and rollout ledger are the
operational authority. Internal recovery candidates are not retroactively called
releases. A consumer release requires one annotated tag named
`v<manifest-version>`, a GitHub release at the same commit, retained release
evidence, and a completed rollout ledger. There is no tag before the release
decision.

The lifecycle is:

1. reconcile every assigned finding and its owner;
2. implement on a feature branch, including the manifest bump whenever skill
   content changes;
3. produce deterministic, integration, strict-host, install, routing, and
   review evidence;
4. record compatibility and migration impact;
5. obtain the operator's ratified candidate gate;
6. merge the reviewed candidate;
7. run independent cold acceptance under HEB-119;
8. only after a `proceed` decision, create the matching tag and GitHub release;
9. execute and retain the per-release rollout ledger; and
10. close only after every required surface has loaded the intended identity or
    has an explicit failed/waived disposition.

## Recovery boundaries

The recovery programme is staged by proof boundary, not by retroactive release
labels: HEB-108/109 restored loadability and validation; HEB-110 established the
safety floor; HEB-111 ratified architecture and routing ownership; HEB-113–117
corrected every retained domain skill; HEB-118 establishes package governance;
and HEB-119 independently accepts or pauses the resulting candidate. Evidence
from one boundary is retained, but cannot substitute for a later boundary's
gate.

A failed gate returns the candidate to implementation. `conditional proceed`
names every remaining condition, owner, evidence, and expiry; it is not a
synonym for release.

## Semantic-version decisions

The finished delta, not the ticket title, selects the version:

- **major**: remove, rename, split, or merge a public skill; change an
  established routing owner; break an input, output, evidence, refusal,
  authority, precedence, installation, explicit-invocation, supported-host, or
  self-containment contract; or make an optional capability mandatory without
  a compatible degraded path;
- **minor**: add compatible package behavior, evidence, metadata, profiles, or
  optional capabilities without changing established ownership or consumers;
- **patch**: correct a compatible defect or evidence carrier without changing
  the public contract.

Every skill-content edit and its manifest bump land in one commit transaction.
Metadata-only release-evidence corrections do not claim a new version unless
they change bytes consumers must receive.

## Release evidence

The release record conforms to `release-evidence.schema.json` and binds the
candidate to the manifest digest, source commit, finding reconciliation,
changed surfaces, migration disposition, required gates, limitations, and
operator decision. Evidence produced by different fixture, catalog, policy,
model, adapter, or source identities is not pooled.

The operational rollout record conforms to `rollout-ledger.schema.json`. It may
live in the tracker, but the schema and all load-bearing distribution rules are
in this package. Final closure runs `validate_package_governance.py --release`
with exported release-evidence and rollout-ledger files. The validator proves
their identities match the immutable tag; the files do not have to be committed
at that tag and the tag is never moved after rollout. Claude.ai propagation is
verified in a new session after the marketplace push by reading a loaded
identity carrier and enumerating the skills. Claude Code requires marketplace
refresh/update, plugin update, and a new session, then direct manifest and
carrier parity checks. Neither surface requires copying skill folders into
consumer repositories.

## Compatibility and migration

Every candidate states one of `none`, `compatible`, or `breaking` for migration.
`none` still requires a rationale. A breaking candidate includes the previous
contract, new contract, affected consumers, required actions, compatibility
window, rollback treatment, and evidence. Host and adapter claims are limited
to rows in `COMPATIBILITY.md` backed by retained evidence.

Prompt generations are independently identified by generator version, source
contract version, and source digest. Wording-only changes do not redefine the
portable contract. A prompt or carrier format break is versioned at the
generator or adapter boundary and affects package SemVer only when the
distributed compatibility contract changes.

## Rollback

Rollback is required for a material safety regression, loadability or routing
failure, manifest/marketplace mismatch, invalid release evidence, unsupported
consumer break, or propagation to the wrong package identity. Stop further
rollout, preserve the failed evidence, identify the last accepted tag, and
choose either a forward repair with a new version or restoration of the last
accepted release. Never move or reuse a published version tag. Rollback success
requires the same surface enumeration and identity verification as rollout.

## Retention and authority

Retain release evidence, routing reports, deterministic logs or artifact links,
the final review, acceptance decision, tag/release identity, rollout ledger,
and rollback record for the life of the supported release plus its successor.
Tracker state records operations; it does not replace installed policy,
contract rationale, compatibility, or reproduction instructions.

The authority and conflict ordering in `registry.yaml` is mechanical. When two
applicable authorities disagree without a declared ordering, stop and obtain
operator disposition rather than selecting the convenient rule.
