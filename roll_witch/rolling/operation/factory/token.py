from ..input import get_token_parser
from ..operations.token import TokenRollOperation
from roll_witch.rolling.protocols import OperationFactory


class TokenOperationFactory(OperationFactory):
    def get_roll_operation(self, roll_type, roll_string, user):
        roll_spec = get_token_parser().parse(roll_string)
        if roll_spec.dice_count > 10000:
            raise Exception("How many?  You must be joking.")
        return TokenRollOperation(roll_spec, user)
