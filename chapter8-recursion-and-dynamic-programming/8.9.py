# 8.9 Parens: Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
# of n pairs of parentheses.
# EXAMPLE
# Input: 3
# Output: ((())), (()()), (())(), ()(()), ()()()

import pdb

def parens(n, memo=None):
	"""
	>>> parens(3)
	{'(()())', '()(())', '()()()', '((()))', '(())()'}
	"""
	# alternative for initial call
	if memo is None:
		memo = []
		for i in range(n+1):
			memo.append(set())

	for i in range(n+1):
		if i == 0:
			memo[i].add("")
		else:
			for paren in memo[i-1]:
				memo[i].add("()" + paren)
				memo[i].add(paren + "()")
				memo[i].add("(" + paren + ")")

	return memo[n]




if __name__ == "__main__":
	import doctest
	doctest.testmod()