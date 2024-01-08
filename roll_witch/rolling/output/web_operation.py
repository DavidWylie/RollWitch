from dataclasses import dataclass
from roll_witch.rolling.roller import RollResult
from ..protocols.result import OperationResult
from ..roller import RollSpec


@dataclass
class WebRollResult:
    result: str
    rolled: str
    met_target: str
    target: str
    total: str


@dataclass
class WebResult:
    request: str
    roller: str
    rolls: [WebRollResult]
    target: str
    met_target: str
    total: str


class WebOperationOutputWriter:
    def write_output(self,operation_request: str, result: OperationResult, roller: str) -> WebResult:
        roll_results = []
        for index, roll_result in enumerate(result.rolls):
            operator_string = self.get_operator(index, roll_result)
            value_string = self.get_value(roll_result)
            if value_string:
                roll_results.append(WebRollResult(
                    rolled=self.get_roll_string(roll_result.roll_spec),
                    result=f"{operator_string}{value_string}",
                    met_target=self.get_met_target_string(roll_result),
                    target=self.get_target_string(roll_result),
                    total=f"{roll_result.total}",
                ))

        return WebResult(
            request=operation_request,
            roller=roller,
            rolls=roll_results,
            total=f"{result.total}",
            target=self.get_target_string(result),
            met_target=self.get_met_target_string(result)
        )

    def get_roll_string(self, roll_spec: RollSpec):
        dice_count = roll_spec.dice_count if roll_spec.dice_count else ''
        dice_sides = f"d{roll_spec.dice_sides}" if roll_spec.dice_sides else ''
        modifier = f"{roll_spec.operator}{roll_spec.dice_modifier}" if roll_spec.dice_modifier > 0 else ''
        return f"{dice_count}{dice_sides} {modifier}"

    def get_met_target_string(self, result):
        if result.had_target():
            if result.met_target:
                met_target_string = "Success"
            else:
                met_target_string = "Failure"
        else:
            met_target_string = ""
        return met_target_string

    def get_target_string(self, result):
        if result.had_target():
            target_string = f" (Target: {result.spec.target_number}) "
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
