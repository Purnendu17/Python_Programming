def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Found target, return index
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    return -1  # Not found

# Given list of 11 numbers (unsorted)
numbers = [12, 5, 8, 15, 3, 10, 1, 7, 9, 6, 4]
target = 7  # Number to search

# Step 1: Sort the list
sorted_numbers = merge_sort(numbers)
print("Sorted List:", sorted_numbers)

# Step 2: Search for the target
index = binary_search(sorted_numbers, target)

# Output result
if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found.")
