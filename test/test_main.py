import unittest
from unittest.mock import patch
import sys
import os
from io import StringIO

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "source")))

import source.game_start as game_start
class TestHubClass(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_hub_initialization(self, mock_stdout):
        """Test Hub initialization and main method execution."""
        # Create an instance of the Hub class
        h = game_start.Hub()

        # Ensure Hub object is created
        self.assertIsInstance(h, game_start.Hub)

        # Now simulate calling the main method (assuming it's the start of the game or something similar)
        with patch.object(h, 'main', return_value=None):
            h.main()  # Simulate calling the main method

        # Capture printed output from the main method and check
        output = mock_stdout.getvalue()
        # Check if certain expected text or result is printed (adjust according to your actual implementation)
        self.assertIn("Welcome to the game", output)  # For example, if the main method starts with this message

    @patch('builtins.input', return_value="1")  # Mock user input (example)
    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_main_interaction(self, mock_stdout, mock_input):
        """Test user interaction within the Hub's main method."""
        h = game_start.Hub()

        # Simulate calling the main method, which would involve user input
        with patch.object(h, 'main', return_value=None):
            h.main()

        # Capture output
        output = mock_stdout.getvalue()

        # Check if expected interaction was printed (like a prompt or feedback message)
        self.assertIn("Please select an option", output)  # Example message printed during interaction

        # Check that user input was properly mocked (e.g., the option '1' was selected)
        mock_input.assert_called_with("1")  # Check if the input() was called with the prompt

    @patch('builtins.input', return_value="start")  # Mocking input for 'start' option
    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_main_start_game(self, mock_stdout, mock_input):
        """Test if starting the game works within the Hub class."""
        h = game_start.Hub()

        # Simulate starting the game
        with patch.object(h, 'main', return_value=None):
            h.main()

        # Capture printed output and check if game has started
        output = mock_stdout.getvalue()

        # You'd want to adjust this assertion based on what happens when the game starts
        self.assertIn("Game starting...", output)  # Assuming this message is printed when the game starts


if __name__ == "__main__":
    unittest.main()
