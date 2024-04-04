"""Data models."""

from dataclasses import dataclass
from enum import Enum


@dataclass
class LeetCodeAPIResponse:
    """LeetCode API response."""

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
        """Return python annotation for this base type."""
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


class ArgType:
    """Argument type."""

    def __init__(self, base_type: BaseType, list_depth: int) -> None:
        self.base_type = base_type
        self.list_depth = list_depth

    def to_python(self) -> str:
        """Return python annotation for this type."""
        if not self.list_depth:
            return self.base_type.to_python()

        return (
            "list[" * self.list_depth
            + self.base_type.to_python()
            + "]" * self.list_depth
        )


class FunctionArg:
    """Function Argument."""

    def __init__(self, name: str, arg_type: ArgType) -> None:
        self.name = name
        self.arg_type = arg_type
