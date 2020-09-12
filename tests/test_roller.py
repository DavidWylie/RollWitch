from unittest import TestCase
from unittest.mock import patch

from roll_witch.dice_bot.roller import StandardRoller
from roll_witch.dice_bot.spec import RollSpec
from roll_witch.dice_bot.result import RollResult


class TestStandardRoller(TestCase):

    @patch("random.randint")
    def test_roll_dice_set_single_die_no_modifier(self, mock_random):
        spec = RollSpec(dice_count=1, dice_sides=13)
        mock_random.return_value = 3
        roller = StandardRoller()
        result = RollResult(spec=spec)
        roller.roll_dice_set(spec, result)
        self.assertEqual(result.total,3)

    @patch("random.randint")
    def test_roll_dice_set_multiple_die_no_modifier(self, mock_random):
        spec = RollSpec(dice_count=4, dice_sides=13)
        mock_random.side_effect = [1,2,3,5]
        roller = StandardRoller()
        result = RollResult(spec=spec)
        roller.roll_dice_set(spec, result)
        self.assertEqual(result.total, 1+2+3+5)

    @patch("random.randint")
    def test_roll_dice_set_single_die_positive_modifier(self, mock_random):
        spec = RollSpec(dice_count=1, dice_sides=13, modifier=7)
        mock_random.side_effect = [1]

        roller = StandardRoller()

        result = roller.roll(spec)
        self.assertEqual( 1 + 7, result.total)

    @patch("random.randint")
    def test_roll_dice_set_multiple_die_positive_modifier(self, mock_random):
        spec = RollSpec(dice_count=3, dice_sides=13, modifier=7)
        mock_random.side_effect = [1,2,3]

        roller = StandardRoller()
        result = roller.roll(spec)
        self.assertEqual(result.total, 6 + 7)

    @patch("random.randint")
    def test_roll_dice_set_multiple_die_negative_modifier(self, mock_random):
        spec = RollSpec(dice_count=3, dice_sides=13, modifier=-7)
        mock_random.side_effect = [1, 2, 3]

        roller = StandardRoller()

        result = roller.roll(spec)
        self.assertEqual(6 - 7, result.total)

    @patch("random.randint")
    def test_roll_dice_happy(self, mock_random):
        mock_random.return_value = 3
        spec = RollSpec(dice_count=1, dice_sides=13)
        roller = StandardRoller()
        value = roller.roll_dice(spec)
        self.assertEqual(3, value)

    def test_roll_dice(self):
        values = []
        for i in range(0, 1000):
            spec = RollSpec(dice_count=1, dice_sides=100)
            roller = StandardRoller()
            value = roller.roll_dice(spec)
            values.append(value)
            self.assertGreater(value, 0)
        print(values)
