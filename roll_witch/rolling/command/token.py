from roll_witch.rolling.input import get_token_parser
from roll_witch.rolling.output import OperationOutputWriter
from roll_witch.rolling.roller import (
    StandardRoller,
    TargetedRoller,
)
from roll_witch.rolling.roller.operation_result import OperationRollResults
from roll_witch.rolling.protocols import Operation


class TokenOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "Standard Dice Roll"
        self.parser = get_token_parser()
        self.roller = StandardRoller()
        self.target_roller = TargetedRoller()
        self.output_parser = OperationOutputWriter()

    def execute(self, roll_string: str, user: str):
        spec = self.parser.parse(roll_string)
        result = OperationRollResults(spec)
        for part in spec.parts:
            result.append_roll_result(self.roller.roll(part))

        if spec.has_target():
            result.met_target = self.target_roller.met_target(spec, result.total)

        return result

    def format_output(self, result, user) -> str:
        return self.output_parser.write_output(result, user)
