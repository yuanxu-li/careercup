# 3.1 Three in One: Describe how you could use a single array to implement three stacks.

class ThreeStacks:
	""" Divide an array into three even stacks
	>>> s = ThreeStacks(30)
	>>> s.push1(10)
	>>> s.push1(20)
	>>> s.is_empty1()
	False
	>>> s.peek1()
	20
	>>> s.pop1()
	20
	>>> s.pop1()
	10
	>>> s.is_empty1()
	True
	>>> s.push2(10)
	>>> s.push2(20)
	>>> s.is_empty2()
	False
	>>> s.peek2()
	20
	>>> s.pop2()
	20
	>>> s.pop2()
	10
	>>> s.is_empty2()
	True
	>>> s.push3(10)
	>>> s.push3(20)
	>>> s.is_empty3()
	False
	>>> s.peek3()
	20
	>>> s.pop3()
	20
	>>> s.pop3()
	10
	>>> s.is_empty3()
	True
	"""
	def __init__(self, length=None):
		if length is None:
			self.length = 30
		else:
			self.length = length
		self.array = [None for i in range(self.length)]
		self.head1 = 0
		self.head2 = int(self.length / 3)
		self.head3 = int(self.length * 2 / 3)
		self.tail1 = self.head1
		self.tail2 = self.head2
		self.tail3 = self.head3

	def pop1(self):
		if self.tail1 > self.head1:
			self.tail1 -= 1
			return self.array[self.tail1]
		else:
			raise Exception("out of bound!")

	def push1(self, item):
		if self.tail1 < self.head2:
			self.array[self.tail1] = item
			self.tail1 += 1
		else:
			raise Exception("out of bound!")

	def peek1(self):
		if self.tail1 > self.head1:
			return self.array[self.tail1 - 1]
		else:
			return None

	def is_empty1(self):
		return self.head1 >= self.tail1

	def pop2(self):
		if self.tail2 > self.head2:
			self.tail2 -= 1
			return self.array[self.tail2]
		else:
			raise Exception("out of bound!")

	def push2(self, item):
		if self.tail2 < self.head3:
			self.array[self.tail2] = item
			self.tail2 += 1
		else:
			raise Exception("out of bound!")

	def peek2(self):
		if self.tail2 > self.head2:
			return self.array[self.tail2 - 1]
		else:
			return None

	def is_empty2(self):
		return self.head2 >= self.tail2

	def pop3(self):
		if self.tail3 > self.head3:
			self.tail3 -= 1
			return self.array[self.tail3]
		else:
			raise Exception("out of bound!")

	def push3(self, item):
		if self.tail3 < self.length:
			self.array[self.tail3] = item
			self.tail3 += 1
		else:
			raise Exception("out of bound!")

	def peek3(self):
		if self.tail3 > self.head3:
			return self.array[self.tail3 - 1]
		else:
			return None

	def is_empty3(self):
		return self.head3 >= self.tail3

class MultiStack:
	"""
	>>> ms = MultiStack()
	>>> ms.push(1, 11)
	>>> ms.push(1, 12)
	>>> ms.push(1, 13)
	>>> ms.push(2, 21)
	>>> ms.push(2, 22)
	>>> ms.push(0, 31)
	>>> ms.push(0, 32)
	>>> ms.pop(1)
	13
	>>> ms.pop(2)
	22
	>>> ms.peek(2)
	21
	"""
	def __init__(self, num_of_stacks=3, stack_size=5):
		self.values = [None for i in range(num_of_stacks * stack_size)]
		self.sizes = [0 for i in range(num_of_stacks)]
		self.capacity = stack_size

	def push(self, stack_num, data):
		if self.is_full(stack_num):
			raise Exception("stack " + str(stack_num) + " full!")
		else:
			self.sizes[stack_num] += 1
			self.values[self.index_of_tail(stack_num)] = data

	def pop(self, stack_num):
		if self.is_empty(stack_num):
			raise Exception("stack " + str(stack_num) + " empty!")
		else:
			value = self.values[self.index_of_tail(stack_num)]
			self.sizes[stack_num] -= 1
			return value

	def peek(self, stack_num):
		if self.is_empty(stack_num):
			return None
		else:
			return self.values[self.index_of_tail(stack_num)]

	def is_full(self, stack_num):
		return self.sizes[stack_num] == self.capacity

	def is_empty(self, stack_num):
		return self.sizes[stack_num] == 0

	def index_of_tail(self, stack_num):
		return stack_num * self.capacity + self.sizes[stack_num] - 1



if __name__ == "__main__":
	import doctest
	doctest.testmod()