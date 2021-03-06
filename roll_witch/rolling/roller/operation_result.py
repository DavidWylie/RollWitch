from roll_witch.rolling.input.spec.operation import OperationSpec
from roll_witch.rolling.roller import RollResult


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
        self._apply_roll_to_total(result)
        self.rolls.append(result)

    def _apply_roll_to_total(self, result: RollResult):
        if result.roll_spec.operator == "+":
            self.total += result.total
            self.roll_total += result.roll_total
        elif result.roll_spec.operator == "-":
            self.total -= result.total
            self.roll_total -= result.roll_total
        elif result.roll_spec.operator == "*":
            self.total *= result.total
            self.roll_total *= result.roll_total
        elif result.roll_spec.operator == "/":
            if result.total:
                self.total = round(self.total / result.total)
            if result.roll_total:
                self.roll_total = round(self.roll_total / result.roll_total)

    def had_target(self) -> bool:
        return self.spec.has_target()
