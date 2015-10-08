# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue
# using two stacks

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

class MyQueue:
	""" use two stacks as to implement a queue. One stack as the main storage,
	while the other one is used to temporarily store nodes to let the oldest
	node out
	>>> q = MyQueue()
	>>> q.enqueue(1)
	>>> q.enqueue(2)
	>>> q.enqueue(3)
	>>> q.dequeue()
	1
	>>> q.dequeue()
	2
	"""
	def __init__(self):
		self.old_stack = Stack()
		self.new_stack = Stack()

	def enqueue(self, data):
		self.new_stack.push(data)
	
	def dequeue(self):
		if self.old_stack.peek() is None:
			self.shift_stack()
		if self.old_stack.peek() is None:
			raise Exception("Empty")
		else:
			return self.old_stack.pop()

	def shift_stack(self):
		while self.new_stack.peek() is not None:
			self.old_stack.push(self.new_stack.pop())




if __name__ == "__main__":
	import doctest
	doctest.testmod()