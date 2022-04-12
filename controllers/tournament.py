"""_summary_
"""

from models.tournament import Tournament


class TournamentManager:
    def __init__(self) -> None:
        self.tournament = Tournament()
        self.get_tournament_information()

    def get_tournament_name(self):
        while self.tournament.name == "":
            name = input("Name: ").capitalize()
            self.tournament.get_name(name)

    def get_tournament_place(self):
        place = input("Place: ").capitalize()
        self.tournament.get_place(place)

    def get_tournament_date(self):
        date = input("Date: ")
        self.tournament.get_date(date)

    def get_tournament_time_control(self):
        while self.tournament.time_control == "":
            time_control = input("Time control: ").capitalize()
            self.tournament.get_time_control(time_control)

    def get_tournament_description(self):
        description = input("Description: ").capitalize()
        self.tournament.get_description(description)

    def get_tournament_information(self):
        self.get_tournament_name()
        self.get_tournament_place()
        self.get_tournament_date()
        self.get_tournament_time_control()
        self.get_tournament_description()
