# 10.4 Sorted Search, No size: You are given an array-like data structure Listy which lacks a size method. It does, however,
# have an elementAt(i) method that returns the element at index i in O(1) time. If i is beyond the bounds of the data structure,
# it returns -1. (For this reason, the data structure only supports positive integers.) Given a Listy which contains sorted,
# positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index.

def find_index(arr, x):
	"""
	>>> find_index([1,2,5,7,9,10], 9)
	4
	>>> find_index([1,2,5,7,9,10], 3)
	-1
	"""
	i = 0
	while True:
		e = element_at(arr, i)
		# find it
		if e == x:
			return i
		# out of bound or the current element is larger than the searched element
		elif e == -1 or e > x:
			return -1
		# continue
		else:
			i += 1

def element_at(arr, i):
	if i in range(len(arr)):
		return arr[i]
	else:
		return -1

if __name__ == "__main__":
	import doctest
	doctest.testmod()