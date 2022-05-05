"""Player model."""


class Player:
    """Class managing the players."""

    def __init__(
        self, name: str, surname: str, birthdate: str, gender: str, elo: int
    ) -> None:
        """Initialize player objects."""
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.elo = elo
        self.total_score = 0
        self.rank = 0

    def update_score(self, points) -> None:
        """Update the player's total score."""
        self.total_score += points

    def update_rank(self, new_rank: int) -> None:
        """Update the player's rank."""
        self.rank = new_rank

    def serialize_player(self) -> None:
        """Serialize a player for the list of players in the database."""
        serialized_player = {
            "name": self.name,
            "surname": self.surname,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "elo": self.elo,
        }
        return serialized_player

    def serialize_player_tournament(self) -> None:
        """Serialize a player for the list of tournaments in the database."""
        serialized_player = {
            "name": self.name,
            "surname": self.surname,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "elo": self.elo,
            "Total score": self.total_score,
            "Rank": self.rank,
        }
        return serialized_player
