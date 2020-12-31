from unittest import TestCase
from hypothesis import given, strategies
from roll_witch.dice_bot.operation.input import get_regex_parser


class TestRegexInputParser(TestCase):
    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
    )
    def test_parse_simple_dice(self, dice_count, dice_sides):
        input_parser = get_regex_parser()
        element = f"{dice_count}d{dice_sides}"
        spec = input_parser.parse(element)
        self.assertEqual(
            dice_count,
            spec.dice_count,
            f"Dice Count in {element} does not match {spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            spec.dice_sides,
            f"Dice Sides in {element} does not match {spec.dice_sides}",
        )
        self.assertEqual(
            0, spec.dice_modifier, f"Dice Modifier in {element} is invalid"
        )
        self.assertIsNone(spec.target_number, f"Target Number in {element} is invalid")

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
        modifier=strategies.integers(min_value=1, max_value=100),
    )
    def test_parse_simple_dice_with_positive_modifier(
        self, dice_count, dice_sides, modifier
    ):
        input_parser = get_regex_parser()
        element = f"{dice_count}d{dice_sides} +{modifier}"
        spec = input_parser.parse(element)
        self.assertEqual(
            dice_count,
            spec.dice_count,
            f"Dice Count in {element} does not match {spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            spec.dice_sides,
            f"Dice Sides in {element} does not match {spec.dice_sides}",
        )
        self.assertGreater(
            spec.dice_modifier, 0, f"Dice Modifier in {element} is invalid"
        )
        self.assertIsNone(spec.target_number, f"Target Number in {element} is invalid")

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
        modifier=strategies.integers(min_value=-100, max_value=0),
    )
    def test_parse_simple_dice_with_negative_modifier(
        self, dice_count, dice_sides, modifier
    ):
        input_parser = get_regex_parser()
        element = f"{dice_count}d{dice_sides} {modifier}"
        spec = input_parser.parse(element)
        self.assertEqual(
            dice_count,
            spec.dice_count,
            f"Dice Count in {element} does not match {spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            spec.dice_sides,
            f"Dice Sides in {element} does not match {spec.dice_sides}",
        )
        self.assertEqual(
            modifier, spec.dice_modifier, f"Dice Modifier in {element} is invalid"
        )
        self.assertIsNone(spec.target_number, f"Target Number in {element} is invalid")

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
        target=strategies.integers(min_value=1, max_value=100),
    )
    def test_parse_lower_target_dice(self, dice_count, dice_sides, target):
        input_parser = get_regex_parser()
        element = f"{dice_count}d{dice_sides} t-{target}"
        spec = input_parser.parse(element)
        print(element)
        self.assertEqual(
            dice_count,
            spec.dice_count,
            f"Dice Count in {element} does not match {spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            spec.dice_sides,
            f"Dice Sides in {element} does not match {spec.dice_sides}",
        )
        self.assertEqual(
            0, spec.dice_modifier, f"Dice Modifier in {element} is invalid"
        )
        self.assertEqual(-target, spec.target_number, "Target Does not match")

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
        target=strategies.integers(min_value=-100, max_value=0),
    )
    def test_parse_lower_target_dice_negative_value(
        self, dice_count, dice_sides, target
    ):
        input_parser = get_regex_parser()
        element = f"{dice_count}d{dice_sides} t{target}"
        spec = input_parser.parse(element)
        print(element)
        self.assertEqual(
            dice_count,
            spec.dice_count,
            f"Dice Count in {element} does not match {spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            spec.dice_sides,
            f"Dice Sides in {element} does not match {spec.dice_sides}",
        )
        self.assertEqual(
            0, spec.dice_modifier, f"Dice Modifier in {element} is invalid"
        )
        self.assertEqual(target, spec.target_number, "Target Does not match")

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
        target=strategies.integers(min_value=1, max_value=100),
    )
    def test_parse_above_target_dice(self, dice_count, dice_sides, target):
        input_parser = get_regex_parser()
        element = f"{dice_count}d{dice_sides} t{target}"
        spec = input_parser.parse(element)
        print(element)
        self.assertEqual(
            dice_count,
            spec.dice_count,
            f"Dice Count in {element} does not match {spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            spec.dice_sides,
            f"Dice Sides in {element} does not match {spec.dice_sides}",
        )
        self.assertEqual(
            0, spec.dice_modifier, f"Dice Modifier in {element} is invalid"
        )
        self.assertEqual(target, spec.target_number, "Target Does not match")
