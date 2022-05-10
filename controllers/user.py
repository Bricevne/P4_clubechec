"""User manager class."""

from controllers.tournament import TournamentManager
from controllers.menu import MenuManager
from controllers.db import DbPlayer, DbTournament

from models.tournament import Tournament
from models.player import Player
from models.match import Match
from models.round import Round

from views.user import UserView


from os import system
import re
from typing import Callable


class UserManager:
    """Class managing user options outside of a tournament."""

    def __init__(self) -> None:
        """Class initializer."""
        self.user_view = UserView()
        self.menu_manager = MenuManager()
        self.tournament_manager = TournamentManager()
        self.db_player = DbPlayer()
        self.db_tournament = DbTournament()

    def get_good_elo(self) -> int:
        """Ask for the player's elo and check if it is an integer.

        Returns:
            int: Player's elo
        """
        elo = 0
        while elo == 0:
            try:
                elo = int(input(self.user_view.get_elo()))
            except ValueError:
                self.user_view.get_wrong_elo()
            else:
                return elo

    def get_good_gender(self) -> str:
        """Ask for the player's gender and check if it is M (male) or F (female).

        Returns:
            str: M or F
        """
        gender = ""
        while gender not in ("M", "F"):
            gender = input(self.user_view.get_gender()).capitalize()
            if gender not in ("M", "F"):
                self.user_view.get_wrong_gender()
            else:
                return gender

    def get_good_birthdate(self) -> str:
        """
        Ask for the player's birthdate and check if a birthdate is in the format YYYY-MM-DD.

        YYYY between 0000 and 9999.
        MM between 01 and 12.
        DD between 01 and 31.
        Does not check unvalid dates such as 2000-02-30.

        Returns:
            str: Player's birthdate
        """
        regex = r"(^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$)"
        not_right = True
        while not_right:
            birthdate = input(self.user_view.get_birthdate())
            if re.search(regex, birthdate):
                not_right = False
                return birthdate
            else:
                self.user_view.get_wrong_birthdate()

    def get_user_confirmation(
        self,
        confirmed_option: tuple,
        unconfirmed_option: tuple,
        get_view_options: Callable,
    ) -> bool:
        """Ask the user for confirmation.

        Args:
            confirmed_option (tuple): Options for confirmation
            unconfirmed_option (tuple): options for refusal
            get_view_options (Callable): Function called when user choice is wrong

        Returns:
            bool: True when confirmed, False otherwise
        """
        option = ""
        while option not in confirmed_option and option not in unconfirmed_option:
            option = input(get_view_options())
            if option not in confirmed_option and option not in unconfirmed_option:
                self.user_view.get_wrong_option()
        if option in confirmed_option:
            return True
        else:
            return False

    def create_player(self) -> object or None:
        """Create a player instance.

        Returns:
            object or None: Player instance if the user confirms, None otherwise
        """
        name = input(self.user_view.get_name()).capitalize()
        surname = input(self.user_view.get_surname()).capitalize()
        birthdate = self.get_good_birthdate()
        gender = self.get_good_gender()
        elo = self.get_good_elo()
        confirmation = self.get_user_confirmation(
            ("y", "Y"), ("n", "N"), self.user_view.get_confirmation
        )
        system("clear")
        if confirmation:
            player = Player(name, surname, birthdate, gender, elo)
            self.user_view.display_player_confirmation()
            return player

    def display_players_by_elo(self) -> None:
        """Display all players in the database by increasing elo.

        Args:
            db_player (object): Player database instance
        """
        players = self.db_player.sort_players_by_elo()
        for player in players:
            self.user_view.display_sorted_players(player)

    def display_players_by_surname(self) -> None:
        """Display all players in the database by surname.

        Args:
            db_player (object): Player database instance
        """
        players = self.db_player.sort_players_by_surname()
        for player in players:
            self.user_view.display_sorted_players(player)

    def display_players(self) -> None:
        """Dispatch the action requested by the user.

        Args:
            player_db (object): Player database instance
        """
        system("clear")

        user_choice = 0
        menu_running = True

        while menu_running:
            user_choice = self.menu_manager.select_menu_option(
                4, self.menu_manager.menu_view.get_player_submenu
            )

            if user_choice == 1:
                self.update_players_elo()
            elif user_choice == 2:
                system("clear")
                self.display_players_by_surname()
            elif user_choice == 3:
                system("clear")
                self.display_players_by_elo()
            elif user_choice == 4:
                system("clear")
                menu_running = False

    def update_players_elo(self) -> None:
        """Update a player's elo by picking his id.

        Unserialize a player dictionnary in the database to modify its elo.
        Display a successful or unsuccessful change.
        """
        try:
            player_id = int(input(self.user_view.get_player_by_id()))
        except ValueError:
            system("clear")
            self.user_view.display_wrong_id_type()
        else:
            player_found = self.db_player.search_player_by_id(player_id)
            if player_found:
                player = Player(
                    player_found["name"],
                    player_found["surname"],
                    player_found["birthdate"],
                    player_found["gender"],
                    player_found["elo"],
                )

                elo = int(input(self.user_view.get_new_elo()))
                player.elo = elo
                self.db_player.update_player(player, player_id)
                system("clear")
                self.user_view.display_successful_change()
            else:
                system("clear")
                self.user_view.display_unsuccessful_change()

    def get_all_players(self, player_db: object) -> dict:
        """Return all players in the database.

        Args:
            player_db (object): Player database instance

        Returns:
            dict: Dictionnary {id : player instance}
        """
        available_players = {}
        for player_found in player_db.players:
            player = Player(
                player_found["name"],
                player_found["surname"],
                player_found["birthdate"],
                player_found["gender"],
                player_found["elo"],
            )
            available_players[player_found.doc_id] = player
        return available_players

    def import_tournament(
        self, tournament_db: object, get_menu: Callable
    ) -> dict or None:
        """Dispatch the action selected by the user (recover a tournament, or go back to previous menu).

        Args:
            tournament_db (object): Tournament database instance
            get_menu (Callable): Function displaying menu

        Returns:
            Dict or None: Dictionnary if the user import a tournament, none otherwise
        """
        user_choice = 0
        menu_running = True

        while menu_running:
            for tournament in tournament_db.tournaments:
                self.user_view.display_tournaments(tournament)

            user_choice = self.menu_manager.select_menu_option(2, get_menu)

            if user_choice == 1:
                tournament = self.recover_tournament(tournament_db)
                return tournament
            elif user_choice == 2:
                system("clear")
                menu_running = False

    def recover_tournament(self, db_tournament: object) -> dict or None:
        """Recover a tournament from the database by unserializing it.

        Args:
            db_tournament (object): Tournament database instance

        Returns:
            Dict or None: Dictionnary of a tournament, none otherwise
        """
        try:
            tournament_id = int(input(self.user_view.get_tournament_by_id()))
        except ValueError:
            self.user_view.display_wrong_id_type()
        else:
            tournament_found = db_tournament.search_tournament_by_id(tournament_id)
            return self.unserialize_tournament(tournament_found)

    def unserialize_tournament(self, tournament_found: dict) -> object or None:
        """Unserialize a tournament in the database.

        Args:
            tournament_found (dict): A tournament

        Returns:
            object or None: A tournament instance if a tournament is found, none otherwise
        """
        if tournament_found:
            tournament = Tournament()
            tournament.name = tournament_found["name"]
            tournament.place = tournament_found["place"]
            tournament.date = tournament_found["date"]
            tournament.description = tournament_found["description"]
            tournament.time_control = tournament_found["time_control"]
            tournament.number_of_players = tournament_found["number_of_players"]
            tournament.number_of_rounds = tournament_found["number_of_rounds"]

            tournament_players = {}
            if len(tournament_found["players"]) > 0:
                for id, player_found in tournament_found["players"].items():
                    player = Player(
                        player_found["name"],
                        player_found["surname"],
                        player_found["birthdate"],
                        player_found["gender"],
                        player_found["elo"],
                    )
                    player.total_score = player_found["total_score"]
                    player.rank = player_found["rank"]
                    tournament_players[id] = player

            tournament.players = tournament_players

            tournament_rounds = []
            if len(tournament_found["rounds"]) > 0:

                for rounds_found in tournament_found["rounds"]:
                    round = Round()
                    round.name = rounds_found["name"]
                    round.start_time = rounds_found["start_time"]
                    round.end_time = rounds_found["end_time"]

                    for match_found in rounds_found["match"]:
                        match = Match(match_found["players_score"])

                        round.match.append(match)

                    tournament_rounds.append(round)
                tournament.rounds = tournament_rounds
            return tournament
        else:
            print("Tournament does not exist.")

    def display_tournament_information(self, get_menu: Callable) -> None:
        """
        Dispatch the action selected by the user.

        Options: isplay list of rounds, display list of matches, go back to previous menu.

        Args:
            get_menu (Callable): Function displaying menu
        """
        user_choice = 0
        menu_running = True

        while menu_running:
            user_choice = self.menu_manager.select_menu_option(5, get_menu)

            if user_choice == 1:
                self.tournament_manager.display_by_rank()
            if user_choice == 2:
                self.tournament_manager.display_by_surname()
            elif user_choice == 3:
                self.tournament_manager.display_rounds()
            elif user_choice == 4:
                self.tournament_manager.display_matches()
            elif user_choice == 5:
                system("clear")
                menu_running = False

    def add_player(self) -> None:
        """Create a new player instance and add it to the database."""
        system("clear")
        added_player = self.create_player()
        if added_player is not None:
            self.db_player.add_player_db(added_player)

    def start_imported_tournament(self):
        """Import a tournament, create a new tournament instance from those information and continue the tournament."""
        imported_tournament = self.import_tournament(
            self.db_tournament, self.menu_manager.menu_view.get_import_menu
        )
        if imported_tournament:
            self.tournament_manager.tournament = imported_tournament
            self.tournament_manager.create_tournament(
                self.db_player, self.db_tournament
            )

    def display_imported_tournament(self):
        """Import a tournament, create a new tournament instance and display its information."""
        found_tournament = self.import_tournament(
            self.db_tournament, self.menu_manager.menu_view.get_import_menu
        )
        if found_tournament:
            self.tournament_manager.tournament = found_tournament
            self.display_tournament_information(
                self.menu_manager.menu_view.get_tournament_information_menu,
            )

    def start_program(self) -> None:
        """Start program.

        Args:
            application (object): Application controller instance
        """
        system("clear")

        self.user_view.display_welcome()

        running = True
        while running:
            self.tournament_manager.tournament = Tournament()
            user_choice = self.menu_manager.select_menu_option(
                6, self.menu_manager.menu_view.get_menu
            )
            if user_choice == 1:
                self.tournament_manager.create_tournament(
                    self.db_player, self.db_tournament
                )
            elif user_choice == 2:
                self.add_player()
            elif user_choice == 3:
                self.display_players()
            elif user_choice == 4:
                self.start_imported_tournament()
            elif user_choice == 5:
                self.display_imported_tournament()
            elif user_choice == 6:
                running = False
