"""Define the db controller."""


from tinydb import TinyDB, Query
from models.player import Player

DB = TinyDB("db/db.json")
USER = Query()
TOURNAMENT = DB.table("Tournament")
PLAYERS = DB.table("Players")


class DbPlayer:
    def __init__(self) -> None:
        self.players = PLAYERS

    def add_player_db(self, player) -> None:
        """Add a player to the players table in the database.

        Args:
            player (Player): Player instance
        """

        self.players.insert(player.serialize_player())

    def search_player_by_name(self, name, surname):
        """_summary_.

        Args:
            name (_type_): _description_
            surname (_type_): _description_

        Returns:
            _type_: _description_
        """
        for player in self.players:
            if player.name == name and player.surname == surname:
                return player
        return None

    def search_player_by_id(self, player_id):
        """_summary_.

        Args:
            player_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        player = self.players.get(doc_id=player_id)
        return player

    def update_player(self, player: object, player_id: int) -> None:
        """Method used to modify a player in the database.

        Args:
            player (PLayer): a Player instance
            player_id (int): contains the player id.
        """
        self.players.update(player.serialize_player(), doc_ids=[player_id])

    def sort_players_by_elo(self):
        """Sort the list from high elo to low.

        Returns:
            players_sort [list]: a sorted list
        """
        sorted_players = sorted(self.players, key=lambda player: player["elo"])
        return sorted_players

    def sort_players_by_surname(self):
        """Sort the list from high elo to low.

        Returns:
            players_sort [list]: a sorted list
        """
        sorted_players = sorted(self.players, key=lambda player: player["surname"])
        return sorted_players

    def get_player_id(self, name: str, surname: str) -> int:
        """Method used to find the player id in the PLAYERS table.
        Args:
            last_name (str): contains the last name entered by the user,
            first_name (str): contains the first name entered by the user,
        Returns:
            player_found.doc_id (int): a player id in the PLAYERS table
        """
        player_found = self.search_table_players(last_name, first_name)
        if player_found:
            return player_found.doc_id
        return None
