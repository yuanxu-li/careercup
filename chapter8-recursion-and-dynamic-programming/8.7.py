# 8.7 Permutations without Dups: Write a method to compute all permutations of a string of unique characters

import pdb

def permutations(string, prefix=None):
	"""
	>>> list(permutations("st"))
	['st', 'ts']
	"""
	# alternative for initial call
	if prefix is None:
		prefix = ""
	# base case
	if not string:
		yield prefix
	# by picking each char in the string as the first char to render all possible permutations recursively
	for i in range(len(string)):
		yield from permutations(string[:i] + string[i+1:], prefix + string[i])

if __name__ == "__main__":
	import doctest
	doctest.testmod()