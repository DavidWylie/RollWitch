from unittest import TestCase
from roll_witch.rolling.output import StandardOutputWriter, TargetedOutputWriter
from roll_witch.rolling.input.spec.operation import RollSpec, OperationSpec
from roll_witch.rolling.roller import RollResult
from roll_witch.rolling.roller import OperationRollResults


class TestStandardOutputWriter(TestCase):
    def test_build_result_string(self):
        writer = StandardOutputWriter()
        spec = OperationSpec()
        roll_spec = RollSpec(dice_sides=10, dice_count=2)
        spec.add_part(roll_spec)
        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(4)
        operation_result = OperationRollResults(spec=spec)
        operation_result.append_roll_result(roll_result)
        result_string = writer.build_result_string(
            roll_result=operation_result, total_string="totalString", user="tester"
        )
        expected_result_string = "tester Roll: totalString Result: 7"
        self.assertEqual(expected_result_string, result_string)


class TestTargetedOutputWriter(TestCase):
    def test_build_result_string_met_target(self):
        writer = TargetedOutputWriter()
        operation_spec = OperationSpec()
        roll_spec = RollSpec(dice_sides=10, dice_count=2, target_number=5)
        operation_spec.add_part(roll_spec)

        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(4)
        roll_result.met_target = True
        operation_result = OperationRollResults(spec=operation_spec)
        operation_result.append_roll_result(roll_result)
        operation_result.met_target = True

        result_string = writer.build_result_string(
            roll_result=operation_result, total_string="totalString", user="tester"
        )
        expected_result_string = "tester Roll: totalString Total: 7 Target: 5 Result: Success"
        self.assertEqual(expected_result_string, result_string)

    def test_build_result_string_missed_target(self):
        writer = TargetedOutputWriter()
        roll_spec = RollSpec(dice_sides=10, dice_count=2, target_number=5)
        operation_spec = OperationSpec()
        operation_spec.add_part(roll_spec)

        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(4)
        roll_result.met_target = False

        operation_result = OperationRollResults(spec=operation_spec)
        operation_result.append_roll_result(roll_result)

        result_string = writer.build_result_string(
            roll_result=operation_result, total_string="totalString", user="tester"
        )
        expected_result_string = "tester Roll: totalString Total: 7 Target: 5 Result: Failed"
        self.assertEqual(expected_result_string, result_string)


class TestBaseOutputWriter(TestCase):
    def test_write_output(self):
        writer = StandardOutputWriter()
        roll_spec = RollSpec(dice_sides=10, dice_count=2)
        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(4)
        op_spec = OperationSpec()
        op_spec.add_part(roll_spec)
        result = OperationRollResults(op_spec)
        result.append_roll_result(roll_result)

        result_string = writer.write_output(result=result, user="tester")
        expected_result_string = "tester Roll: [3, 4] = 7 Result: 7"
        self.assertEqual(expected_result_string, result_string)

    def test_build_total_string(self):
        writer = StandardOutputWriter()
        roll_spec = RollSpec(dice_sides=10, dice_count=2)
        op_spec = OperationSpec()
        op_spec.add_part(roll_spec)
        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(4)
        result = OperationRollResults(op_spec)
        result.append_roll_result(roll_result)
        result_string = writer.build_total_string(result=result)
        expected_result_string = "[3, 4] = 7"
        self.assertEqual(expected_result_string, result_string)

    def test_build_total_string_with_modifier(self):
        writer = StandardOutputWriter()
        roll_spec = RollSpec(dice_sides=10, dice_count=2, modifier=7)
        op_spec = OperationSpec()
        op_spec.add_part(roll_spec)
        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(5)
        roll_result.append_roll(4)
        roll_result.apply_modifier(7)
        result = OperationRollResults(op_spec)
        result.append_roll_result(roll_result)
        result_string = writer.build_total_string(result=result)
        expected_result_string = "[5, 4] = 9 + 7"
        self.assertEqual(expected_result_string, result_string)
