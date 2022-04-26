"""Match model."""


class Match:
    """Class managing matchs."""

    def __init__(self) -> None:
        """Initialize match objects."""
        self.players_score = ()

    def generate_match(self, round_list) -> None:
        """Generate player pairs.
        round_list is the list of rounds in the tournament model.
        """
        if len(round_list) == 1:
            players_by_rank = [
                id for id in sorted(self.players.keys(), key=lambda item: item[4])
            ]
            middle = len(players_by_rank) / 2
        else:
            pass
