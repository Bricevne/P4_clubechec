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

    def get_wrong_player_number(self) -> str:
        """Display a message when not enough players are available for the tournament."""
        return "You need at least 8 players to choose from for a tournament."

    def get_player(self) -> str:
        """Display a message for selecting a player."""
        return "Please select a player's id to add him to the tournament : "

    def get_wrong_id(self) -> str:
        """Display a message when a player is already selected or does not exist."""
        return "Please choose a valid id from the list. "

    def get_tournament_options(self) -> str:
        """Display tournament menu."""
        menu_options = "\n\
        1. Select players\n\
        2. Modify round numbers\n\
        3. Start tournament\n\
        4. Save data\n\
        5. Back\n"
        return menu_options

    def get_wrong_option(self) -> None:
        """Display error message."""
        error_message = "Oops! That was no valid option. Try again."
        print(error_message)

    def get_wrong_round_number(self) -> None:
        """Display error message."""
        error_message = "Oops! This is not a number!"
        print(error_message)
