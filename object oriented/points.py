class POINT:
    # Constructor to initialize x, y, and z
    def __init__(self, x, y, z):
        self.x = x  # Public property
        self.y = y  # Public property
        self.z = z  # Public property

    # Method to calculate and return the sum of squares of x, y, and z
    def sqsum(self):
        return self.x**2 + self.y**2 + self.z**2

# Example usage:
point = POINT(1, 2, 3)
result = point.sqsum()
print(f"The sum of squares is: {result}")