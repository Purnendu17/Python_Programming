class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def reverse_between(head, m, n):
    currNode = head
    prevNode = None
    i = 1

    # Move currNode to the position m
    while i < m:
        prevNode = currNode
        currNode = currNode.next
        i += 1

    # Store pointers to the start and end of the reversed segment
    revHead = currNode
    revTail = None

    # Reverse the linked list from position m to n
    while i <= n:
        nextNode = currNode.next
        currNode.next = revTail
        revTail = currNode
        currNode = nextNode
        i += 1

    # Connect the reversed segment back to the list
    if prevNode is not None:
        prevNode.next = revTail
    else:
        head = revTail
    revHead.next = currNode

    return head


def print_list(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print("NULL")


if __name__ == "__main__":
  
    # Initialize linked list
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
    head.next.next.next.next.next.next = Node(70)

    print("Original list: ", end="")
    print_list(head)

    head = reverse_between(head, 3, 6)

    print("Modified list: ", end="")
    print_list(head)
