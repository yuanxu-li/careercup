# 4.10 Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm
# to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is,
# if you cut off the tree at node n, the two trees would be identical.

class Node:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

	def set_left(self, left):
		self.left = left

	def set_right(self, right):
		self.right = right

	def preorder(self):
		if self.left is None and self.right is None:
			yield self.value
			yield None
			yield None
		elif self.left is None:
			yield None
			yield self.value
			for value in self.right.preorder():
				yield value
		elif self.right is None:
			yield self.value
			for value in self.left.preorder():
				yield value
			yield None
		else:
			yield self.value
			for value in self.left.preorder():
				yield value
			for value in self.right.preorder():
				yield value

	def inorder(self):
		if self.left is None and self.right is None:
			yield None
			yield self.value
			yield None
		elif self.left is None:
			yield self.value
			yield None
			for value in self.right.inorder():
				yield value
		elif self.right is None:
			for value in self.left.inorder():
				yield value
			yield self.value
			yield None
		else:
			for value in self.left.inorder():
				yield value
			yield self.value
			for value in self.right.inorder():
				yield value

	def is_subtree_of(self, node):
		""" if a tree has the same preorder traversal as a part of another tree, it is a subtree of the second tree
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
		>>> n1.is_subtree_of(n0)
		True
		>>> a = Node(1)
		>>> b = Node(2)
		>>> c = Node(3)
		>>> a.set_left(b)
		>>> a.set_right(c)
		>>> a.is_subtree_of(n0)
		False
		"""
		return ''.join(map(str, self.preorder())) in ''.join(map(str, node.preorder()))

if __name__ == "__main__":
	import doctest
	doctest.testmod()