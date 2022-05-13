"""Tournament view."""


class TournamentView:
    """Class managing tournament displays."""

    def __init__(self) -> None:
        """Class initializer."""
        pass

    def get_view_name(self) -> str:
        """Return name for input.

        Returns:
            str: Information for name
        """
        return "Name: "

    def get_view_place(self) -> str:
        """Return place for input.

        Returns:
            str: Information for place
        """
        return "Place: "

    def get_view_date(self) -> str:
        """Return date for input.

        Returns:
            str: Information for date
        """
        return "Date: "

    def get_view_time_control(self) -> str:
        """Return time control for input.

        Returns:
            str: Information for time control
        """
        return "Time_control: "

    def get_view_description(self) -> str:
        """Return description for input.

        Returns:
            str: Information for description
        """
        return "Description: "

    def get_view_round(self) -> str:
        """Return number of rounds for input.

        Returns:
            str: Information for number of rounds
        """
        return "Number of rounds: "

    def get_view_players(self) -> str:
        """Return number of players for input.

        Returns:
            str: Information for number of players
        """
        return "Number of players: "

    def get_wrong_player_number(self, number_of_players: int) -> None:
        """Print a message when not enough players are available for the tournament.

        Args:
            number_of_players (int): number of players needed in the database to start the tournament
        """
        print(
            f"You need at least {number_of_players} players to choose from for a tournament."
        )

    def get_player(self) -> str:
        """Return a message for selecting a player.

        Returns:
            str: Message to ask the user for a player's id
        """
        return "Please select a player's id to add him to the tournament : "

    def get_wrong_id(self) -> str:
        """Return a message when a player is already selected or does not exist."""
        print("Please choose a valid id from the list. ")

    def get_wrong_round_number(self) -> None:
        """Print an error message when the user picks a letter instead of a number."""
        error_message = "Oops! This is not a number!"
        print(error_message)

    def get_view_round_name(self) -> str:
        """Return a message to ask the user the current round's name.

        Returns:
            str: Information for round name
        """
        return "Round name: "

    def get_view_match(self, match_counter: int) -> None:
        """Print match results message.

        Args:
            match_counter (int): Count for the number of matches of a round
        """
        message = f"Match {match_counter} | results\n"
        print(message)

    def get_wrong_score_type(self) -> None:
        """Print message when the user inserts a wrong score."""
        message = "You have to give a score (Lose : 0, Win : 1, Draw : 0.5)"
        print(message)

    def show_ranking(self, player: object) -> None:
        """Print the message format for rankings.

        Args:
            player (object): Player instance
        """
        message = f"{player.rank} : {player.name} {player.surname} - Total score : {player.total_score}"
        print(message)

    def display_message_end_tournament(self) -> None:
        """Print a message when the tournament ends."""
        message = "\nThe tournament ended !"
        print(message)

    def display_rounds_superior_to_players(self) -> None:
        """Print a message when the number of rounds is superior or equal to the number of players."""
        message = "The number of rounds must be inferior to the number of players."
        print(message)

    def display_players_inferior_to_rounds(self) -> None:
        """Print a message when the number of players is inferior or equal to the number of rounds."""
        message = "The number of players must be superior to the number of rounds."
        print(message)

    def display_players_not_even(self) -> None:
        """Print a message when the number of players is not even."""
        message = "The number of players must be even for a tournament."
        print(message)

    def display_match_result_format(
        self,
        player_one: str,
        player_two: str,
        player_one_score: int,
        player_two_score: int,
    ) -> None:
        """Display a match with its results in a tournament report."""
        print(
            f"{player_one} : {player_one_score} - " f"{player_two_score} : {player_two}"
        )

    def display_players_by_id(self, id: int, player: object) -> None:
        """Display players by id for players selection at the beginning of a tournament.

        Args:
            id (int): Player id
            player (object): Player instance
        """
        print(f"{id} : {player.name} {player.surname}")

    def display_tournament_rounds(self, round: object) -> None:
        """Display a tournament's rounds.

        Args:
            round (object): Round instance
        """
        print(
            f"Name: {round.name}   Starting time: {round.start_time}   Ending time: {round.end_time}"
        )

    def display_next_matches(
        self, counter: int, first_player: str, second_player: str
    ) -> None:
        """Display a match to be played in the next round.

        Args:
            counter (int): Counter of match
            first_player (str): First player name surname
            second_player (str): Second player name surname
        """
        print(f"Match {counter} : {first_player}  -  {second_player}")

    def display_round_name(self, round: object) -> None:
        """Display a round's name when displaying matches in a tournament report.

        Args:
            round (object):
        """
        print(f"\n{round.name}")
