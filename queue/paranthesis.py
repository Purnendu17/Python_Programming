def check_and_correct_parentheses(s):
    stack = []
    position_stack = []  # To track positions of unmatched parentheses
    pairs = {')': '(', '}': '{', ']': '['}
    
    errors = []
    
    for i, char in enumerate(s):
        if char in "({[":
            stack.append(char)
            position_stack.append(i)
        elif char in ")}]":
            if stack and stack[-1] == pairs[char]:  # Matching case
                stack.pop()
                position_stack.pop()
            else:
                errors.append((i, f"Error: '{char}' at position {i} has no matching '{pairs[char]}'"))
    
    # Check for unmatched opening brackets
    while stack:
        unmatched_pos = position_stack.pop()
        errors.append((unmatched_pos, f"Error: '{stack.pop()}' at position {unmatched_pos} has no closing match"))

    # If errors exist, correct the string
    if errors:
        print("Errors found:")
        for _, error in sorted(errors):
            print(error)

        # Correcting the string by removing unmatched brackets
        corrected_s = list(s)
        for pos, _ in sorted(errors, reverse=True):
            corrected_s.pop(pos)

        return "".join(corrected_s)

    return s  # If valid, return as it is

# Example usage
s = input("Enter a string with parentheses: ")
result = check_and_correct_parentheses(s)
