from roll_witch.dice_bot.spec import OperationSpec
from roll_witch.dice_bot.result import RollResult


class OperationResult:
    rolls: [RollResult]

    def __init__(self, spec: OperationSpec) -> None:
        super().__init__()
        self.total = 0
        self.roll_total = 0
        self.rolls = []
        self.spec = spec
        self.met_target = False

    def append_roll_result(self, result: RollResult):
        if result.roll_spec.operation == '+':
            self.total += result.total
            self.roll_total += result.roll_total
        elif result.roll_spec.operation == '-':
            self.total -= result.total
            self.roll_total -= result.roll_total
        self.rolls.append(result)

    def had_target(self) -> bool:
        return self.spec.has_target()