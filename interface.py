#Family Tree Creator - Create a class called Person which 
#will have a name, when they were born and when (and if) they died. 
#Allow the user to create these Person classes and 
#put them into a family tree structure. 
#Print out the tree to the screen.

from person import Person
from parent import Parent
from child import Child 

class Interface:
    def __init__(self):
        self.name = None

    def main_menu(self):
        self.set_name()

        play_game = input("Hi {}, would you like to create a family tree? [yes/no]".format(self.name))
        play_game = play_game.lower()

        self.start_game(play_game)  

    def set_name(self):
        # GREET USER
        print("Welcome to Family Tree!")
        name = input("Please, tell me your name: ")

        #SET USER NAME
        self.name = name.lower()

    def start_game(self, play_game):
        if play_game == "yes":
            print("Great! Let's get started!")
            ## method to have user input the first member of family 
        else:
            print("No worries! Create one next time!")

    
    # def create_family():
    #     print("Let's enter your first family member")
    #     return Person(
    #         input('Name: '),
    #         input('Date of Birth: '),
    #         input('Date of Death: '),
    #     )

