class Employee:
    def __init__(self, ID, Salary):
        self.ID = ID
        self.__Salary = Salary #Making salary private

anamika = Employee(1230,20)

print("ID =", anamika.ID)
print("Salary =", anamika.Salary) #Error of attribute salary being absent arises
