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
		self.parent = None
		self.value = value
		self.size = 1

	def set_left(self, left):
		self.left = left
		if left is not None:
			left.parent = self

	def set_right(self, right):
		self.right = right
		if right is not None:
			right.parent = self

class Tree:
	def __init__(self):
		self.root = None

	def _insert(self, value, node):
		node.size += 1
		if value < node.value:
			if node.left is None:
				node.left = Node(value)
				node.left.parent = node
			else:
				self._insert(value, node.left)
		else:
			if node.right is None:
				node.right = Node(value)
				node.right.parent = node
			else:
				self._insert(value, node.right)

	def insert(self, value):
		if self.root is None:
			self.root = Node(value)
		else:
			self._insert(value, self.root)

	def _find(self, value, node):
		if value == node.value:
			return node
		elif value < node.value and node.left is not None:
			self._find(value, node.left)
		elif value > node.value and node.right is not None:
			self._find(value, node.right)
		else:
			return None

	def find(self, value):
		if self.root is not None:
			return self._find(value, self.root)
		else:
			return None

	def _delete(self, value, node):
		node.size -= 1
		# node in left subtree
		if node.value < value:
			if node.left is not None:
				return self._delete(value, node.left)
			else:
				return None
		# node in right subtree
		elif node.value > value:
			if node.right is not None:
				return self._delete(value, node.right)
			else:
				return None
		# node found
		else:
			# if there are no children
			if node.left is None and node.right is None:
				if node == node.parent.left:
					node.parent.set_left(None)
				else:
					node.parent.set_right(None)
			# if there is only a left child
			elif node.left is not None and node.right is None:
				if node == node.parent.left:
					node.parent.set_left(node.left)
				else:
					node.parent.set_right(node.left)
			# if there is only a right child
			elif node.left is None and node.right is not None:
				if node == node.parent.left:
					node.parent.set_left(node.right)
				else:
					node.parent.set_right(node.right)
			# if there are both left and right children
			else:
				# find the maximum node in the left subtree, exchange the values between it and the current node,
				# then delete the maximum node
				temp_node = node.left
				while temp_node.right is not None:
					temp_node.size -= 1
					temp_node = temp_node.right
				node.value = temp_node.value
				if temp_node == temp_node.parent.left:
					temp_node.parent.left = None
				else:
					temp_node.parent.right = None


	def delete(self, value):
		if self.root is None:
			return None

		if self.root.value == value:
			if self.root.left is not None and self.root.right is not None:
				self.root.size -= 1
				temp_node = self.root.left
				while temp_node.right is not None:
					temp_node.size -= 1
					temp_node = temp_node.right
				self.root.value = temp_node.value
				if temp_node == temp_node.parent.left:
					temp_node.parent.left = None
				else:
					temp_node.parent.right = None
				temp_node.size = 1
			elif self.root.left is not None and self.root.right is None:
				self.root.left.parent = None
				self.root = self.root.left
			elif self.root.left is None and self.root.right is not None:
				self.root.right.parent = None
				self.root = self.root.right
			else:
				self.root = None
		else:
			self._delete(value, self.root)



	def get_random_node(self):
		"""
		1. get the size of the tree, n
		2. get a random integer k between [0, n)
		3. recursively inorder traverse the left subtree or the right subtree according to k
		time complexity: O(logn)
		>>> T = Tree()
		>>> T.insert(8)
		>>> T.insert(6)
		>>> T.insert(10)
		>>> T.insert(3)
		>>> T.insert(7)
		>>> T.insert(2)
		>>> T.insert(9)
		>>> T.insert(11)
		>>> T.root.size
		8
		>>> T.get_kth_node(T.root.left.size).value
		8
		>>> T.get_kth_node(0).value
		2
		>>> T.get_kth_node(1).value
		3
		>>> T.delete(8)
		>>> T.root.size
		7
		>>> T.get_kth_node(T.root.left.size).value
		7
		"""
		n = self.root.size
		k = random.randrange(n)
		return self.get_kth_node(k)

	def get_kth_node(self, k):
		return self._get_kth_node(k, self.root)

	def _get_kth_node(self, k, node):
		""" get the kth node (inorder traversal)
		"""
		if k < 0:
			raise Exception("k < 0")

		if node.left is None:
			if k == 0:
				return node
			else:
				return self._get_kth_node(k-1, node.right)
		else:
			if k < node.left.size:
				return self._get_kth_node(k, node.left)
			elif k == node.left.size:
				return node
			else:
				return self._get_kth_node(k-node.left.size, node.right)

if __name__ == "__main__":
	import doctest
	doctest.testmod()