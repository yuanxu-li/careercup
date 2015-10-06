class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
	def __str__(self):
		return str(self.data)

class LinkedList:
	def __init__(self, l=None, head=None):
		self.head = head
		if l is not None:
			l.reverse()
			for item in l:
				self.insert(item)

	def __eq__(self, other):
		cursor1 = self.head
		cursor2 = other.head
		while cursor1 is not None and cursor2 is not None:
			if cursor1.data != cursor2.data:
				return False
			cursor1 = cursor1.next
			cursor2 = cursor2.next
		if cursor1 is None and cursor2 is None:
			return True
		else:
			return False

	def insert(self, data):
		"""
		>>> l = LinkedList()
		>>> l.insert(1)
		>>> l.return_list()
		[1]
		>>> l.insert(2)
		>>> l.return_list()
		[2, 1]
		"""
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def size(self):
		current = self.head
		count = 0
		while current is not None:
			count += 1
			current = current.next
		return count

	def search(self, data):
		current = self.head
		found = False
		while current is not None and found is False:
			if current.data == data:
				found = True
			else:
				current = current.next
		if current is None:
			return None
		else:
			return current

	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while found is False and current is not None:
			if current.data == data:
				found = True
			else:
				previous = current
				current = current.next

		if current is None:
			raise ValueError("Data not in list")
		elif found is True:
			if previous is None:
				self.head = current.next
			else:
				previous.next = current.next

	


	def copy(self):
		"""
		>>> l1 = LinkedList([1, 2, 3])
		>>> l2 = l1.copy()
		>>> l2.return_list()
		[1, 2, 3]
		"""
		cursor = self.head
		new_list = LinkedList()
		new_cursor = new_list.head
		while cursor is not None:
			if new_cursor is None:
				new_list.head = Node(cursor.data)
				new_cursor = new_list.head
			else:
				new_cursor.next = Node(cursor.data)
				new_cursor = new_cursor.next
			cursor = cursor.next
		return new_list

	def reverse(self):
		""" reverse the linked list
		>>> l = LinkedList([1,2,3])
		>>> l.return_list()
		[1, 2, 3]
		>>> l.reverse()
		>>> l.return_list()
		[3, 2, 1]
		"""
		cursor = self.head
		new_list = LinkedList()
		while cursor is not None:
			new_list.insert(cursor.data)
			cursor = cursor.next
		self.head = new_list.head

	def return_list(self):
		result = []
		cursor = self.head
		while cursor is not None:
			result.append(cursor.data)
			cursor = cursor.next
		return result

	# 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
	# How would you solve this problem if a temporary buffer is not allowed?
	def remove_dups(self):
		"""
		remove duplicates from singly linked list. In the examples, I transform 
		the linked list to or from list, for the sake of test. But within the function,
		the operations are performed on the linked list.
		>>> linked_list = LinkedList([1,4,2,1,2,5,5])
		>>> linked_list.remove_dups()
		>>> linked_list.return_list()
		[1, 4, 2, 5]
		>>> linked_list = LinkedList([])
		>>> linked_list.remove_dups()
		>>> linked_list.return_list()
		[]
		"""
		current = self.head
		while current is not None:
			forward = current
			while forward.next is not None:
				if forward.next.data == current.data:
					forward.next = forward.next.next
				else:
					forward = forward.next
			current = current.next

	# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element
	# of a singly linked list
	def return_k_to_last(self, k):
		""" return the kth to last element from linked list
		>>> linked_list = LinkedList([1,4,2,5])
		>>> print(linked_list.return_k_to_last(1))
		5
		>>> print(linked_list.return_k_to_last(2))
		2
		>>> print(linked_list.return_k_to_last(3))
		4
		>>> print(linked_list.return_k_to_last(4))
		1
		>>> print(linked_list.return_k_to_last(5))
		None
		>>> linked_list = LinkedList()
		>>> print(linked_list.return_k_to_last(1))
		None
		"""
		cursor1 = self.head
		cursor2 = self.head
		for i in range(k):
			if cursor1 is not None:
				cursor1 = cursor1.next
			else:
				return None
		while cursor1 is not None:
			cursor1 = cursor1.next
			cursor2 = cursor2.next
		return cursor2

	# 2.3 Delete Middle Node: Implement an algorithm to delete a node in the middle
	# of a single linked list, given only access to that node
	# EXAMPLE
	# Input: the node c from the linked list a -> b -> c -> d -> e
	# Result: nothing is returned, but the new linked list looks like a -> b -> d -> e
	def delete_middle_node(self):
		""" delete the middle node
		>>> linked_list = LinkedList([1,4,2,5])
		>>> linked_list.delete_middle_node()
		>>> linked_list.return_list()
		[1, 4, 5]
		"""
		if self.head is None:
			return
		length = self.size()
		current = self.head
		previous = None
		count = 0
		while count < int(length / 2) and current is not None:
			previous = current
			current = current.next
			count += 1
		if current is None:
			raise Exception("cannot find middle node!")
		elif previous is None:
			self.head = current.next
		else:
			previous.next = current.next

	# 2.4 Partition: Write code to partition a linked list around a value x, such that
	# all nodes less than x come before all nodes greater than or equal to x. If x is
	# contained within the list, the values of x only need to be after the elements
	# less than x (see below).
	# EXAMPLE
	# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
	# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
	def partition(self, x):
		""" partition the linked list around a given value x, such that all values less than x come before values
		greater than or equal to x
		>>> linked_list = LinkedList([3,5,8,5,10,2,1])
		>>> linked_list.partition(5)
		>>> linked_list.return_list()
		[3, 1, 2, 5, 8, 5, 10]
		"""
		if self.head is None:
			return self
		# find the insert point, which will be represented as cursor
		previous = None
		current = self.head
		while current is not None and current.data < x:
			previous = current
			current = current.next
		# if all nodes are less than x, return as it is
		if current is None:
			return
		else:
			cursor = previous

		# create a virtual node, to make it consistent, which will be deleted afterwards
		virtual_node = False
		if cursor is None:
			M = x - 1000
			self.insert(M)
			cursor = self.head
			virtual_node = True
		# looping over the rest of list to append the nodes less than x to the cursor
		previous = cursor.next
		current = previous.next
		while current is not None:
			if current.data < x:
				# delete current
				previous.next = current.next
				# append current to cursor
				current.next = cursor.next
				cursor.next = current
				current = previous.next
			else:
				previous = current
				current = current.next
		if virtual_node:
			self.head = self.head.next

	# 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains
	# a single digit. The digits are stored in reverse order, such that the 1's digit is at the
	# head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
	# EXAMPLE
	# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295
	# Output: 2 -> 1 -> 9. That is, 912
	# FOLLOW UP
	# Suppose the digits are stored in forward order. Repeat the above problem
	# EXAMPLE
	# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617 + 295
	# Output: 9 -> 1 -> 2. That is, 912
	@staticmethod
	def sum_lists_reverse(l1, l2):
		""" numbers are stored in backward order
		>>> l1 = LinkedList([7, 1, 6])
		>>> l2 = LinkedList([5, 9, 2])
		>>> l3 = LinkedList.sum_lists_reverse(l1, l2)
		>>> l3.return_list()
		[2, 1, 9]
		"""
		cursor1 = l1.head
		cursor2 = l2.head
		l3 = LinkedList()
		cursor3 = l3.head
		carryover = 0
		while cursor1 is not None and cursor2 is not None:
			digit = int((cursor1.data + cursor2.data + carryover) % 10)
			carryover = (cursor1.data + cursor2.data + carryover) / 10
			new_node = Node(digit)
			if cursor3 is None:
				l3.head = new_node
				cursor3 = l3.head
			else:
				cursor3.next = new_node
				cursor3 = cursor3.next
			cursor1 = cursor1.next
			cursor2 = cursor2.next

		while cursor1 is not None:
			digit = int((cursor1.data + carryover) % 10)
			carryover = (cursor1.data + carryover) / 10
			new_node = Node(digit)
			if cursor3 is None:
				l3.head = new_node
				cursor3 = l3.head
			else:
				cursor3.next = new_node
				cursor3 = cursor3.next
			cursor1 = cursor1.next

		while cursor2 is not None:
			digit = int((cursor2.data + carryover) % 10)
			carryover = (cursor2.data + carryover) / 10
			new_node = Node(digit)
			if cursor3 is None:
				l3.head = new_node
				cursor3 = l3.head
			else:
				cursor3.next = new_node
				cursor3 = cursor3.next
			cursor2 = cursor2.next

		return l3

	@staticmethod
	def sum_lists_forward(l1, l2):
		""" numbers are stored in backward order
		>>> l1 = LinkedList([6, 1, 7])
		>>> l2 = LinkedList([2, 9, 5])
		>>> l3 = LinkedList.sum_lists_forward(l1, l2)
		>>> l3.return_list()
		[9, 1, 2]
		"""
		l1.reverse()
		l2.reverse()
		l3 = LinkedList.sum_lists_reverse(l1, l2)
		l3.reverse()
		return l3

	# 2.6 Palindrome: Implement a function to check if a linked list is a palindrome
	def is_palindrome(self):
		""" check if a linked list is a palindrome
		>>> LinkedList([1, 2, 2, 1]).is_palindrome()
		True
		>>> LinkedList().is_palindrome()
		True
		>>> LinkedList([1, 2, 4, 2, 4]).is_palindrome()
		False
		"""
		reverse_list = self.copy()
		reverse_list.reverse()
		return self == reverse_list

	# 2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect.
	# Return the intersecting node. Note that the intersection is defined based on reference, not value.
	# That is, if the kth node of the first linked list is the exact same node (by reference) as the jth
	# node of the second linked list, then they are intersecting.
	def intersection(self, other):
		""" store self linked list as a dict, with its id (memory address) as the key, and loop through
		the second linked list to see if the id of any node is the same as in the dict
		>>> shared_list = LinkedList([1, 2, 3, 4, 5])
		>>> l1 = LinkedList(head=shared_list.head)
		>>> l2 = LinkedList(head=shared_list.head)
		>>> l1.insert(4)
		>>> l1.insert(5)
		>>> l2.insert(4)
		>>> print(l1.intersection(l2))
		1
		"""
		if self.head is None or other.head is None:
			return None
		dict1 = {}
		cursor = self.head
		while cursor is not None:
			dict1[id(cursor)] = cursor
			cursor = cursor.next
		cursor = other.head
		while cursor is not None:
			if id(cursor) in dict1:
				return cursor
			else:
				cursor = cursor.next
		return None

	# 2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node
	# at the beginning of the loop
	# DEFINITION:
	# Circular linked list: A (corrupt) linked list in which a node's next pointer to an earlier node,
	# so as to make a loop in the linked list.
	# EXAMPLE
	# Input: A -> B -> C -> D -> E -> C [the same C as earlier]
	# Output: C
	def loop_detection(self):
		""" similar approach as intersection. store each node's id in a dict, and check if any following node's id
		is in it
		>>> l = LinkedList([1, 2, 3, 4, 5, 6, 7, 8])
		>>> l.return_k_to_last(2).next = l.return_k_to_last(4)
		>>> print(l.loop_detection())
		5
		"""
		cursor = self.head
		dict1 = {}
		while cursor is not None:
			if id(cursor) in dict1:
				return cursor
			else:
				dict1[id(cursor)] = cursor
				cursor = cursor.next
		return None


def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()


	