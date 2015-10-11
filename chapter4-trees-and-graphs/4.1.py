# 4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out
# whether there is a route between two nodes.

from collections import deque

class Node:
	def __init__(self, name):
		self.name = name
		self.children = []
	def add_child(self, *nodes):
		self.children.extend(nodes)


class Graph:
	"""
	>>> n0 = Node("0")
	>>> n1 = Node("1")
	>>> n2 = Node("2")
	>>> n3 = Node("3")
	>>> n4 = Node("4")
	>>> n5 = Node("5")
	>>> n6 = Node("6")
	>>> n0.add_child(n1, n2, n3)
	>>> n1.add_child(n0)
	>>> n2.add_child(n0, n4)
	>>> n3.add_child(n0, n4)
	>>> n4.add_child(n3, n5)
	>>> n5.add_child(n4)
	>>> g = Graph([n0, n1, n2, n3, n4, n5, n6])
	>>> g.find_route_bfs(n0, n5)
	True
	>>> g.find_route_bfs(n0, n6)
	False
	>>> g.find_route_dfs(n0, n5)
	True
	>>> g.find_route_dfs(n0, n6)
	False
	"""
	def __init__(self, nodes=None):
		if nodes == None or len(nodes) == 0:
			self.nodes = []
		else:
			self.nodes = nodes

	def find_route_dfs(self, start_node, end_node):
		if start_node == end_node:
			return True
		for child in start_node.children:
			if self.find_route_bfs(child, end_node) is True:
				return True
		return False

	def find_route_bfs(self, start_node, end_node):
		# trivial case
		if start_node == end_node:
			return True

		visited = {}
		for node in self.nodes:
			visited[node] = False
		queue = deque()
		visited[start_node] = True
		queue.appendleft(start_node)
		while queue:
			node = queue.pop()
			for child in node.children:
				if visited[child] is False:
					if child == end_node:
						return True
					visited[child] = True
					queue.appendleft(child)
		return False

if __name__ == "__main__":
	import doctest
	doctest.testmod()