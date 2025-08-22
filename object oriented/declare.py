class Employee:
    def __init__(self, ID, Salary, Department):
        self.ID = ID
        self.Salary = Salary
        self.Department = Department

    # Method to calculate tax (20% of salary)
    def tax(self):
        return self.Salary * 0.2
    
    # Method to calculate salary per day (assuming 20 working days)
    def salaryperday(self):
        return self.Salary / 20
    

# Creating an instance (object) of the Employee class
anamika = Employee(1230, 2000, "ModuleNotFound")

# Printing details of the employee
print("ID =", anamika.ID)
print("Salary =", anamika.Salary)
print("Department =", anamika.Department)
print("Tax =", anamika.tax())  # Calling the tax method
print("Salary per day =", anamika.salaryperday())  # Calling the salaryperday method
