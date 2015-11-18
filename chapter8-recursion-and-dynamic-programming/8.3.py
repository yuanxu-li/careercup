# 8.3 Magic Index: A magic index in an array A[0...n-1] is defined to be an index such that
# A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index,
# if one exists, in array A
# FOLLOW UP
# What if the values are not distinct?



def magic_index_distinct_binary(array, start=None, end=None):
	""" Instead of linear search, we can actually do binary search, and decide which half to search according
	to the comparison of the current index and value
	>>> magic_index_distinct_binary([-1, 0, 2, 4, 5])
	2
	"""
	if start is None or end is None:
		start = 0
		end = len(array)-1
	if start > end:
		return None
	mid = int((start + end) / 2)
	if mid == array[mid]:
		return mid
	elif mid > array[mid]:
		return magic_index_distinct_binary(array, mid+1, end)
	else:
		return magic_index_distinct_binary(array, start, mid-1)



def magic_index_nondistinct(array):
	""" Since the values are not distinct, the comparison of the middle index and value assures us nothing.
	In this case, we have to do linear search, and literally loop over the entire array until we find a magic
	index.
	>>> magic_index_nondistinct([-1, 0, 2, 4, 5])
	2
	"""
	for index, value in enumerate(array):
		if index == value:
			return index
	return None

def magic_index_nondistinct_updated(array, start=None, end=None):
	""" It is actually possible to reduce the search space by comparing the middle index and value.
	>>> magic_index_nondistinct_updated([-1, 0, 2, 4, 5])
	2
	"""
	if start is None or end is None:
		start = 0
		end = len(array) - 1

	if start > end:
		return None
	mid = int((start + end) / 2)
	if mid == array[mid]:
		return mid
	# search left
	left = magic_index_nondistinct_updated(array, start, min(mid-1, array[mid]))
	if left is not None:
		return left
	# search right
	right = magic_index_nondistinct_updated(array, max(mid+1, array[mid]))
	if right is not None:
		return right
	# if nothing is found
	return None




if __name__ == "__main__":
	import doctest
	doctest.testmod()