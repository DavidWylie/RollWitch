from unittest import TestCase
from unittest.mock import patch
from roll_witch.rolling import command


class TestShadowrunOperation(TestCase):
    @patch("random.randint")
    def test_shadowrun_dice_roll(self, mock_roll):
        mock_roll.side_effect = [1,2,3,4,5,6]
        response = command.shadow_run.execute("6d6", "Another TestUser")
        expected_response = "Another TestUser Roll: [1, 2, 3, 4, 5, 6] Result: 2"
        self.assertEqual(expected_response, response)
