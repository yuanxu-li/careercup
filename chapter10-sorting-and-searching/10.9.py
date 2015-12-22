# 10.9 Sorted Matrix Search: Given an M*N matrix in which each row and
# each column is sorted in ascending order, write a method to find
# an element

import pdb

def sorted_matrix_search(m, x, row_start=None, row_end=None, col_start=None, col_end=None):
	"""
	search through the diagonal and branch into different quarters based on
	the current element.
	>>> m = [[1, 4, 5, 11], [2, 5, 6, 12], [3, 9, 10, 19]]
	>>> sorted_matrix_search(m, 6)
	(1, 2)
	"""
	# alternative for initial call
	if row_start is None:
		row_start = 0
		row_end = len(m) - 1
		col_start = 0
		col_end = len(m[0]) - 1

	# pdb.set_trace()

	# out of bounds
	if row_start > row_end or col_start > col_end:
		return None
	# single row/column
	if row_start == row_end:
		return sorted_row_search(m, x, row_start, col_start, col_end)
	elif col_start == col_end:
		return sorted_col_search(m, x, col_start, row_start, row_end)

	# search through the diagonal until the diagonal element is larger than x
	for i, j in zip(range(row_start, row_end+1), range(col_start, col_end+1)):
		# now found
		if m[i][j] == x:
			return (i, j)
		# the previous diagonal element is less than x 
		# while this element is larger than x
		# then x is in the left down quarter or the right upper quarter
		elif m[i][j] > x:
			# left down quarter or right upper quarter
			return sorted_matrix_search(m, x, i, row_end, col_start, j-1) \
				or sorted_matrix_search(m, x, row_start, i-1, j, col_end)



def sorted_row_search(m, x, row, col_start, col_end):
	while col_start <= col_end:
		col_mid = (col_start + col_end) // 2
		if m[row][col_mid] == x:
			return (row, col_mid)
		elif m[row][col_mid] > x:
			col_start = col_mid + 1
		else:
			col_end = col_mid - 1
	return None



def sorted_col_search(m, x, col, row_start, row_end):
	while row_start <= row_end:
		row_mid = (row_start + row_end) // 2
		if m[row_mid][col] == x:
			return (row_mid, col)
		elif m[row_mid][col] > x:
			row_start = row_mid + 1
		else:
			row_end = row_mid - 1
	return None

if __name__ == "__main__":
	import doctest
	doctest.testmod()
