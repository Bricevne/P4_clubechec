"""Menu manager class."""


from typing import Callable
from views.menu import MenuView
from os import system


class MenuManager:
    """Class managing the starting menu."""

    def __init__(self) -> None:
        """Class initializer."""
        self.menu_view = MenuView()

    def select_menu_option(self, number_of_options: int, get_menu: Callable) -> int:
        """Ask for User's choice in a list of options.

        If the user's input is wrong, display an error message until the input is right.

        Args:
            number_of_options (int): Number of options in the menu
            get_menu (Callable): Function calling the menu

        Returns:
            int: Number of the chosen option
        """
        menu_option = 0
        while menu_option not in range(1, number_of_options + 1):
            try:
                menu_option = int(input(get_menu()))
            except ValueError:
                system("clear")
                self.menu_view.get_wrong_choice()
            else:
                system("clear")
                if menu_option not in range(1, number_of_options + 1):
                    self.menu_view.get_wrong_choice()
        return menu_option
