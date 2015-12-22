# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order.

import pdb

def sort_merge(A, len_A, B, len_B):
	"""
	move A rightward to leave space for B, and then merge the moved A and the original B into the array A used
	to occupy
	>>> A = [1, 3, 5, 6, 7, 8, 9, 11, 0, 0, 0, 0, 0]
	>>> B = [2, 4, 10]
	>>> sort_merge(A, 8, B, len(B))
	>>> A
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0]
	"""
	# move A rightward to leave space for B
	for i in range(len_A - 1, -1, -1):
		A[i + len_B] = A[i]
	# merge A and B into the array A used to occupy
	i = len_B	# start index of A
	j = 0 # start index of B
	k = 0 # start index of the new array
	while i < len_A + len_B and j < len_B:
		if A[i] >= B[j]:
			A[k] = B[j]
			k += 1
			j += 1
		else:
			A[k] = A[i]
			k += 1
			i += 1
	while i < len_A + len_B:
		A[k] = A[i]
		i += 1
		k += 1
	while j < len_B:
		A[k] = B[j]
		j += 1
		k += 1

if __name__ == "__main__":
	import doctest
	doctest.testmod()