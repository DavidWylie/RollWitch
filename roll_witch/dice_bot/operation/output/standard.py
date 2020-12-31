from roll_witch.dice_bot.protocols import Result
from .base import BaseOutputWriter


class StandardOutputWriter(BaseOutputWriter):
    def build_result_string(self, roll_result: Result, total_string, user):
        return f"{user} Roll: {total_string} Result: {roll_result.total}"
