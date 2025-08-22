# # creating class for an employee'
# class Employee:
#  ID = 1234
#  Salary = 20
#  department = "H"

#     #creating class object below
# anamika = Employee(1234,20,"H")
#     #object.property
#     # print prperties of this object 
# print("ID=",anamika.ID)

class Employee:
    # Defining class variables
    ID = 1234
    Salary = 20
    Department = "ModuleNotFoundError"

# Creating an instance (object) of the Employee class
anamika = Employee()
# Creating property outside of the Employee class
anamika.title="Engineering Lead"

# Accessing and printing the properties of the object
print("ID =", anamika.ID)
print("Salary =", anamika.Salary)
print("Department =", anamika.Department)
print("Title =", anamika.title)