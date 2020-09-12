from roll_witch.dice_bot.spec import RollSpec
from typing import Match
import re


_instance = None


class RegexInputParser:
    def __init__(self) -> None:
        super().__init__()
        self.spec_regex = {
            "target_spec": re.compile(r"(\d*)d(\d+)\st([\-]*[0-9]+)"),
            "modifier_spec": re.compile(r"(\d*)d(\d+)\s*([+\-])*([0-9]*)"),
        }
        self.matchers = {
            "target_spec": self.create_target_matcher(),
            "modifier_spec": self.create_modifier_matcher(),
        }

    @staticmethod
    def create_target_matcher():
        def match(target_match: Match):
            if target_match.group(1):
                dice_count = int(target_match.group(1))
            else:
                dice_count = 1

            return RollSpec(
                dice_count=int(dice_count),
                dice_sides=int(target_match.group(2)),
                modifier=0,
                target_number=int(target_match.group(3)),
            )

        return match

    @staticmethod
    def create_modifier_matcher():
        def match(modifier_match: Match):
            if modifier_match.group(3):
                if modifier_match.group(3) == "+":
                    modifier = int(modifier_match.group(4))
                else:
                    modifier = -int(modifier_match.group(4))
            else:
                modifier = 0

            if modifier_match.group(1):
                dice_count = int(modifier_match.group(1))
            else:
                dice_count = 1

            return RollSpec(
                dice_count=dice_count,
                dice_sides=int(modifier_match.group(2)),
                modifier=modifier,
                target_number=None,
            )

        return match

    def parse(self, roll_string: str):
        for spec_name, regex in self.spec_regex.items():
            match = regex.fullmatch(roll_string)
            if match:
                matcher = self.matchers.get(spec_name)
                return matcher(match)

        raise Exception("Roll What?  Try again  e.g. roll 1d10 +10 or roll 1d6 t6")


def get_regex_parser() -> RegexInputParser:
    global _instance

    if _instance is None:
        _instance = RegexInputParser()

    return _instance
