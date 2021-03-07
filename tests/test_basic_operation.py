from unittest import TestCase
from unittest.mock import patch
from roll_witch.rolling import command

class TestStandardOperation(TestCase):
    @patch("random.randint")
    def test_easy_dice_roll(self, mock_roll):
        mock_roll.side_effect = [10]
        response = command.basic.execute("t33 easy", "Another TestUser")
        expected_response = "Another TestUser " \
                            "Roll: [10] = 10 " \
                            "Total: 10 " \
                            "Target: 66 " \
                            "Result: Special"
        self.assertEqual(expected_response, response)

    @patch("random.randint")
    def test_hard_dice_roll(self, mock_roll):
        mock_roll.side_effect = [10]
        response = command.basic.execute("t40 hard", "Another TestUser")
        expected_response = "Another TestUser " \
                            "Roll: [10] = 10 " \
                            "Total: 10 " \
                            "Target: 20 " \
                            "Result: Success"
        self.assertEqual(expected_response, response)
