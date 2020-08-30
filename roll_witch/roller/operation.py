from . import RollSpec, input_parser
from .output_parser import TargetedOutputWriter, StandardOutputWriter
from .roller import StandardRoller, TargetedRoller


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
            roll_result = self.roller.do_roll()
            return self.output.write_output(roll_result, self.user)
        except Exception as e:
            return f"Error rolling dice \n {e}"


def get_roll_operation(roll_string, user):
    roll_spec = input_parser.parse(roll_string)
    return RollOperation(roll_spec, user)
