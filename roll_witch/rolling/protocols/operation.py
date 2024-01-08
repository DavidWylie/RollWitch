from typing import Protocol
from rolling.protocols.result import OperationResult


class Operation(Protocol):
    name: str
    def execute(self, roll_string: str, user: str) -> OperationResult:
        raise Exception("Not implemented yet")

    def format_output(self, roll_result, user) -> str:
        raise Exception("Not implemented yet")