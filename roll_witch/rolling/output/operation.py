from roll_witch.rolling.roller import RollResult
from ..protocols.result import OperationResult


class OperationOutputWriter:
    def write_output(self, result: OperationResult, user: str) -> str:
        parts = []
        for index, roll_result in enumerate(result.rolls):
            operator_string = self.get_operator(index, roll_result)
            value_string = self.get_value(roll_result)
            parts.append(f"{operator_string}{value_string}")

        target_string = self.get_target_string(result)
        roll_string = "".join(parts)
        return f"{user} Roll: {roll_string} Result: {result.total}{target_string}"

    def get_target_string(self, result):
        if result.had_target():
            if result.met_target:
                target_string = f" Target: {result.spec.target_number} Success"
            else:
                target_string = f" Target: {result.spec.target_number} Failure"
        else:
            target_string = ""
        return target_string

    def get_value(self, roll_result: RollResult):
        if roll_result.rolls:
            return f"{roll_result.rolls}"
        elif roll_result.roll_spec.has_modifier():
            return roll_result.roll_spec.dice_modifier
        else:
            return ""

    def get_operator(self, index, roll_result):
        if index > 0 and roll_result.operator:
            return f" {roll_result.operator} "
        else:
            return ""
