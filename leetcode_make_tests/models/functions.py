from dataclasses import dataclass
from typing import Self

from leetcode_make_tests.models.types import ArgType


class FunctionArg:
    """Function Argument."""

    def __init__(self, name: str, arg_type: ArgType) -> None:
        self.name = name
        self.arg_type = arg_type

    def __eq__(self, x: Self) -> bool:
        """Implement equality operator."""
        return self.name == x.name and self.arg_type == x.arg_type


@dataclass
class FunctionSignature:
    """Function definition."""

    name: str
    arg_list: list[FunctionArg]
    return_type: ArgType
