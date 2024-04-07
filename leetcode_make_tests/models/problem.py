"""Data model for describing LeetCode problem."""

from dataclasses import dataclass

from leetcode_make_tests.models.functions import FunctionSignature
from leetcode_make_tests.models.unittests import UnitTest


@dataclass
class LeetCodeProblem:
    """LeetCode Problem."""

    question_id: int
    title_slug: str
    title: str
    function_signature: FunctionSignature
    unit_tests: list[UnitTest]
