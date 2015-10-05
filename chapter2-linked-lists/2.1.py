# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
# How would you solve this problem if a temporary buffer is not allowed?
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	def __str__(self):
		return str(self.content)

class LinkedList:
	def __init__(self, head=None):
		self.head = head
	def insert(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

def remove_dups(l):
	""" remove duplicates from a doubly linked list, which is represented as a deque
	>>> remove_dups([2,2,1,6,1,4,2,6])
	[2, 1, 6, 4]
	>>> remove_dups(deque())
	deque([])
	"""
	ll = LinkedList()
	for i in range(len(l) - 1, -1, -1):
		ll.insert(l[i])
	
	