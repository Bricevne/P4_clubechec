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
        self.number_of_players = 8
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

    def set_number_of_players(self, number_of_players: int) -> None:
        """Set tournament's description."""
        self.number_of_players = number_of_players

    def add_round(self, round: object) -> None:
        """Set tournament's description."""
        self.rounds.append(round)

    def sort_by_elo_list(self) -> list:
        """Sort players objects by rank."""
        return sorted(self.players.items(), key=lambda x: x[1].elo)

    def sort_by_score_list(self) -> list:
        """Sort players objects by decreasing total score.

        Output in list format.
        """
        return sorted(
            self.players.items(), key=lambda x: x[1].total_score, reverse=True
        )

    def generate_pairs(self) -> None:
        """Generate player pairs.

        round_list is the list of rounds in the tournament model.
        """
        if len(self.rounds) == 0:
            sorted_players = self.sort_by_elo_list()

            matches = []
            for number in range(0, len(sorted_players) // 2):
                new_match = (
                    sorted_players[number],
                    sorted_players[number + len(sorted_players) // 2],
                )
                matches.append(new_match)
            return matches
        else:
            sorted_players = self.sort_by_score_list()

            matches = []
            for number in range(0, len(sorted_players) // 2):
                new_match = (
                    sorted_players[number],
                    sorted_players[number + len(sorted_players) // 2],
                )
                matches.append(new_match)
            return matches

    def sort_by_score_dict(self) -> None:
        """Sort players objects by decreasing total score.

        Output in dict format.
        """
        sorted_players = {k: v for k, v in self.sort_by_score_list()}
        return sorted_players

    def sort_by_elo_dict(self) -> None:
        """Sort players objects by decreasing total score.

        Output in dict format.
        """
        sorted_players = {k: v for k, v in self.sort_by_elo_list()}
        return sorted_players
