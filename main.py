"""Main code."""


from controllers.application import Application

from models.player import Player


# FOR TEST ONLY
def players_test():
    """Test function."""
    player = {}
    counter = 1
    brice = Player("Brice", "Venayre", "", "M", 1234)
    paul = Player("Paul", "Ducasse", "", "M", 4232)
    jean = Player("Jean", "Courage", "", "M", 2344)
    marie = Player("Marie", "Larisse", "", "F", 3654)
    helene = Player("Helene", "Walker", "", "F", 5566)
    romain = Player("Romain", "Rondet", "", "M", 6456)
    alan = Player("Alan", "Smith", "", "M", 7543)
    celia = Player("Celia", "Lachaise", "", "F", 8567)
    for i in (brice, paul, jean, marie, helene, romain, alan, celia):
        player[counter] = i
        counter += 1
    return player


# FOR TEST ONLY


def main():
    """Code managing the whole tournament process."""
    application = Application()

    players = {}

    # player_counter = len(players) + 1
    player_counter = 9

    # FOR TEST ONLY
    players = players_test()
    # FOR TEST ONLY

    # start new tournament,
    running = True
    while running:

        user_choice = application.menu_manager.select_menu_option()

        if user_choice == 1:

            enough_players = application.tournament_manager.get_tournament_players(
                players
            )

            tournament_running = True
            if not enough_players:
                tournament_running = False

            while tournament_running:
                tournament_option = application.tournament_manager.select_option(
                    range(1, 5),
                    application.tournament_manager.tournament_view.get_tournament_options,
                )
                if tournament_option == 1:
                    application.tournament_manager.get_round()
                elif tournament_option == 2:

                    end_tournament = application.tournament_manager.start_tournament()
                    players = {}
                    # FOR TEST ONLY
                    players = players_test()
                    # FOR TEST ONLY
                    tournament_running = False
                    if not end_tournament:
                        running = False

                elif tournament_option == 3:
                    pass
                elif tournament_option == 4:
                    tournament_running = False
                    running = False

        elif user_choice == 2:
            added_player = application.user_manager.add_player()
            players[player_counter] = added_player
            player_counter += 1
        elif user_choice == 3:
            application.tournament_manager.display_by_rank()
        elif user_choice == 4:
            running = False


if __name__ == "__main__":
    main()
