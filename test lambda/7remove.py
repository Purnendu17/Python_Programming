def remove_odd_index_chars(s):
    return s[::2] 
input_string = "abcdef"
result = remove_odd_index_chars(input_string)
print(f"String after removing characters with odd index values: '{result}'")
