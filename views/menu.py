"""Menu view."""


class MenuView:
    """Class managing menu displays."""

    def __init__(self) -> None:
        """Initialize class."""
        pass

    def display_welcome(self) -> None:
        """Print a message welcoming the user."""
        message = "Welcome to the event! Please choose an option."
        print(message)

    def get_menu(self) -> str:
        """Return main menu.

        Returns:
            str: The main menu
        """
        menu_options = "\n\
        1. Create tournament\n\
        2. Add player\n\
        3. Display players\n\
        4. Import Tournament\n\
        5. List of Tournaments\n\
        6. Quit\n"
        return menu_options

    def get_wrong_choice(self) -> None:
        """Print an error message when the user picks a wrong option."""
        error_message = "Oops! That was no valid option. Try again."
        print(error_message)
