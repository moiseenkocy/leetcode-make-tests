import pytest

from leetcode_make_tests.models import ArgType, BaseType


@pytest.mark.parametrize(
    ("arg_type", "expected_result"),
    [
        (ArgType(base_type=BaseType.BOOLEAN, list_depth=0), "bool"),
        (ArgType(base_type=BaseType.STRING, list_depth=1), "list[str]"),
        (
            ArgType(base_type=BaseType.INTEGER, list_depth=5),
            "list[list[list[list[list[int]]]]]",
        ),
    ],
)
def test_argtype_annotation_success(arg_type: ArgType, expected_result: str) -> None:
    """Test successful calculation of type annotation."""
    result = arg_type.annotation

    assert result == expected_result
