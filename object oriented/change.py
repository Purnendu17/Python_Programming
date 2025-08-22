class player:
    formerteams = [] # class variable
    teamname = 'Liverpool'
    def _init_(self,name):
        self.name = name # creating instance variables

        p1 = player('avani')
        p2 = player('anamika')

        p1 = player('avani')
        p1.formerteams.append('barcelona') # wrong use of class variable
        p2 = player('anamika')
        p2.formerteams.append('chelesa') # wrong use of class variable 
        print(p1.name)
        print(p1.teamname)
        print(p1.formerteams)