# 8.8 Permutations with Dups: Write a method to compute all permutations of a string whose characters
# are not necessarily unique. The list of permutations should not have duplicates.

def permutations_dups(string, prefix=None, memo=None):
	"""
	>>> list(permutations_dups("sst"))
	['sst', 'sts', 'tss']
	"""
	# alternative for initial call
	if prefix is None or memo is None:
		prefix = ""
		memo = set()

	# base case
	if not string:
		if prefix not in memo:
			memo.add(prefix)
			yield prefix
	# by picking each char in the string as the first char to render all possible permutations recursively
	for i in range(len(string)):
		yield from permutations_dups(string[:i] + string[i+1:], prefix + string[i], memo)

if __name__ == "__main__":
	import doctest
	doctest.testmod()