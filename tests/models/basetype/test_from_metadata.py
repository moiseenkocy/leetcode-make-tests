import pytest

from leetcode_make_tests.models import BaseType


@pytest.mark.parametrize(
    ("metadata_base_type", "expected_result"),
    [
        ("void", BaseType.VOID),
        ("boolean", BaseType.BOOLEAN),
        ("integer", BaseType.INTEGER),
        ("double", BaseType.DOUBLE),
        ("character", BaseType.CHARACTER),
        ("string", BaseType.STRING),
        ("ListNode", BaseType.LISTNODE),
        ("TreeNode", BaseType.TREENODE),
    ],
)
def test_basetype_from_metadata_success(
    metadata_base_type: str, expected_result: BaseType
) -> None:
    """Test successful calculation of base_type from metadata format."""
    result = BaseType.from_metadata(metadata_base_type)

    assert result == expected_result
