# 4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
# Avoid storing aditinoal nodes in a data structure. NOTE: This is not necessarily a binary search tree.

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

	def set_left(self, left):
		self.left = left
		left.set_parent(self)

	def set_right(self, right):
		self.right = right
		right.set_parent(self)

	def set_parent(self, parent):
		self.parent = parent

	def depth(self):
		depth = 0
		node = self
		while node.parent is not None:
			node = node.parent
			depth += 1
		return depth

	@staticmethod
	def find_common_ancestor(node1, node2):
		"""
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
		>>> Node.find_common_ancestor(n7, n6).value
		8
		>>> print(Node.find_common_ancestor(n7, Node(1)))
		None
		"""
		depth1 = node1.depth()
		depth2 = node2.depth()
		if depth1 > depth2:
			for i in range(depth1 - depth2):
				node1 = node1.parent
		else:
			for i in range(depth2 - depth1):
				node2 = node2.parent

		while node1 is not None and node2 is not None and node1 != node2:
			node1 = node1.parent
			node2 = node2.parent

		# node1 and node2 are in two different trees
		if node1 is None or node2 is None:
			return None
		else:
			return node1

if __name__ == "__main__":
	import doctest
	doctest.testmod()