# 16.24 Pairs with Sum: Design an algorithm to find all pairs of integers within
# an array which sum to a specified value.

from collections import Counter

def pairs_with_sum(arr, k):
	"""
	put all elements into a Counter (similar to a dict), for each value, search for the complementary value
	>>> pairs_with_sum([1, 2, 3, 1, 5, 3, 4, 9, 4, 6, 2, 2, 2, 2], 4)
	[[1, 3], [1, 3], [2, 2], [2, 2]]
	"""
	c = Counter(arr)
	result = []
	while c:
		value1, count1 = c.popitem()
		# the value matches itself
		if k - value1 == value1:
			for _ in range(count1 // 2):
				result.append([value1, value1])
		# find matching value
		count2 = c.pop(k - value1, None)
		if count2 is None:
			continue
		for _ in range(min(count1, count2)):
			result.append([value1, k - value1])
	return result

if __name__ == "__main__":
	import doctest
	doctest.testmod()