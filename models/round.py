"""Turn model."""

from datetime import datetime


class Round:
    """Class managing turns."""

    def __init__(self) -> None:
        """Initialize round objects."""
        self.name = ""
        self.match = []
        self.start_time = ""
        self.end_time = ""

    def set_round_name(self, name: str) -> None:
        """Set the round's name.

        Args:
            name (str): The round's name
        """
        self.name = name

    def set_starting_time(self) -> None:
        """Set the round's starting time."""
        self.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def set_ending_time(self) -> None:
        """Set the round's ending time."""
        self.end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def add_match(self, match_to_add: object) -> None:
        """Add a match to the round.

        Args:
            match (object): A match instance
        """
        self.match.append(match_to_add)

    def serialize_round(self) -> dict:
        """Serialize a round for the list of tournaments in the database.

        Returns:
            dict: a dictionnary of round instances' attributes
        """
        serialized_round = {
            "name": self.name,
            "match": self.match,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }
        return serialized_round
