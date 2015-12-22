# 10.3 Search in Rotated Array: given a sorted array of a integers that has been rotated an unknown number
# of times, write code to find an element in the array. You may assume that the array was originally sorted
# in increasing order.

def search_array(array, e):
	""" by comparing the middle index with the leftmost and rightmost index respectively.
	If the leftmost index is less than the middle index, then the left side is in strictly increasing order
	If the rightmost index is larger than the middle index, then the right side is in strictly increasing order
	>>> search_array([4, 5, 6, 7, 8, 9, 0, 1, 2], 9)
	5
	>>> search_array([4, 5, 6, 7, 8, 9, 0, 1, 2], 4)
	0
	"""
	left = 0
	right = len(array) - 1


	while left <= right:
		mid = (left + right) // 2
		# base case
		if array[mid] == e:
			return mid
		# the left side is sorted
		if array[left] < array[mid]:
			# the element is in the left sorted side
			if array[left] <= e and e < array[mid]:
				right = mid - 1
			# the element is in the right unsorted side
			else:
				left = mid + 1
		# the right side is sorted
		else:
			# the element is in the right sorted side
			if array[mid] < e and e <= array[right]:
				left = mid + 1
			# the element is in the left unsorted side
			else:
				right = mid - 1


if __name__ == "__main__":
	import doctest
	doctest.testmod()