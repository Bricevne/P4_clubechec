"""Tournament model."""

from models.round import Round


class Tournament:
    """Class managing tournaments."""

    def __init__(self) -> None:
        """Initialize Tournament objects."""
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
        """Set the tournament's name.

        Args:
            name (str): The tournament's name
        """
        self.name = name

    def set_place(self, place: str) -> None:
        """Set the tournament's place.

        Args:
            place (str): The tournament's location
        """
        unvalid_cities = ("Moscou", "Tokyo")
        if place not in unvalid_cities:
            self.place = place

    def set_date(self, date: str) -> None:
        """Set the tournament's date.

        Args:
            date (str): The tournament's date
        """
        self.date = date

    def set_time_control(self, time_control: str) -> None:
        """Set the tournament's time control type.

        Args:
            time_control (str): The tournament's type control, a  blitz, a bullet or a "coup rapide"
        """
        unvalid_time_control = ("Blitz", "Bullet", "Coup rapide")
        if time_control in unvalid_time_control:
            self.time_control = time_control

    def set_description(self, description: str) -> None:
        """Set the tournament's description.

        Args:
            description (str): The tournament's description
        """
        self.description = description

    def select_players(self, players: dict) -> None:
        """Set for the tournament's players.

        Args:
            players (dict): A dictionnary of player's instances for a tournament
        """
        self.players = players

    def set_round(self, number_of_rounds: int) -> None:
        """Set the tournament's number of rounds.

        Args:
            number_of_rounds (int): The tournament's number of rounds
        """
        self.number_of_rounds = number_of_rounds

    def set_number_of_players(self, number_of_players: int) -> None:
        """Set the tournament's number of players.

        Args:
            number_of_players (int): The tournament's number of players
        """
        self.number_of_players = number_of_players

    def add_round(self, round: object) -> None:
        """Add a round instance to the rounds attribute.

        Args:
            round (object): A round instance
        """
        self.rounds.append(round)

    def sort_by_elo_list(self) -> tuple:
        """Sort players instances by elo.

        Returns:
            tuple: A tuple containing tuples of a player's id and player instance sorted by elo
        """
        return sorted(self.players.items(), key=lambda player: player[1].elo)

    def sort_by_elo_dict(self) -> dict:
        """Sort players instances by elo.

        Returns:
            dict: a dictionnary of id and player instances "sorted" by elo
        """
        sorted_players = {k: v for k, v in self.sort_by_elo_list()}
        return sorted_players

    def sort_by_surname_list(self) -> tuple:
        """Sort players instances by surname.

        Returns:
            tuple: A tuple containing tuples of a player's id and player instance sorted by elo
        """
        return sorted(self.players.items(), key=lambda player: player[1].surname)

    def sort_by_surname_dict(self) -> dict:
        """Sort players instances by surname.

        Returns:
            dict: a dictionnary of id and player instances "sorted" by surname
        """
        sorted_players = {k: v for k, v in self.sort_by_surname_list()}
        return sorted_players

    def sort_by_score_list(self) -> tuple:
        """Sort players instances by decreasing total score.

        Returns:
            tuple: A tuple containing tuples of a player's id and player instance sorted by total score
        """
        return sorted(
            self.players.items(), key=lambda player: player[1].total_score, reverse=True
        )

    def sort_by_score_dict(self) -> dict:
        """Sort players instances by decreasing total score.

        Returns:
            dict: a dictionnary of id and player instances "sorted" by score
        """
        sorted_players = {k: v for k, v in self.sort_by_score_list()}
        return sorted_players

    def generate_pairs(self) -> list:
        """Generate player pairs for each match.

        Pairs are sorted by elo for the first round, and by total score for the others.

        Returns:
            list: a list containing tuples with 2 player instances each
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
            for number in range(0, len(sorted_players), 2):
                new_match = (
                    sorted_players[number],
                    sorted_players[number + 1],
                )
                matches.append(new_match)
            return matches

    def serialize_tournament(self) -> dict:
        """Serialize a tournament for the database when ites attributes don't contain objects.

        Returns:
            dict: a dictionnary of tournament instances' attributes
        """
        serialized_tournament = {
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "number_of_rounds": self.number_of_rounds,
            "number_of_players": self.number_of_players,
            "rounds": self.rounds,
            "players": self.players,
            "time_control": self.time_control,
            "description": self.description,
        }
        return serialized_tournament

    def serialize_tournament_attributes(self) -> object:
        """Serialize all tournaments attributes containing objects.

        Returns:
            object: A tournament instance
        """
        players_serialized = {}
        if len(self.players) > 0:
            for id, player in self.players.items():
                serialized_player = player.serialize_player_tournament()
                players_serialized[id] = serialized_player

        rounds_serialized = []
        if len(self.rounds) > 0:
            for round in self.rounds:
                new_round = Round()
                new_round.name = round.name
                new_round.start_time = round.start_time
                new_round.end_time = round.end_time

                for match in round.match:
                    serialized_match = match.serialize_match()

                    new_round.match.append(serialized_match)

                serialized_round = new_round.serialize_round()
                rounds_serialized.append(serialized_round)

        tournament_to_serialize = Tournament()
        tournament_to_serialize.name = self.name
        tournament_to_serialize.place = self.place
        tournament_to_serialize.date = self.date
        tournament_to_serialize.number_of_rounds = self.number_of_rounds
        tournament_to_serialize.number_of_players = self.number_of_players
        tournament_to_serialize.rounds = rounds_serialized
        tournament_to_serialize.players = players_serialized
        tournament_to_serialize.time_control = self.time_control
        tournament_to_serialize.description = self.description

        return tournament_to_serialize
