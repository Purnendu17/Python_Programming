class TwoStacks:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size  # Initially, the list is filled with 0s
        self.top1 = -1  # Top for Stack 1
        self.top2 = size  # Top for Stack 2

    def push1(self, value):
        """Push element onto first stack"""
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = value
            return self.arr  # Return current list state
        else:
            raise OverflowError("Stack 1 Overflow")

    def push2(self, value):
        """Push element onto second stack"""
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = value
            return self.arr  # Return current list state
        else:
            raise OverflowError("Stack 2 Overflow")

    def pop1(self):
        """Pop element from first stack"""
        if self.top1 >= 0:
            value = self.arr[self.top1]
            self.arr[self.top1] = 0  # Reset to 0 after popping
            self.top1 -= 1
            return value, self.arr  # Return popped value and current list state
        else:
            raise IndexError("Stack 1 Underflow")

    def pop2(self):
        """Pop element from second stack"""
        if self.top2 < self.size:
            value = self.arr[self.top2]
            self.arr[self.top2] = 0  # Reset to 0 after popping
            self.top2 += 1
            return value, self.arr  # Return popped value and current list state
        else:
            raise IndexError("Stack 2 Underflow")

# Example Usage
ts = TwoStacks(5)  # List size = 5
print(ts.arr)  # Initial state: [0, 0, 0, 0, 0]

print(ts.push1(3))  # Stack 1: [3, 0, 0, 0, 0]
print(ts.push2(9))  # Stack 2: [3, 0, 0, 0, 9]
print(ts.push1(5))  # Stack 1: [3, 5, 0, 0, 9]

popped_value, current_list = ts.pop1()
print(f"Popped: {popped_value}, Current List: {current_list}")  # Output: Popped 5, List: [3, 0, 0, 0, 9]
