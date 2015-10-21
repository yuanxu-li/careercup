# 5.3 Flip Bit to Win: You have an integer and you can flip exactly one bit from a bit from a 0 to a 1.
# Write code to find the length of the longest sequence of 1s you could create.
# EXAMPLE
# Input: 1775 (or: 11011101111)
# Output: 8

def longest_sequence(x):
	""" by tracking a previous length and a current length, we are always able to compare
	>>> longest_sequence(1775)
	8
	"""
	previous = 0
	current = 0
	max = 0
	if x & 1 == 1:
		current = 1

	while x != 0 and x != -1:
		x >>= 1
		if x & 1 == 0:
			if previous != 0 and current != 0:
				max = previous + current + 1 if previous + current + 1 > max else max
			previous = current
			current = 0
		else:
			current += 1
	return max

if __name__ == "__main__":
	import doctest
	doctest.testmod()