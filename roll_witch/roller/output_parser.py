from . import RollResult
from abc import ABC


class BaseOutputWriter(ABC):
    def write_output(self, roll_result: RollResult, user):
        total_string = self.build_total_string(roll_result)
        return self.build_result_string(roll_result, total_string, user)

    def build_total_string(self, roll_result: RollResult):
        modifier_string = roll_result.formatted_modifier() if roll_result.had_modifier() else ''
        return f"{roll_result.rolls} = {roll_result.total} {modifier_string}"

    def build_result_string(self, roll_result: RollResult, total_string, user):
        return "Unsupported"


class StandardOutputWriter(BaseOutputWriter):
    def build_result_string(self, roll_result: RollResult, total_string, user):
        return f"{user} Roll: {total_string} Result: {roll_result.total} "


class TargetedOutputWriter(BaseOutputWriter):
    def build_result_string(self, roll_result: RollResult, total_string, user):
        success_string = 'Success' if roll_result.met_target() else 'Failed'
        return f"{user} Roll: {total_string} = {roll_result.total} Result: {success_string}"
