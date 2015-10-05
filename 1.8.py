# 1.8 Zero Matrix: Write an algorithm such that if an element in an M*N matrix is 0, its entire row and column are set to 0.

def zero_matrix(matrix):
	""" For matrix, if an element is 0, set its entire row and column to 0
	>>> zero_matrix([[1,2,0,0],[5,6,7,8],[9,0,11,12]])
	[[0, 0, 0, 0], [5, 0, 0, 0], [0, 0, 0, 0]]
	>>> zero_matrix([])
	[]
	"""
	# return empty matrix directly
	if len(matrix) == 0:
		return matrix
	row_indices = set()
	column_indices = set()
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				row_indices.add(i)
				column_indices.add(j)

	for i in row_indices:
		for j in range(len(matrix[0])):
			matrix[i][j] = 0

	for i in range(len(matrix)):
		for j in column_indices:
			matrix[i][j] = 0
	
	return matrix

def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()