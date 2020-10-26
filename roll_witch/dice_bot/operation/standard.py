from roll_witch.dice_bot.spec import RollSpec
from roll_witch.dice_bot.input import get_regex_parser, get_basic_rpg_parser
from roll_witch.dice_bot.output import TargetedOutputWriter, StandardOutputWriter
from roll_witch.dice_bot.roller import StandardRoller, TargetedRoller


INPUT_PARSERS = {
    'regex': get_regex_parser,
    'basic_rpg': get_basic_rpg_parser
}


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


def get_roll_operation(type, roll_string, user):
    parser = INPUT_PARSERS[type]()
    roll_spec = parser.parse(roll_string)
    if roll_spec.dice_count > 10000:
        raise Exception("How many?  You must be joking.")
    return RollOperation(roll_spec, user)
