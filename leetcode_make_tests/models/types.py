import re
from enum import Enum
from typing import Self


class BaseType(Enum):
    """Base types for arguments."""

    VOID = 0
    BOOLEAN = 1
    INTEGER = 2
    DOUBLE = 3
    CHARACTER = 4
    STRING = 5
    LISTNODE = 6
    TREENODE = 7

    @property
    def annotation(self) -> str:
        """Return python annotation for this base type."""
        return {
            BaseType.VOID: "None",
            BaseType.BOOLEAN: "bool",
            BaseType.INTEGER: "int",
            BaseType.DOUBLE: "float",
            BaseType.CHARACTER: "str",
            BaseType.STRING: "str",
            BaseType.LISTNODE: "ListNode",
            BaseType.TREENODE: "TreeNode",
        }[self]

    @staticmethod
    def from_metadata(metadata_base_type: str) -> Self:
        """Parse base_type from metadata format."""
        try:
            return {
                "void": BaseType.VOID,
                "boolean": BaseType.BOOLEAN,
                "integer": BaseType.INTEGER,
                "double": BaseType.DOUBLE,
                "character": BaseType.CHARACTER,
                "string": BaseType.STRING,
                "ListNode": BaseType.LISTNODE,
                "TreeNode": BaseType.TREENODE,
            }[metadata_base_type]
        except KeyError as exc:
            raise ValueError from exc


class ArgType:
    """Argument type."""

    def __init__(self, base_type: BaseType, list_depth: int = 0) -> None:
        self.base_type = base_type
        self.list_depth = list_depth

    def __eq__(self, x: Self) -> bool:
        """Implement equality operator."""
        return self.base_type == x.base_type and self.list_depth == x.list_depth

    @property
    def annotation(self) -> str:
        """Return python annotation for this type."""
        if not self.list_depth:
            return self.base_type.annotation

        return (
            "list[" * self.list_depth
            + self.base_type.annotation
            + "]" * self.list_depth
        )

    @staticmethod
    def from_metadata(metadata_arg_type: str) -> Self:
        """Parse arg_type from metadata format."""
        m = re.match(r"([A-Za-z]+)(?:\[\])+$", metadata_arg_type)
        if m:
            return ArgType(
                base_type=BaseType.from_metadata(m.group(1)),
                list_depth=metadata_arg_type.count("[]"),
            )

        m = re.match(r"^(?:list<)+([A-Za-z]+)>+$", metadata_arg_type)
        if m:
            return ArgType(
                base_type=BaseType.from_metadata(m.group(1)),
                list_depth=metadata_arg_type.count("list<"),
            )

        return ArgType(
            base_type=BaseType.from_metadata(metadata_arg_type),
        )
