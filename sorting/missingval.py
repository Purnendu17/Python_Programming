def find_missing_value(lst):
    # Find the expected sum of numbers from the minimum to the maximum value
    expected_sum = sum(range(lst[0], lst[-1] + 1))
    
    # Find the actual sum of the list
    actual_sum = sum(lst)
    
    # The missing number will be the difference between expected and actual sums
    missing_value = expected_sum - actual_sum
    
    return missing_value

# Example usage
lst = [1, 2, 3, 4, 6, 7, 8, 9, 10]
missing = find_missing_value(lst)
print(f"The missing value is {missing}")
