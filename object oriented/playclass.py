class Player: 
    teamname = 'Liverpool'  # Class variable

    def __init__(self, name): 
        self.name = name  # Instance variable

    @classmethod
    def getteamname(cls):
        return cls.teamname
    
p1 = Player('Avani')
print(p1.name)
print(p1.getteamname())