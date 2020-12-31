from typing import Protocol
from .targetable import Targetable


class Result(Protocol):
    total: int
    roll_total: int
    spec: Targetable
    met_target: bool
