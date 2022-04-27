"""Tournament model."""


class Tournament:
    """Class managing tournaments."""

    def __init__(self) -> None:
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
        self.number_of_rounds = 4
        self.rounds = []
        self.players = {}
        self.time_control = ""
        self.description = ""

    def set_name(self, name: str) -> None:
        """Set tournament's name."""
        self.name = name

    def set_place(self, place: str) -> None:
        """Set tournament's place."""
        unvalid_cities = ("Moscou", "Tokyo")
        if place not in unvalid_cities:
            self.place = place

    def set_date(self, date: str) -> None:
        """Set tournament's date."""
        self.date = date

    def set_time_control(self, time_control: str) -> None:
        """Set tournament's time control type."""
        unvalid_time_control = ("Blitz", "Bullet", "Coup rapide")
        if time_control in unvalid_time_control:
            self.time_control = time_control

    def set_description(self, description: str) -> None:
        """Set tournament's description."""
        self.description = description

    def select_players(self, players: dict) -> None:
        """Ask for the tournament's players."""
        self.players = players

    def set_round(self, number_of_rounds: int) -> None:
        """Set tournament's description."""
        self.number_of_rounds = number_of_rounds

    def add_round(self, round: object) -> None:
        """Set tournament's description."""
        self.rounds.append(round)

    def generate_pairs(self) -> None:
        """Generate player pairs.

        round_list is the list of rounds in the tournament model.
        """
        if len(self.rounds) == 0:
            sorted_players = dict(
                (key, value)
                for (key, value) in sorted(
                    self.players.items(), key=lambda x: x[1].rank
                )
            )

            id_players = [id for id in sorted_players.keys()]
            matches = []
            for number in range(0, len(id_players) // 2):
                new_match = (
                    sorted_players[id_players[number]],
                    sorted_players[id_players[number + len(id_players) // 2]],
                )
                matches.append(new_match)
            return matches
        else:
            pass
