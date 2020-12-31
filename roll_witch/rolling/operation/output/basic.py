from math import ceil, floor

from . import TargetedOutputWriter
from roll_witch.rolling.protocols import Result


class BasicOutputWriter(TargetedOutputWriter):
    def build_success_string(self, roll_result: Result):
        target_number = abs(roll_result.spec.target_number)

        if roll_result.total <= ceil(target_number * 0.05):
            return "Critical"

        if roll_result.total <= ceil(target_number * 0.2):
            return "Special"

        if roll_result.total <= ceil(target_number):
            return "Success"

        failure_chance = 100 - target_number
        fumble_roll = 100 - floor(failure_chance * 0.05)

        if roll_result.total >= fumble_roll:
            return "Fumble"

        return "Failed"
