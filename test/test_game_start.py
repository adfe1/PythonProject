import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Sicherstellen, dass der Pfad zum 'source' Verzeichnis korrekt hinzugefügt wird
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, '..', 'source')
sys.path.append(source_dir)

import game_start  # Hier sicherstellen, dass das game_start-Modul korrekt importiert wird
Hub = game_start.Hub()

class TestHubClass(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_clear_screen(self, mock_stdout):
        """Test clear_screen() works by checking system calls."""
        with patch('os.system') as mock_clear:
            Hub.clear_screen()
            mock_clear.assert_called_once_with('cls' if os.name == 'nt' else 'clear')

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_loading_bar(self, mock_stdout):
        """Test display_loading_bar() prints the loading bar correctly."""
        with patch('builtins.print') as mock_print:
            Hub.display_loading_bar()
            mock_print.assert_any_call("\r|██████████████████████████████████████████████████████| 100%")

    @patch('builtins.input', return_value="1")  # Mock user input for option 1 (Play)
    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_start_play_option(self, mock_stdout, mock_input):
        """Test the 'Play' option in the main menu."""
        with patch.object(Hub, 'clear_screen'), patch.object(Hub, 'start'):
            Hub.start()
            mock_input.assert_called_with("Enter your choice: ")
            self.assertIn("1. Play", mock_stdout.getvalue())  # Ensure play option is displayed

    @patch('builtins.input', return_value="4")  # Mock user input for option 4 (Quit)
    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_start_quit_option(self, mock_stdout, mock_input):
        """Test the 'Quit' option in the main menu."""
        with patch.object(Hub, 'clear_screen'), patch.object(Hub, 'start'):
            with self.assertRaises(SystemExit):  # Quit should exit the program
                Hub.start()
            mock_input.assert_called_with("Enter your choice: ")

    @patch('builtins.input', side_effect=["y", "easy"])  # Mock restart input and difficulty choice
    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_restart(self, mock_stdout, mock_input):
        """Test restart logic after death."""
        with patch.object(Hub, 'clear_screen'), patch.object(Hub, 'start'):
            Hub.restart()
            mock_input.assert_any_call("You died \nDo you want to restart? Y/N \n")  # Check restart prompt
            mock_input.assert_any_call("Enter difficulty (easy/medium/hard): ")  # Check difficulty prompt

    @patch('builtins.input', return_value="1")  # Mock input for option to replay after win
    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_win(self, mock_stdout, mock_input):
        """Test win logic and replay options."""
        with patch.object(Hub, 'clear_screen'), patch.object(Hub, 'start'):
            Hub.win()
            mock_input.assert_called_with("Do you want to play again? (1) or go back to the main menu? (2) ")
            self.assertIn("You won!", mock_stdout.getvalue())  # Ensure win message is shown

    @patch('builtins.input', return_value="1")  # Mock input to go to main menu from credits
    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_display_credits(self, mock_stdout, mock_input):
        """Test that credits are displayed correctly."""
        with patch.object(Hub, 'clear_screen'), patch.object(Hub, 'start'):
            Hub.display_credits()
            self.assertIn("Game created by Adrian Fetscher", mock_stdout.getvalue())  # Ensure credits message is displayed
            mock_input.assert_called_with("Press Enter to return to the main menu...")

    @patch('builtins.input', return_value="1")  # Mock input for option to play
    @patch('sys.stdout', new_callable=StringIO)  # Capture printed output
    def test_main(self, mock_stdout, mock_input):
        """Test the main method calls start correctly."""
        with patch.object(Hub, 'start', return_value=None):
            Hub.main()
            mock_input.assert_called_with("Enter your choice: ")
            self.assertIn("1. Play", mock_stdout.getvalue())  # Ensure menu options are printed

if __name__ == "__main__":
    unittest.main()
