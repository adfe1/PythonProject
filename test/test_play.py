import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Sicherstellen, dass der Pfad zum 'source' Verzeichnis korrekt hinzugefügt wird
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, '..', 'source')
sys.path.append(source_dir)

# Hier sicherstellen, dass das play-Modul korrekt importiert wird
import play

# Wir gehen davon aus, dass die Klasse Round und die notwendigen Importe bereits im Scope sind
class TestRoundGame(unittest.TestCase):

    def setUp(self):
        """Set up initial conditions for the tests."""
        # Initialisiere grundlegende Kartenparameter (für Testzwecke, kleine Karte)
        self.arena = [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]
        self.traps = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
        self.length = 3
        self.width = 3
        self.safe_field = 5  # Es gibt 5 sichere Felder auf dieser kleinen Karte

    @patch('builtins.input', return_value="1 1")  # Mock input für Benutzer, um die Zelle (1,1) auszuwählen
    @patch('sys.stdout', new_callable=StringIO)  # Erfasst die gedruckte Ausgabe
    def test_play_valid_input(self, mock_stdout, mock_input):
        """Test, dass play() mit gültigem Input funktioniert und die korrekte Arena ausgegeben wird."""
        arena, traps, length, width, safe_field = play.Round.play()

        # Überprüfe, ob die Arena korrekt aktualisiert wurde (wir nehmen an, mine_count ist korrekt für (1, 1) und keine Bombe dort)
        self.assertEqual(arena[0][0], '0')  # Nach Auswahl von (1,1) sollte '0' für keine Bomben in der Nähe angezeigt werden
        self.assertEqual(safe_field, 4)  # Das sichere Feld sollte nach einem gültigen Zug um 1 verringert werden

        # Überprüfe, ob die korrekte Ausgabe gedruckt wurde
        output = mock_stdout.getvalue()
        self.assertIn("Arena:", output)  # Sollte den Arenahaupttext drucken
        self.assertIn("Mine count in the selected cell:", output)  # Sollte die Minenzahl erwähnen

    @patch('builtins.input', return_value="3 3")  # Mock input für Benutzer, um (3,3) auszuwählen, was eine Falle enthält
    @patch('sys.stdout', new_callable=StringIO)  # Erfasst die gedruckte Ausgabe
    def test_play_invalid_input(self, mock_stdout, mock_input):
        """Test, dass play() korrekt funktioniert, wenn der Benutzer eine Falle trifft."""
        # Sollte einen Neustart auslösen, da (3,3) eine Falle enthält
        arena, traps, length, width, safe_field = play.Round.play()

        # Überprüfe, ob das Spiel bei einer Falle neu startet
        self.assertEqual(arena[2][2], 'X')  # Die Zelle (3,3) sollte 'X' bleiben (nicht aktualisiert wegen der Bombe)
        self.assertEqual(safe_field, 5)  # Das sichere Feld bleibt gleich, da es eine Bombe war
        output = mock_stdout.getvalue()
        self.assertIn("Mine count in the selected cell:", output)  # Sollte die Minenzahl erwähnen

    @patch('sys.stdout', new_callable=StringIO)  # Erfasst die gedruckte Ausgabe
    def test_cheat_mode(self, mock_stdout):
        """Test, dass cheat_mode() korrekt die Fallen-Anordnung ausgibt."""
        play.Round.cheat_mode()

        # Überprüfe, ob die Ausgabe die korrekte Fallen-Anordnung enthält
        output = mock_stdout.getvalue()
        self.assertIn("Traps (1 = Bomb, 0 = Safe):", output)  # Sollte "Traps" erwähnen
        self.assertIn(" 1 2 3", output)  # Sollte die Spalten drucken
        self.assertIn(" 0 1 0", output)  # Die erste Reihe der Fallen
        self.assertIn(" 0 0 1", output)  # Die zweite Reihe der Fallen
        self.assertIn(" 1 0 0", output)  # Die dritte Reihe der Fallen

    @patch('builtins.input', return_value="1 1")  # Mock input
    @patch('sys.stdout', new_callable=StringIO)  # Erfasst die gedruckte Ausgabe
    def test_game(self, mock_stdout, mock_input):
        """Test den Spiel-Loop, um sicherzustellen, dass es startet und eine Runde spielt."""
        # Normalerweise würde dies in einer Schleife laufen, wir wollen jedoch nach einem Aufruf herausbrechen
        with patch.object(play.Round, 'play', return_value=(self.arena, self.traps, self.length, self.width, self.safe_field)):
            play.Round.game()  # Dies sollte einmal ausgeführt werden und dann abbrechen

        # Überprüfe, ob die Spiel-Schleife mindestens einmal die korrekte Spiel-Ausgabe druckt
        output = mock_stdout.getvalue()
        self.assertIn("Arena:", output)  # Sollte den Arenahaupttext drucken
        self.assertIn("Mine count in the selected cell:", output)  # Sollte die Minenzahl erwähnen


if __name__ == "__main__":
    unittest.main()
