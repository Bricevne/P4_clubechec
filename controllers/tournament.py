"""Tournament controller."""

from models.tournament import Tournament
from views.tournament import TournamentView


class TournamentManager:
    """Class managing the tournament."""

    def __init__(self, available_players: dict) -> None:
        """Initialize class."""
        self.tournament = Tournament()
        self.tournament_view = TournamentView()
        self.get_tournament_information()
        self.available_players = available_players

    def get_tournament_name(self) -> None:
        """Ask for the tournament's name."""
        while not self.tournament.name:
            name = input(self.tournament_view.get_view_name()).capitalize()
            self.tournament.set_name(name)

    def get_tournament_place(self) -> None:
        """Ask for the tournament's place."""
        place = input(self.tournament_view.get_view_place()).capitalize()
        self.tournament.set_place(place)

    def get_tournament_date(self) -> None:
        """Ask for the tournament's date."""
        date = input(self.tournament_view.get_view_date())
        self.tournament.set_date(date)

    def get_tournament_time_control(self) -> None:
        """Ask for the tournament's time control type."""
        while not self.tournament.time_control:
            time_control = input(
                self.tournament_view.get_view_time_control()
            ).capitalize()
            self.tournament.set_time_control(time_control)

    def get_tournament_description(self) -> None:
        """Ask for the tournament's description."""
        description = input(self.tournament_view.get_view_description()).capitalize()
        self.tournament.set_description(description)

    def get_tournament_information(self) -> None:
        """Ask for the tournament's information."""
        self.get_tournament_name()
        self.get_tournament_place()
        self.get_tournament_date()
        self.get_tournament_time_control()
        self.get_tournament_description()
