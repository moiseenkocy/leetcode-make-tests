"""Data models."""

from dataclasses import dataclass


@dataclass
class LeetCodeAPIResponse:
    """Data model for LeetCode API response."""

    question_id: int
    title_slug: str
    title: str
    description: str
    test_cases: list[str]
    metadata: str
