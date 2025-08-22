def pascal_recursive(row, col):
    # Base cases: First and last elements in each row are 1
    if col == 0 or col == row:
        return 1
    # Recursive case: Sum of the two numbers above
    return pascal_recursive(row-1, col-1) + pascal_recursive(row-1, col)

# Function to generate full Pascal's Triangle
def generate_pascals_triangle(n):
    triangle = []
    for row in range(n):
        current_row = [pascal_recursive(row, col) for col in range(row+1)]
        triangle.append(current_row)
    return triangle

# Function to perform Binary Search on a given row of the Pascal's Triangle
def binary_search(row, target):
    left, right = 0, len(row) - 1
    while left <= right:
        mid = (left + right) // 2
        if row[mid] == target:
            return mid  # Found the target
        elif row[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    return -1  # Target not found

# Example to generate Pascal's Triangle for 5 rows and search for a target
n = 5
target = 6

# Step 1: Generate Pascal's Triangle
pascals_triangle = generate_pascals_triangle(n)

# Step 2: Search for the target in the 4th row (index 3)
row_to_search = pascals_triangle[3]
index = binary_search(row_to_search, target)

# Print the result
if index != -1:
    print(f"Element {target} found at index {index} in row {row_to_search}.")
else:
    print(f"Element {target} not found in the row.")
