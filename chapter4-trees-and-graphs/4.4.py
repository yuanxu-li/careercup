# 4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question,
# a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

class Node:
	def __init__(self):
		self.left = None
		self.right = None

	def check_height(self):
		if self.left is None and self.right is None:
			return 0
		elif self.left is None:
			right_height = self.right.check_height()
			if right_height != 0:
				return -1
			else:
				return 1
		elif self.right is None:
			left_height = self.left.check_height()
			if left_height != 0:
				return -1
			else:
				return 1
		else:
			left_height = self.left.check_height()
			right_height = self.right.check_height()
			if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
				return -1
			else:
				return 1 + max(left_height, right_height)

	def is_balanced(self):
		"""
		recursive solution. compare the height of its left subtree and right subtree
		>>> n0 = Node()
		>>> n1 = Node()
		>>> n2 = Node()
		>>> n3 = Node()
		>>> n4 = Node()
		>>> n5 = Node()
		>>> n6 = Node()
		>>> n7 = Node()
		>>> n0.left = n1
		>>> n0.right = n2
		>>> n1.left = n3
		>>> n1.right = n4
		>>> n2.left = n5
		>>> n2.right = n6
		>>> n3.left = n7
		>>> n0.is_balanced()
		True
		>>> n8 = Node()
		>>> n7.right = n8
		>>> n0.is_balanced()
		False
		"""
		if self.check_height() != -1:
			return True
		else:
			return False

if __name__ == "__main__":
	import doctest
	doctest.testmod()