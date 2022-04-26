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
    while running:
        user_choice = menu_manager.select_menu_option()
        if user_choice == 1:
            tournament_manager = TournamentManager(players)

            tournament_running = True
            while tournament_running:
                tournament_option = tournament_manager.select_tournament_option()
                if tournament_option == 1:
                    tournament_manager.get_tournament_players()
                elif tournament_option == 2:
                    tournament_manager.get_round()
                elif tournament_option == 3:
                    pass
                elif tournament_option == 4:
                    pass
                elif tournament_option == 5:
                    tournament_running = False

        elif user_choice == 2:
            added_player = user_manager.add_player()
            players[player_counter] = added_player
            player_counter += 1
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            running = False


if __name__ == "__main__":
    main()
