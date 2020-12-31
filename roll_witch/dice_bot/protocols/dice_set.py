from typing import Protocol


class DiceSet(Protocol):
    dice_sides: int
    dice_count: int
