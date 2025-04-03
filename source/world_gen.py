# pylint: disable=too-few-public-methods
"""Map Generation"""
import random
import typing
from typing import Tuple, List


class Map:
    """
    Class responsible for creating the game map based on the selected difficulty.
    """

    @staticmethod
    def map(difficulty: str) -> Tuple[List[List[str]], List[List[int]], int, int, int]:
        """
        Generates the game map based on the selected difficulty.

        Args:
            difficulty (str): The difficulty level for the map ('easy', 'medium', 'hard').

        Returns:
            tuple: Contains the map (arena), traps, length, width, and the number of safe fields.
        """
        # Define difficulty parameters
        difficulty_params = {
            "easy": {"length": (4, 5), "width": (4, 5), "trap_density": 0.2},
            "medium": {"length": (6, 7), "width": (6, 7), "trap_density": 0.3},
            "hard": {"length": (8, 9), "width": (8, 9), "trap_density": 0.4}
        }

        if difficulty not in difficulty_params:
            raise ValueError("Invalid difficulty level")

        params:typing.Any = difficulty_params[difficulty]
        length:int = random.randint(*params["length"])
        width:int = random.randint(*params["width"])
        trap_density = params["trap_density"]

        # Initialize arena and traps
        arena= [["X" for _ in range(length)] for _ in range(width)]
        traps = [[0 for _ in range(length)] for _ in range(width)]

        # Fill the traps array with random values based on difficulty
        safe_field: int  = 0
        for x in range(width):
            for y in range(length):
                if random.random() < trap_density:
                    traps[x][y] = 1  # Place a trap
                else:
                    traps[x][y] = 0  # No trap
                    safe_field += 1  # Count safe fields

        return arena, traps, length, width, safe_field
