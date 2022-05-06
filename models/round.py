"""Turn model."""

from datetime import date
import time


class Round:
    """Class managing turns."""

    def __init__(self) -> None:
        """Initialize turn objects."""
        self.name = ""
        self.match = []
        self.start_time = ""
        self.end_time = ""

    def set_round_name(self, name) -> None:
        """Set the round's name."""
        self.name = name

    def set_starting_time(self) -> str:
        """Set the round's starting time."""
        today_time = time.time()
        date_from_current_time = date.fromtimestamp(today_time)
        self.start_time = date_from_current_time.ctime()

    def set_ending_time(self) -> str:
        """Set the round's starting time."""
        today_time = time.time()
        date_from_current_time = date.fromtimestamp(today_time)
        self.end_time = date_from_current_time.ctime()

    def add_match(self, match) -> None:
        """Add a match to the round."""
        self.match.append(match)

    def serialize_round(self):
        """Serialize a player for the list of tournaments in the database."""
        serialized_round = {
            "name": self.name,
            "match": self.match,
            "start_time": self.start_time,
            "end_time": self.end_time,
        }
        return serialized_round
