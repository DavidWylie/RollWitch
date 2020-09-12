from unittest import TestCase
from hypothesis import given, strategies
from roll_witch.dice_bot.input import TokenInputParser


class TestTokenInputParser(TestCase):
    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
    )
    def test_parse_simple_dice(self, dice_count, dice_sides):
        input_parser = TokenInputParser()
        element = f"{dice_count}d{dice_sides}"
        spec = input_parser.parse(element)
        dice_spec = spec.parts[0]
        self.assertEqual(1, len(spec.parts))
        self.assertEqual(
            dice_count,
            dice_spec.dice_count,
            f"Dice Count in {element} does not match {dice_spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            dice_spec.dice_sides,
            f"Dice Sides in {element} does not match {dice_spec.dice_sides}",
        )

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
        modifier=strategies.integers(min_value=1, max_value=100),
    )
    def test_parse_simple_dice_with_positive_modifier(
        self, dice_count, dice_sides, modifier
    ):
        input_parser = TokenInputParser()
        element = f"{dice_count}d{dice_sides} +{modifier}"
        spec = input_parser.parse(element)
        dice_spec = spec.parts[0]
        modifier_spec = spec.parts[1]
        self.assertEqual(
            dice_count,
            dice_spec.dice_count,
            f"Dice Count in {element} does not match {dice_spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            dice_spec.dice_sides,
            f"Dice Sides in {element} does not match {dice_spec.dice_sides}",
        )
        self.assertEqual(
            modifier,
            modifier_spec.dice_modifier,
            f"Dice Modifier in {element} is invalid",
        )

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
        modifier=strategies.integers(min_value=-100, max_value=-1),
    )
    def test_parse_simple_dice_with_negative_modifier(
        self, dice_count, dice_sides, modifier
    ):
        input_parser = TokenInputParser()
        element = f"{dice_count}d{dice_sides} {modifier}"
        spec = input_parser.parse(element)
        dice_spec = spec.parts[0]
        modifier_spec = spec.parts[1]
        self.assertEqual(
            dice_count,
            dice_spec.dice_count,
            f"Dice Count in {element} does not match {dice_spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            dice_spec.dice_sides,
            f"Dice Sides in {element} does not match {dice_spec.dice_sides}",
        )
        self.assertEqual(
            abs(modifier),
            modifier_spec.dice_modifier,
            f"Dice Modifier in {element} is invalid",
        )
        self.assertEqual(
            "-", modifier_spec.operator, f"Dice Modifier in {element} is invalid"
        )

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
        target=strategies.integers(min_value=-100, max_value=0),
    )
    def test_parse_lower_target_dice(self, dice_count, dice_sides, target):
        input_parser = TokenInputParser()
        element = f"{dice_count}d{dice_sides} t{target}"
        spec = input_parser.parse(element)
        dice_spec = spec.parts[0]
        target_spec = spec.parts[1]
        self.assertEqual(
            dice_count,
            dice_spec.dice_count,
            f"Dice Count in {element} does not match {dice_spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            dice_spec.dice_sides,
            f"Dice Sides in {element} does not match {dice_spec.dice_sides}",
        )
        self.assertEqual(target, target_spec.target_number, "Target Does not match")
        self.assertEqual(target, spec.target_number, "Target Does not match")

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
        target=strategies.integers(min_value=1, max_value=100),
    )
    def test_parse_above_target_dice(self, dice_count, dice_sides, target):
        input_parser = TokenInputParser()
        element = f"{dice_count}d{dice_sides} t{target}"
        spec = input_parser.parse(element)
        dice_spec = spec.parts[0]
        target_spec = spec.parts[1]
        print(element)
        self.assertEqual(
            dice_count,
            dice_spec.dice_count,
            f"Dice Count in {element} does not match {dice_spec.dice_count}",
        )
        self.assertEqual(
            dice_sides,
            dice_spec.dice_sides,
            f"Dice Sides in {element} does not match {dice_spec.dice_sides}",
        )
        self.assertEqual(target, target_spec.target_number, "Target Does not match")

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
    )
    def test_parse_multiple_simple_dice(self, dice_count, dice_sides):
        input_parser = TokenInputParser()
        element = f"{dice_count}d{dice_sides} + {dice_count}d{dice_sides} + {dice_count}d{dice_sides}"
        spec = input_parser.parse(element)
        self.assertEqual(3, len(spec.parts))
        for dice_spec in spec.parts:
            self.assertEqual(
                dice_count,
                dice_spec.dice_count,
                f"Dice Count in {element} does not match {dice_spec.dice_count}",
            )
            self.assertEqual(
                dice_sides,
                dice_spec.dice_sides,
                f"Dice Sides in {element} does not match {dice_spec.dice_sides}",
            )

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
    )
    def test_parse_multiple_simple_dice_leading_space(self, dice_count, dice_sides):
        input_parser = TokenInputParser()
        element = f"{dice_count}d{dice_sides} +{dice_count}d{dice_sides} +{dice_count}d{dice_sides}"
        spec = input_parser.parse(element)
        self.assertEqual(3, len(spec.parts))
        for dice_spec in spec.parts:
            self.assertEqual(
                dice_count,
                dice_spec.dice_count,
                f"Dice Count in {element} does not match {dice_spec.dice_count}",
            )
            self.assertEqual(
                dice_sides,
                dice_spec.dice_sides,
                f"Dice Sides in {element} does not match {dice_spec.dice_sides}",
            )

    @given(
        dice_count=strategies.integers(min_value=1, max_value=100),
        dice_sides=strategies.integers(min_value=1, max_value=100),
    )
    def test_parse_multiple_simple_dice_no_leading_space(self, dice_count, dice_sides):
        input_parser = TokenInputParser()
        element = f"{dice_count}d{dice_sides}+{dice_count}d{dice_sides}+{dice_count}d{dice_sides}"
        spec = input_parser.parse(element)
        self.assertEqual(3, len(spec.parts))
        for dice_spec in spec.parts:
            self.assertEqual(
                dice_count,
                dice_spec.dice_count,
                f"Dice Count in {element} does not match {dice_spec.dice_count}",
            )
            self.assertEqual(
                dice_sides,
                dice_spec.dice_sides,
                f"Dice Sides in {element} does not match {dice_spec.dice_sides}",
            )
