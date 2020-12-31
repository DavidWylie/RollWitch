from .parser.token import TokenInputParser
from .spec import DiceSpec, ModifierSpec, TargetSpec

_instance = None


def get_token_parser() -> TokenInputParser:
    global _instance

    if _instance is None:
        _instance = TokenInputParser()

        _instance.add_spec(DiceSpec())
        _instance.add_spec(ModifierSpec())
        _instance.add_spec(TargetSpec())

    return _instance
