"""Menu manager class."""


from views.menu import MenuView
from os import system


class MenuManager:
    """Class managing the starting menu."""

    def __init__(self) -> None:
        """Class initializer."""
        self.display = MenuView()

    def select_main_menu_option(self, number_of_options) -> int:
        """Ask for User choice."""
        menu_option = 0
        while menu_option not in range(1, number_of_options + 1):
            try:
                menu_option = int(input(self.display.get_menu()))
            except ValueError:
                system("clear")
                self.display.get_wrong_choice()
            else:
                system("clear")
                if menu_option not in range(1, number_of_options + 1):
                    self.display.get_wrong_choice()
        return menu_option
