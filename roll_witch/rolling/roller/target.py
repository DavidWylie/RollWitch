from .standard import StandardRoller
from .result import RollResult
from .spec import RollSpec
from roll_witch.rolling.protocols import Targetable


class TargetedRoller(StandardRoller):
    def roll(self, spec: RollSpec) -> RollResult:
        roll_result = RollResult(spec=spec)
        self.roll_dice_set(spec, roll_result)
        self.apply_modifier(spec, roll_result)
        roll_result.met_target = self.met_target(spec, roll_result.total)
        return roll_result

    def met_target(self, spec: Targetable, roll_total):
        if spec.target_number >= 0:
            return roll_total > spec.target_number
        else:
            return roll_total <= abs(spec.target_number)
