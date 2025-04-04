import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, '..', 'source')
sys.path.append(source_dir)
# test_game_start.py
import unittest
from game_start import Hub

class TestGameStart(unittest.TestCase):
    def setUp(self):
        """Initialisiert die Hub-Klasse vor jedem Test."""
        self.hub = Hub()

    def test_hub_instance(self):
        """Testet, ob eine Instanz der Hub-Klasse korrekt erstellt wird."""
        self.assertIsInstance(self.hub, Hub, "Die erstellte Instanz sollte vom Typ Hub sein.")

    def test_main_method(self):
        """Testet, ob die main-Methode der Hub-Klasse ohne Fehler ausgeführt wird."""
        try:
            self.hub.main()
        except Exception as e:
            self.fail(f"Die main-Methode hat einen Fehler ausgelöst: {e}")

if __name__ == '__main__':
    unittest.main()
