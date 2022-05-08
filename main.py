"""Main code."""


from os import system
from controllers.application import Application


def main():
    """Code managing the whole tournament process."""
    running = True
    while running:

        application = Application()
        user_choice = application.menu_manager.select_menu_option(6)

        if user_choice == 1:
            application.tournament_manager.create_tournament(application)
        elif user_choice == 2:
            added_player = application.user_manager.add_player()
            if added_player is not None:
                application.db_player.add_player_db(added_player)

        elif user_choice == 3:
            system("clear")
            player_db = application.db_player
            application.user_manager.display_players(player_db)

        elif user_choice == 4:
            tournament_db = application.db_tournament
            imported_tournament = application.user_manager.import_tournament(
                tournament_db, application.user_manager.user_view.get_import_menu
            )
            if imported_tournament:
                application.tournament_manager.tournament = imported_tournament
                application.tournament_manager.create_tournament(application)

        elif user_choice == 5:
            tournament_db = application.db_tournament
            found_tournament = application.user_manager.import_tournament(
                tournament_db, application.user_manager.user_view.get_import_menu
            )
            if found_tournament:
                application.tournament_manager.tournament = found_tournament
                application.tournament_manager.display_by_rank()
                application.user_manager.display_tournament_information(
                    application,
                    application.user_manager.user_view.get_tournament_information_menu,
                )
        elif user_choice == 6:
            running = False


if __name__ == "__main__":
    main()
