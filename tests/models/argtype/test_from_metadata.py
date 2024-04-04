import pytest

from leetcode_make_tests.models import ArgType, BaseType


@pytest.mark.parametrize(
    ("metadata_arg_type", "expected_result"),
    [
        ("integer", ArgType(base_type=BaseType.INTEGER, list_depth=0)),
        ("double[]", ArgType(base_type=BaseType.DOUBLE, list_depth=1)),
        ("string[][][][]", ArgType(base_type=BaseType.STRING, list_depth=4)),
        ("list<character>", ArgType(base_type=BaseType.CHARACTER, list_depth=1)),
        (
            "list<list<list<boolean>>>",
            ArgType(base_type=BaseType.BOOLEAN, list_depth=3),
        ),
    ],
)
def test_argtype_from_metadata_success(
    metadata_arg_type: str, expected_result: ArgType
) -> None:
    """Test successful calculation of arg_type from metadata format."""
    result = ArgType.from_metadata(metadata_arg_type)

    assert result == expected_result
