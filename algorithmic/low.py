def to_lowercase_divide_conquer(s):
    # Base case: if the string is empty or a single character
    if len(s) == 0:
        return ""
    if len(s) == 1:
        # Check if the character is uppercase and convert to lowercase
        if 'A' <= s <= 'Z':
            print(f"Converting {s} to {s.lower()}")
            return s.lower()
        else:
            print(f"{s} is already lowercase")
            return s

    # Divide the string into two halves
    mid = len(s) // 2
    left = to_lowercase_divide_conquer(s[:mid])
    right = to_lowercase_divide_conquer(s[mid:])

    # Conquer: combine the results
    return left + right

# Test the function
test_string = "AVanIguPTa"
result = to_lowercase_divide_conquer(test_string)
print(f"Original: {test_string}")
print(f"Converted: {result}")
