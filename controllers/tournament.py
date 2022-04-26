"""Tournament controller."""

from models.tournament import Tournament
from views.tournament import TournamentView
from models.round import Round
from random import randint


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

    def select_tournament_option(self) -> int:
        """Ask for User choice."""
        menu_option = 0
        while menu_option not in (1, 2, 3, 4, 5):
            try:
                menu_option = int(input(self.tournament_view.get_tournament_options()))
            except ValueError:
                self.tournament_view.get_wrong_option()
            else:
                if menu_option not in (1, 2, 3, 4, 5):
                    self.tournament_view.get_wrong_option()
        return menu_option

    def select_round_option(self) -> int:
        """Ask for User choice."""
        menu_option = 0
        while menu_option not in (1, 2, 3, 4):
            try:
                menu_option = int(input(self.tournament_view.get_round_options()))
            except ValueError:
                self.tournament_view.get_wrong_option()
            else:
                if menu_option not in (1, 2, 3, 4):
                    self.tournament_view.get_wrong_option()
        return menu_option

    def select_match_option(self) -> int:
        """Ask for User choice."""
        menu_option = 0
        while menu_option not in (1, 2, 3, 4):
            try:
                menu_option = int(input(self.tournament_view.get_match_options()))
            except ValueError:
                self.tournament_view.get_wrong_option()
            else:
                if menu_option not in (1, 2, 3, 4):
                    self.tournament_view.get_wrong_option()
        return menu_option

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

    def get_players_round_list(self, matchs) -> tuple:
        """Get players names and surnames for displays."""
        first_player = matchs[0][0][1].name + " " + matchs[0][0][1].surname
        second_player = matchs[0][1][1].name + " " + matchs[0][1][1].surname
        third_player = matchs[1][0][1].name + " " + matchs[1][0][1].surname
        fourth_player = matchs[1][1][1].name + " " + matchs[1][1][1].surname
        fifth_player = matchs[2][0][1].name + " " + matchs[2][0][1].surname
        sixth_player = matchs[2][1][1].name + " " + matchs[2][1][1].surname
        seventh_player = matchs[3][0][1].name + " " + matchs[3][0][1].surname
        eighth_player = matchs[3][1][1].name + " " + matchs[3][1][1].surname
        return (
            first_player,
            second_player,
            third_player,
            fourth_player,
            fifth_player,
            sixth_player,
            seventh_player,
            eighth_player,
        )

    def get_matchs_list(self, players):
        """Get matchs displays."""
        return self.tournament_view.display_following_matchs(
            self.get_players_round_list(players)
        )

    def start_new_round(self) -> None:
        """Start a new round."""
        new_round = Round()
        new_round.set_starting_time()
        self.get_round_name(new_round)

        player_pairs = self.tournament.generate_pairs()
        self.get_matchs_list(player_pairs)

    def end_round(self, round: object) -> None:
        """End a round by setting the ending time."""
        round.set_ending_time()

    def start_new_match(self) -> None:
        """Start a new round."""
