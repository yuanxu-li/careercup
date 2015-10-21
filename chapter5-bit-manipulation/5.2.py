# 5.2 Binary to String: Given a real number between 0 and 1 (e.g., 0.72) that is passed in as a double,
# print the binary representation. If the number cannot be represented accurately in binary with at most
# 32 characters, print "ERROR".

import pdb

def binary_to_string(f):
	""" For a number in base 10 can be represented as: d_1 * 2^(-1) + d_2 * 2^(-2) + ... + d_n * 2^(-n), each time we
	multiply the number by 2, we will get d_i before the decimal point.
	>>> binary_to_string(0.72)
	ERROR
	>>> binary_to_string(0.25)
	'.01'
	>>> binary_to_string(0.6)
	ERROR
	>>> binary_to_string(0.375)
	'.011'
	"""
	if f > 1 or f < 0:
		print("ERROR")
		return
	l = ["."]
	while f > 0 and len(l) <= 32:
		f *= 2
		if f >= 1:
			l.append("1")
			f -= 1
		else:
			l.append("0")

	# pdb.set_trace()

	if f <= 0:
		return "".join(l)
	else:
		print("ERROR")

if __name__ == "__main__":
	import doctest
	doctest.testmod()