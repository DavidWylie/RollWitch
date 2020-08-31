from unittest import TestCase
from roll_witch.dice_bot import RollResult, RollSpec


class TestRollResult(TestCase):
    def test_append_roll(self):
        roll_result = RollResult(spec=RollSpec(dice_count=1, dice_sides=6))
        self.assertEqual([], roll_result.rolls)
        roll_result.append_roll(1)
        self.assertEqual([1], roll_result.rolls)
        roll_result.append_roll(2)
        self.assertEqual([1, 2], roll_result.rolls)

    def test_apply_modifier(self):
        roll_result = RollResult(spec=RollSpec(dice_count=1, dice_sides=6))
        roll_result.apply_modifier(7)
        self.assertEqual(7, roll_result.total)

    def test_apply_modifier_on_total(self):
        roll_result = RollResult(spec=RollSpec(dice_count=1, dice_sides=6))
        roll_result.total = 10
        roll_result.apply_modifier(7)
        self.assertEqual(17, roll_result.total)

    def test_had_target(self):
        roll_result = RollResult(spec=RollSpec(dice_count=1, dice_sides=6, target_number=10))
        self.assertEqual(True, roll_result.had_target())

    def test_had_no_target(self):
        roll_result = RollResult(spec=RollSpec(dice_count=1, dice_sides=6))
        self.assertEqual(False, roll_result.had_target())

    def test_had_modifier(self):
        roll_result = RollResult(spec=RollSpec(dice_count=1, dice_sides=6, modifier=10))
        self.assertEqual(True, roll_result.had_modifier())

    def test_had_no_modifier(self):
        roll_result = RollResult(spec=RollSpec(dice_count=1, dice_sides=6))
        self.assertEqual(False, roll_result.had_modifier())
