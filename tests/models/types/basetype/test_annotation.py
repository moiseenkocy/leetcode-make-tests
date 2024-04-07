import pytest

from leetcode_make_tests.models.types import BaseType


@pytest.mark.parametrize(
    ("base_type", "expected_result"),
    [
        (BaseType.VOID, "None"),
        (BaseType.BOOLEAN, "bool"),
        (BaseType.INTEGER, "int"),
        (BaseType.DOUBLE, "float"),
        (BaseType.CHARACTER, "str"),
        (BaseType.STRING, "str"),
        (BaseType.LISTNODE, "ListNode"),
        (BaseType.TREENODE, "TreeNode"),
    ],
)
def test_basetype_annotation_success(base_type: BaseType, expected_result: str) -> None:
    """Test successful calculation of type annotation."""
    result = base_type.annotation

    assert result == expected_result
