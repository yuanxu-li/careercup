# 10.4 Sorted Search, No size: You are given an array-like data structure Listy which lacks a size method. It does, however,
# have an elementAt(i) method that returns the element at index i in O(1) time. If i is beyond the bounds of the data structure,
# it returns -1. (For this reason, the data structure only supports positive integers.) Given a Listy which contains sorted,
# positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index.

def find_index(arr, x):
	"""
	The naive approach is O(n) by searching through the entire array.
	A better approach would be using binary search, but one problem remains:
	we do not know the array length.
	Therefore we split this problem into two steps:
	1. find the length n in O(logn) time, by increasing n from 1, to 2, 4, 8
	until element_at returns -1 which means it is out of bound
	2. apply binary search to this array in O(logn)
	>>> find_index([1,2,5,7,9,10], 9)
	4
	>>> find_index([1,2,5,7,9,10], 3)
	-1
	"""
	# find the length
	n = 1
	while element_at(arr, n) != -1:
		n *= 2

	# binary search
	low = 0
	high = n - 1
	while low <= high:
		mid = (low + high) // 2
		mid_value = element_at(arr, mid)
		if mid_value == x:
			return mid
		elif mid_value > x or mid_value == -1:
			high = mid - 1
		else:
			low = mid + 1
	return -1


def element_at(arr, i):
	if i in range(len(arr)):
		return arr[i]
	else:
		return -1

if __name__ == "__main__":
	import doctest
	doctest.testmod()