from typing import Protocol


class DiceModifier(Protocol):
    dice_modifier: int

    def has_modifier(self) -> bool:
        return False
