from random import randint
from . import RollSpec, RollResult


class StandardRoller():
    def __init__(self, spec: RollSpec) -> None:
        super().__init__()
        self.spec = spec

    def dice_sides(self):
        return self.spec.dice_sides

    def dice_count(self):
        return self.spec.dice_count

    def roll(self) -> RollResult:
        roll_result = RollResult(spec=self.spec)
        self.roll_dice_set(roll_result)
        return roll_result

    def roll_dice_set(self, roll_result):
        for dice in range(0, self.dice_count()):
            roll_result.append_roll(self.roll_dice())
        roll_result.apply_modifier(self.spec.dice_modifier)

    def roll_dice(self):
        roll = randint(0, self.dice_sides())
        return 0 if self._reset_percentiles(roll) else roll

    def _reset_percentiles(self, roll):
        return roll == 100 and self.dice_sides() == 100


class TargetedRoller(StandardRoller):
    def do_roll(self) -> RollResult:
        roll_result = RollResult(spec=self.spec)
        self.roll_dice_set(roll_result)
        roll_result.met_target = self.met_target(roll_result.total)
        return roll_result

    def met_target(self, roll_total):
        if self.spec.target_number >= 0:
            return roll_total > self.spec.target_number
        else:
            return roll_total <= abs(self.spec.target_number)
