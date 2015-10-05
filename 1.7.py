# 1.7 Rotate Matrix: Given an image represented by an N*N matrix, where each pixel in the image is 4 bytes, write a method to rotate
# the image by 90 degrees. Can you do this in place?

def rotate_matrix(matrix):
	""" Take a matrix (list of lists), and rotate the matrix clockwise
	>>> rotate_matrix([[1,2,3],[4,5,6],[7,8,9]])
	[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
	>>> rotate_matrix([])
	[]
	"""
	length = len(matrix)

	# first, flip along the main diagonal
	for i in range(length):
		for j in range(i+1, length):
			# swap two elements
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	# second, flip left and right
	for i in range(length):
		for j in range(int(length/2)):
			# swap two elements
			matrix[i][j], matrix[i][length-1-j] = matrix[i][length-1-j], matrix[i][j]

	return matrix

def rotate_matrix_modified(matrix):
	""" Rotate a matrix with a layer-by-layer approach
	>>> rotate_matrix_modified([[1,2,3],[4,5,6],[7,8,9]])
	[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
	>>> rotate_matrix_modified([])
	[]
	"""
	length = len(matrix)

	for layer in range(int(length / 2)):
		for i in range(length - 1 - layer):
			# left, top, right, bottom <- bottom, left, top, right
			offset = layer + i
			matrix[length - 1 - offset][layer],\
			matrix[layer][offset],\
			matrix[offset][length - 1 - layer],\
			matrix[length - 1 - layer][length - 1 - offset]\
			=\
			matrix[length - 1 - layer][length - 1 - offset],\
			matrix[length - 1 - offset][layer],\
			matrix[layer][offset],\
			matrix[offset][length - 1 - layer]

	return matrix


def main():
	import doctest
	doctest.testmod()

if __name__ == "__main__":
	main()