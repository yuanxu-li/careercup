# 10.5 Sparse Search: Given a sorted array of strings that is interspersed with empty strings, write a method to find
# the location of a given string.

def sparse_search(arr, x):
	"""
	Since the array is interspersed with empty strings, we need another variable to keep track of the indices, called ind.
	Each time we loop over a non-empty string, we add ind by 1
	>>> sparse_search(["aab", "", "", "aabc", "", "abcc", "", "", "abcd", "", "acdf"], "abcd")
	3
	>>> sparse_search(["aab", "", "", "aabc", "", "abcc", "", "", "abcd", "", "acdf"], "abc")
	-1
	"""
	ind = 0
	for i in range(len(arr)):
		# find it
		if arr[i] == x:
			return ind
		# the current element is already larger than the searched element
		elif arr[i] > x:
			return -1
		elif arr[i]:
			ind += 1
	return -1

if __name__ == "__main__":
	import doctest
	doctest.testmod()