# 4.7 Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs
# of projects, where the first project is dependent on the second project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be build.
# If there is no valid build order, return an error.

from enum import Enum
from collections import deque

class Color(Enum):
	WHITE = 0
	GRAY = 1
	BLACK = 2

class Node:
	def __init__(self, name):
		self.name = name
		self.children = []
	def add_child(self, child):
		self.children.append(child)

class Graph:
	"""
	>>> a = Node("a")
	>>> b = Node("b")
	>>> c = Node("c")
	>>> d = Node("d")
	>>> e = Node("e")
	>>> f = Node("f")
	>>> g = Graph([a, b, c, d, e, f])
	>>> a.add_child(d)
	>>> f.add_child(b)
	>>> b.add_child(d)
	>>> f.add_child(a)
	>>> d.add_child(c)
	>>> g.dfs()
	True
	>>> g.print_queue()
	f
	e
	b
	a
	d
	c
	>>> d.add_child(f)
	>>> g.dfs()
	False
	"""
	def __init__(self, nodes=None):
		if nodes is None or len(nodes) == 0:
			self.nodes = []
		else:
			self.nodes = nodes

	def dfs(self):
		self.visited = {}
		self.queue = deque()
		for node in self.nodes:
			self.visited[node] = Color.WHITE
		for node in self.nodes:
			if self.visited[node] == Color.WHITE:
				if self.dfs_visit(node) is False:
					return False
		return True

	def dfs_visit(self, node):
		self.visited[node] = Color.GRAY
		# print("Start " + node.name)
		for child in node.children:
			if self.visited[child] == Color.GRAY:
				return False
			if self.visited[child] == Color.WHITE:
				if self.dfs_visit(child) is False:
					return False
		self.visited[node] = Color.BLACK
		# print("Finish " + node.name)
		self.queue.appendleft(node)

	def print_queue(self):
		for item in self.queue:
			print(item.name)

if __name__ == "__main__":
	import doctest
	doctest.testmod()