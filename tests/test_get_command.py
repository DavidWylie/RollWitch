from unittest import TestCase
from unittest.mock import patch
from roll_witch.rolling import command


class TestGetCommand(TestCase):
    @patch("random.randint")
    def test_invalid_command(self, mock_roll):
        mock_roll.side_effect = [1,2,3,4,5,6]
        response, input_text = command.get_command("hello")

        self.assertIsNone(response)
