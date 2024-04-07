from leetcode_make_tests.client import LeetCodeClient
from leetcode_make_tests.models import FunctionArg, FunctionSignature
from leetcode_make_tests.models.types import ArgType, BaseType

SAMPLE_METADATA = '{\r\n  "name": "merge",\r\n  "params": [\r\n    {\r\n      "name": "nums1",\r\n      "type": "integer[]",\r\n      "implicitsizeparam": false\r\n    },\r\n    {\r\n      "name": "m",\r\n      "type": "integer"\r\n    },\r\n    {\r\n      "name": "nums2",\r\n      "type": "integer[]",\r\n      "implicitsizeparam": false\r\n    },\r\n    {\r\n      "name": "n",\r\n      "type": "integer"\r\n    }\r\n  ],\r\n  "return": {\r\n    "type": "void"\r\n  },\r\n  "output": {\r\n    "paramindex": 0\r\n  }\r\n}'  # noqa: E501


def test__parse_function_signature_success() -> None:
    """Test the successful exec of _parse_function_signature method."""
    result = LeetCodeClient._parse_function_signature(SAMPLE_METADATA)

    assert result == FunctionSignature(
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
