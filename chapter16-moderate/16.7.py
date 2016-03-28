# 16.7 Number Max: Write a method that finds the maximum of two numbers. You should not use if-else
# or any other comparison operator.

def get_max(a, b):
	"""
	>>> get_max(17, 504)
	504
	>>> get_max(17, -504)
	17
	"""
	c = a - b
	# k = 0 if c is positive, 1 if c is negative
	k = (c >> 31) & 0x1
	return a - k * c

if __name__ == "__main__":
	import doctest
	doctest.testmod()