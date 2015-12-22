# 10.2 Group Anagrams: Write a method to sort an array of strings so that all the anagrams are
# next to each other.

from collections import defaultdict

def group_anagrams(strings):
	"""
	create a dict to map from a sorted string to a list of the original strings, then simply all strings mapped
	by the same key will be grouped together. If the length of string are considered constant, time complexity
	is only O(n), since we only have to loop over the array twice, first time to generate the dict, second time
	to loop over the keys to group anagrams mapped by the same key
	>>> group_anagrams(["asd", "atr", "tar", "pppp", "dsa", "rta", "eryvdf"])
	['atr', 'tar', 'rta', 'asd', 'dsa', 'pppp', 'eryvdf']
	"""
	d = defaultdict(list)
	for s in strings:
		sorted_s = "".join(sorted(s))
		d[sorted_s].append(s)
	new_strings = []
	for sorted_s in d:
		new_strings.extend(d[sorted_s])
	return new_strings

if __name__ == "__main__":
	import doctest
	doctest.testmod()