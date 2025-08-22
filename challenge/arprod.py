def product_except_self(nums):
    n = len(nums)
    result = [1] * n  # Initialize the result array with 1

    # Compute prefix product
    prefix = 1
    for i in range(n):
        result[i] = prefix  # Store prefix product in result
        prefix *= nums[i]   # Update prefix for next iteration

    # Compute suffix product and update result
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix  # Multiply suffix with the stored prefix product
        suffix *= nums[i]    # Update suffix for next iteration

    return result

# Example usage:
nums = [1, 2, 3, 4]
print(product_except_self(nums))  
