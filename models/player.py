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
