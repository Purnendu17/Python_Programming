class CALCULATOR:
    # Constructor to initialize num1 and num2
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    # Method to add num1 and num2
    def add(self):
        return self.num1 + self.num2

    # Method to subtract num2 from num1
    def subtract(self):
        return self.num1 - self.num2

    # Method to multiply num1 and num2
    def multiply(self):
        return self.num1 * self.num2

    # Method to divide num1 by num2
    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Division by zero is not allowed"

# Example usage:
calc = CALCULATOR(10, 5)
print("Addition:", calc.add())
print("Subtraction:",calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())