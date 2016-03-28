# 16.9 Operations: Write methods to implement the multiply, subtract, and divide operations for integers.
# The result of all of these are integers. Use only the add operator.

def multiply(a, b):
	"""
	>>> multiply(13, 17)
	221
	>>> multiply(6, 1)
	6
	"""
	a, b = min(a, b), max(a, b)
	# base case
	if a == 1:
		return b
	# recursive case
	else:
		# even
		if a % 2 == 0:
			temp_result = multiply(a >> 1, b)
			return temp_result << 1
		else:
			temp_result = multiply(a >> 1, b)
			return (temp_result << 1) + b

def subtract(a, b):
	"""
	>>> subtract(0, 5)
	-5
	>>> subtract(5, 0)
	5
	"""
	return a + ~b + 1

def divide(a, b):
	"""
	>>> divide(14, 5)
	2
	>>> divide(4, 100)
	0
	"""
	if a < b:
		return 0
	else:
		return 1 + divide(subtract(a, b), b)


if __name__ == "__main__":
	import doctest
	doctest.testmod()