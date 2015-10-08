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
		self.stack1 = Stack()
		self.stack2 = Stack()
	def enqueue(self, data):
		self.stack1.push(data)
	def dequeue(self):
		if self.stack1.peek() is None:
			raise Exception("out of bound!")
		while self.stack1.peek() is not None:
			self.stack2.push(self.stack1.pop())
		to_be_returned = self.stack2.pop()
		while self.stack2.peek() is not None:
			self.stack1.push(self.stack2.pop())
		return to_be_returned

if __name__ == "__main__":
	import doctest
	doctest.testmod()