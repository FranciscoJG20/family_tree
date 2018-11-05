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

        self.choose_to_play()
        family_tree = input("{}, would you like to create a family tree?".format(name))

        self.start_game(play_game, self.name)  

    def set_name(self):
        # GREET USER
        print("Welcome to Family Tree")
        name = input("Please, tell me your name: ")

        #SET USER NAME
        print("Hi {}!".format(name))
        self.name = name

    def choose_to_play(self):
        print("yes")
        print("no")

    def start_game(self, play_game):
        if play_game == "yes":
            print("Great! Let's get started!")
        else:
            print("No worries! Create one next time!")

