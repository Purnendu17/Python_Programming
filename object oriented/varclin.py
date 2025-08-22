class Player: 
    teamname = 'Liverpool'  # Class variable

    def __init__(self, name): 
        self.name = name  # Instance variable

# Creating instances (objects) of the Player class
p1 = Player('Avani')
p2 = Player('Anamika')

# Accessing instance and class variables
print(p1.name)
print(p1.teamname)
print(p2.name)
print(p2.teamname)
