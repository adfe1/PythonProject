"""All screens like Start, death,winning Screen"""
import sys
import os
import world_gen
import play


class Hub:
    """Handles the Main menu."""

    @staticmethod
    def clear_screen()->None:
        """Clear terminal screen for different OS."""
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def display_loading_bar()->None:
        """Display loading bar for the map creation."""
        for i in range(101):
            barr = '█' * (i // 2)
            print(f'\r|{barr:<50}| {i}%', end='')
        print()

    @staticmethod
    def start()->None:
        """Start the main game hub."""
        print("Welcome to the Game \nMap Creation:")
        Hub.display_loading_bar()

        print("\nSpace Survival")
        print("1. Play \n2. Change difficulty \n3. Quit \n4. Credits")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                Hub.clear_screen()
                play.Round.game()
            elif choice == 2:
                diff = input("Choose difficulty (easy/medium/hard): ").lower()
                world_gen.Map.map(diff)
                Hub.clear_screen()
                Hub.start()  # Restart the main menu
            elif choice == 3:
                print("Thank you for playing")
                sys.exit()  # Exit the program
            elif choice == 4:
                Hub.display_credits()
            elif choice == 6:
                play.Round.cheat_mode()
            else:
                print("Invalid choice. Please select a valid option.")
                Hub.start()  # Restart the main menu on invalid choice
        except ValueError:
            print("Please enter a valid number.")
            Hub.start()  # Restart the main menu if input is not a number

    @staticmethod
    def restart()->None:
        """Handle the restart logic after dying."""
        r = input("You died \nDo you want to restart? Y/N \n")
        if r.lower() == "y":
            Hub.clear_screen()
            diff = input("Enter difficulty (easy/medium/hard): ").lower()
            world_gen.Map.map(diff)
            play.Round.game()
        elif r.lower() == "n":
            Hub.clear_screen()
            Hub.start()  # Return to the main menu
        else:
            print("Invalid input, please enter Y or N.")
            Hub.restart()  # Retry if input is invalid

    @staticmethod
    def win()->None:
        """Handle winning logic."""
        print("You won!")
        w = input("Do you want to play again? (1) or go back to the main menu? (2) ")
        if w == "1":
            Hub.clear_screen()
            play.Round.game()
        elif w == "2":
            Hub.clear_screen()
            Hub.start()  # Go back to the main menu
        else:
            print("Invalid input, please choose 1 or 2.")
            Hub.win()  # Retry if input is invalid

    @staticmethod
    def display_credits()->None:
        """Display the credits of the game."""
        print("Game created by Adrian Fetscher")
        input("Press Enter to return to the main menu...")
        Hub.clear_screen()
        Hub.start()  # Go back to the main menu

    @staticmethod
    def main()->None:
        """Main entry point of the Hub."""
        Hub.start()  # Start the game hub
pass
