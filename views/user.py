"""User view."""


class UserView:
    """Class managing user views."""

    def __init__(self) -> None:
        """Initialize class."""
        pass

    def display_welcome(self) -> None:
        """Print a message welcoming the user."""
        message = "Welcome to the event! Please choose an option."
        print(message)

    def get_name(self) -> str:
        """Return name message.

        Returns:
            str: Name information
        """
        return "Name: "

    def get_surname(self) -> str:
        """Return surname message.

        Returns:
            str: Surname information
        """
        return "Surname: "

    def get_birthdate(self) -> str:
        """Return birthdate message.

        Returns:
            str: Birthdate information
        """
        return "Birthdate: "

    def get_gender(self) -> str:
        """Return gender message.

        Returns:
            str: Gender information
        """
        return "Gender (M/F): "

    def get_elo(self) -> str:
        """Return elo message.

        Returns:
            str: Elo information
        """
        return "Elo: "

    def get_wrong_elo(self) -> None:
        """Print a message when the elo is wrong."""
        print("Elo must be an integer.")

    def get_wrong_gender(self) -> None:
        """Print a message when the user's gender input is wrong."""
        print("Gender must be M for males and F for females.")

    def get_wrong_birthdate(self) -> None:
        """Print a message when the user's birthdate input is wrong."""
        print("Birthdate must be in the format YYYY-MM-DD.")

    def get_confirmation(self) -> str:
        """Ask for the user's confirmation to add a player.

        Returns:
            str: Confirmation message
        """
        return "Do you confirm? (y/n) : "

    def display_player_confirmation(self) -> None:
        """Print a confirmation when a player has been successfully added."""
        print("The player has successfully been added!")

    def display_sorted_players(self, player: dict) -> None:
        """Print players' information present in the database.

        Args:
            player (dict): Dictionnary of a player's information
        """
        print(
            f"id: {player.doc_id}   player: {player['name']} {player['surname']}   "
            f"gender: {player['gender']}   elo: {player['elo']}"
        )

    def get_player_by_id(self) -> str:
        """Return player's id message.

        Returns:
            str: id information
        """
        message = "Select the player's id: "
        return message

    def get_new_elo(self) -> str:
        """Return new elo message.

        Returns:
            str: New elo information
        """
        message = "New elo: "
        return message

    def display_successful_change(self) -> None:
        """Print a message for a successful elo change."""
        message = "Player's elo has been successfully modified."
        print(message)

    def display_unsuccessful_change(self) -> None:
        """Print a message when the user picks an ID not attributed to a player."""
        message = "No player with this ID has been found."
        print(message)

    def display_wrong_id_type(self) -> None:
        """Print a message when the user inserts a wrong id."""
        message = "This is not an ID."
        print(message)

    def display_tournaments(self, tournament: dict) -> None:
        """Print tournaments' information.

        Args:
            tournament (dict): Dictionnary of a tournament's information
        """
        print(
            f"id: {tournament.doc_id}   name: {tournament['name']}  place: {tournament['place']}   "
            f"description: {tournament['description']}"
        )

    def get_tournament_by_id(self) -> str:
        """Return a message to ask the user an id.

        Returns:
            str: Message asking for a tournament's id
        """
        message = "Select the tournament's id: "
        return message
