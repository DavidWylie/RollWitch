from unittest import TestCase
from roll_witch.dice_bot import RollSpec


class TestRollSpec(TestCase):
    def test_has_target(self):
        spec = RollSpec(target_number=7, dice_sides=1, dice_count=1)
        self.assertEqual(True, spec.has_target())

    def test_has_target_no_target(self):
        spec = RollSpec( dice_sides=1, dice_count=1)
        self.assertEqual(False, spec.has_target())

    def test_has_modifier(self):
        spec = RollSpec(modifier=10, dice_sides=1, dice_count=1)
        self.assertEqual(True, spec.has_modifier())

    def test_has_no_modifier(self):
        spec = RollSpec(dice_sides=1, dice_count=1)
        self.assertEqual(False, spec.has_modifier())
