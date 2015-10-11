# 4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree

class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

	def is_bst(self):
		"""
		Recursive solution. For a tree to be BST, the left subtree and the right subtree have to be BST's, and the value of the root
		must be >= the largest value of the left subtree and <= the smallest value of the right subtree
		>>> n0 = Node(8)
		>>> n1 = Node(6)
		>>> n2 = Node(9)
		>>> n3 = Node(3)
		>>> n4 = Node(7)
		>>> n5 = Node(7)
		>>> n6 = Node(10)
		>>> n7 = Node(2)
		>>> n0.left = n1
		>>> n0.right = n2
		>>> n1.left = n3
		>>> n1.right = n4
		>>> n2.left = n5
		>>> n2.right = n6
		>>> n3.left = n7
		>>> n1.is_bst()
		True
		>>> n2.is_bst()
		True
		>>> n0.is_bst()
		False
		"""
		if self.left is None and self.right is None:
			return True
		elif self.left is None:
			return self.value <= self.right.min_bst() and self.right.is_bst()
		elif self.right is None:
			return self.value >= self.left.max_bst() and self.left.is_bst()
		else:
			return self.value <= self.right.min_bst()\
				and self.value >= self.left.max_bst()\
				and self.left.is_bst()\
				and self.right.is_bst()

	def min_bst(self):
		if self.left:
			return self.left.min_bst()
		else:
			return self.value

	def max_bst(self):
		if self.right:
			return self.right.max_bst()
		else:
			return self.value

if __name__ == "__main__":
	import doctest
	doctest.testmod()