# 16.6 Smallest Difference: Given two arrays of integers, compute the pair of values (one value in each
# array) with the smallest (non-negative) difference. Return the difference.
# Example
# Input: {1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
# Output: 3. That is, the pair (11, 8).

def smallest_pair(arr1, arr2):
	"""
	We first sort the two arrays, and then move towards from the smallest values of both arrays. Each time
	we store the currently smallest pair and its difference, and we move along the array where the value
	is smaller.
	>>> smallest_pair([1, 3, 15, 11, 2], [23, 127, 235, 19, 8])
	(11, 8)
	"""
	if len(arr1) == 0 or len(arr2) == 0:
		return None
	arr1.sort()
	arr2.sort()
	pair = (arr1[0], arr2[0])
	difference = abs(arr1[0] - arr2[0])
	i, j = 0, 0
	while i < len(arr1) and j < len(arr2):
		# check possible smallest difference
		if abs(arr1[i] - arr2[j]) < difference:
			pair = (arr1[i], arr2[j])
			difference = abs(arr1[i] - arr2[j])
		if arr1[i] <= arr2[j]:
			i += 1
		else:
			j += 1

	return pair

if __name__ == "__main__":
	import doctest
	doctest.testmod()