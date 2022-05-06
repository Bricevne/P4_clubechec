"""Match model."""


class Match:
    """Class managing matchs."""

    def __init__(self, players_score: tuple) -> None:
        """Initialize match objects."""
        self.players_score = players_score

    def serialize_match(self):
        """Serialize a player for the list of tournaments in the database."""
        serialized_match = {
            "players_score": self.players_score,
        }
        return serialized_match
