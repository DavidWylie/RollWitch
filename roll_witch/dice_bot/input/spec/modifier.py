import re
from typing import Match

from roll_witch.dice_bot.input.spec import InputPartSpec
from roll_witch.dice_bot.spec import RollSpec


class ModifierSpec(InputPartSpec):
    def __init__(self) -> None:
        super().__init__()
        self.regex = re.compile(r"([+\-])*([0-9]+)")
        self.name = "modifier_spec"

    def apply(self, match: Match):
        if match.group(1) == "+":
            modifier = int(match.group(2))
            return RollSpec(modifier=modifier, operation="+")
        elif match.group(1) == "-":
            modifier = int(match.group(2))
            return RollSpec(modifier=modifier, operation="-")
        else:
            modifier = int(match.group(2))
            return RollSpec(modifier=modifier, operation="+")
