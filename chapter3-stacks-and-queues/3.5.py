# 3.5 Sort Stack: Write a program to sort a stack such that the smallest
# items are on the top. You can use an additional temporary stack, but
# you may not copy the elements into any other data structure (such as
# an array). The stack supports the following operation: push, pop, peek,
# and isEmpty.

class StackNode:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self, next=None):
		self.top = None
		self.next = next
		self.size = 0
	def push(self, data):
		node = StackNode(data)
		node.next = self.top
		self.top = node
		self.size += 1
	def pop(self):
		if self.top is None:
			raise Exception("out of bound!")
		else:
			data = self.top.data
			self.top = self.top.next
			self.size -= 1
			return data
	def peek(self):
		if self.top is None:
			return None
		else:
			return self.top.data
	def is_empty(self):
		return self.top is None
	def sort(self, compare=lambda x, y : x > y):
		""" merge sort
		time complexity: f(n) = 2*f(n/2) + 2n => O(nlogn)
		>>> s = Stack()
		>>> s.push(2)
		>>> s.push(1)
		>>> s.push(3)
		>>> s.push(4)
		>>> s.push(0)
		>>> s.sort()
		>>> s.pop()
		0
		>>> s.pop()
		1
		>>> s.pop()
		2
		>>> s.pop()
		3
		>>> s.pop()
		4
		"""
		if self.top == None:
			return
		middle = self.pop()
		upper_stack = Stack()
		lower_stack = Stack()
		while self.peek() is not None:
			data = self.pop()
			if compare(data, middle):
				lower_stack.push(data)
			else:
				upper_stack.push(data)
		reverse_compare = lambda x, y: not compare(x, y)
		lower_stack.sort(compare=reverse_compare)
		upper_stack.sort(compare=reverse_compare)

		while lower_stack.peek() is not None:
			self.push(lower_stack.pop())
		self.push(middle)
		while upper_stack.peek() is not None:
			self.push(upper_stack.pop())

if __name__ == "__main__":
	import doctest
	doctest.testmod()



