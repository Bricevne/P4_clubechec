"""Player manager class."""

from model.player import Player
from view.player import PlayerView


class PlayerManager:
    """Class managing the addition of players."""

    def __init__(self):
        """Init."""
        self.display = PlayerView()

    def add_player(self):
        """Add a player."""
        name = input(self.display.get_name())
        surname = input(self.display.get_surname())
        birthdate = input(self.display.get_birthdate())
        gender = input(self.display.get_gender())
        rank = int(input(self.display.get_rank()))
        player = Player(name, surname, birthdate, gender, rank)
        return player
