# 4.12 Paths with Sum: You are given a binary tree in which each node contains an integer value
# (which might be positive or negative). Design an algorithm to count the number of paths that
# sum to a given value. The path does not need to start or end at the root or a leaf, but it
# must go downwards (traveling only from parent nodes to child nodes).

import pdb

class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

	def set_left(self, left):
		self.left = left

	def set_right(self, right):
		self.right = right

	def num_of_paths(self, array, value):
		"""
		>>> n0 = Node(8)
		>>> n1 = Node(6)
		>>> n2 = Node(10)
		>>> n3 = Node(3)
		>>> n4 = Node(7)
		>>> n5 = Node(9)
		>>> n6 = Node(11)
		>>> n7 = Node(2)
		>>> n0.set_left(n1)
		>>> n0.set_right(n2)
		>>> n1.set_left(n3)
		>>> n1.set_right(n4)
		>>> n2.set_left(n5)
		>>> n2.set_right(n6)
		>>> n3.set_left(n7)
		>>> n0.num_of_paths([], 9)
		2
		"""
		this_num = 0
		this_sum = 0
		array = array.copy()
		array.append(self.value)
		for i in reversed(range(len(array))):
			this_sum += array[i]
			if this_sum == value:
				this_num += 1
		if self.left is not None:
			this_num += self.left.num_of_paths(array, value)
		if self.right is not None:
			this_num += self.right.num_of_paths(array, value)
		return this_num

if __name__ == "__main__":
	import doctest
	doctest.testmod()