# 5.4 Next Number: Given a positive integer, print the next smaller and the next larger number that have the same
# number of 1 bits in their binary representation.

import pdb

def get_next_larger(x):
	"""
	1. Flip the rightmost non-trailing zero, at position p
	2. Clear bits to the right of p, count 1's as c1
	3. Append c1 1's to the end
	>>> get_next_larger(43)
	45
	>>> get_next_larger(76)
	81
	"""
	
	# compute c0 and c1
	c = x
	c0 = 0
	c1 = 0
	while (c & 1) == 0 and c != 0:
		c0 += 1
		c >>= 1
	while (c & 1) == 1 and c != 0:
		c1 += 1
		c >>= 1
	p = c0 + c1

	# flip the rightmost non-trailing zero
	x |= (1 << p)
	# clear all bits to the right of p
	x &= ~((1 << p) - 1)
	# insert (c1-1) ones on the right
	x |= (1 << (c1 - 1)) - 1

	return x

def get_next_smaller(x):
	"""
	1. Flip the rightmost non-trailing one, at position p
	2. Clear bits to the right of p, count 0's as c0
	3. Append c0 0's to the end
	>>> get_next_smaller(43)
	39
	>>> get_next_smaller(76)
	74
	"""
	c = x
	c0 = 0
	c1 = 0
	while (c & 1) == 1 and c != 0:
		c1 += 1
		c >>= 1
	while (c & 1) == 0 and c != 0:
		c0 += 1
		c >>= 1
	p = c0 + c1

	# pdb.set_trace()

	# flip the rightmost non-trailing one
	x &= (~(1 << p))
	# clear all bits to the right of p
	x &= ~((1 << p) - 1)
	# insert (c0-1) zeros on the right, next to the flipped 1
	x |= (((1 << (c1 + 1)) - 1) << (p - c1 - 1))

	return x

if __name__ == "__main__":
	import doctest
	doctest.testmod()