class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def find_height(root):
    if root is None:
        return -1  # height of empty tree is -1 (or 0 if you count nodes instead of edges)
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return 1 + max(left_height, right_height)

# Create BST
root = None
for key in [20, 10, 5, 15, 30, 25, 35]:
    root = insert(root, key)

# Find height
print("Height of BST:", find_height(root))
