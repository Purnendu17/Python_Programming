class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Adds a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def search(self, value):
        """Searches for a value in the doubly linked list and prints True if found, otherwise False."""
        temp = self.head
        while temp:
            if temp.data == value:
                print(True)
                return
            temp = temp.next
        print(False)

# Example usage
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

# Searching for values
dll.search(3)  
dll.search(5)  
