"""Player model."""


class Player:
    """Class managing the players."""

    def __init__(
        self, name: str, surname: str, birthdate: str, gender: str, rank: int
    ) -> None:
        """Initialize player objects."""
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.total_score = 0
        self.rank = rank

    def update_score(self, points) -> None:
        """Update the player's total score."""
        self.total_score += points

    def update_rank(self, new_rank: int) -> None:
        """Update the player's rank."""
        self.rank = new_rank
