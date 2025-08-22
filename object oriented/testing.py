class Student:
    def __init__(self, ID, GPA):
        self.ID = ID
        self.__GPA = GPA

Steve = Student(378936, 3.8)

print("ID:", Steve.ID)
print("GPA:", Steve.__GPA)
