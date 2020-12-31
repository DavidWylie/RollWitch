from typing import Pattern, Match

from roll_witch.rolling.roller import RollSpec


class InputPartSpec:
    regex: Pattern
    name: str

    def matches_pattern(self, part_string) -> Match:
        return self.regex.fullmatch(part_string)

    def apply(self, target_match: Match) -> [RollSpec, None]:
        return None
