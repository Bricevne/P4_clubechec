"""Main code."""


from os import system
from socket import AF_APPLETALK
from controllers.application import Application


def main():
    """Code managing the whole tournament process."""
    system("clear")
    running = True
    while running:

        application = Application()
        user_choice = application.menu_manager.select_main_menu_option(4)

        if user_choice == 1:
            system("clear")
            players = application.user_manager.get_all_players(application.db_player)
            enough_players = application.tournament_manager.set_tournament_information(
                players
            )
            application.db_tournament.add_tournament_db(
                application.tournament_manager.tournament
            )
            tournament_running = True
            if not enough_players:
                tournament_running = False

            while tournament_running:
                tournament_option = application.tournament_manager.select_option(
                    5,
                    application.tournament_manager.tournament_view.get_tournament_options,
                )
                if tournament_option == 1:
                    system("clear")
                    enough_players = (
                        application.tournament_manager.get_participating_players(
                            players
                        )
                    )
                    if enough_players:
                        end_tournament = (
                            application.tournament_manager.start_tournament()
                        )
                        tournament_running = False
                        if not end_tournament:
                            running = False
                elif tournament_option == 2:
                    system("clear")
                    application.tournament_manager.get_round_numbers()
                elif tournament_option == 3:
                    system("clear")
                    application.tournament_manager.get_player_numbers()
                elif tournament_option == 4:
                    pass
                elif tournament_option == 5:
                    tournament_running = False
                    running = False

        elif user_choice == 2:
            added_player = application.user_manager.add_player()
            if added_player is not None:
                application.db_player.add_player_db(added_player)

        elif user_choice == 3:
            system("clear")
            player_db = application.db_player
            application.user_manager.display_players(player_db)

        elif user_choice == 4:
            running = False


if __name__ == "__main__":
    main()
