from roll_witch.rolling.input import get_token_parser
from roll_witch.rolling.output import OperationOutputWriter
from roll_witch.rolling.roller import RollResult, RollSpec
from roll_witch.rolling.roller import StandardRoller
from roll_witch.rolling.roller.operation_result import OperationResult


class ShadowRunResult(OperationResult):
    def had_target(self) -> bool:
        return False

    def _apply_roll_to_total(self, result: RollResult):
        for roll in result.rolls:
            if roll >= result.spec.target_number:
                self.total += 1
            self.roll_total += result.roll_total


def execute(roll_string: str, user: str):
    spec = get_spec(roll_string)
    roller = StandardRoller()
    output_parser = OperationOutputWriter()
    result = ShadowRunResult(spec)
    for part in spec.parts:
        part.target_number = spec.target_number
        result.append_roll_result(roller.roll(part))

    return output_parser.write_output(result, user)


def get_spec(roll_string):
    parser = get_token_parser()
    roll_spec = parser.parse(roll_string)
    if not roll_spec.target_number:
        roll_spec.add_part(RollSpec(target_number=5, operation=None))
    return roll_spec
