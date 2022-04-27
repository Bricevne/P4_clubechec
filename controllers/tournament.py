"""Tournament controller."""

from models.tournament import Tournament
from views.tournament import TournamentView
from models.round import Round


class TournamentManager:
    """Class managing the tournament."""

    def __init__(self, available_players: dict) -> None:
        """Initialize class."""
        self.tournament = Tournament()
        self.tournament_view = TournamentView()
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

    def select_option(self, number_of_options: tuple, get_view_options):
        """Ask for the available options."""
        option = 0
        while option not in number_of_options:
            try:
                option = int(input(get_view_options()))
            except ValueError:
                self.tournament_view.get_wrong_option()
            else:
                if option not in number_of_options:
                    self.tournament_view.get_wrong_option()
        return option

    def get_tournament_players(self) -> bool:
        """Get 8 players who will participate in the tournament."""
        if len(self.available_players) < 8:
            self.tournament_view.get_wrong_player_number()
            return False
        else:
            self.get_tournament_information()
            counter = 0
            selected_players = {}
            while counter < 8:
                for id, player in self.available_players.items():
                    if id not in selected_players.keys():
                        print(f"{id} : {player.name} {player.surname}")
                player_id = int(input(self.tournament_view.get_player()))
                if (
                    player_id not in selected_players.keys()
                    and player_id in self.available_players.keys()
                ):
                    selected_players[player_id] = self.available_players[player_id]
                    counter += 1
                else:
                    print(self.tournament_view.get_wrong_id())
            self.tournament.select_players(selected_players)
            return True

    def get_round(self) -> None:
        """Ask for the tournament's number of rounds."""
        try:
            number_of_rounds = int(input(self.tournament_view.get_view_round()))
        except ValueError:
            self.tournament_view.get_wrong_option()
        else:
            self.tournament.set_round(number_of_rounds)

    def get_round_name(self, round_object) -> None:
        """Ask for the new round's name.

        Args:
            round_object (object): object from the round's model
        """
        name = input(self.tournament_view.get_view_round_name())
        round_object.set_round_name(name)

    def get_players_round_list(self, matches) -> tuple:
        """Display round matches."""
        match_counter = 1
        for match in matches:
            first_player = match[0].name + " " + match[0].surname
            second_player = match[1].name + " " + match[1].surname
            print(f"Match {match_counter} : {first_player}  -  {second_player}")
            match_counter += 1

    def start_new_round(self) -> None:
        """Start a new round."""
        new_round = Round()
        new_round.set_starting_time()
        self.get_round_name(new_round)

        player_pairs = self.tournament.generate_pairs()
        self.get_players_round_list(player_pairs)

        new_round.set_ending_time()
        return new_round

    def start_new_match(self) -> None:
        """Start a new round."""
