from ..output import OperationOutputWriter
from ..spec import OperationSpec
from roll_witch.rolling.roller import RollSpec, RollResult, StandardRoller, TargetedRoller
from ..result import OperationResult
from roll_witch.rolling.protocols import Operation


class TokenRollOperation(Operation):
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
