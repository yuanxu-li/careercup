# 4.6 Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node
# in a binary search tree. You may assume that each node has a link to its parent.

class Node:
	def __init__(self, value=0):
		self.left = None
		self.right = None
		self.parent = None
		self.value = value

	def set_left(self, left):
		self.left = left
		left.set_parent(self)

	def set_right(self, right):
		self.right = right
		right.set_parent(self)

	def set_parent(self, parent):
		self.parent = parent

	def successor(self):
		"""
		Iterative solution. If the right child is None, return its parent; if the right child is not None, return the leftmost
		offspring of the right child
		>>> n0 = Node(8)
		>>> n1 = Node(6)
		>>> n2 = Node(9)
		>>> n3 = Node(3)
		>>> n4 = Node(7)
		>>> n5 = Node(8)
		>>> n6 = Node(10)
		>>> n7 = Node(2)
		>>> n0.set_left(n1)
		>>> n0.set_right(n2)
		>>> n1.set_left(n3)
		>>> n1.set_right(n4)
		>>> n2.set_left(n5)
		>>> n2.set_right(n6)
		>>> n3.set_left(n7)
		>>> n0.successor().value
		8
		>>> n3.successor().value
		6
		"""
		if self.right is None:
			node = self
			while node.parent is not None and node == node.parent.right:
				node = node.parent
			return node.parent
		else:
			node = self.right
			while node.left is not None:
				node = node.left
			return node

if __name__ == "__main__":
	import doctest
	doctest.testmod()