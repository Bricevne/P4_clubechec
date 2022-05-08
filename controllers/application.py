"""Controller class."""


from controllers.menu import MenuManager
from controllers.user import UserManager
from controllers.tournament import TournamentManager
from controllers.db import DbPlayer, DbTournament


class Application:
    """Application class containing all controllers."""

    def __init__(self) -> None:
        """Initialize class."""
        self.user_manager = UserManager()
        self.tournament_manager = TournamentManager()
        self.menu_manager = MenuManager()
        self.db_player = DbPlayer()
        self.db_tournament = DbTournament()
