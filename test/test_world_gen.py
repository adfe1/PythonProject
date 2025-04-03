import unittest
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, '..', 'source')
sys.path.append(source_dir)

from world_gen import Map

# Assuming the Map class is already defined in the scope

class TestMapGeneration(unittest.TestCase):

    def test_easy_difficulty(self):
        arena, traps, length, width, safe_field = Map.map("easy")

        # Check map size based on difficulty
        self.assertGreaterEqual(length, 4)
        self.assertLessEqual(length, 5)
        self.assertGreaterEqual(width, 4)
        self.assertLessEqual(width, 5)

        # Ensure that safe_field is within bounds
        total_cells = length * width
        self.assertGreaterEqual(safe_field, 0)
        self.assertLessEqual(safe_field, total_cells)

        # Check that traps are correctly distributed according to trap density
        total_traps = sum([sum(row) for row in traps])
        expected_traps = total_cells * 0.2  # Expected traps based on difficulty
        self.assertAlmostEqual(total_traps, expected_traps, delta=total_cells * 0.1)  # Allowing a margin for randomness

    def test_medium_difficulty(self):
        arena, traps, length, width, safe_field = Map.map("medium")

        # Check map size based on difficulty
        self.assertGreaterEqual(length, 6)
        self.assertLessEqual(length, 7)
        self.assertGreaterEqual(width, 6)
        self.assertLessEqual(width, 7)

        # Ensure that safe_field is within bounds
        total_cells = length * width
        self.assertGreaterEqual(safe_field, 0)
        self.assertLessEqual(safe_field, total_cells)

        # Check that traps are correctly distributed according to trap density
        total_traps = sum([sum(row) for row in traps])
        expected_traps = total_cells * 0.3  # Expected traps based on difficulty
        self.assertAlmostEqual(total_traps, expected_traps, delta=total_cells * 0.1)  # Allowing a margin for randomness

    def test_hard_difficulty(self):
        arena, traps, length, width, safe_field = Map.map("hard")

        # Check map size based on difficulty
        self.assertGreaterEqual(length, 8)
        self.assertLessEqual(length, 9)
        self.assertGreaterEqual(width, 8)
        self.assertLessEqual(width, 9)

        # Ensure that safe_field is within bounds
        total_cells = length * width
        self.assertGreaterEqual(safe_field, 0)
        self.assertLessEqual(safe_field, total_cells)

        # Check that traps are correctly distributed according to trap density
        total_traps = sum([sum(row) for row in traps])
        expected_traps = total_cells * 0.4  # Expected traps based on difficulty
        self.assertAlmostEqual(total_traps, expected_traps, delta=total_cells * 0.1)  # Allowing a margin for randomness

    def test_invalid_difficulty(self):
        # Test invalid difficulty level
        with self.assertRaises(ValueError):
            Map.map("invalid")

    def test_type_annotations(self):
        # Ensure return type is a tuple with the correct structure
        arena, traps, length, width, safe_field = Map.map("easy")

        self.assertIsInstance(arena, list)
        self.assertIsInstance(traps, list)
        self.assertIsInstance(length, int)
        self.assertIsInstance(width, int)
        self.assertIsInstance(safe_field, int)

        # Check that arena and traps are lists of lists
        self.assertTrue(all(isinstance(row, list) for row in arena))
        self.assertTrue(all(isinstance(row, list) for row in traps))


if __name__ == "__main__":
    unittest.main()