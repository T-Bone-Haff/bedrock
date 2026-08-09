# HEB-108 independent routing review

Two isolated forward-routing passes reviewed only the final skill frontmatter and the shared prompts in `tests/fixtures/routing.yaml`. The reviewers were not given the remediation diagnosis or implementation history. After one adversarial pass identified dual textual ownership of direct construct-spec authorship, `author-decision-record` was aligned with its body: it selects the doctype but routes construct-spec authorship and amendment to `author-construct-spec`.

## Results

- Both reviewers independently evaluated all 31 cases against the current catalog.
- Both reviews matched all 31 declared primary routes.
- The `author-construct-spec-negative` case correctly selected no Bedrock skill.
- Every negative case avoided its excluded skill.
- All five overlap cases selected the declared primary route.
- The reported construct-spec ambiguity was corrected; no known fixture ambiguity or misroute remains.

This review is independent description-level evidence. It does not substitute for the authenticated Claude Code adapter run required by the routing workflow.
