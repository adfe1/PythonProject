"""Play Mechaniks """
import os
import game_start
import world_gen

# Initialize map and traps
M = world_gen.Map()
arena, traps, length, width, safe_field = M.map(difficulty="medium")

"""Module for the game mechanics"""

class Round:
    """Handles all game mechanics."""

    safe = safe_field

    @staticmethod
    def play()-> tuple[list[list[str]], list[list[int]], int, int, int]:
        """Play mechanics."""
        safe = safe_field
        h = game_start.Hub()
        mine_count = 0

        # Getting user input and checking for validity
        try:
            i, j = input("Welches Feld wollen Sie aufdecken (z.B. 1 1): ").split()
            y = int(i) - 1
            x = int(j) - 1

            if x < 0 or x >= width or y < 0 or y >= length:
                print("Ungültige Eingabe! Bitte geben Sie gültige Koordinaten ein.")
                return arena, traps, length, width, safe_field
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie zwei Zahlen ein.")
            return arena, traps, length, width, safe_field

        # Check if the selected cell contains a trap
        if traps[x][y] == 0:  # No bomb in the selected cell
            safe -= 1
        else:  # Bomb found
            h.restart()
            return arena, traps, length, width, safe_field

        # Counting bombs around the selected cell
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < length:  # Make sure we're within bounds
                    if traps[nx][ny] == 1:
                        mine_count += 1

        # Update the arena with the mine count in the selected cell
        arena[x][y] = str(mine_count)

        # Check if the game has been won
        if safe <= 0:
            h.win()

        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

        # Print the generated map with coordinates
        print("\nArena:")
        # Print column numbers above the map with correct alignment
        print("   ", end="")  # Align the column numbers
        for col in range(length):
            print(f"{col + 1:2}", end=" ")  # Print column numbers aligned
        print()

        # Print each row of the arena
        for row in range(width):
            print(f"{row + 1:2} ", end="")  # Print row numbers aligned
            for col in range(length):
                print(f" {arena[row][col]} ", end="")  # Print each cell
            print()

        print("\nMine count in the selected cell:", mine_count)

        return arena, traps, length, width, safe_field

    @staticmethod
    def cheat_mode() -> None:
        """Hidden cheat mode to display trap placement in the main menu."""
        print("\nTraps (1 = Bomb, 0 = Safe):")
        # Print column numbers above the traps map with correct alignment
        print("   ", end="")  # Align the column numbers
        for col in range(length):
            print(f"{col + 1:2}", end=" ")  # Print column numbers aligned
        print()

        # Print each row of traps
        for row in range(width):
            print(f"{row + 1:2} ", end="")  # Print row numbers aligned
            for col in range(length):
                print(f" {traps[row][col]} ", end="")  # Print trap values (0 or 1)
            print()
        game_start.Hub.start()

    @staticmethod
    def game()->None:
        """This function is called to start a new game."""
        while True:
            Round.play()
