# 6.10 Poison: You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips
# which can be used to detect poison. A single drop of poison will turn the test strip positive
# permanently. You can put any number of drops on a test strip at once and you can reuse a test strip
# as many times as you'd like (as long as the results are negative). However, you can only run tests
# once per day and it takes seven days to return a result. How would you figure out the poisoned bottle
# in as few days as possible?
# FOLLOW UP
# Write code to simulate your approach.

import math
import pdb

def poison_test(n, k, poison_num):
	""" n is the number of bottles of sode, and k is the number of test strips.
	1000 bottles can be represented as binary numbers which have 10 digits. If the i-th digit of a bottle is 1,
	we add a drop to i-th strip. Then we send all the strips for test, if j-th strip is positive, it indicates that
	the j-th digits of the poisoned bottle is 1. Because we need seven days to return a result, the minimum days are 7.
	>>> poison_test(1000, 10, 500)
	500
	>>> poison_test(1024, 10, 400)
	400
	>>> poison_test(1025, 10, 300)
	-1
	"""
	
	# if n is larger than 2^k, we would not be able to use k strips to detect among n bottles
	if n > math.pow(2, k):
		return -1
	bottles = [False for i in range(n)]
	strips = [False for i in range(k)]
	bottles[poison_num] = True
	for i, bottle in enumerate(bottles):
		strip_index = 0
		while i > 0:
			if i & 1 == 1:
				# add one drop to corresponding strip by making it True
				strips[strip_index] = strips[strip_index] or bottle
			strip_index += 1
			i >>= 1
	positive = get_positive(strips)
	num = get_num(positive)
	return num

def get_positive(strips):
	positive = []
	for i, strip in enumerate(strips):
		if strip:
			positive.append(i)
	return positive
	
def get_num(positive):
	num = 0
	for i in positive:
		# pdb.set_trace()
		num |= 1 << i
	return num


if __name__ == "__main__":
	import doctest
	doctest.testmod()
