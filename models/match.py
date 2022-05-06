"""Match model."""


class Match:
    """Class managing matchs."""

    def __init__(self, players_score: tuple) -> None:
        """Initialize match objects.

        Args:
            players_score (tuple): a tuple with two lists containing a player's id and a score
        """
        self.players_score = players_score

    def serialize_match(self) -> dict:
        """Serialize a match for the list of tournaments in the database.

        Returns:
            dict: a dictionnary of match instance attributes
        """
        serialized_match = {
            "players_score": self.players_score,
        }
        return serialized_match
