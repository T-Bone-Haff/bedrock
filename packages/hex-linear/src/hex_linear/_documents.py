"""Fixed provider documents; caller text is supplied only as variables."""
ISSUE = """id identifier title description url updatedAt
    team { id } state { id name type } priority assignee { id } parent { id }
    dueDate archivedAt completedAt creator { id }"""
COMMENT = "id body createdAt user { id } issue { id identifier }"
RELATION = "id type issue { id } relatedIssue { id } archivedAt"
PAGE_INFO = "pageInfo { endCursor hasNextPage }"
DOCUMENTS = {
    "Viewer": "query Viewer { viewer { id name } }",
    "GetIssue": f"query GetIssue($id: String!) {{ issue(id: $id) {{ {ISSUE} }} }}",
    "ListIssues": f"""query ListIssues($first: Int!, $after: String, $filter: IssueFilter, $includeArchived: Boolean!) {{
        issues(first: $first, after: $after, filter: $filter, includeArchived: $includeArchived) {{ nodes {{ {ISSUE} }} {PAGE_INFO} }}
    }}""",
    "CreateIssue": f"""mutation CreateIssue($input: IssueCreateInput!) {{
        issueCreate(input: $input) {{ success issue {{ {ISSUE} }} }}
    }}""",
    "UpdateIssue": f"""mutation UpdateIssue($id: String!, $input: IssueUpdateInput!) {{
        issueUpdate(id: $id, input: $input) {{ success issue {{ {ISSUE} }} }}
    }}""",
    "ListComments": f"""query ListComments($id: String!, $first: Int!, $after: String) {{
        issue(id: $id) {{ id identifier comments(first: $first, after: $after) {{ nodes {{ {COMMENT} }} {PAGE_INFO} }} }}
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
    "ListIssueLabels": f"""query ListIssueLabels($id: String!, $first: Int!, $after: String, $includeArchived: Boolean!) {{
        issue(id: $id) {{ id labels(first: $first, after: $after, includeArchived: $includeArchived) {{
            nodes {{ id name }} {PAGE_INFO}
        }} }}
    }}""",
    "CreateRelation": f"""mutation CreateRelation($input: IssueRelationCreateInput!) {{
        issueRelationCreate(input: $input) {{ success issueRelation {{ {RELATION} }} }}
    }}""",
    "DeleteRelation": """mutation DeleteRelation($id: String!) {
        issueRelationDelete(id: $id) { success entityId }
    }""",
}
for operation, field in (("ListOutgoingRelations", "relations"), ("ListIncomingRelations", "inverseRelations")):
    DOCUMENTS[operation] = f"""query {operation}($id: String!, $first: Int!, $after: String, $includeArchived: Boolean!) {{
        issue(id: $id) {{ id {field}(first: $first, after: $after, includeArchived: $includeArchived) {{
            nodes {{ {RELATION} }} {PAGE_INFO}
        }} }}
    }}"""
