"""Main code."""


from controllers.user import UserManager


def main():
    """Run main code."""
    user_manager = UserManager()
    user_manager.start_program()


if __name__ == "__main__":
    main()
