from typing import Protocol


class Operation(Protocol):
    def execute(self) -> str:
        raise Exception("Not implemented yet")
