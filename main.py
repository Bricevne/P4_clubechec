"""Main code."""

from controllers.menu import MenuManager
from controllers.user import UserManager


def main():
    """Code managing the whole tournament process."""
    menu_manager = MenuManager()
    user_manager = UserManager()

    running = True
    while running is True:
        user_choice = menu_manager.select_menu_option()
        if user_choice == 1:
            running = False
        elif user_choice == 2:
            added_player = user_manager.add_player()
        elif user_choice == 3:
            running = False
        elif user_choice == 4:
            running = False


if __name__ == "__main__":
    main()
