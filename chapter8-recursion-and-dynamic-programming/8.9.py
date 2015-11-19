# 8.9 Parens: Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
# of n pairs of parentheses.
# EXAMPLE
# Input: 3
# Output: ((())), (()()), (())(), ()(()), ()()()

import pdb

def parens(n, memo=None):
	""" We base every case on a previous case. To construct combinations for n pairs from 
	>>> parens(3)
	{'(()())', '()(())', '()()()', '((()))', '(())()'}
	"""
	# base case
	if n == 0:
		return set([""])
	# recursive case
	result_set = set()
	for paren in parens(n-1):
		result_set.add("()" + paren)
		result_set.add(paren + "()")
		result_set.add("(" + paren + ")")

	return result_set

def parens_updated(n, left_rem=None, right_rem=None, prefix=None):
	""" We build a string from scratch. Each step there are two possibilities:
	1. add left paren (precondition: still left paren left)
	2. add right paren (precondition: left paren more than right paren)
	>>> set(parens_updated(3))
	{'(()())', '()(())', '()()()', '((()))', '(())()'}
	"""
	# alternative for initial call
	if left_rem is None or right_rem is None or prefix is None:
		left_rem = n
		right_rem = n
		prefix = ""
	# base case
	if left_rem == 0 and right_rem == 0:
		yield prefix
	# recursive case
	else:
		if left_rem > 0:
			yield from parens_updated(n, left_rem - 1, right_rem, prefix + "(")
		if right_rem > left_rem:
			yield from parens_updated(n, left_rem, right_rem - 1, prefix + ")")






if __name__ == "__main__":
	import doctest
	doctest.testmod()