from roll_witch.rolling.input import get_token_parser
from roll_witch.rolling.output import OperationOutputWriter
from roll_witch.rolling.roller import (
    StandardRoller,
    TargetedRoller,
)
from roll_witch.rolling.roller.operation_result import OperationResult


def execute(roll_string: str, user: str):
    spec = get_spec(roll_string)
    roller = StandardRoller()
    target_roller = TargetedRoller()
    output_parser = OperationOutputWriter()
    result = OperationResult(spec)
    for part in spec.parts:
        result.append_roll_result(roller.roll(part))

    if spec.has_target():
        result.met_target = target_roller.met_target(spec, result.total)

    return output_parser.write_output(result, user)


def get_spec(roll_string):
    parser = get_token_parser()
    roll_spec = parser.parse(roll_string)
    return roll_spec
