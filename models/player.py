"""Player model."""


class Player:
    """Class managing the players."""

    def __init__(
        self, name: str, surname: str, birthdate: str, gender: str, elo: int
    ) -> None:
        """Initialize player objects.

        Args:
            name (str): The player's name
            surname (str): The player's surname
            birthdate (str): The player's birthdate in format YYYY-MM-DD
            gender (str): The player's gender (M/F)
            elo (int): The player's elo
        """
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.elo = elo
        self.total_score = 0
        self.rank = 0

    def update_score(self, points: int) -> None:
        """Update the player's total score.

        Args:
            points (int): The points to be added to the player's total score
        """
        self.total_score += points

    def update_rank(self, new_rank: int) -> None:
        """Update the player's rank.

        Args:
            new_rank (int): The player's new rank
        """
        self.rank = new_rank

    def serialize_player(self) -> dict:
        """Serialize a player for the list of players in the database.

        Returns:
            dict: a dictionnary of player instances attributes except for the rank and total score
                    used for the player's database.
        """
        serialized_player = {
            "name": self.name,
            "surname": self.surname,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "elo": self.elo,
        }
        return serialized_player

    def serialize_player_tournament(self) -> dict:
        """Serialize a player for the tournaments in the database.

        Returns:
            dict: a dictionnary of player instances attributes
                    used for the tournament's database.
        """
        serialized_player = {
            "name": self.name,
            "surname": self.surname,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "elo": self.elo,
            "total_score": self.total_score,
            "rank": self.rank,
        }
        return serialized_player
