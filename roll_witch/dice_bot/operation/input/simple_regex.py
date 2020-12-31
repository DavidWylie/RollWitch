from roll_witch.dice_bot.operation.input.parser.base import InputParser
from roll_witch.dice_bot.operation.input.parser.regex import RegexInputParser
from roll_witch.dice_bot.operation.input.spec import (
    TargetWithDiceSpec,
    DiceWithModifierSpec,
)

_instance = None


def get_regex_parser() -> InputParser:
    global _instance

    if _instance is None:
        _instance = RegexInputParser()
        _instance.add_spec(TargetWithDiceSpec())
        _instance.add_spec(DiceWithModifierSpec())

    return _instance
