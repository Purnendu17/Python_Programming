class Employee:
    def __init__(self, ID, Salary, Department):
        self.ID = ID
        self.Salary = Salary
        self.Department = Department

# Creating an instance (object) of the Employee class
anamika = Employee(1230,20,"ModuleNotFound")

print("ID =", anamika.ID)
print("Salary =", anamika.Salary)
print("Department =", anamika.Department)
