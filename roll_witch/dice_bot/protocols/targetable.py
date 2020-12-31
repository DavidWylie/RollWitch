from typing import Protocol


class Targetable(Protocol):
    target_number: int

    def has_target(self) -> bool:
        return False
