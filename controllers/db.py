"""Define the database controller."""


from tinydb import TinyDB

DB = TinyDB("db/db.json")
TOURNAMENT = DB.table("Tournament")
PLAYERS = DB.table("Players")


class DbPlayer:
    """Class managing the player database."""

    def __init__(self) -> None:
        """Initialize class."""
        self.players = PLAYERS

    def add_player_db(self, player: object) -> None:
        """Add a player to the players table in the database.

        Args:
            player (object): Player instance
        """

        self.players.insert(player.serialize_player())

    def search_player_by_id(self, player_id: int) -> dict:
        """Search a player in the database with his id.

        Args:
            player_id (int): Player's id

        Returns:
            dict: Dictionnary containing a player's information
        """
        player = self.players.get(doc_id=player_id)
        return player

    def update_player(self, player: object, player_id: int) -> None:
        """Update a player's information in the database, knowing his id.

        Args:
            player (object): Player instance
            player_id (int): Player's id
        """
        self.players.update(player.serialize_player(), doc_ids=[player_id])

    def sort_players_by_elo(self) -> list:
        """Sort the list of players from low elo to high.

        Returns:
            list: Sorted list of players
        """
        sorted_players = sorted(self.players, key=lambda player: player["elo"])
        return sorted_players

    def sort_players_by_surname(self) -> list:
        """Sort the list of players by surname.

        Returns:
            list: Sorted list of players
        """
        sorted_players = sorted(self.players, key=lambda player: player["surname"])
        return sorted_players


class DbTournament:
    """Class managing the tournament database."""

    def __init__(self) -> None:
        """Initialize class."""
        self.tournaments = TOURNAMENT

    def add_tournament_db(self, tournament: object) -> None:
        """Add a tournament to the tournament table in the database.

        Args:
            tournament (object): Tournament instance
        """
        self.tournaments.insert(tournament.serialize_tournament())

    def update_tournament_db(self, tournament: object, tournament_id: int) -> None:
        """Update a tournament's information in the database, knowing its id.

        Args:
            tournament (object): Tournament instance
            tournament_id (int): Tournament id
        """
        self.tournaments.update(
            tournament.serialize_tournament(), doc_ids=[tournament_id]
        )

    def search_tournament_by_id(self, tournament_id: int) -> dict:
        """Search a tournament thanks to its id.

        Args:
            tournament_id (int): Tournament id

        Returns:
            dict: Dictionnary of a tournament's information
        """
        tournament = self.tournaments.get(doc_id=tournament_id)
        return tournament

    def search_tournament_id_by_description(self, description: str) -> int:
        """Search a tournament thanks to its description.

        Args:
            description (str): Tournament's description

        Returns:
            int: Tournament id
        """
        for tournament in self.tournaments:
            if tournament["description"] == description:
                return tournament.doc_id
