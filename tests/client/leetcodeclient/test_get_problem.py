from pytest_mock import MockerFixture

from leetcode_make_tests.client import LeetCodeClient
from leetcode_make_tests.models import (
    ArgType,
    BaseType,
    FunctionArg,
    FunctionSignature,
    LeetCodeAPIResponse,
    LeetCodeProblem,
    UnitTest,
)

SAMPLE_FUNCTION_SIGNATURE = FunctionSignature(
    name="function_name",
    arg_list=[
        FunctionArg(
            name="elems", arg_type=ArgType(base_type=BaseType.DOUBLE, list_depth=1),
        ),
        FunctionArg(
            name="n", arg_type=ArgType(base_type=BaseType.INTEGER, list_depth=0),
        ),
    ],
    return_type=ArgType(base_type=BaseType.INTEGER, list_depth=0),
)

SAMPLE_UNIT_TESTS = [
    UnitTest(arg_values=[[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3], return_value=None),
    UnitTest(arg_values=[[1], 1, [], 0], return_value=None),
    UnitTest(arg_values=[[0], 0, [1], 1], return_value=None),
]


def test_get_problem_success(mocker: MockerFixture) -> None:
    """Test the successful exec of get_problem method."""
    mocker.patch(
        "leetcode_make_tests.api.LeetCodeAPI.get_problem",
        return_value=LeetCodeAPIResponse(
            question_id=123456,
            title_slug="__TITLE_SLUG__",
            title="__TITLE__",
            description="__CONTENT__",
            test_cases=["__CASE_1__", "__CASE_2__", "__CASE_3__"],
            metadata="__METADATA__",
        ),
    )
    mocker.patch(
        "leetcode_make_tests.client.LeetCodeClient._parse_function_signature",
        return_value=SAMPLE_FUNCTION_SIGNATURE,
    )
    mocker.patch(
        "leetcode_make_tests.client.LeetCodeClient._parse_unit_test",
        side_effect=SAMPLE_UNIT_TESTS,
    )

    result = LeetCodeClient.get_problem("__TITLE_SLUG__")

    assert result == LeetCodeProblem(
        question_id=123456,
        title_slug="__TITLE_SLUG__",
        title="__TITLE__",
        function_signature=SAMPLE_FUNCTION_SIGNATURE,
        unit_tests=SAMPLE_UNIT_TESTS,
    )


def test_get_problem_doesnt_exist(mocker: MockerFixture) -> None:
    """Test case for non-existent problem."""
    mocker.patch("leetcode_make_tests.api.LeetCodeAPI.get_problem", return_value=None)

    result = LeetCodeClient.get_problem("adadadssasd")

    assert result is None
