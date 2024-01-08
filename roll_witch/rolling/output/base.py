from roll_witch.rolling.roller import RollResult
from abc import ABC, abstractmethod

from rolling.protocols.result import OperationResult


class BaseOutputWriter(ABC):
    def write_output(self, result: OperationResult, user):
        total_string = self.build_total_string(result)
        return self.build_result_string(result, total_string, user)

    def build_total_string(self, result: OperationResult):
        roll_result = result.rolls[0]
        modifier_string = roll_result.formatted_modifier()
        return f"{roll_result.rolls} = {roll_result.roll_total}{modifier_string}"

    @abstractmethod
    def build_result_string(self, roll_result: OperationResult, total_string, user):
        return "Unsupported"
