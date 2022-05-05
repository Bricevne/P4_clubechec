"""User view."""


class UserView:
    """Class managing user views."""

    def __init__(self) -> None:
        """Initialize class."""
        pass

    def get_name(self) -> str:
        """Display name."""
        return "Name: "

    def get_surname(self) -> str:
        """Display surname."""
        return "Surname: "

    def get_birthdate(self) -> str:
        """Display birthdate."""
        return "Birthdate: "

    def get_gender(self) -> str:
        """Display gender."""
        return "Gender (M/F): "

    def get_elo(self) -> str:
        """Display rank."""
        return "Elo: "

    def get_confirmation(self) -> str:
        """Ask for the user's confirmation."""
        return "Do you confirm? (y/n) : "

    def get_wrong_option(self) -> str:
        """Get wrong option."""
        print("Select a valid option.")

    def display_player_confirmation(self) -> str:
        """"""
        print("The player has successfully been added!")

    def display_sorted_players(self, player):
        print(
            f"id: {player.doc_id}   player: {player['name']} {player['surname']}   "
            f"gender: {player['gender']}   elo: {player['elo']}"
        )

    def get_submenu(self) -> str:
        """Display submenu."""
        menu_options = "\n\
        1. Modify player information\n\
        2. Display by surname\n\
        3. Display by elo\n\
        4. Back to menu\n"
        return menu_options
