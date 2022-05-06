"""Tournament controller."""

from models.tournament import Tournament
from views.tournament import TournamentView
from models.round import Round
from models.match import Match
from models.player import Player
from os import system


class TournamentManager:
    """Class managing the tournament."""

    def __init__(self) -> None:
        """Initialize class."""
        self.tournament = Tournament()
        self.tournament_view = TournamentView()

    @staticmethod
    def dash(n):
        """Class decorator."""

        def decorate(fn):
            def wrapper(*args, **kwargs):
                print(n * "-")
                result = fn(*args, **kwargs)
                print(n * "-")
                return result

            return wrapper

        return decorate

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
        system("clear")

    def select_option(self, number_of_options: tuple, get_view_options):
        """Ask for the available options."""
        option = 0
        while option not in range(1, number_of_options + 1):
            try:
                option = int(input(get_view_options()))
            except ValueError:
                system("clear")
                self.tournament_view.get_wrong_option()
            else:
                if option not in range(1, number_of_options + 1):
                    system("clear")
                    self.tournament_view.get_wrong_option()
        return option

    def set_tournament_information(self, available_players) -> bool:
        """Get 8 players who will participate in the tournament."""
        if len(available_players) < self.tournament.number_of_players:
            self.tournament_view.get_wrong_player_number(
                self.tournament.number_of_players
            )
            return False
        else:
            self.get_tournament_information()
            return True

    def get_participating_players(self, available_players):
        """_summary_.

        Args:
            available_players (_type_): _description_
        """
        if len(available_players) < self.tournament.number_of_players:
            self.tournament_view.get_wrong_player_number(
                self.tournament.number_of_players
            )
        else:
            counter = 0
            selected_players = {}
            while counter < self.tournament.number_of_players:
                for id, player in available_players.items():
                    if id not in selected_players.keys():
                        print(f"{id} : {player.name} {player.surname}")
                try:
                    player_id = int(input(self.tournament_view.get_player()))
                except ValueError:
                    system("clear")
                    print(self.tournament_view.get_wrong_id())
                else:
                    if (
                        player_id not in selected_players.keys()
                        and player_id in available_players.keys()
                    ):
                        selected_players[player_id] = available_players[player_id]
                        counter += 1
                        system("clear")
                    else:
                        system("clear")
                        print(self.tournament_view.get_wrong_id())
            self.tournament.select_players(selected_players)

    def get_round_numbers(self) -> None:
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

    def get_player_numbers(self) -> None:
        """Ask for the tournament's number of rounds."""
        try:
            number_of_players = int(input(self.tournament_view.get_view_players()))
        except ValueError:
            self.tournament_view.get_wrong_option()
        else:
            self.tournament.set_number_of_players(number_of_players)

    def get_players_matches(self, matches) -> tuple:
        """Display all the matches that will occur during the round."""
        match_counter = 1
        for match in matches:
            first_player = match[0][1].name + " " + match[0][1].surname
            second_player = match[1][1].name + " " + match[1][1].surname
            print(f"Match {match_counter} : {first_player}  -  {second_player}")
            match_counter += 1

    def start_new_round(self) -> None:
        """Start a new round."""
        new_round = Round()
        new_round.set_starting_time()
        self.get_round_name(new_round)

        player_pairs = self.tournament.generate_pairs()
        self.get_players_matches(player_pairs)

        match_number = 0
        while match_number < len(player_pairs):
            first_player_id = player_pairs[match_number][0][0]
            first_player = (
                player_pairs[match_number][0][1].name
                + " "
                + player_pairs[match_number][0][1].surname
                + " : "
            )
            second_player_id = player_pairs[match_number][1][0]
            second_player = (
                player_pairs[match_number][1][1].name
                + " "
                + player_pairs[match_number][1][1].surname
                + " : "
            )
            results = self.start_new_match(match_number, first_player, second_player)
            match_result = Match(
                self.get_match_object_format(
                    first_player_id,
                    second_player_id,
                    results,
                )
            )
            self.get_new_total_scores(match_result)

            # print(self.tournament.players)
            # for v in self.tournament.players.values():
            # print(v.total_score)

            new_round.add_match(match_result)
            # print(match_result.players_score)
            match_number += 1

        new_round.set_ending_time()
        self.tournament.add_round(new_round)
        # print(new_round.match)
        # print(self.tournament.rounds)

    @dash(40)
    def start_new_match(self, match_number, first_player, second_player) -> None:
        """Start a new match."""
        match_number += 1
        self.tournament_view.get_view_match(match_number)
        first_player_result = self.get_result(first_player)
        second_player_result = self.get_result(second_player)
        return (first_player_result, second_player_result)

    def get_result(self, player):
        """Ask for the user's input for players' scores."""
        player_result = -1
        while player_result not in (0, 0.5, 1):
            try:
                player_result = float(input(player))
            except ValueError:
                self.tournament_view.get_wrong_score_type()
            else:
                if player_result not in (0, 0.5, 1):
                    self.tournament_view.get_wrong_score_type()
        return player_result

    def get_match_object_format(self, first_player_id, second_player_id, result: tuple):
        """Put the results in a tuple containing two lists [player, score]."""
        match = ([first_player_id, result[0]], [second_player_id, result[1]])
        return match

    def get_new_total_scores(self, match: object) -> None:
        """_summary_."""
        self.tournament.players[match.players_score[0][0]].update_score(
            match.players_score[0][1]
        )
        self.tournament.players[match.players_score[1][0]].update_score(
            match.players_score[1][1]
        )

    def update_ranking(self):
        """Update the general ranking based on ranks."""
        sorted_players = self.tournament.sort_by_score_dict()
        rank_counter = 1
        for player in sorted_players.values():
            player.update_rank(rank_counter)
            rank_counter += 1

    def display_by_rank(self):
        """Display the players by rank."""
        sorted_players = self.tournament.sort_by_score_dict()
        for player in sorted_players.values():
            self.tournament_view.show_ranking(player)

    def start_tournament(self, application):
        """Start tournament."""
        round_running = True
        while (
            len(self.tournament.rounds) < self.tournament.number_of_rounds
            and round_running
        ):
            round_option = self.select_option(
                3,
                self.tournament_view.get_round_options,
            )
            if round_option == 1:
                system("clear")
                self.start_new_round()
                self.update_db(application)
                self.update_ranking()

            elif round_option == 2:
                system("clear")
                self.display_by_rank()
            elif round_option == 3:
                return False

        self.tournament_view.display_message_end_tournament()
        self.display_by_rank()
        return True

    def start_tournament_info(self, application: object):

        tournament_running = True
        players = application.user_manager.get_all_players(application.db_player)

        # If there is already a time_control defined, tournament's information has already been set.
        if self.tournament.time_control == "":
            enough_players = self.set_tournament_information(players)
            application.db_tournament.add_tournament_db(self.tournament)
            if not enough_players:
                tournament_running = False

        while tournament_running:

            if len(self.tournament.players) != 0:
                tournament_option = 1
            else:
                tournament_option = self.select_option(
                    4,
                    self.tournament_view.get_tournament_options,
                )
            if tournament_option == 1:
                if len(self.tournament.players) == 0:
                    self.get_participating_players(players)
                    self.update_db(application)
                else:
                    end_tournament = self.start_tournament(application)
                    tournament_running = False
                    if not end_tournament:
                        running = False

            elif tournament_option == 2:
                system("clear")
                self.get_round_numbers()
                self.update_db(application)
            elif tournament_option == 3:
                system("clear")
                self.get_player_numbers()
                self.update_db(application)
            elif tournament_option == 4:
                tournament_running = False
                running = False

    def get_tournament_db_id(self, application, tournament_description) -> None:
        """Method used to modify the elo rank of a player.
        if the player exists in the database, else return an error."""
        tournament_id = application.db_tournament.search_tournament_id_by_description(
            tournament_description
        )
        return tournament_id

    def update_tournament(self, application, tournament, tournament_id) -> None:
        """Method used to modify the elo rank of a player.
        if the player exists in the database, else return an error."""
        application.db_tournament.update_tournament_db(tournament, tournament_id)

    def update_db(self, application):
        tournament_id = self.get_tournament_db_id(
            application, self.tournament.description
        )

        players_serialized = {}
        if len(self.tournament.players) > 0:
            for id, player in self.tournament.players.items():
                serialized_player = Player.serialize_player_tournament(player)
                players_serialized[id] = serialized_player

        rounds_serialized = []
        if len(self.tournament.rounds) > 0:
            for round in self.tournament.rounds:
                new_round = Round()
                new_round.name = round.name
                new_round.start_time = round.start_time
                new_round.end_time = round.end_time

                for match in round.match:
                    serialized_match = Match.serialize_match(match)

                    new_round.match.append(serialized_match)

                serialized_round = Round.serialize_round(new_round)
                rounds_serialized.append(serialized_round)

        tournament_to_serialize = Tournament()
        tournament_to_serialize.name = self.tournament.name
        tournament_to_serialize.place = self.tournament.place
        tournament_to_serialize.date = self.tournament.date
        tournament_to_serialize.number_of_rounds = self.tournament.number_of_rounds
        tournament_to_serialize.number_of_players = self.tournament.number_of_players
        tournament_to_serialize.rounds = rounds_serialized
        tournament_to_serialize.players = players_serialized
        tournament_to_serialize.time_control = self.tournament.time_control
        tournament_to_serialize.description = self.tournament.description

        self.update_tournament(application, tournament_to_serialize, tournament_id)
