from roll_witch.rolling.operation.factory import standard_factory
from unittest import TestCase
from unittest.mock import patch


class TestStandardOperation(TestCase):
    @patch("random.randint")
    def test_simple_dice_roll(self, mock_roll):
        mock_roll.side_effect = [10]
        operation = standard_factory.get_roll_operation('regex', "d10", "Another TestUser")
        response = operation.execute()
        expected_response = "Another TestUser Roll: [10] = 10 Result: 10"
        self.assertEqual(expected_response, response)
