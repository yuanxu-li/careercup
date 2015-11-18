# 8.4 Power Set: Write a method to return all subsets of a set.

def power_set(s, memo=None):
	""" For a set, each we add it to the final list, and run the algorithm against its one-item-less subset
	>>> power_set(set([1,2,3,4,5]))
	[{1, 2, 3, 4, 5}, {2, 3, 4, 5}, {3, 4, 5}, {4, 5}, {5}, set(), {4}, {3, 5}, {3}, {3, 4}, {2, 4, 5}, {2, 5}, {2}, {2, 4}, {2, 3, 5}, {2, 3}, {2, 3, 4}, {1, 3, 4, 5}, {1, 4, 5}, {1, 5}, {1}, {1, 4}, {1, 3, 5}, {1, 3}, {1, 3, 4}, {1, 2, 4, 5}, {1, 2, 5}, {1, 2}, {1, 2, 4}, {1, 2, 3, 5}, {1, 2, 3}, {1, 2, 3, 4}]
	"""
	returned = False
	if memo is None:
		memo = []
		returned = True
	if s not in memo:
		memo.append(s)
		for elem in s:
			power_set(s - set([elem]), memo)

	if returned == True:
		return memo

if __name__ == "__main__":
	import doctest
	doctest.testmod()