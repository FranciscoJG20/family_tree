from parent import Parent 

class Child(Parent):

    def __init__(self, name, dob, dod="false"):
        Parent.__init(self, name, dob, dod="false")
	

