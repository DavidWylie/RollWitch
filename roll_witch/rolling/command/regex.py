from roll_witch.rolling.input import get_regex_parser
from roll_witch.rolling.output import TargetedOutputWriter, StandardOutputWriter
from roll_witch.rolling.roller import TargetedRoller, StandardRoller
from rolling.protocols import Operation
from rolling.protocols.result import OperationResult
from rolling.roller import OperationRollResults


class RegexOperation(Operation):
    def __init__(self):
        self.name = "Regular Expression Roll"
        self.targeted_roller = TargetedRoller()
        self.standard_roller = StandardRoller()
        self.targeted_output_writer = TargetedOutputWriter()
        self.standard_output_writer = StandardOutputWriter()
        self.parser = get_regex_parser()

    def execute(self, roll_string: str, user: str) -> OperationResult:
        try:
            roll_spec = self.parser.parse(roll_string)
            result = OperationRollResults(roll_spec)
            if roll_spec.has_target():
                result.append_roll_result(self.targeted_roller.roll(roll_spec))
            else:
                result.append_roll_result(self.standard_roller.roll(roll_spec))
            return result
        except Exception as e:
            raise Exception(f"{e}")

    def format_output(self, result: OperationResult, user):
        try:
            if result.had_target():
                return self.targeted_output_writer.write_output(result, user)
            else:
                return self.standard_output_writer.write_output(result, user)
        except ValueError:
            raise Exception("Your answer is just too big to give you")
        except Exception as e:
            raise Exception(f"{e}")
