"""Tournament view."""


class TournamentView:
    """Class managing tournament displays."""

    def __init__(self) -> None:
        """Class initializer."""
        pass

    def get_view_name(self) -> str:
        """Display name input."""
        return "Name: "

    def get_view_place(self) -> str:
        """Display place input."""
        return "Place: "

    def get_view_date(self) -> str:
        """Display date input."""
        return "Date: "

    def get_view_time_control(self) -> str:
        """Display time control input."""
        return "Time_control: "

    def get_view_description(self) -> str:
        """Display description input."""
        return "Description: "

    def get_view_round(self) -> str:
        """Display round input."""
        return "Number of rounds: "

    def get_view_players(self) -> str:
        """Display number of players input."""
        return "Number of players: "

    def get_wrong_player_number(self, number_of_players) -> None:
        """Display a message when not enough players are available for the tournament."""
        print(
            f"You need at least {number_of_players} players to choose from for a tournament."
        )

    def get_player(self) -> str:
        """Display a message for selecting a player."""
        return "Please select a player's id to add him to the tournament : "

    def get_wrong_id(self) -> str:
        """Display a message when a player is already selected or does not exist."""
        return "Please choose a valid id from the list. "

    def get_tournament_options(self) -> str:
        """Display tournament menu."""
        menu_options = "\n\
        1. Start tournament\n\
        2. Modify round numbers\n\
        3. Modify number of players\n\
        4. Save data\n\
        5. Quit\n"
        return menu_options

    def get_round_options(self) -> str:
        """Display round menu."""
        menu_options = "\n\
        1. New round\n\
        2. Show ranking\n\
        3. Save data\n\
        4. Quit\n"
        return menu_options

    def get_wrong_option(self) -> None:
        """Display error message."""
        error_message = "Oops! That was no valid option. Try again."
        print(error_message)

    def get_wrong_round_number(self) -> None:
        """Display error message."""
        error_message = "Oops! This is not a number!"
        print(error_message)

    def get_view_round_name(self) -> str:
        """Display round name."""
        return "Round name: "

    def get_view_match(self, match_counter: int) -> None:
        """Display match result."""
        message = f"Match {match_counter} | results\n"
        print(message)

    def get_wrong_score_type(self) -> None:
        """Display."""
        message = "You have to give a score (Lose : 0, Win : 1, Draw : 0.5)"
        print(message)

    def show_ranking(self, player):
        """Display the message format for rankings."""
        message = f"{player.rank} : {player.name} {player.surname} - Total score : {player.total_score}"
        print(message)

    def display_message_end_tournament(self) -> None:
        """Diaplsy."""
        message = "The tournament ends ! The final ranking is: "
        print(message)
