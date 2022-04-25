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
        name = input(self.tournament_view.get_view_name()).capitalize()
        self.tournament.set_name(name)

    def get_tournament_place(self) -> None:
        """Ask for the tournament's place."""
        while not self.tournament.place:
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

    def get_tournament_players(self) -> None:
        """Get 8 players who will participate in the tournament."""
        if len(self.available_players) < 8:
            print(self.tournament_view.get_wrong_player_number())
        else:
            count = 0
            selected_players = {}
            while count < 8:
                for id, player in self.available_players.items():
                    if id not in selected_players.keys():
                        print(f"{id} : {player.name} {player.surname}")
                player_id = int(input(self.tournament_view.get_player()))
                if (
                    player_id not in selected_players.keys()
                    and player_id in self.available_players.keys()
                ):
                    selected_players[player_id] = self.available_players[player_id]
                    count += 1
                else:
                    print(self.tournament_view.get_wrong_id())
            self.tournament.select_players(selected_players)
