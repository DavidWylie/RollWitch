from roll_witch.dice_bot.spec import Targetable, RollSpec
from typing import Protocol, Type


class Result(Protocol):
    total: int
    roll_total: int
    spec: Targetable
    met_target: bool


class RollResult(Result):
    roll_spec: RollSpec

    def __init__(self, spec: Targetable) -> None:
        super().__init__()
        self.total = 0
        self.roll_total = 0
        self.rolls = []
        self.spec = spec

        if isinstance(spec, RollSpec):
            self.roll_spec = spec
        else:
            raise Exception("Invalid Spec")

        self.met_target = False

    def append_roll(self, roll):
        self.total += roll
        self.roll_total += roll
        self.rolls.append(roll)

    def apply_modifier(self, modifier):
        self.total += modifier

    def formatted_modifier(self) -> str:
        if self.roll_spec.has_modifier():
            if self.roll_spec.dice_modifier >= 0:
                return f" + {self.roll_spec.dice_modifier}"
            else:
                return f" - {abs(self.roll_spec.dice_modifier)}"
        else:
            return ""

    @property
    def operator(self):
        return self.roll_spec.operation
