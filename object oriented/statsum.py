class MathMixin:
    @staticmethod
    def add_numbers(*args):
        #Adds any number of arguments passed to it.
        return sum(args)


class Statistics(MathMixin):
    def __init__(self, data):
        self.data = data  # Instance variable to hold a list of numbers

    def compute_sum(self):
       # Computes the sum of the data using the add_numbers method.
        return self.add_numbers(*self.data)


# Example usage:
data = [10, 20, 30, 40, 50]
stats = Statistics(data)

print("Data:", stats.data)
print("Sum of data:", stats.compute_sum())


