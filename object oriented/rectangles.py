class Rectangle:
    # Constructor to initialize length and width
    def __init__(self, length, width):
        self.__length = length  # Private attribute
        self.__width = width    # Private attribute

    # Getter for length
    def get_length(self):
        return self.__length

    # Setter for length
    def set_length(self, length):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("Length must be positive")

    # Getter for width
    def get_width(self):
        return self.__width

    # Setter for width
    def set_width(self, width):
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Width must be positive")

    # Method to calculate area
    def area(self):
        return self.__length * self.__width

    # Method to calculate perimeter
    def perimeter(self):
        return 2 * (self.__length + self.__width)

# Example usage:
rect = Rectangle(10, 5)
print(f"Area: {rect.area()}")  
print(f"Perimeter: {rect.perimeter()}")  

# Modify dimensions using setters
rect.set_length(15)
rect.set_width(7)
print(f"Updated Area: {rect.area()}")  
print(f"Updated Perimeter: {rect.perimeter()}")  