# 5.1 Insertin: You are given two 32-bit numbers, N and M, and two bit positions,
# i and j. Write a method to insert M into N such that M starts at bit j and ends
# at bit i. You can assume that the bits j through i have enough space to fit all
# of M. That is, if M = 10011, you can assume that there are at least 5 bits between
# j and i. You would not, for example, have j = 3 and i = 2, because M could not fully
# fit between bit 3 and bit 2.
# EXAMPLE
# Input: N = 1000000000, M = 10011, i = 2, j = 6
# Output: N = 10001001100

import pdb

def insert(M, N, i, j):
	""" Insert M into N between the bits from i to j, by masking the bits between i and j and then inserting M
	>>> insert(binary_to_int("10011"), binary_to_int("10000000000"), 2, 6)
	'10001001100'
	"""
	mask = ~(((1 << (j - i + 1)) - 1) << i)
	# pdb.set_trace()
	return int_to_binary((N & mask) | (M << i))

def binary_to_int(x):
	""" take in a binary string and return the corresponding int
	>>> binary_to_int("101")
	5
	>>> binary_to_int("100000")
	32
	>>> binary_to_int("10011")
	19
	"""
	sum = 0
	for d in x:
		sum = sum * 2 + int(d)
	return sum

def int_to_binary(x):
	""" take in an int and return the corresponding binary string
	>>> int_to_binary(1)
	'1'
	>>> int_to_binary(5)
	'101'
	>>> int_to_binary(11)
	'1011'
	"""
	l = []
	while x != 0 and x != -1:
		l.append(str(x % 2))
		x = x // 2
	l.reverse()
	if x == 0:
		return "".join(l)
	else:
		return "-" + "".join(l)

if __name__ == "__main__":
	import doctest
	doctest.testmod()