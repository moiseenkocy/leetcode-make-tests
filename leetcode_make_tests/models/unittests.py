"""Data model for describing unit tests."""

from dataclasses import dataclass
from typing import Any


@dataclass
class UnitTest:
    """LeetCode Unit Test."""

    arg_values: list[Any]
    return_value: Any
