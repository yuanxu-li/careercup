# 16.21 Sum Swap: Given two arrays of integers, find a pair of values (one value from each array)
# that you can swap to give the two arrays the same sum.
# EXAMPLE
# Input: {4, 1, 2, 1, 1, 2} and {3, 6, 3, 3}
# Output: {1, 3}

def sum_swap(arr1, arr2):
	"""
	To give the two arrays the same sum, we should find a pair of values whose difference is half the difference of
	the respective sums of two arrays.
	>>> sum_swap([4, 1, 2, 1, 1, 2], [3, 6, 3, 3])
	(1, 3)
	"""
	sum1 = sum(arr1)
	sum2 = sum(arr2)

	# the difference of sum1 and sum2 is not even, no result
	if (sum1 - sum2) % 2 != 0:
		return None
	
	arr1.sort()
	arr2.sort()

	diff = abs(sum1 - sum2) / 2
	# look for a value in arr1 which has a corresponding value+diff in arr2
	if sum1 < sum2:
		i = 0
		j = 0
		while i < len(arr1) and j < len(arr2):
			# find this pair and return
			if arr1[i] + diff == arr2[j]:
				return (arr1[i], arr2[j])
			elif arr1[i] + diff < arr2[j]:
				i += 1
			else:
				j += 1

	# look for a value in arr2 which has a corresponding value+diff in arr1
	else:
		i = 0
		j = 0
		while i < len(arr1) and j < len(arr2):
			# find this pair and return
			if arr2[j] + diff == arr1[i]:
				return (arr1[i], arr2[j])
			elif arr2[j] + diff < arr1[i]:
				j += 1
			else:
				i += 1

	return None

if __name__ == "__main__":
	import doctest
	doctest.testmod()

