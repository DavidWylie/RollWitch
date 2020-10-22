import re
from typing import Match

from roll_witch.dice_bot.input.spec import InputPartSpec
from roll_witch.dice_bot.spec import RollSpec


class BasicRpgSpec(InputPartSpec):
    def __init__(self) -> None:
        super().__init__()
        self.regex = re.compile(r"t(\d*) [easy,hard]]")
        self.name = "basic_spec"

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
            dice_count=1,
            dice_sides=100,
            modifier=0,
            target_number=None,
        )