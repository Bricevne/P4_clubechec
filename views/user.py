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

    def get_wrong_elo(self) -> None:
        print("Elo must be an integer.")

    def get_wrong_gender(self) -> None:
        print("Gender must be M for males and F for females.")

    def get_wrong_birthdate(self) -> None:
        print("Birthdate must be in the format YYYY-MM-DD.")

    def get_confirmation(self) -> str:
        """Ask for the user's confirmation."""
        return "Do you confirm? (y/n) : "

    def get_wrong_option(self) -> str:
        """Get wrong option."""
        print("Oops! That was no valid option, try again.")

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

    def get_player_by_id(self) -> str:
        message = "Select the player's id: "
        return message

    def get_new_elo(self) -> str:
        message = "New elo: "
        return message

    def display_successful_change(self) -> str:
        message = "Player's elo has been successfully modified."
        print(message)

    def display_unsuccessful_change(self) -> str:
        message = "No player with this ID has been found."
        print(message)

    def display_wrong_id_type(self) -> str:
        message = "This is not an ID."
        print(message)

    def get_import_menu(self):
        """Display submenu."""
        menu_options = "\n\
        1. Select a tournament\n\
        2. Back to menu\n"
        return menu_options

    def display_tournaments(self, tournament):
        print(
            f"id: {tournament.doc_id}   name: {tournament['name']}  place: {tournament['place']}   "
            f"description: {tournament['description']}"
        )

    def get_tournament_by_id(self) -> str:
        message = "Select the tournament's id: "
        return message
