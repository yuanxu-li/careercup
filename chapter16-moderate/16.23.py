# 16.23 Rand7 from Rand5: Implement a method rand7() given rand5(). That is,
# given a method that generates a random number between 0 and 4 (inclusive),
# write a method that generates a random number between 0 and 6 (inclusive).

import random

def rand5():
	return random.randint(0, 4)

def rand7():
	"""
	We use two layers, i.e., 2-d array to map 5 separate values into
	7 separate values.
	0: 0, 1, 2, 3, 4
	1: 5, 6, 0, 1, 2
	2: 3, 4, 5, 6, 0
	3: 1, 2, 3, 4, 5
	4: 6, None, None, None, None
	>>> rand7()
	"""
	mapper = [[0, 1, 2, 3, 4], [5, 6, 0, 1, 2], [3, 4, 5, 6, 0], [1, 2, 3, 4, 5], [6, None, None, None, None]]
	value = None
	while value is None:
		value = mapper[rand5()][rand5()]
	return value

if __name__ == "__main__":
	import doctest
	doctest.testmod()