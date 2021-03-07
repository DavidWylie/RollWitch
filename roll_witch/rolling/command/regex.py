from roll_witch.rolling.input import get_regex_parser
from roll_witch.rolling.output import TargetedOutputWriter, StandardOutputWriter
from roll_witch.rolling.roller import TargetedRoller, StandardRoller


def execute(roll_string: str, user: str):
    roll_spec = get_spec(roll_string)
    if roll_spec.has_target():
        return do_targeted_roll(roll_spec, user)
    else:
        return do_standard_roll(roll_spec, user)


def get_spec(roll_string):
    parser = get_regex_parser()
    roll_spec = parser.parse(roll_string)
    return roll_spec


def do_targeted_roll(spec, user):
    try:
        roller = TargetedRoller()
        output = TargetedOutputWriter()
        roll_result = roller.roll(spec)
        output = output.write_output(roll_result, user)
        if len(output) > 2000:
            raise ValueError()
        return output
    except ValueError:
        raise Exception("Your answer is just too big to give you")
    except Exception as e:
        raise Exception(f"{e}")


def do_standard_roll(spec, user):
    try:
        roller = StandardRoller()
        output = StandardOutputWriter()
        roll_result = roller.roll(spec)
        output = output.write_output(roll_result, user)
        if len(output) > 2000:
            raise ValueError()
        return output
    except ValueError:
        raise Exception("Your answer is just too big to give you")
    except Exception as e:
        raise Exception(f"{e}")
