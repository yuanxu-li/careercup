# 10.5 Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a method to find
# the location of a given string.

def sparse_search(arr, x, first=None, last=None):
	"""
	with empty strings interspersed, it is a bit harder to apply binary search,
	since an empty mid element makes no sense for comparison. However, we can shift
	the mid index to find the closest mid non-empty element for comparison in order 
	to decide which half to go to.
	>>> sparse_search(["aab", "", "", "aabc", "", "abcc", "", "", "abcd", "", "acdf"], "abcd")
	8
	>>> sparse_search(["aab", "", "", "aabc", "", "abcc", "", "", "abcd", "", "acdf"], "abc")
	-1
	"""
	# alternative for initial call
	if first is None or last is None:
		first = 0
		last = len(arr) - 1

	# edge case
	if first > last:
		return -1
	mid = (first + last) // 2

	# first and last element can be emtpy strings, but gotta make sure
	# mid element is non-empty for comparison so that we can decide
	# which half to search
	if not arr[mid]:
		left = mid - 1
		right = mid + 1

		while True:
			if left < first and right > last:
				return -1
			elif arr[left] and first <= left:
				mid = left
				break
			elif arr[right] and right <= last:
				mid = right
				break
			left += 1
			right += 1

	# now that mid element is non-empty, compare it with searched element x
	if arr[mid] == x:
		return mid
	elif arr[mid] > x:
		return sparse_search(arr, x, first, mid-1)
	else:
		return sparse_search(arr, x, mid+1, last)





if __name__ == "__main__":
	import doctest
	doctest.testmod()