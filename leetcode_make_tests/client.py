"""LeetCode Client."""

import json

from leetcode_make_tests.api import LeetCodeAPI
from leetcode_make_tests.models.functions import FunctionArg, FunctionSignature
from leetcode_make_tests.models.problem import LeetCodeProblem
from leetcode_make_tests.models.types import ArgType
from leetcode_make_tests.models.unittests import UnitTest


class LeetCodeClient:
    """A LeetCode client for fetching data from the API and parsing it."""

    @classmethod
    def get_problem(cls, title_slug: str) -> LeetCodeProblem:
        """Fetch problem from API and process its data."""
        api_response = LeetCodeAPI.get_problem(title_slug)

        if api_response is None:
            return None

        question_id = api_response.question_id
        title_slug = api_response.title_slug
        title = api_response.title

        function_signature = cls._parse_function_signature(api_response.metadata)
        unit_tests = [
            cls._parse_unit_test(unit_test, function_signature)
            for unit_test in api_response.test_cases
        ]

        return LeetCodeProblem(
            question_id=question_id,
            title_slug=title_slug,
            title=title,
            function_signature=function_signature,
            unit_tests=unit_tests,
        )

    @staticmethod
    def _parse_function_signature(metadata: str) -> FunctionSignature:
        """Parse function signature from API response metadata."""
        metadata = json.loads(metadata)

        return FunctionSignature(
            name=metadata["name"],
            arg_list=[
                FunctionArg(
                    name=arg["name"],
                    arg_type=ArgType.from_metadata(arg["type"]),
                )
                for arg in metadata["params"]
            ],
            return_type=ArgType.from_metadata(metadata["return"]["type"]),
        )

    @staticmethod
    def _parse_unit_test(
        test_case: str,
        function_signature: FunctionSignature,
    ) -> UnitTest:
        return UnitTest(arg_values=[], return_value=None)
