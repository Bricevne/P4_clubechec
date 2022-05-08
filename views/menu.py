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

    def get_tournament_information_menu(self) -> str:
        """Return a message with a menu.

        Returns:
            str: Message of options when selecting a tournament
        """
        menu_options = "\n\
        1. Display player (rank)\n\
        2. Display player (alphabet)\n\
        3. Display rounds\n\
        4. Display matches\n\
        5. Back to menu\n"
        return menu_options

    def get_player_submenu(self) -> str:
        """Return submenu.

        Returns:
            str: Message to display the submenu
        """
        menu_options = "\n\
        1. Modify player information\n\
        2. Display by surname\n\
        3. Display by elo\n\
        4. Back to menu\n"
        return menu_options

    def get_import_menu(self) -> str:
        """Return a message with a menu.

        Returns:
            str: Message of options when importing a tournament
        """
        menu_options = "\n\
        1. Select a tournament\n\
        2. Back to menu\n"
        return menu_options

    def get_tournament_options(self) -> str:
        """Return the tournament menu.

        Returns:
            str: Tournament menu
        """
        menu_options = "\n\
        1. Start tournament\n\
        2. Modify round numbers\n\
        3. Modify number of players\n\
        4. Quit\n"
        return menu_options

    def get_round_options(self) -> str:
        """Return round menu.

        Returns:
            str: Round menu
        """
        menu_options = "\n\
        1. New round\n\
        2. Show ranking\n\
        3. Quit\n"
        return menu_options
