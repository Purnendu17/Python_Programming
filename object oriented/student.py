class Student:
    # Constructor to initialize name and roll number
    def __init__(self, name, roll_no):
        self.__name = name  # Private attribute
        self.__roll_no = roll_no  # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            raise ValueError("Name must be a non-empty string")

    # Getter for roll number
    def get_roll_no(self):
        return self.__roll_no

    # Setter for roll number
    def set_roll_no(self, roll_no):
            self.__roll_no = roll_no


# Example usage:
student = Student("Avani", 127)
print(f"Name: {student.get_name()}, Roll No: {student.get_roll_no()}")

# Modify student details using setters
student.set_name(" Dora")
student.set_roll_no(456)
print(f"Updated Name: {student.get_name()}, Updated Roll No: {student.get_roll_no()}")