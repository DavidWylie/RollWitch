from unittest import TestCase
from unittest.mock import patch

from roll_witch.dice_bot.roller import StandardRoller
from roll_witch.dice_bot import RollSpec, RollResult


class TestStandardRoller(TestCase):
    def test_dice_sides(self):
        spec = RollSpec(dice_count=1, dice_sides=13)
        roller = StandardRoller(spec)
        self.assertEqual(spec.dice_sides, roller.dice_sides())

    def test_dice_count(self):
        spec = RollSpec(dice_count=7, dice_sides=13)
        roller = StandardRoller(spec)
        self.assertEqual(spec.dice_count, roller.dice_count())

    @patch("random.randint")
    def test_roll_dice_set_single_die_no_modifier(self, mock_random):
        spec = RollSpec(dice_count=1, dice_sides=13)
        mock_random.return_value = 3
        roller = StandardRoller(spec)
        result = RollResult(spec=spec)
        roller.roll_dice_set(result)
        self.assertEqual(result.total,3)

    @patch("random.randint")
    def test_roll_dice_set_multiple_die_no_modifier(self, mock_random):
        spec = RollSpec(dice_count=4, dice_sides=13)
        mock_random.side_effect = [1,2,3,5]
        roller = StandardRoller(spec)
        result = RollResult(spec=spec)
        roller.roll_dice_set(result)
        self.assertEqual(result.total, 1+2+3+5)

    @patch("random.randint")
    def test_roll_dice_set_single_die_positive_modifier(self, mock_random):
        spec = RollSpec(dice_count=1, dice_sides=13, modifier=7)
        mock_random.side_effect = [1]

        roller = StandardRoller(spec)
        result = RollResult(spec=spec)

        roller.roll_dice_set(result)
        self.assertEqual(result.total, 1 + 7)

    @patch("random.randint")
    def test_roll_dice_set_multiple_die_positive_modifier(self, mock_random):
        spec = RollSpec(dice_count=3, dice_sides=13, modifier=7)
        mock_random.side_effect = [1,2,3]

        roller = StandardRoller(spec)
        result = RollResult(spec=spec)

        roller.roll_dice_set(result)
        self.assertEqual(result.total, 6 + 7)

    @patch("random.randint")
    def test_roll_dice_set_multiple_die_negative_modifier(self, mock_random):
        spec = RollSpec(dice_count=3, dice_sides=13, modifier=-7)
        mock_random.side_effect = [1, 2, 3]

        roller = StandardRoller(spec)
        result = RollResult(spec=spec)

        roller.roll_dice_set(result)
        self.assertEqual(result.total, 6 - 7)

    @patch("random.randint")
    def test_roll_dice_happy(self, mock_random):
        mock_random.return_value = 3
        spec = RollSpec(dice_count=1, dice_sides=13)
        roller = StandardRoller(spec)
        value = roller.roll_dice()
        self.assertEqual(3, value)

    @patch("random.randint")
    def test_roll_dice_percentile(self, mock_random):
        mock_random.return_value = 100
        spec = RollSpec(dice_count=1, dice_sides=100)
        roller = StandardRoller(spec)
        value = roller.roll_dice()
        self.assertEqual(0, value)

    def test__reset_percentiles_reset(self):
        spec = RollSpec(dice_count=1, dice_sides=100)
        roller = StandardRoller(spec)
        result = roller._reset_percentiles(100)
        self.assertEqual(True, result)

    def test__reset_percentiles_wrong_dice_size(self):
        spec = RollSpec(dice_count=1, dice_sides=200)
        roller = StandardRoller(spec)
        result = roller._reset_percentiles(100)
        self.assertEqual(False, result)

    def test__reset_percentiles_wrong_value(self):
        spec = RollSpec(dice_count=1, dice_sides=200)
        roller = StandardRoller(spec)
        result = roller._reset_percentiles(50)
        self.assertEqual(False, result)