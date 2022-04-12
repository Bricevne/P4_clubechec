"""Tournament controller."""

from models.tournament import Tournament
from views.tournament import TournamentView


class TournamentManager:
    """Class managing the tournament."""

    def __init__(self) -> None:
        """Initialize class."""
        self.tournament = Tournament()
        self.tournament_view = TournamentView()
        self.get_tournament_information()

    def get_tournament_name(self):
        """Ask for the tournament's name."""
        while not self.tournament.name:
            name = input(self.tournament_view.get_view_name()).capitalize()
            self.tournament.get_name(name)

    def get_tournament_place(self):
        """Ask for the tournament's place."""
        place = input(self.tournament_view.get_view_place()).capitalize()
        self.tournament.get_place(place)

    def get_tournament_date(self):
        """Ask for the tournament's date."""
        date = input(self.tournament_view.get_view_date())
        self.tournament.get_date(date)

    def get_tournament_time_control(self):
        """Ask for the tournament's time control type."""
        while not self.tournament.time_control:
            time_control = input(
                self.tournament_view.get_view_time_control()
            ).capitalize()
            self.tournament.get_time_control(time_control)

    def get_tournament_description(self):
        """Ask for the tournament's description."""
        description = input(self.tournament_view.get_view_description()).capitalize()
        self.tournament.get_description(description)

    def get_tournament_information(self):
        """Ask for the tournament's information."""
        self.get_tournament_name()
        self.get_tournament_place()
        self.get_tournament_date()
        self.get_tournament_time_control()
        self.get_tournament_description()
