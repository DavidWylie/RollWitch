from roll_witch.rolling.input import get_token_parser
from roll_witch.rolling.output import OperationOutputWriter
from roll_witch.rolling.roller import RollResult, RollSpec
from roll_witch.rolling.roller import StandardRoller
from roll_witch.rolling.roller.operation_result import OperationRollResults
from rolling.protocols import Operation
from rolling.protocols.result import OperationResult


class ShadowRunRollResults(OperationRollResults):
    def had_target(self) -> bool:
        return False

    def _apply_roll_to_total(self, result: RollResult):
        for roll in result.rolls:
            if roll >= result.spec.target_number:
                self.total += 1
            self.roll_total += result.roll_total


class ShadowRunOperation(Operation):
    def __init__(self):
        super().__init__()
        self.name = "Shadow Run Roll"
        self.parser = get_token_parser()
        self.roller = StandardRoller()
        self.output_parser = OperationOutputWriter()

    def execute(self, roll_string: str, user: str):
        spec = self.get_spec(roll_string)
        result = ShadowRunRollResults(spec)
        for part in spec.parts:
            part.target_number = spec.target_number
            result.append_roll_result(self.roller.roll(part))

        return result

    def format_output(self, result: OperationResult, user) -> str:
        return self.output_parser.write_output(result, user)

    def get_spec(self, roll_string):
        roll_spec = self.parser.parse(roll_string)
        if not roll_spec.target_number:
            roll_spec.add_part(RollSpec(target_number=5, operation=None))
        return roll_spec
