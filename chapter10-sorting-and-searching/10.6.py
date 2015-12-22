# 10.6 Sort Big File: Imagine you have a 20 GB file with one string per line. Explain how you would sort the file.

from collections import deque
import math
import pdb

def sort_large_array(arr, limit):
	"""
	We imitate this problem by limiting the size of an array we could use in memory, except the original array used to
	imitate the large file. The idea is that we split the array into arrays of largest possible size, sort each respectively,
	and merge them into the original array. Note that the method sorting each smaller array can be any possible sorting algorithm
	>>> import string
	>>> import random
	>>> arr = [''.join(random.choice(string.printable) for _ in range(random.randint(1, 10))) for _ in range(40)]
	>>> sort_large_array(arr, 10)
	>>> arr
	"""
	num_of_arrs = math.ceil(len(arr) / limit)
	arr_of_arrs = [deque(mystery_sort(arr[i*limit : (i+1)*limit])) for i in range(num_of_arrs)]
	# merge all sub-arrays into the original array
	i = 0
	while more_values(arr_of_arrs):
		arr[i] = min_value(arr_of_arrs)
		# pdb.set_trace()
		i += 1


		

def min_value(arr_of_arrs):
	"""
	>>> from collections import deque
	>>> min_value([deque(["2","4","5"]),deque(["3","6","9"]),deque(["5","6","7","9"]),deque([])])
	'2'
	"""
	# clear empty arrays
	i = 0
	while i < len(arr_of_arrs):
		if len(arr_of_arrs[i]) == 0:
			del arr_of_arrs[i]
		else:
			i += 1
	min_arr = min(arr_of_arrs, key=lambda arr: arr[0])

	return min_arr.popleft()

def more_values(arr_of_arrs):
	for arr in arr_of_arrs:
		if len(arr) > 0:
			return True
	return False


def mystery_sort(arr):
	return sorted(arr)

if __name__ == "__main__":
	import doctest
	doctest.testmod()