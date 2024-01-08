from typing import Protocol
from .targetable import Targetable


class Result(Protocol):
    total: int
    roll_total: int
    spec: Targetable
    met_target: bool


class OperationResult(Protocol):
    rolls: [Result]
    total: int
    roll_total: int
    spec: Targetable
    met_target: bool

    def append_roll_result(self, result: Result) -> None:
        raise Exception("Not implemented yet")

    def had_target(self) -> bool:
        return False
