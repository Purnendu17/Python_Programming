class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list

    # Append a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Insert a node at a specific index
    def insert_at_index(self, index, data):
        new_node = Node(data)

        if index == 0:  # Insert at head
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0

        while current is not None and count < index - 1:  # Traverse to (index-1)th node
            current = current.next
            count += 1

        if current is None:  # If index is out of range
            print(f"Index {index} out of bounds")
            return

        # Insert node at index
        new_node.next = current.next
        current.next = new_node

    # Print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage
ll = LinkedList()

# Adding 7 elements
for num in [10, 20, 30, 40, 50, 60, 70]:
    ll.append(num)

print("Linked List before insertion:")
ll.print_list()

# Insert element at index 5 (6th position in 0-based index)
ll.insert_at_index(5, 99)

print("Linked List after inserting 99 at index 5:")
ll.print_list()
