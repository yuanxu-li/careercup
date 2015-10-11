# 4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
# a binary search tree with minimal height

class Node:
	def __init__(self, value):
		self.set_left(None)
		self.set_right(None)
		self.value = value

	def set_left(self, left):
		self.left = left

	def set_right(self, right):
		self.right = right

	@staticmethod
	def bst_generate(array):
		""" pick the median number of an array, use it as the root, and recursively return its left child and right child
		>>> root = Node.bst_generate([0,1,2,3,4,5,6,7,8,9])
		>>> root.value
		5
		>>> root.right.value
		8
		>>> root.left.value
		2
		"""
		# base case
		if len(array) == 0:
			return None
		elif len(array) == 1:	# unnecessary, but could reduce one level of recursion
			return Node(array[0])
		# recursive case
		middle = int(len(array) / 2)
		median_node = Node(array[middle])
		median_node.set_left(Node.bst_generate(array[:middle]))
		median_node.set_right(Node.bst_generate(array[middle+1:]))
		return median_node

if __name__ == "__main__":
	import doctest
	doctest.testmod()