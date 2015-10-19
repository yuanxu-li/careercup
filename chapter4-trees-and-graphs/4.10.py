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
		time complexity: O(n+m), which is the time to construct the preorders but occupies too much space
		for the two trees are too large
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

	def contained_in(self, node):
		"""
		time complexity: O(n+km), where k is the number of occurences of T2's root in T1
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
		>>> n1.contained_in(n0)
		True
		>>> a = Node(1)
		>>> b = Node(2)
		>>> c = Node(3)
		>>> a.set_left(b)
		>>> a.set_right(c)
		>>> a.contained_in(n0)
		False
		"""
		if self.match(node):
			return True
		else:
			if node.left is None and node.right is None:
				return False
			elif node.left is None:
				return self.contained_in(node.right)
			elif node.right is None:
				return self.contained_in(node.left)
			else:
				return self.contained_in(node.left) or self.contained_in(node.right)


	def match(self, node):
		""" if the root matches then continue comparing their offsprings. Once there is a pair of unmatched offsprings,
		returns False
		"""
		# if the value of the two roots are different, there is no need to compare their offsprings. Simply return False
		if self.value != node.value:
			return False
		
		# both of their children are empty
		if self.left == node.left == None and self.right == node.right == None:
			return True
		elif self.left == node.left == None and self.right != None and node.right != None:
			return self.right.match(node.right)
		elif self.right == node.right == None and self.left != None and node.left != None:
			return self.left.match(node.left)
		elif self.left != None and self.right != None and node.left != None and node.right != None:
			return self.left.match(node.left) and self.right.match(node.right)

		# the structure of the two trees are different
		return False




if __name__ == "__main__":
	import doctest
	doctest.testmod()