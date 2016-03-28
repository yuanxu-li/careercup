# 16.19 Pond Sizes: You have an integer matrix representing a plot of land, where the value
# at that location represents the height above sea level. A value of zeros indicates water.
# A pond is a region of water connected vertically, horizontally, or diagonally. The size
# of the pond is the total number of connected water cells. Write a method to compute
# the sizes of all ponds in the matrix.
# EXAMPLE
# Input:
# 0 2 1 0
# 0 1 0 1
# 1 1 0 1
# 0 1 0 1
# Output: 2, 4, 1 (in any order)

from collections import defaultdict
import pdb

def pond_sizes(matrix):
	"""
	We employ DFS to search from non-marked cells to expand its area. By trying to
	use every cell as the starting point, we will be able to search the entire matrix.
	>>> pond_sizes([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]])
	[2, 4, 1]
	"""
	# change all non-zeros into None so that we can use numbers to indicate the index
	# of ponds. And the heights of land do not affect the result
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] != 0:
				matrix[i][j] = None

	# depth-first search to find all connected water cells to make up a pond
	pond_index = 1
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			# 0 means this cell is water and not yet marked
			if matrix[i][j] == 0:
				mark_pond(matrix, i, j, pond_index)
				pond_index += 1

	pond_sizes_dict = defaultdict(int)
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] is not None:
				pond_sizes_dict[matrix[i][j]] += 1   
	return list(pond_sizes_dict.values())

def mark_pond(matrix, i, j, pond_index):
	"""
	search from matrix[i][j] for all connected water cells, based on DFS, all to be marked
	as pond_index
	"""
	# pdb.set_trace()
	# if the indices are not in range or this cell is not a markable water cell, done with this cell
	if i not in range(len(matrix)) or j not in range(len(matrix[0])) or matrix[i][j] != 0:
		return
	# mark this cell
	matrix[i][j] = pond_index
	# search in eight directions
	mark_pond(matrix, i-1, j-1, pond_index)
	mark_pond(matrix, i-1, j, pond_index)
	mark_pond(matrix, i-1, j+1, pond_index)
	mark_pond(matrix, i, j-1, pond_index)
	mark_pond(matrix, i, j+1, pond_index)
	mark_pond(matrix, i+1, j-1, pond_index)
	mark_pond(matrix, i+1, j, pond_index)
	mark_pond(matrix, i+1, j+1, pond_index)
	return

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	

