def merge_sorted_lists(num1, num2):
    """Merges two sorted lists into one sorted list."""
    i, j = 0, 0
    merged = []
    
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            merged.append(num1[i])
            i += 1
        else:
            merged.append(num2[j])
            j += 1

    # Add remaining elements
    merged.extend(num1[i:])
    merged.extend(num2[j:])

    return merged

# Taking input from user
m = int(input("Enter size of first list (m): "))
n = int(input("Enter size of second list (n): "))

num1 = list(map(int, input(f"Enter {m} sorted numbers for first list: ").split()))
num2 = list(map(int, input(f"Enter {n} sorted numbers for second list: ").split()))

# Ensure input lists are sorted (optional check)
assert num1 == sorted(num1), "First list is not sorted!"
assert num2 == sorted(num2), "Second list is not sorted!"

# Merging the lists
merged_list = merge_sorted_lists(num1, num2)

print("Merged Sorted List:", merged_list)
