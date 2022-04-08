"""Main code."""

from controller.menu import MenuManager
from controller.player import PlayerManager


def main():
    """Code managing the whole tournament process."""
    menu_manager = MenuManager()
    player_manager = PlayerManager()

    running = True
    while running is True:
        user_choice = menu_manager.select_menu_option()
        if user_choice == 1:
            running = False
        elif user_choice == 2:
            added_player = player_manager.add_player()
        elif user_choice == 3:
            running = False
        elif user_choice == 4:
            running = False


if __name__ == "__main__":
    main()
