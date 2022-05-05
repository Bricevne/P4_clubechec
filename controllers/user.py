"""User manager class."""

from models.player import Player
from views.user import UserView
from os import system


class UserManager:
    """Class managing."""

    def __init__(self) -> None:
        """Init."""
        self.display = UserView()

    def add_player(self) -> object:
        """Add a player."""
        system("clear")
        name = input(self.display.get_name()).capitalize()
        surname = input(self.display.get_surname()).capitalize()
        birthdate = input(self.display.get_birthdate())
        gender = input(self.display.get_gender()).capitalize()
        elo = int(input(self.display.get_elo()))
        confirmation = self.get_user_confirmation(
            ("y", "Y"), ("n", "N"), self.display.get_confirmation
        )
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

    def select_menu_option(self, number_of_options) -> int:
        """Ask for User choice."""
        menu_option = 0
        while menu_option not in range(1, number_of_options + 1):
            try:
                menu_option = int(input(self.display.get_submenu()))
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
            user_choice = self.select_menu_option(4)

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
        player_id = int(input("Quel joueur ? "))

        player_found = db_player.search_player_by_id(player_id)
        if player_found:
            player = Player(
                player_found["name"],
                player_found["surname"],
                player_found["birthdate"],
                player_found["gender"],
                player_found["elo"],
            )

            elo = int(input("nouvel elo :"))
            player.elo = elo
            db_player.update_player(player, player_id)
            print("Le joueur a bien été modifié.")
        else:
            print("Aucun joueur avec cet ID n'a été trouvé.")

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
