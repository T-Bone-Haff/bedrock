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


@dataclass(frozen=True)
class Comment:
    id: str
    body: str
    created_at: str


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


class IssueUpdate(TypedDict, total=False):
    title: str
    description: str | None
    stateId: str
    assigneeId: str | None
    priority: int


@dataclass(frozen=True)
class IssueFilter:
    team_id: str | None = None
    assignee_id: str | None = None
    state_id: str | None = None
