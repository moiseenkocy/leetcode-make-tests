"""Data models."""

from dataclasses import dataclass
from typing import Any, Self

from leetcode_make_tests.models.types import ArgType


class FunctionArg:
    """Function Argument."""

    def __init__(self, name: str, arg_type: ArgType) -> None:
        self.name = name
        self.arg_type = arg_type

    def __eq__(self, x: Self) -> bool:
        """Implement equality operator."""
        return self.name == x.name and self.arg_type == x.arg_type


@dataclass
class FunctionSignature:
    """Function definition."""

    name: str
    arg_list: list[FunctionArg]
    return_type: ArgType


@dataclass
class LeetCodeAPIResponse:
    """LeetCode API response."""

    question_id: int
    title_slug: str
    title: str
    description: str
    test_cases: list[str]
    metadata: str


@dataclass
class UnitTest:
    """LeetCode Unit Test."""

    arg_values: list[Any]
    return_value: Any


@dataclass
class LeetCodeProblem:
    """LeetCode Problem."""

    question_id: int
    title_slug: str
    title: str
    function_signature: FunctionSignature
    unit_tests: list[UnitTest]
