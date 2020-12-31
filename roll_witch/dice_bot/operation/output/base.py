from roll_witch.dice_bot.roller import RollResult
from roll_witch.dice_bot.protocols import Result
from abc import ABC, abstractmethod
from typing import Protocol


class OutputParser(Protocol):
    def write_output(self, roll_result: Result, user: str):
        return "Unknown"


class BaseOutputWriter(ABC):
    def write_output(self, roll_result: Result, user):
        total_string = self.build_total_string(roll_result)
        return self.build_result_string(roll_result, total_string, user)

    def build_total_string(self, roll_result: Result):
        if isinstance(roll_result, RollResult):
            modifier_string = roll_result.formatted_modifier()
            return f"{roll_result.rolls} = {roll_result.roll_total}{modifier_string}"
        else:
            raise Exception("Invalid Output parser for given data")

    @abstractmethod
    def build_result_string(self, roll_result: Result, total_string, user):
        return "Unsupported"
