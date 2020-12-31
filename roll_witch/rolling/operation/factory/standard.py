from roll_witch.rolling.roller import StandardRoller, TargetedRoller
from ..input import get_regex_parser, get_basic_rpg_parser
from ..operations import standard
from ..output import (
    TargetedOutputWriter,
    StandardOutputWriter,
    BasicOutputWriter,
)
from roll_witch.rolling.protocols import OperationFactory


class StandardOperationFactory(OperationFactory):
    input_parsers = {"regex": get_regex_parser, "basic_rpg": get_basic_rpg_parser}

    def get_roll_operation(self, roll_type, roll_string, user):
        roll_spec = self._get_spec(roll_type, roll_string)
        roller, output = self._get_roller_and_output(roll_type, roll_spec)

        return standard.RollOperation(
            spec=roll_spec, user=user, roller=roller, output=output
        )

    def _get_spec(self, roll_type, roll_string):
        parser = self.input_parsers[roll_type]()
        roll_spec = parser.parse(roll_string)
        if roll_spec.dice_count > 10000:
            raise Exception("How many?  You must be joking.")

        return roll_spec

    def _get_roller_and_output(self, roll_type, roll_spec):
        if roll_type == "basic_rpg":
            roller = TargetedRoller()
            output = BasicOutputWriter()
        elif roll_spec.has_target():
            roller = TargetedRoller()
            output = TargetedOutputWriter()
        else:
            roller = StandardRoller()
            output = StandardOutputWriter()

        return roller, output
