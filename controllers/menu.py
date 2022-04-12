"""Menu manager class."""


from views.menu import MenuView


class MenuManager:
    """Class managing the starting menu."""

    def __init__(self) -> None:
        """Class initializer."""
        self.display = MenuView()

    def select_menu_option(self) -> int:
        """Ask for User choice."""
        menu_option = 0
        while menu_option not in (1, 2, 3, 4):
            try:
                menu_option = int(input(self.display.get_menu()))
            except ValueError:
                self.display.get_wrong_choice()
            else:
                if menu_option not in (1, 2, 3, 4):
                    self.display.get_wrong_choice()
        return menu_option
