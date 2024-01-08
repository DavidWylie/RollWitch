from roll_witch.rolling.input import get_basic_rpg_parser
from roll_witch.rolling.output import TargetedOutputWriter
from roll_witch.rolling.roller import TargetedRoller
from math import ceil, floor
from rolling.protocols import Operation
from rolling.protocols.result import OperationResult
from rolling.roller import OperationRollResults


class BasicOutputWriter(TargetedOutputWriter):
    def build_success_string(self, roll_result: OperationResult):
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


class BasicOperation(Operation):
    def __init__(self):
        super().__init__()
        self.roller = TargetedRoller()
        self.output_writer = BasicOutputWriter()
        self.parser = get_basic_rpg_parser()

    def execute(self, roll_string: str, user: str) -> OperationResult:
        try:
            spec = self.get_spec(roll_string)
            result = OperationRollResults(spec)
            roll_result = self.roller.roll(spec)
            result.append_roll_result(roll_result)
            return result
        except ValueError:
            raise Exception("Your answer is just too big to give you")
        except Exception as e:
            raise Exception(f"{e}")

    def format_output(self, result: OperationResult, user):
        try:
            output = self.output_writer.write_output(result, user)
            if len(output) > 2000:
                raise ValueError()
            return output
        except ValueError:
            raise Exception("Your answer is just too big to give you")
        except Exception as e:
            raise Exception(f"{e}")

    def get_spec(self, roll_string):
        return self.parser.parse(roll_string)
