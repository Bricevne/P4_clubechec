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
        """Initialize Tournament objects.

        Args:
            name (str): Tournament's name
            place (str): Tournament's place
            date (str): Tournament's date
            number_of_turns (int): _description_
            rounds (list): _description_
            players (dict): _description_
            time_control (str): _description_
            description (str): _description_
        """
        self.name = name
        self.place = place
        self.date = date
        self.number_of_turns = 4
        self.rounds = []
        self.players = {}
        self.time_control = time_control
        self.description = description
