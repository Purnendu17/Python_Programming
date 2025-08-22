
import ctypes
class Node:
	def __init__(self, value):
		self.value = value
		self.npx = 0
		
class XorLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.__nodes = []
	
	def insert(self, value):
		
		# Initialize a new Node
		node = Node(value)
		
		# Check If XOR linked list is empty
		if self.head is None:
			self.head = node
			self.tail = node
		
		else:
			self.head.npx = id(node) ^ self.head.npx
			node.npx = id(self.head)
			self.head = node
		self.__nodes.append(node)
		
# Function to print elements of the XOR Linked List
	def printList(self):
		
		if self.head != None:
			prev_id = 0
			node = self.head
			next_id = 1
			print(node.value, end=' ')
			
			# Traverse XOR linked list
			while next_id:
				next_id = prev_id ^ node.npx
				
				if next_id:
					prev_id = id(node)
					node = self.__type_cast(next_id)
					print(node.value, end=' ')
				else:
					return
				
	def isEmpty(self):
		if self.head is None:
			return True
		return False
	
	# method to return a new instance of type
	def __type_cast(self, id):
		return ctypes.cast(id, ctypes.py_object).value
	
	
	# Function to reverse the XOR linked list
	def reverse(self):

		if self.head != None:
			prev_id = 0
			node = self.tail
			next_id = 1
			
			print(node.value, end=' ')
			
			while next_id:
				# Forward traversal
				next_id = prev_id ^ node.npx
				if next_id:
					prev_id = id(node)
					node = self.__type_cast(next_id)
					print(node.value, end=' ')
				else:
					return
					
head = XorLinkedList()
head.insert(10)
head.insert(20)
head.insert(30)
head.insert(40)
print("XOR linked list: ", end = "")
head.printList()

print()
print("Reversed XOR linked list: ", end = "")
head.reverse()

