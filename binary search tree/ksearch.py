class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert key and keep track of parents
def insert_with_parents(root, key):
    if not root:
        return Node(key), None, []

    current = root
    parent = None
    path = []  # To store (node, direction) along the way

    while True:
        path.append(current)
        parent = current

        if key < current.data:
            if current.left:
                current = current.left
            else:
                current.left = Node(key)
                path.append(current.left)
                return root, current.left, path
        else:
            if current.right:
                current = current.right
            else:
                current.right = Node(key)
                path.append(current.right)
                return root, current.right, path

# Find ancestors with same value as key from the path
def find_same_value_ancestors(path, key):
    return [node.data for node in path[:-1] if node.data == key]

# Pretty print the path visually
def print_path(path):
    print("\n Traversal Path from Root to Inserted Node:")
    for i, node in enumerate(path):
        connector = " |__ " if i != len(path) - 1 else " (Inserted)"
        print(f"{'    '*i}{node.data}{connector}")

# --- Example usage ---

# Build BST
root = Node(20)
insert_with_parents(root, 10)
insert_with_parents(root, 30)
insert_with_parents(root, 20)  # Duplicate
insert_with_parents(root, 20)  # Another duplicate

# Insert target key and get path
key = 20
root, inserted_node, path = insert_with_parents(root, key)

# Print path
print_path(path)

# Find and print ancestors with same value
same_val_ancestors = find_same_value_ancestors(path, key)
print("\n Ancestors with same value as", key, ":", same_val_ancestors)
