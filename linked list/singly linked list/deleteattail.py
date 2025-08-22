class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list

    # Append a node at the end
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Set the new node as the next of last node

    # Delete node at tail (last node)
    def delete_at_tail(self):
        if not self.head:  # If the list is empty
            print("List is empty. Nothing to delete.")
            return

        if not self.head.next:  # If there is only one node
            self.head = None  # Remove the only node
            return

        second_last = self.head
        while second_last.next.next:  # Traverse to the second last node
            second_last = second_last.next
        second_last.next = None  # Remove the last node

    # Print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate end of the list

# Example Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

print("Linked List before deletion:")
ll.print_list()

ll.delete_at_tail()

print("Linked List after deletion at tail:")
ll.print_list()
