# 4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the
# nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists)

from collections import deque

class Node:
	def __init__(self):
		self.left = None
		self.right = None

	def list_of_depths(self):
		"""
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
		>>> l = n0.list_of_depths()
		>>> len(l[0])
		1
		>>> len(l[1])
		2
		>>> len(l[2])
		4
		>>> len(l[3])
		1
		"""
		depth_lists = [[self]]
		queue = deque()
		queue.appendleft(self)

		while queue:
			temp_list = []
			# for a specific depth
			while queue:
				node = queue.pop()
				if node.left:
					temp_list.append(node.left)
				if node.right:
					temp_list.append(node.right)
			# if this depth still has nodes
			if len(temp_list) > 0:
				# store the list of the depth
				depth_lists.append(temp_list)
				for node in temp_list:
					queue.appendleft(node)
		return depth_lists

if __name__ == "__main__":
	import doctest
	doctest.testmod()