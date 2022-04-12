"""Turn model."""


class Turn:
    """Class managing turns."""

    def __init__(self, name: str, start_time, end_time) -> None:
        """Initialize turn objects."""
        self.name = name
        self.match = []
        self.start_time = start_time
        self.end_time = end_time
