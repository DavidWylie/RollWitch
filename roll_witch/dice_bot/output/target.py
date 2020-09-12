from roll_witch.dice_bot.result import Result
from .base import BaseOutputWriter


class TargetedOutputWriter(BaseOutputWriter):
    def build_result_string(self, roll_result: Result, total_string, user):
        success_string = "Success" if roll_result.met_target else "Failed"
        return f"{user} Roll: {total_string} = {roll_result.total} Result: {success_string}"
