class ListProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def remove_even(self):
        """Removes even numbers from the list."""
        self.numbers = [x for x in self.numbers if x % 2 != 0]

    def get_list(self):
        """Returns the processed list."""
        return self.numbers

# Example usage:
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processor = ListProcessor(lst)
processor.remove_even()
print(processor.get_list())  

