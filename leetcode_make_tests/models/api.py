"""Data models for describing API responses."""

from dataclasses import dataclass


@dataclass
class LeetCodeAPIResponse:
    """LeetCode API response."""

    question_id: int
    title_slug: str
    title: str
    description: str
    test_cases: list[str]
    metadata: str
