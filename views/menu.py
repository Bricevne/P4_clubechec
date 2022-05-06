"""Menu view."""


class MenuView:
    """Class managing menu displays."""

    def __init__(self) -> None:
        """Initialize class."""
        pass

    def display_welcome(self) -> None:
        """_summary_."""
        message = "Welcome to the event! Please choose an option."
        print(message)

    def get_menu(self) -> str:
        """Display menu."""
        menu_options = "\n\
        1. Create tournament\n\
        2. Add player\n\
        3. Display players\n\
        4. Import Tournament\n\
        5. Quit\n"
        return menu_options

    def get_wrong_choice(self) -> None:
        """Display error message."""
        error_message = "Oops! That was no valid option. Try again."
        print(error_message)
