"""Tests for leetcode_make_tests.models."""

import pytest

from leetcode_make_tests.models import BaseType


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
def test_basetype_to_python_success(base_type: BaseType, expected_result: str) -> None:
    """Test successful convertation to python types."""
    result = base_type.to_python()

    assert result == expected_result
