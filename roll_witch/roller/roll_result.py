from roll_witch.roller import RollSpec


class RollResult():
    def __init__(self, spec:RollSpec) -> None:
        super().__init__()
        self.total = 0
        self.rolls = []
        self.spec = spec

    def append_roll(self, roll):
        self.total += roll
        self.rolls.append(roll)

    def apply_modifier(self, modifier):
        self.total += modifier

    def had_target(self) -> bool:
        return self.spec.has_target()

    def had_modifier(self) -> bool:
        return self.spec.has_modifier()

    def formatted_modifier(self) -> str:
        return f"+{self.spec.dice_modifier}" if self.spec.dice_modifier > 0 else f"{self.spec.dice_modifier}"
