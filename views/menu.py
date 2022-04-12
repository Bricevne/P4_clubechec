"""Menu view."""


class MenuView:
    """Class managing menu displays."""

    def __init__(self) -> None:
        """Initialize class."""
        pass

    def get_menu(self) -> str:
        """Display menu."""
        menu_options = "Welcome to the event! Please choose an option.\n\
        1. Create tournament\n\
        2. Add player\n\
        3. View ranking\n\
        4. Quit\n"
        return menu_options

    def get_wrong_choice(self):
        """Display error message."""
        error_message = "Oops! That was no valid option. Try again."
        print(error_message)
