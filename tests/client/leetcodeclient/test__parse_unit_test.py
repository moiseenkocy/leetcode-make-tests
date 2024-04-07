import pytest

from leetcode_make_tests.client import LeetCodeClient
from leetcode_make_tests.models import UnitTest
from leetcode_make_tests.models.functions import FunctionArg, FunctionSignature
from leetcode_make_tests.models.types import ArgType, BaseType

SAMPLE_FUNCTION_SIGNATURE = FunctionSignature(
    name="merge",
    arg_list=[
        FunctionArg(
            name="nums1",
            arg_type=ArgType(base_type=BaseType.INTEGER, list_depth=1),
        ),
        FunctionArg(
            name="m",
            arg_type=ArgType(base_type=BaseType.INTEGER),
        ),
        FunctionArg(
            name="nums2",
            arg_type=ArgType(base_type=BaseType.INTEGER, list_depth=1),
        ),
        FunctionArg(
            name="n",
            arg_type=ArgType(base_type=BaseType.INTEGER),
        ),
    ],
    return_type=ArgType(base_type=BaseType.VOID),
)


@pytest.mark.skip()
@pytest.mark.parametrize(
    ("test_case", "function_signature", "expected_result"),
    [
        (
            "[1,2,3,0,0,0]\n3\n[2,5,6]\n3",
            SAMPLE_FUNCTION_SIGNATURE,
            UnitTest(
                arg_values=[[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
                return_value=None,
            ),
        ),
        (
            "[1]\n1\n[]\n0",
            SAMPLE_FUNCTION_SIGNATURE,
            UnitTest(arg_values=[[1], 1, [], 0], return_value=None),
        ),
        (
            "[0]\n0\n[1]\n1",
            SAMPLE_FUNCTION_SIGNATURE,
            UnitTest(arg_values=[[0], 0, [1], 1], return_value=None),
        ),
    ],
)
def test__parse_unit_test_success(
    test_case: str,
    function_signature: FunctionSignature,
    expected_result: UnitTest,
) -> None:
    """Test the successful exec of _parse_unit_test method."""
    result = LeetCodeClient._parse_unit_test(test_case, function_signature)

    assert result == expected_result
