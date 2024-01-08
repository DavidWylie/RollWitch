from .base import BaseOutputWriter
from ..protocols.result import OperationResult


class TargetedOutputWriter(BaseOutputWriter):
    def build_success_string(self, roll_result: OperationResult):
        return "Success" if roll_result.met_target else "Failed"

    def build_result_string(self, roll_result: OperationResult, total_string, user):
        success_string = self.build_success_string(roll_result)
        return (
            f"{user} "
            f"Roll: {total_string} "
            f"Total: {roll_result.total} "
            f"Target: {abs(roll_result.spec.target_number)} "
            f"Result: {success_string}"
        )
