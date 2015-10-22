# 5.7 Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions
# as possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on)

def swap_odd_even_bits(x):
	""" We can get the odd and even bits separately and move them into the right place, and then merge them back
	>>> swap_odd_even_bits(3456)
	>>> swap_odd_even_bits(24623)
	"""
	return ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1)

if __name__ == "__main__":
	import doctest
	doctest.testmod()