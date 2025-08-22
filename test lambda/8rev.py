def reverse_if_multiple_of_four(s):
    if len(s) % 4 == 0:
        return s[::-1]  
    return s  
input_string = "abcdefgh"
result = reverse_if_multiple_of_four(input_string)
print(f"Result: '{result}'")
