"""Main code."""

from controllers.menu import MenuManager
from controllers.user import UserManager
from controllers.tournament import TournamentManager


from models.player import Player


def players_test():
    """Test function."""
    player = {}
    counter = 1
    brice = Player("Brice", "Venayre", "", "M", 1)
    paul = Player("Paul", "Ducasse", "", "M", 4)
    jean = Player("Jean", "Courage", "", "M", 2)
    marie = Player("Marie", "Larisse", "", "F", 3)
    helene = Player("Helene", "Walker", "", "F", 6)
    romain = Player("Romain", "Rondet", "", "M", 5)
    alan = Player("Alan", "Smith", "", "M", 7)
    celia = Player("Celia", "Lachaise", "", "F", 8)
    for i in (brice, paul, jean, marie, helene, romain, alan, celia):
        player[counter] = i
        counter += 1
    return player


def main():
    """Code managing the whole tournament process."""
    menu_manager = MenuManager()
    user_manager = UserManager()

    players = {}

    # player_counter = len(players) + 1
    player_counter = 9

    # FOR TEST ONLY
    players = players_test()
    # FOR TEST ONLY

    running = True
    while running:
        user_choice = menu_manager.select_menu_option()

        if user_choice == 1:

            tournament_manager = TournamentManager(players)

            enough_players = tournament_manager.get_tournament_players()
            tournament_running = True
            if not enough_players:
                tournament_running = False

            while tournament_running:
                tournament_option = tournament_manager.select_option(
                    range(1, 5),
                    tournament_manager.tournament_view.get_tournament_options,
                )
                if tournament_option == 1:
                    tournament_manager.get_round()
                elif tournament_option == 2:

                    round_running = True
                    while (
                        len(tournament_manager.tournament.rounds)
                        < tournament_manager.tournament.number_of_rounds
                    ) and round_running:

                        round_option = tournament_manager.select_option(
                            range(1, 5),
                            tournament_manager.tournament_view.get_round_options,
                        )
                        if round_option == 1:
                            new_round = tournament_manager.start_new_round()
                            tournament_manager.tournament.add_round(new_round)

                        elif round_option == 2:
                            pass
                        elif round_option == 3:
                            pass
                        elif round_option == 4:
                            round_running = False
                            tournament_running = False
                            running = False

                elif tournament_option == 3:
                    pass
                elif tournament_option == 4:
                    tournament_running = False
                    running = False

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
