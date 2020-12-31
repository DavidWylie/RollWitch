from typing import Protocol
from .operation import Operation


class OperationFactory(Protocol):
    def get_roll_operation(
        self, roll_type: str, roll_string: str, user: str
    ) -> Operation:
        raise Exception("Not implemented yet")
