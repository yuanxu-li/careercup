# 8.5 Recursive Multiply: Write a recursive function to multiply two numbers without using the * operator.
# You can use additions, subtraction, and bit shifting, but you should minimize the number of those operations.

def multiply_recursive(x, y):
	""" x can be seen as x1x2, while y as y1y2.
	steps are listed as follows:
	1. compute x1y1, call the result A
	2. compute x2y2, call the result B
	3. compute (x1+x2)(y1+y2), call the result C
	4. compute C-A-B, call the result K; this number is equal to x1y2+x2y1
	5. compute A*2^(2m)+K*2^m+B
	>>> multiply_recursive(4, 18)
	72
	>>> multiply_recursive(38, 41)
	1558
	>>> multiply_recursive(1001, 1002)
	1003002
	"""
	length1 = bit_length(x)
	length2 = bit_length(y)

	if length1 == 0 or length2 == 0:
		return 0
	elif length1 == 1:
		return y
	elif length2 == 1:
		return x
	else:
		m = max(length1, length2) // 2
		x1 = x >> m
		x2 = ((1 << m) - 1) & x
		y1 = y >> m
		y2 = ((1 << m) - 1) & y
		A = multiply_recursive(x1, y1)
		B = multiply_recursive(x2, y2)
		C = multiply_recursive(x1 + x2, y1 + y2)
		K = C - A - B
		return (A << (2*m)) + (K << m) + B


def bit_length(num):
	"""
	>>> bit_length(4)
	3
	>>> bit_length(5)
	3
	>>> bit_length(1024)
	11
	"""
	l = 0
	while num > 0:
		num >>= 1
		l += 1
	return l


def multiply_recursive_updated(x, y):
	""" Make sure x is always not greater than y as inputs
	Example: to compute 20 * 45, we recursively compute 10 * 25, and add it to itself as the result;
	to compute 19 * 45, we recursively compute 9 * 45, add it to itself, and add 45 the larger number to it as the result;
	base case is 1 * y or 0 * y.
	By reducing x the smaller number instead of y the larger number, we save time by reaching the base case faster.
	>>> multiply_recursive_updated(4, 18)
	72
	>>> multiply_recursive_updated(38, 41)
	1558
	>>> multiply_recursive_updated(1001, 1002)
	1003002
	"""
	# base case
	if x == 0:
		return 0
	elif x == 1:
		return y

	# recursive case
	temp_x = x >> 1
	half_prod = multiply_recursive_updated(temp_x, y)
	if x % 2 == 0:
		return half_prod + half_prod
	else:
		return half_prod + half_prod + y




if __name__ == "__main__":
	import doctest
	doctest.testmod()