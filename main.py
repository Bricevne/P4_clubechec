"""Main code."""

from controller.menu import MenuManager
from controller.player import PlayerManager


def main():
    """Code managing the whole tournament process."""
    menu_manager = MenuManager()
    player_manager = PlayerManager()

    software_on = True
    while software_on is True:
        user_choice = menu_manager.select_menu_option()
        if user_choice == 1:
            software_on = False
        elif user_choice == 2:
            added_player = player_manager.add_player()
        elif user_choice == 3:
            software_on = False
        elif user_choice == 4:
            software_on = False


if __name__ == "__main__":
    main()
