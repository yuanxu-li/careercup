# 16.1 Number Swapper: Write a function to swap a number in place (that is, without
# temporary variables).

def swap_1(a, b):
	"""
	>>> swap_1(1, 2)
	(2, 1)
	"""
	a, b = b, a
	return a, b

def swap_2(a, b):
	"""
	we use a' and b' to represent the original a and b
	>>> swap_2(1, 2)
	(2, 1)
	"""
	a = a + b
	# now a = a' + b', b = b'
	b = a - b
	# now a = a' + b', b = a'
	a = a - b
	# now a = b', b = a', the values of a and b have been swapped
	return a, b

if __name__ == "__main__":
	import doctest
	doctest.testmod()