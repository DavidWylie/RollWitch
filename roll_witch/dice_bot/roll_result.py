from roll_witch.dice_bot import RollSpec


class RollResult():
    def __init__(self, spec:RollSpec) -> None:
        super().__init__()
        self.total = 0
        self.roll_total = 0
        self.rolls = []
        self.spec = spec
        self.met_target = False

    def append_roll(self, roll):
        self.total += roll
        self.roll_total += roll
        self.rolls.append(roll)

    def apply_modifier(self, modifier):
        self.total += modifier

    def had_target(self) -> bool:
        return self.spec.has_target()

    def had_modifier(self) -> bool:
        return self.spec.has_modifier()

    def formatted_modifier(self) -> str:
        return f" + {self.spec.dice_modifier}" if self.spec.dice_modifier >= 0 else f" - {abs(self.spec.dice_modifier)}"
