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

    def search(self, value):
        """Searches for a value in the linked list and prints True if found, otherwise False."""
        temp = self.head
        while temp:
            if temp.data == value:
                print(True)
                return
            temp = temp.next
        print(False)

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

# Searching for values
ll.search(3) 
ll.search(5) 
