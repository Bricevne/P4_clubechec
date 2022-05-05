"""Controller class."""


from controllers.menu import MenuManager
from controllers.user import UserManager
from controllers.tournament import TournamentManager
from controllers.db import DbPlayer


class Application:
    """Application class."""

    def __init__(self) -> None:
        """Initialize class."""
        self.user_manager = UserManager()
        self.tournament_manager = TournamentManager()
        self.menu_manager = MenuManager()
        self.db_player = DbPlayer()