import re
from typing import Match

from .base import InputPartSpec
from roll_witch.rolling.roller import RollSpec


class ModifierSpec(InputPartSpec):
    def __init__(self) -> None:
        super().__init__()
        self.regex = re.compile(r"([+\-*/])*([0-9]+)")
        self.name = "modifier_spec"

    def apply(self, match: Match):
        operator = match.group(1)
        operators = ["+", "-", "*", "/"]
        if operator in operators:
            modifier = int(match.group(2))
            return RollSpec(modifier=modifier, operation=operator)
        else:
            modifier = int(match.group(2))
            return RollSpec(modifier=modifier, operation="+")
