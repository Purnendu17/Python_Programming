class Player: 
    teamname = 'Liverpool'  # Class variable

    def __init__(self, name): 
        self.name = name  # Instance variable

    @staticmethod
    def demo():
        print("I am static")

#calling the static method correctly:
Player.demo()  # Calling using the class name

p1 = Player("Avani")  # Creating an instance
p1.demo()  # Calling using the instance