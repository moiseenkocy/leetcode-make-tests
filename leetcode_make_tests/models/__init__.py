"""Data models."""

from dataclasses import dataclass
from typing import Any

from leetcode_make_tests.models.functions import FunctionSignature


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
