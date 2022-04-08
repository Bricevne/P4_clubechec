"""Menu view."""


class MenuView:
    """Class managing menu displays."""

    @staticmethod
    def get_menu():
        """Display menu."""
        menu_options = "Welcome to the event! Please choose an option.\n\
        1. Create tournament\n\
        2. Add player\n\
        3. View ranking\n\
        4. Quit\n"
        return menu_options

    @staticmethod
    def get_wrong_choice():
        """Display error message."""
        error_message = "Oops! That was no valid option. Try again."
        return print(error_message)
