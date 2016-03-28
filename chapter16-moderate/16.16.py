# 16.16 Sub Sort: Given an array of integers, write a method to find inices m and n such
# that if you sorted elements m through n, the entire array would be sorted. Minimize n - m
# (that is, find the smallest such sequence).
# EXAMPLE
# Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
# Output: (3, 9)

import pdb

def sub_sort_brute_force(arr):
	"""
	In this method, we simply sort the array, and find the part of the sorted array where it is
	different from the original array.
	Time Complexity:
	1. sorting the array takes O(nlogn)
	2. searching from the beginning and end of the array takes O(n)
	>>> sub_sort_brute_force([1, 2, 3, 4, 5, 6, 7])
	(0, 0)
	>>> sub_sort_brute_force([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
	(3, 9)
	"""
	sorted_arr = sorted(arr)

	# search from the beginning to find m, where it starts to differ from the original array
	m = 0
	while m < len(arr):
		if sorted_arr[m] != arr[m]:
			break
		m += 1

	# if the sorted array is identical to the original array, which means the original array is already sorted
	if m == len(arr):
		return (0, 0)

	# search from the end to find n, where it starts to differ from the original array
	n = len(arr) - 1
	while n > m:
		if sorted_arr[n] != arr[n]:
			break
		n -= 1

	return (m, n)



if __name__ == "__main__":
	import doctest
	doctest.testmod()