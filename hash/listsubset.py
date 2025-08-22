# Input lists from user
l1 = input("Enter elements of list l1 separated by spaces: ").split()
l2 = input("Enter elements of list l2 separated by spaces: ").split()

# Convert l1 into a hash set
hash_set = set(l1)

# Check if all elements of l2 are in the hash_set
is_subset = all(elem in hash_set for elem in l2)

# Output the result
if is_subset:
    print("l2 is a subset of l1")
else:
    print("l2 is not a subset of l1")
