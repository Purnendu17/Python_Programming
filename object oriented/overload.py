class Employee:
    def __init__(self, ID, Salary, Department):
        self.ID = ID
        self.Salary = Salary
        self.Department = Department
    
    # Method to assign additional attributes (overloading-like behavior)
    def demo(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    # Method to calculate tax (20% of salary)
    def tax(self):
        return self.Salary * 0.2
    
    # Method to calculate salary per day (assuming 20 working days)
    def salaryperday(self):
        return self.Salary / 20
    

# Creating an instance (object) of the Employee class
anamika = Employee(1230, 2000, "ModuleNotFound")

# Calling the demo method to set additional attributes
anamika.demo("a", "b", "c", "d")

# Printing details of the additional attributes
print(anamika.a)  
print(anamika.b)  

