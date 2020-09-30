import re
from typing import Match

from roll_witch.dice_bot.input.spec import InputPartSpec
from roll_witch.dice_bot.spec import RollSpec


class TargetSpec(InputPartSpec):
    def __init__(self) -> None:
        super().__init__()
        self.regex = re.compile(r"t([\-]*[0-9]+)")
        self.name = "target_spec"

    def apply(self, match: Match):
        return RollSpec(target_number=int(match.group(1)), operation=None)


class TargetWithDiceSpec(InputPartSpec):
    def __init__(self) -> None:
        super().__init__()
        self.regex = re.compile(r"(\d*)d(\d+)\st([\-]*[0-9]+)")
        self.name = "target_and_dice_spec"

    def apply(self, match: Match):
        if match.group(1):
            dice_count = int(match.group(1))
        else:
            dice_count = 1

        return RollSpec(
            dice_count=int(dice_count),
            dice_sides=int(match.group(2)),
            modifier=0,
            target_number=int(match.group(3)),
        )
