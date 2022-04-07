"""Turn model."""


class Turn:
    """Class managing turns."""

    def __init__(self, name: str, match: list(object), start_time, end_time):
        """Initialize turn objects."""
        self.name = name
        self.match = None
        self.start_time = start_time
        self.end_time = end_time
