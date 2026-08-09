# HEB-108 Wave 1 baseline

Captured from `main` at `aa772938f50cedc498a4917422961162bc09b9b2` on 2026-08-09 before remediation.

## Strict host validation

Command:

```sh
claude plugin validate --strict plugins/bedrock
```

Result: failed. Claude Code 2.1.224 reported invalid YAML frontmatter for nine skills:

- `agent-code`
- `app-delivery-pipeline`
- `application-code`
- `author-execution-relay`
- `author-standard`
- `debug`
- `frontend-code`
- `infrastructure-code`
- `testing`

## Description limits

Direct measurement found six descriptions above the 1,024-character host limit:

| Skill | Characters |
| --- | ---: |
| frontend-code | 1,752 |
| author-construct-spec | 1,406 |
| app-delivery-pipeline | 1,360 |
| agent-code | 1,140 |
| code-review | 1,117 |
| author-execution-relay | 1,028 |

The ratified ledger recorded five over-limit descriptions. This evidence preserves the observed disk delta without changing any finding disposition.

## Missing enforcement

- No repository CI workflow ran strict plugin validation.
- No deterministic package validator existed.
- No positive, negative, or overlap routing fixtures existed.
- No isolated install/reload smoke test existed.
