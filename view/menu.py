"""Menu view."""


class MenuView:
    """Class managing menu displays."""

    @staticmethod
    def get_menu():
        """Display menu."""
        menu_options = "1. Create tournament \n2. Add player \n3. View ranking \n"
        return menu_options

    @staticmethod
    def get_wrong_choice():
        """Display error message."""
        error_message = "Oops!  That was no valid option.  Try again."
        return error_message
