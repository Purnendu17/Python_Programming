def describe(arg):
    if isinstance(arg, str):
        print(f"The string '{arg}' has {len(arg)} characters.")
    elif isinstance(arg, list):
         print(f"The list {arg} has {len(arg)} elements, and their sum is {sum(arg)}.")
    elif isinstance(arg, int):
         print(f"The number {arg} doubled is {arg * 2}.")
    else:
         print("Unsupported type!")

# Testing
print(describe("Avani"))     # String input
print(describe([1, 2, 3]))   # List input
print(describe(42))          # Integer input
print(describe(None))        # Unsupported type

