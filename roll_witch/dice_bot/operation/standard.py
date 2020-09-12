from roll_witch.dice_bot.spec import RollSpec
from roll_witch.dice_bot.input import get_regex_parser
from roll_witch.dice_bot.output import TargetedOutputWriter, StandardOutputWriter
from roll_witch.dice_bot.roller import StandardRoller, TargetedRoller


class RollOperation:
    def __init__(self, spec: RollSpec, user: str) -> None:
        super().__init__()
        self.user = user
        self.spec = spec
        if spec.has_target():
            self.roller = TargetedRoller()
            self.output = TargetedOutputWriter()
        else:
            self.roller = StandardRoller()
            self.output = StandardOutputWriter()

    def execute(self):
        try:
            roll_result = self.roller.roll(self.spec)
            output = self.output.write_output(roll_result, self.user)
            if len(output) > 2000:
                raise ValueError()
            return output
        except ValueError:
            raise Exception("Your answer is just too big to give you")
        except Exception as e:
            raise Exception(f"{e}")


def get_roll_operation(roll_string, user):
    roll_spec = get_regex_parser().parse(roll_string)
    if roll_spec.dice_count > 10000:
        raise Exception("How many?  You must be joking.")
    return RollOperation(roll_spec, user)
