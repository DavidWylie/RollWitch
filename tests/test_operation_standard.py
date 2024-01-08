from unittest import TestCase
from unittest.mock import patch
from roll_witch.rolling.command.regex import RegexOperation


class TestStandardOperation(TestCase):
    @patch("random.randint")
    def test_simple_dice_roll(self, mock_roll):
        mock_roll.side_effect = [10]
        operation = RegexOperation()
        response = operation.execute("d10", "Another TestUser")
        actual_response = operation.format_output(response, "Another TestUser")
        expected_response = "Another TestUser Roll: [10] = 10 Result: 10"
        self.assertEqual(expected_response, actual_response)
