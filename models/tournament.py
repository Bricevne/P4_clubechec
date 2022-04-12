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

    def get_name(self, name):
        unvalid_cities = ("Moscou", "Tokyo")
        if name not in unvalid_cities:
            self.name = name

    def get_place(self, place):
        self.place = place

    def get_date(self, date):
        self.date = date

    def get_time_control(self, time_control):
        unvalid_time_control = ("Blitz", "Bullet", "Coup rapide")
        if time_control in unvalid_time_control:
            self.time_control = time_control

    def get_description(self, description):
        self.description = description
