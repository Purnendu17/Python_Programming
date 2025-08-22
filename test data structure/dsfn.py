import random

class CustomStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        print(f"Pushed {val} onto the stack.")

    def pop(self):
        if not self.stack:
            print("Stack is empty. Nothing to pop.")
            return None
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        print(f"Popped {val} from the stack.")
        return val

    def getRandom(self):
        if not self.stack:
            print("Stack is empty. No random element.")
            return None
        random_val = random.choice(self.stack)
        print(f"Random element selected: {random_val}")
        return random_val

    def getMinimum(self):
        if not self.min_stack:
            print("Stack is empty. No minimum element.")
            return None
        min_val = self.min_stack[-1]
        print(f"Current minimum element: {min_val}")
        return min_val

# Example Usage
stack = CustomStack()
stack.push(5)
stack.push(2)
stack.push(8)
stack.push(1)
stack.getMinimum()
stack.getRandom()
stack.pop()
stack.getMinimum()