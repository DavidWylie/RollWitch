from roll_witch.rolling.input import get_basic_rpg_parser
from roll_witch.rolling.output import TargetedOutputWriter
from roll_witch.rolling.roller import TargetedRoller
from math import ceil, floor
from roll_witch.rolling.protocols import Result


class BasicOutputWriter(TargetedOutputWriter):
    def build_success_string(self, roll_result: Result):
        target_number = abs(roll_result.spec.target_number)

        if roll_result.total <= ceil(target_number * 0.05):
            return "Critical"

        if roll_result.total <= ceil(target_number * 0.2):
            return "Special"

        if roll_result.total <= ceil(target_number):
            return "Success"

        failure_chance = 100 - target_number
        fumble_roll = 100 - floor(failure_chance * 0.05)

        if roll_result.total >= fumble_roll:
            return "Fumble"

        return "Failed"


def execute(roll_string: str, user: str):
    try:
        spec = get_spec(roll_string)
        roll_result = TargetedRoller().roll(spec)
        output = BasicOutputWriter().write_output(roll_result, user)
        if len(output) > 2000:
            raise ValueError()
        return output
    except ValueError:
        raise Exception("Your answer is just too big to give you")
    except Exception as e:
        raise Exception(f"{e}")


def get_spec(roll_string):
    parser = get_basic_rpg_parser()
    return parser.parse(roll_string)
