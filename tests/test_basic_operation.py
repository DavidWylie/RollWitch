from unittest import TestCase
from unittest.mock import patch
from rolling.command import BasicOperation


class TestStandardOperation(TestCase):
    @patch("random.randint")
    def test_easy_dice_roll(self, mock_roll):
        mock_roll.side_effect = [10]
        operation = BasicOperation()
        response = operation.execute("t33 easy", "Another TestUser")
        actual_result = operation.format_output(response, "Another TestUser")
        expected_response = "Another TestUser " \
                            "Roll: [10] = 10 " \
                            "Total: 10 " \
                            "Target: 66 " \
                            "Result: Special"
        self.assertEqual(expected_response, actual_result)

    @patch("random.randint")
    def test_hard_dice_roll(self, mock_roll):
        mock_roll.side_effect = [10]
        operation = BasicOperation()
        response = operation.execute("t40 hard", "Another TestUser")
        actual_result = operation.format_output(response, "Another TestUser")
        expected_response = "Another TestUser " \
                            "Roll: [10] = 10 " \
                            "Total: 10 " \
                            "Target: 20 " \
                            "Result: Success"
        self.assertEqual(expected_response, actual_result)
