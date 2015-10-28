# 6.10 Poison: You have 1000 bottles of soda, and exactly one is poisoned. You have 10 test strips
# which can be used to detect poison. A single drop of poison will turn the test strip positive
# permanently. You can put any number of drops on a test strip at once and you can reuse a test strip
# as many times as you'd like (as long as the results are negative). However, you can only run tests
# once per day and it takes seven days to return a result. How would you figure out the poisoned bottle
# in as few days as possible?
# FOLLOW UP
# Write code to simulate your approach.

# Day 1: we split 1000 bottles into 10 groups, each having 100 bottles and getting one drop from each bottle
# to make one drop for each group. We test the 10 drops against the 10 test strips, and reduce our search
# down to one group and waste one test strip

# Day 2: similar approach, but now we only have 9 test strips to test against 9 groups for all the bottles remaining
# from last test

# Day n: ...

import math

def poison_test(n, k):
	""" n is the number of bottles of sode, and k is the number of test strips
	>>> poison_test(1000, 10)
	4
	"""
	i = 0
	while n > 1:
		n = math.ceil(n / k)
		k -= 1
		i += 1
	return i

if __name__ == "__main__":
	import doctest
	doctest.testmod()