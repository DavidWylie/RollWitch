from .base import BaseOutputWriter
from ..protocols.result import OperationResult


class StandardOutputWriter(BaseOutputWriter):
    def build_result_string(self, roll_result: OperationResult, total_string, user):
        return f"{user} Roll: {total_string} Result: {roll_result.total}"
