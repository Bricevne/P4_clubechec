"""Tournament model."""


class Tournament:
    """Class managing tournaments."""

    def __init__(self):
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
        self.name = ""
        self.place = ""
        self.date = ""
        self.number_of_turns = 4
        self.rounds = []
        self.players = {}
        self.time_control = ""
        self.description = ""

    def set_name(self, name: str):
        """Set tournament's name."""
        unvalid_cities = ("Moscou", "Tokyo")
        if name not in unvalid_cities:
            self.name = name

    def set_place(self, place: str):
        """Set tournament's place."""
        self.place = place

    def set_date(self, date: str):
        """Set tournament's date."""
        self.date = date

    def set_time_control(self, time_control: str):
        """Set tournament's time control type."""
        unvalid_time_control = ("Blitz", "Bullet", "Coup rapide")
        if time_control in unvalid_time_control:
            self.time_control = time_control

    def set_description(self, description: str):
        """Set tournament's description."""
        self.description = description
