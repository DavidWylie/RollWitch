from roll_witch.dice_bot.operation import get_roll_operation
from unittest import TestCase
from unittest.mock import patch


class TestStandardOperation(TestCase):
    @patch("random.randint")
    def test_simple_dice_roll(self, mock_roll):
        mock_roll.side_effect = [10]
        operation = get_roll_operation('roll', "d10", "Another TestUser")
        response = operation.execute()
        expected_response = "Another TestUser Roll: [10] = 10 Result: 10"
        self.assertEqual(expected_response, response)
