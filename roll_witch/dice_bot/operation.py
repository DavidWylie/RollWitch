from . import RollSpec
from .input_parser import RegexInputParser
from .output_parser import TargetedOutputWriter, StandardOutputWriter
from .roller import StandardRoller, TargetedRoller

regex_input_parser = RegexInputParser()


class RollOperation():
    def __init__(self, spec: RollSpec, user: str) -> None:
        super().__init__()
        self.user = user
        if spec.has_target():
            self.roller = TargetedRoller(spec)
            self.output = TargetedOutputWriter()
        else:
            self.roller = StandardRoller(spec)
            self.output = StandardOutputWriter()

    def execute(self):
        try:
            roll_result = self.roller.roll()
            output = self.output.write_output(roll_result, self.user)
            if len(output) > 2000:
                raise ValueError()
            return output
        except ValueError as e:
            raise Exception(f"Your answer is just too big to give you")
        except Exception as e:
            raise Exception(f"{e}")


def get_roll_operation(roll_string, user):
    global regex_input_parser
    roll_spec = regex_input_parser.parse(roll_string)
    if roll_spec.dice_count > 10000:
        raise Exception("How many?  You must be joking.")
    return RollOperation(roll_spec, user)
