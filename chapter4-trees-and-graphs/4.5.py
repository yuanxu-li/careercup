# 4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree

class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value
	def set_left(self, left):
		self.left = left
	def set_right(self, right):
		self.right = right

	def is_bst(self, min=None, max=None):
		""" by passing down max and min each level down, we check if each subtree is a bst
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
		>>> n0.is_bst()
		True
		"""
		if (min is not None and self.value < min) or (max is not None and self.value > max):
			return False
		if self.left is None and self.right is None:
			return True
		elif self.left is None:
			return self.right.is_bst(self.value, max)
		elif self.right is None:
			return self.left.is_bst(min, self.value)
		else:
			return self.left.is_bst(min, self.value) and self.right.is_bst(self.value, max)


if __name__ == "__main__":
	import doctest
	doctest.testmod()