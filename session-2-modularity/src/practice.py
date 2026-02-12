class Player:
    # Classes need to start with a capital letter
    # Classes will have attributes/variables and methods/functions
    def __init__(self, name, email): # THis is the initialise the set up
        self.name = name
        self.email = email
        self.high_score = 0
        self.banned = False
        
    def __str__(self):
        return f"Name: {self.name} | Email: {self.email} | HS: {self.high_score}"