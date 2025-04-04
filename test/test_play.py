import unittest
from unittest.mock import patch
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, '..', 'source')
sys.path.append(source_dir)

from play import (Round)

class TestPlayMechanics(unittest.TestCase):
    def setUp(self):
        """Setup for the tests."""
        self.round = Round()

    @patch('builtins.input', return_value="1 1")
    @patch('os.system')  # Mock os.system to prevent clearing the terminal during tests
    def test_play_valid_input(self, mock_system, mock_input):
        """Test play method with valid input."""
        arena, traps, length, width, safe_field = Round.play()
        self.assertIsInstance(arena, list)
        self.assertIsInstance(traps, list)
        self.assertIsInstance(length, int)
        self.assertIsInstance(width, int)
        self.assertIsInstance(safe_field, int)

    @patch('builtins.input', side_effect=["invalid", "1 1"])
    @patch('os.system')  # Mock os.system to prevent clearing the terminal during tests
    def test_play_invalid_input(self, mock_system, mock_input):
        """Test play method with invalid input followed by valid input."""
        arena, traps, length, width, safe_field = Round.play()
        self.assertIsInstance(arena, list)

    def test_cheat_mode(self):
        """Test cheat_mode method."""
        with patch('builtins.print') as mock_print:
            Round.cheat_mode()
            # Check if the traps map is printed
            mock_print.assert_called()

    @patch('play.Round.play', side_effect=KeyboardInterrupt)
    def test_game_exit(self, mock_play):
        """Test game method to ensure it exits on KeyboardInterrupt."""
        with self.assertRaises(KeyboardInterrupt):
            Round.game()

if __name__ == '__main__':
    unittest.main()
