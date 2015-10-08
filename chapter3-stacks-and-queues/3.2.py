# 3.2 Stack Min: How would you design a stack which, in addition to push and pop,
# has a function min which returns the minimum element? Push, pop and min should
# all operate in O(1) time.

class StackNode:
	def __init__(self, data, min=None):
		self.data = data
		self.next = None
		self.min = data

class Stack:
	""" Each StackNode stores the minimum of its substack. The minimum changes
	within constant time when push or pop happens
	>>> s = Stack()
	>>> s.peek()
	>>> s.push(1)
	>>> s.push(2)
	>>> s.peek()
	2
	>>> s.min()
	1
	>>> s.push(0)
	>>> s.min()
	0
	"""
	def __init__(self):
		self.top = None

	def push(self, data):
		if self.top is None:
			self.top = StackNode(data)
		else:
			node = StackNode(data)
			node.next = self.top
			node.min = data if data < self.top.min else self.top.min
			self.top = node

	def pop(self):
		if self.top is None:
			raise Exception("out of bound!")
		else:
			data = self.top.data
			self.top = self.top.next
			return data

	def peek(self):
		if self.top is None:
			return None
		else:
			return self.top.data

	def min(self):
		return self.top.min

	def is_empty(self):
		return self.top is None

if __name__ == "__main__":
	import doctest
	doctest.testmod()