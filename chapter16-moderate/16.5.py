# 16.5 Factorial Zeros: Write an algorithm which computes the number of trailing zeros
# in n factorial

def factorial_trailing_zeros(n):
	"""
	Note that trailing zeros are essentially created by 5 * 2. Other multiplications like
	15 * 6 can still be factored into 5 * 2. Therefore, we need to find how many 5's multiples are there.
	No need to find how many 2's multiples because there are many more even numbers than 5's multiples.
	>>> factorial_trailing_zeros(5)
	1
	>>> factorial_trailing_zeros(11)
	2
	"""
	return n // 5

if __name__ == "__main__":
	import doctest
	doctest.testmod()