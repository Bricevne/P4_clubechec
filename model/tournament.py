"""Tournament model."""


class Tournament:
    """Class managing tournaments."""

    def __init__(
        self,
        name: str,
        place: str,
        date: str,
        number_of_turns: int,
        rounds: list(object),
        players: dict,
        time_control: str,
        description: str,
    ):
        """Initialize tournament objects."""
        self.name = name
        self.place = place
        self.date = date
        self.number_of_turns = 4
        self.rounds = []
        self.players = {}
        self.time_control = time_control
        self.description = description
