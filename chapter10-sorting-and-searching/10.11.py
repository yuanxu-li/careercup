# 10.11 Peaks and Valleys: In an array of integers, a "peak" is an element 
# which is greater than or equal to the adjacent integers and a "valley" is
# an element which is less than or equal to the adjacent integers. For example,
# in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys.
# Given an array of integers, sort the array into an alternating sequence of
# peaks and valleys.

def peaks_and_valleys(arr):
	"""
	Firstly we sort the array into an ascending order. Then pick elements
	from the left half and the right half in turn. Since the left elements
	are smaller than or equal to the middle element while the right elements
	are larger than or equal to the middle element, this way we ensure that
	peaks and valleys are in alternating sequence.
	>>> peaks_and_valleys([5, 8, 6, 2, 3, 4, 6])
	[2, 8, 3, 6, 4, 6, 5]
	"""
	arr.sort()
	arr2 = []
	i = 0
	j = len(arr)-1
	while i < j:
		arr2.append(arr[i])
		arr2.append(arr[j])
		i += 1
		j -= 1
	if i == j:
		arr2.append(arr[i])
	return arr2

if __name__ == "__main__":
	import doctest
	doctest.testmod()