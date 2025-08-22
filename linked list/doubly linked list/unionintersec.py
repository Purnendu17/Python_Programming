class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

def get_union(head1, head2):
    elements = set()
    union_list = LinkedList()
    
    temp = head1
    while temp:
        elements.add(temp.data)
        temp = temp.next
    
    temp = head2
    while temp:
        elements.add(temp.data)
        temp = temp.next
    
    for item in elements:
        union_list.append(item)
    
    return union_list

def get_intersection(head1, head2):
    elements1 = set()
    elements2 = set()
    intersection_list = LinkedList()
    
    temp = head1
    while temp:
        elements1.add(temp.data)
        temp = temp.next
    
    temp = head2
    while temp:
        elements2.add(temp.data)
        temp = temp.next
    
    common_elements = elements1.intersection(elements2)
    for item in common_elements:
        intersection_list.append(item)
    
    return intersection_list

# Example usage:
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)

list2 = LinkedList()
list2.append(3)
list2.append(4)
list2.append(5)
list2.append(6)

print("List 1:")
list1.print_list()
print("List 2:")
list2.print_list()

union_result = get_union(list1.head, list2.head)
print("Union:")
union_result.print_list()

intersection_result = get_intersection(list1.head, list2.head)
print("Intersection:")
intersection_result.print_list()
