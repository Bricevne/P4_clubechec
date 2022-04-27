"""Match model."""


class Match:
    """Class managing matchs."""

    def __init__(self, players_score: tuple) -> None:
        """Initialize match objects."""
        self.players_score = players_score
