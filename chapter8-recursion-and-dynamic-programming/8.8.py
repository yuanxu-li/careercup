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

from collections import defaultdict

def permutations_dups_updated(prefix, remaining=None, freq_table=None):
	"""
	We count the frequencies of each character, and then use that to recursively construct permutations.
	Each time we take a character
	>>> list(permutations_dups_updated("sst"))
	['tss', 'sts', 'sst']
	"""
	# alternative for initial call
	if freq_table is None or remaining is None:
		freq_table = defaultdict(int)
		for char in prefix:
			freq_table[char] += 1
		remaining = len(prefix)
		yield from permutations_dups_updated("", remaining, freq_table)
	else:
		# base case
		if remaining == 0:
			yield prefix
		# recursive case
		else:
			for char in freq_table:
				if freq_table[char] > 0:
					freq_table[char] -= 1
					yield from permutations_dups_updated(prefix + char, remaining - 1, freq_table)
					freq_table[char] += 1





if __name__ == "__main__":
	import doctest
	doctest.testmod()