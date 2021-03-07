import re
from typing import Match

from .base import InputPartSpec
from roll_witch.rolling.roller import RollSpec


class DiceSpec(InputPartSpec):
    def __init__(self) -> None:
        super().__init__()
        self.regex = re.compile(r"([+\-*/])*(\d*)d(\d+)", re.IGNORECASE)
        self.name = "dice_spec"

    def apply(self, match: Match):
        if match.group(1):
            operation = match.group(1)
        else:
            operation = "+"

        if match.group(2):
            dice_count = int(match.group(2))
        else:
            dice_count = 1

        return RollSpec(
            dice_count=int(dice_count),
            dice_sides=int(match.group(3)),
            operation=operation,
        )


class DiceWithModifierSpec(InputPartSpec):
    def __init__(self) -> None:
        super().__init__()
        self.regex = re.compile(r"(\d*)d(\d+)\s*([+\-])*([0-9]*)", re.IGNORECASE)
        self.name = "modifier_and_dice_spec"

    def apply(self, match: Match):
        if match.group(3):
            if match.group(3) == "+":
                modifier = int(match.group(4))
            else:
                modifier = -int(match.group(4))
        else:
            modifier = 0

        if match.group(1):
            dice_count = int(match.group(1))
        else:
            dice_count = 1

        return RollSpec(
            dice_count=dice_count,
            dice_sides=int(match.group(2)),
            modifier=modifier,
            target_number=None,
        )
