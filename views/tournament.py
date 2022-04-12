"""Tournament view."""


class TournamentView:
    """Class managing tournament displays."""

    def __init__(self) -> None:
        """Class initializer."""
        pass

    def get_view_name(self) -> str:
        """Get name input."""
        return "Name: "

    def get_view_place(self) -> str:
        """Get place input."""
        return "Place: "

    def get_view_date(self) -> str:
        """Get date input."""
        return "Date: "

    def get_view_time_control(self) -> str:
        """Get time control input."""
        return "Time_control: "

    def get_view_description(self) -> str:
        """Get description input."""
        return "Description: "
