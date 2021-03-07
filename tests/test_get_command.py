from unittest import TestCase
from unittest.mock import patch
from roll_witch.rolling import command


class TestGetCommand(TestCase):
    def test_invalid_command(self):
        response, input_text = command.get_command("hello")
        self.assertIsNone(response)

    def test_spacing_in_commands(self):
        response, input_text = command.get_command("! Roll 1d6")
        expected, test_input_text = command.get_command("!roll 1d6")
        self.assertEqual(expected, response)
