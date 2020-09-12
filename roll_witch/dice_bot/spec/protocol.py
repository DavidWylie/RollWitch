from typing import Protocol


class Targetable(Protocol):
    target_number: int

    def has_target(self) -> bool:
        return False


class DiceSet(Protocol):
    dice_sides: int
    dice_count: int


class DiceModifier(Protocol):
    dice_modifier: int

    def has_modifier(self) -> bool:
        return False
