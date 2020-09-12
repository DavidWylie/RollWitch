from unittest import TestCase
from roll_witch.dice_bot.output import StandardOutputWriter, TargetedOutputWriter
from roll_witch.dice_bot.spec import RollSpec
from roll_witch.dice_bot.result import RollResult


class TestStandardOutputWriter(TestCase):
    def test_build_result_string(self):
        writer = StandardOutputWriter()
        roll_spec = RollSpec(dice_sides=10, dice_count=2)
        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(4)

        result_string = writer.build_result_string(
            roll_result=roll_result,
            total_string="totalString",
            user="tester"
        )
        expected_result_string = "tester Roll: totalString Result: 7"
        self.assertEqual(expected_result_string, result_string)


class TestTargetedOutputWriter(TestCase):
    def test_build_result_string_met_target(self):
        writer = TargetedOutputWriter()
        roll_spec = RollSpec(dice_sides=10, dice_count=2, target_number=5)
        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(4)
        roll_result.met_target = True

        result_string = writer.build_result_string(
            roll_result=roll_result,
            total_string="totalString",
            user="tester"
        )
        expected_result_string = "tester Roll: totalString = 7 Result: Success"
        self.assertEqual(expected_result_string, result_string)

    def test_build_result_string_missed_target(self):
        writer = TargetedOutputWriter()
        roll_spec = RollSpec(dice_sides=10, dice_count=2, target_number=5)
        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(4)
        roll_result.met_target = False

        result_string = writer.build_result_string(
            roll_result=roll_result,
            total_string="totalString",
            user="tester"
        )
        expected_result_string = "tester Roll: totalString = 7 Result: Failed"
        self.assertEqual(expected_result_string, result_string)


class TestBaseOutputWriter(TestCase):
    def test_write_output(self):
        writer = StandardOutputWriter()
        roll_spec = RollSpec(dice_sides=10, dice_count=2)
        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(4)

        result_string = writer.write_output(
            roll_result=roll_result,
            user="tester"
        )
        expected_result_string = "tester Roll: [3, 4] = 7 Result: 7"
        self.assertEqual(expected_result_string, result_string)

    def test_build_total_string(self):
        writer = StandardOutputWriter()
        roll_spec = RollSpec(dice_sides=10, dice_count=2)
        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(3)
        roll_result.append_roll(4)

        result_string = writer.build_total_string(
            roll_result=roll_result
        )
        expected_result_string = "[3, 4] = 7"
        self.assertEqual(expected_result_string, result_string)

    def test_build_total_string_with_modifier(self):
        writer = StandardOutputWriter()
        roll_spec = RollSpec(dice_sides=10, dice_count=2, modifier=7)
        roll_result = RollResult(spec=roll_spec)
        roll_result.append_roll(5)
        roll_result.append_roll(4)
        roll_result.apply_modifier(7)

        result_string = writer.build_total_string(
            roll_result=roll_result
        )
        expected_result_string = "[5, 4] = 9 + 7"
        self.assertEqual(expected_result_string, result_string)
