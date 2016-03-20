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

def peaks_and_valleys_swap(arr):
	"""
	The idea is also to sort the array in the first place. Then we iterate through the array,
	jumping two elements and swapping them at a time. Since every three elements satisfy
	"small <= medium <= large", swapping them will make "medium >= small <= large", and medium
	becomes a peak and small becomes a valley
	>>> peaks_and_valleys_swap([5, 8, 6, 2, 3, 4, 6])
	[3, 2, 5, 4, 6, 6, 8]
	"""
	arr.sort()
	for i in range(1, len(arr), 2):
		arr[i], arr[i-1] = arr[i-1], arr[i]
	return arr

def peaks_and_valleys_optimal(arr):
	""" we do not have to sort the array at all. Note that as long as we put peaks in the right places,
	all valleys will be already in the right places. Then we iterate through the array, jumping
	two elements at a time, putting the largest element among the three in the middle to make a peak
	>>> peaks_and_valleys_optimal([5, 8, 6, 2, 3, 4, 6])
	[5, 8, 2, 6, 3, 6, 4]
	"""
	# if the length of array <= 2, it is naturally a sorted array
	if len(arr) <= 2:
		return arr
	for i in range(1, len(arr)-1, 2):
		# middle is max
		if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
			continue
		# left is max
		elif arr[i-1] >= arr[i] and arr[i-1] >= arr[i+1]:
			arr[i-1], arr[i] = arr[i], arr[i-1]
		# right is max
		else:
			arr[i+1], arr[i] = arr[i], arr[i+1]
	return arr



if __name__ == "__main__":
	import doctest
	doctest.testmod()