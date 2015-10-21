# 5.6 Conversion: Write a function to determine the number of bits you would need
# to flip to convert integer A to integer B
# EXAMPLE
# Input: 29 (or 11101), 15 (or: 01111)
# Output: 2

def conversion(a, b):
	"""
	>>> conversion(29, 15)
	2
	"""
	return bin(a ^ b).count("1")



if __name__ == "__main__":
	import doctest
	doctest.testmod()