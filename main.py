"""Main code."""


from controllers.application import Application


def main():
    """Code managing the whole tournament process."""
    application = Application()
    application.menu_manager.display.display_welcome()

    running = True
    while running:

        user_choice = application.menu_manager.select_main_menu_option(4)
        if user_choice == 1:

            players = application.user_manager.get_all_players(application.db_player)
            enough_players = application.tournament_manager.get_tournament_players(
                players
            )

            tournament_running = True
            if not enough_players:
                tournament_running = False

            while tournament_running:
                tournament_option = application.tournament_manager.select_option(
                    4,
                    application.tournament_manager.tournament_view.get_tournament_options,
                )
                if tournament_option == 1:
                    application.tournament_manager.get_round()
                elif tournament_option == 2:

                    end_tournament = application.tournament_manager.start_tournament()
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
            if added_player is not None:
                application.db_player.add_player_db(added_player)

        elif user_choice == 3:
            player_db = application.db_player
            application.user_manager.display_players(player_db)

        elif user_choice == 4:
            running = False


if __name__ == "__main__":
    main()
