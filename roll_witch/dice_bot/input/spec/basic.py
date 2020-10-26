import re
from math import ceil
from typing import Match

from roll_witch.dice_bot.input.spec import InputPartSpec
from roll_witch.dice_bot.spec import RollSpec


class BasicRpgSpec(InputPartSpec):
    def __init__(self) -> None:
        super().__init__()
        self.regex = re.compile(r"t(\d*)\s*(easy|hard)*")
        self.name = "basic_spec"

    def apply(self, match: Match):
        target_number = -int(match.group(1))

        if match.group(2):
            modifier = match.group(2)
            if modifier == "hard":
                target_number = ceil(target_number / 2)
            elif modifier == "easy":
                target_number = target_number * 2

        return RollSpec(
            dice_count=1,
            dice_sides=100,
            modifier=0,
            target_number=target_number,
        )
