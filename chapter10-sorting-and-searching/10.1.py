# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B.
# Write a method to merge B into A in sorted order.

import pdb

def sort_merge(A, B, len_A):
	"""
	If we merge A and B into the back of A, we do not have to shift A.

	>>> A = [1, 3, 5, 6, 7, 8, 9, 11, 0, 0, 0, 0, 0]
	>>> B = [2, 4, 10]
	>>> sort_merge(A, B, 8)
	>>> A
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0]
	"""
	# merge A and B into the the back of A
	i = len_A - 1 # backward index of A
	j = len(B) - 1 # backward index of B
	k = len_A + len(B) - 1 # backward index of the new array
	while i >= 0 and j >= 0:
		if A[i] >= B[j]:
			A[k] = A[i]
			k -= 1
			i -= 1
		else:
			A[k] = B[j]
			k -= 1
			j -= 1
	while i >= 0:
		A[k] = A[i]
		i -= 1
		k -= 1
	while j >= 0:
		A[k] = B[j]
		j -= 1
		k -= 1

if __name__ == "__main__":
	import doctest
	doctest.testmod()