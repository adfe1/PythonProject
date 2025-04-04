import sys
import os
import unittest
from unittest.mock import patch

# Ensure the path to the 'source' directory is correctly added
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, '..', 'source')
sys.path.append(source_dir)
# test_hub.py
from game_start import Hub

class TestHub(unittest.TestCase):
    @patch('builtins.print')
    @patch('os.system')  # Mock os.system to prevent clearing the terminal
    def test_clear_screen(self, mock_system, mock_print):
        """Test the clear_screen method."""
        Hub.clear_screen()
        mock_system.assert_called_once()  # Ensure os.system is called

    @patch('builtins.print')
    def test_display_loading_bar(self, mock_print):
        """Test the display_loading_bar method."""
        Hub.display_loading_bar()
        self.assertGreater(mock_print.call_count, 0)  # Ensure print is called multiple times

    @patch('builtins.input', return_value="1")
    @patch('hub.Hub.clear_screen')
    @patch('play.Round.game')
    def test_start_play_option(self, mock_game, mock_clear_screen, mock_input):
        """Test the start method with 'Play' option."""
        Hub.start()
        mock_game.assert_called_once()  # Ensure play.Round.game is called

    @patch('builtins.input', return_value="3")
    @patch('sys.exit')
    def test_start_quit_option(self, mock_exit, mock_input):
        """Test the start method with 'Quit' option."""
        Hub.start()
        mock_exit.assert_called_once()  # Ensure sys.exit is called

    @patch('builtins.input', return_value="easy")
    @patch('world_gen.Map.map')
    def test_start_change_difficulty(self, mock_map, mock_input):
        """Test the start method with 'Change difficulty' option."""
        Hub.start()
        mock_map.assert_called_once_with("easy")  # Ensure world_gen.Map.map is called with difficulty

    @patch('builtins.input', return_value="y")
    @patch('hub.Hub.clear_screen')
    @patch('play.Round.game')
    def test_restart_yes_option(self, mock_game, mock_clear_screen, mock_input):
        """Test the restart method with 'Yes' option."""
        Hub.restart()
        mock_game.assert_called_once()  # Ensure play.Round.game is called

    @patch('builtins.input', return_value="n")
    @patch('hub.Hub.clear_screen')
    def test_restart_no_option(self, mock_clear_screen, mock_input):
        """Test the restart method with 'No' option."""
        Hub.restart()
        mock_clear_screen.assert_called_once()  # Ensure Hub.clear_screen is called

    @patch('builtins.input', return_value="1")
    @patch('hub.Hub.clear_screen')
    @patch('play.Round.game')
    def test_win_play_again_option(self, mock_game, mock_clear_screen, mock_input):
        """Test the win method with 'Play again' option."""
        Hub.win()
        mock_game.assert_called_once()  # Ensure play.Round.game is called

    @patch('builtins.input', return_value="2")
    @patch('hub.Hub.clear_screen')
    def test_win_main_menu_option(self, mock_clear_screen, mock_input):
        """Test the win method with 'Main menu' option."""
        Hub.win()
        mock_clear_screen.assert_called_once()  # Ensure Hub.clear_screen is called

    @patch('builtins.print')
    @patch('builtins.input', return_value="")
    @patch('hub.Hub.clear_screen')
    def test_display_credits(self, mock_clear_screen, mock_input, mock_print):
        """Test the display_credits method."""
        Hub.display_credits()
        self.assertGreater(mock_print.call_count, 0)  # Ensure credits are printed
        mock_clear_screen.assert_called_once()  # Ensure Hub.clear_screen is called

if __name__ == '__main__':
    unittest.main()
