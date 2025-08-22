def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find middle index
        
        if arr[mid] == target:
            return mid  # Found target at mid index
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
            
    return -1  # Target not found

# Taking user input
arr = list(map(int, input("Enter sorted numbers (space-separated): ").split()))
target = int(input("Enter the number to search for: "))

# Searching for the target
index = binary_search(arr, target)

# Printing the result
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")
