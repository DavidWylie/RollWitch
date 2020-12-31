from .parser.base import InputParser
from .parser.regex import RegexInputParser
from .spec import BasicRpgSpec

_instance = None


def get_basic_rpg_parser() -> InputParser:
    global _instance

    if _instance is None:
        _instance = RegexInputParser()
        _instance.add_spec(BasicRpgSpec())

    return _instance
