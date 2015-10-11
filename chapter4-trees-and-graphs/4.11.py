# 4.11 Random Node: You are implementing a binary tree class from scratch which, in addition ot insert, find,
# and delete, has a method getRandomNode() which returns a random node from the tree. All nodes shoudl be equally
# likely to be chosen. Design and implement an algorithm for get RandomNode, and explain how you would implement the
# rest of the methods.

import random
import pdb

class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value
		self.size = None

	def set_left(self, left):
		self.left = left

	def set_right(self, right):
		self.right = right

	def get_random_node(self):
		"""
		1. get the size of the tree, n
		2. get a random integer k between [0, n)
		3. recursively inorder traverse the left subtree or the right subtree according to k
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
		>>> n0.count_size()
		8
		>>> n0.get_kth_node(n0.left.count_size()).value
		8
		>>> n0.get_kth_node(0).value
		2
		>>> n0.get_kth_node(1).value
		3
		"""
		n = self.count_size()
		k = random.randrange(n)
		return self.get_kth_node(k)

	def get_kth_node(self, k):
		""" get the kth node (inorder traversal)
		"""
		if k < 0:
			raise Exception("k < 0")

		if self.left is None:
			if k == 0:
				return self
			else:
				return self.right.get_kth_node(k-1)
		else:
			if k < self.left.count_size():
				return self.left.get_kth_node(k)
			elif k == self.left.count_size():
				return self
			else:
				return self.right.get_kth_node(k-self.left.count_size())

	def count_size(self):
		""" calculate the size of the subtree rooted in this node
		"""
		# if the size has been calculated before, return it directly
		if self.size is None:
			if self.left is None and self.right is None:
				self.size = 1
			elif self.left is None:
				self.size = 1 + self.right.count_size()
			elif self.right is None:
				self.size = 1 + self.left.count_size()
			else:
				self.size = 1 + self.left.count_size() + self.right.count_size()
		return self.size

if __name__ == "__main__":
	import doctest
	doctest.testmod()