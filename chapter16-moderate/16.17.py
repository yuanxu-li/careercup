# 16.17 Contiguous Sequence: You are given an array of integers (both positive and negative).
# Find the contiguous sequence with the largest sum. Return the sum
# EXAMPLE
# Input: 2, -8, 3, -2, 4, -10
# Output: 5 (i.e., {3, -2, 4})

def largest_sum(arr):
	"""
	We start from the beginning of the array, and keep track of the sum from the beginning. We
	will update the largest sum if the current sum if larger than the previous one. Also, when
	we find the sum is smaller than 0, we restart the beginning from the next value, because all
	previous values will only decrease the sum.
	>>> largest_sum([2, -8, 3, -2, 4, -10])
	5
	"""
	largest = 0
	cur_sum = 0
	for i in range(len(arr)):
		# if the current value leads to negative sum, then skip it and start counting from the next value
		if arr[i] + cur_sum < 0:
			cur_sum = 0
			continue
		cur_sum += arr[i]
		# try updating the largest only when arr[i] is larger than 0
		if arr[i] > 0 and cur_sum > largest:
			largest = cur_sum

	return largest

if __name__ == "__main__":
	import doctest
	doctest.testmod()