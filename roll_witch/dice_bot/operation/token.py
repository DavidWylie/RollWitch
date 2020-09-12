from roll_witch.dice_bot.output import OperationOutputWriter
from roll_witch.dice_bot.spec import OperationSpec, RollSpec
from roll_witch.dice_bot.result import RollResult, OperationResult
from roll_witch.dice_bot.input import get_token_parser
from roll_witch.dice_bot.roller import StandardRoller, TargetedRoller


class TokenRollOperation:
    def __init__(self, spec: OperationSpec, user: str) -> None:
        super().__init__()
        self.user = user
        self.spec = spec
        self.roller = StandardRoller()
        self.target_roller = TargetedRoller()
        self.output_parser = OperationOutputWriter()

    def execute(self):
        result = OperationResult(self.spec)
        for part in self.spec.parts:
            result.append_roll_result(self.execute_part(part))

        if self.spec.has_target():
            result.met_target = self.target_roller.met_target(self.spec, result.total)

        return self.output_parser.write_output(result, self.user)

    def execute_part(self, roll_spec: RollSpec) -> RollResult:
        try:
            return self.roller.roll(roll_spec)
        except ValueError:
            raise Exception("Your answer is just too big to give you")
        except Exception as e:
            raise Exception(f"{e}")


def get_token_roll_operation(roll_string, user):
    roll_spec = get_token_parser().parse(roll_string)
    if roll_spec.dice_count > 10000:
        raise Exception("How many?  You must be joking.")
    return TokenRollOperation(roll_spec, user)
