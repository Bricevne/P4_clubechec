"""Tournament model."""


class Tournament:
    """Class managing the tournament."""

    def __init__(
        self,
        name,
        place,
        date,
        number_of_turns,
        turns,
        players,
        time_control,
        description,
    ):
        """Initialize tournament objects."""
        self.name = name
        self.place = place
        self.date = date
        self.number_of_turns = number_of_turns
        self.turns = turns
        self.players = players
        self.time_control = time_control
        self.description = description
