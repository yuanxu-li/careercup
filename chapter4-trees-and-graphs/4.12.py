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
		time complexity: O(nlogn), for every node has been visited once
		and the number of possible paths ending in each node is proportional
		to the depth that is logn.
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
		>>> n0.num_of_paths([], 8)
		1
		"""
		this_num = 0
		this_sum = 0
		array = array.copy()
		array.append(self.value)
		# pdb.set_trace()
		for i in reversed(range(len(array))):
			this_sum += array[i]
			if this_sum == value:
				this_num += 1
		if self.left is not None:
			this_num += self.left.num_of_paths(array, value)
		if self.right is not None:
			this_num += self.right.num_of_paths(array, value)
		# pdb.set_trace()
		return this_num

	def count_paths(self, target, running=None, path_count=None):
		"""
		We only traverse each node once, but keep all the old states in a dictionary called path_count and pass it along.
		Each time we come to a new node, we update the dictionary and search the dictionary to see how many times the desired
		sum is stored, which is the number of paths for this node. We recursively apply this approach to its offsprings.
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
		>>> n0.count_paths(8)
		1
		>>> n0.count_paths(9)
		2
		"""
		# initilization from the root
		if running is None or path_count is None:
			path_count = {}
			path_count[0] = 1
			return self.count_paths(target, 0, path_count)
		# process among offsprings
		else:
			total_paths = 0
			running += self.value
			possible_sum = running - target
			if running in path_count:
				path_count[running] += 1
			else:
				path_count[running] = 1
			# pdb.set_trace()
			if possible_sum in path_count:
				total_paths += path_count[possible_sum]
			if self.left is not None:
				total_paths += self.left.count_paths(target, running, path_count)
			if self.right is not None:
				total_paths += self.right.count_paths(target, running, path_count)
			# when we leave this node, we reset the path_count to counter the effect by this node
			if running in path_count:
				path_count[running] -= 1
			return total_paths






if __name__ == "__main__":
	import doctest
	doctest.testmod()