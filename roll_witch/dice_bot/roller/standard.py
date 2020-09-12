import random
from roll_witch.dice_bot.result import RollResult
from roll_witch.dice_bot.spec import RollSpec, DiceSet, DiceModifier
from os import urandom


random.seed(urandom(15))


class StandardRoller:
    def __init__(self) -> None:
        super().__init__()

    def roll(self, spec: RollSpec) -> RollResult:
        roll_result = RollResult(spec=spec)
        self.roll_dice_set(spec, roll_result)
        self.apply_modifier(spec, roll_result)
        return roll_result

    def apply_modifier(self, spec: DiceModifier, roll_result):
        roll_result.apply_modifier(spec.dice_modifier)

    def roll_dice_set(self, spec: DiceSet, roll_result):
        if spec.dice_count > 0:
            for dice in range(0, spec.dice_count):
                roll_result.append_roll(self.roll_dice(spec))

    def roll_dice(self, spec: DiceSet):
        return random.randint(1, spec.dice_sides)
