from typing import Protocol, Pattern, Match
import re

from roll_witch.dice_bot.spec import RollSpec


class InputPartSpec():
    regex: Pattern
    name: str

    def matches_pattern(self, part_string):
        return self.regex.fullmatch(part_string)

    def apply(self, target_match: Match):
        return None


class DiceSpec(InputPartSpec):
    def __init__(self) -> None:
        super().__init__()
        self.regex = re.compile(r"([+\-])*(\d*)d(\d+)")
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


class TargetSpec(InputPartSpec):
    def __init__(self) -> None:
        super().__init__()
        self.regex = re.compile(r"t([\-]*[0-9]+)")
        self.name = "target_spec"

    def apply(self, match: Match):
        return RollSpec(target_number=int(match.group(1)), operation=None)
