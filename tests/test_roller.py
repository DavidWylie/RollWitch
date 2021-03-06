from unittest import TestCase
from unittest.mock import patch

from roll_witch.rolling.roller import StandardRoller, RollResult
from roll_witch.rolling.roller.generator import RandomNumberGenerator
from roll_witch.rolling.input.spec.operation import RollSpec


class TestGenerator(RandomNumberGenerator):
    def __init__(self, numbers: list) -> None:
        super().__init__()
        self.numbers = numbers

    def get_int(self, less_than):
        return self.numbers.pop(0)


class TestStandardRoller(TestCase):
    @patch("roll_witch.rolling.roller.generator.get_instance")
    def test_roll_dice_set_single_die_no_modifier(self, mock_generator):
        spec = RollSpec(dice_count=1, dice_sides=13)
        mock_generator.return_value = TestGenerator([3])
        roller = StandardRoller()
        result = RollResult(spec=spec)
        roller.roll_dice_set(spec, result)
        self.assertEqual(result.total, 3)

    @patch("roll_witch.rolling.roller.generator.get_instance")
    def test_roll_dice_set_multiple_die_no_modifier(self, mock_generator):
        spec = RollSpec(dice_count=4, dice_sides=13)
        mock_generator.return_value = TestGenerator([1, 2, 3, 5])
        roller = StandardRoller()
        result = RollResult(spec=spec)
        roller.roll_dice_set(spec, result)
        self.assertEqual(result.total, 1 + 2 + 3 + 5)

    @patch("roll_witch.rolling.roller.generator.get_instance")
    def test_roll_dice_set_single_die_positive_modifier(self, mock_generator):
        spec = RollSpec(dice_count=1, dice_sides=13, modifier=7)
        mock_generator.return_value = TestGenerator([1])

        roller = StandardRoller()

        result = roller.roll(spec)
        self.assertEqual(1 + 7, result.total)

    @patch("roll_witch.rolling.roller.generator.get_instance")
    def test_roll_dice_set_multiple_die_positive_modifier(self, mock_generator):
        spec = RollSpec(dice_count=3, dice_sides=13, modifier=7)
        mock_generator.return_value = TestGenerator([1, 2, 3])

        roller = StandardRoller()
        result = roller.roll(spec)
        self.assertEqual(result.total, 6 + 7)

    @patch("roll_witch.rolling.roller.generator.get_instance")
    def test_roll_dice_set_multiple_die_negative_modifier(self, mock_generator):
        spec = RollSpec(dice_count=3, dice_sides=13, modifier=-7)
        mock_generator.return_value = TestGenerator([1, 2, 3])

        roller = StandardRoller()

        result = roller.roll(spec)
        self.assertEqual(6 - 7, result.total)

    @patch("roll_witch.rolling.roller.generator.get_instance")
    def test_roll_dice_happy(self, mock_generator):
        mock_generator.return_value = TestGenerator([3])
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
