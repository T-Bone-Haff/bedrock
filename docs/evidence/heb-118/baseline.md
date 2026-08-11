# HEB-118 package-governance baseline

## Accepted starting identity

- repository: `T-Bone-Haff/bedrock`
- source baseline: `e3073d11aca23d88b32fcdb7f342cd90bab439e8`
- baseline manifest: `8.0.0`
- implementation candidate: `8.1.0`, derived as a compatible minor after the
  additive package-governance delta existed
- existing release tags at kickoff: none
- release state: candidate; HEB-119 retains the only release decision

The lack of tags is not repaired by retroactively calling recovery candidates
consumer releases. HEB-118 defines and enforces the tag/release contract; the
first tag may be created only after HEB-119 returns `proceed`.

## Finding reconciliation

The HEB-107 register contains 39 package-wide findings. Nineteen were already
implemented and evidenced by upstream recovery, architecture, safety, and
domain streams. HEB-118 owns the remaining twenty package-governance seams.
`manifest.yaml` names all 39 identities exactly once and binds each to retained
repository evidence.

HEB-118 residual findings are `PKG-004–012`, `PKG-017–023`, `PKG-026`,
`PKG-028`, `PKG-033`, and `PKG-039`. They are realized through:

- manifest, marketplace, license, changelog, and tracked-orientation coherence;
- installed lifecycle, support, security, compatibility, deprecation, rollback,
  threat-model, quickstart, and rebind contracts;
- machine-readable authority, precedence, capability, lifecycle, prompt-format,
  release-evidence, and rollout-ledger records;
- measured catalog/entrypoint budgets rather than an unqualified word cap; and
- a fail-closed candidate validator plus a stricter post-acceptance `--release`
  mode that requires the tag, proceed decision, evidence, and completed rollout.

## Authority and portability

The package manifest remains the sole current-version authority. Marketplace
metadata and changelog headings are checked carriers. The portable-core and
Claude-adapter contract identities remain separate from package SemVer.

The user-owned root `AGENTS.md` was preserved unchanged. The tracked
`docs/repository-orientation.md` is the orientation authority, `CLAUDE.md` is
its checked Claude carrier, and root `AGENTS.md` is ignored local Codex context
that is neither packaged nor release authority.

No skill was removed, renamed, split, merged, or rerouted. No optional runtime
capability became mandatory. Codex/OpenAI, Cursor, and SOFIA runner support are
not claimed. HEB-122 is unchanged.

## Distribution ruling

Claude.ai/Cowork consumes a pushed marketplace version in the next new session.
Claude Code requires marketplace refresh/update, plugin update, and a new
session. Both surfaces must verify the intended manifest identity and 13-skill
inventory. Neither requires copying skill content into consumer repositories.

The operational rollout ledger may live in Linear, but it conforms to the
installed schema and cannot carry load-bearing contract or rationale unavailable
to an installed consumer.
