# 10.3 Search in Rotated Array: given a sorted array of a integers that has been rotated an unknown number
# of times, write code to find an element in the array. You may assume that the array was originally sorted
# in increasing order.

def search_array(array, e):
	""" by comparing the middle index with the leftmost and rightmost index respectively.
	If the leftmost index is less than the middle index, then the left side is in strictly increasing order
	If the rightmost index is larger than the middle index, then the right side is in strictly increasing order.
	We determine which half the element is in by looking at the ordered half.
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
		elif array[right] > array[mid]:
			# the element is in the right sorted side
			if array[mid] < e and e <= array[right]:
				left = mid + 1
			# the element is in the left unsorted side
			else:
				right = mid - 1
		# cannot determine which side is sorted
		elif array[left] == array[mid]:
			# if left == mid but mid != right, left through mid are the same
			# since mid != x, there is no sense in searching this part
			if array[mid] != array[right]:
				left = mid + 1
			# if left == mid == right, still cannot decide which side
			# is sorted or identical, need more neighbors to help decide
			else:
				# let's search the left side to decide
				temp_left = left
				temp_mid = mid
				temp_right = right
				while temp_left < temp_mid:
					if array[temp_left] != array[temp_mid]:
						break
				if temp_left == temp_mid:
					left = mid + 1
				else:
					right = mid - 1




if __name__ == "__main__":
	import doctest
	doctest.testmod()