# 10.10 Rank from Stream: Imagine you are reading in a stream of integers.
# Periodically, you wish to be able to look up the rank of a number x
# (the number of values less than or equal to x). Implement the data structures
# and algorithms to support these operations. That is, implement the method
# track(int x), which is called when each number is generated, and the method
# getRankOfNumber(int x), which returns the number of values less than
# or equal to x (not including itself).
# EXAMPLE
# Stream(in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
# getRankOfNumber(1) = 0
# getRankOfNumber(3) = 1
# getRankOfNumber(4) = 3

import pdb

class Node:
	"""
	Node can represent a tree node or a tree rooted in this node.
	When inserting nodes into a tree, we also record the size of a tree in
	its root.
	>>> tree = Node(5)
	>>> tree.insert(1)
	>>> tree.insert(4)
	>>> tree.insert(4)
	>>> tree.insert(5)
	>>> tree.insert(9)
	>>> tree.insert(7)
	>>> tree.insert(13)
	>>> tree.insert(3)
	>>> tree.get_rank(1)
	0
	>>> tree.get_rank(3)
	1
	>>> tree.get_rank(4)
	3
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.left_size = 0

	def insert(self, value):
		# left branch
		if value <= self.value:
			self.left_size += 1
			if self.left is None:
				self.left = Node(value)
			else:
				self.left.insert(value)
		# right branch
		else:
			if self.right is None:
				self.right = Node(value)
			else:
				self.right.insert(value)

	def get_rank(self, value):
		# this node
		if value == self.value:
			return self.left_size
		# left branch
		elif value < self.value:
			if self.left is None:
				return -1
			else:
				return self.left.get_rank(value)
		# right branch
		else:
			if self.right is None:
				return -1
			else:
				right_rank = self.right.get_rank(value)
				if right_rank != -1:
					# pdb.set_trace()
					return self.left_size + 1 + right_rank
				else:
					return -1


if __name__ == "__main__":
	import doctest
	doctest.testmod()
