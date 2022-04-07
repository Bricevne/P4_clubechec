"""Menu manager class."""


from view.menu import MenuView


class MenuManager:
    """Class managing the starting menu."""

    def __init__(self):
        """Init."""
        self.display = MenuView()

    def select_menu_option(self):
        """Ask for User choice."""
        menu_option = 0
        while menu_option not in (1, 2, 3):
            try:
                menu_option = int(input(self.display.get_menu()))
            except (TypeError, ValueError):
                self.display.get_wrong_choice()
        return menu_option
