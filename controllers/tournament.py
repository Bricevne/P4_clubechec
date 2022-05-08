"""Tournament controller."""

from models.tournament import Tournament
from views.tournament import TournamentView
from models.round import Round
from models.match import Match
from models.player import Player
from typing import Callable

# from controllers.menu import MenuManager
from os import system


class TournamentManager:
    """Class managing the tournament."""

    def __init__(self) -> None:
        """Initialize class."""
        self.tournament = Tournament()
        self.tournament_view = TournamentView()
        # self.menu_view = MenuManager()

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
        """Get all the tournament's information."""
        self.get_tournament_name()
        self.get_tournament_place()
        self.get_tournament_date()
        self.get_tournament_time_control()
        self.get_tournament_description()
        system("clear")

    def select_option(self, number_of_options: int, get_view_options: Callable) -> int:
        """Ask the user to pick from the available options.

        Args:
            number_of_options (int): Number of options available to pick from
            get_view_options (Callable): Method from the tournament view to display options

        Returns:
            int: Option picked
        """
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

    def set_tournament_information(self, available_players: dict) -> bool:
        """Check if there are enough players for the current tournament (Default: 8).

        Ask for the tournament's information if players are enough.

        Args:
            available_players (dict): Dictionnary of players from the database {id: player object}

        Returns:
            bool: False when not enough player in the database, True otherwise
        """
        if len(available_players) < self.tournament.number_of_players:
            self.tournament_view.get_wrong_player_number(
                self.tournament.number_of_players
            )
            return False
        else:
            self.get_tournament_information()
            return True

    def get_participating_players(self, available_players: dict) -> None:
        """Get the participants in a tournament instance if enough players are in the database.

        Args:
            available_players (dict): Dictionnary of available players in the database
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
        """Get the tournament's number of rounds."""
        try:
            number_of_rounds = int(input(self.tournament_view.get_view_round()))
        except ValueError:
            self.tournament_view.get_wrong_option()
        else:
            self.tournament.set_round(number_of_rounds)

    def get_round_name(self, round_object: object) -> None:
        """Get the new round's name.

        Args:
            round_object (object): Round instance
        """
        name = input(self.tournament_view.get_view_round_name())
        round_object.set_round_name(name)

    def get_player_numbers(self) -> None:
        """Get the tournament's number of players."""
        try:
            number_of_players = int(input(self.tournament_view.get_view_players()))
        except ValueError:
            self.tournament_view.get_wrong_option()
        else:
            self.tournament.set_number_of_players(number_of_players)

    def get_players_matches(self, matches: list[tuple]) -> None:
        """Display all the matches that will occur during the round.

        Args:
            matches (list[tuple]): A list containing tuples with 2 player instances each
        """
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

        match_counter = 0
        while match_counter < len(player_pairs):
            first_player_id = player_pairs[match_counter][0][0]
            first_player = (
                player_pairs[match_counter][0][1].name
                + " "
                + player_pairs[match_counter][0][1].surname
                + " : "
            )
            second_player_id = player_pairs[match_counter][1][0]
            second_player = (
                player_pairs[match_counter][1][1].name
                + " "
                + player_pairs[match_counter][1][1].surname
                + " : "
            )
            results = self.start_new_match(match_counter, first_player, second_player)
            match_result = Match(
                self.get_match_object_format(
                    first_player_id,
                    second_player_id,
                    results,
                )
            )
            self.update_new_total_scores(match_result)

            new_round.add_match(match_result)
            match_counter += 1

        new_round.set_ending_time()
        self.tournament.add_round(new_round)

    @dash(40)
    def start_new_match(
        self, match_counter: int, first_player: str, second_player: str
    ) -> tuple[float]:
        """Start a new match and ask the user the matches' scores.

        Args:
            match_counter (int): Counter for matches
            first_player (str): String to display the first player's name and surname
            second_player (str): String to display the second player's name and surname

        Returns:
            tuple[float]: A tuple of float scores
        """
        match_counter += 1
        self.tournament_view.get_view_match(match_counter)
        first_player_result = self.get_result(first_player)
        second_player_result = self.get_result(second_player)
        return (first_player_result, second_player_result)

    def get_result(self, player: str) -> float:
        """Ask for the user's input for players' scores.

        0.0 for a loss, 0.5 for a draw and 1.0 for a win.

        Args:
            player (str): String to display a player's name and surname

        Returns:
            float: A player's score
        """
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

    def get_match_object_format(
        self, first_player_id: int, second_player_id: int, result: tuple
    ) -> tuple[list]:
        """Put the results in a match format (tuple).

        Args:
            first_player_id (int): First player id
            second_player_id (int): Second player id
            result (tuple): Results of both player's scores

        Returns:
            tuple[list]: Tuple containing two lists [player id, score]
        """
        match = ([first_player_id, result[0]], [second_player_id, result[1]])
        return match

    def update_new_total_scores(self, match: object) -> None:
        """Update players' total scores in the tournament instance.

        Args:
            match (object): Match instance
        """
        self.tournament.players[match.players_score[0][0]].update_score(
            match.players_score[0][1]
        )
        self.tournament.players[match.players_score[1][0]].update_score(
            match.players_score[1][1]
        )

    def update_ranking(self) -> None:
        """Update the general ranking based on scores."""
        sorted_players = self.tournament.sort_by_score_dict()
        rank_counter = 1
        for player in sorted_players.values():
            player.update_rank(rank_counter)
            rank_counter += 1

    def display_by_rank(self) -> None:
        """Display the players by rank."""
        self.update_ranking()
        sorted_players = self.tournament.sort_by_score_dict()
        for player in sorted_players.values():
            self.tournament_view.show_ranking(player)

    def start_tournament(self, application: object) -> bool:
        """Start tournament.

        Args:
            application (object): Controller Application instance

        Returns:
            bool: True if the tournament is over, False if stopped before the end
        """
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
                self.update_ranking()
                self.display_by_rank()
            elif round_option == 3:
                return False

        self.tournament_view.display_message_end_tournament()
        self.display_by_rank()
        return True

    def create_tournament(self, application: object) -> None:
        """Create a new tournament.

        Args:
            application (object): Controller application instance
        """
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
                    self.start_tournament(application)
                    tournament_running = False

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

    def get_tournament_db_id(
        self, application: object, tournament_description: str
    ) -> int or bool:
        """Recover the tournament's id thanks to its description in the database.

                Args:
            application (object): Controller application instance
            tournament_description (str): Tounrnament's description

        Returns:
            int or bool: Tournament id if found, False if not
        """
        tournament_id = application.db_tournament.search_tournament_id_by_description(
            tournament_description
        )
        return tournament_id

    def update_tournament(
        self, application: object, tournament: object, tournament_id: int
    ) -> None:
        """Update an existing tournament in the database.

        Args:
            application (object): Controller application instance
            tournament (object): Tournament instance
            tournament_id (int): Tournament id
        """
        application.db_tournament.update_tournament_db(tournament, tournament_id)

    def update_db(self, application: object) -> None:
        """Serialize players, rounds and matches in a new tournament instance, and update it in the database.

        Args:
            application (object): Controller application instance
        """
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
