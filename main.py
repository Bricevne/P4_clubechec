"""Main code."""

from controller.menu import MenuManager


def main():
    """Code managing the whole tournament process."""
    menu_manager = MenuManager()
    menu_manager.select_menu_option()


if __name__ == "__main__":
    main()
