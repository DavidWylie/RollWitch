from unittest import TestCase
from unittest.mock import patch
from roll_witch.rolling import command


class TestStandardOperation(TestCase):
    @patch("random.randint")
    def test_simple_dice_roll(self, mock_roll):
        mock_roll.side_effect = [10]
        response = command.regex.execute("d10", "Another TestUser")
        expected_response = "Another TestUser Roll: [10] = 10 Result: 10"
        self.assertEqual(expected_response, response)
