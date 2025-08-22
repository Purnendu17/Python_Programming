from itertools import permutations
def print_permutations(s, length):
    perms = permutations(s, length)
    for perm in perms:
        print(''.join(perm))
input_string = "abc"
length = 2
print_permutations(input_string, length)
