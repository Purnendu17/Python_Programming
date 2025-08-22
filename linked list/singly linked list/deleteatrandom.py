class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds a new node with the given data at the end of the list."""
        if not self.head:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def delete_value(self, value):
        """Deletes the first occurrence of value from the linked list."""
        if not self.head:
            print(False)
            return
        
        # If head node itself holds the value to be deleted
        if self.head.data == value:
            self.head = self.head.next
            self.print_list()
            return True
        
        temp = self.head
        prev = None
        
        # Search for the value in the list
        while temp and temp.data != value:
            prev = temp
            temp = temp.next
        
        # If value was not found
        if not temp:
            print(False)
            return
        
        # Unlink the node from the linked list
        prev.next = temp.next
        
        # Print the modified list
        self.print_list()
        print(True)
        return True

    def print_list(self):
        """Prints the linked list."""
        temp = self.head
        result = []
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(result) if result else "Empty List")

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

print("Original List:")
ll.print_list()

# Deleting value 3 (exists in the list)
print("Deleting 3:")
ll.delete_value(3)

# Trying to delete value 5 (not in the list)
print("Deleting 5:")
ll.delete_value(5)
