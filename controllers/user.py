"""User manager class."""

from models.player import Player
from views.user import UserView


class UserManager:
    """Class managing."""

    def __init__(self) -> None:
        """Init."""
        self.display = UserView()

    def add_player(self) -> object:
        """Add a player."""
        name = input(self.display.get_name())
        surname = input(self.display.get_surname())
        birthdate = input(self.display.get_birthdate())
        gender = input(self.display.get_gender())
        rank = int(input(self.display.get_rank()))
        player = Player(name, surname, birthdate, gender, rank)
        return player
