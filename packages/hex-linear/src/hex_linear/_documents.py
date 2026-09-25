"""Fixed provider documents; caller text is supplied only as variables."""
ISSUE = "id identifier title description url updatedAt"
COMMENT = "id body createdAt"
PAGE_INFO = "pageInfo { endCursor hasNextPage }"
DOCUMENTS = {
    "Viewer": "query Viewer { viewer { id name } }",
    "GetIssue": f"query GetIssue($id: String!) {{ issue(id: $id) {{ {ISSUE} }} }}",
    "ListIssues": f"""query ListIssues($first: Int!, $after: String, $filter: IssueFilter) {{
        issues(first: $first, after: $after, filter: $filter) {{ nodes {{ {ISSUE} }} {PAGE_INFO} }}
    }}""",
    "CreateIssue": f"""mutation CreateIssue($input: IssueCreateInput!) {{
        issueCreate(input: $input) {{ success issue {{ {ISSUE} }} }}
    }}""",
    "UpdateIssue": f"""mutation UpdateIssue($id: String!, $input: IssueUpdateInput!) {{
        issueUpdate(id: $id, input: $input) {{ success issue {{ {ISSUE} }} }}
    }}""",
    "ListComments": f"""query ListComments($id: String!, $first: Int!, $after: String) {{
        issue(id: $id) {{ comments(first: $first, after: $after) {{ nodes {{ {COMMENT} }} {PAGE_INFO} }} }}
    }}""",
    "CreateComment": f"""mutation CreateComment($input: CommentCreateInput!) {{
        commentCreate(input: $input) {{ success comment {{ {COMMENT} }} }}
    }}""",
    "ListTeams": f"""query ListTeams($first: Int!, $after: String) {{
        teams(first: $first, after: $after) {{ nodes {{ id name }} {PAGE_INFO} }}
    }}""",
    "ListStates": f"""query ListStates($id: String!, $first: Int!, $after: String) {{
        team(id: $id) {{ states(first: $first, after: $after) {{ nodes {{ id name }} {PAGE_INFO} }} }}
    }}""",
    "ListUsers": f"""query ListUsers($first: Int!, $after: String) {{
        users(first: $first, after: $after) {{ nodes {{ id name }} {PAGE_INFO} }}
    }}""",
}
