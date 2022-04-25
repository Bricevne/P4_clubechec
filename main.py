"""Main code."""

from controllers.menu import MenuManager
from controllers.user import UserManager
from controllers.tournament import TournamentManager


def main():
    """Code managing the whole tournament process."""
    menu_manager = MenuManager()
    user_manager = UserManager()

    players = {}
    player_counter = len(players) + 1

    running = True
    while running is True:
        user_choice = menu_manager.select_menu_option()
        if user_choice == 1:
            tournament_manager = TournamentManager(players)
            tournament_manager.get_tournament_players()
            print(tournament_manager.tournament.players)
        elif user_choice == 2:
            added_player = user_manager.add_player()
            players[player_counter] = added_player
            player_counter += 1
        elif user_choice == 3:
            running = False
        elif user_choice == 4:
            running = False


if __name__ == "__main__":
    main()
