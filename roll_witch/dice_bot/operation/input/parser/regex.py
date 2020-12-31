from roll_witch.dice_bot.operation.input.parser.base import InputParser
from roll_witch.dice_bot.operation.input.spec import InputPartSpec


class RegexInputParser(InputParser):
    def __init__(self) -> None:
        super().__init__()
        self.part_specs = {}

    def add_spec(self, spec: InputPartSpec):
        self.part_specs[spec.name] = spec

    def parse(self, roll_string: str):
        for spec_name, spec in self.part_specs.items():
            match = spec.matches_pattern(roll_string)
            if match:
                return spec.apply(match)
        raise Exception(
            f"Roll What?  {roll_string} is not valid Try again  e.g. roll 1d10 +10 or roll 1d6 t6"
        )
