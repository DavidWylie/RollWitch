from roll_witch.dice_bot.spec import RollSpec
from roll_witch.dice_bot.input import get_regex_parser, get_basic_rpg_parser
from roll_witch.dice_bot.output import (
    TargetedOutputWriter,
    StandardOutputWriter,
    BasicOutputWriter,
)
from roll_witch.dice_bot.roller import StandardRoller, TargetedRoller


INPUT_PARSERS = {"regex": get_regex_parser, "basic_rpg": get_basic_rpg_parser}


class RollOperation:
    def __init__(self, spec: RollSpec, user: str, roller, output) -> None:
        super().__init__()
        self.user = user
        self.spec = spec
        self.roller = roller
        self.output = output

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


def get_roll_operation(roll_type, roll_string, user):
    roll_spec = _get_spec(roll_type, roll_string)
    roller, output = _get_roller_and_output(roll_type, roll_spec)

    return RollOperation(spec=roll_spec, user=user, roller=roller, output=output)


def _get_spec(roll_type, roll_string):
    parser = INPUT_PARSERS[roll_type]()
    roll_spec = parser.parse(roll_string)
    if roll_spec.dice_count > 10000:
        raise Exception("How many?  You must be joking.")

    return roll_spec


def _get_roller_and_output(roll_type, roll_spec):
    if roll_type == "basic_rpg":
        roller = TargetedRoller()
        output = BasicOutputWriter()
    elif roll_spec.has_target():
        roller = TargetedRoller()
        output = TargetedOutputWriter()
    else:
        roller = StandardRoller()
        output = StandardOutputWriter()

    return roller, output
