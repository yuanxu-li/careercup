# 3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets
# too high, it might topples. Therefore, in real life, we would start a new
# stack when the previous stack exceeds some threshold. Implement a data
# structure SetOfStacks that mimics this. SetOfStacks should be composed of
# several stacks and should create a new stack once the previous one exceeds
# capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically
# to a single stack (that is, pop() should return the same values as it would)
# if there were just a single stack).
# FOLLOW UP
# Implement a function popAt(int index) which performs a pop operation on a
# specific sub-stack.

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

class SetOfStacks:
	""" Use a set of stacks of limited capacity to mimic a single stack
	>>> stacks = SetOfStacks()
	>>> stacks.push(1)
	>>> stacks.push(2)
	>>> stacks.push(3)
	>>> stacks.push(4)
	>>> stacks.push(5)
	>>> stacks.peek()
	5
	>>> stacks.push(6)
	>>> stacks.peek()
	6
	>>> stacks.pop()
	6
	>>> stacks.pop()
	5
	>>> stacks.push(1)
	>>> stacks.push(2)
	>>> stacks.push(3)
	>>> stacks.popAt(1)
	1
	"""
	def __init__(self, capacity=5):
		self.top = None
		self.capacity = capacity

	def push(self, data):
		# if empty set of stacks
		if self.top is None:
			self.top = Stack()
			self.top.push(data)
		else:
			# if the current stack is full, initialize a new stack
			if self.top.size >= self.capacity:
				self.top = Stack(next=self.top)
			self.top.push(data)

	def pop(self):
		# empty set of stacks
		if self.top is None:
			raise Exception("empty set of stacks")
		else:
			to_be_returned = self.top.pop()
			if self.top.peek() is None:
				self.top = self.top.next
			return to_be_returned

	def peek(self):
		if self.top is None:
			return None
		else:
			return self.top.peek()

	def is_empty(self):
		return self.top is None

	def popAt(self, index):
		""" pop operation on a specific sub-stack
		"""
		stack = self.top
		while stack is not None and index > 0:
			stack = stack.next
			index -= 1
		if stack is None:
			raise Exception("index out of bound!")
		else:
			return stack.pop()


if __name__ == "__main__":
	import doctest
	doctest.testmod()