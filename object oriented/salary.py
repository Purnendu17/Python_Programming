class Employee:
    increment = 1.1  # Class attribute for salary increment factor

    def __init__(self, name, salary):
        self.name = name  # Instance variable for employee name
        self.salary = salary  # Instance variable for employee salary

    @classmethod
    def update_increment(cls, new_increment):
        #Update the salary increment factor.
        cls.increment = new_increment

    def apply_increment(self):
        #Apply the increment to the employee's salary.
        self.salary *= self.increment

# Test the Employee class
emp1 = Employee("Avani", 50000)
print("Initial salary of", emp1.name , ":" , emp1.salary)

# Apply the increment
emp1.apply_increment()
print("Salary after applying increment:", emp1.salary)

# Update the increment factor
Employee.update_increment(1.2)
print("Updated increment factor:", Employee.increment)

# Apply the new increment
emp1.apply_increment()
print("Salary after applying new increment:", emp1.salary)
