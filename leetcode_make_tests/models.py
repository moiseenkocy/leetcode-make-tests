"""Data models."""

from dataclasses import dataclass
from enum import Enum


@dataclass
class LeetCodeAPIResponse:
    """Data model for LeetCode API response."""

    question_id: int
    title_slug: str
    title: str
    description: str
    test_cases: list[str]
    metadata: str


class BaseType(Enum):
    """Base types for arguments."""

    VOID = 0
    BOOLEAN = 1
    INTEGER = 2
    DOUBLE = 3
    CHARACTER = 4
    STRING = 5
    LISTNODE = 6
    TREENODE = 7

    def to_python(self) -> str:
        """Convert to python annotated type."""
        return {
            BaseType.VOID: "None",
            BaseType.BOOLEAN: "bool",
            BaseType.INTEGER: "int",
            BaseType.DOUBLE: "float",
            BaseType.CHARACTER: "str",
            BaseType.STRING: "str",
            BaseType.LISTNODE: "ListNode",
            BaseType.TREENODE: "TreeNode",
        }[self]
