"""The small supported subset of Linear's model, not its entire schema."""
from dataclasses import dataclass
from typing import Generic, NotRequired, TypeVar, TypedDict


@dataclass(frozen=True)
class Issue:
    id: str
    identifier: str
    title: str
    description: str | None
    url: str
    updated_at: str
    context: "IssueContext | None" = None


@dataclass(frozen=True)
class Comment:
    id: str
    body: str
    created_at: str
    attribution: "CommentAttribution | None" = None


@dataclass(frozen=True)
class Reference:
    id: str
    name: str


T = TypeVar("T")


@dataclass(frozen=True)
class Page(Generic[T]):
    items: tuple[T, ...]
    end_cursor: str | None
    has_next_page: bool


class IssueCreate(TypedDict):
    teamId: str
    title: str
    description: NotRequired[str]
    stateId: NotRequired[str]
    assigneeId: NotRequired[str]
    priority: NotRequired[int]
    parentId: NotRequired[str]


class IssueUpdate(TypedDict, total=False):
    title: str
    description: str | None
    stateId: str
    assigneeId: str | None
    priority: int
    parentId: str | None


@dataclass(frozen=True)
class IssueFilter:
    team_id: str | None = None
    assignee_id: str | None = None
    state_id: str | None = None
    parent_id: str | None = None


@dataclass(frozen=True)
class WorkflowState:
    id: str
    name: str
    type: str


@dataclass(frozen=True)
class IssueContext:
    """Complete scalar context from a provider result; labels are paginated separately."""
    team_id: str
    state: WorkflowState
    priority: int
    assignee_id: str | None
    parent_id: str | None
    due_date: str | None
    archived_at: str | None
    completed_at: str | None
    creator_id: str | None


@dataclass(frozen=True)
class CommentAttribution:
    issue_id: str
    author_id: str | None


@dataclass(frozen=True)
class IssueRelation:
    id: str
    type: str
    issue_id: str
    related_issue_id: str
    archived_at: str | None
