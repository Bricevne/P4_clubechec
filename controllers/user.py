"""User manager class."""

from models.player import Player
from views.user import UserView
from models.match import Match
from models.round import Round

from os import system
import re
from models.tournament import Tournament


class UserManager:
    """Class managing."""

    def __init__(self) -> None:
        """Init."""
        self.display = UserView()

    def get_good_elo(self) -> None:
        """Ask for the tournament's number of rounds."""
        elo = 0
        while elo == 0:
            try:
                elo = int(input(self.display.get_elo()))
            except ValueError:
                self.display.get_wrong_elo()
            else:
                return elo

    def get_good_gender(self) -> None:
        """Ask for the tournament's number of rounds."""
        gender = ""
        while gender not in ("M", "F"):
            gender = input(self.display.get_gender()).capitalize()
            if gender not in ("M", "F"):
                self.display.get_wrong_gender()
            else:
                return gender

    def get_good_birthdate(self):
        """
        Check if a birthdate is in the format YYYY-MM-DD.

        YYYY between 0000 and 9999.
        MM between 01 and 12.
        DD between 01 and 31.
        Does not check unvalid dates such as 2000-02-30.
        """
        regex = r"(^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$)"
        not_right = True
        while not_right:
            birthdate = input(self.display.get_birthdate())
            if re.search(regex, birthdate):
                not_right = False
                return birthdate
            else:
                self.display.get_wrong_birthdate()

    def add_player(self) -> object:
        """Add a player."""
        system("clear")
        name = input(self.display.get_name()).capitalize()
        surname = input(self.display.get_surname()).capitalize()
        birthdate = self.get_good_birthdate()
        gender = self.get_good_gender()
        elo = self.get_good_elo()
        confirmation = self.get_user_confirmation(
            ("y", "Y"), ("n", "N"), self.display.get_confirmation
        )
        system("clear")
        if confirmation:
            player = Player(name, surname, birthdate, gender, elo)
            self.display.display_player_confirmation()
            return player
        pass

    def get_user_confirmation(
        self, confirmed_option: tuple, unconfirmed_option: tuple, get_view_options
    ):
        """Ask for the available options."""
        option = ""
        while option not in confirmed_option and option not in unconfirmed_option:
            option = input(get_view_options())
            if option not in confirmed_option and option not in unconfirmed_option:
                self.display.get_wrong_option()
        if option in confirmed_option:
            return True
        else:
            return False

    def display_players_by_elo(self, db_player: object):
        players = db_player.sort_players_by_elo()
        for player in players:
            self.display.display_sorted_players(player)

    def display_players_by_surname(self, db_player: object):
        players = db_player.sort_players_by_surname()
        for player in players:
            self.display.display_sorted_players(player)

    def select_menu_option(self, number_of_options, get_menu) -> int:
        """Ask for User choice."""
        menu_option = 0
        while menu_option not in range(1, number_of_options + 1):
            try:
                menu_option = int(input(get_menu()))
            except ValueError:
                self.display.get_wrong_option()
            else:
                if menu_option not in range(1, number_of_options + 1):
                    self.display.get_wrong_option()
        return menu_option

    def display_players(self, player_db) -> None:
        """Dispatch the action requested by the user.
        Args:
            user_choice (int): contains the user choice entered by the user.
        """
        user_choice = 0
        menu_running = True

        while menu_running:
            user_choice = self.select_menu_option(4, self.display.get_submenu)

            if user_choice == 1:

                self.update_players_elo(player_db)
            elif user_choice == 2:
                system("clear")
                self.display_players_by_surname(player_db)
            elif user_choice == 3:
                system("clear")
                self.display_players_by_elo(player_db)
            elif user_choice == 4:
                system("clear")
                menu_running = False

    def update_players_elo(self, db_player) -> None:
        """Method used to modify the elo rank of a player.
        if the player exists in the database, else return an error."""
        try:
            player_id = int(input(self.display.get_player_by_id()))
        except ValueError:
            system("clear")
            self.display.display_wrong_id_type()
        else:
            player_found = db_player.search_player_by_id(player_id)
            if player_found:
                player = Player(
                    player_found["name"],
                    player_found["surname"],
                    player_found["birthdate"],
                    player_found["gender"],
                    player_found["elo"],
                )

                elo = int(input(self.display.get_new_elo()))
                player.elo = elo
                db_player.update_player(player, player_id)
                system("clear")
                self.display.display_successful_change()
            else:
                system("clear")
                self.display.display_unsuccessful_change()

    def get_all_players(self, player_db):
        """_summary_."""
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

    def select_tournaments(self, tournament_db) -> None:
        """Dispatch the action requested by the user.
        Args:
            user_choice (int): contains the user choice entered by the user.
        """
        user_choice = 0
        menu_running = True

        while menu_running:
            for tournament in tournament_db.tournaments:
                self.display.display_tournaments(tournament)

            user_choice = self.select_menu_option(2, self.display.get_import_menu)

            if user_choice == 1:
                tournament = self.recover_tournament(tournament_db)
                return tournament
            elif user_choice == 2:
                system("clear")
                menu_running = False

    def recover_tournament(self, db_tournament):
        """
        Update the elo rank of a player.

        if the player exists in the database, else return an error.
        """
        try:
            tournament_id = int(input(self.display.get_tournament_by_id()))
        except ValueError:
            self.display.display_wrong_id_type()
        else:
            tournament_found = db_tournament.search_tournament_by_id(tournament_id)

            if tournament_found:
                tournament = Tournament()
                tournament.name = tournament_found["name"]
                tournament.place = tournament_found["place"]
                tournament.date = tournament_found["date"]
                tournament.description = tournament_found["description"]
                tournament.time_control = tournament_found["time_control"]

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
                print("not found")
