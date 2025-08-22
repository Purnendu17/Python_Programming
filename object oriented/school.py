class Student:
    # Class variable shared by all instances
    school = "IHS"

    def __init__(self, name, age):
        # Instance variables unique to each student
        self.name = name
        self.age = age
        self.formerschool = []

# Create instances of the Student class
s1 = Student("Avani", 16)
s2 = Student("Anamika", 15)
s1.formerschool.append("DPS")
s2.formerschool.append("DPS")

print(s1.name)
print(s1.age)
print(s1.formerschool)
print(s1.school)
print(s2.name)
print(s2.age)
print(s2.formerschool)
print(s2.school)