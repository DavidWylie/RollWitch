from roll_witch.dice_bot.spec import RollSpec, OperationSpec
from typing import Match
import re

_instance = None


class TokenInputParser:
    def __init__(self) -> None:
        super().__init__()
        self.spec_regex = {
            "dice_spec": re.compile(r"([+\-])*(\d*)d(\d+)"),
            "modifier_spec": re.compile(r"([+\-])*([0-9]+)"),
            "target_spec": re.compile(r"t([\-]*[0-9]+)"),
        }
        self.matchers = {
            "dice_spec": self.create_dice_matcher(),
            "modifier_spec": self.create_modifier_matcher(),
            "target_spec": self.create_target_matcher(),
        }

    @staticmethod
    def create_dice_matcher():
        def match(match: Match):
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

        return match

    @staticmethod
    def create_modifier_matcher():
        def match(match: Match):
            if match.group(1) == "+":
                modifier = int(match.group(2))
                return RollSpec(modifier=modifier, operation="+")
            elif match.group(1) == "-":
                modifier = int(match.group(2))
                return RollSpec(modifier=modifier, operation="-")
            else:
                modifier = int(match.group(2))
                return RollSpec(modifier=modifier, operation="+")
        return match

    @staticmethod
    def create_target_matcher():
        def match(match: Match):
            return RollSpec(target_number=int(match.group(1)), operation=None)

        return match

    def parse(self, roll_string: str):
        parts = roll_string.replace(" + ", "+").replace("+", " +").split()
        spec = OperationSpec()
        for part in parts:
            part_spec = self.parse_part(part)
            spec.add_part(part_spec)
        return spec

    def parse_part(self, part_string):
        for spec_name, regex in self.spec_regex.items():
            match = regex.fullmatch(part_string)
            if match:
                matcher = self.matchers.get(spec_name)
                return matcher(match)
        raise Exception(f"Roll What?  {part_string} is not valid Try again  e.g. roll 1d10 +10 or roll 1d6 t6")


def get_token_parser() -> TokenInputParser:
    global _instance

    if _instance is None:
        _instance = TokenInputParser()

    return _instance
