from unittest import TestCase
from roll_witch.rolling.output import OperationOutputWriter
from roll_witch.rolling.input.spec.operation import OperationSpec, RollSpec
from roll_witch.rolling.roller import RollResult, OperationResult


class TestTokenOutputWriter(TestCase):
    def test_single_operation(self):
        user = "Test"
        spec = OperationSpec()
        roll_spec = RollSpec(dice_count=3, dice_sides=6, operation="+")
        spec.add_part(roll_spec)
        operation_result = OperationResult(spec)
        roll_result = RollResult(roll_spec)
        roll_result.append_roll(1)
        roll_result.append_roll(2)
        roll_result.append_roll(3)
        operation_result.append_roll_result(roll_result)
        writer = OperationOutputWriter()

        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: [1, 2, 3] Result: 6"
        self.assertEqual(expected_result, result)

    def test_multiple_dice_operations(self):
        user = "Test"
        spec = OperationSpec()
        roll_spec = RollSpec(dice_count=3, dice_sides=6, operation="+")
        spec.add_part(roll_spec)
        operation_result = OperationResult(spec)
        roll_result = RollResult(roll_spec)
        roll_result.append_roll(1)
        roll_result.append_roll(2)
        roll_result.append_roll(3)
        operation_result.append_roll_result(roll_result)

        roll_spec_2 = RollSpec(dice_count=3, dice_sides=20, operation="+")
        spec.add_part(roll_spec_2)
        roll_result_2 = RollResult(roll_spec_2)
        roll_result_2.append_roll(5)
        roll_result_2.append_roll(10)
        roll_result_2.append_roll(15)
        operation_result.append_roll_result(roll_result_2)
        writer = OperationOutputWriter()

        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: [1, 2, 3] + [5, 10, 15] Result: 36"
        self.assertEqual(expected_result, result)

    def test_single_modifier_operations(self):
        user = "Test"
        spec = OperationSpec()
        roll_spec = RollSpec(modifier=5, operation="+")
        spec.add_part(roll_spec)
        operation_result = OperationResult(spec)
        roll_result = RollResult(roll_spec)
        roll_result.apply_modifier(5)

        operation_result.append_roll_result(roll_result)
        writer = OperationOutputWriter()

        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: 5 Result: 5"
        self.assertEqual(expected_result, result)

    def test_multiple_modifier_operations(self):
        user = "Test"
        spec = OperationSpec()
        operation_result = OperationResult(spec)

        roll_spec = RollSpec(modifier=5, operation="+")
        spec.add_part(roll_spec)
        roll_result = RollResult(roll_spec)
        roll_result.apply_modifier(5)
        operation_result.append_roll_result(roll_result)

        roll_spec_2 = RollSpec(modifier=3, operation="-")
        spec.add_part(roll_spec_2)
        roll_result_2 = RollResult(roll_spec_2)
        roll_result_2.apply_modifier(3)
        operation_result.append_roll_result(roll_result_2)

        roll_spec_3 = RollSpec(modifier=2, operation="+")
        spec.add_part(roll_spec_3)
        roll_result_3 = RollResult(roll_spec_3)
        roll_result_3.apply_modifier(2)
        operation_result.append_roll_result(roll_result_3)

        writer = OperationOutputWriter()
        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: 5 - 3 + 2 Result: 4"
        self.assertEqual(expected_result, result)

    def test_mixed_operation(self):
        user = "Test"
        spec = OperationSpec()
        operation_result = OperationResult(spec)

        roll_spec = RollSpec(modifier=5, operation="+")
        spec.add_part(roll_spec)
        roll_result = RollResult(roll_spec)
        roll_result.apply_modifier(5)
        operation_result.append_roll_result(roll_result)

        roll_spec_2 = RollSpec(dice_count=3, dice_sides=20, operation="-")
        spec.add_part(roll_spec_2)
        roll_result_2 = RollResult(roll_spec_2)
        roll_result_2.append_roll(1)
        roll_result_2.append_roll(2)
        roll_result_2.append_roll(3)
        operation_result.append_roll_result(roll_result_2)

        roll_spec_3 = RollSpec(modifier=2, operation="-")
        spec.add_part(roll_spec_3)
        roll_result_3 = RollResult(roll_spec_3)
        roll_result_3.apply_modifier(2)
        operation_result.append_roll_result(roll_result_3)

        writer = OperationOutputWriter()
        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: 5 - [1, 2, 3] - 2 Result: -3"
        self.assertEqual(expected_result, result)

    def test_targeted_multiple_operation(self):
        user = "Test"
        spec = OperationSpec()
        roll_spec = RollSpec(dice_count=3, dice_sides=6, operation="+")
        spec.add_part(roll_spec)
        spec.target_number = 5
        operation_result = OperationResult(spec)
        roll_result = RollResult(roll_spec)
        roll_result.append_roll(1)
        roll_result.append_roll(2)
        roll_result.append_roll(3)
        operation_result.append_roll_result(roll_result)

        roll_spec_3 = RollSpec(modifier=2, operation="-")
        spec.add_part(roll_spec_3)
        roll_result_3 = RollResult(roll_spec_3)
        roll_result_3.apply_modifier(2)
        operation_result.append_roll_result(roll_result_3)

        operation_result.met_target = False
        writer = OperationOutputWriter()

        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: [1, 2, 3] - 2 Result: 4 Target: 5 Failure"
        self.assertEqual(expected_result, result)

    def test_targetted_single_operation(self):
        user = "Test"
        spec = OperationSpec()
        roll_spec = RollSpec(dice_count=3, dice_sides=6, operation="+")
        spec.add_part(roll_spec)
        spec.target_number = 5
        operation_result = OperationResult(spec)
        roll_result = RollResult(roll_spec)
        roll_result.append_roll(1)
        roll_result.append_roll(2)
        roll_result.append_roll(3)
        operation_result.append_roll_result(roll_result)
        operation_result.met_target = True
        writer = OperationOutputWriter()

        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: [1, 2, 3] Result: 6 Target: 5 Success"
        self.assertEqual(expected_result, result)

    def test_multiply_dice_operations(self):
        user = "Test"
        spec = OperationSpec()
        roll_spec = RollSpec(dice_count=3, dice_sides=6, operation="+")
        spec.add_part(roll_spec)
        operation_result = OperationResult(spec)
        roll_result = RollResult(roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(2)
        roll_result.append_roll(5)
        operation_result.append_roll_result(roll_result)

        roll_spec_2 = RollSpec(dice_count=3, dice_sides=20, operation="*")
        spec.add_part(roll_spec_2)
        roll_result_2 = RollResult(roll_spec_2)
        roll_result_2.append_roll(2)
        roll_result_2.append_roll(2)
        roll_result_2.append_roll(1)
        operation_result.append_roll_result(roll_result_2)
        writer = OperationOutputWriter()

        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: [3, 2, 5] * [2, 2, 1] Result: 50"
        self.assertEqual(expected_result, result)

    def test_multiply_with_addition_dice_operations(self):
        user = "Test"
        spec = OperationSpec()
        roll_spec = RollSpec(dice_count=3, dice_sides=6, operation="+")
        spec.add_part(roll_spec)
        operation_result = OperationResult(spec)
        roll_result = RollResult(roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(2)
        roll_result.append_roll(5)
        operation_result.append_roll_result(roll_result)

        roll_spec_2 = RollSpec(dice_count=3, dice_sides=20, operation="*")
        spec.add_part(roll_spec_2)
        roll_result_2 = RollResult(roll_spec_2)
        roll_result_2.append_roll(2)
        roll_result_2.append_roll(2)
        roll_result_2.append_roll(1)
        operation_result.append_roll_result(roll_result_2)

        roll_spec_3 = RollSpec(dice_count=0, dice_sides=0, modifier=3, operation="+")
        spec.add_part(roll_spec_3)
        roll_result_3 = RollResult(roll_spec_3)
        roll_result_3.apply_modifier(roll_spec_3.dice_modifier)
        operation_result.append_roll_result(roll_result_3)

        writer = OperationOutputWriter()

        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: [3, 2, 5] * [2, 2, 1] + 3 Result: 53"
        self.assertEqual(expected_result, result)

    def test_multiply_operator_operations(self):
        user = "Test"
        spec = OperationSpec()
        roll_spec = RollSpec(dice_count=3, dice_sides=6, operation="+")
        spec.add_part(roll_spec)
        operation_result = OperationResult(spec)
        roll_result = RollResult(roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(2)
        roll_result.append_roll(5)
        operation_result.append_roll_result(roll_result)

        roll_spec_3 = RollSpec(dice_count=0, dice_sides=0, modifier=3, operation="*")
        spec.add_part(roll_spec_3)
        roll_result_3 = RollResult(roll_spec_3)
        roll_result_3.apply_modifier(roll_spec_3.dice_modifier)
        operation_result.append_roll_result(roll_result_3)

        writer = OperationOutputWriter()

        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: [3, 2, 5] * 3 Result: 30"
        self.assertEqual(expected_result, result)

    def test_divide_operator_operations(self):
        user = "Test"
        spec = OperationSpec()
        roll_spec = RollSpec(dice_count=3, dice_sides=6, operation="+")
        spec.add_part(roll_spec)
        operation_result = OperationResult(spec)
        roll_result = RollResult(roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(2)
        roll_result.append_roll(5)
        operation_result.append_roll_result(roll_result)

        roll_spec_3 = RollSpec(dice_count=0, dice_sides=0, modifier=2, operation="/")
        spec.add_part(roll_spec_3)
        roll_result_3 = RollResult(roll_spec_3)
        roll_result_3.apply_modifier(roll_spec_3.dice_modifier)
        operation_result.append_roll_result(roll_result_3)

        writer = OperationOutputWriter()

        result = writer.write_output(operation_result, user)
        expected_result = "Test Roll: [3, 2, 5] / 2 Result: 5"
        self.assertEqual(expected_result, result)
